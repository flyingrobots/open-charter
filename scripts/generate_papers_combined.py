#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _iter_paper_sources(repo_root: Path, paper_dir: Path) -> list[Path]:
    output_path = paper_dir / "papers_combined.txt"

    candidates: list[Path] = []
    for ext in (".tex", ".bib"):
        candidates.extend(paper_dir.rglob(f"*{ext}"))

    def sort_key(p: Path) -> tuple[int, str]:
        rel = p.relative_to(repo_root).as_posix()
        priority = {
            "paper/main.tex": 0,
            "paper/charter-core.tex": 1,
            "paper/charter-technical-standard.tex": 2,
            "paper/charter-commentary.tex": 3,
            "paper/charter-suite-map.tex": 4,
            "paper/charter_preamble.tex": 10,
            "paper/charter_meta.tex": 11,
            "paper/charter_body.tex": 12,
            "paper/charter_core_body.tex": 13,
            "paper/charter_technical_standard_body.tex": 14,
            "paper/charter_commentary_body.tex": 15,
            "paper/refs.bib": 20,
        }
        return priority.get(rel, 100), rel

    sources = [p for p in candidates if p.resolve() != output_path.resolve()]
    sources.sort(key=sort_key)
    return sources


def _format_combined(repo_root: Path, sources: list[Path]) -> str:
    out: list[str] = []
    for path in sources:
        rel = path.relative_to(repo_root).as_posix()
        out.append(f"# {rel}\n")
        content = _read_text(path)
        if content and not content.endswith("\n"):
            content += "\n"
        out.append(content)
        out.append("\n")
    return "".join(out)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate paper/papers_combined.txt (a single text file containing all LaTeX sources "
            "for the suite, formatted as '# <filename>\\n<file content>\\n'."
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional output path (defaults to paper/papers_combined.txt).",
    )
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    paper_dir = repo_root / "paper"
    output_path = Path(args.output).resolve() if args.output else (paper_dir / "papers_combined.txt")

    if not paper_dir.exists():
        raise RuntimeError("paper/ directory not found (run from within the repo)")

    sources = _iter_paper_sources(repo_root=repo_root, paper_dir=paper_dir)
    combined = _format_combined(repo_root=repo_root, sources=sources)
    _write_text(output_path, combined)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))

