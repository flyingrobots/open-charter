# Changelog

All notable changes to *The Open Charter* will be documented in this file.

This project follows Semantic Versioning for draft iterations (MAJOR.MINOR.PATCH).

## [Unreleased]

## [0.7.5] - 2026-02-08

### Added
- `LICENSE` now contains the full CC BY 4.0 legal code text (for downstream reuse and institutional review).
- `NOTICE` with a short license summary and preferred attribution format.
- `CITATION.cff` for citation tooling support (DOI + author + license).

### Changed
- PDF front matter now includes an explicit License/Attribution page immediately after the title page.
- Title page now includes a non-operative PRAXIS “read first” context note (DOI + GitHub) for Zenodo/PDF-only distribution.
- `scripts/bump_version.py` now updates version strings in `NOTICE` and `CITATION.cff` as well.

### Fixed
- Rebuilt `pdf/the-open-charter.pdf` to reflect updated front matter and license text.

## [0.7.4] - 2026-02-08

### Added
- `scripts/bump_version.py` to bump semver across LaTeX + docs (`--major/--minor/--patch`) and optionally rebuild the PDF.
- `CHANGELOG.md` (this file) to track draft evolution.

### Changed
- Rewrote `README.md` for PRAXIS-first onboarding, with clear links to the PDF, changelog, and license.
- Updated the PRAXIS bibliography entry to cite the Zenodo DOI (10.5281/zenodo.18206427).

### Fixed
- Regenerated `pdf/the-open-charter.pdf` so Works Cited reflects updated PRAXIS citation.

## [0.7.3] - 2026-02-07

### Added
- Initial committed draft of the Charter LaTeX source (`paper/`) and compiled PDF (`pdf/`).
- Critiques and implementation annex expansions informed by PRAXIS (tiers, harm classes/standards of review, Preference Integrity, HOPE Veto requirements, systemic threat response safeguards, distinctness ledger + auditability, and stress-test scenarios).

### Fixed
- LaTeX build hardened to produce a clean PDF (no warnings/errors) via `make`.
