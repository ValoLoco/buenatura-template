# Skills Protocol

Use this when no routing table entry covers your task, or when a task requires a capability not yet defined.

---

## Step 1: Check Internal Skills

Open `skills/README.md`.
Is there an internal skill that fits?
- Yes: load it and follow its instructions exactly.
- No: go to Step 2.

---

## Step 2: Search skills.sh

Visit https://skills.sh: the open agent skills directory maintained by Vercel.
Search for the capability you need.

Examples of available skills:
- `copywriting`: persuasive content generation
- `code-reviewer`: automated code review checklist
- `data-analysis`: structured data reasoning
- `pdf`: PDF reading and extraction
- `content-strategy`: content planning and calendars

**How to install a skill from skills.sh:**

Option A: Manual copy (no tools required)
1. Open the skill page on skills.sh.
2. Copy the skill file content.
3. Save it to `skills/[skill-name].md` in this project.
4. Add it to `skills/README.md` with its load condition.

Option B: Via MCP tool (if MCP is configured)
1. Use the `load_skill` MCP tool with the exact skill name.
2. The skill file is injected into context automatically.
3. No manual copy needed.

Option C: CLI or VS Code Extension (recommended if available)
1. Install the skills.sh VS Code extension from the marketplace, or the CLI.
2. Run `skills install [skill-name]`.
3. Skill is downloaded to `skills/` and registered automatically.

Not sure which option applies? Use Option A. It always works.

---

## Step 3: Build a New Skill

No internal skill and nothing on skills.sh fits? Follow `skills/skill-creation-guide.md`.

New skills must:
- Do one thing well (single responsibility).
- Start with YAML frontmatter (name and description).
- Include a routing table entry in `skills/README.md`.
- Be testable in isolation against sample inputs.
- Pass the evaluator at >= 0.85 before use.

---

## Step 4: Contribute Back

If the new skill is generic and useful beyond this project, submit it to https://skills.sh.
This keeps the ecosystem healthy and reduces future build cost.
