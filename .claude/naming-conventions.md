# Naming Conventions

Applies to all files, folders, branches, agents, and skills in any project using this template.

---

## Files (Markdown, documents, outputs)

- Format: `YYYY-MM-DD-task-description-vN.md`
- Example: `2026-03-11-dmaic-defect-analysis-v1.md`
- Dates always ISO 8601: YYYY-MM-DD.
- Increment version on each revision: v1, v2, v3.
- Exceptions: `README.md`, `CLAUDE.md`, `CHANGELOG.md` (uppercase, no date prefix).

## Phase-Close Summary Files

Generated at the end of each DMAIC or Project Execution phase to preserve context before unloading.

- Format: `YYYY-MM-DD-[workflow]-[phase]-summary.md`
- Examples: `2026-03-11-dmaic-define-summary.md`, `2026-03-11-project-initiate-summary.md`
- Store in `output/` alongside the full phase output.
- These are not versioned. One summary per phase per run.

## Config and Data Files

- Format: `kebab-case.json` or `kebab-case.yaml`
- Example: `agent-config.json`, `workflow-settings.yaml`
- No version suffix needed unless multiple versions coexist.

## Skills Files

- Format: `kebab-case.md`
- Example: `research-workflow.md`, `veritas-verification.md`, `project-charter.md`
- Register every new skill in `skills/README.md` immediately after creation.
- Every skill file must start with YAML frontmatter (`name` and `description` fields).

## Folders

- Format: `kebab-case`
- Example: `project-alpha`, `client-onboarding`
- No spaces. No special characters.
- Uppercase exceptions (these exist in the template by default): `KNOWLEDGE`, `MEMORY`.
- Additional uppercase directories may be added per project convention but must be listed here.

## Branches

- Format: `feature/YYYY-MM-DD-task-name`
- Example: `feature/2026-03-11-add-dmaic-workflow`
- Hotfixes: `fix/YYYY-MM-DD-issue-description`

## Agents

- Format: `[capability]` in kebab-case. Prefer the shortest unambiguous capability noun.
- Example: `researcher`, `comms`, `decider`, `reviewer`, `dmaic`, `project`, `6sigma`
- Each agent requires two files: `[name].md` (instructions) and `[name].json` (config).
- Register every new agent in `agent-scaffold/agents/README.md` and `.claude/routing-table.md`.
- Do not use the `-agent` suffix. It is redundant. The directory already scopes the files as agents.
