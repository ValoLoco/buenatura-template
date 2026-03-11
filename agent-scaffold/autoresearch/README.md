# autoresearch scaffold

Autonomous experiment loop for local BitNet inference.
Based on karpathy/autoresearch. Adapted for CPU-first, sovereign operation.

## Files

| File | Role | Editable |
|---|---|---|
| `experiment.py` | Agent-editable surface: CONFIG, eval_fn | YES (agent only) |
| `harness.py` | Fixed eval harness, timing, metric output | NO |
| `eval_prompts.jsonl.example` | Format reference for prompt generation | NO |
| `eval_prompts.jsonl` | Generated at setup from project context | Generated |
| `results.tsv` | Experiment log (git-untracked) | Auto-written |

## Prerequisites

```bash
bash infra/bootstrap.sh
```

## Running One Experiment

```bash
python3 harness.py > run.log 2>&1
grep "^val_score:" run.log
```

## Autonomous Loop

Point your agent at `skills/autoresearch.md` and say:

```
Have a look at skills/autoresearch.md and kick off a new experiment. Do the setup first.
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `BITNET_MODEL` | `infra/models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf` | Model path |
| `BITNET_THREADS` | all available | CPU thread count |
