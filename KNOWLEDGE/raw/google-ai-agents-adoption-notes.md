# Adoption Notes: Google AI Agents Guide -> buenatura-template

**Ref:** `raw/google-ai-agents-startup-guide.md`  
**Date:** 2026-03-12  
**Revised:** 2026-03-12 (corrected file paths and tool architecture after audit)

Analysis of what maps to, extends, or challenges the current buenatura-template scaffold.

---

## Confirmed Alignments (already doing this)

- **Agent scaffold exists** (`agent-scaffold/`) - maps directly to Google's ADK agent structure (model + tools + orchestration)
- **Skills directory** (`skills/`) - aligns with Google's tool layer: discrete, composable capabilities the agent can invoke
- **KNOWLEDGE + MEMORY directories** - maps to Google's memory architecture: KNOWLEDGE = long-term/RAG corpus, MEMORY = working/transactional state
- **Lean file structure** - consistent with Google's recommendation to start simple and layer complexity
- **Multi-model routing** - already implemented via `skills/model-routing.md` and `.claude/routing-table.md`

---

## High-Value Adoptions (implement these)

### 1. Grounding Layer (RAG)
- **What:** Semantic search across KNOWLEDGE/ corpus so the agent retrieves relevant chunks, not full files
- **How:** `tools/knowledge_search.py` (executable) + `skills/knowledge-search.md` (agent instruction)
- **Status:** Implemented in this commit
- **Priority:** High - directly improves token efficiency and grounding for all agent tasks

### 2. AgentOps Pattern (Observability)
- **What:** Structured JSONL logging of agent reasoning steps, tool calls, and outcomes
- **How:** Add `agent-scaffold/ops/trace_logger.py` writing to `output/traces/`
- **Status:** Pending
- **Priority:** High - enables debugging and continuous improvement without heavy infra

### 3. MCP Protocol Support
- **What:** Model Context Protocol as standard interface for tool/skill invocation
- **How:** Ensure `skills/` instruction files follow MCP schema (name, description, input_schema, output_schema)
- **Status:** Pending
- **Priority:** Medium - future-proofs interoperability with external agents and orchestrators

### 4. Agent Identity Hardening
- **What:** Explicit agent identity spec: name, purpose, instructions, constraints, persona, guardrails
- **How:** Extend `CLAUDE.md` with an identity block above the routing instructions
- **Status:** Partially done - CLAUDE.md exists but lacks explicit identity declaration
- **Priority:** Low / quick win

---

## Non-Adoptions (conscious decisions)

| Google Recommendation | Why We Skip |
|---|---|
| Vertex AI Agent Engine | Sovereign infra preference. Local BitNet + Cloud Run is sufficient. |
| Google Agentspace (no-code) | Code-first by design, always. |
| BigQuery for long-term memory | Overkill. Flat KNOWLEDGE files + SQLite index scales appropriately. |
| Gemini model family | Model-agnostic by design. BitNet, Ollama, and API models via unified interface. |

---

## Implemented File Structure

```
tools/
  knowledge_search.py       # Executable: sqlite-vec two-table RAG, incremental index

skills/
  knowledge-search.md       # Agent instruction: when and how to invoke the tool

KNOWLEDGE/
  .index/
    knowledge.db            # git-ignored, rebuilt by bootstrap.sh
    index_manifest.json     # committed, tracks file hashes

agent-scaffold/
  ops/
    trace_logger.py         # PENDING: JSONL trace writer for AgentOps pattern
```

---

## Next Action

Implement `agent-scaffold/ops/trace_logger.py` - next highest leverage item after RAG is live.
