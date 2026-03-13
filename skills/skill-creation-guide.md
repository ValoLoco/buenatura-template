---
name: skill-creation-guide
description: Step-by-step process for building a new skill file when no internal or skills.sh skill covers the need.
---

# Skill Creation Guide

Use this when no internal skill and no skills.sh skill covers your need.

---

## Step 1: Define the Skill

- Name: one clear capability (e.g., `contract-review`).
- Trigger condition: when exactly should this skill be loaded?
- Input: what does it need to function?
- Output: what does it produce?

---

## Step 2: Add YAML Frontmatter (Required)

Every skill file must begin with YAML frontmatter for auto-discovery by Claude agents.
Without this, the skill cannot be auto-loaded.

```
---
name: [kebab-case-skill-name]
description: [one sentence. No more.]
---
```

Rules:
- `name`: kebab-case, unique within the project, matches the filename.
- `description`: one sentence summary of what the skill does. No em dashes.

---

## Step 3: Write the Skill File

Structure (after the frontmatter):

```
# [Skill Name]

[One-sentence purpose.]

## Trigger Conditions
[When exactly to load this skill.]

## Steps
1. ...
2. ...

## Rules
- ...

## Handoffs
[Where to escalate if scope is exceeded. Reference specific agents by @command.]

## Output
[Format and file location. Follow global naming: output/YYYY-MM-DD-[task-subtype]-vN.md]

## Verification
[3-test protocol: happy path, edge case, error case. Score >= 0.85 with evaluator.md before marking production-ready.]
```

Keep the file under 500 lines. If it grows beyond that, split into a main file and referenced sub-files.

---

## Step 4: Register (All 4 Surfaces Required)

A skill is not registered until all four surfaces are updated. Incomplete registration is a High-severity defect per guardrails.md Gate 5.

```
Registration Checklist:
[ ] skills/README.md              Add row: name, file path, load condition.
[ ] .claude/routing-table.md      Add row in Task Routing table + row in Agent Registry if a new agent was created.
[ ] agent-scaffold/agents/        If an agent was created: both [name].md AND [name].json must be present.
[ ] MEMORY/context.md             Add a row to the Past Decisions table: date, agent, decision, rationale.
```

Do not mark the skill as ready until all four checkboxes are ticked.

---

## Step 5: Test and Evaluate

Run the skill on at least 3 sample tasks before marking it ready:
- Happy path: normal expected input.
- Edge case: unusual but valid input.
- Error case: invalid or incomplete input.

Score with `.claude/evaluator.md`. Must reach 0.85 aggregate on all three tests.
If any test scores < 0.85: iterate via `workflows/iteration-loop.md` and re-test before marking ready.

---

## Step 6: Contribute Back

If the skill is generic and useful beyond this project, submit to https://skills.sh.
