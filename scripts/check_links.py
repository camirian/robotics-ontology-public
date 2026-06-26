#!/usr/bin/env python3
"""Check that internal links and file references in this repo resolve.

Standard-library only (Python 3.8+). No dependencies.

It scans every Markdown file for:
  * Markdown links of the form [text](target)
  * Inline-code references that look like repo paths ending in a known
    extension (e.g. `scripts/foo.py`, `sysml_v2_models/bar.sysml`)

For each local target it confirms the file (and any #anchor) exists.
External links (http/https/mailto) are skipped. Exits non-zero if any
internal reference is broken.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Markdown link: [text](target)
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# Inline-code path-like reference: `something/with.ext` or `file.ext`
CODE_REF = re.compile(r"`([^`\n]+?\.(?:md|sysml|py|sh|txt|cfg|toml|yml|yaml))`")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "tel:")


def anchors_in(path: Path) -> set:
    """Return GitHub-style anchor slugs for all headings in a Markdown file."""
    anchors = set()
    if path.suffix.lower() != ".md":
        return anchors
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"#{1,6}\s+(.*)", line)
        if not m:
            continue
        text = m.group(1).strip()
        slug = re.sub(r"[^\w\s-]", "", text.lower())
        slug = re.sub(r"\s+", "-", slug)
        anchors.add(slug)
    return anchors


def check_target(raw: str, source: Path, problems: list, base: Path) -> None:
    target = raw.strip().strip("<>").split(" ", 1)[0]
    if not target or target.startswith(SKIP_PREFIXES):
        return

    path_part, _, anchor = target.partition("#")
    if not path_part:  # pure same-page anchor handled by '#' skip already
        return

    resolved = (base / path_part).resolve()
    rel = path_part

    if not resolved.exists():
        problems.append(f"{source.relative_to(REPO_ROOT)}: missing target '{rel}'")
        return

    if anchor and resolved.is_file():
        if anchor.lower() not in anchors_in(resolved):
            problems.append(
                f"{source.relative_to(REPO_ROOT)}: missing anchor '#{anchor}' in '{rel}'"
            )


def main() -> int:
    md_files = sorted(REPO_ROOT.rglob("*.md"))
    md_files = [p for p in md_files if ".git" not in p.parts]

    problems: list = []
    checked = 0

    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="replace")
        # Markdown links resolve relative to the file they appear in.
        for m in MD_LINK.finditer(text):
            checked += 1
            check_target(m.group(1), md, problems, md.parent)
        # Inline-code references are only treated as repo paths when they
        # contain a '/' (a directory separator); bare filenames in backticks
        # are prose, not links. Such paths are conventionally repo-relative.
        for m in CODE_REF.finditer(text):
            ref = m.group(1)
            if "/" not in ref or " " in ref or ref.startswith(SKIP_PREFIXES):
                continue
            checked += 1
            check_target(ref, md, problems, REPO_ROOT)

    print(f"Scanned {len(md_files)} Markdown file(s); checked {checked} reference(s).")
    if problems:
        print(f"\n{len(problems)} broken reference(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("All internal links and file references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
