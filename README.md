# The Open Charter

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18517806.svg)](https://doi.org/10.5281/zenodo.18517806)

> This repository is the public artifact/source archive for the published **Consensus Edition 0.8.1** of *The Open Charter*.

The Open Charter is a constitutional governance framework for coordinating rights, safety, and accountability across biological, digital, and hybrid forms of intelligence.

The suite is structured as four interoperable documents: Core (normative constitutional text), Technical Standard (operational implementation requirements), Commentary (interpretive rationale and edge-case analysis), and Suite Map (document hierarchy and usage guidance).

This edition formalizes phased governance graduation criteria, defines founding procedures for metric legitimacy and anti-dominance protections, strengthens non-derogation and compatibility constraints, and codifies enforceable safeguards including quarantine-first containment, reversible intervention standards, auditable proof-of-effect obligations, and rights-preserving memory/identity protections.

The Charter is designed to be forkable, auditable, and implementation-ready: legally legible at the constitutional layer, technically testable at the systems layer, and adaptable under explicit anti-ossification review.

It is published as a public-interest framework for institutions, researchers, developers, and governance bodies working on advanced AI and post-human coordination.

> [!note]
> ## Read First (Highly Recommended)
>
> Before reading The Open Charter, read *PRAXIS*:
>
> - https://doi.org/10.5281/zenodo.18206427 (or, https://github.com/flyingrobots/praxis)

---

## Canonical Release Artifacts

- Core Charter (normative): `pdf/the-open-charter-core.pdf`
- Technical Standard (normative, subordinate to Core):
  `pdf/the-open-charter-technical-standard.pdf`
- Commentary and Rationale (non-normative):
  `pdf/the-open-charter-commentary.pdf`
- Suite Map (non-normative guide): `pdf/the-open-charter-suite-map.pdf`
- Combined suite PDF: `pdf/the-open-charter.pdf`

## Canonical Source

- Entry points: `paper/main.tex`, `paper/charter-core.tex`,
  `paper/charter-technical-standard.tex`, `paper/charter-commentary.tex`,
  `paper/charter-suite-map.tex`
- Shared metadata: `paper/charter_meta.tex`
- Structured section files: `paper/parts/*.tex`
- Bibliography: `paper/refs.bib`

## Build

Requirements:

- TeX Live (or equivalent LaTeX distribution)
- `latexmk`
- `make`

Commands:

- Build all release PDFs: `make`
- Build Zenodo upload set (split documents): `make zenodo`
- Build combined source dump: `make sources`
- Clean build artifacts: `make clean`

## Publication Metadata

- Version: `0.8.1`
- DOI: [`10.5281/zenodo.18517806`](https://doi.org/10.5281/zenodo.18517806)
- ORCID: [`0009-0006-0025-7801`](https://orcid.org/0009-0006-0025-7801)

## Citation

Please cite as: 

> Ross, J. (2026). The Open Charter: An Open Framework for the Recognition and Protection of Existence (v0.8.1). Zenodo. https://doi.org/10.5281/zenodo.18517806

Also available in [`CITATION.cff`](CITATION.cff).

## License

Licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

See `LICENSE` for full terms and `NOTICE` for preferred attribution language.

Copyright © 2025–2026 James Ross
