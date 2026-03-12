# Adoption Notes: Google AI Agents Guide → buenatura-template

**Ref:** `KNOWLEDGE/google-ai-agents-startup-guide.md`  
**Date:** 2026-03-12

Analysis of what maps to, extends, or challenges the current buenatura-template scaffold.

---

## Confirmed Alignments (already doing this)

- **Agent scaffold exists** (`agent-scaffold/`) — maps directly to Google's ADK agent structure (model + tools + orchestration)
- **Skills directory** (`skills/`) — aligns with Google's "tool layer": discrete, composable capabilities the agent can invoke
- **KNOWLEDGE + MEMORY directories** — maps to Google's memory architecture: KNOWLEDGE = long-term/RAG corpus, MEMORY = working/transactional state
- **Lean file structure** — consistent with Google's recommendation to start simple and layer complexity

---

## High-Value Adoptions (implement these)

### 1. Grounding Layer (RAG)
- **What:** Connect agent to KNOWLEDGE corpus via vector search so responses cite verified sources, not hallucinations
- **How:** Add a `skills/rag_query.py` skill that indexes KNOWLEDGE/ markdown files and retrieves relevant chunks before responding
- **Priority:** High — directly improves output quality for all agent tasks

### 2. AgentOps Pattern (Observability)
- **What:** Structured logging of agent reasoning steps, tool calls, and outcomes — not just final outputs
- **How:** Add `agent-scaffold/ops/` with a lightweight trace logger that writes JSONL to `output/traces/`
- **Priority:** High — enables debugging and quality improvement without heavy infra

### 3. Multi-Model Routing
- **What:** Route tasks by complexity: cheap/fast model for simple tasks, powerful model for reasoning
- **How:** Add a `agent-scaffold/router.py` that classifies task complexity and selects model accordingly
- **Priority:** Medium — meaningful cost + latency optimization as usage scales

### 4. MCP Protocol Support
- **What:** Model Context Protocol as standard interface for tool/skill invocation
- **How:** Ensure `skills/` follow MCP schema (name, description, input_schema, output_schema)
- **Priority:** Medium — future-proofs interoperability with external agents and orchestrators

### 5. Agent Identity File
- **What:** Google recommends defining agent identity explicitly: name, purpose, instructions, constraints
- **How:** Formalize `CLAUDE.md` (already present) as the canonical agent identity spec, ensure it covers persona + guardrails
- **Priority:** Low/Quick win — already partially done, just needs explicit identity sections

---

## Non-Adoptions (conscious decisions)

| Google Recommendation | Why We Skip |
|---|---|
| Vertex AI Agent Engine | Sovereign infra preference; local BitNet inference + Cloud Run is sufficient |
| Google Agentspace (no-code) | We are code-first by design |
| BigQuery for long-term memory | Overkill for current scale; flat KNOWLEDGE files + optional SQLite is sufficient |
| Gemini model family | Model-agnostic by design; BitNet + Ollama + API models via unified interface |

---

## Proposed Template Additions (action items)

```
agent-scaffold/
  ops/
    trace_logger.py       # JSONL trace writer for AgentOps pattern
    eval.py               # Simple outcome evaluator
  router.py               # Multi-model complexity router

skills/
  rag_query.py            # KNOWLEDGE/ corpus retrieval skill

KNOWLEDGE/
  (this file + source guide already added)
```

---

## Next Action

Implement `skills/rag_query.py` first — highest leverage, directly improves grounding for all agent tasks in any project bootstrapped from this template.
