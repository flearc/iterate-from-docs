#!/usr/bin/env python3
"""Validate the installable iterate-from-docs skill without third-party packages."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "iterate-from-docs"
SKILL_FILE = SKILL_DIR / "SKILL.md"
METADATA_FILE = SKILL_DIR / "agents" / "openai.yaml"
EXPECTED_NAME = "iterate-from-docs"
FORBIDDEN_AUXILIARY = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
}


def fail(errors: list[str], message: str) -> None:
    """Append one validation failure."""
    errors.append(message)


def parse_frontmatter(text: str, errors: list[str]) -> dict[str, str]:
    """Parse the skill's intentionally simple two-field YAML frontmatter."""
    if not text.startswith("---\n"):
        fail(errors, "SKILL.md must start with YAML frontmatter")
        return {}
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        fail(errors, "SKILL.md frontmatter must have an opening and closing delimiter")
        return {}
    fields: dict[str, str] = {}
    for line in parts[1].splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            fail(errors, f"invalid frontmatter line: {line!r}")
            continue
        fields[key.strip()] = value.strip()
    return fields


def markdown_anchors(text: str) -> set[str]:
    """Return GitHub-style anchors for the simple headings used by this skill."""
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE):
        anchor = heading.lower().strip()
        anchor = re.sub(r"[^\w\- ]", "", anchor, flags=re.UNICODE)
        anchor = re.sub(r"\s+", "-", anchor)
        count = counts.get(anchor, 0)
        counts[anchor] = count + 1
        anchors.add(anchor if count == 0 else f"{anchor}-{count}")
    return anchors


def validate() -> list[str]:
    """Return every structural validation failure."""
    errors: list[str] = []
    if not SKILL_FILE.is_file():
        return [f"missing {SKILL_FILE.relative_to(ROOT)}"]
    if not METADATA_FILE.is_file():
        return [f"missing {METADATA_FILE.relative_to(ROOT)}"]

    skill_text = SKILL_FILE.read_text(encoding="utf-8")
    fields = parse_frontmatter(skill_text, errors)
    if set(fields) != {"name", "description"}:
        fail(errors, "frontmatter must contain only name and description")
    if fields.get("name") != EXPECTED_NAME:
        fail(errors, f"frontmatter name must be {EXPECTED_NAME!r}")
    description = fields.get("description", "")
    if len(description) < 80 or "TODO" in description:
        fail(errors, "description must explain behavior and triggering contexts")
    if len(skill_text.splitlines()) > 500:
        fail(errors, "SKILL.md must stay under 500 lines")
    if "[TODO" in skill_text or re.search(r"^TODO:\\s", skill_text, re.MULTILINE):
        fail(errors, "SKILL.md contains an unresolved TODO")

    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", skill_text):
        if target.startswith(("http://", "https://", "#")):
            continue
        path, separator, fragment = target.partition("#")
        resolved = (SKILL_DIR / path).resolve()
        try:
            resolved.relative_to(SKILL_DIR.resolve())
        except ValueError:
            fail(errors, f"skill link escapes the skill directory: {target}")
            continue
        if not resolved.exists():
            fail(errors, f"broken skill link: {target}")
            continue
        if separator and fragment:
            target_anchors = markdown_anchors(resolved.read_text(encoding="utf-8"))
            if fragment not in target_anchors:
                fail(errors, f"broken skill link anchor: {target}")

    metadata = METADATA_FILE.read_text(encoding="utf-8")
    if "$$" + EXPECTED_NAME in metadata:
        fail(errors, "default prompt contains a duplicated dollar sign")
    if "$" + EXPECTED_NAME not in metadata:
        fail(errors, "default prompt must explicitly invoke $iterate-from-docs")
    short_match = re.search(r'^  short_description: "([^"]+)"$', metadata, re.MULTILINE)
    if short_match is None or not 25 <= len(short_match.group(1)) <= 64:
        fail(errors, "short_description must contain 25 to 64 characters")

    for filename in FORBIDDEN_AUXILIARY:
        if (SKILL_DIR / filename).exists():
            fail(errors, f"auxiliary project documentation belongs at repository root: {filename}")

    return errors


def main() -> int:
    """Print a concise result and return a process exit status."""
    errors = validate()
    if errors:
        print("validate_skill failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print("validate_skill: iterate-from-docs is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
