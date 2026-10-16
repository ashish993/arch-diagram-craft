#!/usr/bin/env python3
"""Dependency-free structural checks for the packaged Agent Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "arch-diagram-craft"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    skill_file = SKILL_DIR / "SKILL.md"
    if not skill_file.is_file():
        fail("skills/arch-diagram-craft/SKILL.md is missing")
    content = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not match:
        fail("SKILL.md needs a delimited YAML frontmatter block")
    frontmatter = match.group(1)
    for key in ("name", "description"):
        if not re.search(rf"^{key}:\s*\S", frontmatter, re.M):
            fail(f"SKILL.md frontmatter is missing {key}")
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.M)
    if not name or name.group(1) != "arch-diagram-craft":
        fail("skill name must match the directory and package name")
    if "[TODO:" in content:
        fail("SKILL.md contains an unfinished TODO placeholder")
    for rel in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        target = rel.split("#", 1)[0]
        if target and not target.startswith(("http://", "https://", "mailto:")):
            if not (SKILL_DIR / target).is_file():
                fail(f"broken skill reference: {rel}")
    for required in (ROOT / "README.md", ROOT / "LICENSE", ROOT / "examples" / "order-flow.html", ROOT / "examples" / "evidence-map.md"):
        if not required.is_file():
            fail(f"required repository file is missing: {required.relative_to(ROOT)}")
    print("PASS: skill package structure and local references are valid")


if __name__ == "__main__":
    main()
