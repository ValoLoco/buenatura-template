"""knowledge_search: semantic search across KNOWLEDGE/ corpus.

Usage:
    python tools/knowledge_search.py "your query" --top-k 5

Returns ranked chunks with source file and relevance score.
Rebuild index automatically when KNOWLEDGE/ files change.

Dependencies (installed by bootstrap.sh):
    pip install sentence-transformers sqlite-vec
"""
import argparse
import hashlib
import json
import textwrap
import sqlite3
from pathlib import Path

import sqlite_vec
from sentence_transformers import SentenceTransformer

KNOWLEDGE_DIR = Path("KNOWLEDGE")
INDEX_DIR = KNOWLEDGE_DIR / ".index"
DB_PATH = INDEX_DIR / "knowledge.db"
MANIFEST_PATH = INDEX_DIR / "index_manifest.json"
CHUNK_SIZE = 400  # words
OVERLAP = 50      # words
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # 80MB, offline-capable
EMBEDDING_DIM = 384


def chunk_text(text: str) -> list[str]:
    words = text.split()
    return [
        " ".join(words[i : i + CHUNK_SIZE])
        for i in range(0, len(words), CHUNK_SIZE - OVERLAP)
        if words[i : i + CHUNK_SIZE]
    ]


def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def get_connection() -> sqlite3.Connection:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    return conn


def init_tables(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            text   TEXT NOT NULL
        )
    """)
    conn.execute(f"""
        CREATE VIRTUAL TABLE IF NOT EXISTS chunk_vecs
        USING vec0(embedding FLOAT[{EMBEDDING_DIM}])
    """)
    conn.commit()


def build_index(model: SentenceTransformer, conn: sqlite3.Connection) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text()) if MANIFEST_PATH.exists() else {}
    changed = False

    for md_file in sorted(KNOWLEDGE_DIR.glob("*.md")):
        fhash = file_hash(md_file)
        if manifest.get(str(md_file)) == fhash:
            continue

        chunks = chunk_text(md_file.read_text(encoding="utf-8"))
        if not chunks:
            continue

        embeddings = model.encode(chunks, show_progress_bar=False, normalize_embeddings=True)

        # Remove stale entries for this file
        stale_ids = conn.execute(
            "SELECT id FROM chunks WHERE source = ?", (str(md_file),)
        ).fetchall()
        if stale_ids:
            ids = [r[0] for r in stale_ids]
            conn.execute(f"DELETE FROM chunk_vecs WHERE rowid IN ({','.join('?'*len(ids))})", ids)
            conn.execute("DELETE FROM chunks WHERE source = ?", (str(md_file),))

        for chunk, emb in zip(chunks, embeddings):
            conn.execute("INSERT INTO chunks(source, text) VALUES (?, ?)", (str(md_file), chunk))
            rowid = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
            conn.execute(
                "INSERT INTO chunk_vecs(rowid, embedding) VALUES (?, ?)",
                (rowid, emb.tobytes()),
            )

        manifest[str(md_file)] = fhash
        changed = True
        print(f"[index] indexed {len(chunks)} chunks from {md_file.name}")

    if changed:
        conn.commit()
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
    else:
        print("[index] all files up to date")


def search(query: str, top_k: int = 5) -> list[dict]:
    model = SentenceTransformer(MODEL_NAME)
    conn = get_connection()
    init_tables(conn)
    build_index(model, conn)

    q_emb = model.encode([query], normalize_embeddings=True)[0]

    rows = conn.execute(
        """
        SELECT c.source, c.text, cv.distance
        FROM chunk_vecs cv
        JOIN chunks c ON c.id = cv.rowid
        WHERE cv.embedding MATCH ?
          AND k = ?
        ORDER BY cv.distance
        """,
        (q_emb.tobytes(), top_k),
    ).fetchall()
    conn.close()

    return [
        {"source": r[0], "text": r[1], "score": round(1 - r[2], 4)}
        for r in rows
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Semantic search over KNOWLEDGE/")
    parser.add_argument("query", help="Natural language query")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results")
    args = parser.parse_args()

    results = search(args.query, args.top_k)
    if not results:
        print("No results found. Run bootstrap.sh and ensure KNOWLEDGE/ has .md files.")
    for i, r in enumerate(results, 1):
        print(f"\n[{i}] score={r['score']} | {r['source']}")
        print(textwrap.fill(r["text"], width=90))
