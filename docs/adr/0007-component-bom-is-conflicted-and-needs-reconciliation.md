---
title: "ADR-0007: Component BOM Is Conflicted and Needs Reconciliation"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, bom, hardware]
backlinks:
  - "[[CONTEXT]]"
  - "[[docs/component-selections]]"
  - "[[yadiggg_hardware_and_electrical_integration]]"
---

# ADR-0007: Component BOM Is Conflicted and Needs Reconciliation

## Status
Accepted

## Context
Multiple active files contain incompatible part selections. Examples include PMIC choice, RAM/eMMC capacities, co-processor family, and microphone part numbers. `docs/component-selections.md` lists a different BOM than `yadiggg_hardware_and_electrical_integration.md`.

## Decision
The BOM is not authoritative until reconciled into one active `docs/bom-current.md` or equivalent.

## Consequences
- Do not order parts from any existing BOM table without reconciliation.
- The next hardware task should be BOM normalization: one part per function, reason, source link, package, availability, lifecycle, and KiCad symbol/footprint status.
