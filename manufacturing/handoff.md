# Supplier handoff — yadiggg engineering review

**Package status:** unreleased engineering-review material only. This request is for engineering review, design-for-manufacturing (DFM) feedback, and prototype-planning estimates. It is not authority to manufacture production units, order parts, create tooling, or treat any source as released.

## Product and requested work

`yadiggg` is an intended pocket field recorder / crate-digging assistant. The user workflow and provisional appearance are described in the [product specification](../physical-design/final-product-source-of-truth.md). The `105 × 60 × 15 mm` envelope is not approved. Camera, display, control, battery, connectors, electrical design, and material/process remain unresolved.

Please review the listed artifacts only for feasibility and DFM questions. Identify missing inputs, incompatible assumptions, supplier-specific constraints, likely process choices, and evidence needed to proceed to a prototype quote. Do not substitute parts or create fabrication data without written engineering approval.

## Available artifacts and limits

| Artifact | Location | Revision / status | Permitted use |
|---|---|---|---|
| Product direction | `physical-design/final-product-source-of-truth.md` | Current design intent; revision is the Git commit recorded in any review bundle | Concept discussion only |
| Visual reference | `assets/product/yadiggg-studio-hero.png` | Concept art | Appearance discussion only; not a drawing |
| Mechanical model | `physical-design/cad/yadiggg_v1_block_model.scad` | Provisional block model; not validated for fit | Packaging discussion only |
| KiCad project | `hardware/yadiggg.kicad_pro`, `hardware/yadiggg.kicad_sch`, `hardware/yadiggg.kicad_pcb` | Incomplete scaffold; no approved electrical design | Not fabrication input |
| Prototype source / OS metadata | `src/sonic_id/`, `yocto-meta/meta-yadiggg/` | Experimental source and unverified build scaffold | Engineering evaluation only |
| Draft component candidates | [`draft-bom.csv`](draft-bom.csv) | Conflicted proposal transcription; every row unverified | Do not purchase or substitute from this file |
| Open blockers | [`readiness register`](../docs/project-state.md) | All production workstreams open | Closure planning |

No released Gerbers, drill files, STEP enclosure, pick-and-place, assembly drawings, test fixture, or approved purchasing BOM is supplied. None will be fabricated from the present scaffold.

## Revision, licensing, and approvals

Review bundle contents are tied to a Git commit and SHA-256 checksums in the generated bundle manifest. The package is marked as an unreleased engineering review. A new bundle is required after source changes.

The repository does not establish redistribution rights for the prototype code or all incorporated source material. Yocto recipes mark the application and image `CLOSED` rather than invent a license. Confirm ownership, third-party attribution, and supplier disclosure rights before redistribution or manufacture.

Production release remains blocked pending the [readiness register](../docs/project-state.md), revision-linked artifact evidence, and approvals by the required engineering, quality, supplier, and regulatory roles. A completed form or populated manifest is not approval.
