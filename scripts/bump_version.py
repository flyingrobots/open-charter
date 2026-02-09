#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SemVer:
    major: int
    minor: int
    patch: int

    @classmethod
    def parse(cls, value: str) -> "SemVer":
        match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", value.strip())
        if not match:
            raise ValueError(f"Invalid version (expected MAJOR.MINOR.PATCH): {value!r}")
        major, minor, patch = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        return cls(major=major, minor=minor, patch=patch)

    def bump_major(self) -> "SemVer":
        return SemVer(self.major + 1, 0, 0)

    def bump_minor(self) -> "SemVer":
        return SemVer(self.major, self.minor + 1, 0)

    def bump_patch(self) -> "SemVer":
        return SemVer(self.major, self.minor, self.patch + 1)

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _replace_exact(text: str, old: str, new: str) -> tuple[str, int]:
    if old == new:
        return text, 0
    count = text.count(old)
    return text.replace(old, new), count


def _extract_charter_version(charter_meta_tex: str) -> str:
    match = re.search(r"\\newcommand\{\\CharterVersion\}\{([^}]+)\}", charter_meta_tex)
    if not match:
        raise RuntimeError("Could not find \\newcommand{\\CharterVersion}{...} in paper/charter_meta.tex")
    return match.group(1).strip()


def _set_charter_version(charter_meta_tex: str, new_version: str) -> tuple[str, int]:
    pattern = r"(\\newcommand\{\\CharterVersion\}\{)([^}]+)(\})"
    updated, n = re.subn(pattern, rf"\g<1>{new_version}\g<3>", charter_meta_tex, count=1)
    if n != 1:
        raise RuntimeError("Failed to update \\CharterVersion in paper/charter_meta.tex (unexpected format)")
    return updated, n


def _ensure_changelog_entry(changelog: str, new_version: str, today: str) -> tuple[str, bool]:
    header = f"## [{new_version}] - {today}"
    if header in changelog:
        return changelog, False

    unreleased_marker = "## [Unreleased]"
    idx = changelog.find(unreleased_marker)
    if idx == -1:
        raise RuntimeError("CHANGELOG.md is missing a '## [Unreleased]' section")

    insert_at = idx + len(unreleased_marker)
    insertion = (
        "\n\n"
        f"{header}\n\n"
        "### Added\n"
        "- \n\n"
        "### Changed\n"
        "- \n\n"
        "### Fixed\n"
        "- \n\n"
        "### Removed\n"
        "- "
    )
    return changelog[:insert_at] + insertion + changelog[insert_at:], True


def _run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=str(cwd), check=True)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Bump The Open Charter version across LaTeX + docs (semver).",
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--major", action="store_true", help="Bump MAJOR and reset MINOR/PATCH to 0.")
    group.add_argument("--minor", action="store_true", help="Bump MINOR and reset PATCH to 0.")
    group.add_argument("--patch", action="store_true", help="Bump PATCH.")
    parser.add_argument(
        "--set",
        metavar="MAJOR.MINOR.PATCH",
        help="Set an explicit version instead of bumping.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print what would change, but write nothing.")
    parser.add_argument(
        "--build",
        action="store_true",
        help="Run `make` after updating versions (rebuilds pdf/the-open-charter.pdf).",
    )

    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    charter_meta_path = repo_root / "paper" / "charter_meta.tex"
    readme_path = repo_root / "README.md"
    critique_path = repo_root / "critiques" / "gpt-5_2-extra-high.md"
    notice_path = repo_root / "NOTICE"
    citation_cff_path = repo_root / "CITATION.cff"
    changelog_path = repo_root / "CHANGELOG.md"

    charter_meta = _read_text(charter_meta_path)
    old_version = _extract_charter_version(charter_meta)
    old = SemVer.parse(old_version)

    if args.set:
        new = SemVer.parse(args.set)
    else:
        if not (args.major or args.minor or args.patch):
            parser.error("one of --major/--minor/--patch or --set is required")
        if args.major:
            new = old.bump_major()
        elif args.minor:
            new = old.bump_minor()
        else:
            new = old.bump_patch()

    new_version = str(new)
    today = _dt.date.today().isoformat()

    updated_charter_meta, _ = _set_charter_version(charter_meta, new_version)

    if not readme_path.exists():
        raise RuntimeError("README.md not found")
    updated_readme, readme_hits = _replace_exact(_read_text(readme_path), old_version, new_version)

    critique_hits = 0
    updated_critique = None
    if critique_path.exists():
        updated_critique, critique_hits = _replace_exact(_read_text(critique_path), old_version, new_version)

    notice_hits = 0
    updated_notice = None
    if notice_path.exists():
        updated_notice, notice_hits = _replace_exact(_read_text(notice_path), old_version, new_version)

    citation_hits = 0
    updated_citation = None
    if citation_cff_path.exists():
        updated_citation, citation_hits = _replace_exact(_read_text(citation_cff_path), old_version, new_version)

    if not changelog_path.exists():
        raise RuntimeError("CHANGELOG.md not found (expected at repo root)")
    updated_changelog, changelog_inserted = _ensure_changelog_entry(_read_text(changelog_path), new_version, today)

    print(f"Old version: {old_version}")
    print(f"New version: {new_version}")
    print(f"- paper/charter_meta.tex: updated \\CharterVersion")
    print(f"- README.md: replaced {readme_hits} occurrence(s)")
    if critique_path.exists():
        print(f"- critiques/gpt-5_2-extra-high.md: replaced {critique_hits} occurrence(s)")
    if notice_path.exists():
        print(f"- NOTICE: replaced {notice_hits} occurrence(s)")
    if citation_cff_path.exists():
        print(f"- CITATION.cff: replaced {citation_hits} occurrence(s)")
    print(f"- CHANGELOG.md: {'inserted' if changelog_inserted else 'already had'} {new_version} entry")

    if args.dry_run:
        return 0

    _write_text(charter_meta_path, updated_charter_meta)
    _write_text(readme_path, updated_readme)
    if critique_path.exists() and updated_critique is not None:
        _write_text(critique_path, updated_critique)
    if notice_path.exists() and updated_notice is not None:
        _write_text(notice_path, updated_notice)
    if citation_cff_path.exists() and updated_citation is not None:
        _write_text(citation_cff_path, updated_citation)
    _write_text(changelog_path, updated_changelog)

    if args.build:
        _run(["make"], cwd=repo_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
