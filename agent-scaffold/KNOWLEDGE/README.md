# Agent Knowledge Base

This directory stores persistent reference material for agents operating in this project.
It is the first place agents check before searching externally (per `skills/research-workflow.md` Step 2).

---

## What Goes Here

- Domain reference documents: frameworks, standards, specifications.
- Verified research outputs promoted from `output/final/` after multiple uses.
- Glossaries, taxonomy files, or definitions the project uses repeatedly.
- Any document an agent would otherwise re-fetch or re-synthesise on each task.

## What Does NOT Go Here

- Draft or unverified content (use `output/` for those).
- Session logs (use `MEMORY/session-log-YYYY-MM-DD.md`).
- Decisions or project state (use `MEMORY/context.md`).
- Files specific to one task (they stay in `output/` until promoted).

---

## Promoting a File to KNOWLEDGE

A file is ready to promote when:
- It has been used as a reference in at least 2 separate tasks.
- It has passed the evaluator at >= 0.85 in its original output context.
- It is domain knowledge, not project state.

Promotion step: copy from `output/final/` to `KNOWLEDGE/`, rename to remove the date prefix if the content is evergreen, and add a row to the index table below.

---

## Index

| File | Topic | Source | Promoted Date |
|------|-------|--------|---------------|
| [filename] | [what it covers] | [original output or external source] | [YYYY-MM-DD] |

This directory starts empty. Add files as the project accumulates verified knowledge.
