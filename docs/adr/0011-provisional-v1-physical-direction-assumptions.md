---
title: "ADR-0011: Provisional V1 Physical Direction Assumptions"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, physical-design, v1, industrial-design]
backlinks:
  - "[[CONTEXT]]"
  - "[[docs/project-state]]"
  - "[[physical-design/physical-direction-brief]]"
  - "[[docs/adr/0002-physical-design-direction-not-yet-locked]]"
---

# ADR-0011: Provisional V1 Physical Direction Assumptions

## Status
Accepted as provisional direction

## Context
The physical direction brief had eight open review questions covering OCR/camera scope, thickness, color direction, form factor, usage scenarios, control type, headphone jack, and product logo placement. The user provided directional answers that should become the next handoff state without falsely treating the industrial design as fully locked.

## Decision
Use the following assumptions for the next physical-design pass:

1. **V1 should attempt OCR/camera plus Sonic ID**, not prematurely remove camera/OCR. The camera/OCR path should stay in V1 exploration as long as it remains feasible, but it is explicitly removable if it creates real space, cost, optical, routing, power, or reliability bottlenecks.
2. **First prototype targets the roomier physical package**, currently interpreted as the 15mm-class prototype rather than the 12mm slim variant. This is enclosure thickness, not copper stackup thickness.
3. **Color direction supports clear/smoke-clear core variants plus a limited-edition expressive colorway.** The core product should not depend on one loud color being universal.
4. **Form factor should feel closer to a modern voice recorder / compact field recorder** than a phone or pager: roughly 3–4 inches long, pocketable, one-handable, and durable.
5. **Use scenarios should support all identification modes**: holding a record, standing near a turntable, browsing crates one-handed, barcode/catalog scanning, visual/text identification, Sonic ID acoustic matching, and database/credits lookup.
6. **Primary physical input should prioritize durability and one-handed reliability** over novelty. The exact input is not locked; choose the most manufacturable/drop-resistant option after a durability trade study.
7. **Keep the 3.5mm jack if space allows.** It is desirable for V1, but should be evaluated against thickness, board edge space, internal stack, analog routing, and enclosure strength.
8. **Physical logo placement is deferred.** Branding will definitely exist on packaging/accessories, but on-device logo placement waits until the physical logo and enclosure surface strategy are refined.

## Consequences
- The next physical-design deliverable should be a placement sketch or block model, not final CAD.
- Camera/OCR needs a feasibility gate instead of being assumed free.
- A control durability matrix is required before selecting slider/button/rocker/wheel.
- The 3.5mm jack remains in the candidate internal stack, but must pass a space and strength check.
- KiCad board outline remains provisional until the voice-recorder-like envelope, ports, controls, camera, mics, jack, antenna, and battery are placed.

## Follow-up Work
1. Create a V1 physical placement sketch.
2. Create an OCR/camera opportunity-cost matrix.
3. Create a control durability matrix.
4. Create a 3.5mm jack fit check.
5. Reconcile these decisions into the BOM-current document before schematic capture.
