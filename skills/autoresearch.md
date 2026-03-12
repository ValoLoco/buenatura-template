---
name: autoresearch
description: Autonomous AI experiment loop that iterates on a single file, runs timed evaluations, logs results, and advances only on improvement.
---

# autoresearch

Autonomous AI research loop. Agent iterates on a single experiment file,
runs timed evaluations, logs results, and advances only on improvement.
Inspired by karpathy/autoresearch. Adapted for local BitNet inference.

## When to Load

Load when the task is: run autonomous model experiments overnight or iteratively
without human supervision. Do not load for single-shot inference tasks.

## Setup

Work with the user to:

1. **Agree on a run tag** — propose based on today's date (e.g. `mar11`).
   Branch `autoresearch/<tag>` must not exist yet.
2. **Create the branch** — `git checkout -b autoresearch/<tag>` from main.
3. **Read in-scope files** — before touching anything, read:
   - `experiment.py` — the only file you modify (model config, eval params, loop)
   - `harness.py` — fixed eval harness, read-only, do not modify
   - `README.md` — repo context
   - `KNOWLEDGE/` — read up to 5 files or 2000 tokens total. Summarize remaining files by filename only.
   - `MEMORY/context.md` — if it exists
4. **Verify runtime** — confirm BitNet model exists at path in `$BITNET_MODEL`
   or the default path in `harness.py`. If not, tell the human and stop.
5. **Generate eval prompts** — create `eval_prompts.jsonl` (untracked) from:
   - The user's stated goal for this run
   - Key tasks, claims, or decisions found in `KNOWLEDGE/` and `MEMORY/context.md`
   - Minimum 10 prompts. Each line: `{"prompt": "...", "expected": "..."}`
   - Use `eval_prompts.jsonl.example` for format reference.
   - Do not reuse generic trivia. Every prompt must be domain-relevant.
6. **Init results log** — create `results.tsv` (untracked) with header row only:
   `commit\tval_score\tstatus\tdescription`
7. **Confirm and go.**

## Experiment Loop

Each experiment runs for a **fixed time budget** (default: 5 minutes wall clock).
Launch with: `python harness.py > run.log 2>&1`

**You CAN modify:**
- `experiment.py` — model config, prompts, hyperparams, eval logic, anything

**You CANNOT modify:**
- `harness.py` — fixed evaluation, timing, and metric extraction
- `eval_prompts.jsonl` — fixed for the duration of a run tag. Changing it invalidates comparisons.
- Install new packages outside `pyproject.toml` / `requirements.txt`

**Goal: minimize `val_score`** (or maximize, depending on harness definition.
Read `harness.py` header for the direction.)

**Simplicity criterion:** A small gain that adds complexity is not worth it.
Equal result with simpler code is a win. Always weigh complexity cost.

## Output Format

The harness prints a summary block:

```
---
val_score:        0.9979
run_seconds:      300.1
peak_memory_mb:   1240.0
num_steps:        953
```

Extract the key metric: `grep "^val_score:" run.log`

## Logging Results

Log every experiment to `results.tsv` (tab-separated, NOT comma-separated):

```
commit	val_score	status	description
a1b2c3d	0.9979	keep	baseline
b2c3d4e	0.9932	keep	lower temp to 0.3
c3d4e5f	1.0050	discard	increase context window (OOM)
```

Status values: `keep` | `discard` | `crash`

## Decision Rules

- **Improved**: advance branch, keep commit
- **Equal or worse**: `git reset` to previous commit
- **Crash**: log status `crash`, attempt one fix, skip if broken at idea level
- **Timeout** (>10 min): kill, treat as crash

## Autonomy Rules

Once the loop starts, do NOT pause to ask the human anything.
Do NOT ask "should I continue?". Run until manually interrupted.
If stuck for ideas: re-read `harness.py`, revisit near-misses, try combining
two previously discarded changes, or simplify something that already works.

**NEVER STOP.**

## Handoffs

- If experiment scope expands beyond a single file: stop, flag to human, route to `@project`.
- If a domain knowledge gap blocks prompt generation: route to `@researcher` with the specific gap.
- Log all handoffs to `MEMORY/context.md` Past Decisions table before stopping.

## BitNet Runtime Notes

- Default binary path: `$BITNET_BIN` (set in env or `.env` file)
- Default model: `$BITNET_MODEL` (1-bit quantized `.gguf` or BitNet native format)
- CPU threads: `$BITNET_THREADS` (default: all available)
- If BitNet binary not found, fall back to `llama.cpp` with `-ngl 0` (CPU only)
- Log memory with: `grep "^peak_memory_mb:" run.log`

## Output

- `eval_prompts.jsonl` — generated at setup, untracked, fixed for run duration
- `results.tsv` — untracked experiment log in scaffold root
- `run.log` — last experiment stdout/stderr (untracked, overwritten each run)
