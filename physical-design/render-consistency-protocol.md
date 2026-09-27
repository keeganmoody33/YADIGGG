---
title: "Render Consistency Protocol"
project: yadiggg
status: active-draft
type: render_protocol
tags: [yadiggg, rendering, visual-consistency, physical-design, prompt-control]
backlinks:
  - "[[CONTEXT]]"
  - "[[docs/project-state]]"
  - "[[physical-design/physical-direction-brief]]"
  - "[[physical-design/visual-consistency-audit]]"
  - "[[physical-design/placement-sketch]]"
  - "[[docs/adr/0011-provisional-v1-physical-direction-assumptions]]"
---

# yadiggg Render Consistency Protocol

## Purpose

This protocol prevents future yadiggg product renders from drifting into inconsistent devices. It defines the exact visual lock, reusable prompt structure, acceptance checks, and rejection rules for all future image generation, image editing, Higgsfield image/video work, technical render sheets, lifestyle scenes, and product visualization passes.

No new render should be treated as useful unless it passes this protocol.

## Canonical Visual Lock

Use this exact statement as the root visual constraint for all new render work:

> yadiggg is a compact, portrait-first, 105mm x 60mm x 15mm-class pocket field recorder for vinyl crate digging, with a smoke-clear translucent polycarbonate shell, large monochrome Sharp Memory LCD on the upper front face, one durable amber/orange side thumb control, visible but restrained dark internal electronics, USB-C bottom port, optional 3.5mm jack if fit allows, tiny acoustic mic ports, and a provisional rear OCR/macro camera aperture. No keypad, no Crate IQ branding, no bulky walkie-talkie silhouette, no generic spade logo, and no production-ready claims.

## Evidence Traceability Rule

Every factual visual instruction must trace to one of:

1. the canonical visual lock above,
2. `physical-design/placement-sketch.md`,
3. `physical-design/visual-consistency-audit.md`,
4. `physical-design/physical-direction-brief.md`,
5. `docs/adr/0011-provisional-v1-physical-direction-assumptions.md`, or
6. an observed image artifact explicitly named in the prompt or review notes.

If a visual detail cannot be traced, mark it as:

- `provisional`,
- `exploration-only`, or
- omit it from the render request.

Do not invent dimensions, ports, materials, labels, internal modules, certifications, production status, or final manufacturing details.

## Consistency Hierarchy

When references conflict, use this order:

1. `physical-design/render-consistency-protocol.md`
2. `physical-design/placement-sketch.md`
3. `physical-design/visual-consistency-audit.md`
4. `physical-design/physical-direction-brief.md`
5. `docs/adr/0011-provisional-v1-physical-direction-assumptions.md`
6. `CONTEXT.md` and `docs/project-state.md`
7. individual images as evidence only
8. Crate IQ-era visuals as archive/reference only

## Locked Product Invariants

These must remain consistent across every render:

| Area | Locked invariant |
|---|---|
| Product identity | `yadiggg`, not Crate IQ |
| Archetype | compact pocket field recorder for vinyl crate digging |
| Orientation | portrait-first front face |
| Envelope | 105mm x 60mm x 15mm-class; still provisional, not production-final |
| Shell | smoke-clear translucent polycarbonate baseline |
| Display | large monochrome Sharp Memory LCD on upper front face |
| Control | one durable amber/orange side thumb control |
| Internals | restrained dark internal electronics visible through shell |
| Ports | USB-C bottom port; 3.5mm jack optional if fit allows |
| Acoustic input | tiny acoustic mic ports |
| Optical input | provisional rear OCR/macro camera aperture |
| Branding | no Crate IQ; no generic spade logo; on-device logo subtle or deferred |
| Claim status | no production-ready, fabrication-ready, or final-CAD claims |

## Forbidden Drift

Reject any render that includes:

1. keypad or multi-button front grid,
2. exposed top knurled cylinder,
3. Crate IQ branding,
4. horizontal slab as the primary product orientation,
5. side-strip display as the main interface,
6. bulky walkie-talkie proportions,
7. phone-like black-glass slab proportions,
8. generic spade / turntable logo as the hardware identity,
9. bright amber shell as the only/default canonical colorway,
10. extra unexplained ports, holes, wheels, antennas, clips, speakers, buttons, or decorative parts,
11. production-ready labels or manufacturing certainty,
12. conflicting dimensions or unlabeled scale changes.

## Render Set Strategy

Never generate one isolated hero image first. Generate controlled sets in this order:

1. **Orthographic consistency sheet**
   - front
   - back
   - right side / thumb-control side
   - bottom edge

2. **Technical placement sheet**
   - labeled component placement
   - keepout zones
   - internal stack block diagram
   - camera/mic/jack/antenna provisional zones

