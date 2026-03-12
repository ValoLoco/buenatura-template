---
name: sipoc
description: Produces a SIPOC process map with boundary triggers and CTQ linkage for DMAIC Define phase.
---

# Skill: SIPOC

Precondition: Project charter exists. Process scope is defined.
Load this skill during DMAIC Phase 1 (Define) to map the process at bird's-eye level.

---

## Purpose

A SIPOC surfaces the full process flow, its inputs, outputs, and the customers who judge quality.
It exists to confirm scope and expose unmeasured hand-offs before detailed mapping begins.
Do not build a detailed process map until the SIPOC is validated.

---

## Output Format

Produce a single markdown file at `output/YYYY-MM-DD-sipoc-v1.md` using the structure below.

---

## SIPOC Structure

### Header
- Project: [from charter]
- Process name: [specific subprocess being mapped]
- Scope level: High-level (default) or Detailed

### Table

| Suppliers | Inputs | Process Steps (5-7 max) | Outputs | Customers |
|-----------|--------|--------------------------|---------|----------|
| [who provides] | [what they provide] | 1. [first step] | [what is produced] | [who receives] |
| | | 2. | | |
| | | 3. | | |

Rule: process steps column must contain 3-7 steps. Fewer means the scope is too narrow. More means the scope is too broad or needs decomposition.

### Boundaries
- Start trigger: [the event that starts this process]
- Stop trigger: [the event that ends this process]

Rule: both triggers must be observable events, not states. Wrong: "when the order is ready." Right: "when the customer submits the order form."

### CTQ Linkage
For each output, identify the CTQ it must satisfy:

| Output | CTQ Metric | Specification / Target |
|--------|------------|------------------------|
| [output] | [measurable quality characteristic] | [value + unit] |

### Validation Questions
- [ ] Are all major hand-offs between departments or systems visible?
- [ ] Is each input traceable to a named supplier?
- [ ] Does the process owner confirm this reflects the actual process?
- [ ] Does each output link to at least one CTQ?

Fail any check: revise before proceeding to Phase 2.
