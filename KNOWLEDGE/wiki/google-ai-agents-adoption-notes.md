---
title: "Google AI Agents: BUENATURA Adoption Notes"
type: overview
sources: ["raw/google-ai-agents-adoption-notes.md"]
updated: 2026-04-13
---

# Google AI Agents: BUENATURA Adoption Notes

Analysis of the Google AI Agents Startup Guide mapped against the buenatura-template scaffold.

## Overview

Four patterns from the Google guide were evaluated for adoption. Two are already aligned. Of the four high-value adoptions identified, one (RAG grounding layer) is implemented. Three remain pending.

## Key Points

- buenatura-template already aligns with Google's agent structure: `agent-scaffold/`, `skills/`, `KNOWLEDGE/`, `MEMORY/`
- RAG grounding via `tools/knowledge_search.py` is live
- AgentOps trace logger is pending (next highest leverage item)
- MCP protocol support is pending (medium priority)
- Google-specific infrastructure (Vertex AI, BigQuery, Gemini) is consciously skipped in favour of sovereign, model-agnostic stack

## Connections

- Related: [[google-ai-agents-startup-guide]] — source document this analysis is based on

## Open Questions

- When should `agent-scaffold/ops/trace_logger.py` be prioritised relative to MCP support?
