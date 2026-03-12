# Self-Extension Protocol

This protocol governs how the template identifies its own gaps and proposes improvements between sessions.
It is the implementation of Principle 9 (Fail Loudly) at the system level.

Any agent or human using this template can trigger this protocol when a gap is found.

---

## When to Trigger

Trigger this protocol when:
- A routing table row is missing for a real task that arrived.
- A skill is referenced in a workflow but does not exist in `skills/`.
- A phase gate cannot pass because a required file is absent.
- The same workaround has been applied more than twice in one session.
- A session-log Self-Extension Flag is marked High priority.

---

## Step 1: Classify the Gap

Assign the gap to one of four types:

| Type | Description | Fix Location |
|------|-------------|-------------|
| Missing skill | A capability needed but no skill file exists | `skills/` |
| Missing workflow | A process needed but no workflow file exists | `workflows/` |
| Broken reference | A file points to something that does not exist | The file containing the broken pointer |
| Routing gap | A task type has no routing table entry | `.claude/routing-table.md` |

---

## Step 2: Write a Gap Record

Before fixing, write a one-row entry to the session log Self-Extension Flags table.
Fields: Type, Location, Description, Proposed Fix, Priority.

Do not skip this step. The log is the only record that a gap was found. Without it, the gap will be rediscovered.

---

## Step 3: Fix

Fix rules by type:

**Missing skill:**
1. Check skills.sh for an existing skill before building.
2. If found: install per `.claude/skills-protocol.md` Option A or B.
3. If not found: build per `skills/skill-creation-guide.md`.
4. Register across all 4 surfaces per `skills/skill-creation-guide.md` Step 4.

**Missing workflow:**
1. Check if an existing workflow can be extended rather than creating a new file. Prefer extension.
2. If a new file is needed: use this structure (same as all workflow files):
   - H1 title describing the workflow purpose.
   - One-sentence purpose statement immediately below the title.
   - Numbered phases or steps, each with: Goal, bullet-list instructions, Phase Gate checklist, Output path.
   - No YAML frontmatter (workflows are not skills).
3. Register in `.claude/routing-table.md` and `.claude/framework-relationships.md`.

**Broken reference:**
1. Identify the correct target (the file that should exist or should be pointed to).
2. Update the pointer. Do not create a duplicate file to satisfy the broken reference.

**Routing gap:**
1. Add a row to `.claude/routing-table.md`.
2. Update `.claude/framework-relationships.md` if the gap involves a new framework.

---

## Step 4: Verify

- [ ] Gap is no longer reproducible.
- [ ] No new broken references introduced by the fix.
- [ ] Session log updated with fix outcome.
- [ ] If the fix involved a new skill or workflow: run it on 1 sample task before marking complete.

---

## Step 5: Prevent Recurrence

After fixing, ask: what guardrail would have caught this before it became a gap?
If one can be added without bloat: add it to `.claude/guardrails.md` or `skills/skill-creation-guide.md`.
If the fix is a pattern worth sharing: submit the skill to https://skills.sh.
