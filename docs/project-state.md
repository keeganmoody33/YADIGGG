---
title: "Project State"
project: yadiggg
status: authoritative
type: handoff_state
tags: [yadiggg, project-state, handoff, obsidian]
backlinks:
  - "[[CONTEXT]]"
  - "[[yadiggg_vault_overview]]"
  - "[[docs/workspace-cleanup-audit]]"
  - "[[docs/adr/0001-source-of-truth-and-archive-policy]]"
  - "[[docs/adr/0010-context-and-adr-are-required-handoff-nodes]]"
---

# yadiggg Project State

## Purpose

This is the **single live status table** for the yadiggg workspace. Start here when entering the project from Obsidian or a new chat session.

This file answers:

1. What is current?
2. What is only a scaffold or prototype?
3. What is reference/archive material?
4. What should happen next?
5. Which ADR explains the decision?

## Status Vocabulary

Use the statuses from [[docs/adr/0008-obsidian-metadata-must-reflect-status]]:

| Status | Meaning |
|---|---|
| `authoritative` | Current source of truth for this area. |
| `active-draft` | Useful and current, but still being refined. |
| `scaffold` | Structure exists, but not real implementation/validation. |
| `prototype` | Working exploration; not production validated. |
| `reference` | Useful input, image, or background material. |
| `superseded` | Replaced by newer files or decisions. |
| `archive-candidate` | Likely should move out of the active vault after approval. |
| `regenerable` | Build/cache/output artifact; recreate from source when needed. |

## Source-of-Truth Spine

| Deliverable | Status | Source / location | Decision record | Next action |
|---|---:|---|---|---|
| Domain language and handoff map | `authoritative` | [[CONTEXT]] | [[docs/adr/0010-context-and-adr-are-required-handoff-nodes]] | Keep updated whenever decisions change. |
| Vault dashboard / MOC | `authoritative` | [[yadiggg_vault_overview]] | [[docs/adr/0001-source-of-truth-and-archive-policy]] | Keep links synced with this table. |
| Cleanup audit | `active-draft` | [[docs/workspace-cleanup-audit]] | [[docs/adr/0001-source-of-truth-and-archive-policy]] | Use as basis for archive moves after user approval. |
| ADR decision spine | `authoritative` | `docs/adr/*.md` | [[docs/adr/0001-source-of-truth-and-archive-policy]] | Add a new ADR for every material decision. |

## Product and Brand Documents

| Deliverable | Status | Source / location | Notes | Next action |
|---|---:|---|---|---|
| Brand identity | `active-draft` | [[yadiggg_brand_identity_and_design_guidelines]] | Strong visual direction, but may conflict with later physical direction and renderings. | Reconcile CMF once physical direction is locked. |
| Product interaction architecture | `active-draft` | [[yadiggg_product_and_interaction_architecture]] | Useful product logic and user flow. | Review after physical controls are placed. |
| Strategic roadmap | `reference` | [[yadiggg_strategic_decision_map_and_roadmap]] | Useful history; contains older “formerly Crate IQ” framing. | Pull only still-current decisions into ADRs. |
| Renderings and use cases | `reference` | [[yadiggg_renderings_and_use_cases]] | Not physical design truth. See ADR-0002. | Reclassify after [[physical-design/physical-direction-brief]] matures. |

## Physical Design and Hardware

| Deliverable | Status | Source / location | Decision record | Next action |
|---|---:|---|---|---|
| Physical direction | `active-draft` | [[physical-design/physical-direction-brief]] | [[docs/adr/0002-physical-design-direction-not-yet-locked]], [[docs/adr/0011-provisional-v1-physical-direction-assumptions]] | Convert provisional V1 assumptions into placement sketch, OCR/camera opportunity-cost matrix, control durability matrix, 3.5mm jack fit check, and KiCad keepout updates. |
| Hardware/electrical integration | `active-draft` | [[yadiggg_hardware_and_electrical_integration]] | [[docs/adr/0007-component-bom-is-conflicted-and-needs-reconciliation]] | Reconcile against BOM and physical direction. |
| Component selections / BOM map | `active-draft` | [[docs/component-selections]] | [[docs/adr/0007-component-bom-is-conflicted-and-needs-reconciliation]] | Create `docs/bom-current.md` before ordering. |
| Design constraints JSON | `reference` | `docs/design-constraints.json` | [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]] | Keep as input; convert into KiCad constraints later. |
| Schematic status report | `scaffold` | [[docs/schematic-status]] | [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]] | Rewrite after real schematic capture/ ERC. |
| Pinmux spec | `active-draft` | [[hardware/yadiggg_pinmux]] | [[docs/adr/0007-component-bom-is-conflicted-and-needs-reconciliation]] | Verify against real NXP pin tables before schematic capture. |
| Audio DAC and mic schematic notes | `active-draft` | [[hardware/yadiggg_audio_dac_and_mic_schematics]] | [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]] | Verify with datasheets and BOM-current. |
| PCB layout guidelines | `active-draft` | [[hardware/yadiggg_pcba_v1_layout_guidelines]] | [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]] | Re-run after physical direction and BOM-current are locked. |

## KiCad CAD Files

