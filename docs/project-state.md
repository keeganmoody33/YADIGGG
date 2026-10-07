# Engineering readiness register

**Release state:** engineering review / prototype planning only. **Production release is not authorized.** Every row below remains open; a document or populated template is not evidence that engineering work or approval has occurred.

This register is the single authoritative view of release blockers. Product intent is defined in the [product specification](../physical-design/final-product-source-of-truth.md); supplier instructions and artifact locations are in the [manufacturer handoff](../manufacturing/handoff.md).

| Workstream | Status | Evidence in this repository | Closure evidence required | Required role(s) |
|---|---|---|---|---|
| Electrical design, schematic, ERC | Open | `hardware/yadiggg.kicad_sch` and its sheets are empty scaffolds; [schematic status](schematic-status.md) | Complete reviewed schematic with actual symbols, connectivity, selected components, ERC results, and disposition of every error/warning | Electrical design engineer; independent reviewer |
| PCB layout, DRC, fabricator review | Open | `hardware/yadiggg.kicad_pcb` is an incomplete outline/scaffold; [historical layout proposal](../archive/historical-proposals/yadiggg_pcba_v1_layout_guidelines.md) is not evidence of completed routing | Routed board tied to the released schematic/BOM, DRC report and approved exceptions, stack-up/constraints, and fabricator DFM acceptance | PCB layout engineer; fabricator |
| Enclosure geometry and fit | Open | `physical-design/cad/yadiggg_v1_block_model.scad` is a provisional block model; concept images are not drawings | Dimensioned CAD with component fit/clearance, control/port/camera decisions, material and process, tolerances, assembly interfaces, and reviewed physical prototype evidence | Mechanical/industrial design engineer; prototype reviewer |
| BOM and substitutions | Open | [`draft-bom.csv`](../manufacturing/draft-bom.csv) transcribes conflicting, unverified proposals | One revision-controlled BOM reconciled to schematic/layout, verified MPN/package/lifecycle/source, approved alternates, quantities, and engineering approval | Electrical/BOM engineer; sourcing reviewer |
| Fabrication and assembly outputs | Open | No released Gerbers, drill files, pick-and-place, assembly drawings, or production CAD are present | Generated outputs from the reviewed design revision; independent output inspection and manufacturer acceptance | Electrical/PCB engineer; mechanical engineer; fabricator/CM |
| Firmware, programming, recovery | Open | `src/sonic_id/` is experimental; `yocto-meta/meta-yadiggg/` is an unverified build scaffold | Reproducible target build tied to released hardware, programming instructions, boot/update/recovery procedure, and tested recovery evidence | Embedded software engineer; manufacturing test engineer |
| Fixture, functional test, calibration | Open | No fixture, acceptance limits, calibration procedure, or test results are present | Test plan and fixture specification with measurable acceptance criteria, calibration method if needed, and recorded prototype verification | Test/validation engineer; manufacturing engineer |
| Packaging and product marking | Open | No released packaging, labels, serial-number scheme, or marking artwork is present | Approved packaging/marking specification tied to product revision and traceability requirements | Product/packaging engineer; quality representative |
| Safety and regulatory assessment | Open | No applicability assessment, test reports, certifications, or approvals are present | Qualified assessment identifies applicable markets/requirements; required test evidence and approvals are completed before release | Product safety/regulatory specialist; responsible engineering approver |

## Release decision

`production_release_eligible` is **false**. Do not manufacture production units, order from proposal prices, treat candidate parts as approved, or create/send fabricated outputs as released data. Engineering review may identify feasibility and DFM work only.

Reopen a row only when its closure evidence exists, is revision-linked, and has been reviewed by the required role. Update this register and the machine-readable release manifest together; production packaging must fail closed while any blocker remains open.
