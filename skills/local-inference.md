---
name: local-inference
description: Runs a prompt through the local BitNet model and returns a text response.
---

# Local Inference

Runs a prompt through the local BitNet b1.58 2B4T model via bitnet.cpp. Zero API cost. Fully offline after bootstrap.

## When to Load

Loaded by `model-routing` when task complexity is scored Low or Medium.
Do not load for tasks requiring long-context reasoning, multi-document synthesis, or high-stakes judgment.

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `prompt` | string | Yes | The full prompt to send to the model |
| `system` | string | No | System instruction (default: "You are a helpful assistant.") |
| `max_tokens` | int | No | Max tokens to generate (default: 256) |
| `temperature` | float | No | Sampling temperature (default: 0.7) |

## Steps

1. Verify model file exists at `infra/models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf`. Fail loudly if missing with message: "Run bash infra/bootstrap.sh first."
2. Construct the inference command with provided parameters.
3. Execute via `run_inference.py`. Capture stdout as response.
4. Return response string to caller.

## Execution

```bash
python3 infra/bitnet/run_inference.py \
  -m infra/models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf \
  -p "[system]\n\n[prompt]" \
  -n [max_tokens] \
  -temp [temperature]
```

## Rules

- Never call this skill before `bootstrap.sh` has been run.
- Always pass a system prompt. An empty system prompt degrades output quality.
- If model returns empty output, fail loudly. Do not silently pass empty string downstream.
- Log every call to `output/local-inference.log`: timestamp, prompt length, token count, latency.

## Output

Returns plain text string. Caller is responsible for parsing structure if needed.
Log entry written to `output/local-inference.log`.
