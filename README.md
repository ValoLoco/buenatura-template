# BUENATURA Template

Sovereign agent template for purpose-driven projects.
Fork this repo or use it as a GitHub Template to bootstrap any project with
skills, workflows, agent scaffold, and local BitNet inference out of the box.

## What is inside

```
.claude/          Agent config: routing, guardrails, evaluator, principles
KNOWLEDGE/        Project-specific knowledge files (you populate this)
MEMORY/           Agent memory and context persistence
agent-scaffold/   Reusable agent scaffolds (includes autoresearch loop)
infra/            Bootstrap scripts and model paths
output/           All agent work output (WIP and final)
skills/           Skill files loaded on demand by agents
workflows/        Workflow files for structured task execution
CLAUDE.md         Agent entry point and routing instructions
CHANGELOG.md      Template version history
VERSION           Current template version (for downstream pinning)
```

## Quickstart

### Option A: GitHub Template (recommended)

1. Click **Use this template** on GitHub.
2. Name your repo and create it.
3. Run setup:

```bash
bash infra/bootstrap.sh
```

### Option B: Clone and adapt

```bash
git clone https://github.com/ValoLoco/buenatura-template.git my-project
cd my-project
rm -rf .git
git init
bash infra/bootstrap.sh
```

### Option C: Pull into existing repo

```bash
curl -sSL https://raw.githubusercontent.com/ValoLoco/buenatura-template/main/infra/bootstrap.sh | bash
```

## Template versioning

Each project initialized from this template records which version it started from.
Pin to a specific version by checking out a tag:

```bash
git clone --branch v1.0.0 https://github.com/ValoLoco/buenatura-template.git
```

## Agent entry point

Point any Claude, POPEBOT, openclaw, or nanoclaw agent at `CLAUDE.md`.
That file is the single routing entry point for all agent tasks.

## autoresearch skill

Includes the full autonomous experiment loop adapted from karpathy/autoresearch.
Runs locally on BitNet. No GPU required. See `skills/autoresearch.md` and
`agent-scaffold/autoresearch/` for setup instructions.

## License

MIT
