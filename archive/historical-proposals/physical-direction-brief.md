---
title: "Physical Direction Brief"
project: yadiggg
status: active-draft
type: industrial_design_brief
tags: [yadiggg, physical-design, industrial-design, mechanical, kicad]
---

> **Historical proposal — unverified.** Preserved as design-session reference, not current requirements, measured geometry, selected components, fit evidence, or manufacturing instructions. The current status is in [the readiness register](../../docs/project-state.md); current product intent is in [the product specification](../../physical-design/final-product-source-of-truth.md).

# yadiggg Physical Direction Brief

This working brief records design questions, not an approved specification. Use the [canonical product specification](final-product-source-of-truth.md) for current intent and the [readiness register](../docs/project-state.md) for open engineering work. Specific components and dimensions mentioned below are unverified proposals or references.

## Purpose

This file is the active working brief for exploring the physical direction of the yadiggg pocket companion.

It exists because [0002-physical-design-direction-not-yet-locked](../docs/adr/0002-physical-design-direction-not-yet-locked.md) states that current renderings are only visual references. They do **not** yet define a manufacturable enclosure, internal stack, control placement, or PCB/mechanical constraints.

## Current Lock Status

| Area | Status | Meaning |
|---|---:|---|
| Brand tone | `directional` | The project wants premium, tactile, crate-digging hardware with translucent casing language. |
| Enclosure dimensions | `unlocked` | Prior docs mention 100 x 55 board, 105 x 60 x 15 enclosure, and 12mm slim variant. Needs reconciliation. |
| Control placement | `unlocked` | Orange slide-button/haptic interaction exists conceptually, not mechanically placed. |
| Display placement | `unlocked` | A monochrome display appears in concept art; display technology/part and face geometry are not selected. |
| Camera/OCR placement | `unlocked` | Camera exists in older architecture docs, but not in the recent KiCad scaffold or component selection map. |
| Microphone placement | `unlocked` | PDM mic array concept exists, but acoustic ports and vibration isolation geometry are not locked. |
| 3.5mm jack placement | `unlocked` | DAC output path exists; physical jack side/orientation/strain relief are not locked. |
| Antenna placement | `unlocked` | RF keepout exists conceptually; enclosure/material interaction not locked. |
| Internal stack | `unlocked` | PCBA/battery/shields/lens/grommets/fasteners are not placed as a package. |
| KiCad board outline | `scaffold` | Current board outline is provisional; do not route around it as final. |

## Design North Star

The physical device should feel like a **dedicated pocket instrument**, not a phone accessory:

- Offline-first and distraction-free.
- One-handable in a record store aisle.
- Tactile enough for dusty, low-light crate-digging.
- Premium enough to sit beside serious audio gear.
- Honest about internal hardware, but not visually noisy.

## Candidate Physical Envelope

These are not locked dimensions. They are working constraints that must be resolved before mechanical CAD and final PCB layout.

| Variant | Approx. outer envelope | Use case | Tradeoff |
|---|---:|---|---|
| Standard / Heavy Digger | ~105mm x 60mm x 15mm | Best battery, grip, easier internal stack | Less pocket-slim. |
| Slim / Pocket Special | ~105mm x 60mm x 12mm | Better pocketability | Smaller battery, tighter optics/PCB, likely HDI. |
| Current PCB scaffold | 100mm x 55mm | Existing KiCad outline placeholder | Must be adjusted once enclosure wall, bosses, ports, and keepouts are known. |

### Provisional Recommendation

Use the **15mm Standard / Heavy Digger** as the first physical prototype direction unless a stricter pocket target is chosen. This keeps enough volume for:

- Li-polymer battery,
- display window and support frame,
- camera/lens barrel if OCR remains in scope,
- isolated mic ports,
- haptic actuator,
- 3.5mm jack depth,
- RF clearance,
- shielding cans,
- realistic assembly tolerances.

## Exterior Layout Direction

### Front Face

