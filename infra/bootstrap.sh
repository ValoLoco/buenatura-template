#!/usr/bin/env bash
# bootstrap.sh — one-command setup for buenatura-template projects
# Run once per machine after cloning or forking the template.
set -euo pipefail

TEMPLATE_VERSION=$(cat VERSION 2>/dev/null || echo "unknown")
echo "[bootstrap] BUENATURA Template v${TEMPLATE_VERSION}"
echo "[bootstrap] Starting setup..."

# 1. Create required directories if missing
for dir in output/final KNOWLEDGE MEMORY infra/models; do
  mkdir -p "$dir"
  echo "[bootstrap] ensured: $dir"
done

# 2. Create placeholder files so directories are tracked
touch KNOWLEDGE/.gitkeep
touch MEMORY/.gitkeep
touch output/.gitkeep
touch output/final/.gitkeep

# 3. Download BitNet model if not present
MODEL_DIR="infra/models/BitNet-b1.58-2B-4T"
MODEL_FILE="$MODEL_DIR/ggml-model-i2_s.gguf"

if [ -f "$MODEL_FILE" ]; then
  echo "[bootstrap] BitNet model already present. Skipping download."
else
  echo "[bootstrap] BitNet model not found at $MODEL_FILE"
  echo "[bootstrap] To download, run:"
  echo "  mkdir -p $MODEL_DIR"
  echo "  huggingface-cli download microsoft/BitNet-b1.58-2B-4T --local-dir $MODEL_DIR"
  echo "[bootstrap] Skipping automatic download (requires huggingface-cli)."
fi

# 4. Check Python
if command -v python3 &>/dev/null; then
  PYVER=$(python3 --version)
  echo "[bootstrap] Python found: $PYVER"
else
  echo "[bootstrap] WARNING: python3 not found. Install Python 3.10+ before running skills."
fi

# 5. Check uv (optional, used by autoresearch scaffold)
if command -v uv &>/dev/null; then
  echo "[bootstrap] uv found: $(uv --version)"
else
  echo "[bootstrap] INFO: uv not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

echo ""
echo "[bootstrap] Setup complete."
echo "[bootstrap] Next: point your agent at CLAUDE.md to begin."
