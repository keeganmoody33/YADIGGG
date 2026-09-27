---
title: "V1 Placement Sketch"
project: yadiggg
status: active-draft
type: physical_placement_sketch
tags: [yadiggg, physical-design, placement, mechanical-constraints, visual-lock]
backlinks:
  - "[[CONTEXT]]"
  - "[[docs/project-state]]"
  - "[[physical-design/physical-direction-brief]]"
  - "[[physical-design/visual-consistency-audit]]"
  - "[[docs/adr/0011-provisional-v1-physical-direction-assumptions]]"
---

# yadiggg V1 Placement Sketch

## Purpose

This document turns the locked visual direction into concrete placement constraints. It is not final CAD, not a production tech pack, and not a fabrication release. It is the working mechanical/visual interface that future industrial design, electrical layout, KiCad keepouts, and rendering work should use.

## Canonical Visual Lock

> yadiggg is a compact, portrait-first, 105mm x 60mm x 15mm-class pocket field recorder for vinyl crate digging, with a smoke-clear translucent polycarbonate shell, large monochrome Sharp Memory LCD on the upper front face, one durable amber/orange side thumb control, visible but restrained dark internal electronics, USB-C bottom port, optional 3.5mm jack if fit allows, tiny acoustic mic ports, and a provisional rear OCR/macro camera aperture. No keypad, no Crate IQ branding, no bulky walkie-talkie silhouette, no generic spade logo, and no production-ready claims.

## Evidence Basis

Every specific claim below is tied to an observed repo artifact or marked as provisional.

| Evidence source | What is directly observed | How this document uses it |
|---|---|---|
| `Downloads/image_1790508905600.png` | Portrait-first grey translucent device, 105mm height, 60mm width, 15mm side depth, large front display, orange side control, rear OCR/macro camera label, tiny acoustic microphone label, corner RF antenna label, USB-C and 3.5mm bottom ports | Primary visual reference for canonical exterior placement |
| `A635cb2ae39c0459eb58a46ec8bbd6ffbH.avif` | 105mm x 60mm x 15mm labeled technical drawing, orange mechanical scan button, dual Knowles MEMS microphone pinholes, USB-C and 3.5mm bottom edge, smoke amber translucent polycarbonate material note | Confirms the recurring 105 x 60 x 15 class and core component set, but horizontal layout is not adopted |
| `A785a6969d2a046a2a18825402ad289f9f.avif` | Exploded assembly with top shell, 2.7-inch Sharp Memory LCD, main PCBA, orange silicone button, CNC aluminum internal frame, 1500mAh Li-Poly battery, Knowles MEMS microphones, bottom shell, USB-C and 3.5mm jack closeups | Informs provisional internal stack only; geometry and color must be reconciled |
| `Aff28a8c6b74a43d18f19da841c804948X.avif` | Manufacturing/process illustration using amber Crate IQ slab and PCBA assembly | Reference only; not canonical external appearance |
| `A2c312300cbc241a593033cc604f7deb5N.png` and duplicate | Upright amber transparent device with many keypad buttons, large top knurled cylinder, visible internals, Sharp Memory LCD | Explicitly rejected as canonical because keypad/cylinder conflict with locked direction |
| `Adedd09730c9846ad95f9d82a4302401e8.png` | Horizontal smoky Crate IQ slab with side display, rear camera, orange top control | Historical visual predecessor; not canonical due old branding and orientation conflict |
| `IMG_3581_converted.png` / `yadigggsketch_rendered.png` | Rough shovel/speaker/record logo sketch with red speaker form and green wave/energy marks | Logo concept reference only; on-device logo remains deferred |

## Non-Negotiable Visual Constraints

