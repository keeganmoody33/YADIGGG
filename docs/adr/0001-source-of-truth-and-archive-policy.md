---
title: "ADR-0001: Source of Truth and Archive Policy"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, source-of-truth, obsidian]
backlinks:
  - "[[CONTEXT]]"
  - "[[yadiggg_vault_overview]]"
---

# ADR-0001: Source of Truth and Archive Policy

## Status
Accepted

## Context
The workspace contains a mixture of active yadiggg specifications, older Crate IQ PDFs, extracted text files that contain no OCR text, rendered-page images, generated KiCad scaffolds, Yocto scaffolds, compiled build outputs, and visual renderings. Obsidian Graph View showed many disconnected nodes because decisions were not captured as stable decision records and many files were labeled as final without a clear role.

## Decision
The active source of truth is:

1. `CONTEXT.md` for domain language, current terms, and cross-document navigation.
2. `docs/adr/` for committed decisions and reasons.
3. Active Markdown specifications that are linked from `yadiggg_vault_overview.md` and `CONTEXT.md`.
4. Active implementation files under `src/`, `hardware/`, `scripts/`, and `yocto-meta/`, but only with the maturity status stated in the cleanup report.

Older Crate IQ PDFs and rendered-page image exports are archival inputs, not current source-of-truth files. They should remain accessible but should not drive current design unless explicitly promoted into an ADR or active spec.

## Consequences
- Future decisions must be recorded as ADRs instead of being buried in chat or narrative docs.
- Files can remain in the vault without being treated as active if their frontmatter/status marks them as archival, reference, scaffold, or superseded.
- Obsidian Graph View should center on `CONTEXT.md`, `yadiggg_vault_overview.md`, and `docs/adr/` rather than treating every PDF/render as equally authoritative.
