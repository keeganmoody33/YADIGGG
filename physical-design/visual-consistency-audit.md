---
title: "Visual Consistency Audit"
project: yadiggg
status: active-draft
type: industrial_design_audit
tags: [yadiggg, visual-consistency, physical-design, industrial-design, form-factor]
backlinks:
  - "[[CONTEXT]]"
  - "[[docs/project-state]]"
  - "[[physical-design/physical-direction-brief]]"
  - "[[docs/adr/0011-provisional-v1-physical-direction-assumptions]]"
  - "[[yadiggg_brand_identity_and_design_guidelines]]"
  - "[[yadiggg_renderings_and_use_cases]]"
---

# yadiggg Visual Consistency Audit

## Purpose

The current product visuals are not consistent enough to use as a single industrial-design source of truth. This audit separates the visual assets into roles, identifies contradictions, and defines the recommended locked visual direction for the next physical-design pass.

This document should be used before generating new renderings, updating the tech pack, changing the KiCad board outline, or briefing a mechanical designer.

## Executive Finding

The visuals currently describe at least **three different products**:

1. **Amber transparent gadget / mini synth direction** — thick translucent amber block, visible internals, exposed large knurled cylinder, many front buttons, Sharp Memory LCD. Visually rich but inconsistent with the current one-control, voice-recorder-like physical direction.
2. **Crate IQ horizontal tech-pack direction** — 105mm x 60mm x 15mm horizontal slab with a right-side vertical display zone, rear camera, top/side orange button, USB-C, 3.5mm jack, microphones, translucent amber shell. More mechanically specified, but still branded as Crate IQ and internally inconsistent with the newer yadiggg direction.
3. **yadiggg compact voice-recorder direction** — 105mm-class pocket device with translucent smoke/clear shell, large front display, side orange control, back OCR/macro camera, tiny acoustic mic ports, corner RF antenna, USB-C and 3.5mm on bottom. This is the strongest candidate for the next locked direction.

The next step should **not** be another freeform render. The next step should be a controlled visual standard: one canonical form factor, one orientation system, one shell CMF, one control architecture, one port layout, and one logo-placement rule.

## Asset Inventory and Role Classification

| Asset | Observed content | Current role | Keep / reject decision |
|---|---|---:|---|
| `Downloads/image_1790508905600.png` | Multi-view grey translucent yadiggg device, 105mm x 60mm x 15mm, large front display, side orange control, rear camera, mic ports, RF antenna, USB-C + 3.5mm bottom | **Best canonical form-factor reference** | Keep as primary V1 visual direction candidate |
| `A635cb2ae39c0459eb58a46ec8bbd6ffbH.avif` | Line/spec drawing, horizontal Crate IQ body, 105mm x 60mm x 15mm, small right-side vertical LCD, camera/branding/front button/side view | Technical predecessor | Keep as reference only; do not use layout as final without revision |
| `A785a6969d2a046a2a18825402ad289f9f.avif` | Exploded view, amber top/bottom shell, LCD, PCBA, CNC aluminum frame, orange button, 1500mAh battery, two Knowles MEMS mics, USB-C and 3.5mm jack | Useful stack concept | Keep for internal-stack concept, but recolor/rebrand and correct geometry |
| `Aff28a8c6b74a43d18f19da841c804948X.avif` | Manufacturing/process flow using the amber Crate IQ slab | Process illustration | Keep as historical/reference; not canonical product appearance |
| `A2c312300cbc241a593033cc604f7deb5N.png` and duplicate | Amber transparent upright mini-gadget with visible internals, large knurled cylinder, many front keys, Sharp LCD | Visual inspiration only | Reject as canonical form factor; conflicts with current physical direction |
| `Adedd09730c9846ad95f9d82a4302401e8.png` | Horizontal smoke/amber Crate IQ back/side view with small dark side display, rear camera, top orange button | Earlier render | Keep as reference only; conflicts with yadiggg name and layout direction |
| `Ab0366a7e4d1c4f86ba5eb0a115a0dd80k.png` | Flat orange generic record/shovel/turntable logo | Deprecated logo exploration | Do not use as hardware identity source of truth |
| `IMG_3581_converted.png` / `yadigggsketch_rendered.png` | Hand sketch: shovel/speaker/record energy, black/red/green expression | Logo concept source | Keep as logo inspiration, not literal product-render style |
| `rendered_pages/Ya Diggg Official Tech Pack_p*.png` | Tech-pack pages claiming production-ready dimensions/materials/BOM/process | Outdated/speculative tech pack render | Keep as reference only; label not production-ready |

