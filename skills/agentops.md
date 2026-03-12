# Skill: agentops

**Type:** Observability instrumentation  
**Executables:** `agent-scaffold/ops/trace_logger.py`, `agent-scaffold/ops/eval.py`  
**When to use:** Instrument any task that involves a tool call, model call, or multi-step execution. Run eval.py to review daily performance.

---

## Tracing a Task

Import and use `TaskTrace` at the start of any agent task:

```python
from agent_scaffold.ops.trace_logger import TaskTrace

trace = TaskTrace(task="describe the task", agent="@agent-name")
trace.step("tool_call", tool="knowledge_search", query="...")
trace.step("tool_result", chunks_returned=3, top_score=0.82)
trace.step("model_call", model="claude-3-5-sonnet", prompt_tokens=1240)
trace.step("model_response", output_tokens=380, score=0.91)
trace.finish(outcome="success")  # or "failure", "escalated"
```

For lightweight one-off events without a full trace:

```python
from agent_scaffold.ops.trace_logger import log_event
log_event({"event": "guardrail_fail", "agent": "@reviewer", "gate": "factual_accuracy"})
```

---

## Reviewing Performance

```bash
# Today's summary
python agent-scaffold/ops/eval.py

# Specific date
python agent-scaffold/ops/eval.py --date 2026-03-12

# Last 50 events only
python agent-scaffold/ops/eval.py --tail 50
```

---

## Trace Storage

- One JSONL file per day at `output/traces/YYYY-MM-DD.jsonl`
- Each line is one event. Append-only. Never edit past traces.
- Trace files are committed to git — they are the audit log.
- Rotate by archiving files older than 90 days to `output/traces/archive/`.

---

## Standard Event Names

| Event | When to use |
|---|---|
| `task_start` | Auto-emitted by TaskTrace constructor |
| `task_end` | Auto-emitted by TaskTrace.finish() |
| `tool_call` | Before invoking any tool or skill |
| `tool_result` | After receiving tool output |
| `model_call` | Before sending prompt to LLM |
| `model_response` | After receiving LLM response |
| `guardrail_fail` | When a guardrail gate does not pass |
| `escalation` | When task is flagged for human review |
| `knowledge_retrieval` | When knowledge-search skill is invoked |
