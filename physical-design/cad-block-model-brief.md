---
title: "CAD Block Model Brief"
project: yadiggg
status: active-draft
type: mechanical_cad_brief
tags: [yadiggg, cad, enclosure, mechanical, block-model, industrial-design]
backlinks:
  - "[[CONTEXT]]"
  - "[[docs/project-state]]"
  - "[[physical-design/physical-direction-brief]]"
  - "[[physical-design/placement-sketch]]"
  - "[[physical-design/render-consistency-protocol]]"
  - "[[docs/adr/0011-provisional-v1-physical-direction-assumptions]]"
---

# yadiggg CAD Block Model Brief

## Purpose

This brief converts the locked yadiggg visual direction into a finite first-pass CAD block model specification. It is intended for Onshape, Fusion 360, FreeCAD, OpenSCAD, or any equivalent mechanical CAD system.

This is **not production CAD**. It is a measured spatial proof model whose job is to answer:

> Can the canonical 105mm x 60mm x 15mm-class portrait-first field-recorder envelope plausibly contain the display, PCBA, battery, side control, USB-C, optional 3.5mm jack, mic ports, antenna keepout, and rear OCR/macro camera aperture?

## Source of Truth

Use these references in order:

1. `physical-design/render-consistency-protocol.md`
2. `physical-design/placement-sketch.md`
3. `physical-design/visual-consistency-audit.md`
4. `physical-design/physical-direction-brief.md`
5. `docs/adr/0011-provisional-v1-physical-direction-assumptions.md`

## Canonical Product Envelope

| Parameter | Value | Status | Evidence / rationale |
|---|---:|---|---|
| Height | 105mm | provisional canonical | observed in `Downloads/image_1790508905600.png`; recurring in tech-pack references |
| Width | 60mm | provisional canonical | observed in `Downloads/image_1790508905600.png`; recurring in tech-pack references |
| Thickness | 15mm | provisional canonical | observed in `Downloads/image_1790508905600.png`; selected as roomier prototype class |
| Corner radius | 6mm starting point | provisional modeling assumption | visually consistent with rounded pocket device; must be adjusted after grip/drop review |
| Shell wall | 1.5mm starting point | provisional modeling assumption | reasonable first-pass placeholder for translucent enclosure study; must be manufacturer-validated |
| Front/back shell split | 7.5mm / 7.5mm nominal | provisional modeling assumption | symmetric first-pass split; actual split may move for assembly |

## Coordinate System

Use this coordinate convention for every CAD file and exported reference:

```text
Origin: device center, mid-plane of device thickness
X axis: width, left negative / right positive, total 60mm
Y axis: height, bottom negative / top positive, total 105mm
Z axis: thickness, front positive / rear negative, total 15mm
```

Face naming:

- `front`: display side, +Z
- `back`: camera side, -Z
- `right`: amber/orange thumb-control side, +X
- `left`: opposite side, -X
- `bottom`: USB-C / optional 3.5mm edge, -Y
- `top`: mic / acoustic exposure edge, +Y

## First-Pass Exterior Geometry

### Body

| Feature | CAD instruction | Status |
|---|---|---:|
| Main body | Rounded rectangle prism, 60mm W x 105mm H x 15mm D | locked envelope, provisional dimensions |
| Corner radius | Start with 6mm external radius | provisional |
| Edge treatment | 1.0-1.5mm soft bevel/fillet around front/back perimeter | provisional |
| Material | Smoke-clear translucent polycarbonate visual material | visual lock, exact resin not final |
| Internal opacity | Shell translucent enough to reveal restrained dark internals, not a clear showcase toy | visual lock |

### Display Window / Front Interface

| Feature | CAD instruction | Status |
|---|---|---:|
| Display module | Upper front recessed rectangle | locked placement concept |
| Display visible area | Start with 48mm W x 38mm H | provisional sizing assumption; must match selected Sharp Memory LCD |
| Display center | X = 0mm, Y = +22mm, Z = front surface | provisional |
| Bezel/gasket | 2mm dark bezel around visible display | provisional |
| Lower front region | Transparent view into dark internal massing / PCBA shields | visual lock |
| Front buttons | None | locked exclusion |