## Major Inconsistencies

### 1. Form factor conflict

The visuals alternate between:

- **upright rectangular device** with many front keys and a top cylinder,
- **horizontal slab** with a small vertical side display,
- **portrait voice-recorder-like block** with a large front display.

Only the third direction aligns with ADR-0011: compact field-recorder / voice-recorder-like, 3–4 inches long, pocketable, one-handable, durable.

### 2. Interface conflict

The current visuals show incompatible control systems:

- large multi-key keypad,
- top orange scan button,
- side orange button,
- large front orange square button,
- possible side slider/button.

This cannot be solved visually until the physical input is narrowed. For visual consistency now, the canonical rule should be: **one prominent amber/orange side control**, with any secondary controls hidden, minimized, or deferred.

### 3. Display conflict

The visuals show at least three display placements:

- front centered Sharp LCD under exposed internals,
- narrow vertical display on the right side of a horizontal slab,
- large landscape display on the upper front face of a portrait device.

Recommended direction: **large front display occupying the upper front face**, because it works with one-handed record-store use and matches the pocket instrument direction better than the side-strip display.

### 4. Color/material conflict

The visuals alternate between:

- smoke-grey translucent shell,
- amber translucent shell,
- smoky brown/black casing,
- bright orange logo-on-black branding.

Recommended CMF hierarchy:

1. **Core product**: smoke-clear / grey translucent polycarbonate.
2. **Accent**: amber/orange physical control.
3. **Limited edition**: amber translucent shell, but not the canonical baseline.
4. **Internal visibility**: matte black PCB/shields where possible to avoid visual clutter through shell.

### 5. Branding/name conflict

Several visuals still show **Crate IQ**, while the current project and brand language are **yadiggg**. This creates identity drift.

Canonical rule: product visuals must not show `Crate IQ` except in archival/reference material. New renders should use either:

- no visible logo, if on-device logo remains deferred, or
- a subtle `yadiggg` mark consistent with the final shovel-speaker identity.

### 6. Logo concept conflict

The logo references are not aligned:

- `Ab0366...png` reads as a polished but generic orange record/shovel/turntable mark.
- `IMG_3581_converted.png` / `yadigggsketch_rendered.png` read as a rough expressive sketch of shovel + red speaker cone + sound/light arcs.
- Brand docs currently describe a shovel-speaker-neon-wave mark, but the polished logo image does not fully match that description.

Canonical rule: do not force a large on-device logo into form-factor visuals until the logo itself is vectorized and resolved. Keep branding subtle or absent in product body renders.

### 7. Camera/OCR conflict

Some images include a rear camera/macro lens. The upright amber mini-gadget does not clearly resolve camera placement. The physical brief says camera/OCR is still being explored, not locked.

Canonical rule: V1 visuals may include a **single rear OCR/macro camera aperture**, but must mark it as provisional until the OCR/camera feasibility gate is complete.

### 8. Port conflict

The strongest recurring port set is USB-C + 3.5mm jack on the bottom edge. That aligns with current goals, but the headphone jack remains conditional on fit.

Canonical rule: show USB-C as locked candidate; show 3.5mm as desired/provisional until jack fit check passes.

## Recommended Canonical Product Direction

### Product archetype

A **compact translucent field-recorder-like pocket instrument** for crate digging.

It should not read as:

- a phone,
- a pager,
- a walkie-talkie,
- a mini keyboard/synth,
- a generic transparent gadget,
- or a packaging/merch object.

### Envelope

Use the 105mm x 60mm x 15mm envelope as the **current visual target**, not as final mechanical truth.

| Dimension | Canonical visual target | Lock status |
|---|---:|---:|
| Height/length | 105mm | provisional target |
| Width | 60mm | provisional target |
| Depth/thickness | 15mm | prototype target |
| Corner radius | rounded, pocket-safe | needs exact value |
| Orientation | portrait-first front face | recommended |

### Front face

Canonical visual requirements:

- Large Sharp Memory LCD in upper front area.
- Subtle visible internals beneath/around display through smoke-clear shell.
- One amber/orange physical control reachable by thumb on side or front-side edge.
- No dense keypad.
- No exposed knurled metal cylinder on top/front.
- Logo deferred or subtle; do not dominate front face.

### Side profile

Canonical visual requirements:

- 15mm-class depth.
- Rounded translucent shell perimeter.
- One amber/orange side control visible.
- Avoid large protruding controls that snag in pocket.

### Back face

Canonical visual requirements:

- Mostly clean translucent back shell.
- Single rear OCR/macro camera aperture if retained for V1 exploration.
- Tiny acoustic mic ports at top/edge or another acoustically justified location.
- Corner RF antenna area may be visually indicated only in technical drawings, not lifestyle renders.

### Bottom edge

Canonical visual requirements:

- USB-C centered or slightly offset based on internal stack.
- 3.5mm jack beside USB-C only if fit/strength check passes.
- No unexplained extra holes or decorative ports.

### CMF

| Element | Canonical direction |
|---|---|
| Shell | smoke-clear / grey translucent polycarbonate |
| Accent control | amber/orange silicone or textured plastic |
| Display | monochrome Sharp Memory LCD look |
| Internals visible through shell | dark/matte black PCB and shield language where possible |
| Limited edition | amber translucent shell allowed only as secondary colorway |
| Logo | subtle/deferred; not a giant front graphic |

## Asset Acceptance Matrix

A visual asset is accepted as canonical only if it passes these checks:

| Check | Requirement |
|---|---|
| Name | Uses yadiggg or no visible name; never Crate IQ for current visuals |
| Form | 105mm-class compact voice-recorder-like body |
| Orientation | Portrait-first product logic unless explicitly marked as alternate view |
| Display | Large front display, not tiny side strip |
| Controls | One dominant amber/orange control; no keypad unless a new ADR approves it |
| Shell | Smoke-clear / grey translucent baseline |
| Internals | Visible but controlled; not busy novelty transparency |
| Camera | Single rear aperture if present; clearly provisional |
| Mics | Tiny acoustic ports with plausible placement |
| Ports | USB-C; 3.5mm only as fit-dependent candidate |
| Logo | Deferred/subtle; no generic spade/turntable logo as device identity |
| Status | Must not claim production-ready until mechanical/BOM/KiCad validation exists |

## Source-of-Truth Ranking

Use this order when visual references conflict:

1. `physical-design/visual-consistency-audit.md` — this audit, for visual consistency rules.
2. `physical-design/physical-direction-brief.md` — current physical design brief and open decisions.
3. `docs/adr/0011-provisional-v1-physical-direction-assumptions.md` — accepted provisional assumptions.
4. `CONTEXT.md` and `docs/project-state.md` — project-level handoff state.
5. Individual render images — reference only, never authoritative by themselves.
6. Crate IQ images or tech-pack pages — archival/reference only unless promoted into active docs.

## Required Next Deliverable

Create `physical-design/placement-sketch.md` as the visual/mechanical bridge from image language to engineering constraints.

It should include:

1. Canonical front view.
2. Canonical back view.
3. Left/right side views.
4. Bottom port view.
5. Internal stack block diagram.
6. Camera/OCR fit option.
7. Mic port placement option.
8. 3.5mm jack fit check.
9. Control durability candidates.
10. Explicit rejected visual directions.

## Rejected Directions

### Reject as canonical: amber keypad mini-gadget

Reason: too busy, too thick-looking, multiple controls, top cylinder is unexplained, and it reads closer to a novelty transparent mini synth than the current pocket field-recorder direction.

### Reject as canonical: Crate IQ horizontal slab with side-strip display

Reason: useful mechanical predecessor, but it keeps old naming, uses a less readable display layout, and conflicts with the current portrait/voice-recorder interpretation.

### Reject as canonical: generic orange turntable/shovel logo as device identity

Reason: too polished in the wrong direction and does not preserve the rough shovel-speaker-neon-wave idea described in the brand guide.

## Working Lock Recommendation

For the next round of product visuals, lock the visual prompt around this statement:

> yadiggg is a compact, portrait-first, 105mm x 60mm x 15mm-class pocket field recorder for vinyl crate digging, with a smoke-clear translucent polycarbonate shell, large monochrome Sharp Memory LCD on the upper front face, one durable amber/orange side thumb control, visible but restrained dark internal electronics, USB-C bottom port, optional 3.5mm jack if fit allows, tiny acoustic mic ports, and a provisional rear OCR/macro camera aperture. No keypad, no Crate IQ branding, no bulky walkie-talkie silhouette, no generic spade logo, and no production-ready claims until physical placement, BOM, and KiCad constraints are reconciled.

## Immediate Repo Follow-up

- Update `yadiggg_renderings_and_use_cases.md` to stop calling existing renderings official or 100% aligned.
- Add this audit to `docs/project-state.md` as the current visual-consistency handoff artifact.
- Generate or sketch a new `placement-sketch.md` using the canonical direction above.
- Keep old visual assets in reference/archive status until a new canonical render set replaces them.