| Constraint | Requirement | Evidence / rationale |
|---|---|---|
| Product name | Current visuals must use `yadiggg` or no visible name | Current project identity and brand docs use yadiggg; Crate IQ assets are archival/reference |
| Orientation | Portrait-first exterior logic | Observed in `Downloads/image_1790508905600.png`; aligns with field-recorder direction |
| Envelope | 105mm x 60mm x 15mm-class | Directly labeled in `Downloads/image_1790508905600.png`; also appears in `A635...avif` tech drawing |
| Shell | Smoke-clear translucent polycarbonate baseline | Observed in canonical image and supported by visual lock; amber shell becomes limited/reference direction |
| Display | Large monochrome Sharp Memory LCD on upper front face | Observed in canonical image; 2.7-inch Sharp Memory LCD appears in tech-pack sources |
| Control | One durable amber/orange side thumb control | Observed in canonical image side view; aligns with one-handed use constraint |
| Keypad | No keypad | Rejects `A2c...png` direction |
| Branding | No Crate IQ branding | Rejects older Crate IQ visual assets as canonical |
| Logo | No generic spade logo; on-device logo deferred/subtle | Brand docs and logo sketch indicate unresolved shovel-speaker mark |
| Production status | No production-ready claims | ADRs state physical design, KiCad, BOM, and validation are not locked |

## Canonical Exterior Placement

### Front View

```text
┌──────────────────────────────┐  105mm class height
│  Rounded smoke-clear shell   │
│  ┌────────────────────────┐  │
│  │                        │  │
│  │  Sharp Memory LCD      │  │  Upper-front dominant display
│  │  monochrome, low power │  │
│  │                        │  │
│  └────────────────────────┘  │
│                              │
│  restrained visible internals│
│  under translucent shell     │
│                              │
│        subtle/optional       │
│        yadiggg mark area     │
└──────────────────────────────┘
          60mm class width
```

#### Front placement constraints

| Area | Placement rule | Status |
|---|---|---:|
| Display | Upper front face, large enough to be the dominant visible interface | canonical visual constraint |
| Visible internals | Lower/front internal electronics may be visible but must be visually restrained | canonical visual constraint |
| Logo | Optional and subtle; do not force large front logo | provisional / deferred |
| Front controls | Avoid keypad or dense button grid | canonical visual constraint |
| Camera | Do not place main OCR camera on front unless a later optical study overrides rear-camera approach | provisional |

## Right Side / Thumb Side

```text
Side profile, 15mm class depth

┌──────────────┐
│              │
│   █ orange   │  durable thumb control
│   █ control  │
│              │
└──────────────┘
```

### Side placement constraints

| Element | Placement rule | Evidence / status |
|---|---|---:|
| Primary control | One amber/orange side thumb control, reachable during one-handed crate browsing | observed in canonical image; canonical visual constraint |
| Control type | Button/slider/rocker not mechanically locked yet | requires durability matrix |
| Protrusion | Must not snag in pocket; should be recessed or low-profile | design requirement, not yet validated |
| Haptic actuator | Should couple to frame, but must be isolated from mic ports | provisional engineering constraint |

## Back View

```text
┌──────────────────────────────┐
│   tiny acoustic mic ports    │
│                         RF   │
│                              │
│             ○                │  provisional OCR/macro camera
│                              │
│                              │
│      mostly clean shell      │
└──────────────────────────────┘
```

### Back placement constraints

| Element | Placement rule | Evidence / status |
|---|---|---:|
| OCR/macro camera | Single rear aperture centered or upper-middle; must be optically justified | observed in canonical image; provisional until camera feasibility gate |
| Mic ports | Tiny acoustic ports near top/edge unless acoustic study changes location | observed in canonical image; provisional geometry |
| RF antenna | Corner antenna zone must be reserved in technical constraints | observed in canonical image label; requires RF/layout validation |
| Back branding | Avoid large branding; keep surface clean | consistent with visual lock and deferred logo rule |

## Bottom Edge

```text
Bottom edge

┌──────────────────────────────┐
│        USB-C      3.5mm?     │
└──────────────────────────────┘
```

### Bottom-edge constraints

| Element | Placement rule | Evidence / status |
|---|---|---:|
| USB-C | Bottom edge candidate, preferably centered or stack-driven | observed in canonical image and tech drawing |
| 3.5mm jack | Bottom edge candidate only if fit, shell strength, and analog routing pass | observed in images; explicitly optional in visual lock |
| Extra ports | Do not add unexplained ports | visual consistency rule |

## Internal Stack Block Diagram

The internal stack is still provisional, but must fit inside the 15mm-class envelope.

