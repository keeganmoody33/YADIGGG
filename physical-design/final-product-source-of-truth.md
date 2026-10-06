---
title: "Final Product Source of Truth"
project: yadiggg
status: authoritative
type: product_design_source_of_truth
tags: [yadiggg, final-product, industrial-design, logo, render, cad, source-of-truth]
backlinks:
  - "[[CONTEXT]]"
  - "[[docs/project-state]]"
  - "[[physical-design/physical-direction-brief]]"
  - "[[physical-design/visual-consistency-audit]]"
  - "[[physical-design/placement-sketch]]"
  - "[[physical-design/render-consistency-protocol]]"
  - "[[physical-design/cad-block-model-brief]]"
  - "[[physical-design/logo-refinement-round-1]]"
  - "[[docs/adr/0011-provisional-v1-physical-direction-assumptions]]"
---

# yadiggg Final Product Source of Truth

## Purpose

This document consolidates the current yadiggg product direction into one source of truth for visual design, logo direction, CAD translation, and product-development next steps.

It exists to prevent drift across:

- AI product renders
- logo iterations
- CAD/block-model work
- technical documentation
- future PCB/enclosure decisions
- marketing visuals
- social/launch assets

## Current Verdict

The current final direction is strong enough to treat as the **V1 industrial-design and brand target**, but not yet as production CAD or manufacturing truth.

In plain language:

> yadiggg is becoming a compact, portrait-first, smoke-clear pocket field recorder for vinyl crate digging. The product identity is now coherent: translucent hardware, monochrome waveform UI, one amber side control, restrained visible electronics, and a shovel-speaker logo system that connects crate digging with acoustic/audio intelligence.

The biggest remaining gap is no longer visual identity. The gap is now **engineering translation**:

1. convert the selected visual direction into CAD,
2. validate the internal stack,
3. reconcile electronics/BOM,
4. decide cloud EDA path,
5. move from concept renders to measured mechanical/PCB constraints.

## Product Form Factor — Current Lock

Use this as the product root statement:

> yadiggg is a compact, portrait-first, 105mm x 60mm x 15mm-class pocket field recorder for vinyl crate digging, with a smoke-clear translucent polycarbonate shell, large monochrome Sharp Memory LCD on the upper front face, one durable amber/orange side thumb control, visible but restrained dark internal electronics, USB-C bottom port, optional 3.5mm jack if fit allows, tiny acoustic mic ports, and a provisional rear OCR/macro camera aperture. No keypad, no Crate IQ branding, no bulky walkie-talkie silhouette, no generic spade logo, and no production-ready claims.

### Locked Product Traits

| Area | Current direction | Status |
|---|---|---:|
| Product name | `yadiggg` | locked |
| Product category | pocket field recorder / crate-digging assistant | locked |
| Orientation | portrait-first | locked |
| Envelope | 105mm x 60mm x 15mm-class | provisional canonical |
| Shell | smoke-clear translucent polycarbonate | visual lock; material grade TBD |
| Display | large monochrome Sharp Memory LCD on upper front | visual lock; exact part TBD |
| Primary control | one amber/orange side thumb control | visual lock; mechanism TBD |
| Internals | visible but restrained dark electronics | visual lock |
| Bottom edge | USB-C, optional 3.5mm if fit allows | provisional |
| Acoustic input | tiny mic ports | provisional placement |
| Optical input | rear OCR/macro camera aperture | provisional / opportunity-cost decision pending |
| Branding | subtle `yadiggg`; no Crate IQ | locked |

## Current Product Image Set

### Canonical product render sheet

File: `media-output/img-muk3t1qo-4a903520.png`

![Orthographic render sheet](../media-output/img-muk3t1qo-4a903520.png)

Use for:

- visual consistency checks
- mechanical layout conversation
- top-level product presentation
- CAD translation reference

Observed strengths:

- Front, back, side, and bottom views are shown together.
- Smoke-clear shell is consistent.
- Portrait-first recorder form is clear.
- Large front display and amber side control are visible.
- Bottom USB-C and 3.5mm language are represented.

Known limitations:

- Exact dimensions remain visual/provisional unless rebuilt in CAD.
- Internal board placement is still AI-implied.
- Camera/mic placements need validation.

### Studio hero render

File: `media-output/img-muk3t2an-1c1e856c.png`

![Studio hero render](../media-output/img-muk3t2an-1c1e856c.png)

Use for:

- website hero
- investor/product deck
- industrial-design direction
- product mood board

Observed strengths:

- Strong premium smoke-clear material feel.
- Large monochrome display is legible and emotionally on-target.
- Side amber control is visible.
- Internal electronics read restrained, not toy-like.

Known limitations:

- Does not show all ports or rear features.
- Should not be used as sole mechanical reference.

### Exploded stack render

File: `media-output/img-muk3tf3s-dd2a5029.png`

