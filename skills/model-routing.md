---
name: model-routing
description: Scores task complexity and routes to local BitNet inference or frontier API.
---

# Model Routing

Decides whether a task routes to local inference (BitNet, zero cost) or the frontier API (Claude, per-token cost). Sovereign by default: local first, API only when justified.

## When to Load

Load at the start of every task before any inference call is made.
This skill is the entry gate for all LLM calls in the system.

## Precondition

The `output/` directory must exist before this skill runs (it logs to `output/routing.log`).
`output/` is scaffolded by the template. If it is missing, run the template setup step first.

## Complexity Scoring

Score the incoming task on four dimensions (1 = low, 3 = high):

| Dimension | Low (1) | Medium (2) | High (3) |
|---|---|---|---|
| **Context length** | < 500 tokens | 500-2000 tokens | > 2000 tokens |
| **Reasoning depth** | Extract / classify / format | Summarize / draft / compare | Multi-step reasoning / strategy / judgment |
| **Stakes** | Internal / draft / throwaway | Client-facing / logged | Irreversible / published / financial |
| **Reversibility** | Fully reversible (edit, draft) | Partially reversible (logged, stored) | Irreversible (send, delete, publish, deploy) |

Sum the four scores. Total range: 4-12.

## Routing Decision

| Total Score | Route | Skill to Load |
|---|---|---|
| 4-6 | Local | `skills/local-inference.md` |
| 7-9 | Local with review | `skills/local-inference.md`, flag output for human review |
| 10-12 | Frontier API | Claude or configured API |

Additional rule: if Reversibility scores 3 (irreversible action), route is minimum Local with review regardless of total score. Any irreversible action also triggers Gate 4 of `.claude/guardrails.md` before execution.

## Rules

- Default to local. Escalate only when score justifies it.
- Log every routing decision to `output/routing.log`: task ID, scores per dimension, total, route chosen, timestamp.
- If unsure about a dimension score, round up (conservative escalation).
- A score of 10-12 does not require additional explanation in the log. A score of 7-9 routed to API must log the reason.

## Output

Returns one of: `local`, `local-review`, `api`.
Log entry written to `output/routing.log`.
