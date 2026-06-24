# yadiggg: Master Domain Context & Architectural Glossary
**File**: `CONTEXT.md`
**Date**: Monday, June 8, 2026
**Status**: Committed & Active (Source of Truth)

This file defines the **domain model language**, core architectural boundaries, and committed system decisions for the **yadiggg** offline companion. It acts as our central context mapping dashboard to enforce consistent terms across all software, firmware, and hardware specifications.

---

## 1. Domain Vocabulary (The Glossary)

To maintain absolute alignment across teams, all design specifications and source code modules must strictly use these terms:

### 💿 Hardware & Electrical Domains
*   **The Pocket Companion**: The physical yadiggg device—an air-gapped, dedicated companion tool for vinyl crate digging, record store cataloging, and sample hunting.
*   **The Main SoC**: The **NXP i.MX 8M Nano** (Quad ARM Cortex-A53 running embedded Yocto Linux). Handles high-performance operations (SQLite searches, OLAF fingerprint extraction, Tesseract OCR scanner).
*   **The Co-Processor**: The **NXP LPC55S69** (Dual ARM Cortex-M33 running bare-metal firmware). Handles instant-on display pre-initialization, real-time power state triggers, and low-latency haptic drivers.
*   **The Memory Display**: The **Sharp LS027B7DH01** 2.7" ultra-low-power reflective memory LCD (400x240, SPI interface).
*   **The Sabre DAC**: The **ESS ES9218PC SABRE** 32-bit Quad headphone DAC and driver, strictly routed to the 3.5mm Aux jack.
*   **The PDM Mic Array**: Dual Knowles **SPH0641LM4H-1** digital MEMS PDM microphones, decimated to 16-bit PCM by the i.MX 8M's hardware decimator block.

### 💾 Software, Data, & DSP Domains
*   **Sonic ID**: The offline acoustic record identification subsystem.
*   **The OLAF DSP Engine**: Offline Lightweight Audio Fingerprinting C-library. Performs Hann windowing, 2048-point real-FFT, 32 logarithmic sub-band partitioning, and spatial/temporal multi-differential hashing.
*   **The Sliding Correlation Matcher**: The algorithm sliding 5-second query sub-fingerprints along pre-compiled SQLite reference fingerprint BLOBs using rapid bitwise **XNOR-popcount** checks.
*   **The Intelligence Graph**: The relational SQLite schema (`yadiggg_schema.sql`) mapping releases, tracks, contributors, and record credits, integrated directly with binary OLAF hashes.
*   **The Basement Scanner**: The optical character recognition (OCR) scanner pipeline using **Tesseract OCR** to resolve wrapped vinyl spine titles, barcodes, and catalog numbers in low-light store environments.

---

## 2. Core Architectural Decisions & Seams

These decisions are the current decision spine. Each material decision should be backed by an ADR in `docs/adr/` before being treated as locked.

1.  **Source of truth policy**: `CONTEXT.md`, `docs/adr/`, and linked active specs define the current project state. See [[docs/adr/0001-source-of-truth-and-archive-policy]].
2.  **Physical design is not yet locked**: current renderings are visual references, not industrial design truth. See [[docs/adr/0002-physical-design-direction-not-yet-locked]].
3.  **KiCad files are scaffolds**: current `.kicad_*` files open in KiCad but are not real schematic capture or fabrication outputs. See [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]].
4.  **Crate IQ files are archival inputs**: older PDFs/rendered pages are provenance/reference, not current specs. See [[docs/adr/0004-crate-iq-files-are-archival-inputs]].
5.  **Sonic ID code is a sandbox prototype**: it needs real audio fixtures, hardware ALSA validation, and reference fingerprint tests. See [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]].
6.  **Yocto layer is a build scaffold**: useful structure, not a verified image yet. See [[docs/adr/0006-yocto-layer-is-build-scaffold]].
7.  **BOM is conflicted**: component selections must be reconciled into a single current BOM before ordering. See [[docs/adr/0007-component-bom-is-conflicted-and-needs-reconciliation]].
8.  **Metadata must reflect status**: Graph links are not enough; status must distinguish authoritative/scaffold/prototype/reference/archive. See [[docs/adr/0008-obsidian-metadata-must-reflect-status]].
9.  **Provisional V1 physical assumptions**: attempt OCR/camera + Sonic ID in V1, target a 15mm-class voice-recorder-like prototype, support clear/smoke-clear and limited color variants, prioritize durable one-handed controls, keep the 3.5mm jack if fit allows, and defer on-device logo placement. See [[docs/adr/0011-provisional-v1-physical-direction-assumptions]].

---

## 🕸️ 3. Specification Connectivity Map (Vault Graph links)

*   **Dashboard**: [[yadiggg_vault_overview]]
*   **Project State**: [[docs/project-state]]
*   **Physical Direction**: [[physical-design/physical-direction-brief]]
*   **Aesthetics & Branding**: [[yadiggg_brand_identity_and_design_guidelines]]
*   **Product Flow**: [[yadiggg_product_and_interaction_architecture]]
*   **Hardware Architecture**: [[yadiggg_hardware_and_electrical_integration]]
*   **PCB Layout Guidelines**: [[hardware/yadiggg_pcba_v1_layout_guidelines]]
*   **BOM Sourcing**: [[docs/component-selections]]
*   **Schematic ERC**: [[docs/schematic-status]]
*   **Sonic ID / DSP Engine**: [[hardware/yadiggg_sonic_id_and_olaf_port]]
*   **Yocto Linux Builder**: [[hardware/yadiggg_yocto_recipe_and_image_build]]
*   **Database Schema**: `yadiggg_schema.sql` (Relational matching engine)
*   **Decision Records**: [[docs/adr/0001-source-of-truth-and-archive-policy]], [[docs/adr/0002-physical-design-direction-not-yet-locked]], [[docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready]], [[docs/adr/0004-crate-iq-files-are-archival-inputs]], [[docs/adr/0005-sonic-id-code-is-sandbox-prototype]], [[docs/adr/0006-yocto-layer-is-build-scaffold]], [[docs/adr/0007-component-bom-is-conflicted-and-needs-reconciliation]], [[docs/adr/0008-obsidian-metadata-must-reflect-status]], [[docs/adr/0009-generators-must-not-overwrite-hand-authored-work]], [[docs/adr/0010-context-and-adr-are-required-handoff-nodes]]
