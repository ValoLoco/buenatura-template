# Framework Relationships

This file defines when to use each framework and how they relate to each other.
Load this when you are unsure which framework applies to your situation.

---

## The Stack

```
Task arrives
    |
    v
OODA: orient and decide which framework to use
    |
    +-- Comms / marketing / negotiation task?     Use: FATE (in workflows/comms-negotiation.md)
    +-- Recurring defect or process gap?          Use: DMAIC Recursive
    +-- Project with multiple phases?             Use: Project Execution
    +-- Business design / MVP / offer / scaling?  Use: Business Architect skill
    +-- Single task needing quality control?      Use: Iteration Loop
    |
    v
During execution:
    +-- Making factual or analytical claims?      Run: VERITAS (standalone)
    +-- Researching any topic?                    Run: Research Workflow (VERITAS embedded)
    |
    v
Before delivery (always):
    +-- Run Guardrails (5 gates)                  File: guardrails.md
    +-- Score with Evaluator (5 dimensions)       File: evaluator.md
    +-- Below threshold?                          Run: Iteration Loop
```

---

## Agent Entry Points

If the task is being executed by a named agent, the agent file is the entry point.
Agents load this routing stack internally. Do not re-route manually.

| Agent | Entry File | Frameworks It Uses |
|-------|------------|--------------------|
| @researcher | `agent-scaffold/agents/researcher.md` | Research Workflow, VERITAS |
| @comms | `agent-scaffold/agents/comms.md` | FATE |
| @decider | `agent-scaffold/agents/decider.md` | OODA |
| @reviewer | `agent-scaffold/agents/reviewer.md` | Guardrails, Evaluator, Iteration Loop |
| @dmaic | `agent-scaffold/agents/dmaic.md` | DMAIC Recursive, phase skills (SIPOC, FMEA, Control Plan) |
| @project | `agent-scaffold/agents/project.md` | Project Execution, phase skills |
| @6sigma | `agent-scaffold/agents/6sigma.md` | DMAIC Recursive, OODA, FMEA, statistical tools, inference gate |
| @biz | `agent-scaffold/agents/business-architect.md` | Business Architect skill, VERITAS, Iteration Loop |

Full agent registry: `.claude/routing-table.md` Agent Registry section.

---

## Framework Purpose Table

| Framework | File | When to Use | What It Produces |
|-----------|------|-------------|------------------|
| OODA | `workflows/ooda-decision.md` | Any decision under uncertainty or ambiguity | A chosen path with rationale |
| FATE | `workflows/comms-negotiation.md` | Any comms, marketing, negotiation, or pitch task | Structured, audience-first message |
| DMAIC Recursive | `workflows/dmaic-recursive.md` | Recurring defect, process gap, quality drift | Root cause + validated solution + control plan |
| Project Execution | `workflows/project-execution.md` | Multi-phase work with defined deliverables | Phase gates, structured outputs per phase |
| Business Architect | `skills/business-architect.md` | One-person business design: market validation, MVP, offer, prototype, agent stack | Phase-tagged deliverables (pain map, offer doc, MVP spec, agent stack plan) |
| Iteration Loop | `workflows/iteration-loop.md` | Any single output needing quality validation | Versioned output meeting 0.85 threshold |
| VERITAS | `skills/veritas-verification.md` | Validating claims outside of research context | 7-lens verification checklist |
| Research Workflow | `skills/research-workflow.md` | Any task requiring knowledge gathering | Verified, cited synthesis (VERITAS embedded) |
| Guardrails | `.claude/guardrails.md` | Before every delivery | Go/no-go decision on 5 gates |
| Evaluator | `.claude/evaluator.md` | Before every delivery | Scored output with aggregate |

---

## Key Relationships

- **FATE lives inside `workflows/comms-negotiation.md`.** There is no separate fate.md file. Load comms-negotiation.md to access FATE.
- **VERITAS has two modes.** Embedded: runs automatically inside Research Workflow at Step 4. Standalone: run directly when validating claims, agent outputs, or strategies outside a research task.
- **Guardrails and Evaluator are always paired.** Never run one without the other before delivery.
- **OODA is the meta-framework.** Use it to decide which other framework to enter.
- **DMAIC contains Iteration Loop.** Each DMAIC phase uses the loop for its own phase outputs.
- **Project Execution triggers DMAIC.** Any phase defect in a project opens a DMAIC sub-loop.
- **Business Architect escalates to DMAIC or Project.** If a business design engagement uncovers a recurring process defect, hand off to @dmaic. If scope exceeds 6 phases, hand off to @project.
- **Agents are entry points, not frameworks.** An agent coordinates frameworks. It does not replace them.
- **Two principle files exist.** `principles-core.md` holds 5 universal principles loaded on every task. `principles-extended.md` holds 8 additional principles (Principles 6-13) required for agent design, system-level tasks, and any task that writes, deletes, or publishes state. Load both for those task types.

---

## Anti-Patterns

| Do Not | Do Instead | Why |
|--------|------------|-----|
| Run DMAIC on a one-off task | Use Iteration Loop | DMAIC is for recurring process defects, not single outputs |
| Run DMAIC on a business design task | Use Business Architect (@biz) | Business design is a creation problem, not a defect problem |
| Run VERITAS after synthesis | Run it on each source before synthesising | Garbage in, garbage out |
| Use FATE before research | Research and verify first, then shape the message | FATE structures facts, it does not replace them |
| Skip OODA when task type is ambiguous | Always orient before acting | Acting without orientation wastes cycles |
| Run Evaluator without Guardrails first | Run Guardrails, then Evaluator | Gates must pass before scoring is meaningful |
| Use em dashes in any output | Use a period, comma, colon, or parentheses | Principle 5: em dashes are banned universally |
| Invoke an agent without checking its scope | Read the agent file first | Agents have explicit scope boundaries |
| Load only principles-core.md for agent/system tasks | Also load principles-extended.md | Principles 6-13 apply to agent design and state-changing operations |
