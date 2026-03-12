# 5 Evaluation Dimensions

Score each dimension 0 to 1. Aggregate must reach 0.85 to ship.
Use the anchor descriptions below for consistent scoring.

---

## 1. Correctness (0-1)

Factually accurate. Technically sound. No errors. Failures surfaced explicitly, not swallowed (Principle 9: Fail Loudly).

| Score | Meaning |
|-------|---------|
| 1.0 | Zero errors. All facts verified. All logic sound. Ambiguities flagged. |
| 0.85 | One minor imprecision, no impact on outcome. |
| 0.70 | One factual or technical error, correctable. |
| 0.50 | Multiple errors or one significant error. |
| < 0.50 | Fundamental correctness failure. Do not ship. |

## 2. Relevance (0-1)

Directly addresses the request. No tangents.

| Score | Meaning |
|-------|---------|
| 1.0 | Every sentence serves the request. Nothing off-topic. |
| 0.85 | Mostly on-point. One minor tangent. |
| 0.70 | Core request addressed but notable scope drift. |
| 0.50 | Partial response. Key aspect of request missed. |
| < 0.50 | Output addresses wrong problem. Do not ship. |

## 3. Completeness (0-1)

All requirements covered. No gaps.

| Score | Meaning |
|-------|---------|
| 1.0 | All requirements met. All gates checked. All outputs produced. |
| 0.85 | One minor requirement missing, easily added. |
| 0.70 | One significant requirement missing. |
| 0.50 | Multiple requirements missing. |
| < 0.50 | Core deliverable absent. Do not ship. |

## 4. Efficiency (0-1)

Optimal resource usage. Concise without losing substance. Minimal footprint: no excess permissions, connections, or files loaded (Principle 12: Minimal Footprint).

| Score | Meaning |
|-------|---------|
| 1.0 | Nothing redundant. Every element earns its place. Footprint minimal. |
| 0.85 | One redundant section or unnecessary step. |
| 0.70 | Noticeable bloat or repeated content. |
| 0.50 | Significant waste: duplicated logic, unused files, excess calls. |
| < 0.50 | Fundamentally inefficient. Carbon Fiber violated. Do not ship. |

## 5. Clarity (0-1)

Easy to understand. Actionable. No ambiguity.

| Score | Meaning |
|-------|---------|
| 1.0 | Instantly clear. Any agent or human can act without clarification. |
| 0.85 | One ambiguous phrase, easily resolved. |
| 0.70 | Requires re-reading. Key action unclear. |
| 0.50 | Multiple ambiguities. Next step is not obvious. |
| < 0.50 | Output is confusing or contradictory. Do not ship. |

---

## Ship Threshold

\( Aggregate = \frac{C_1 + C_2 + C_3 + C_4 + C_5}{5} \)

Aggregate >= 0.85: SHIP to `output/final/`.
Aggregate < 0.85: REVISE via `workflows/iteration-loop.md`.
Any single dimension < 0.50: STOP. Do not ship regardless of aggregate.

---

## Handoff to Iteration Loop

When passing a failed output to `workflows/iteration-loop.md`, include this handoff block:

```
Iteration Loop Handoff:
  Output file: [path to the file being revised]
  Current version: [vN]
  Failed dimensions: [list dimension names and scores]
  Failed gates: [list gate numbers and findings]
  Specific defects: [one sentence per defect, actionable]
  Revision instruction: [what must change to pass]
```

Do not pass the output to the loop without this block. Vague handoffs produce generic rewrites that do not fix the actual defect.
