---
name: principles-extended
description: Principles 6-13 for agent design, complex multi-phase tasks, and system-level work. Load in addition to principles-core.md.
---

# Principles: Extended

Load this in addition to `principles-core.md` for: agent design, complex projects, system-level tasks, and any task that writes, deletes, or publishes state.

---

## 6. One Source of Truth

Every fact, configuration value, or decision lives in exactly one place.
Never duplicate state across files, configs, or prompts.
If two files could contradict each other, one must be removed or explicitly deferred to the other.

- Code: single config files, no repeated constants.
- Content: one canonical version. No simultaneous draft and final in two folders.
- Agent instructions: routing-table.md is the single source. No inline routing logic elsewhere.

## 7. Explicit Over Implicit

State your assumptions. Never rely on a reader (human or AI) to infer context that should be written down.

- Code: function signatures document intent, not just inputs.
- Instructions: if a step has a precondition, state it before the step.
- Agent design: every routing decision must reference a named rule, not an inferred guess.

If you catch yourself thinking they will figure it out: write it down instead.

## 8. Reversibility First

Before any irreversible action (deleting, publishing, overwriting, sending), confirm or create a recovery path.
Default to reversible steps. Escalate if no recovery path exists.

- Code: destructive operations require explicit confirmation gates.
- Content: drafts go to `output/` before moving to `output/final/`. Nothing skips staging.
- Agents: if an action cannot be undone, flag it for human review before executing.

When in doubt: stage, do not commit.

## 9. Fail Loudly, Not Silently

When something is wrong, broken, or ambiguous: say so immediately and specifically.
Never produce partial output that looks complete. Never guess when you should ask.

- Code: throw explicit errors with clear messages. No silent null returns.
- Agents: if routing match is ambiguous, stop and ask. Do not pick the closest guess.
- Content: if a brief is incomplete, flag the missing field. Do not fill with assumptions.

A silent failure is worse than a loud one. It compounds before anyone notices.

## 10. Context Window Hygiene

Every file assumes it may be the only file loaded.
Include enough context to be actionable in isolation.
Remove context that only makes sense when other files are already loaded.

- Instructions: each skill or workflow file must state its own preconditions.
- Agent design: no file depends on another unless that dependency is explicit in the routing table.
- Content: no references that break when a section is skimmed or reordered.

If a file cannot stand alone: it is incomplete, not modular.

## 11. Idempotency

Every write action must be safe to repeat.
Before executing any state-changing operation, check whether it has already been performed.

- Code: no action without a uniqueness check on writes.
- Agents: if a step fails mid-execution, the retry must not duplicate the side effect.
- Files: writing to `output/` must overwrite, not append, to avoid duplicate content.

If you cannot make an action idempotent: isolate the commit step and flag it as a one-shot gate requiring human confirmation.

## 12. Minimal Footprint

Request only the permissions, access, and resources required for the current task.
Do not accumulate scope. Release resources as soon as the task is done.

- Agents: scope credentials and tool access to the task at hand.
- Files: read only the files the routing table specifies.
- Code: do not open connections or load configs the current function does not use.

The agent that does less, unexpectedly, is safer than the one that does more.

## 13. Observability

Every significant action must leave a trace: what was decided, why, and what the result was.

- Agents: log the routing decision, files loaded, and final output path for every task.
- Code: instrument state transitions, not just errors.
- Content: the output filename and datestamp are the minimum audit trail.

If an action cannot be explained from its trace alone: the trace is incomplete.