![Exploded stack render](../media-output/img-muk3tf3s-dd2a5029.png)

Use for:

- conceptual internal architecture
- CAD block-model planning
- investor explanation
- technical storytelling

Observed strengths:

- Communicates layered assembly well.
- Shows shell, display, PCBA, battery, side control, USB-C, optional 3.5mm, rear aperture concepts.
- Good bridge between rendering and mechanical design.

Known limitations:

- Not a verified BOM or PCB layout.
- Component proportions are illustrative.
- Labels are conceptual, not authoritative part choices.

### Lifestyle render

File: `media-output/img-muk3u79p-5263ad31.png`

![Crate-digging lifestyle render](../media-output/img-muk3u79p-5263ad31.png)

Use for:

- use-case storytelling
- ecommerce/social visuals
- brand narrative
- launch-page context

Observed strengths:

- Clearly places yadiggg in a vinyl crate-digging workflow.
- Shows one-handed pocketable scale.
- Display, shell, and side control remain consistent.

Known limitations:

- Lifestyle image is not geometry truth.
- Device scale should be checked against CAD once modeled.

## Current Logo Direction

### Preferred current logo reference

File: `media-output/img-muvo7mgq-aeae663b.png`

![Current logo direction](../media-output/img-muvo7mgq-aeae663b.png)

This is the current preferred logo direction after simplification.

It combines:

- expressive shovel-speaker icon energy,
- orange handle,
- simplified red/orange speaker cone,
- green upward/right sound-wave energy,
- clean technical `yadiggg` wordmark.

### Logo traits to preserve

| Trait | Requirement |
|---|---|
| Wordmark | exact lowercase `yadiggg` |
| Font feel | clean, technical, geometric, hardware-compatible |
| Icon | shovel-speaker hybrid, not a generic spade |
| Speaker | simplified red/orange cone, not over-detailed |
| Waves | green, moving up/right, not vertical parentheses |
| Background | light/cream for current master presentation |
| Use case | product, docs, boot screen, packaging, merch |

### Remaining logo refinements

The logo system is close, but not finished enough for final vector assets.

Next refinements:

1. Convert to vector or vector-like master.
2. Create full-color master.
3. Create one-color dark version.
4. Create one-color light version.
5. Create icon-only mark.
6. Create horizontal lockup.
7. Create stacked lockup.
8. Test at tiny sizes: boot screen, shell marking, app icon, favicon.
9. Reduce or tune wave count for small marks.
10. Make shovel head slightly less shield-like while keeping speaker read.

## Image / Logo Iteration Ledger

### Current preferred assets

| Role | File | Status | Use |
|---|---|---:|---|
| Product orthographic sheet | `media-output/img-muk3t1qo-4a903520.png` | current | product reference / CAD bridge |
| Product hero render | `media-output/img-muk3t2an-1c1e856c.png` | current | hero visual |
| Exploded stack | `media-output/img-muk3tf3s-dd2a5029.png` | active-draft | concept architecture |
| Lifestyle render | `media-output/img-muk3u79p-5263ad31.png` | current | use-case visual |
| Logo master direction | `media-output/img-muvo7mgq-aeae663b.png` | current | brand direction |

### Logo iteration history

| File | Read | Status |
|---|---|---:|
| `media-output/img-mujspg9r-88019fbf.png` | hardware badge mark; clean dark-background direction | reference |
| `media-output/img-mujspi8y-83e51195.png` | expressive underground signal mark; strong energy | reference |
| `media-output/img-mujspgo1-16f6e9df.png` | technical wordmark lockup; clean font reference | reference |
| `media-output/img-muvkcmn8-8e7e3d33.png` | shovel/speaker refinement attempt | superseded |
| `media-output/img-muvkfahw-9302c363.png` | cleaner speaker refinement | superseded |
| `media-output/img-muvlkhkf-cfed2f8e.png` | expressive icon + technical wordmark | reference |
| `media-output/img-muvlodmx-1319d06c.png` | stronger speaker origin but less selected | superseded |
| `media-output/img-muvlpiy4-b5e98d7f.png` | expressive icon + technical wordmark alternate | reference |
| `media-output/img-muvo7mgq-aeae663b.png` | simplified speaker detail | current |

### Deprecated visual directions

Do not use these as future design truth:

- amber keypad mini-synth render,
- horizontal Crate IQ slab layouts,
- generic spade/record logo,
- any image with `Crate IQ` branding,
- bulky walkie-talkie silhouettes,
- visuals with dense front keypad controls,
- visuals claiming production-ready status.

## CAD / Mechanical State

Current CAD source files:

- `physical-design/cad-block-model-brief.md`
- `physical-design/cad/yadiggg_v1_block_model.scad`

Current CAD state:

