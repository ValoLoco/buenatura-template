---
name: fmea
description: Produces a ranked FMEA risk register with RPN scores for DMAIC Analyze phase.
---

# Skill: FMEA (Failure Modes and Effects Analysis)

Precondition: SIPOC complete. Process steps identified.
Load this skill during DMAIC Phase 3 (Analyze) to identify, rank, and prioritize failure modes.

---

## Purpose

FMEA converts qualitative root cause analysis into a ranked, actionable risk register.
RPN scores determine which failure modes to address first.
Updated after Phase 4 (Improve) to confirm RPN reduction.

---

## Scoring Scales (1-10 each)

**Severity (S):** Impact on the customer or next process if the failure occurs.
- 1-3: Minor. Customer unlikely to notice.
- 4-6: Moderate. Customer notices, some dissatisfaction.
- 7-8: High. Customer dissatisfied, potential rework.
- 9-10: Critical. Safety risk, regulatory breach, or complete failure.

**Occurrence (O):** Frequency of the root cause occurring.
- 1-2: Remote (< 1 in 10,000).
- 3-4: Low (1 in 1,000).
- 5-6: Moderate (1 in 100).
- 7-8: High (1 in 10).
- 9-10: Very high (> 1 in 2).

**Detection (D):** Ability of current controls to catch the failure before it reaches the customer.
- 1-2: Almost certain detection.
- 3-4: High likelihood of detection.
- 5-6: Moderate. May be caught.
- 7-8: Low. Unlikely to be caught.
- 9-10: No control exists.

**RPN formula:**
\( RPN = S \times O \times D \)

For scoring guidance when used outside of FMEA context (e.g., iteration-loop.md): S = severity of the defect, O = likelihood it recurs, D = likelihood current process catches it.

---

## Prioritization Rules

- RPN > 150: act.
- S >= 9: act regardless of RPN.
- Any RPN increase after action: unacceptable, escalate immediately.

---

## Output Format

Produce a markdown file at `output/YYYY-MM-DD-fmea-v1.md`.
Use the table below. All columns required.

### FMEA Table

| Process Step | Failure Mode | Effect | S | Root Cause | O | Current Controls | D | RPN | Action | Owner | Target Date | New S | New O | New D | New RPN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [step from SIPOC] | [what could go wrong] | [impact on output/customer] | | [why it occurs] | | [controls in place today] | | | [action to reduce RPN] | | | | | | |

---

## Validation Before Delivery

- [ ] Every process step from the SIPOC has at least one failure mode.
- [ ] No S, O, or D field is blank.
- [ ] All RPN > 150 have a named action and owner.
- [ ] All S >= 9 rows have a named action and owner.
- [ ] Action effectiveness verification method is documented below the table.

Action verification method: [describe how actions will be confirmed effective]

Fail any check: flag the gap and stop. Do not deliver an incomplete FMEA.
