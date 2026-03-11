#!/usr/bin/env python3
"""
harness.py — fixed eval harness for the autoresearch loop.
DO NOT MODIFY. This file is read-only to the agent.

Metric: val_score (lower is better).
Defined as mean error over the eval prompt set, normalized by item count.
Fully deterministic at temperature=0.

The agent modifies experiment.py only.
This file controls timing, eval, and summary output.
"""

import os
import sys
import time
import json
import subprocess
import importlib.util
from pathlib import Path

# --- Constants (do not modify) ---
TIME_BUDGET_SECONDS = 300
TIMEOUT_KILL_SECONDS = 600
EVAL_PROMPTS_FILE = Path("eval_prompts.jsonl")
MODEL_PATH = Path(os.environ.get(
    "BITNET_MODEL",
    "infra/models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf"
))
INFERENCE_SCRIPT = Path("infra/bitnet/run_inference.py")


def verify_runtime():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. Run bash infra/bootstrap.sh first."
        )
    if not INFERENCE_SCRIPT.exists():
        raise FileNotFoundError(
            f"Inference script not found at {INFERENCE_SCRIPT}."
        )
    if not EVAL_PROMPTS_FILE.exists():
        raise FileNotFoundError(
            f"Eval prompts not found at {EVAL_PROMPTS_FILE}. Run setup in skills/autoresearch.md first."
        )


def load_experiment():
    spec = importlib.util.spec_from_file_location("experiment", "experiment.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_inference(prompt: str, config: dict) -> str:
    cmd = [
        "python3", str(INFERENCE_SCRIPT),
        "-m", str(MODEL_PATH),
        "-p", f"{config.get('system', 'You are a helpful assistant.')}\n\n{prompt}",
        "-n", str(config.get("max_tokens", 128)),
        "-temp", "0",
    ]
    threads = os.environ.get("BITNET_THREADS")
    if threads:
        cmd += ["-t", threads]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if not result.stdout.strip():
        raise RuntimeError(f"Empty output from inference. stderr: {result.stderr[:300]}")
    return result.stdout.strip()


def score_response(expected: str, actual: str) -> float:
    exp_tokens = set(expected.lower().split())
    act_tokens = set(actual.lower().split())
    if not exp_tokens:
        return 1.0
    overlap = len(exp_tokens & act_tokens) / len(exp_tokens)
    return 1.0 - overlap


def get_peak_memory_mb() -> float:
    """Cross-platform peak RSS. Linux: ru_maxrss in KB. macOS: ru_maxrss in bytes."""
    try:
        import resource
        rss = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        if sys.platform == "darwin":
            return rss / (1024 * 1024)
        return rss / 1024
    except Exception:
        return 0.0


def main():
    verify_runtime()
    experiment = load_experiment()
    config = experiment.CONFIG

    prompts = []
    with open(EVAL_PROMPTS_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                prompts.append(json.loads(line))

    eval_fn = getattr(experiment, "eval_fn", None)
    wall_start = time.time()
    scores = []
    steps = 0

    for item in prompts:
        if time.time() - wall_start >= TIME_BUDGET_SECONDS:
            break
        prompt = item["prompt"]
        expected = item.get("expected", "")
        try:
            response = run_inference(prompt, config)
            steps += 1
            score = eval_fn(prompt, expected, response) if eval_fn else score_response(expected, response)
            scores.append(score)
        except Exception as e:
            scores.append(1.0)
            print(f"[harness] eval error on step {steps}: {e}", flush=True)

    run_seconds = time.time() - wall_start
    val_score = sum(scores) / len(scores) if scores else 1.0
    peak_memory_mb = get_peak_memory_mb()

    print("---")
    print(f"val_score:        {val_score:.6f}")
    print(f"run_seconds:      {run_seconds:.1f}")
    print(f"peak_memory_mb:   {peak_memory_mb:.1f}")
    print(f"num_steps:        {steps}")


if __name__ == "__main__":
    main()
