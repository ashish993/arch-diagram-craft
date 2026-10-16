#!/usr/bin/env python3
"""Dependency-free structural checks for the packaged Agent Skill."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "arch-diagram-craft"


class DocumentCheck(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.resources: list[str] = []
        self.svg_accessibility: list[tuple[str, str]] = []
        self.title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        if values.get("src"):
            self.resources.append(values["src"] or "")
        if tag == "title":
            self.title = True
        if tag == "svg":
            self.svg_accessibility.append((values.get("role", "") or "", values.get("aria-labelledby", "") or ""))


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
    required_files = (
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "examples" / "order-flow.html",
        ROOT / "examples" / "evidence-map.md",
        ROOT / "examples" / "context-container.html",
        ROOT / "examples" / "context-container-evidence.md",
        ROOT / "examples" / "sequence.html",
        ROOT / "examples" / "sequence-evidence.md",
        ROOT / "examples" / "deployment.html",
        ROOT / "examples" / "deployment-evidence.md",
        ROOT / "examples" / "business-process.html",
        ROOT / "examples" / "business-process-evidence.md",
        ROOT / "docs" / "research-notes.md",
        ROOT / "docs" / "research-notes.html",
        ROOT / "examples" / "QA_REPORT.md",
    )
    for required in required_files:
        if not required.is_file():
            fail(f"required repository file is missing: {required.relative_to(ROOT)}")
    for phrase in ("Render, inspect, revise, and repeat", "arrowhead visibly points", "No text is hidden", "Visual QA feedback loop"):
        if phrase not in content:
            fail(f"SKILL.md is missing required visual QA guidance: {phrase}")
    html_files = sorted((ROOT / "examples").glob("*.html")) + [ROOT / "docs" / "index.html", ROOT / "docs" / "research-notes.html"]
    for html_file in html_files:
        parser = DocumentCheck()
        parser.feed(html_file.read_text(encoding="utf-8"))
        if not parser.title:
            fail(f"HTML document is missing a title element: {html_file.relative_to(ROOT)}")
        for role, labelledby in parser.svg_accessibility:
            if role != "img" or not labelledby or not set(labelledby.split()).issubset(parser.ids):
                fail(f"SVG needs role=img and valid aria-labelledby targets: {html_file.relative_to(ROOT)}")
        for href in [*parser.links, *parser.resources]:
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "tel:")):
                continue
            if not parsed.path:
                if parsed.fragment and parsed.fragment not in parser.ids:
                    fail(f"broken in-page link in {html_file.relative_to(ROOT)}: {href}")
                continue
            target = unquote(parsed.path)
            if html_file.parent == ROOT / "docs" and target.startswith("examples/"):
                local_target = ROOT / target
            else:
                local_target = (html_file.parent / target).resolve()
            candidates = [local_target]
            if local_target.suffix == ".html":
                candidates.append(local_target.with_suffix(".md"))
            if not any(candidate.is_file() for candidate in candidates):
                fail(f"broken local HTML link in {html_file.relative_to(ROOT)}: {href}")
    print("PASS: skill package structure and local references are valid")


if __name__ == "__main__":
    main()
