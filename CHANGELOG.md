# Changelog

All notable changes to *The Open Charter* will be documented in this file.

This project follows Semantic Versioning for draft iterations (MAJOR.MINOR.PATCH).

## [Unreleased]

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