| Area | Status |
|---|---:|
| Envelope | defined as 105mm x 60mm x 15mm-class |
| Coordinate system | defined |
| Exterior block model | drafted as OpenSCAD source |
| Render/export | not generated locally; OpenSCAD not installed during last attempt |
| STEP/STL | not yet exported |
| Onshape/Fusion model | not yet created |
| Internal stack | bounding boxes drafted, not validated |
| PCB keepouts | not yet translated into PCB CAD |

### CAD next action

The next mechanical step is not another AI render. It is:

> Open or recreate the block model in Onshape, Fusion 360, FreeCAD, or OpenSCAD, then export measured front/back/side/bottom views and STEP/STL.

Minimum CAD deliverables:

1. front orthographic view,
2. rear orthographic view,
3. right-side control view,
4. bottom port view,
5. exploded stack placeholder,
6. STEP or STL export,
7. updated screenshots checked against this document.

## EDA / PCB Direction

KiCad remains scaffold/reference, not fabrication truth.

Current likely cloud EDA paths:

1. Flux.ai — best cloud-first, AI-assisted rebuild candidate.
2. EasyEDA Pro — best practical manufacturing-oriented online path.
3. KiCad — keep files as reference/scaffold unless local setup is fixed.

Do not treat current KiCad files as manufacturing-ready.

Before real PCB layout:

1. finalize CAD block model,
2. define PCB outline/keepouts,
3. reconcile BOM-current,
4. validate display, battery, USB-C, jack, side control, mic, camera, antenna placement,
5. rebuild schematic in selected EDA tool.

## Final Product Development Path

### Phase 1 — Visual system lock

Status: nearly complete.

Required remaining tasks:

- [ ] Create logo vector package.
- [ ] Create one-color logo variants.
- [ ] Create app/boot-screen icon variant.
- [ ] Create final render contact sheet.
- [ ] Archive superseded image iterations.

### Phase 2 — CAD block model

Status: drafted, not executed.

Required tasks:

- [ ] Open/recreate `yadiggg_v1_block_model.scad` in CAD.
- [ ] Export measured views.
- [ ] Validate port/control/display locations.
- [ ] Decide if rear OCR/macro camera stays.
- [ ] Decide whether 3.5mm jack physically fits.
- [ ] Create mechanical keepout notes for PCB.

### Phase 3 — Electronics reconciliation

Status: active-draft/scaffold.

Required tasks:

- [ ] Create `docs/bom-current.md`.
- [ ] Confirm display module.
- [ ] Confirm audio path.
- [ ] Confirm mic architecture.
- [ ] Confirm SoC/MCU/module direction.
- [ ] Confirm battery/charging approach.
- [ ] Confirm side control mechanism.
- [ ] Confirm USB-C and optional 3.5mm implementation.

### Phase 4 — Cloud EDA rebuild

Status: not started.

Required tasks:

- [ ] Choose Flux.ai or EasyEDA Pro.
- [ ] Rebuild schematic from current docs.
- [ ] Translate CAD keepouts into board constraints.
- [ ] Generate PCB layout.
- [ ] Export neutral manufacturing package.

### Phase 5 — Prototype package

Status: not started.

Required tasks:

- [ ] Export PCB Gerber/drill/BOM/PnP.
- [ ] Export enclosure STEP/STL.
- [ ] Create assembly notes.
- [ ] Create visual/product spec sheet.
- [ ] Create supplier/manufacturer inquiry package.

## What We Think Right Here

The current direction is coherent and worth locking.

### Strongest decisions

1. The product should be portrait-first, not horizontal.
2. The shell should stay smoke-clear/translucent.
3. The front should be dominated by a monochrome waveform/display UI.
4. The side amber control is a strong identity anchor.
5. The shovel-speaker logo is the right brand metaphor.
6. The clean technical `yadiggg` wordmark is better than the rough brush wordmark for master identity.
7. The simplified speaker cone is better for real hardware branding.

### Biggest risks

1. Rear OCR/macro camera may add mechanical/electrical complexity.
2. 3.5mm jack may not fit comfortably in 15mm thickness.
3. Exact display/battery/PCB stack is not validated.
4. Logo still needs vectorization and small-size testing.
5. AI renders may imply details that are not CAD-verified.
6. KiCad project is scaffold, not manufacturable.

### Recommended immediate next move

Do not generate more broad product renders right now.

Instead:

1. finalize logo vector package,
2. create CAD block model views,
3. create a final product contact sheet,
4. archive superseded visuals,
5. then choose Flux.ai or EasyEDA Pro for schematic rebuild.

## Current Final Statement

> yadiggg V1 is a compact smoke-clear pocket field recorder for vinyl crate digging, built around a large monochrome waveform display, one amber side thumb control, restrained visible internals, and a shovel-speaker brand mark. The visual identity is now coherent. The next phase is mechanical and electrical truth: CAD block model, BOM reconciliation, and cloud EDA rebuild.
