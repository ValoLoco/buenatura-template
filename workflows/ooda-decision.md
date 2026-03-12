# Generic OODA Decision Framework

Use for any decision under uncertainty, task routing, or dynamic real-time adaptation.
OODA loops continuously. Each cycle feeds the next. Speed through the loop is the advantage.

---

## Phase 1: Observe

**Goal**: Gather unfiltered raw data. Do not interpret yet.

- Inputs: user request, context files, metrics, feedback, environment signals.
- Capture what is actually happening, not what you expect.
- Key question: What is actually happening right now?

**Observe Checklist:**
- [ ] All available context files read.
- [ ] No interpretation applied yet.
- [ ] Data gaps identified and noted.

---

## Phase 2: Orient

**Goal**: Synthesise observations into a situational picture.

- Apply mental models: DMAIC patterns, first principles, domain knowledge.
- Identify what is familiar, what is novel, what is ambiguous.
- Acknowledge biases and knowledge gaps explicitly.
- Key question: What does this mean?

**Orient Checklist:**
- [ ] Observations synthesised.
- [ ] Relevant mental models applied.
- [ ] Assumptions and biases named.
- [ ] Knowledge gaps flagged for escalation if critical.

---

## Phase 3: Decide

**Goal**: Select the best path with available information.

- Generate 2-3 options minimum. Do not default to the first idea.
- Score each option: Impact (1-5), Feasibility (1-5), Alignment (1-5).
- Select the highest combined score. Document the rationale.
- Identify a fallback if the primary option fails.
- Key question: What should we do?

**Decide Checklist:**
- [ ] Minimum 2 options generated.
- [ ] Options scored on impact, feasibility, alignment.
- [ ] Decision and rationale documented.
- [ ] Fallback option named.

---

## Phase 4: Act

**Goal**: Execute the decision with precision. Measure the outcome. Feed results back.

- Execute as decided. No scope creep.
- Monitor outcomes in real time.
- After acting: record what changed and whether the outcome matched expectation.
- Feed the result explicitly back into the next Observe phase as a new input.
- If outcome deviates from expectation: tighten the loop. Do not abandon it.
- Key question: Did it work? What changed? What does the next Observe cycle now see?

**Act Checklist:**
- [ ] Decision executed as planned.
- [ ] Outcome measured and recorded.
- [ ] Deviation from expectation noted (if any).
- [ ] Result fed back into next Observe as a named input.
- [ ] Loop continues until stable or task complete.

---

## Framework Selection Guide

Use this when unsure which framework to apply.

| Situation | Use |
|-----------|-----|
| Fast-moving decision, uncertainty, routing choice | OODA (this file) |
| Recurring defect or measurable process gap | DMAIC (`workflows/dmaic-recursive.md`) |
| Single output needing quality validation | Iteration Loop (`workflows/iteration-loop.md`) |
| Multi-phase project with defined deliverables | Project Execution (`workflows/project-execution.md`) |
| Comms, marketing, negotiation, or pitch | FATE (`workflows/comms-negotiation.md`) |
| Unsure which framework applies | Load `.claude/framework-relationships.md` for the full decision tree, then return here to start at Observe. |

---

## OODA vs DMAIC: Detailed Comparison

| Dimension | OODA | DMAIC |
|-----------|------|-------|
| Speed | Seconds to minutes | Days to weeks |
| Best for | Dynamic decisions, routing, real-time | Process improvement, defect elimination |
| Data requirement | Minimal: act on best available | Rigorous: validate before acting |
| Loop type | Continuous | Project-based with defined phases |
| Trigger | Uncertainty, ambiguity, fast-moving context | Recurring defect, quality gap, process drift |
