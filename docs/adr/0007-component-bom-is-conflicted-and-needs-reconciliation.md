---
title: "ADR-0007: Component BOM Is Conflicted and Needs Reconciliation"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, bom, hardware]
---

# ADR-0007: Component BOM Is Conflicted and Needs Reconciliation

## Status
Accepted

## Context
Historical proposals contain incompatible part selections, including PMIC, RAM/eMMC capacities, co-processor family, and microphone part numbers. The former hardware proposal is preserved at `archive/historical-proposals/yadiggg_hardware_and_electrical_integration.md`.

## Decision
No purchasing BOM is approved. `manufacturing/draft-bom.csv` is a traceable candidate transcription; it must not be treated as selected parts until an electrical/BOM engineer reconciles and approves it.

## Consequences
- Do not order parts from any existing BOM table without reconciliation.
- Reconcile candidates against verified datasheets, schematic, layout, lifecycle/sourcing evidence, package, and approved substitutions.
- Record closure evidence and engineering review in the readiness register before ordering.
