# Repository instructions

- Treat `skills/iterate-from-docs/SKILL.md` as the only owner of runtime workflow guidance.
- Keep installation, contribution, and repository maintenance information in `README.md`, not inside the Skill.
- Put reusable briefs and ledgers in `skills/iterate-from-docs/references/templates.md`; do not add auxiliary quick-reference or changelog files.
- Update `agents/openai.yaml` when the skill name, trigger description, or default prompt changes.
- Keep durable prose in current-state language and give every fact one home.
- Run `python3 scripts/validate_skill.py` and `git diff --check` before publishing.
- Preserve the MIT license and DeepSeek Harness provenance statement.

Use focused changes. Do not add dependencies or automation unless they delete repeated maintenance or enforce a deterministic invariant.