Provisional front-face hierarchy:

1. **Monochrome display concept** in the upper/front dominant area; exact technology and part remain unresolved.
2. **Primary logo mark** below or beside the display, depending on enclosure orientation.
3. **Minimal visible hardware**, with translucent shell revealing selected shield/PCB features intentionally.

Open decisions:

- Portrait vs landscape primary orientation.
- Whether the LCD is centered or biased toward thumb controls.
- Whether the logo appears on shell exterior, interior print, or beneath translucent plastic.

### Right / Thumb Side

Provisional right-side controls:

- Main **orange slide-button** or scan trigger.
- Haptic feedback mechanically isolated from microphones.

Open decisions:

- Is the scan trigger a slider, momentary switch, rocker, or wheel?
- Is there a second navigation input, or is the device intentionally single-control?
- Which side is correct for right-handed and left-handed use?

### Bottom Edge

Provisional bottom-edge ports:

- USB-C for charging/update/drag-and-drop firmware packages.
- 3.5mm aux/headphone jack if depth allows clean routing.

Open decisions:

- Whether headphone jack sits bottom edge or side edge.
- Whether USB-C and jack can coexist without weakening shell or crowding PCB.
- Strain-relief and port reinforcement strategy.

### Top Edge

Provisional top-edge functions:

- Optional microphone acoustic ports if they need line-of-sight exposure.
- Antenna keepout may prefer an edge/corner zone away from hand shadowing.

Open decisions:

- Mic port location: top edge, front face, or split left/right.
- RF antenna corner and hand-blocking risk.

### Back Face

If the Basement Scanner / OCR camera remains in scope, the back face likely needs:

- Pinhole/macro camera aperture.
- Light-tight black internal barrel.
- Possibly a small alignment cue around the aperture.

Open decisions:

- Is camera/OCR still core for V1, or is V1 Sonic ID/audio-first?
- If camera remains, is the device used by pointing the back face at labels/spines?
- Minimum focus distance and hand posture.

## Internal Stack Direction

Provisional internal stack from front to back:

```text
[Front translucent shell / lens or display window]
[Display support / gasket / light-control layer]
[Main PCBA with SoC, memory, PMIC, audio, RF]
[Shield cans over high-speed digital zones]
[Battery pack on rear or opposite side of PCBA]
[Rear shell with camera aperture and/or service markings]
```

If camera remains in scope:

```text
[Rear shell aperture]
[Black rubber light seal]
[Black-anodized camera/lens barrel]
[Camera FPC module]
[Main PCBA MIPI connector]
```

If PDM mic array remains in scope:

```text
[External acoustic port]
[Water/dust mesh if required]
[Short acoustic channel]
[MEMS mic on isolated PCB finger-tab]
[Silicone grommet / damping interface]
[Main PCBA ground reference]
```

## Component Placement Requirements

### Display

- Place display where one-handed viewing is possible while thumb reaches the scan/control input.
- Keep display flex/connector accessible without crossing RF antenna keepouts.
- Add mechanical bezel/gasket strategy; do not rely on raw PCB placement alone.

### Camera / OCR

Status: unresolved for V1.

If retained:

- Camera must have a back-face aperture with optical alignment marks.
- Must be shielded from internal light leakage from translucent shell and display.
- Lens barrel must be mechanically referenced to shell, not only PCBA.
- MIPI path must be short and shielded.

If deferred:

- Remove camera-dependent physical claims from current specs or mark them as future variant.
- Simplify physical direction around Sonic ID + database lookup + audio preview.

### PDM Microphones

- Place microphones away from haptic actuator and main mechanical switch impulse path.
- Use separated acoustic ports if stereo capture/beam comparison matters.
- Maintain short PDM routes, but physical acoustic isolation takes priority over shortest trace.
- Finger-tab isolation is a concept, not locked geometry.

### 3.5mm Audio Jack

