# BUENATURA AI Agent Template

A lean, sovereign scaffold for AI-driven projects, agents, and workflows.
Built on 13 principles. Optimised for one-person and small-team operations.
Every file has a purpose. No bloat.

## What Is Here

| Folder | Purpose |
|--------|---------|
| `.claude/` | Core rules: routing, guardrails, evaluator, principles, session log |
| `workflows/` | Process definitions: DMAIC, OODA, FATE, project lifecycle, iteration loop |
| `skills/` | Reusable behaviour modules: research, verification, FMEA, control plan, business design |
| `agent-scaffold/` | Blank agent template + 8 ready-to-use agents + PLAYBOOKS, TEMPLATES, MEMORY, KNOWLEDGE |
| `infra/` | Local inference backend: BitNet submodule + bootstrap script |
| `KNOWLEDGE/` | Persistent reference material promoted from verified outputs |
| `MEMORY/` | Agent memory: context.md (state) + session logs |
| `output/` | All deliverables land here |
| `output/final/` | Approved, shipped deliverables |

## Quick Start

1. Copy this repo to your project root. Rename the folder to your project name (kebab-case).
2. Open `CLAUDE.md`. It works as-is. No edits required.
3. Open `agent-scaffold/agents/README.md`. Identify which of the 8 pre-built agents fit your use case.
4. `[PROJECT_ROOT]` in agent files is a runtime token. The agent resolves it automatically. Do not replace it manually.
5. To create a custom agent: copy `agent-scaffold/instructions.md` and `agent-scaffold/config.json`. Fill in the role and scope. Register across all 4 surfaces per `skills/skill-creation-guide.md` Step 4.
6. Add domain reference documents to `KNOWLEDGE/` per the promotion criteria in `KNOWLEDGE/README.md`.
7. If your first task type is unclear, open `.claude/framework-relationships.md`.
8. Run your first task through `CLAUDE.md` routing. Confirm output lands in `output/`.

## The 8 Agents

| Command | Agent | What It Does |
|---------|-------|--------------|
| `@researcher` | Research Agent | Gather, synthesise, and verify information |
| `@comms` | Comms Agent | Draft and validate communication output via FATE |
| `@decider` | Decision Agent | Structure decisions using OODA |
| `@reviewer` | Quality Reviewer | Run guardrails and evaluator. Returns pass or fail. |
| `@dmaic` | DMAIC Agent | Execute DMAIC loop for recurring process defects |
| `@project` | Project Agent | Execute 6-phase project lifecycle |
| `@6sigma` | Six Sigma Expert | Master Black Belt statistical and Lean depth |
| `@biz` | Business Architect | One-person AI business design, MVP scoping, agent stack planning |

## Local Inference (Zero Cost)

This template includes a local inference backend via [BitNet b1.58 2B4T](https://github.com/microsoft/BitNet).
Runs entirely on CPU. Uses 0.4GB RAM. Costs zero per token after setup.

```bash
# One-time setup
bash infra/bootstrap.sh
```

Every task routes through `skills/model-routing.md` first. Low and medium complexity tasks run locally.
High complexity tasks escalate to the configured frontier API.

## Core Principles

5 principles active on every task (`principles-core.md`):
- **Carbon Fiber**: Maximum strength, minimum weight.
- **YAGNI**: Add complexity only when requirements demand it.
- **AI-First**: Every output comprehensible in one context window.
- **Uncle Bob**: One function, one job, self-documenting.
- **No Em Dashes**: Banned in all output without exception.

8 extended principles for agent design and state-changing operations (`principles-extended.md`): One Source of Truth, Explicit Over Implicit, Reversibility First, Fail Loudly, Context Window Hygiene, Idempotency, Minimal Footprint, Observability.

## Version

Current: `1.1.0` — See `CHANGELOG.md` for full history.
