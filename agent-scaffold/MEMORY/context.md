# Agent Memory

Store agent-specific working context, preferences, and accumulated learnings here.
Update this file after every project close (Phase 6 of `project-execution.md`).
Update Active Projects at the start and end of every session.

---

## Active Projects

Log current in-progress work so context can be resumed after a session ends.

| Project | Phase | Last Action | Next Action | Updated |
|---------|-------|-------------|-------------|---------|
| buenatura-template v1.2.0 | Control (closed) | Full framework sync + registration fixes complete | Run DMAIC again at next session start to catch new drift | 2026-03-13 |

Remove a row when the project reaches Phase 6 (Close).

---

## Working Preferences

Document stable preferences for this agent. Update only when a preference changes.

- Tone: Direct, concise, no filler sentences.
- Output format: Tables for comparisons, numbered lists for steps, paragraphs for context.
- Depth: Diagnosis first, then recommendations, then next steps. No summaries.
- Language: English only.
- Em dashes: Banned. Use period, comma, colon, or parentheses instead.

---

## Past Decisions

Log key decisions so rationale is preserved across sessions.
Format: one row per decision. Do not edit past rows. Append only.

| Date | Decision | Rationale | Outcome |
|------|----------|-----------|---------|
| 2026-03-12 | Split principles into core (1-5) and extended (6-13) | Core loads on every task. Extended loads only for agent design and state-changing tasks. Reduces context window waste. | Implemented in `.claude/principles-core.md` and `.claude/principles-extended.md`. |
| 2026-03-12 | Add `@biz` Business Architect agent | One-person AI business design needed as a distinct capability. Separate from `@project` (lifecycle) and `@dmaic` (defects). | Implemented. Registered in routing-table, framework-relationships, agents/README.md. |
| 2026-03-12 | Add RAG layer via `tools/knowledge_search.py` | Loading full KNOWLEDGE/ files on every task wastes context window. Semantic search returns only relevant chunks. | Implemented. Skill registered in `skills/knowledge-search.md` and routing-table. |
| 2026-03-12 | Add AgentOps observability via `agent-scaffold/ops/` | Principle 13 (Observability) requires every significant action to leave a trace. JSONL traces enable daily eval. | Implemented. Skill registered in `skills/agentops.md` and routing-table. |
| 2026-03-13 | Adopt file-by-file push protocol for cross-repo sync | Batch pushes caused timeout failures. Single-file commits are atomic, recoverable, and timeout-safe. | Adopted. Used for entire v1.2.0 sync session. |

---

## Lessons Learned

Log what worked and what did not. Append only. Never delete.

| Date | Lesson | Context | Action Taken |
|------|--------|---------|-------------|
| 2026-03-13 | Template completeness must be verified at session start with a cross-repo diff check, not assumed. | v1.2.0 DMAIC cycle opened finding 35% completeness despite v1.1.0 appearing complete. | Added control measure to CHANGELOG v1.2.0. Run DMAIC at session start going forward. |
| 2026-03-13 | skills/README.md and routing-table.md drift silently when new skills are added without running 4-surface registration. | `knowledge-search`, `agentops`, `veritas-verification`, `business-architect`, `skill-creation-guide` all unregistered despite files existing. | Patched both files. Updated `skill-creation-guide.md` Step 4 in v1.1.0 to enforce 4-surface rule. |
| 2026-03-13 | VERSION file must be bumped as part of every CHANGELOG entry, not as a separate task. | VERSION still read 1.1.0 after CHANGELOG was updated to 1.2.0. | Bumped to 1.2.0. Add VERSION bump to CHANGELOG update checklist. |
