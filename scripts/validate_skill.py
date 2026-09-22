#!/usr/bin/env python3
"""Validate this skill package without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py"}
HAN_RE = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF]")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def text_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix.lower() in TEXT_SUFFIXES
    )


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail("SKILL.md frontmatter is not closed")

    values: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def validate_frontmatter() -> None:
    if not SKILL.exists():
        fail("SKILL.md is missing")
    values = parse_frontmatter(SKILL.read_text(encoding="utf-8"))
    name = values.get("name", "")
    description = values.get("description", "")
    if name != "vcaa-text-response-style":
        fail("frontmatter name must be vcaa-text-response-style")
    if len(name) > 64 or not NAME_RE.fullmatch(name):
        fail("frontmatter name must be lowercase hyphen-case and at most 64 characters")
    if not description or "TODO" in description:
        fail("frontmatter description is missing or unfinished")


def validate_english_only(files: list[Path]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        match = HAN_RE.search(text)
        if match:
            line = text.count("\n", 0, match.start()) + 1
            fail(f"non-English CJK character found in {path.relative_to(ROOT)}:{line}")


def validate_no_placeholders(files: list[Path]) -> None:
    unfinished_tokens = ("[" + "TODO", "TO" + "DO:")
    for path in files:
        text = path.read_text(encoding="utf-8")
        if any(token in text for token in unfinished_tokens):
            fail(f"unfinished TODO found in {path.relative_to(ROOT)}")


def validate_relative_links(files: list[Path]) -> None:
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                fail(f"broken relative link in {path.relative_to(ROOT)}: {target}")


def validate_required_files() -> None:
    required = [
        "README.md",
        "PROMPT_TEMPLATE.md",
        "EVALUATION.md",
        "agents/openai.yaml",
        "references/vcaa-style-guide.md",
        "references/sunset-boulevard-core-evidence.md",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"required file is missing: {relative}")

    agent_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$vcaa-text-response-style" not in agent_yaml:
        fail("agents/openai.yaml default prompt must mention $vcaa-text-response-style")


def main() -> None:
    files = text_files()
    validate_frontmatter()
    validate_required_files()
    validate_english_only(files)
    validate_no_placeholders(files)
    validate_relative_links(files)
    print(f"Validated {len(files)} text files successfully.")


if __name__ == "__main__":
    main()
