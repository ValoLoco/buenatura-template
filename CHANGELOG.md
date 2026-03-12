# Changelog

All notable changes to this template follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.2.0] - 2026-03-13 (DMAIC Full Sync: template completeness 35% to 100%)

### Added

**RAG Layer**
- `tools/knowledge_search.py`: semantic search over `KNOWLEDGE/` corpus using `sentence-transformers` + `sqlite-vec`. Incremental index, 400-word chunks, 50-word overlap, offline-capable.
- `skills/knowledge-search.md`: skill file for invoking the RAG tool. Rules, score threshold (0.50), top-K guidance, prerequisites.

**AgentOps Observability Layer**
- `agent-scaffold/ops/trace_logger.py`: lightweight JSONL trace writer. `TaskTrace` class + `log_event()` function. One file per day at `output/traces/YYYY-MM-DD.jsonl`.
- `agent-scaffold/ops/eval.py`: daily trace evaluator. Reports task count, success rate, avg latency, tool call frequency, failure list.
- `agent-scaffold/ops/__init__.py`: package init for `agent_scaffold.ops` imports.
- `skills/agentops.md`: skill file documenting trace instrumentation, event names, storage rules, and eval usage.

**Full Framework Sync from bue-buenatura-org**
- `.claude/principles-core.md`: Principles 1-5 (Carbon Fiber, YAGNI, AI-First, Uncle Bob, No Em Dashes). Loaded on every task.
- `.claude/principles-extended.md`: Principles 6-13 (One Source of Truth, Explicit Over Implicit, Reversibility First, Fail Loudly, Context Window Hygiene, Idempotency, Minimal Footprint, Observability). Load for agent design and state-changing tasks.
- `.claude/principles.md`: deprecated stub with redirect to core/extended. Prevents silent failures on stale references.
- `.claude/guardrails.md`: 5 validation gates (Principle Compliance, Output Quality, Resource Efficiency, Safety and Reversibility, Business Alignment and Observability). Includes Irreversible Action Confirmation template and two Standing Audit Rules.
- `.claude/evaluator.md`: 5-dimension scoring model (Correctness, Relevance, Completeness, Efficiency, Clarity). Ship threshold 0.85. Handoff block format for iteration-loop.
- `.claude/framework-relationships.md`: full decision tree mapping task types to frameworks, agent entry points table, framework purpose table, key relationships, anti-patterns.
- `.claude/naming-conventions.md`: file, folder, branch, agent, and skill naming rules. Phase-close summary file format.
- `.claude/skills-protocol.md`: 4-step protocol for finding, installing, and building skills. skills.sh integration (manual, MCP, CLI options).
- `.claude/session-log-template.md`: session log template implementing Principle 13. Routing log, actions log, quality gate results, self-extension flags, session close checklist.
- `.claude/self-extension-protocol.md`: 5-step protocol for classifying, recording, fixing, verifying, and preventing recurrence of framework gaps.
- `skills/model-routing.md`: complexity scoring on 4 dimensions (context length, reasoning depth, stakes, reversibility). Routes local (BitNet) or frontier API. Conservative escalation rule on irreversible actions.
- `skills/local-inference.md`: BitNet b1.58 2B4T inference skill. Input schema, execution command, fail-loud rules, log output.
- `skills/project-charter.md`: structured charter template for DMAIC Define phase. Problem statement number rule, SMART goal, scope with explicit out-of-scope, stakeholder table, timeline, risks.
- `skills/sipoc.md`: SIPOC with boundary triggers (observable events only) and CTQ linkage. 3-7 step rule. Validation checklist.
- `skills/fmea.md`: FMEA with S/O/D scales (1-10), RPN formula, prioritisation rules (RPN > 150, S >= 9), full table structure. Action verification method required.
- `skills/control-plan.md`: control plan with control method options (statistical and non-statistical), Cpk targets, benefit tracking, audit frequency. All rows require named owners.
- `skills/research-workflow.md`: 6-step context-first research process. VERITAS as mandatory gate between search and synthesis. Good output checklist.
- `skills/veritas-verification.md`: 7-lens verification framework (V E R I T A S). Standalone and embedded modes.
- `workflows/dmaic-recursive.md`: full 5-phase DMAIC with phase gate checklists, CTQ tree construction rules, MSA, Cpk formulas, FMEA integration, control chart limits, context hygiene (phase-close summaries), recursive sub-loop rule, sigma reference table.
- `workflows/iteration-loop.md`: evaluate-ship-or-revise loop. Handoff block consumption protocol, revision prioritisation by RPN, DMAIC escalation trigger conditions, output naming convention.
- `workflows/ooda-decision.md`: 4-phase OODA (Observe, Orient, Decide, Act) with checklists per phase. Framework selection guide. OODA vs DMAIC comparison table.
- `workflows/comms-negotiation.md`: FATE framework (Focus, Authority, Tribe, Emotion). Application matrix for 6 use cases. Output structure. Negotiation preparation checklist.
- `workflows/project-execution.md`: 6-phase project lifecycle (Initiate, Align, Structure, Execute, Reflect, Close). Phase gate checklists. Context hygiene (phase-close summaries). Integrates all DMAIC skills.
- `agent-scaffold/config.json`: baseline agent config template. `load_on_start`, `load_on_task` maps, output dirs, ship threshold, escalation target.
- `agent-scaffold/instructions.md`: agent instructions template. Task execution protocol (7 steps incl. inference gate), scope boundaries, escalation protocol.
- `infra/README.md`: infra layer documentation. Contents table, setup commands, requirements, post-bootstrap state.

### Mirrored to bue-buenatura-org/MAIN/TEMPLATE
- `tools/knowledge_search.py`
- `skills/knowledge-search.md`
- `skills/agentops.md`
- `agent-scaffold/ops/trace_logger.py`
- `agent-scaffold/ops/eval.py`
- `agent-scaffold/ops/__init__.py`

### Root Cause (template incompleteness at session start)
Two root causes: (1) the template was bootstrapped incrementally across sessions without a sync gate, leaving `.claude/`, `skills/`, and `workflows/` partially populated; (2) no cross-repo diff check existed to catch drift between `buenatura-template` and `bue-buenatura-org/MAIN/TEMPLATE`. This DMAIC cycle adds both the missing files and the awareness that a sync check should run at the start of every session involving both repos.

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
