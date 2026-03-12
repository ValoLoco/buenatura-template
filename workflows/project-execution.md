# Generic Project Execution: 6-Phase Lifecycle

A universal project framework for any scope. Each phase has a gate checklist.
Any defect or quality gap found in any phase triggers `workflows/dmaic-recursive.md`.

---

## Phase 1: Initiate

**Goal**: Establish shared understanding of what, why, and who.

- Load `skills/project-charter.md`. Produce charter using that skill's structure and validation rules.
- Define success metrics (CTQs) with units and targets.
- Assign ownership. Set communication cadence.

**Phase Gate:**
- [ ] Charter complete per `skills/project-charter.md` validation checks.
- [ ] At least one measurable CTQ with a target value and unit defined.
- [ ] Owner assigned to a named person.

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 1 outcomes (charter headline, key CTQs, owner) to `output/YYYY-MM-DD-project-initiate-summary.md`. Unload Phase 1 files.

Output: `output/YYYY-MM-DD-project-charter-v1.md`

---

## Phase 2: Align

**Goal**: Confirm strategic fit and resolve ambiguity before work begins.

- Validate alignment with mission, strategy, and available resources.
- Run `workflows/ooda-decision.md` on any open questions.
- Confirm budget, tools, and team capacity.

**Phase Gate:**
- [ ] Strategic alignment confirmed.
- [ ] All open questions resolved (no blocking ambiguities).
- [ ] Resources confirmed.

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 2 outcomes (alignment decisions, resource confirmation) to `output/YYYY-MM-DD-project-align-summary.md`. Unload Phase 2 files.

Output: `output/YYYY-MM-DD-project-alignment-v1.md`

---

## Phase 3: Structure

**Goal**: Design the process before executing it.

- Load `skills/sipoc.md`. Produce SIPOC with boundary triggers and CTQ linkage.
- Build CTQ tree from SIPOC outputs: Business Objective > Driver > Metric > Target > Operational Definition.
- Load `skills/fmea.md`. Run FMEA on identified process steps. Calculate RPN. Prioritise top risks.
- Define work breakdown structure with clear deliverables.

**Phase Gate:**
- [ ] SIPOC complete per `skills/sipoc.md` validation checks.
- [ ] Each CTQ has a target value, unit, and operational definition.
- [ ] FMEA complete: all RPN > 150 and all S >= 9 have assigned actions.
- [ ] Work breakdown structure approved.

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 3 outcomes (SIPOC scope, top FMEA risks, WBS headline) to `output/YYYY-MM-DD-project-structure-summary.md`. Unload Phase 3 files.

Output: `output/YYYY-MM-DD-project-structure-v1.md`

---

## Phase 4: Execute

**Goal**: Deliver with consistent quality. Catch defects early.

- Deliver work in iterations using `workflows/iteration-loop.md`.
- Trigger `workflows/dmaic-recursive.md` for any recurring defect.
- Apply `.claude/guardrails.md` and `.claude/evaluator.md` per deliverable.

**Phase Gate:**
- [ ] All deliverables pass guardrails.
- [ ] Evaluator aggregate >= 0.85 per deliverable.
- [ ] No open critical defects.

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 4 outcomes (deliverables completed, defects found and resolved, final quality scores) to `output/YYYY-MM-DD-project-execute-summary.md`. Unload per-deliverable context.

Output per deliverable: `output/YYYY-MM-DD-[deliverable]-v1.md`

---

## Phase 5: Reflect

**Goal**: Extract and store learnings before closing.

- Retrospective: what worked, what did not, root causes of issues.
- Write lessons learned to `MEMORY/context.md` (Lessons Learned table).
- Update `MEMORY/context.md` Active Projects: mark this project complete.
- Score overall project via `.claude/evaluator.md` dimensions.
- Identify any reusable patterns to convert into skills or playbooks.

**Phase Gate:**
- [ ] Retrospective completed.
- [ ] Lessons written to `MEMORY/context.md` Lessons Learned table.
- [ ] Active Projects row removed or marked complete in `MEMORY/context.md`.
- [ ] New skills or playbooks registered if created.

**Phase Close -- Context Hygiene:**
Write a one-paragraph summary of Phase 5 outcomes (key lessons, skills created) to `output/YYYY-MM-DD-project-reflect-summary.md`. Unload Phase 5 files.

Output: `output/YYYY-MM-DD-project-retrospective-v1.md`

---

## Phase 6: Close

**Goal**: Hand over cleanly. Lock in the result.

- Final delivery and formal handover.
- Load `skills/control-plan.md`. Document control plan per that skill's structure and validation checks.
- Move all final outputs to `output/final/`.
- Archive working files.

**Phase Gate:**
- [ ] All outputs in `output/final/`.
- [ ] Control plan complete per `skills/control-plan.md` validation checks.
- [ ] Ownership assigned to a named person.
- [ ] Stakeholder sign-off received.

Output: `output/YYYY-MM-DD-project-close-v1.md`
