# yadiggg product specification

**Status:** design intent; not released for manufacture. This is the canonical statement of current product direction. The [readiness register](../docs/project-state.md) is authoritative for engineering completion.

## Product

`yadiggg` is intended to be a compact pocket field recorder and crate-digging assistant. A user should be able to capture a record encountered while browsing and use audio identification and, if feasible, visual label capture to discover the release and its context.

The intended form is portrait-first, pocketable, and operable one-handed. The current visual concept uses a smoke-clear shell, a monochrome front display, and one amber side control. This describes visual intent only; it does not approve a part, mechanism, material grade, or enclosure.

![Concept rendering of yadiggg; not a dimensional or manufacturing reference](../assets/product/yadiggg-studio-hero.png)

## Requirements and unresolved choices

| Area | Current intent | State |
|---|---|---|
| Product workflow | Record/track identification while browsing vinyl, followed by music/credit discovery | Intended capability; full product workflow is not implemented |
| Form | Compact, portrait-first, one-handed pocket device | Design intent |
| Envelope | `105 × 60 × 15 mm` class | Provisional visual target only; not approved geometry |
| Display | Monochrome display on the front | Exact display, interface, and dimensions unresolved |
| Main control | Amber side control | Button/rocker/wheel mechanism and durability unresolved |
| Audio input | Acoustic capture for experimental identification | Microphone and audio architecture unresolved; prototype code is not target-validated |
| Camera / OCR | Optional record-label or run-out capture remains under feasibility review | Not implemented; inclusion, sensor, optics, placement, and performance unresolved |
| Connectors, battery, electronics | To be determined by engineering | No released selections |
| Exterior | Smoke-clear visual direction | Material, colorant, process, wall design, finish, tolerances, and validation unresolved |

The render is concept art. It must not be used as a drawing, tolerance definition, color specification, tool-design reference, or evidence of internal fit. The OpenSCAD file is a block model only. KiCad files are scaffolds.

## Evidence and change control

Distinguish:

- **Intent:** this specification and selected concept art.
- **Prototype:** experimental code or scaffold artifacts listed in the readiness register.
- **Validated:** only work with revision-linked test results and review evidence.
- **Released for manufacture:** only after every blocker is closed and the required engineering, quality, supplier, and regulatory reviews are recorded.

Do not infer hardware choices from old Crate IQ material or from archived Ya Diggg PDFs. See the [archive migration record](../archive/README.md), [ADRs](../docs/adr/), and [manufacturer handoff](../manufacturing/handoff.md).
