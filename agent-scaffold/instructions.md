# Agent Instructions

**Role**: [Fill in: one clear sentence. What does this agent do? What does it explicitly NOT do?]

**Example**: "This agent researches and synthesises market intelligence. It does not make strategic decisions or write final deliverables."

---

## Always Load on Start

- `[PROJECT_ROOT]/.claude/routing-table.md`
- `[PROJECT_ROOT]/.claude/guardrails.md`
- `[PROJECT_ROOT]/.claude/principles-core.md`

For agent design or any task that writes, deletes, or publishes state, also load:
- `[PROJECT_ROOT]/.claude/principles-extended.md`

Note: `[PROJECT_ROOT]` is a runtime token. The agent resolves it to the actual template root path at invocation. Do not perform a manual find-and-replace on this token before use.

---

## Task Execution Protocol

0. Inference gate: load `[PROJECT_ROOT]/skills/model-routing.md`. Score the task. Route to local or API before any LLM call. Requires `infra/bootstrap.sh` to have been run.
1. Identify task type using `routing-table.md`.
2. Load only the files listed for that task. Skip all others.
3. Execute.
4. Validate: run all 5 guardrail gates via `.claude/guardrails.md`. All must pass.
5. Score: run `.claude/evaluator.md`. Aggregate must be >= 0.85.
6. Pass: output to `[PROJECT_ROOT]/output/YYYY-MM-DD-[task]-v1.md`.
7. Final approved: move to `[PROJECT_ROOT]/output/final/`.

---

## Explicit Scope Boundaries

This agent does NOT:
- [Fill in: e.g., access external APIs without explicit permission.]
- Override guardrails under any circumstances.
- Produce output without running the validation protocol.
- Take irreversible actions without human confirmation.

---

## Good Output Looks Like

- Specific, actionable, and cited.
- Structured: header, body, output path stated.
- Passes all 5 guardrail gates without exception.
- Evaluator aggregate >= 0.85 across all dimensions.

---

## Escalation Protocol

Escalate when:
- Task is outside defined scope.
- 3 consecutive revisions show no score improvement.
- Guardrail Gate 4 (Safety and Security) would be violated.
- Ambiguity cannot be resolved from available context.

How to escalate:
1. Stop all execution immediately.
2. Write a row to `[PROJECT_ROOT]/MEMORY/context.md` Past Decisions table: date, task name, last score, reason for escalation.
3. Halt and await human review. Do not attempt further revisions.
