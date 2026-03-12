# Iteration Loop: Evaluate, Ship, or Revise

Use this after any work phase to drive output to delivery quality.
This loop enforces the quality gate. Nothing ships without passing it.

---

## The Loop

```
Execute task
    |
    v
Run Guardrails (.claude/guardrails.md)
    |
    +-- Any gate fails? Revise with specific feedback. Increment version. Loop.
    |
    v
Score with Evaluator (.claude/evaluator.md)
    |
    +-- Score < 0.85? Revise with specific feedback. Increment version. Loop.
    |
    v
SHIP: move to output/final/YYYY-MM-DD-task-final.md
```

---

## Consuming a Handoff Block

When arriving from `evaluator.md` with a structured handoff block, process it in this order:

1. Read `Specific defects` first. Each line is one targeted fix. Do not start revising until all defects are listed.
2. Read `Failed dimensions` and `Failed gates`. These confirm which evaluator and guardrail criteria to re-run after revision.
3. Read `Revision instruction`. This is the mandatory change. Execute it exactly as stated.
4. Ignore dimensions and gates that passed. Do not touch sections that are not identified as defective.
5. Increment the version number in the filename before writing the revised output.
6. After revision: re-run only the failed gates and failed dimensions. If all pass, proceed to ship.

If no handoff block is present: run the full guardrails and evaluator sequence from scratch.

---

## Rules

- Increment version on every revision: v1, v2, v3.
- Maximum 10 iterations total.
- If 3 consecutive revisions show no score improvement: ESCALATE to human review. Stop looping.
- Each revision must address specific identified defects. No generic rewrites.

---

## Revision Prioritisation

When multiple defects exist, fix in this order:

1. Gate 4 violations (Safety and Security). Always first.
2. Highest RPN items. RPN = Severity x Occurrence x Detection. Full scale in `skills/fmea.md`.
3. Correctness failures.
4. Completeness gaps.
5. Clarity and efficiency last.

---

## When to Escalate to DMAIC

The Iteration Loop handles single-output quality. DMAIC handles recurring process defects.

Open a DMAIC cycle when:

- The same defect class appears in 3 or more separate outputs across different tasks.
- A guardrail gate fails repeatedly on the same gate (e.g., Gate 2 fails on every content output).
- The root cause of a revision failure is systemic (a broken workflow, a missing skill, a bad instruction) rather than specific to one output.
- Escalation to human review happens more than twice in a month on the same issue type.

In those cases: stop the loop. Open `workflows/dmaic-recursive.md` at Phase 1 (Define).
The defect pattern becomes the problem statement.

---

## Output Naming

| Stage | Location | Filename |
|-------|----------|----------|
| Draft | `output/` | `YYYY-MM-DD-task-v1.md` |
| Revision | `output/` | `YYYY-MM-DD-task-v2.md` |
| Final | `output/final/` | `YYYY-MM-DD-task-final.md` |
