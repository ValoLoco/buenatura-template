---
name: project-charter
description: Produces a structured project charter for DMAIC Define phase or project initiation.
---

# Skill: Project Charter

Precondition: A problem has been identified and a DMAIC loop is being initiated.
Load this skill when task type is `Project Lifecycle` or `Process Improvement / Defect` at the Define phase.

---

## Purpose

A project charter defines the problem, goal, scope, and team before any measurement or analysis begins.
Nothing proceeds to Phase 2 (Measure) without a completed charter.

---

## Output Format

Produce a single markdown file at `output/YYYY-MM-DD-charter-v1.md` using the structure below.
All fields are required. If a field cannot be filled, write `UNKNOWN - flag for human input` and stop.

---

## Charter Structure

### Project Title
Format: [Process name] + [Problem] + [Benefit direction]
Example: `Invoice Processing / Late Payments / Cycle Time Reduction`

### Problem Statement
In [process], current performance is [baseline metric +/- variation],
resulting in [impact: financial / customer / operational] per [period].
Target: [desired metric]. Estimated annual benefit: [value].

Rule: problem statement must contain a number. No number = not a problem statement.

### Goal Statement (SMART)
Reduce / Increase [metric] from [baseline] to [target] by [date].
Target sigma improvement: minimum 2-sigma shift.

### Scope
- In scope: [processes / locations / product lines / segments]
- Out of scope: [explicitly excluded areas]

Rule: out-of-scope must be populated. An empty out-of-scope field invites scope creep.

### Team
- Sponsor: [name / role]
- Lead: [name / role]
- Members: [names / roles]
- Coach: [name / role or N/A]

### Key Stakeholders
| Stakeholder | Interest | Support Level (High/Med/Low) |
|-------------|----------|------------------------------|
| [name/group] | [what they care about] | |

### Timeline
| Phase | Target Date |
|-------|-------------|
| Define | |
| Measure | |
| Analyze | |
| Improve | |
| Control | |

### Risks and Assumptions
| Risk | Mitigation |
|------|------------|
| [risk] | [action] |

Assumptions: list each critical assumption explicitly. No implicit assumptions.

---

## Validation Before Delivery

- [ ] Problem statement contains a baseline metric with a number.
- [ ] Goal statement has a measurable target and a date.
- [ ] Out-of-scope is populated.
- [ ] Sponsor is named (not a role placeholder).
- [ ] No field reads as a placeholder except those explicitly flagged for human input.

Fail any check: flag the missing field and stop. Do not deliver a partial charter.
