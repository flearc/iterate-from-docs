# iterate-from-docs

A reusable Codex skill for shipping changes quickly without letting implementation, tests, decisions, and documentation drift apart.

The workflow was distilled from the documentation system and Git history of [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It is an independent community project and is not affiliated with DeepSeek.

## What it enforces

- Read the narrow chain of instructions, architecture, component docs, and relevant Git history.
- Resolve root-to-leaf instruction overlays separately for every affected path.
- Give every durable fact one owner and link instead of copying.
- Lock an observable iteration outcome, non-goals, owners, deletion scope, and evidence before editing.
- Update code, tests, docs, decisions, generated artifacts, and removals as one coherent change.
- Delete duplicate paths, unsupported surfaces, speculative abstractions, stale tests, and unnecessary compatibility code.
- Validate through the real entry path with the smallest evidence set that can catch the regression.

## Repository layout

```text
skills/iterate-from-docs/  Installable Codex skill and its on-demand templates
scripts/validate_skill.py  Dependency-free structural validation
.github/workflows/         Validation on pushes and pull requests
```

Project maintenance belongs at the repository root. Runtime guidance belongs only in `skills/iterate-from-docs/SKILL.md`.

## Install

Clone the repository, then copy or symlink `skills/iterate-from-docs` into `${CODEX_HOME:-$HOME/.codex}/skills/iterate-from-docs`.

Example with a symlink:

```sh
git clone https://github.com/flearc/iterate-from-docs.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)/iterate-from-docs/skills/iterate-from-docs" "${CODEX_HOME:-$HOME/.codex}/skills/iterate-from-docs"
```

If that destination already exists, update or remove it intentionally before installing; the command above does not overwrite an existing skill.

## Use

```text
Use $iterate-from-docs to implement this change while keeping code, tests, decisions, and documentation aligned.
```

The skill can also trigger automatically for non-trivial feature, fix, architecture, removal, cleanup, and documentation-drift work.

## Maintain

Edit the owner rather than duplicating information:

- Workflow and behavioral guidance: `skills/iterate-from-docs/SKILL.md`
- Reusable working artifacts: `skills/iterate-from-docs/references/templates.md`
- Skill-list metadata: `skills/iterate-from-docs/agents/openai.yaml`
- Installation and contribution information: this README

Run the same validation as CI:

```sh
python3 scripts/validate_skill.py
```

Keep the skill body under 500 lines. Add a permanent rule only when it changes agent behavior; keep examples and templates in the on-demand reference.

## License

MIT