| Deliverable | Status | Source / location | Decision record | Next action |
|---|---:|---|---|---|
| KiCad project shell | `scaffold` | `hardware/yadiggg.kicad_pro` | [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]] | Open in KiCad 10, then begin real schematic capture. |
| KiCad master schematic | `scaffold` | `hardware/yadiggg.kicad_sch` | [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]] | Add real symbols, pins, nets, annotations. |
| KiCad sub-sheets | `scaffold` | `hardware/yadiggg_*.kicad_sch` | [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]] | Fill with real circuits only after BOM reconciliation. |
| KiCad PCB file | `scaffold` | `hardware/yadiggg.kicad_pcb` | [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]] | Treat board outline as provisional until physical direction locks. |
| KiCad generator script | `scaffold` | `scripts/generate_kicad_project.py` | [[docs/adr/0009-generators-must-not-overwrite-hand-authored-work]] | Do not rerun after manual KiCad edits unless backup/dry-run is added. |

## Firmware, OS, and Data

| Deliverable | Status | Source / location | Decision record | Next action |
|---|---:|---|---|---|
| Firmware/update architecture | `active-draft` | [[yadiggg_firmware_and_update_architecture]] | [[docs/adr/0006-yocto-layer-is-build-scaffold]] | Validate boot claims against target board later. |
| Yocto setup script | `scaffold` | `yadiggg_yocto_setup.sh` | [[docs/adr/0006-yocto-layer-is-build-scaffold]] | Run in real Yocto build env; capture build log. |
| Yocto layer | `scaffold` | `yocto-meta/meta-yadiggg/` | [[docs/adr/0006-yocto-layer-is-build-scaffold]] | Build with BitBake before treating as verified. |
| Yocto recipe guide | `active-draft` | [[hardware/yadiggg_yocto_recipe_and_image_build]] | [[docs/adr/0006-yocto-layer-is-build-scaffold]] | Update after successful image build. |
| Database schema | `active-draft` | `yadiggg_schema.sql` | [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]] | Separate seed/mock data from production schema. |
| Local SQLite DB | `regenerable` | `yadiggg.db` | [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]] | Regenerate from schema; do not hand-edit. |
| Intelligence graph spec | `active-draft` | [[yadiggg_intelligence_graph_and_schema]] | [[docs/adr/0001-source-of-truth-and-archive-policy]] | Reconcile against current SQL schema. |
| Adversarial validation protocol | `active-draft` | [[yadiggg_adversarial_testing_and_validation_protocol]] | [[docs/adr/0010-context-and-adr-are-required-handoff-nodes]] | Convert tests into executable validation checklist later. |

## Sonic ID / Audio Code

| Deliverable | Status | Source / location | Decision record | Next action |
|---|---:|---|---|---|
| Sonic ID architecture note | `active-draft` | [[hardware/yadiggg_sonic_id_and_olaf_port]] | [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]] | Correct language that overstates production readiness. |
| OLAF-like DSP code | `prototype` | `src/sonic_id/olaf.c`, `src/sonic_id/olaf.h` | [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]] | Add fixtures, compare against known references, verify algorithm. |
| Capture daemon | `prototype` | `src/sonic_id/yadiggg_capture.c` | [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]] | Validate on target ALSA/PDM hardware. |
| ALSA config | `active-draft` | `src/sonic_id/asound.conf` | [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]] | Test on target kernel/audio card. |
| Object files and binary | `regenerable` | `src/sonic_id/*.o`, `yadiggg_capture` | [[docs/adr/0001-source-of-truth-and-archive-policy]] | Move to build/cache or delete later. |

## Archive / Reference Inputs

| Deliverable | Status | Source / location | Decision record | Next action |
|---|---:|---|---|---|
| Crate IQ PDFs | `archive-candidate` | `Crate Iq *.pdf` | [[docs/adr/0004-crate-iq-files-are-archival-inputs]] | Move to `archive/source-inputs/` after approval. |
| Duplicate Ya Diggg PDFs | `archive-candidate` | `Ya Diggg Advanced Specs (1).pdf`, `Ya Diggg Sonic Id Spec (1).pdf` | [[docs/adr/0004-crate-iq-files-are-archival-inputs]] | Remove duplicates after confirming originals. |
| Failed OCR text | `archive-candidate` | `extracted_text/*.txt` | [[docs/adr/0004-crate-iq-files-are-archival-inputs]] | Archive or delete; most contain no useful text. |
| Rendered page images | `reference` | `rendered_pages/*.png` | [[docs/adr/0002-physical-design-direction-not-yet-locked]] | Move to reference/archive after physical brief. |
| Root image files | `reference` | `*.png`, `*.avif` | [[docs/adr/0002-physical-design-direction-not-yet-locked]] | Label with meaning or archive. |

## Current Top Priorities

1. **Create physical placement sketch** from [[physical-design/physical-direction-brief]] and [[docs/adr/0011-provisional-v1-physical-direction-assumptions]].
2. **Run OCR/camera opportunity-cost matrix** before treating camera/OCR as locked.
3. **Run control durability matrix** before choosing slider/button/rocker/wheel.
4. **Reconcile BOM** into `docs/bom-current.md` before schematic capture or part ordering.
5. **Convert KiCad scaffold into real schematic capture** only after physical direction and BOM-current are stable.
6. **Clean archive/cache files** after user approves move plan.

## Handoff Rule

Before ending a future session, update this file if any deliverable changes status, if a new source-of-truth file appears, or if a decision is made that affects physical design, BOM, KiCad, firmware, Yocto, or Sonic ID.
