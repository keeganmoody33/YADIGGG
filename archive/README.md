# Archive and migration map

This directory preserves source material for provenance; it is not current product authority. The current yadiggg specification and engineering readiness are in [`physical-design/final-product-source-of-truth.md`](../physical-design/final-product-source-of-truth.md) and [`docs/project-state.md`](../docs/project-state.md).

| Previous location | Current location | Disposition |
|---|---|---|
| Root `Crate Iq *.pdf`, `Intelligence Engine Test.pdf`, and the scope-page image | `archive/legacy-crate-iq/` | Preserved with original filenames as historical inputs |
| Root `Ya Diggg *.pdf` | `archive/yadiggg-source/pdfs/` | Preserved as source/reference documents, not current specifications |
| Root `yadiggg_*.pdf` | `archive/generated-exports/pdfs/` | Preserved as generated PDF exports; the Markdown remains the editable source |
| Root-level brand, interaction, firmware, graph/schema, rendering, and roadmap proposals; detailed audio/pinmux/PCB/Sonic-ID notes | `archive/historical-proposals/` | Preserved with original names as unverified engineering history, not current requirements |
| `physical-design/physical-direction-brief.md`, `visual-consistency-audit.md`, `placement-sketch.md`, and `cad-block-model-brief.md` | `archive/historical-proposals/` | Original detailed drafts retained; active files now point to the current specification and blockers |
| Original `docs/component-selections.md` and `docs/schematic-status.md` | `archive/historical-proposals/` | Original proposals preserved; active pages now point to the candidate BOM/readiness status |
| `yadiggg_adversarial_testing_and_validation_protocol.md` | `docs/testing/adversarial-validation-protocol.md` | Moved to testing documentation; protocol is not test evidence |
| `yadiggg_schema.sql` | `data/schema.sql` | Production schema separated from its synthetic sample rows, now in `data/demo/seed.sql` |
| `yadiggg_yocto_setup.sh` | `archive/historical-proposals/yadiggg_yocto_setup.sh` | Preserved but explicitly marked historical; hard-coded user path and destructive build-configuration writes make it unsafe to run |
| `scripts/connect_obsidian_vault.py` | Removed | Rewrote curated Markdown and added repetitive metadata |
| `scripts/deploy_yocto_layer.py` | `scripts/validate_yocto_layer.py` | Replaced by a read-only canonical-source consistency check; the checked-in layer is used directly |
| `docs/workspace-cleanup-audit.md` | Removed | Superseded by this migration map and the current readiness register; stale “after approval” cleanup notes no longer apply |
| `rendered_pages/*.png` | `archive/rendered-pages/` | Preserved page renders; not engineering deliverables |
| `media-output/*.png` | `assets/brand/reference/` | Preserved logo explorations; current logo image is still concept art |
| Unlabelled root `*.png` and `*.avif` references | `assets/reference/` | Preserved with original filenames and their documented historical context |
| `tue_jun_23_2026_documentation_drafts_for_project_migration.zip` | `archive/migration-inputs/` | Preserved intact; its distinct draft/spec files were inspected before moving |

The following derived or redundant files were removed:

- `A2c312300cbc241a593033cc604f7deb5N (1).png` was byte-identical to the retained `assets/reference/A2c312300cbc241a593033cc604f7deb5N.png`.
- The two `(1)` Advanced Specs page renders and `(1)` Sonic ID page render were byte-identical to their corresponding retained renders in `archive/rendered-pages/`.
- Every `extracted_text/*.txt` contained only `[No text found on this page]` page markers. The source PDFs remain preserved above.
- Tracked C object files, the compiled capture binary, the KiCad editor project-local file, and generated image-edit caches were removed. Rebuildable source and CAD files remain.

The ZIP contains a conversation export plus three separate draft documents (BOM, placement sketch, and camera-feasibility matrix); it was not treated as a duplicate of the active documentation. No historical part selection, estimate, geometry, or approval in archived material is an approved purchasing or manufacturing decision.
