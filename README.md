# BUENATURA AI Agent Template

A lean, sovereign scaffold for AI-driven projects, agents, and workflows.
Built on 13 principles. Optimised for one-person and small-team operations.
Every file has a purpose. No bloat.

## 🚀 Quick Start – Free in GitHub Codespaces (NemoClaw + Nemotron)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ValoLoco/buenatura-template)

1. Click the button above (or **Code → Codespaces → Create codespace on main**)
2. Get a free `NIM_API_KEY` at [build.nvidia.com](https://build.nvidia.com)
3. Run this one-liner:
   ```bash
   curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
   ```
4. Run `nemoclaw onboard` and complete the quick wizard
5. Start with `CLAUDE.md` — your agent router is ready

> NemoClaw is alpha software (March 2026). The template works perfectly without it — this is optional.

## What Is Here

| Folder | Purpose |
|--------|---------|
| `.claude/` | Core rules: routing, guardrails, evaluator, principles, naming conventions, session log, self-extension protocol |
| `workflows/` | Process definitions: DMAIC, OODA, FATE, project lifecycle, iteration loop |
| `skills/` | Reusable behaviour modules: knowledge search (RAG), research, verification, FMEA, control plan, business design, AgentOps |
| `tools/` | Executable Python tools: `knowledge_search.py` (semantic search over KNOWLEDGE/) |
| `agent-scaffold/` | Blank agent template + 8 ready-to-use agents + ops (AgentOps), PLAYBOOKS, TEMPLATES, MEMORY, KNOWLEDGE |
| `infra/` | Local inference backend: BitNet submodule + bootstrap script |
| `KNOWLEDGE/` | Persistent reference material: `raw/` (sources), `wiki/` (LLM-maintained pages), `index.md`, `log.md` |
| `MEMORY/` | Agent memory: context.md (state) + session logs |
| `output/` | All deliverables land here |
| `output/final/` | Approved, shipped deliverables |

## Quick Start

1. Copy this repo to your project root. Rename the folder to your project name (kebab-case).
2. Open `CLAUDE.md`. It works as-is. No edits required.
3. Open `agent-scaffold/agents/README.md`. Identify which of the 8 pre-built agents fit your use case.
4. `[PROJECT_ROOT]` in agent files is a runtime token. The agent resolves it automatically. Do not replace it manually.
5. To create a custom agent: copy `agent-scaffold/instructions.md` and `agent-scaffold/config.json`. Fill in the role and scope. Register across all 4 surfaces per `skills/skill-creation-guide.md` Step 4.
6. Add domain reference documents to `KNOWLEDGE/raw/` and tell the agent to ingest them.
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

## Knowledge Management (LLM Wiki)

`KNOWLEDGE/` follows a three-layer wiki pattern. The LLM builds and maintains a persistent, interlinked knowledge base. Not a raw retrieval index.

**Three layers:**
- `KNOWLEDGE/raw/` — immutable source documents. Drop files here. Never edited.
- `KNOWLEDGE/wiki/` — LLM-maintained markdown pages: summaries, entity pages, concept pages, cross-references.
- `KNOWLEDGE/index.md` — catalog of all wiki pages with one-line summaries, organized by category.
- `KNOWLEDGE/log.md` — append-only timeline of every ingest, query, and lint pass.

**How to use:**

1. Drop a source file (`.md`, `.txt`, `.pdf` text export) into `KNOWLEDGE/raw/`.
2. Tell the agent: `Ingest KNOWLEDGE/raw/your-file.md`
3. The agent reads it, writes a summary wiki page, updates up to 15 existing pages, updates `index.md` and `log.md`.
4. Ask questions: `Query: what do we know about X?` — the agent reads the index, loads relevant pages, and synthesizes an answer. Good answers are filed back into the wiki automatically.
5. Periodically: `Lint the wiki` — the agent checks for contradictions, orphan pages, and stale claims.

This is tool-agnostic. Any LLM that can read and write Markdown files runs this workflow.
See `CLAUDE.md → LLM Wiki Workflow` for the full operation spec.

## Local Inference (Zero Cost)

This template includes a local inference backend via [BitNet b1.58 2B4T](https://github.com/microsoft/BitNet).
Runs entirely on CPU. Uses 0.4GB RAM. Costs zero per token after setup.

```bash
# One-time setup
bash infra/bootstrap.sh
```

Every task routes through `skills/model-routing.md` first. Low and medium complexity tasks run locally.
High complexity tasks escalate to the configured frontier API.

## RAG: Semantic Knowledge Search

The `tools/knowledge_search.py` tool indexes all `.md` files in `KNOWLEDGE/` and returns semantically relevant chunks for any query.
Load `skills/knowledge-search.md` before accessing `KNOWLEDGE/` directly. Context window stays lean.

```bash
python tools/knowledge_search.py "your query" --top-k 5
```

## AgentOps: Built-in Observability

Every agent task can be instrumented with `agent-scaffold/ops/trace_logger.py`.
One JSONL trace file per day at `output/traces/YYYY-MM-DD.jsonl`.
Review daily performance with `python agent-scaffold/ops/eval.py`.
Load `skills/agentops.md` for the full instrumentation guide.

## Core Principles

5 principles active on every task (`principles-core.md`):
- **Carbon Fiber**: Maximum strength, minimum weight.
- **YAGNI**: Add complexity only when requirements demand it.
- **AI-First**: Every output comprehensible in one context window.
- **Uncle Bob**: One function, one job, self-documenting.
- **No Em Dashes**: Banned in all output without exception.

8 extended principles for agent design and state-changing operations (`principles-extended.md`): One Source of Truth, Explicit Over Implicit, Reversibility First, Fail Loudly, Context Window Hygiene, Idempotency, Minimal Footprint, Observability.

## Version

Current: `1.2.0` — See `CHANGELOG.md` for full history.