### Right-Side Thumb Control

| Feature | CAD instruction | Status |
|---|---|---:|
| Control type | Recessed pill/slider placeholder | provisional; mechanism not locked |
| Control color | Amber/orange | visual lock |
| Control size | Start with 7mm W x 22mm H x 2mm proud/recessed detail | provisional |
| Control center | X = +30mm side face, Y = +12mm, Z = 0mm | provisional ergonomic starting point |
| Pocket-snag rule | No sharp protrusion; maintain rounded edges | design requirement |

### Back Camera / Mic / Antenna

| Feature | CAD instruction | Status |
|---|---|---:|
| Rear OCR/macro camera aperture | Circular aperture on rear shell | provisional |
| Camera aperture diameter | Start with 7mm visible circular opening | provisional |
| Camera center | X = 0mm, Y = +25mm, Z = rear surface | provisional |
| Mic ports | Two or three tiny top/back edge pinholes | provisional |
| Mic port diameter | Start with 0.8-1.0mm holes | provisional; requires acoustic design |
| RF keepout | Reserve top-right or corner region inside shell | provisional; requires RF validation |

### Bottom Ports

| Feature | CAD instruction | Status |
|---|---|---:|
| USB-C cutout | Centered or near-centered rounded slot on bottom edge | observed / provisional |
| USB-C opening | Start with 9.5mm W x 3.5mm H cutout | provisional connector-clearance placeholder |
| 3.5mm jack opening | Optional circular cutout on bottom edge | optional |
| 3.5mm opening | Start with 6.5mm circular clearance | provisional; depends on jack selection |
| Port reinforcement | Add local boss/thickened area around openings | required for later CAD |

## Internal Block Model

The internal geometry should be represented as simple bounding boxes first. The goal is collision/space proof, not detailed electronics.

| Subsystem | First-pass bounding volume | Placement assumption | Status |
|---|---:|---|---:|
| Display module | 52mm W x 42mm H x 2.5mm D | upper front | provisional |
| Main PCBA | 52mm W x 86mm H x 1.6mm D | behind display/lower body | provisional |
| Shield/thermal zones | 36mm W x 28mm H x 2mm D blocks | over SoC/audio/power regions | provisional |
| Battery | 38mm W x 48mm H x 5mm D | lower/rear volume | provisional |
| Camera module | 10mm W x 10mm H x 4mm D | behind rear aperture | provisional |
| Mic assembly | 8mm W x 4mm H x 2mm D | top/back acoustic path | provisional |
| Side control module | 5mm W x 24mm H x 5mm D | right side cavity | provisional |
| USB-C connector | 9mm W x 7mm H x 4mm D | bottom board edge | provisional |
| 3.5mm jack | 6.5mm diameter x 12mm barrel | bottom board edge | optional / likely high-risk |

## Required CAD Deliverables

A first CAD pass is complete only when it includes:

1. Outer rounded body envelope.
2. Front shell and rear shell split.
3. Large upper-front display placeholder.
4. Lower internal visual-massing area.
5. Right-side amber thumb-control placeholder.
6. Rear OCR/macro camera aperture placeholder.
7. Top/back mic-port placeholders.
8. Bottom USB-C cutout.
9. Optional bottom 3.5mm cutout as removable/suppressed feature.
10. Internal PCBA, battery, display, camera, and side-control bounding boxes.
11. Named construction planes / coordinate axes.
12. Exportable STEP or STL block model.
13. Screenshot/render set: front, back, side, bottom, exploded.

## CAD Layer / Object Naming

Use these exact object names where the CAD tool supports naming:

```text
body_shell_front
body_shell_rear
display_window
lcd_module_block
pcba_main_block
battery_block
shield_zone_blocks
side_control_amber
usb_c_cutout
jack_3p5_optional_cutout
rear_camera_aperture
mic_port_holes
rf_keepout_zone
logo_deferred_zone
```

## Modeling Procedure

### Phase 1: Envelope

1. Create a 60mm x 105mm sketch on the front plane.
2. Add 6mm corner radii.
3. Extrude symmetrically to 15mm total thickness.
4. Apply 1.0-1.5mm edge fillets.
5. Assign smoke-clear translucent material.

