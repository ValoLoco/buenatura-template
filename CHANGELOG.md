# Changelog

All notable changes to this template follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.1.0] - 2026-03-12 (DMAIC Audit: 3 passes, 15 defects resolved)

### Added
- `@biz` Business Architect agent: `agent-scaffold/agents/business-architect.md` + `.json`
- `skills/business-architect.md`: full One-Person AI Business Playbook (6 phases, Handoffs, Verification)
- Full 8-agent roster in `agent-scaffold/agents/`: researcher, comms, decider, reviewer, dmaic, project, 6sigma, biz
- All 8 agent JSON configs with version history and `load_on_task` maps
- `workflows/` directory with 5 workflow files: comms-negotiation, dmaic-recursive, iteration-loop, ooda-decision, project-execution
- `MEMORY/session-log-2026-03-12.md`: first full session log (Principle 13: Observability)
- `agent-scaffold/PLAYBOOKS/README.md` and `agent-scaffold/TEMPLATES/README.md`: scaffold directories with format guides
- `agent-scaffold/MEMORY/context.md` and `agent-scaffold/KNOWLEDGE/` with `README.md` and `links.md`
- `agent-scaffold/instructions.md` and `agent-scaffold/config.json`: blank agent scaffold for custom agents

### Changed
- `README.md`: agent count corrected 7 to 8. Quick Start Step 5 references 4-surface registration checklist.
- `.claude/framework-relationships.md`: `@biz` added to The Stack decision tree, Agent Entry Points, Framework Purpose Table, Key Relationships, Anti-Patterns.
- `skills/skill-creation-guide.md`: Step 3 template extended (Trigger Conditions, Handoffs, Output, Verification). Step 4 replaced with explicit 4-surface registration checklist.
- `.claude/routing-table.md`: Quality Review row adds `skills/veritas-verification.md`. Create Agent row adds `skills/skill-creation-guide.md`. Agent Registry footer updated to list all 4 registration surfaces.
- `.claude/self-extension-protocol.md`: fixed 2 broken path refs (`skills-protocol.md`, `skill-creation-guide.md`). Step 3 updated to 4-surface registration. All bare filenames given full paths.
- `agent-scaffold/KNOWLEDGE/links.md`: Business Design section added with `@biz` references.
- `MEMORY/context.md`: fully initialized with active project, 4 past decision rows, escalation log, backlog, and lessons learned.
- `skills/README.md`: `business-architect` load condition row added.

### Root Cause (all 15 defects)
Two root causes: (1) deferred sync — descriptor files (README, framework-relationships, routing-table) not updated when `@biz` was added; (2) incomplete registration standard — `skill-creation-guide.md` Step 4 listed only 2 of 4 required registration surfaces, making incomplete agent registration the default outcome on every new agent creation.

---

## [1.0.0] - 2026-03-12

### Added
- Full agent scaffold: skills, workflows, .claude config, KNOWLEDGE, MEMORY, output, infra directories
- Skills: model-routing, local-inference, research-workflow, veritas-verification, project-charter, sipoc, fmea, control-plan, autoresearch
- autoresearch skill and scaffold: autonomous BitNet experiment loop inspired by karpathy/autoresearch
- .claude config: routing-table, guardrails, evaluator, principles, naming-conventions, session-log, skills-protocol, self-extension-protocol
- bootstrap.sh for one-command local setup
- VERSION file for downstream pinning
