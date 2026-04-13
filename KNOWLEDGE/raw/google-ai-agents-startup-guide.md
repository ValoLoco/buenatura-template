# Google Startup Technical Guide: AI Agents

**Source:** https://services.google.com/fh/files/misc/startup_technical_guide_ai_agents_final.pdf  
**Publisher:** Google Cloud  
**Pages:** 64  
**Added:** 2026-03-12

## Summary

Google's definitive 64-page playbook for startups building production-grade AI agents. Covers the full journey from concept to scaled deployment using Google Cloud's stack (Vertex AI, Gemini, ADK).

## Three-Part Structure

### Section 1: Core Concepts
- AI agents = LLM + tools + memory + orchestration + runtime
- Move from "ask a question" to "set a goal, let the agent orchestrate steps"
- Five layers every agent needs: Model, Tools, Memory, Orchestration, Runtime
- Model tiers: Gemini 2.5 Flash-Lite (fast/cheap) → Flash (balanced) → Pro (complex reasoning)
- Multi-agent systems: light models handle routine, heavy models handle complex reasoning

### Section 2: Building
- **No-code path:** Google Agentspace (manage AI workforces without code)
- **Code-first path:** Agent Development Kit (ADK) — supports multi-agent, MCP, A2A protocols
- Grounding techniques: RAG → GraphRAG → Agentic RAG (agent reasons about *how* to find data)
- Vector databases (Vertex AI Search) prevent hallucination
- Memory layers: working (in-context), transactional (Firestore), long-term (BigQuery)

### Section 3: Scaling to Production
- AgentOps = DevOps for agents: monitor drift, audit reasoning, evaluate outcomes
- Agent Starter Pack: pre-built infra with CI/CD + monitoring out-of-the-box
- Deploy via: Vertex AI Agent Engine (memory + lifecycle) or Cloud Run (containerized)
- Responsible AI: safety, compliance, reasoning auditability

## Key Principles

| Goal | Best Approach |
|---|---|
| Intelligent workflows | ADK + ReAct orchestration |
| Factual accuracy | RAG / GraphRAG grounding |
| Automate external actions | API/tool integrations |
| Scale reliably | Vertex AI Agent Engine / Cloud Run |
| Persistent memory | Firestore + BigQuery + Memorystore |
| Multi-agent communication | MCP + A2A protocols |
| Production reliability | AgentOps monitoring |

## Most Practical Chapters

Per community consensus: **Chapters 7, 8, 9, and 41** are highest signal for implementation.

## BUENATURA Adoption Notes

See `wiki/google-ai-agents-adoption-notes.md` for mapped adoption recommendations against the buenatura-template scaffold.
