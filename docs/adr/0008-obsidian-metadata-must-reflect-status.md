---
title: "ADR-0008: Obsidian Metadata Must Reflect Status"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, obsidian, metadata]
---

# ADR-0008: Obsidian Metadata Must Reflect Status

## Status
Superseded for current project status by `docs/project-state.md`.

## Context
A previous backlink pass marked many Markdown files as `status: completed`, even when some are scaffolds, prototypes, or reference-only. This caused Graph View to become more connected but not more truthful.

## Historical decision
The original Obsidian cleanup pass needed to distinguish status from graph connectivity. It proposed these labels:

- `authoritative`: current source of truth.
- `active-draft`: actively useful but incomplete.
- `scaffold`: generated structure, not validated implementation.
- `prototype`: working exploration, not production.
- `reference`: useful input or visual reference.
- `superseded`: kept only for provenance.
- `archive-candidate`: likely to move out of active vault after review.

## Consequences
- The repository now uses GitHub-readable links and the engineering readiness register as current status authority.
- Historical frontmatter labels do not imply verification, approval, or manufacturing release.
