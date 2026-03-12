---
name: research-workflow
description: Structured context-first research process with VERITAS verification as a mandatory gate between search and synthesis.
---

# Research Workflow Skill

A structured, context-first research process for any topic.
VERITAS verification is a mandatory gate between search and synthesis.

---

## Steps

### 1. Define Scope

- State the specific research question in one sentence.
- Define explicit out-of-scope boundaries.
- Identify the minimum viable answer: what does done look like?

### 2. Check Context First

- Read all available project context files before searching externally.
- Check `KNOWLEDGE/` and `MEMORY/context.md` for this agent.
- If the answer exists in context: use it. Do not search unnecessarily.

### 3. Search (in this order)

1. Internal repo and project files.
2. Web search (primary sources preferred over summaries).
3. skills.sh for methodology or process questions.

What a good search looks like:
- Use specific, narrow queries. Avoid broad terms.
- Search for the source, not the summary (e.g., original paper, not a blog about it).
- Run at least 2 independent searches on different angles of the question.
- Stop when 2+ independent sources agree, or when diminishing returns are clear.

### 4. Verify with VERITAS (mandatory gate)

Before synthesizing anything, apply `skills/veritas-verification.md` to every source found.

Run each source through the 7 VERITAS lenses:
- V: Is this source credible and current?
- E: Does the evidence directly support the claim?
- R: Is the reasoning sound?
- I: Does this serve the research intent?
- T: Is this factually accurate with no selective omission?
- A: Does it conflict with other sources? If yes, flag explicitly.
- S: Does it contribute to a coherent synthesis?

Discard sources that fail V, E, or T.
Flag sources that fail A (conflicting data). Include both sides in the output.

### 5. Synthesize

- Extract only the key insights that answer the research question.
- Cite every claim inline.
- Surface conflicting data explicitly. Do not hide disagreement.
- State uncertainty where it exists. Never fill gaps with assumptions.

### 6. Output

Write findings to `output/YYYY-MM-DD-research-[topic]-v1.md`.

---

## Rules

- No speculation. Every claim needs a source.
- Prefer primary sources over summaries.
- Conflicting data must be surfaced, not resolved by omission.
- If uncertain: state it. Uncertainty is data.

---

## Good Research Output Includes

- [ ] Research question restated at the top.
- [ ] Scope and out-of-scope stated.
- [ ] At least 2 independent sources per key claim.
- [ ] All sources VERITAS-verified (checklist run).
- [ ] Conflicting data flagged if found.
- [ ] Uncertainty statements where applicable.
- [ ] Synthesis section: key insights only, no raw data dump.
- [ ] All claims cited inline.