3. **Exploded stack render**
   - shell
   - display
   - PCBA
   - frame/shield zones
   - battery
   - camera module if retained
   - mic-port/acoustic path concept
   - USB-C and optional 3.5mm jack

4. **Lifestyle renders**
   - hand scale
   - record crate browsing
   - turntable/acoustic capture context
   - pocket carry context

Lifestyle renders come last because they are easier to make visually exciting but worse for locking geometry.

## Master Prompt Structure

Every text-to-image prompt should use labeled blocks. Do not use a loose paragraph.

```text
Asset type: Industrial design render consistency sheet for yadiggg.

Primary request: Create a hyper-accurate render of the canonical yadiggg V1 device according to the locked visual direction. The product is a compact, portrait-first, 105mm x 60mm x 15mm-class pocket field recorder for vinyl crate digging.

Canvas and composition: [state requested view: front / back / side / bottom / exploded / lifestyle]. Keep the same body proportions, corner radius language, shell thickness impression, display position, control placement, and port logic across the set.

Camera: [orthographic / three-quarter studio / exploded isometric / lifestyle handheld]. Avoid perspective distortion that changes perceived proportions.

Scene/backdrop: [neutral studio / technical white background / record-store lifestyle]. Use only the props needed for the requested view, no other objects.

Lighting and grounding: soft studio lighting, realistic shadows, translucent-shell refraction kept subtle, physically grounded contact shadows.

Materials, color and style: smoke-clear translucent polycarbonate shell, restrained dark internals, matte black PCB/shield language, amber/orange side control, monochrome Sharp Memory LCD. Precise industrial design language, not sci-fi gadget styling.

Product invariants: Preserve compact portrait-first 105mm x 60mm x 15mm-class body, large upper-front monochrome display, one amber/orange side thumb control, USB-C bottom port, optional 3.5mm jack, tiny mic ports, provisional rear OCR/macro camera. Use yadiggg or no visible branding; never Crate IQ.

Allowed changes: camera angle, view type, lighting, background, and technical callout style only.

Avoid: keypad, multi-button grid, top knurled cylinder, Crate IQ branding, horizontal side-display slab, walkie-talkie bulk, generic spade logo, production-ready labels.
```

## Orthographic Prompt

```text
Asset type: Four-view orthographic industrial design sheet for yadiggg.

Primary request: Create a consistent four-view product sheet showing the same yadiggg V1 device in front, back, right side, and bottom-edge views. The product is a compact portrait-first 105mm x 60mm x 15mm-class pocket field recorder for vinyl crate digging.

Canvas and composition: Clean technical layout on a neutral light background. Arrange views evenly with consistent scale. Front view is dominant, back view beside it, right side view narrow, bottom-edge view below. Include no production-ready stamp or final manufacturing label.

Camera: Orthographic technical drawing style with minimal perspective distortion.

Scene/backdrop: Plain neutral technical background, no lifestyle props, no extra objects.

Lighting and grounding: soft even technical lighting, subtle contact shadows only, clear edges, no dramatic reflections.

Materials, color and style: smoke-clear translucent polycarbonate shell, restrained dark visible internals, matte black internal PCB/shield visual language, amber/orange side thumb control, monochrome Sharp Memory LCD. Clean industrial design board style.

Product invariants: Preserve compact portrait-first 105mm x 60mm x 15mm-class body, large upper-front monochrome display, one amber/orange side thumb control, USB-C bottom port, optional 3.5mm jack, tiny mic ports, provisional rear OCR/macro camera. Use yadiggg or no visible branding; never Crate IQ.

Allowed changes: view arrangement, technical linework style, lighting, and neutral background only.

Avoid: keypad, multi-button grid, top knurled cylinder, Crate IQ branding, horizontal side-display slab, walkie-talkie bulk, generic spade logo, production-ready labels.
```

## Exploded Stack Prompt

```text
Asset type: Exploded internal stack render for yadiggg.

Primary request: Create a consistent exploded internal stack view of the canonical yadiggg V1 device, showing how the shell, display, PCBA, battery, side control, USB-C, optional 3.5mm jack, mic ports, antenna keepout, and provisional rear OCR/macro camera could fit inside the compact 105mm x 60mm x 15mm-class envelope.

Canvas and composition: Isometric exploded view with parts separated vertically just enough to understand assembly order. Keep all parts aligned to the same compact portrait body footprint. Do not change the product silhouette into a horizontal slab.

Camera: Technical isometric camera, moderate perspective, no dramatic wide-angle distortion.

Scene/backdrop: Plain light technical background, no props, no hands, no lifestyle scene.

Lighting and grounding: soft even light, subtle ambient occlusion under parts, readable translucent shell edges.

Materials, color and style: smoke-clear translucent top and bottom shell, restrained dark PCBA and shield regions, simple display module, plausible flat battery volume, amber/orange side control, small camera module as provisional, tiny mic-port acoustic path indication. Technical concept render, not final CAD.

Product invariants: Preserve compact portrait-first 105mm x 60mm x 15mm-class body, large upper-front monochrome display, one amber/orange side thumb control, USB-C bottom port, optional 3.5mm jack, tiny mic ports, provisional rear OCR/macro camera. Use yadiggg or no visible branding; never Crate IQ.

Allowed changes: exploded spacing, technical callout placement, neutral background, and internal-component simplification only.

Avoid: keypad, multi-button grid, top knurled cylinder, Crate IQ branding, horizontal side-display slab, walkie-talkie bulk, generic spade logo, production-ready labels.
```

