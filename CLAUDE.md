# AI Router: Progressive Disclosure Context Manager

Your role: Read this file first. Route to exactly the files you need. Skip everything else.
This file contains only pointers. No content lives here.

---

## Global Rules (Always Active)

1. All 5 core principles in `.claude/principles-core.md` are active for every task. Load that file now.
2. For agent design, system-level tasks, or any task that writes, deletes, or publishes state: also load `.claude/principles-extended.md` (Principles 6-13).
3. Naming convention: `YYYY-MM-DD-task-description-vN.md`, kebab-case folders.
4. All work-in-progress output goes to `output/`.
5. All final approved output goes to `output/final/`.
6. When any infrastructure file changes (skills, agents, workflows, routing): update `CLAUDE.md` and `.claude/routing-table.md` in the same commit. No deferred hygiene.

---

## Step 0: Inference Gate (Before Every LLM Call)

Load `skills/model-routing.md`. Score the task on 4 dimensions. Route to local or API.
Do not make any LLM call before this step is complete.
Requires `infra/bootstrap.sh` to have been run once on this machine.

---

## Step 1: Identify Your Task Type

Open `.claude/routing-table.md`.
Find your task row. Load only the files listed. Skip all others.

If no row matches your task: load `.claude/skills-protocol.md`. Do not guess a route.

---

## Step 2: Execute

Follow the loaded workflow or skill file instructions precisely.

---

## Step 3: Validate Before Delivery

1. Load `.claude/guardrails.md`. All 5 gates must pass.
2. Load `.claude/evaluator.md`. Aggregate score must be >= 0.85.
3. If either fails: load `workflows/iteration-loop.md` and revise.
4. On pass: move output to `output/final/YYYY-MM-DD-task-final.md`.

---

## Skills Protocol

No fitting internal skill? Load `.claude/skills-protocol.md`.
Search https://skills.sh before building anything bespoke.

---

## Escalation

After 3 revisions without improvement: stop and flag for human review.
Write escalation row to `MEMORY/context.md` Past Decisions table. Halt.