### Phase 2: Front Features

1. Add display recess/window on upper front.
2. Add dark display bezel.
3. Add monochrome display plane.
4. Add simplified waveform UI texture only if using visual render mode.
5. Add lower dark internal-massing blocks visible through shell.
6. Do not add keypad/buttons to front.

### Phase 3: Side Control

1. Add right-side recessed vertical/pill control cavity.
2. Add amber/orange control insert.
3. Keep edges rounded and pocket-safe.
4. Leave switch mechanism abstract until control durability matrix is complete.

### Phase 4: Back Features

1. Add rear camera aperture placeholder.
2. Add camera-module bounding block behind aperture.
3. Add tiny mic port holes near top/back edge.
4. Add RF keepout zone as non-rendered construction volume or translucent annotation.

### Phase 5: Bottom Ports

1. Add USB-C bottom cutout.
2. Add connector bounding block behind cutout.
3. Add optional 3.5mm jack cutout as a suppressible feature.
4. Add jack barrel bounding block and mark it high-risk.

### Phase 6: Internal Blocks

1. Add LCD module block.
2. Add main PCBA block.
3. Add shield/thermal placeholder blocks.
4. Add battery block.
5. Add side-control module block.
6. Check gross collisions.
7. Record every collision or impossible stack assumption.

## Validation Checklist

Before using CAD renders as product truth, answer:

| Check | Pass condition |
|---|---|
| Envelope | Overall body remains 105mm x 60mm x 15mm-class |
| Display | Display fits without consuming side-control or port space |
| PCBA | Main PCBA can plausibly route to display, USB-C, side control, mics, camera, and optional jack |
| Battery | Battery block fits without crushing camera, ports, or antenna zone |
| USB-C | Connector cutout is physically reachable and structurally reinforced |
| 3.5mm jack | Jack barrel fits without weakening shell or violating analog/layout constraints |
| Camera | Rear camera has aperture, light path, module depth, and board connection path |
| Mics | Mic ports are not blocked by hand, shell ribs, display, or haptic/control impulse path |
| Antenna | RF keepout exists away from battery/shields/ground pours |
| Side control | Control is reachable one-handed and not pocket-snaggy |
| Front | No keypad or extra buttons appear |
| Branding | No Crate IQ or generic spade logo appears |
| Claims | No production-ready/fabrication-ready claim is present |

## Known High-Risk Areas

1. **3.5mm jack fit** — likely one of the hardest features in a 15mm-class shell.
2. **Rear OCR/macro camera** — may force stack height, light-seal complexity, MIPI routing, and shell opacity tradeoffs.
3. **Mic placement** — must work during crate browsing, turntable capture, and hand-held use without occlusion.
4. **Side control** — visual lock says one amber/orange side control, but mechanism is still undecided.
5. **Battery volume** — no selected battery pack is locked; block dimensions are only placeholders.
6. **Translucent shell** — internal electronics must look intentional, not messy.

## Recommended CAD Tool Path

### Browser-first path

Use **Onshape** if local CAD setup is a problem:

1. Create a Part Studio named `yadiggg_v1_block_model`.
2. Model the envelope and features using the dimensions above.
3. Use separate parts for shell, display, PCBA, battery, and control blocks.
4. Export STEP for repo archival.
5. Export screenshots for `physical-design/cad-renders/`.

### Desktop fallback

Use **Fusion 360** if it works locally and you want better product renders/materials.

### Script-first fallback

Use the accompanying OpenSCAD starter model as a quick geometry proof if no full CAD tool is available.

## Output Folder Recommendation

```text
physical-design/cad/
physical-design/cad/exports/
physical-design/cad/renders/
```

Keep exported CAD artifacts out of `hardware/` until they are engineering-validated.

## Immediate Next Action

Create a simple block model first. Do not model fine details, ribs, snaps, screws, gasket grooves, or exact PCB footprints until these high-risk questions are answered:

1. Is the 3.5mm jack still in V1?
2. Is rear OCR/macro camera still in V1?
3. Which side-control mechanism wins?
4. Which display module is actually selected?
5. What battery cell dimensions are realistic?