- Must sit near DAC analog zone to keep analog traces short.
- Needs shell wall support and insertion-force strain relief.
- Should avoid RF antenna corner and PMIC switching region.
- Board edge cutout and jack height must drive enclosure thickness.

### Antenna

- Needs edge/corner placement with all-layer copper keepout.
- Avoid hand-covered zones if possible.
- Translucent polycarbonate is RF-friendlier than metal, but shield cans and battery placement can detune antenna.
- Antenna placement must be co-designed with enclosure and hand posture.

### Haptic Actuator

- Place close enough to the body frame for tactile energy transfer.
- Keep away from PDM mic ports and camera module.
- Mechanically isolate from mic finger-tabs.

### Battery

- The battery is likely the largest internal volume driver.
- Decide whether battery sits behind the PCBA or beside it.
- Battery placement affects heat, hand feel, antenna, and case stiffness.

## CMF Direction

CMF = Color, Material, Finish.

### Current Directional Language

- Translucent smoke-grey or amber polycarbonate casing.
- High-contrast orange tactile control.
- Black/dark internal shield cans and PCBA elements visible through shell.
- Premium, minimal, rugged crate-digging object.

### Conflicts to Resolve

- Some docs/images reference smoke-grey translucent casing.
- Some docs reference amber/orange translucent casing.
- Some renderings introduce violet/magenta logo language that may conflict with orange/black hardware language.
- Physical brand application should be reconciled with actual shell color and internal part visibility.

### Provisional CMF Recommendation

For first physical prototype:

| Surface | Direction | Reason |
|---|---|---|
| Outer shell | Smoke-grey translucent polycarbonate | Shows internal hardware without over-warming every visual. |
| Primary control | Amber/orange tactile slider/button | Strong interaction affordance and brand accent. |
| Internal shield cans | Matte or black-anodized metal | Functional EMI shielding with intentional visible structure. |
| PCBA | Matte black solder mask | Better through-shell visual coherence. |
| Logo | Inside-surface print or etched insert | Protects mark from wear. |

## KiCad and Mechanical Constraints

Do not treat the current KiCad board outline as final. Before real routing:

1. Lock enclosure outer envelope.
2. Lock wall thickness and internal boss/screw strategy.
3. Lock port locations and board-edge constraints.
4. Lock display cutout and FPC routing.
5. Decide camera/OCR inclusion for V1.
6. Lock battery dimensions.
7. Lock antenna corner/keepout.
8. Lock microphone port/finger-tab geometry.
9. Update board outline and component keepout zones in KiCad.
10. Only then begin placement/routing.

## Canonical V1 Visual Lock

Use this as the controlling visual statement for new renders, placement sketches, and tech-pack updates:

> yadiggg is a compact, portrait-first, 105mm x 60mm x 15mm-class pocket field recorder for vinyl crate digging, with a smoke-clear translucent polycarbonate shell, large monochrome Sharp Memory LCD on the upper front face, one durable amber/orange side thumb control, visible but restrained dark internal electronics, USB-C bottom port, optional 3.5mm jack if fit allows, tiny acoustic mic ports, and a provisional rear OCR/macro camera aperture. No keypad, no Crate IQ branding, no bulky walkie-talkie silhouette, no generic spade logo, and no production-ready claims.

This statement supersedes inconsistent prior renderings as visual direction, but it does **not** make the industrial design production-ready. Dimensions, port placement, control mechanism, camera feasibility, mic placement, battery, antenna, jack fit, and KiCad constraints still require engineering validation.

## Provisional V1 Physical Assumptions

These assumptions come from the latest user review, [visual-consistency-audit](visual-consistency-audit.md), and [0011-provisional-v1-physical-direction-assumptions](../docs/adr/0011-provisional-v1-physical-direction-assumptions.md). They are **provisional working assumptions**, not final industrial-design lock.

