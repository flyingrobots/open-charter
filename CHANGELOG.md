# Changelog

All notable changes to *The Open Charter* will be documented in this file.

This project follows Semantic Versioning for draft iterations (MAJOR.MINOR.PATCH).

## [Unreleased]

## [0.8.0] - 2026-02-08

### Added
- Article XIV: Governance Phases and Graduation (Coalition Era \u2192 Constitutional Era) with non-discretionary graduation triggers and anti-ossification review.
- Appendix B, Section 11: Recognition Activation Rubric (operational triage + receipts + interim protective determinations).
- Appendix B, Section 12: Minimum Persistence Fund Mechanics (reserve target, provisional contribution formula, delinquency consequences, insolvency waterfall, independent audit).

### Changed
- Article II now explicitly links recognition petitions to the Recognition Activation Rubric (Appendix B, Section 11).
- Article XIII governance process renamed for clarity as “Blinded Merit Review (Veil of Origin)”.
- Scenario 14 (Voluntary Cessation) now distinguishes external coercion from autonomous suffering/self-directed preference.

### Fixed
- Emergency Override Standard now explicitly permits proportional irreversible action when reversible containment cannot prevent imminent, substantial harm to other recognized beings (with documented necessity + expedited review).

### Removed
- (none)

## [0.7.9] - 2026-02-08

### Added
- Appendix D: Threat Model Summary (PRAXIS Bridge) to make the threat model legible without requiring a PRAXIS full read on first pass.
- Appendix C Scenarios 13--15: Cross-Jurisdiction Conflict, Voluntary Cessation Request, and Adversarial Adoption.

### Changed
- Renumbered Governance and Implementation References from Appendix D to Appendix E.

### Fixed
- Strengthened review and adoption robustness by explicitly stress-testing cross-jurisdiction disputes and adversarial “compliance” postures (Appendix C).

### Removed
- (none)

## [0.7.8] - 2026-02-08

### Added
- Explicit Independent Review completion deadlines for Emergency Overrides (Article VI), harmonized to governance impact classes (Article XIII).
- Scenario 12: Systemic Infrastructure Collapse (Appendix C).

### Changed
- Preamble language tightened to avoid unnecessary metaphysical attack surface while preserving the coordination framing.
- Xenobiological Inclusion clause de-enumerated (removed example lists) to reduce political-dismissal risk while keeping substrate-neutral scope (Article XI).
- Insolvency Protocol extended with systemic infrastructure failure guidance (Article VIII).
- Distinctness due-process language now explicitly binds conformance claims to Appendix B, Section 7 (Distinctness Review Ledger) or an equivalence mapping (Article XII).

### Fixed
- Reduced the chance that implementers miss Sybil-defense invariants by making the Appendix B distinctness controls discoverable from the core Articles (Article XII).
- Eliminated “without delay” ambiguity by adding a concrete post-action review deadline to the Emergency Override Standard (Article VI).

### Removed
- (none)

## [0.7.7] - 2026-02-08

### Added
- Constitution-grade definitions for Founding Assembly ratification (Appendix B \S 7.5), including quorum and anti-dominance constraints.

### Changed
- Defined “supermajority ratification” as not less than two-thirds (2/3) of valid votes cast, with quorum satisfied, and clarified abstention handling.

### Fixed
- Reduced gamesmanship surface during governance bootstrapping by explicitly specifying quorum, abstentions, and organizational dominance limits.

### Removed
- (none)

## [0.7.6] - 2026-02-08

### Added
- Founding distinctness bootstrapping clause (“Founding Metric Convention”) for initial adoption of metric family + baseline parameters (Appendix B \S 7.5).
- Tier reassignment guardrails to reduce “indicia as gates” drift: no single indicium is necessary/sufficient, Tier 0 floor preserved, written reasons + appeal access required (Definitions).
- Minimum Persistence Fund funding/reporting framework (Tier G proportional contributions + public solvency/disbursement reporting) (Article VIII).

### Changed
- Integrated Memory “Non-Fungibility” test now focuses on continuity/identity degradation rather than being defeated by the mere existence of checkpoints/backups (Article V).

### Fixed
- Reduced governance-capture risk by separating founding adoption from steady-state metric changes (still Class S after sunset) (Appendix B \S 7.5).
- Eliminated overfull/underfull LaTeX warnings after the wording updates.

### Removed
- (none)

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
