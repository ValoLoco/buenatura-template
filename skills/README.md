# Skills Index

Load skills only when the routing table specifies them.
One skill per task. No preloading.

---

## Inference Layer (Load First on Every Task)

Scoring scale: 4 dimensions (Context Length, Reasoning Depth, Stakes, Reversibility), each 1-3. Total range: 4-12.

| Skill | File | Load When |
|-------|------|-----------|
| Model Routing | `model-routing.md` | **Every task. Entry gate for all LLM calls.** Routes to local or API based on 4-dimension score. |
| Local Inference | `local-inference.md` | When model-routing total scores 4-9. Requires `bootstrap.sh` to have been run. |

---

## Internal Skills

| Skill | File | Load When |
|-------|------|-----------|
| Knowledge Search | `knowledge-search.md` | Before any task requiring retrieval from KNOWLEDGE/ corpus. Run before loading full files. |
| Research Workflow | `research-workflow.md` | Any task requiring context-first knowledge gathering. VERITAS runs embedded at Step 4. |
| VERITAS Verification | `veritas-verification.md` | Validating claims, agent outputs, or strategies outside of a research task. Run standalone. |
| Project Charter | `project-charter.md` | DMAIC Define phase. Project Execution Phase 1 (Initiate). |
| SIPOC | `sipoc.md` | DMAIC Define phase. Project Execution Phase 3 (Structure). |
| FMEA | `fmea.md` | DMAIC Analyze phase. Project Execution Phase 3 (Structure). |
| Control Plan | `control-plan.md` | DMAIC Control phase. Project Execution Phase 6 (Close). |
| Business Architect | `business-architect.md` | One-person AI business design: market validation, MVP, offer, prototype, agent stack. |
| AgentOps | `agentops.md` | Instrument any task with tool calls, model calls, or multi-step execution. Run eval.py for daily review. |
| Autoresearch | `autoresearch.md` | Autonomous iterative model experimentation. Run overnight or unattended. Requires BitNet runtime. |
| Skill Creation Guide | `skill-creation-guide.md` | When building a new skill from scratch. Follow all 4 registration surfaces in Step 4. |

**VERITAS usage note**: when running Research Workflow, VERITAS is already embedded at Step 4. Load `veritas-verification.md` standalone only when you are validating output or claims without doing a full research task.

---

## External Skills (skills.sh)

Search https://skills.sh before building any new skill.

Highly relevant categories:
- `copywriting` - content generation best practices
- `code-reviewer` - automated code review
- `content-strategy` - content planning and calendars
- `data-analysis` - structured data reasoning
- `pdf` - PDF reading and extraction

Install via manual copy or MCP tool. See `.claude/skills-protocol.md` for instructions.

---

## Creating a New Skill

Follow `skill-creation-guide.md` for the full process.
Every new skill must be registered here before it is used.
