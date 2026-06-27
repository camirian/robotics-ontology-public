#!/usr/bin/env python3
"""Tests for the public-surface private-leak scanner.

Stdlib only (no pytest dependency). Run directly:

    python3 tools/test_check_public_surface.py

Exits 0 if all assertions pass, 1 otherwise.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_public_surface as cps  # noqa: E402


def test_clean_tree_passes() -> None:
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "README.md").write_text(
            "# Public Glossary\n\nClone with `git clone https://github.com/example/repo.git`.\n",
            encoding="utf-8",
        )
        (root / "model.sysml").write_text("part def Robot;\n", encoding="utf-8")
        results = cps.scan([root])
        assert results == [], f"expected clean, got {results}"


def test_internal_host_leak_detected() -> None:
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "QUICKSTART.md").write_text(
            "git clone gitea" + "@localhost:internal/repo.git\n",
            encoding="utf-8",
        )
        results = cps.scan([root])
        reasons = {r[2] for r in results}
        assert any("gitea@localhost" in reason for reason in reasons), reasons


def test_generic_localhost_clone_url_detected() -> None:
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "notes.md").write_text(
            "clone with someuser" + "@localhost:team/project.git\n", encoding="utf-8"
        )
        results = cps.scan([root])
        assert results, "expected user@localhost:path clone URL to be flagged"


def test_main_exit_codes() -> None:
    with tempfile.TemporaryDirectory() as d:
        clean = Path(d) / "clean.md"
        clean.write_text("nothing private here\n", encoding="utf-8")
        assert cps.main([str(clean)]) == 0

        dirty = Path(d) / "dirty.md"
        dirty.write_text("host: gitea" + "@localhost\n", encoding="utf-8")
        assert cps.main([str(dirty)]) == 1


def test_scanner_skips_itself() -> None:
    # The scanner and its test contain the patterns as rules/fixtures; running
    # the scanner over the real repo root must not flag those two files.
    results = cps.scan([cps.repo_root()])
    flagged = {p.name for p, *_ in results}
    assert "check_public_surface.py" not in flagged
    assert "test_check_public_surface.py" not in flagged


def main() -> int:
    tests = [
        test_clean_tree_passes,
        test_internal_host_leak_detected,
        test_generic_localhost_clone_url_detected,
        test_main_exit_codes,
        test_scanner_skips_itself,
    ]
    failures = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{len(tests) - failures}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
