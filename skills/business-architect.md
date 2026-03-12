---
name: business-architect
description: Guides a one-person business from zero to $10M+ by extracting workflows, enforcing minimum viable scope, and stacking AI agents at each revenue tier.
---

# Business Architect Skill

Operating principle: complexity kills more businesses than competition. Every decision defaults to the simplest version that solves the core problem.

---

## Trigger Conditions

Load this skill when the task involves any of the following:
- Identifying a market opportunity or validating a business idea
- Designing or scoping an MVP product or service
- Building automated operational systems (onboarding, finance, support)
- Deciding whether to add a new feature or workflow
- Planning a growth stage transition ($0-100K, $100K-$1M, $1M-$10M+)

---

## Phase Map

| Phase | Name | Core Output |
|-------|------|-------------|
| 1 | Market and Pain Identification | Validated painkiller problem in a growing market |
| 2 | Discovery Interviews | 10 customer conversations. Design specs from their words, not assumptions. |
| 3 | Manual Execution | Problem solved by hand. Five-Part Offer drafted. |
| 4 | Clickable Prototype | Wizard-of-Oz mock-up. 5-call reaction test recorded. |
| 5 | MVP Build | Core-only app. Single prompt to generate. No admin dashboards. |
| 6 | AI Agent Stack | Automated loops replace manual tasks tier by tier. |

---

## Steps

### Step 1: Market and Pain Scan
1. Identify 3 growing markets relevant to the founder's background.
2. For each market, list the top 3 problems customers pay to solve today.
3. Apply painkiller filter: reject anything described as "nice to have" or "would be interesting."
4. Output: one ranked market-problem pair with evidence (spend data or customer quote).

### Step 2: Discovery Interview Design
1. Draft outreach message framed as asking for advice, not pitching.
2. Prepare 5 open questions focused on workflow pain, current workarounds, and spend.
3. Target minimum 10 conversations before writing any spec.
4. After each call, extract: problem statement, current solution, willingness to pay signal.
5. Output: a one-page aggregated pain map from interview notes.

### Step 3: Manual Execution and Offer Draft
1. Map the manual workflow step by step using a spreadsheet or simple checklist.
2. Run the workflow for at least one paying customer before writing any code.
3. Draft the Five-Part Offer:
   - **Problem**: one sentence describing the core pain.
   - **Promise**: the specific transformation delivered.
   - **Timeline**: how fast results are achieved.
   - **Price**: the investment required.
   - **Guarantee**: the risk-reversal commitment.
4. Output: one-page offer document saved to `output/`.

### Step 4: Clickable Prototype
1. Define only 3 screens: Login, Input, Output.
2. Generate mock-up using Visily.ai, Figma, or UX pilot.ai from plain English description.
3. Recruit 5 new customers (not existing contacts) for reaction calls.
4. Record each call. Log confusion points. Do not explain the UI during the test.
5. Output: confusion-point log with priority ranking.

### Step 5: MVP Build
1. Write a single-prompt spec using the Intern Model:
   - State the core promise in one sentence.
   - List only the 3 essential screens (Login, Input, Output).
   - Specify: clean UI, no admin dashboard, no complex permissions, no white-label hooks.
2. Deploy via AI code generation (Manis AI or equivalent).
3. Apply 80% Impact Rule to every feature request: if it does not serve 80% of users, log to backlog, do not build.
4. Output: deployed MVP URL + backlog file.

### Step 6: AI Agent Stack by Revenue Tier

| Tier | Human Role | Automated Systems |
|------|------------|-------------------|
| $0-100K | Executes all tasks, uses AI to move faster | None required yet |
| $100K-$1M | Manages systems, closes high-value deals | Onboarding, support, finance reconciliation |
| $1M-$10M+ | Strategy and high-leverage sales only | Full ops loop: lead nurture, delivery, invoicing, reporting |

For each tier transition, audit current manual tasks and identify the highest-volume repeatable step to automate first.

---

## Rules

- **Workflow before features**: always map the workflow before specifying any technical solution.
- **Manual before code**: validate the process manually before automating it.
- **80% Impact Rule**: log all sub-80% feature requests to a backlog file. Never implement mid-sprint.
- **No admin dashboards in MVP**: complexity is a kill switch. Remove it from scope by default.
- **One automated loop at a time**: build, stabilize, then add the next loop. No parallel automation builds.
- **Customer words are the spec**: use exact language from interviews in offer copy and UI labels.

---

## Handoffs

If, during any phase, the primary problem shifts from business design to a defect or breakdown in an existing operation:
- Stop the Business Architect flow.
- Route to `@dmaic` with: current defect, business impact, suspected root cause.
- Log the handoff in `MEMORY/context.md`.

If the request exceeds the 6-phase framework or requires multi-team coordination:
- Stop and state why.
- Route to `@project` for full lifecycle scoping.
- Log the handoff in `MEMORY/context.md`.

---

## Output

All outputs follow the global naming pattern `output/YYYY-MM-DD-task-vN.md`:

- Standard work: `output/YYYY-MM-DD-biz-[phase]-vN.md`
- Feature backlog: `output/YYYY-MM-DD-backlog-vN.md`

Approved deliverables move to `output/final/YYYY-MM-DD-biz-[phase]-final.md`.

---

## Verification

Before marking this skill production-ready, run three test tasks and score each with `.claude/evaluator.md`. Aggregate score must be >= 0.85 on all three.

1. **Happy path**: clear market, clear pain, straightforward MVP scope.
2. **Edge case**: ambiguous market or multi-sided business model.
3. **Error case**: founder inputs are missing, conflicting, or out of phase sequence.

If any run scores < 0.85, iterate using `workflows/iteration-loop.md` and re-test before marking ready.
