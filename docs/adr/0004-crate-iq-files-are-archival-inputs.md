---
title: "ADR-0004: Crate IQ Files Are Archival Inputs"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, archive, crate-iq]
---

# ADR-0004: Crate IQ Files Are Archival Inputs

## Status
Accepted

## Context
The root workspace contains older Crate IQ PDFs, extracted text, and rendered-page image files. Many extracted text files contain only `[No text found on this page]`. Current yadiggg specs supersede many Crate IQ naming and design assumptions, but the old files may still be useful as provenance/reference.

## Decision
Treat Crate IQ files as archival inputs, not active specifications.

Recommended handling:

- Preserve original PDFs under `archive/legacy-crate-iq/source-pdfs/` and page renders under `archive/rendered-pages/`.
- Remove only generated failed-extraction text that contains no recovered text; retain the source PDFs.
- Record moves and exact duplicate removals in `archive/README.md`.
- Reassess any historical idea against the current product specification and readiness register before reusing it.

## Consequences
- Current design decisions should cite active yadiggg docs/ADRs, not Crate IQ PDFs directly.
- Archived Crate IQ files are provenance, not current requirements or approved design inputs.
