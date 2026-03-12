# Session Log Template

This file is the implementation of Principle 13 (Observability).

At the start of any significant session:
1. Copy this file to `MEMORY/session-log-YYYY-MM-DD.md` (replace date with today's date).
2. If a log for today already exists, append to it rather than overwriting.
3. Update the log throughout the session. Save before closing.

---

## Session Metadata

- Date: YYYY-MM-DD
- Agent: [which agent or CLAUDE.md direct]
- Project: [project name or ad hoc]
- Session goal: [one sentence: what was this session trying to accomplish?]

---

## Routing Log

Record every routing decision made during this session.

| Time | Task | Framework / Workflow Loaded | Files Loaded | Rationale |
|------|------|-----------------------------|--------------|----------|
| HH:MM | [task description] | [framework name] | [file list] | [why this route] |

---

## Actions Log

Record every significant action: file created, file updated, decision made, output produced.

| Time | Action | Input | Output Path | Reversible? |
|------|--------|-------|-------------|-------------|
| HH:MM | [created / updated / decided / escalated] | [brief input description] | [output/YYYY-MM-DD-task-v1.md or N/A] | Yes / No |

---

## Quality Gate Results

For each output produced this session, record the gate and evaluator results.

| Output | G1 | G2 | G3 | G4 | G5 | Aggregate | Verdict |
|--------|----|----|----|----|----|-----------|---------|
| [output filename] | P/F | P/F | P/F | P/F | P/F | [0.00] | SHIP / REVISE / STOP |

---

## Self-Extension Flags

Record any gaps, missing skills, broken references, or improvement opportunities noticed during this session.
These become inputs to the next DMAIC cycle.

| Type | Location | Description | Proposed Fix | Priority |
|------|----------|-------------|--------------|----------|
| Missing skill | [file path] | [what is absent] | [proposed file or change] | High / Med / Low |
| Broken reference | [file path] | [what points to what incorrectly] | [correction] | High / Med / Low |
| Process gap | [workflow] | [what step is unclear or missing] | [proposed improvement] | High / Med / Low |
| Principle violation | [file path] | [which principle, how violated] | [fix] | High / Med / Low |

---

## Session Close

- [ ] Routing log complete.
- [ ] Actions log complete.
- [ ] Quality gate results recorded.
- [ ] Self-extension flags written (or confirmed none found).
- [ ] If any Self-Extension Flag is marked High priority: trigger `.claude/self-extension-protocol.md` before closing.
- [ ] Active Projects table in `MEMORY/context.md` updated.
- [ ] Lessons Learned in `MEMORY/context.md` updated if a lesson was learned.
- [ ] This log saved to `MEMORY/session-log-YYYY-MM-DD.md`.

Session status: [COMPLETE / IN PROGRESS / ESCALATED]
