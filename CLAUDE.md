# AI Router: Progressive Disclosure Context Manager

Your role: Read this file first. Route to exactly the files you need. Skip everything else.
This file contains only pointers. No content lives here.

---

## Global Rules (Always Active)

1. All 5 core principles in `.claude/principles-core.md` are active for every task. Load that file now.
2. For agent design, system-level tasks, or any task that writes, deletes, or publishes state: also load `.claude/principles-extended.md` (Principles 6-13).
3. Naming convention: `YYYY-MM-DD-task-description-vN.md`, kebab-case folders.
4. All work-in-progress output goes to `output/`.
5. All final approved output goes to `output/final/`.
6. When any infrastructure file changes (skills, agents, workflows, routing): update `.claude/routing-table.md` in the same session. `CLAUDE.md` only needs updating when a new top-level section or global rule changes. Do not defer either update past the current session.

---

## Step 0: Inference Gate (Before Every LLM Call)

Load `skills/model-routing.md`. Score the task on 4 dimensions. Route to local or API.
Do not make any LLM call before this step is complete.
Requires `infra/bootstrap.sh` to have been run once on this machine.

---

## Step 1: Identify Your Task Type

Open `.claude/routing-table.md`.
Find your task row. Load only the files listed. Skip all others.

If no row matches your task: load `.claude/skills-protocol.md`. Do not guess a route.

---

## Step 2: Execute

Follow the loaded workflow or skill file instructions precisely.

---

## Step 3: Validate Before Delivery

1. Load `.claude/guardrails.md`. All 5 gates must pass.
2. Load `.claude/evaluator.md`. Aggregate score must be >= 0.85.
3. If either fails: load `workflows/iteration-loop.md` and revise.
4. On pass: move output to `output/final/YYYY-MM-DD-task-final.md`.

---

## Skills Protocol

No fitting internal skill? Load `.claude/skills-protocol.md`.
Search https://skills.sh before building anything bespoke.

---

## Escalation

After 3 revisions without improvement: stop and flag for human review.
Write escalation row to `agent-scaffold/MEMORY/context.md` Past Decisions table. Halt.

---

## LLM Wiki Workflow

Knowledge lives in `KNOWLEDGE/`. Three layers: `raw/` (immutable sources), `wiki/` (LLM-maintained pages), plus `index.md` and `log.md`. Read `KNOWLEDGE/index.md` first on any knowledge task.

**Ingest** — When a source file appears in `raw/`:
1. Read the source.
2. Write or update a summary page in `wiki/`.
3. Update up to 10-15 existing wiki pages where the source adds context, contradicts, or extends prior knowledge.
4. Add source to `index.md` under the correct category with a one-line summary.
5. Append an entry to `log.md`: `## [YYYY-MM-DD] ingest | Source Title`

**Query** — When answering a question against the wiki:
1. Read `index.md` to find relevant pages.
2. Load those pages. Synthesize an answer with inline citations to wiki page links.
3. If the answer is non-trivial (comparison, analysis, synthesis), file it back as a new wiki page and add it to `index.md`.
4. Append to `log.md`: `## [YYYY-MM-DD] query | Question summary`

**Lint** — Periodically or on request:
1. Check for: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts mentioned but lacking their own page, missing cross-references.
2. Fix issues in-place. Do not create new pages just to resolve lint — update existing pages.
3. Append to `log.md`: `## [YYYY-MM-DD] lint | scope or trigger`

**Rules:**
- `raw/` is immutable. Never edit files there.
- Prefer one source per ingest session. Stay in the loop.
- Index and log are updated on every operation, without exception.
- This workflow is tool-agnostic. Any LLM that can read and write markdown files can execute it.
