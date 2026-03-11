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

## Steps
1. ...
2. ...

## Rules
- ...

## Output
[Format and file location.]
```

Keep the file under 500 lines. If it grows beyond that, split into a main file and referenced sub-files.

---

## Step 4: Register

Add to `skills/README.md` with: name, file path, and load condition.
Add a routing table entry in `.claude/routing-table.md`.

---

## Step 5: Test and Evaluate

Run the skill on at least 3 sample tasks before marking it ready:
- Happy path: normal expected input.
- Edge case: unusual but valid input.
- Error case: invalid or incomplete input.

Score with `.claude/evaluator.md`. Must reach 0.85 aggregate on all three tests.

---

## Step 6: Contribute Back

If the skill is generic and useful beyond this project, submit to https://skills.sh.
