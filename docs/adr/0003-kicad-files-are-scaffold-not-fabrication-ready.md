---
title: "ADR-0003: KiCad Files Are Scaffold, Not Fabrication-Ready"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, kicad, pcb]
backlinks:
  - "[[CONTEXT]]"
  - "[[hardware/yadiggg_pcba_v1_layout_guidelines]]"
  - "[[docs/schematic-status]]"
---

# ADR-0003: KiCad Files Are Scaffold, Not Fabrication-Ready

## Status
Accepted

## Context
The generated KiCad project was created from scripts during the chat. It includes a project file, master schematic, sub-sheets, and PCB outline. KiCad parser errors were fixed, but the files do not contain placed real symbols, footprints, nets, ERC-clean circuits, routed traces, or manufacturable Gerber outputs.

## Decision
The current KiCad files are a scaffold only:

- `hardware/yadiggg.kicad_pro` is a project shell.
- `hardware/yadiggg.kicad_sch` and sub-sheets are empty hierarchical pages.
- `hardware/yadiggg.kicad_pcb` contains a board outline and comments, not routed hardware.
- `scripts/generate_kicad_project.py` is useful as a generator but should not overwrite hand-edited KiCad work once real schematic capture begins.

## Consequences
- Do not describe the KiCad project as fabrication-ready.
- Do not generate Gerbers from this scaffold for manufacturing.
- Next valid PCB step is real schematic capture with symbols, footprints, nets, ERC, then board placement/routing and DRC.
