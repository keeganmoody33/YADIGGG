---
title: "ADR-0009: Generators Must Not Overwrite Hand-Authored Work"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, generators, workflow]
---

# ADR-0009: Generators Must Not Overwrite Hand-Authored Work

## Status
Accepted

## Context
Scripts in `scripts/` generated KiCad files and mass-injected Obsidian metadata. These are useful bootstrap tools, but repeated runs can overwrite manual KiCad work or erase carefully curated frontmatter.

## Decision
Generator scripts must be treated as bootstrap or migration tools. Before reuse, they must be made idempotent and safe against overwriting hand-authored files.

## Consequences
- `scripts/generate_kicad_project.py` refuses to overwrite existing files unless `--force` is explicitly supplied; it remains a scaffold generator, not an engineering validator.
- The destructive `scripts/connect_obsidian_vault.py` and hard-coded layer deployer were removed. The read-only `scripts/validate_yocto_layer.py` checks the checked-in recipe without writing files.
