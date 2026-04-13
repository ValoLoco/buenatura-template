---
title: "Google Startup Technical Guide: AI Agents"
type: source
sources: ["raw/google-ai-agents-startup-guide.md"]
updated: 2026-04-13
---

# Google Startup Technical Guide: AI Agents

Google Cloud's 64-page playbook for building production-grade AI agents, covering the full stack from concept to deployment.

## Overview

Published by Google Cloud. Structured in three parts: core concepts, building, and scaling to production. Targets startups using Google's stack (Vertex AI, Gemini, ADK) but contains tool-agnostic architecture principles.

## Key Points

- Every agent needs five layers: Model, Tools, Memory, Orchestration, Runtime
- Memory has three tiers: working (in-context), transactional (Firestore), long-term (BigQuery)
- Grounding progression: RAG → GraphRAG → Agentic RAG
- AgentOps = DevOps applied to agents: monitor drift, audit reasoning, evaluate outcomes
- Two deployment paths: Vertex AI Agent Engine or Cloud Run

## Connections

- Related: [[google-ai-agents-adoption-notes]] — BUENATURA-specific adoption analysis

## Open Questions

- How does Agentic RAG map to the current `tools/knowledge_search.py` implementation?