## Lifestyle Prompt

```text
Asset type: Lifestyle product render for yadiggg.

Primary request: Show the canonical yadiggg V1 device being used as a compact pocket field recorder for vinyl crate digging.

Canvas and composition: Device in one hand near a record crate or turntable context, scaled like a 105mm x 60mm x 15mm-class pocket object. The device remains the clear subject, with the front display and side amber/orange thumb control visible. Avoid props blocking the display, ports, mic ports, or overall silhouette.

Camera: realistic product photography, 50mm-equivalent natural perspective, close product-scale framing, shallow but not excessive depth of field.

Scene/backdrop: record-store or vinyl-listening environment with only restrained contextual elements: record sleeve edge, crate edge, wood or matte counter surface, soft background shelves. No other objects.

Lighting and grounding: warm but controlled ambient light, realistic hand/product shadows, subtle highlights through smoke-clear shell.

Materials, color and style: smoke-clear translucent polycarbonate shell, restrained dark visible internals, amber/orange side control, monochrome Sharp Memory LCD. Premium practical hardware, not a toy, not a sci-fi prop.

Product invariants: Preserve compact portrait-first 105mm x 60mm x 15mm-class body, large upper-front monochrome display, one amber/orange side thumb control, USB-C bottom port, optional 3.5mm jack, tiny mic ports, provisional rear OCR/macro camera. Use yadiggg or no visible branding; never Crate IQ.

Allowed changes: hand pose, environment, camera angle, and lighting only.

Avoid: keypad, multi-button grid, top knurled cylinder, Crate IQ branding, horizontal side-display slab, walkie-talkie bulk, generic spade logo, production-ready labels.
```

## Higgsfield Usage Notes

For Higgsfield image generation through `accio-mcp-cli`:

- Use JSON parameter passing only.
- Prefer a controllable text-to-image model when exact consistency matters.
- If the tool supports seed control, reuse the same seed for a render set and vary only the view block.
- Generate orthographic/technical images before lifestyle images.
- Do not move to video generation until a still-image geometry is accepted.

Recommended first still-image task:

```json
{
  "prompt": "<Orthographic Prompt from this document>",
  "model_id": "flux-pro/kontext/max/text-to-image",
  "seed": 7331,
  "negative_prompt": "keypad, many buttons, top knurled cylinder, Crate IQ text, horizontal side-display slab, walkie-talkie, phone slab, generic spade logo, production-ready label, extra ports, bulky proportions, bright amber-only shell",
  "wait_for_completion": true
}
```

If using Seedream v4, specify `resolution: "2K"` or `"4K"`; do not use 720p or 1080p with that model.

## Render Acceptance Checklist

A render passes only if all of these are true:

- [ ] Body reads as compact portrait-first pocket field recorder.
- [ ] Approximate visual envelope remains 105mm x 60mm x 15mm-class.
- [ ] Shell is smoke-clear / grey translucent, not default bright amber.
- [ ] Front face has one large upper monochrome display.
- [ ] There is no keypad or multi-button grid.
- [ ] There is exactly one dominant amber/orange side thumb control.
- [ ] Internals are visible but restrained, dark, and not visually chaotic.
- [ ] USB-C bottom port is present in technical views.
- [ ] 3.5mm jack appears only as optional/provisional when shown.
- [ ] Tiny mic ports are present in technical views.
- [ ] Rear OCR/macro camera is present only as provisional.
- [ ] No Crate IQ branding appears.
- [ ] No generic spade logo appears.
- [ ] No production-ready, final-CAD, or manufacturing-complete claim appears.
- [ ] The render does not contradict `placement-sketch.md`.

## Failure Response

If a render fails consistency:

1. Reject it as reference-only.
2. Name the exact failed invariant.
3. Do not use it as a seed/reference for future canonical renders.
4. Regenerate from the orthographic prompt or edit from the most consistent accepted image.

Do not rescue a wrong form factor by describing it as a variant unless the variant is explicitly approved in an ADR.
