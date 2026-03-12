# Recursive DMAIC Self-Improvement Loop

DMAIC is a data-driven framework for eliminating defects and improving any repeatable process.
The recursive variant means: any defect discovered within a phase triggers a nested DMAIC sub-loop before proceeding.

---

## Phase 1: Define

**Goal**: Establish a precise, agreed problem statement and success criteria.

- State the problem: what, where, when, how much impact. A problem statement with no number is not a problem statement.
- Build the CTQ tree:
  - Start from the Voice of Customer or Business.
  - Decompose to a Driver (the requirement behind the need).
  - Decompose to a measurable CTQ metric.
  - For each CTQ metric, define:
    - Target value with unit (example: cycle time <= 5 working days).
    - Operational definition: the exact measurement procedure so two people measuring independently get the same number.
  - No CTQ is valid without both a target value and an operational definition.
- Load `skills/sipoc.md`. Produce a SIPOC with boundary triggers and CTQ linkage per that skill.
- Define success criteria. No measurement begins without agreed success criteria.

**Phase Gate -- must pass before Phase 2:**
- [ ] Problem statement contains a baseline metric with a number and a unit.
- [ ] Each CTQ metric has a target value with a unit.
- [ ] Each CTQ metric has a written operational definition.
- [ ] SIPOC is complete with boundary triggers and CTQ linkage.
- [ ] Stakeholders have reviewed and agreed.

**Phase Close -- Context Hygiene:**
Before loading Phase 2, write a one-paragraph summary of Phase 1 outcomes to `output/YYYY-MM-DD-dmaic-define-summary.md`.
This summary replaces the full phase context in subsequent phases. Unload Phase 1 files after writing.

Output: `output/YYYY-MM-DD-dmaic-define-v1.md`

---

## Phase 2: Measure

**Goal**: Establish a reliable baseline using validated data.

- Identify the measurement system. Run MSA (Gauge R&R) if physical measurement.
- Collect data. Verify process stability before calculating capability.
- Calculate baseline process capability:

  \( C_p = \frac{USL - LSL}{6\sigma} \)

  \( C_{pk} = \min\left(\frac{USL - \mu}{3\sigma},\ \frac{\mu - LSL}{3\sigma}\right) \)

- A process is capable when \( C_{pk} \geq 1.33 \) (4-sigma minimum).

**Phase Gate -- must pass before Phase 3:**
- [ ] Measurement system validated (MSA complete or documented as N/A with justification).
- [ ] Baseline data collected (minimum 30 data points recommended).
- [ ] Cp and Cpk calculated and documented.
- [ ] Process confirmed stable (no special cause variation).

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 2 outcomes and baseline metrics to `output/YYYY-MM-DD-dmaic-measure-summary.md`.
Unload Phase 2 files. Carry only the summary into Phase 3.

Output: `output/YYYY-MM-DD-dmaic-measure-v1.md`

---

## Phase 3: Analyze

**Goal**: Identify and validate the root cause(s) of the defect.

- Map the process. Identify waste (muda) and variation sources.
- Apply root cause tools:
  - 5 Whys: drill from symptom to root cause.
  - Ishikawa (fishbone): categorise causes (6M: Man, Machine, Method, Material, Measurement, Mother Nature).
  - Pareto chart: rank causes by frequency or impact (80/20 rule).
- Load `skills/fmea.md`. Run FMEA to prioritise failure modes.

  \( RPN = Severity \times Occurrence \times Detection \)

- Validate root causes with data. Hypothesis without data is assumption.

**Phase Gate -- must pass before Phase 4:**
- [ ] At least one root cause validated with data.
- [ ] FMEA complete: RPN calculated for all significant failure modes.
- [ ] All RPN > 150 and all S >= 9 have assigned actions.
- [ ] Top 3 root causes ranked and documented.
- [ ] No assumed causes remain. All tested.

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 3 outcomes (validated root causes, top RPN items) to `output/YYYY-MM-DD-dmaic-analyze-summary.md`.
Unload Phase 3 files. Carry only the summary into Phase 4.

Output: `output/YYYY-MM-DD-dmaic-analyze-v1.md`

---

## Phase 4: Improve

**Goal**: Design, test, and validate a solution that eliminates the root cause.

- Generate solution options. Use Pugh matrix for structured comparison.
- Apply TRIZ for innovative problem-solving if conventional options fall short.
- Run DOE (Design of Experiment) to optimise the solution:
  - Full factorial for <= 3 factors.
  - Fractional factorial for 4+ factors.
- Pilot the solution. Measure results against Phase 2 baseline.
- Confirm Cpk improvement is statistically significant.

**Phase Gate -- must pass before Phase 5:**
- [ ] Solution selected with documented rationale.
- [ ] Pilot results show measurable improvement vs baseline.
- [ ] Cpk post-pilot >= target.
- [ ] No new failure modes introduced (FMEA updated with new RPN scores).

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 4 outcomes (solution implemented, pilot results, new Cpk) to `output/YYYY-MM-DD-dmaic-improve-summary.md`.
Unload Phase 4 files. Carry only the summary into Phase 5.

Output: `output/YYYY-MM-DD-dmaic-improve-v1.md`

---

## Phase 5: Control

**Goal**: Lock in the improvement. Prevent regression.

- Load `skills/control-plan.md`. Build a control plan per that skill's structure and validation checks.
- Build a control chart to monitor the process:

  Individuals (X-mR) control limits:
  \( UCL = \bar{x} + 3 \cdot \frac{\overline{MR}}{1.128} \)
  \( LCL = \bar{x} - 3 \cdot \frac{\overline{MR}}{1.128} \)

- Assign clear ownership. No owner = no control.
- Monitor for 30-90 days post-implementation.
- Write lessons learned to `MEMORY/context.md` (Lessons Learned table).
- If the process drifts beyond control limits: trigger a new DMAIC from Phase 1.

**Phase Gate -- project close:**
- [ ] Control plan complete per `skills/control-plan.md` validation checks.
- [ ] Control chart in place and being monitored.
- [ ] Ownership assigned to a named person.
- [ ] Baseline vs final Cpk delta documented.
- [ ] Lessons learned written to `MEMORY/context.md`.

Output: `output/YYYY-MM-DD-dmaic-control-v1.md`

---

## Recursive Rule

If a defect is discovered within any phase, do not proceed to the next phase.
Treat the defect as a new Define statement. Run a sub-loop.
Label sub-loop outputs: `output/YYYY-MM-DD-dmaic-[phase]-sub1-v1.md`.
Sub-loops nest without limit but each must complete their own Phase Gate before the parent phase continues.

---

## Sigma Reference

| Sigma Level | DPMO | Yield |
|-------------|------|-------|
| 3 sigma | 66,807 | 93.32% |
| 4 sigma | 6,210 | 99.38% |
| 5 sigma | 233 | 99.977% |
| 6 sigma | 3.4 | 99.9997% |

**Target for most AI-driven processes: 4 sigma minimum (Cpk >= 1.33).**
