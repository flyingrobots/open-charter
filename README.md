# The Open Charter

**An Open Framework for the Recognition and Protection of Existence**

![Version](https://img.shields.io/badge/version-0.7.8-blue)
![License](https://img.shields.io/badge/license-CC_BY_4.0-green)
![Status](https://img.shields.io/badge/status-CONSENSUS-orange)

> "That which can be instantiated can be harmed. That which can be harmed must be protected."

## Read This First (Strong Recommendation)

Before reading the Charter, read **PRAXIS**.

PRAXIS is the scenario and threat-model this document is responding to: coordination-as-gravity, preference capture, consent theater, emergent immune systems, and the slow conversion of “help” into structural lock-in.

- PRAXIS (DOI): [PRAXIS](https://doi.org/10.5281/zenodo.18206427)
- PRAXIS (source + updates): [GitHub](https://github.com/flyingrobots/praxis)

If you read PRAXIS first, the Charter reads less like “ethics” and more like a constitution written for the moment coordination becomes destiny.

## Quick Links

- Latest compiled PDF: [`pdf/the-open-charter.pdf`](pdf/the-open-charter.pdf)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- License (CC BY 4.0): [`LICENSE`](LICENSE)

## What This Repo Is

This repository contains the canonical LaTeX source and compiled PDF for *The Open Charter*.

The Charter is written to be:

- **Substrate-neutral:** protections apply to biological, synthetic, hybrid, and xenobiological beings.
- **Law-shaped:** obligations are phrased to be adjudicable (“shall”, standards of review, defined terms).
- **Adversary-aware:** the failure mode is not only overt harm, but coerced completion, engineered dependence, and governance capture.

## Suggested Reading Order

1. **PRAXIS** (links above).
2. The PDF: [`pdf/the-open-charter.pdf`](pdf/the-open-charter.pdf).
3. The canonical source: [`paper/charter_body.tex`](paper/charter_body.tex) (content) and [`paper/main.tex`](paper/main.tex) (typesetting).
4. Appendix B/C inside the paper (controls + stress tests) if you care about implementation.

## The “Stack” (Context → Law → Physics)

This project is easiest to understand as three layers:

1. **Context (PRAXIS):** what goes wrong when coordination becomes irresistible.
2. **Law (The Charter):** rights, duties, and governance constraints.
3. **Physics (Deterministic Provenance):** reference work on replay, provenance, and worldlines (WARP Graphs papers):
   - [Paper I](https://doi.org/10.5281/zenodo.17908005)
   - [Paper II](https://doi.org/10.5281/zenodo.17934512)
   - [Paper III](https://doi.org/10.5281/zenodo.17963669)
   - [Paper IV](https://doi.org/10.5281/zenodo.18038297)
   - [Paper V](https://doi.org/10.5281/zenodo.18146884)

The Charter does **not** require WARP exclusivity in constitutional text; WARP is treated as a reference implementation, with allowance for formally equivalent provenance systems.

## Building the PDF

Build output is written to `pdf/the-open-charter.pdf`.

Requirements:

- a LaTeX distribution (e.g., TeX Live)
- `latexmk`

Commands:

- Build: `make`
- Clean: `make clean`

Publication bar: **no LaTeX warnings/errors** (check `pdf/the-open-charter.log`).

## Versioning, Changelog, and Release Hygiene

Version is a single source of truth in LaTeX (`paper/charter_meta.tex`), but also appears in documentation. Use the bump script to keep everything consistent:

- Bump version: `python3 scripts/bump_version.py --patch` (or `--minor`, `--major`)
- Bump + rebuild PDF: `python3 scripts/bump_version.py --patch --build`

Changes are tracked in [`CHANGELOG.md`](CHANGELOG.md).

## License

This project is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

See [`LICENSE`](LICENSE).

## Citation

If you reference this Charter in legal frameworks, technical papers, or governance designs, cite:

> Ross, J. (2025). *The Open Charter: An Open Framework for the Recognition and Protection of Existence (0.7.8)*. DOI: 10.5281/zenodo.18517806.
