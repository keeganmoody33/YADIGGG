---
title: "ADR-0004: Crate IQ Files Are Archival Inputs"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, archive, crate-iq]
backlinks:
  - "[[CONTEXT]]"
  - "[[yadiggg_strategic_decision_map_and_roadmap]]"
---

# ADR-0004: Crate IQ Files Are Archival Inputs

## Status
Accepted

## Context
The root workspace contains older Crate IQ PDFs, extracted text, and rendered-page image files. Many extracted text files contain only `[No text found on this page]`. Current yadiggg specs supersede many Crate IQ naming and design assumptions, but the old files may still be useful as provenance/reference.

## Decision
Treat Crate IQ files as archival inputs, not active specifications.

Recommended handling:

- Keep the original PDFs in an archive/reference folder.
- Keep rendered pages only if needed for visual review; otherwise mark as derived/cache.
- Treat extracted text files with no OCR text as failed extraction artifacts and archive or delete later after user approval.
- Promote any still-valid Crate IQ content into active yadiggg Markdown or ADRs before using it.

## Consequences
- Current design decisions should cite active yadiggg docs/ADRs, not Crate IQ PDFs directly.
- Obsidian Graph View should not use every Crate IQ render as an active node.
