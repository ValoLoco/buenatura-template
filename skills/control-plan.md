---
name: control-plan
description: Produces a control plan with ownership, measurement, and reaction plans for DMAIC Control phase.
---

# Skill: Control Plan

Precondition: FMEA complete. Improvement implemented and validated.
Load this skill during DMAIC Phase 5 (Control) to lock in the improvement and prevent regression.

---

## Purpose

A control plan assigns ongoing ownership of each critical process parameter.
Without a control plan, improvements regress. A control chart without an owner is not a control plan.

---

## Long-term Capability Target

\( C_{pk} \geq 1.67 \) recommended for critical characteristics.
\( C_{pk} \geq 1.33 \) minimum for standard process parameters.

If post-improvement \( C_{pk} \) < 1.33: do not close the project. Return to Phase 4.

---

## Output Format

Produce a markdown file at `output/YYYY-MM-DD-control-plan-v1.md`.
All columns required. Empty cells are not permitted.

### Control Plan Table

| Process Step | Parameter | Specification / Tolerance | Measurement Method | Sample Size / Frequency | Control Method | Reaction Plan | Owner | Document Reference |
|---|---|---|---|---|---|---|---|---|
| [step] | [input or output variable] | [target +/- tolerance] | [gage, system, or method] | [n= / interval] | [chart type or non-statistical method] | [if out of control: who does what] | [named person] | [SOP or WI number] |

### Control Method Options

Statistical:
- Individuals (I-MR): continuous data, subgroup size = 1.
- Xbar-R: continuous data, subgroup size 2-10.
- p-chart: proportion defective, variable sample size.
- np-chart: number defective, fixed sample size.
- c-chart: count of defects, fixed area of opportunity.
- u-chart: count of defects per unit, variable area.
- EWMA / CUSUM: detecting small shifts in the mean.

Non-statistical:
- Visual inspection standard.
- Checklist or audit.
- Mistake-proofing device (poka-yoke).
- Training matrix with sign-off.
- Periodic calibration record.

---

## Key Completion Checks

- [ ] Every CTQ from the CTQ tree has a row in this table.
- [ ] Every high-RPN item from the FMEA has a row in this table.
- [ ] Every row has a named owner (not a role title).
- [ ] Every reaction plan specifies who acts and within what timeframe.
- [ ] Audit frequency is set (quarterly minimum after year one).
- [ ] Benefit tracking method and responsible person are documented.
- [ ] Final \( C_{pk} \) vs baseline \( C_{pk} \) delta is recorded.

Benefit tracking method: [describe]
Responsible: [named person]
Next audit date: [date]

Fail any check: flag the gap and stop. Do not hand over an incomplete control plan.
