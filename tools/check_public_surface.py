#!/usr/bin/env python3
"""Public-surface private-leak scanner.

Scans tracked text files for internal/private *infrastructure* references that
must never appear in this public mirror: internal git hosts and private clone
URLs (e.g. ``gitea@localhost``). Stdlib only; no third-party dependencies.

Scope note: this scanner deliberately targets internal hostnames/clone URLs,
not the public "Citadel" ecosystem brand name, which is intentional public
portfolio branding present in ``README.md``. Whether to keep that branding is a
documentation decision tracked in the master plan, not a private-leak failure.

Usage:
    python3 tools/check_public_surface.py [PATH ...]

With no PATH arguments, scans the repository root (the parent of this file's
directory). Exits 0 when clean, 1 when any leak is found.

This is intentionally a *private-leak detector*, not a broken-link checker:
it does not flag references to not-yet-present scripts, so it stays narrowly
scoped to the public-safety guarantee in AGENTS.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Patterns that indicate private/internal context leaking into the public repo.
# Each entry: (compiled regex, human-readable reason).
LEAK_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"gitea@localhost", re.IGNORECASE), "internal git host (gitea@localhost)"),
    (re.compile(r"\bgit@localhost\b", re.IGNORECASE), "internal git host (git@localhost)"),
    (re.compile(r"\w+@localhost:[\w/.-]+", re.IGNORECASE), "private clone URL (user@localhost:path)"),
]

# File suffixes worth scanning (text/docs only).
TEXT_SUFFIXES = {".md", ".sysml", ".py", ".txt", ".sh", ".yml", ".yaml", ".json", ".cfg", ".toml"}

# Paths to skip (this scanner and its tests legitimately contain the patterns
# as detection rules / fixtures).
SKIP_NAMES = {"check_public_surface.py", "test_check_public_surface.py"}
SKIP_DIRS = {".git", "venv", "node_modules", "__pycache__", ".pytest_cache"}


def iter_text_files(roots: list[Path]):
    for root in roots:
        if root.is_file():
            yield root
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.name in SKIP_NAMES:
                continue
            if path.suffix.lower() in TEXT_SUFFIXES:
                yield path


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    """Return list of (line_no, reason, line_text) for any leaks found."""
    findings: list[tuple[int, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return findings
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern, reason in LEAK_PATTERNS:
            if pattern.search(line):
                findings.append((lineno, reason, line.strip()))
    return findings


def scan(roots: list[Path]) -> list[tuple[Path, int, str, str]]:
    results: list[tuple[Path, int, str, str]] = []
    for path in iter_text_files(roots):
        for lineno, reason, line in scan_file(path):
            results.append((path, lineno, reason, line))
    return results


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def main(argv: list[str]) -> int:
    if argv:
        roots = [Path(a) for a in argv]
    else:
        roots = [repo_root()]

    results = scan(roots)
    if not results:
        print("public-surface scan: OK (no private/internal leaks found)")
        return 0

    print("public-surface scan: FAILED")
    for path, lineno, reason, line in results:
        print(f"  {path}:{lineno}: {reason}")
        print(f"      > {line}")
    print(f"\n{len(results)} leak(s) found. Remove internal references before publishing.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
