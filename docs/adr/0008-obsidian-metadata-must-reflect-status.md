---
title: "ADR-0008: Obsidian Metadata Must Reflect Status"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, obsidian, metadata]
backlinks:
  - "[[CONTEXT]]"
  - "[[yadiggg_vault_overview]]"
---

# ADR-0008: Obsidian Metadata Must Reflect Status

## Status
Accepted

## Context
A previous backlink pass marked many Markdown files as `status: completed`, even when some are scaffolds, prototypes, or reference-only. This caused Graph View to become more connected but not more truthful.

## Decision
Obsidian frontmatter must distinguish status from graph connectivity. Use these statuses:

- `authoritative`: current source of truth.
- `active-draft`: actively useful but incomplete.
- `scaffold`: generated structure, not validated implementation.
- `prototype`: working exploration, not production.
- `reference`: useful input or visual reference.
- `superseded`: kept only for provenance.
- `archive-candidate`: likely to move out of active vault after review.

## Consequences
- Backlinks are not enough; status and role must be accurate.
- Cleanup should update frontmatter before any file moves.
