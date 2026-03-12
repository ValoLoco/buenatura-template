# Skill: knowledge-search

**Type:** Tool invocation  
**Executable:** `tools/knowledge_search.py`  
**When to use:** Before any task that requires retrieving facts, context, or prior decisions from the KNOWLEDGE/ corpus. Use instead of loading full files.

---

## Invocation

```bash
python tools/knowledge_search.py "<natural language query>" --top-k 5
```

Returns the top-K most semantically relevant chunks from indexed KNOWLEDGE/ files with source path and relevance score.

---

## Rules

1. Run this before loading any KNOWLEDGE/ file directly. If results are sufficient, do not load the full file.
2. Use top-3 results for focused tasks. Use top-5 for broad synthesis tasks.
3. If no results are returned, fall back to direct file load and flag that the index may need a rebuild.
4. Never inject more than top-5 chunks into a single prompt context. Score threshold: discard results below 0.50.
5. Cite the source path in your response when using retrieved content.

---

## Prerequisites

- `infra/bootstrap.sh` must have been run once on this machine.
- `sentence-transformers` and `sqlite-vec` must be installed.
- KNOWLEDGE/ must contain at least one `.md` file.

---

## Index Behaviour

- Index rebuilds incrementally. Only changed files are re-embedded.
- Index lives at `KNOWLEDGE/.index/knowledge.db` (git-ignored).
- Manifest at `KNOWLEDGE/.index/index_manifest.json` tracks file hashes.
