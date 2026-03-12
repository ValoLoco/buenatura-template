# Templates

Store reusable output formats here.
A Template answers: **what should X look like?**

---

## Playbooks vs Templates

| | Template | Playbook |
|-|----------|----------|
| Question answered | What should X look like? | How do I do X? |
| Content | Structure, headers, placeholder fields | Numbered steps, decision points |
| Example | New client onboarding brief format | How to onboard a new client |
| Lives in | `TEMPLATES/` | `PLAYBOOKS/` |

---

## Index

| File | Output Type | Use When |
|------|-------------|----------|
| (none yet) | | |

Add a row for every new template.

---

## Template Format

```
# [Template Name]

Use when: [Specific situation this template serves]
Produces: [What kind of output]

---

## [Section 1 Header]

[FILL IN: description of what goes here]

## [Section 2 Header]

[FILL IN: description of what goes here]

---

Output to: output/YYYY-MM-DD-[task]-v1.md
```
