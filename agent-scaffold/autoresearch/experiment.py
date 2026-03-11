#!/usr/bin/env python3
"""
experiment.py — agent-editable experiment surface.
This is the ONLY file the agent modifies.

CONFIG dict is read by harness.py. Everything here is fair game:
- system prompt
- max_tokens
- custom eval_fn

Do not touch harness.py.
"""

# --- Agent modifies this block ---
CONFIG = {
    "system": "You are a helpful assistant. Answer concisely and accurately.",
    "max_tokens": 128,
}


# --- Optional: override the scoring function ---
# If defined, harness.py calls eval_fn(prompt, expected, actual) -> float
# Return value must be float. Lower is better.
# Delete this function to use harness default (token overlap).
def eval_fn(prompt: str, expected: str, actual: str) -> float:
    """Baseline: token overlap. Agent should replace with task-specific logic."""
    exp_tokens = set(expected.lower().split())
    act_tokens = set(actual.lower().split())
    if not exp_tokens:
        return 1.0
    overlap = len(exp_tokens & act_tokens) / len(exp_tokens)
    return 1.0 - overlap
