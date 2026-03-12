"""trace_logger: lightweight AgentOps trace writer.

Writes one JSONL line per agent event to output/traces/YYYY-MM-DD.jsonl.
Call log_event() at each meaningful step: task start, tool call, tool result,
model call, model response, guardrail check, final output.

Usage (from any agent or tool):
    from agent_scaffold.ops.trace_logger import log_event, TaskTrace

    trace = TaskTrace(task="summarise client brief", agent="@researcher")
    trace.step("tool_call", tool="knowledge_search", query="client brief Q1")
    trace.step("tool_result", chunks_returned=3, top_score=0.82)
    trace.step("model_call", model="claude-3-5-sonnet", prompt_tokens=1240)
    trace.step("model_response", output_tokens=380, score=0.91)
    trace.finish(outcome="success")
"""
import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TRACES_DIR = Path("output/traces")


def _ensure_dir() -> None:
    TRACES_DIR.mkdir(parents=True, exist_ok=True)


def _trace_file() -> Path:
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return TRACES_DIR / f"{date_str}.jsonl"


def log_event(event: dict[str, Any]) -> None:
    """Append a single event dict as a JSONL line. Thread-safe via append mode."""
    _ensure_dir()
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        **event,
    }
    with _trace_file().open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


class TaskTrace:
    """Context manager and step recorder for a single agent task."""

    def __init__(self, task: str, agent: str, metadata: dict[str, Any] | None = None):
        self.trace_id = str(uuid.uuid4())[:8]
        self.task = task
        self.agent = agent
        self.started_at = time.monotonic()
        self.metadata = metadata or {}
        log_event({
            "trace_id": self.trace_id,
            "event": "task_start",
            "agent": agent,
            "task": task,
            **self.metadata,
        })

    def step(self, event: str, **kwargs: Any) -> None:
        """Log a named step with arbitrary key-value context."""
        log_event({
            "trace_id": self.trace_id,
            "event": event,
            "agent": self.agent,
            **kwargs,
        })

    def finish(self, outcome: str = "success", **kwargs: Any) -> None:
        """Log task completion with elapsed time in seconds."""
        elapsed = round(time.monotonic() - self.started_at, 3)
        log_event({
            "trace_id": self.trace_id,
            "event": "task_end",
            "agent": self.agent,
            "task": self.task,
            "outcome": outcome,
            "elapsed_s": elapsed,
            **kwargs,
        })
