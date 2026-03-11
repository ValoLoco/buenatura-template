# Master Routing Table

Match your task to a row. Load only the listed files. Skip everything else.
This table is the single source of routing truth. Do not duplicate it elsewhere.

## Inference Gate (Always First)

Before any LLM call, run `skills/model-routing.md` to score complexity and select the inference tier.
Scoring scale: 4 dimensions, each 1-3. Total range: 4-12.

| Score | Route | Action |
|---|---|---|
| 4-6 | Local | Load `skills/local-inference.md`. No API call. |
| 7-9 | Local + review | Load `skills/local-inference.md`. Flag output for human review. |
| 10-12 | Frontier API | Use configured API (Claude or equivalent). Log escalation reason. |

Additional rule: if Reversibility dimension scores 3 (irreversible action), minimum route is Local + review regardless of total score.

Requires `infra/bootstrap.sh` to have been run once on this machine.

---

## Task Routing

| Task | Read | Skip | Load Skill |
|------|------|------|------------|
| Research / Fact-Finding | `.claude/guardrails.md` | All workflow files | `skills/research-workflow.md`, `skills/veritas-verification.md` |
| Comms / Marketing / Negotiations | `workflows/comms-negotiation.md` | `agent-scaffold/` | `skills/research-workflow.md` |
| Decision-Making | `workflows/ooda-decision.md` | All execution folders | None |
| Process Improvement / Defect: Define | `workflows/dmaic-recursive.md`, `.claude/guardrails.md` | Content workflows | `skills/project-charter.md`, `skills/sipoc.md` |
| Process Improvement / Defect: Analyze | `workflows/dmaic-recursive.md`, `.claude/guardrails.md` | Content workflows | `skills/fmea.md`, `skills/veritas-verification.md` |
| Process Improvement / Defect: Control | `workflows/dmaic-recursive.md`, `.claude/guardrails.md` | Content workflows | `skills/control-plan.md` |
| Project Lifecycle | `workflows/project-execution.md` | Completed phases | `skills/project-charter.md`, `skills/research-workflow.md` |
| Code / Build | `.claude/principles-core.md`, `.claude/principles-extended.md`, `.claude/guardrails.md` | `workflows/` | Check skills.sh for `code-reviewer` |
| Quality Review | `.claude/guardrails.md`, `.claude/evaluator.md`, `workflows/iteration-loop.md` | All else | None |
| Template Gap Found | `.claude/self-extension-protocol.md` | All else | None |
| Session Start / Close | `.claude/session-log-template.md` | All else | None |
| Create Agent | `agent-scaffold/` (full), `.claude/skills-protocol.md`, `.claude/principles-extended.md` | All workflow files | `skills/veritas-verification.md` |
| Autonomous Experiment Loop | `agent-scaffold/autoresearch/` (full) | All workflow files | `skills/autoresearch.md` |
| No Skill Exists | `.claude/skills-protocol.md` | All else | Search skills.sh first |

Output always to `output/YYYY-MM-DD-task-vN.md`.
Final approved output to `output/final/YYYY-MM-DD-task-final.md`.

---

## Agent Registry

Default agents live in `agent-scaffold/agents/`. Each has a `.md` (instructions) and `.json` (config).
To add a new agent: create both files, add a row here, update `agent-scaffold/agents/README.md`.

| Command | Agent File | Type | Responsibility |
|---------|------------|------|----------------|
| `@researcher` | `agent-scaffold/agents/researcher.md` | Flat specialist | Research, synthesis, verification |
| `@comms` | `agent-scaffold/agents/comms.md` | Flat specialist | Communication and negotiation drafting |
| `@decider` | `agent-scaffold/agents/decider.md` | Flat specialist | Decision structuring via OODA |
| `@reviewer` | `agent-scaffold/agents/reviewer.md` | Flat specialist | Guardrails + evaluator audit |
| `@dmaic` | `agent-scaffold/agents/dmaic.md` | Flat specialist | DMAIC loop execution |
| `@project` | `agent-scaffold/agents/project.md` | Phase coordinator | 6-phase project lifecycle |
| `@6sigma` | `agent-scaffold/agents/6sigma.md` | Domain expert | Master Black Belt statistical and Lean depth |
