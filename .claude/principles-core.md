---
name: principles-core
description: The 5 universal principles loaded on every session start. Apply to all output types without exception.
---

# Principles: Core

Load this on every session start. These 5 principles apply to all output: code, content, strategy, research, agent design.

For the full 13-principle set, load `principles-extended.md` (required for agent design and complex multi-phase tasks).

---

## 1. Carbon Fiber Principle

Maximum strength with minimum weight.
Every line, every word, every file, every folder must earn its place.
If you cannot explain why it exists, remove it.

- Code: no dead code, no over-engineering.
- Content: no filler sentences, no redundant sections.
- Process: no steps that do not move the outcome forward.

## 2. YAGNI (You Aren't Gonna Need It)

Start simple. Add complexity only when concrete requirements demand it.
Do not build for imaginary future needs.

- Code: no speculative abstractions or premature generalization.
- Process: no workflows for problems that do not yet exist.
- Content: no sections covering every possible edge case unprompted.

## 3. AI-First Development

All output must be instantly comprehensible to both humans and AI within standard context windows.
Avoid abstractions that require loading additional context to understand.

- Code: self-documenting names, single-responsibility functions.
- Files: each file must make sense on its own.
- Instructions: one clear action per step.

## 4. Uncle Bob's Clean Code

Functions do one thing and do it well.
Code reads like well-written prose. Names are self-documenting.
Comments explain why, not what.

- Content: one idea per paragraph. Headers are signposts, not summaries.
- Process: one responsibility per agent, one purpose per file.

## 5. No Em Dashes

Em dashes (the character: —) are banned in all output without exception.
Applies to code comments, documentation, content, strategies, and agent instructions.

Use instead: a period, a comma, a colon, or parentheses.

Wrong: "This is the output — it must be clean."
Right: "This is the output. It must be clean."

If you generate an em dash in any output: revise before delivery. No exceptions.
