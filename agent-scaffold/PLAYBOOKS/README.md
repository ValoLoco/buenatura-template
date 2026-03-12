# Playbooks

Store step-by-step procedures for recurring tasks here.
A Playbook answers: **how do I do X?**

---

## Playbooks vs Templates

| | Playbook | Template |
|-|----------|----------|
| Question answered | How do I do X? | What should X look like? |
| Content | Numbered steps, decision points, tools to use | Structure, headers, placeholder fields |
| Example | How to onboard a new client | New client onboarding brief format |
| Lives in | `PLAYBOOKS/` | `TEMPLATES/` |

---

## Index

| File | Purpose | Trigger |
|------|---------|---------|
| (none yet) | | |

Add a row for every new playbook.

---

## Playbook Format

```
# [Playbook Name]

Trigger: [When exactly to use this playbook]
Inputs: [What is needed to start]
Owner: [Who runs this]

## Steps
1. [Action]
2. [Action]
   - Decision point: if X then Y, if not then Z.
3. [Action]

## Output
[What this playbook produces and where it goes]

## Done When
[Clear completion criteria]
```