| Decision | Current direction | Tradeoff / fallback |
|---|---|---|
| V1 scope | Attempt **OCR/camera + Sonic ID + database credits + audio preview** in V1. | Keep camera/OCR until real bottlenecks appear. If size, optics, routing, power, cost, or reliability become too expensive, remove camera/OCR and focus V1 on Sonic ID + database/credits + audio preview. |
| Thickness | First prototype should target the **roomier 15mm-class enclosure**, not the 12mm slim target. | This refers to enclosure/device thickness, not 4-layer PCB copper stackup thickness. 12mm can remain a later slim variant after the internal stack is proven. |
| Color direction | Core product should support **clear/smoke-clear translucent** direction, with room for a louder limited-edition colorway. | Avoid making a loud color the only product direction. CMF should support both standard and special-edition shells. |
| Form factor | Move toward a **modern voice-recorder-like object**, roughly 3–4 inches long, pocketable, one-handable, and durable. | Not a phone slab, not a pager-first object. Actual width/thickness must be driven by display, battery, jack, controls, camera, antenna, and hand feel. |
| Usage scenarios | Support **all major identification scenarios**: holding a record, standing near a turntable, browsing crates one-handed, scanning barcode/catalog/visual clues, Sonic ID acoustic matching, and database/credits lookup. | The input/UX must not assume one posture only. Physical controls should work when the user has one hand occupied. |
| Primary control | Pick the **most durable, manufacturable, one-handed input** after a control durability trade study. | Do not lock slider/button/rocker/wheel yet. The winning control should survive drops, dust, pocket carry, repeated presses, and one-handed use. |
| 3.5mm jack | Keep the jack in V1 **if space allows**. | Desired feature, but must pass fit/strength/analog-routing check. If it compromises the internal stack too much, revisit. |
| Physical logo | Product logo placement is deferred. Packaging/accessories will carry branding; on-device logo waits until the physical logo and shell surface strategy are refined. | Do not force logo placement into the enclosure before CMF and form are settled. |

## Physical Design Decisions Required Next

| Decision | Options | Current recommendation |
|---|---|---|
| OCR/camera feasibility gate | retain / miniaturize / remove | Retain for V1 exploration; cut only if the opportunity cost is proven too high. |
| Camera implementation | tiny camera module / scan-line style module / deferred | Explore the smallest feasible optical scanner/camera approach; document tradeoffs before committing. |
| Control mechanism | recessed tactile button / sealed slider / rocker / wheel / combo input | Run durability/manufacturing comparison; choose the least fragile one-handed option. |
| Device envelope | ~3–4 inch voice-recorder form / wider scanner form | Start with voice-recorder-like hand model and test against components. |
| Enclosure thickness | 15mm prototype / 12mm slim later | Start 15mm class for prototype, keep 12mm as later variant. |
| CMF | clear / smoke-clear / limited color | Standard: clear or smoke-clear translucent; limited edition can be more expressive. |
| Headphone jack | keep / remove / optional variant | Keep if fit check passes. |
| Logo placement | packaging/accessories only / subtle on-device mark / internal mark | Defer on-device mark until logo and shell strategy mature. |

## Open Questions for the Next Review

1. What is the smallest realistic OCR/camera module approach: true camera, scan-line sensor, barcode-style scanner, or another optical reader?
2. What exact voice-recorder-like envelope should we test first: length, width, thickness, and grip radius?
3. Which control architecture wins the durability study: sealed button, recessed button, slider, rocker, wheel, or combo?
4. Where does the 3.5mm jack physically fit without weakening the shell or forcing bad analog routing?
5. Where do microphone ports belong if the device must work in all use scenarios, not just one posture?
6. What shell material/finish gives the best clear/smoke-clear look while hiding scuffs and internal clutter?
7. What must the next placement sketch prove before KiCad board-outline changes begin?

## Next Deliverable

Create a `physical-design/placement-sketch.md` or equivalent with:

- front view block layout,
- back view block layout,
- side edge port/control layout,
- internal stack cross-section,
- keepout map for KiCad.

This brief must be updated before any claim that the physical direction is locked.
