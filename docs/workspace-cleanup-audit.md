---
title: "Workspace Cleanup Audit"
project: yadiggg
status: active-draft
type: audit_report
tags: [yadiggg, cleanup, obsidian, architecture-review]
backlinks:
  - "[[CONTEXT]]"
  - "[[yadiggg_vault_overview]]"
  - "[[docs/adr/0001-source-of-truth-and-archive-policy]]"
---

# yadiggg Workspace Cleanup Audit

## Executive Summary

The workspace is **not clean enough to treat as a final engineering vault**. It has useful work, but it mixes:

1. active yadiggg specs,
2. older Crate IQ source/reference PDFs,
3. failed OCR extraction text files,
4. rendered image caches,
5. KiCad scaffolds,
6. Yocto scaffolds,
7. sandbox C prototypes,
8. generated metadata/backlink passes,
9. and conflicting BOM/physical-design assumptions.

The biggest issue is not only file clutter. The deeper issue is that the vault lacked a decision spine. That has now been repaired by creating `docs/adr/0001` through `docs/adr/0010` and updating `CONTEXT.md` plus `yadiggg_vault_overview.md`.

## Current Truth Level

| Area | Current status | Notes |
|---|---|---|
| `CONTEXT.md` | Keep / authoritative spine | Updated to point at ADRs and stop overstating lock status. |
| `docs/adr/` | Keep / authoritative decision memory | Newly added. Should become the handoff spine. |
| Root yadiggg Markdown specs | Keep, but status varies | Some are active references; some overstate finality. |
| `hardware/*.kicad_*` | Keep / scaffold | Opens after parser fixes, but not fabrication-ready. |
| `src/sonic_id/` | Keep / prototype | Compiles locally, but real audio/target validation missing. |
| `yocto-meta/meta-yadiggg/` | Keep / scaffold | Structure exists; no verified BitBake image yet. |
| Crate IQ PDFs | Archive/reference | Useful provenance, not active truth. |
| `extracted_text/*.txt` | Archive/delete candidates | Most contain only `[No text found]`; failed extraction artifacts. |
| `rendered_pages/*.png` | Archive/reference or derived cache | Useful for visual review, but not active design truth. |
| Random root image assets | Needs review | Some may be design references; currently unlabeled and disconnected. |
| Build outputs (`*.o`, `yadiggg_capture`, `yadiggg.db`) | Regenerable artifacts | Keep only if convenient; should not be source of truth. |

## Recommended File Disposition

### Keep as Active Source of Truth

These should stay in the active vault root or active subfolders:

- `CONTEXT.md`
- `yadiggg_vault_overview.md`
- `docs/adr/*.md`
- `yadiggg_product_and_interaction_architecture.md`
- `yadiggg_brand_identity_and_design_guidelines.md`
- `yadiggg_firmware_and_update_architecture.md`
- `yadiggg_adversarial_testing_and_validation_protocol.md`
- `yadiggg_intelligence_graph_and_schema.md`
- `yadiggg_schema.sql`
- `yadiggg_yocto_setup.sh`

Caveat: several of these still need frontmatter status correction from `completed` to `authoritative`, `active-draft`, or `reference`.

### Keep, But Mark as Scaffold or Prototype

- `hardware/yadiggg.kicad_pro`
- `hardware/yadiggg.kicad_sch`
- `hardware/yadiggg_*.kicad_sch`
- `hardware/yadiggg.kicad_pcb`
- `scripts/generate_kicad_project.py`
- `scripts/deploy_yocto_layer.py`
- `scripts/connect_obsidian_vault.py`
- `src/sonic_id/*`
- `yocto-meta/meta-yadiggg/**`

Reason: these are useful seams and adapters for future work, but the current interface does not hide enough implementation complexity to call them deep or production-ready. They are bootstrap scaffolds.

### Keep as Reference, Not Manufacturing Truth

- `yadiggg_renderings_and_use_cases.md`
- root visual images (`*.png`, `*.avif`) pending labeling
- `yadiggg_pinmux_routing.png`
- `yadiggg_spec_mismatches.png`
- generated PDFs of active Markdown specs

Reason: current physical direction is not locked. The visual references do not yet define a manufacturable industrial design system.

### Archive Candidates

Move later, with user approval, to something like `archive/source-inputs/`:

- `Crate Iq Quick Start.pdf`
- `Crate Iq Typography Final.pdf`
- `Crate Iq Firmware Architecture.pdf`
- `Crate Iq Final Bom.pdf`
- `Crate Iq User Interactions.pdf`
- `Crate Iq Physical Specs.pdf`
- `Crate Iq Scope Document.pdf`
- `Crate Iq Master Roadmap.pdf`
- `Crate Iq Usa Sourcing Plan.pdf`
- `Intelligence Engine Test.pdf`
- duplicate PDFs: `Ya Diggg Advanced Specs (1).pdf`, `Ya Diggg Sonic Id Spec (1).pdf`

