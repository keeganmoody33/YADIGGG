---
title: "ADR-0009: Generators Must Not Overwrite Hand-Authored Work"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, generators, workflow]
backlinks:
  - "[[CONTEXT]]"
  - "[[scripts/generate_kicad_project]]"
  - "[[scripts/connect_obsidian_vault]]"
---

# ADR-0009: Generators Must Not Overwrite Hand-Authored Work

## Status
Accepted

## Context
Scripts in `scripts/` generated KiCad files and mass-injected Obsidian metadata. These are useful bootstrap tools, but repeated runs can overwrite manual KiCad work or erase carefully curated frontmatter.

## Decision
Generator scripts must be treated as bootstrap or migration tools. Before reuse, they must be made idempotent and safe against overwriting hand-authored files.

## Consequences
- Do not rerun `scripts/generate_kicad_project.py` after KiCad editing starts unless it gains backup/dry-run protection.
- Do not rerun `scripts/connect_obsidian_vault.py` until it is improved to preserve status, aliases, and custom metadata.
