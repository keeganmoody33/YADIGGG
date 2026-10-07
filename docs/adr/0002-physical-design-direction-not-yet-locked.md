---
title: "ADR-0002: Physical Design Direction Is Not Yet Locked"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, physical-design, industrial-design]
---

# ADR-0002: Physical Design Direction Is Not Yet Locked

## Status
Accepted

## Context
The workspace contains visual renderings and brand/application mockups, but the user identified that the physical direction is not actually aligned yet. The renderings do not establish a reliable physical product direction, enclosure geometry, control placement, camera/sensor placement, internal packaging, or manufacturable industrial design.

## Decision
Treat current images and rendering documents as visual references only. They are not locked industrial design specifications.

The physical design remains unresolved until a dedicated physical direction package exists with:

- Enclosure dimensions and variants.
- Front/back/side orthographic references.
- Button, display, port, camera, microphone, speaker/DAC jack, and antenna placements.
- Internal stack layout: PCBA, battery, shield cans, lens barrel, grommets, haptic actuator, fasteners.
- Material/color/finish callouts reconciled with brand direction.
- Constraints that are reflected in KiCad board outline and mechanical CAD.

## Consequences
- `yadiggg_renderings_and_use_cases.md` must not be treated as manufacturing truth.
- Physical design work should be split into a new active package before further PCB placement/routing claims are made.
- KiCad geometry should remain a scaffold until physical direction is locked.