```text
Front side
│
├─ Smoke-clear front shell / display window
├─ Sharp Memory LCD + display gasket/support
├─ Main PCBA with SoC, memory, PMIC, audio DAC, RF module
├─ Shield cans / thermal spreader zones
├─ Battery pack, likely rear or offset from main PCBA
├─ Camera module and light seal if OCR remains in scope
├─ Mic acoustic channel + mesh + MEMS mic isolation detail
└─ Smoke-clear rear shell
│
Back side
```

### Internal stack constraints

| Subsystem | Placement rule | Evidence / status |
|---|---|---:|
| Display | Front-side assembly with window/gasket; not just PCB-mounted visual element | inferred from display requirement; needs mechanical design |
| PCBA | Must fit within shell, ports, display, battery, antenna, camera, and mic constraints | provisional |
| Battery | Largest volume driver; likely rear/offset placement | observed 1500mAh battery in exploded view; capacity not locked |
| Camera | Rear aperture plus internal light seal if retained | observed in canonical and tech-pack images; provisional |
| Mics | Isolated from switch/haptic impulse path | physical brief requirement; geometry not locked |
| Antenna | Corner/edge keepout away from shields and battery mass | observed label; RF validation required |
| 3.5mm jack | Board-edge mechanical and analog-routing constraint | observed; fit check required |

## Placement Keepout Checklist for KiCad / Mechanical CAD

Before the KiCad board outline is updated or components are placed, define keepouts for:

1. Display active area, bezel, gasket, and FPC escape.
2. Side amber control travel/cavity and switch landing zone.
3. USB-C shell opening and connector reinforcement.
4. Optional 3.5mm jack barrel, insertion force, and analog zone.
5. Rear OCR/macro camera aperture, lens barrel, and light seal.
6. Mic acoustic ports, dust mesh, acoustic channel, and mic isolation region.
7. RF antenna corner and copper keepout.
8. Battery footprint, swell allowance, adhesive/pull-tab/service clearance.
9. Screw bosses, snap joints, sonic-weld ribs, or fastener strategy.
10. Internal frame/shield-can height and heat spread zones.

## Rejected Visual Directions

### Rejected: keypad mini-gadget

Observed in `A2c312300cbc241a593033cc604f7deb5N.png` and duplicate. It shows many front keys and a large top knurled cylinder. This conflicts with the locked one-control pocket field-recorder direction.

### Rejected: Crate IQ horizontal side-display slab

Observed in `Adedd09730c9846ad95f9d82a4302401e8.png`, `A635cb2ae39c0459eb58a46ec8bbd6ffbH.avif`, and related tech-pack pages. It is useful precedent but not canonical because it uses old branding and a horizontal side-display layout.

### Rejected: generic spade/turntable logo as device identity

Observed in `Ab0366a7e4d1c4f86ba5eb0a115a0dd80k.png`. It does not preserve the unresolved shovel-speaker-neon-wave concept strongly enough to drive product-body design.

## Decisions Still Required

| Decision | Why it blocks mechanical constraints | Current action |
|---|---|---|
| OCR/camera feasibility | Camera drives rear aperture, MIPI routing, shell opacity/light sealing, and stack height | Create camera opportunity-cost matrix |
| Control mechanism | Button vs slider vs rocker changes side cutout, sealing, haptics, durability, and BOM | Create control durability matrix |
| 3.5mm jack fit | Jack affects thickness, board edge, analog routing, shell strength, and pocket durability | Create jack fit check |
| Mic port placement | Mic performance depends on port exposure, isolation, and hand occlusion | Create mic placement options |
| Battery volume | Battery drives thickness, weight, heat, and rear-shell geometry | Define candidate pack sizes |
| Logo placement | Surface strategy affects CMF, tooling, print/etch process, and brand consistency | Defer until logo vector and shell surface strategy are resolved |

## Next Engineering Output

The next artifact should be a measured block model, not a freeform render. It should test whether the canonical 105mm x 60mm x 15mm-class envelope can contain:

- display,
- PCBA,
- battery,
- USB-C,
- optional 3.5mm jack,
- side control,
- mic ports,
- antenna keepout,
- and rear OCR/macro camera.

If the answer is no, the fallback should change the constraints explicitly rather than generating another inconsistent visual.