Reason: they are provenance/reference, but active specs have moved to yadiggg Markdown and ADRs.

### Delete or Archive as Failed Extraction Artifacts

Move later, with user approval, to `archive/failed-extractions/` or delete:

- `extracted_text/*.txt`

Reason: most contain only page markers and `[No text found on this page]`. They are not useful Obsidian content and pollute search/graph if indexed.

### Regenerable Build Artifacts

Archive/delete later after user approval:

- `src/sonic_id/*.o`
- `yadiggg_capture`
- `yadiggg.db`
- `hardware/.history/` if not intentionally used
- `.DS_Store`

Reason: these are generated outputs or editor/system metadata. They should not be hand-maintained.

## Known Erroneous or Overstated Claims

These need correction in future doc passes:

1. **KiCad readiness**: earlier summaries overstated the project as production/fabrication-ready. ADR-0003 now corrects this.
2. **Yocto readiness**: the layer exists but no verified BitBake image exists. ADR-0006 corrects this.
3. **Sonic ID readiness**: local compile is not production validation. ADR-0005 corrects this.
4. **Physical design alignment**: renderings are not a physical direction package. ADR-0002 corrects this.
5. **BOM conflicts**: `docs/component-selections.md` conflicts with `yadiggg_hardware_and_electrical_integration.md`. ADR-0007 flags reconciliation as required.
6. **Graph metadata**: mass-added `status: completed` frontmatter was too coarse. ADR-0008 defines a better status vocabulary.

## Architecture Review: Deepening Opportunities

### Candidate 1: Create a `Project State` Module

**Files involved**: `CONTEXT.md`, `yadiggg_vault_overview.md`, `docs/adr/*.md`, future `docs/project-state.md`.

**Problem**: Status is spread across many files. Understanding what is current requires bouncing between specs, generated outputs, and chat memory.

**Solution**: Create one deep `Project State` module that lists every major deliverable with role, status, owner, source-of-truth link, and next action.

**Benefit**: Better locality. Future sessions read one file and know what to trust.

**Recommendation**: Strong.

### Candidate 2: Create a `Physical Direction Package`

**Files involved**: `yadiggg_renderings_and_use_cases.md`, brand guide, hardware integration, KiCad board files.

**Problem**: Visuals exist, but they are not a manufacturable physical direction. PCB geometry and renderings are not tied to a real enclosure/package.

**Solution**: Create `physical-design/` with orthographic views, dimensions, interaction map, CMF, internal stack, and constraints that drive KiCad/mechanical work.

**Benefit**: Better leverage and locality. KiCad and mechanical design can depend on a clear interface instead of scattered images.

**Recommendation**: Strong.

### Candidate 3: Normalize the BOM into One Current BOM

**Files involved**: `docs/component-selections.md`, `yadiggg_hardware_and_electrical_integration.md`, old `Crate Iq Final Bom.pdf`.

**Problem**: Multiple BOMs disagree on PMIC, memory, eMMC, microphones, co-processor, and camera assumptions.

**Solution**: Create `docs/bom-current.md` with one selected part per function and explicit rejected alternatives.

**Benefit**: High leverage. Ordering, KiCad symbols, footprints, and sourcing can all depend on one stable interface.

**Recommendation**: Strong.

### Candidate 4: Split Generated Outputs from Source Files

**Files involved**: `rendered_pages/`, `extracted_text/`, generated PDFs, `.o`, database, binaries.

**Problem**: The vault treats generated assets like active knowledge. This makes Graph View noisy and search misleading.

**Solution**: Create an archive/cache convention: `archive/source-inputs/`, `archive/rendered-pages/`, `build/`, `cache/`, or equivalent.

**Benefit**: Better locality and less noise. Active docs become readable as a knowledge base.

**Recommendation**: Worth exploring.

## Recommended Next Actions

1. Create `docs/project-state.md` as the active handoff file.
2. Reclassify frontmatter statuses across active Markdown files using ADR-0008.
3. Create `physical-design/physical-direction-brief.md` and move renderings into reference status.
4. Create `docs/bom-current.md` and reconcile all BOM conflicts.
5. After review, move archive candidates using Trash-safe operations, not permanent deletion.
6. Add `.gitignore` for generated artifacts and system metadata if this becomes a Git repo.

## Do Not Do Yet

- Do not delete Crate IQ files until the user confirms archival policy.
- Do not rerun `scripts/generate_kicad_project.py` after hand-editing KiCad files.
- Do not generate manufacturing files from the current KiCad scaffold.
- Do not order parts from either current BOM until reconciliation is complete.
