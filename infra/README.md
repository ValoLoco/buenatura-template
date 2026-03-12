# infra/

Infrastructure layer for local model inference. One job: stand up the BitNet backend.

## Contents

| Path | Purpose |
|---|---|
| `bitnet/` | Git submodule: microsoft/BitNet |
| `models/` | Model weights (.gitignored, pulled by bootstrap.sh) |
| `bootstrap.sh` | One-command setup: builds BitNet + downloads model |

## Setup

```bash
# Add BitNet as submodule (once, when instantiating from TEMPLATE)
git submodule add https://github.com/microsoft/BitNet.git infra/bitnet

# Run bootstrap (once per machine)
bash infra/bootstrap.sh
```

## Requirements

- python >= 3.9
- cmake >= 3.22
- clang >= 18
- huggingface-cli (`pip install huggingface_hub`)

## After Bootstrap

The local inference backend is available to all skills via `skills/local-inference.md`.
Model weights live in `infra/models/` and are never committed to the repo.
