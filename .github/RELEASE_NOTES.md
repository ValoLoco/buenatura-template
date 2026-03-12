# Release Notes

## v1.1.0 — 2026-03-12

Full DMAIC audit sync from source repo. 15 defects resolved across 3 passes.

### Added
- 8-agent roster (researcher, comms, decider, reviewer, dmaic, project, 6sigma, @biz)
- All 8 agent JSON configs with version history
- `skills/business-architect.md`: one-person AI business design (6 phases, $0 to $10M+)
- `agent-scaffold/PLAYBOOKS/`, `TEMPLATES/`, `MEMORY/`, `KNOWLEDGE/` scaffold directories
- `agent-scaffold/agents/README.md` with When-to-Use routing guide

### Changed
- `README.md`: rewritten with full 8-agent table and updated Quick Start
- `skills/skill-creation-guide.md`: Step 4 now enforces all 4 registration surfaces
- `VERSION`: 1.0.0 to 1.1.0
- `CHANGELOG.md`: v1.1.0 entry with root cause analysis

### Root Cause (all 15 defects)
Two patterns: deferred descriptor sync and incomplete registration standard.
Both resolved. Gate 5 Rule A now covers these classes going forward.

---

## v1.0.0 — 2026-03-11

Initial release. Full agent scaffold, skills, workflows, .claude config, local inference backend.
