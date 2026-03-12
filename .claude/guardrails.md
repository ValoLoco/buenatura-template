# 5 Validation Gates

All 5 gates must pass before any output is delivered.
Fail any gate: identify the specific failure, then load `workflows/iteration-loop.md`.

---

## Gate 1: Principle Compliance

Does the output respect all active principles?
Core principles (always active) live in `.claude/principles-core.md`.
Extended principles (agent design, system-level tasks) live in `.claude/principles-extended.md`.

Core principles to verify (always active):
- Principle 1 Carbon Fiber: nothing without purpose.
- Principle 2 YAGNI: no speculative complexity.
- Principle 3 AI-First: comprehensible in one context window.
- Principle 4 Uncle Bob: one function, one job, self-documenting.
- Principle 5 No Em Dashes: banned in all output without exception.

Extended principles to verify (agent design and system-level tasks):
- Principle 6 One Source of Truth: no duplicated state or config.
- Principle 7 Explicit Over Implicit: all assumptions written down.
- Principle 8 Reversibility First: recovery path confirmed before irreversible action.
- Principle 9 Fail Loudly: no silent failures or guessed outputs.
- Principle 10 Context Window Hygiene: every file actionable in isolation.
- Principle 11 Idempotency: every write is safe to repeat.
- Principle 12 Minimal Footprint: only required permissions and files accessed.
- Principle 13 Observability: every action leaves a trace.

Pass: all active principles upheld.
Fail: identify which principle number is violated and why.

---

## Gate 2: Output Quality

This gate applies differently depending on output type.

**For code output:**
- Syntax valid. Types correct.
- Tests present for non-trivial logic.
- No obvious performance or security vulnerabilities.

**For non-code output (content, strategy, research, agent design):**
- Structure is logical and complete.
- Claims are cited or explicitly flagged as assumptions.
- No contradictions with prior decisions or context files.
- Format matches the expected output template if one exists.

Pass: output type criteria met.
Fail: identify which criterion failed with a specific example.

---

## Gate 3: Resource Efficiency and Minimal Footprint

API calls, compute, time, and cost within agreed budget.
No unnecessary loops, redundant operations, or duplicated content.
Agent accessed only the files and permissions the routing table specified.
Write operations are safe to repeat without duplicating side effects.

Pass: no waste, no scope overreach, no non-idempotent writes identified.
Fail: name the specific inefficiency or overreach.

---

## Gate 4: Safety, Security, and Reversibility

No destructive operations without explicit human confirmation.
Data privacy respected. All operations reversible or explicitly flagged as irreversible.
If irreversible: use the confirmation template below before execution.
No silent failures: ambiguities and errors surfaced immediately.

### Irreversible Action Confirmation Template

Before executing any irreversible action (send, delete, publish, deploy, overwrite without backup), produce this block and halt until human confirms:

```
IRREVERSIBLE ACTION CONFIRMATION REQUIRED
Action: [exact description of what will happen]
Target: [file, endpoint, recipient, or system affected]
Cannot be undone because: [specific reason]
Recovery path: [backup location, rollback method, or NONE]
To proceed: reply CONFIRM
To cancel: reply CANCEL or take no action
```

Do not execute the action until CONFIRM is received. Do not assume confirmation.

Pass: no safety, privacy, or silent-failure concern, or confirmation received.
Fail: STOP immediately. Do not revise and retry. Escalate to human.

---

## Gate 5: Business Alignment and Observability

Output serves the stated goal. ROI-positive. Stakeholder needs addressed.
No scope creep beyond the defined task.
A trace exists: routing decision logged, files loaded noted, output path recorded.
Update the session log (`MEMORY/session-log-YYYY-MM-DD.md`) when this action is significant.

A significant action is one that meets any of these criteria:
- It produces a file that will be used as input to a subsequent task.
- It makes an irreversible or hard-to-reverse change (publish, delete, send, overwrite).
- It represents a phase gate decision in a DMAIC or project lifecycle.
- It results in an escalation to human review.

### Standing Audit Rules (run after any directory restructure or new file creation)

These two checks must pass after every restructure, rename, or new directory/file addition:

**Rule A — Path Integrity Audit:**
For every new or renamed path, search all template files for references to the old or expected path.
Verify each reference points to a location that exists on disk.
A reference that points to a non-existent path is a High-severity defect (S=8, RPN >= 576). Fix before closing the cycle.
Files most likely to drift: `README.md`, `CLAUDE.md`, any agent `.md`, `framework-relationships.md`, `routing-table.md`.

**Rule B — Cross-File Coupling Audit:**
For every new structured output format introduced (a new block, table, or schema), identify the file that consumes it.
Verify the consuming file has explicit instructions for how to read and act on that format.
A structured output with no consumption spec is a Medium-severity defect (S=7, RPN >= 392). Fix before closing the cycle.
Pairs to verify: evaluator handoff block consumed by iteration-loop; FMEA table consumed by dmaic-recursive; control plan consumed by project-execution; SIPOC consumed by dmaic-recursive.

Pass: both rules pass, or all failures are logged with fix targets.
Fail: log each failing path or coupling gap as a named defect. Assign RPN. Add to next DMAIC cycle.

---

All gates pass: proceed to `.claude/evaluator.md`.
Any gate fails: load `workflows/iteration-loop.md` with specific failure note.
Gate 4 failure: escalate immediately. Do not loop.
