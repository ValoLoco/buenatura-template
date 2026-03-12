"""eval: simple outcome evaluator for agent traces.

Reads today's (or a specified date's) JSONL trace file and reports:
  - Task count and success rate
  - Average elapsed time per task
  - Tool call frequency
  - Tasks that ended in failure or escalation

Usage:
    python agent_scaffold/ops/eval.py
    python agent_scaffold/ops/eval.py --date 2026-03-12
    python agent_scaffold/ops/eval.py --tail 50
"""
import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

TRACES_DIR = Path("output/traces")


def load_traces(date_str: str, tail: int | None = None) -> list[dict]:
    path = TRACES_DIR / f"{date_str}.jsonl"
    if not path.exists():
        print(f"No trace file found for {date_str} at {path}")
        return []
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    if tail:
        lines = lines[-tail:]
    return [json.loads(l) for l in lines if l.strip()]


def summarise(events: list[dict]) -> None:
    tasks: dict[str, dict] = {}
    tool_calls: Counter = Counter()
    model_calls: Counter = Counter()

    for e in events:
        tid = e.get("trace_id", "unknown")
        ev = e.get("event", "")

        if ev == "task_start":
            tasks[tid] = {"task": e.get("task"), "agent": e.get("agent"), "outcome": None, "elapsed_s": None}

        elif ev == "task_end":
            if tid in tasks:
                tasks[tid]["outcome"] = e.get("outcome", "unknown")
                tasks[tid]["elapsed_s"] = e.get("elapsed_s")

        elif ev == "tool_call":
            tool_calls[e.get("tool", "unknown")] += 1

        elif ev == "model_call":
            model_calls[e.get("model", "unknown")] += 1

    completed = [t for t in tasks.values() if t["outcome"] is not None]
    success = [t for t in completed if t["outcome"] == "success"]
    failures = [t for t in completed if t["outcome"] != "success"]
    times = [t["elapsed_s"] for t in completed if t["elapsed_s"] is not None]
    avg_time = round(sum(times) / len(times), 2) if times else None

    print(f"\n{'='*50}")
    print(f"Tasks completed : {len(completed)}")
    print(f"Success rate    : {round(len(success)/len(completed)*100, 1)}%" if completed else "Success rate    : n/a")
    print(f"Avg elapsed     : {avg_time}s" if avg_time else "Avg elapsed     : n/a")
    print(f"\nTool calls:")
    for tool, count in tool_calls.most_common():
        print(f"  {tool}: {count}")
    print(f"\nModel calls:")
    for model, count in model_calls.most_common():
        print(f"  {model}: {count}")
    if failures:
        print(f"\nFailed / escalated tasks:")
        for t in failures:
            print(f"  [{t['outcome']}] {t['agent']} — {t['task']}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate agent trace log")
    parser.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"), help="Date to evaluate (YYYY-MM-DD)")
    parser.add_argument("--tail", type=int, default=None, help="Only evaluate last N events")
    args = parser.parse_args()
    events = load_traces(args.date, args.tail)
    if events:
        summarise(events)
