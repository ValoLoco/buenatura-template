# Default Agent Roster

This directory contains the 8 default agents for this template.
Each agent has two files: `[name].md` (instructions) and `[name].json` (config).

---

## Quick Start

1. Identify which agent matches your task (see roster below).
2. The `[PROJECT_ROOT]` token in each agent file is resolved at runtime by the agent. You do not replace it manually. It refers to the root of the directory where this template lives on your machine.
3. Invoke the agent with its `@command` in your AI interface.
4. The agent loads its own files. You do not need to load anything manually.

To create a new agent: copy `agent-scaffold/instructions.md` and `agent-scaffold/config.json`, fill in the placeholders, and register it across all 4 surfaces (see `skills/skill-creation-guide.md` Step 4).

---

## Roster

| Command | Agent | Type | Single Responsibility |
|---------|-------|------|----------------------|
| `@researcher` | Research Agent | Flat specialist | Gather, synthesise, verify information. |
| `@comms` | Comms Agent | Flat specialist | Draft and validate communication output. |
| `@decider` | Decision Agent | Flat specialist | Structure decisions using OODA. |
| `@reviewer` | Quality Reviewer | Flat specialist | Run guardrails + evaluator. Returns pass/fail. |
| `@dmaic` | DMAIC Agent | Phase coordinator | Execute DMAIC loop. Delegates to phase skills. |
| `@project` | Project Agent | Phase coordinator | Execute 6-phase project lifecycle. |
| `@6sigma` | Six Sigma Expert | Domain expert | Master Black Belt statistical and Lean depth. |
| `@biz` | Business Architect | Domain expert | One-person AI business design, MVP scoping, and agent stack planning. |

---

## When to Use Which Agent

- **Research question or fact-finding**: `@researcher`
- **Writing a message, pitch, or negotiation**: `@comms`
- **Choosing between options or paths**: `@decider`
- **Checking if output is ready to ship**: `@reviewer`
- **Running a process improvement project**: `@dmaic`
- **Running a full multi-phase project**: `@project`
- **Deep statistical or Lean analysis**: `@6sigma`
- **Building or scaling a one-person AI business**: `@biz`

If no agent fits: route via `CLAUDE.md` directly.

---

## Architecture Decision

This roster is flat by design. CLAUDE.md is the router. No CSuite hierarchy layer exists.
Add a coordinator layer only when two or more agents are regularly delegating to each other in ways that create ambiguity. Not before.

---

## Principles Applied

- Each agent does one thing (Principle 4: Uncle Bob).
- Each agent loads only what its role requires (Principle 12: Minimal Footprint).
- No agent duplicates logic from another (Principle 6: One Source of Truth).
- Every agent escalates rather than guesses (Principle 9: Fail Loudly).
