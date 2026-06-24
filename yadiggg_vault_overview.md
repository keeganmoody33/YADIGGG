# 🌿 yadiggg: Master System Engineering & Industrial Design Vault
**Vault Location**: `/Users/keeganmoody/Downloads/YADIGGG/`
**Current Phase**: Workspace audit complete; source-of-truth repair in progress

Welcome to the **yadiggg master dashboard**. This file is optimized to act as your **Map of Content (MOC)** and Interactive Dashboard inside **Obsidian**. It now separates authoritative decisions from scaffolds, prototypes, archival references, and visual exploration files so Graph View reflects the project honestly.

---

## 🗺️ 1. Interactive Vault Navigation Map (MOC)

Select any of the connected system specifications below to load their technical parameters and layout rules:

### ✅ Start Here
*   **[Project State](docs/project-state.md)** — Single live status table for every deliverable, including source-of-truth, scaffold, prototype, reference, archive-candidate, and next-action status.
*   **[Workspace Cleanup Audit](docs/workspace-cleanup-audit.md)** — Current cleanup/architecture audit identifying what to keep, archive, correct, or treat as generated output.

### 🎨 Brand & Product Experience
*   **[Brand Guidelines](yadiggg_brand_identity_and_design_guidelines.md)** — Corelower-case geometric logo specs, vector mathematically derived soundwaves, physical colorways, and amber polycarbonate case aesthetics.
*   **[Interaction & Flow Design](yadiggg_product_and_interaction_architecture.md)** — Offline-first product design, raw vinyl search flows, and physical haptic dial control structures.

### 📐 Physical CAD & Hardware Layout
*   **[Physical Direction Brief](physical-design/physical-direction-brief.md)** — Active physical product direction brief for enclosure, controls, screen/camera/mic/jack/antenna placement, internal stack, CMF, and KiCad/mechanical constraints.
*   **[Electrical Integration Spec](yadiggg_hardware_and_electrical_integration.md)** — High-level SoC (i.MX 8M Nano) specifications, MEMS digital microphone array, ESS Sabre Quad-DAC analog circuits, and tactile LRAs.
*   **[4-Layer Layout & Routing Guidelines](hardware/yadiggg_pcba_v1_layout_guidelines.md)** — Stackup prepregs, 40R/80R high-speed memory traces, 50R RF microstrip coplanar waveguide, and split analog/digital ground plane zones (`GND_DIG` vs `GND_ANA`).
*   **[Component Selections (BOM)](docs/component-selections.md)** — Part number selections, active package dimensions (0402 passives for local SMT lines), and LCSC/Digikey identifiers.
*   **[Schematic and ERC Status Report](docs/schematic-status.md)** — 5-sheet hierarchical structure, design clearance rules, and ERC validation logs.

### 💿 Firmware & Embedded Linux OS
*   **[System & Update Architecture](yadiggg_firmware_and_update_architecture.md)** — Asymmetric dual-core boot speed optimizations (Cortex-M7 pre-init + Cortex-A53 Linux), and eMMC dual-boot (A/B) secure partition rollback scheme.
*   **[Acoustic Fingerprinting & OLAF Spec](hardware/yadiggg_sonic_id_and_olaf_port.md)** — Low-level PDM capture, ALSA configuration buffers, STFT 32-log band DSP, and Sliding Correlation lookups.
*   **[Yocto Layer & Image Builder Specs](hardware/yadiggg_yocto_recipe_and_image_build.md)** — Custom `meta-yadiggg` metadata overlay recipes, automatic startup scripts (`yadiggg-init`), and monolithic read-only kernel configurations.

### 💾 Data & QA Validation
*   **[Optimized Database Schema](yadiggg_schema.sql)** — Structured SQLite schema with optimized indexing on barcodes and catalog numbers, packed binary fingerprint BLOB tracking, and Roy Ayers seed data.
*   **[Adversarial Testing & Stress Protocol](yadiggg_adversarial_testing_and_validation_protocol.md)** — Red Team testing scenarios (database overload, basement scanner low-light fuzz, physical JTAG desoldering defenses, and passive thermals).

### 🧭 Decision Spine / Handoff Memory
*   **[ADR-0001: Source of Truth and Archive Policy](docs/adr/0001-source-of-truth-and-archive-policy.md)**
*   **[ADR-0002: Physical Design Direction Is Not Yet Locked](docs/adr/0002-physical-design-direction-not-yet-locked.md)**
*   **[ADR-0003: KiCad Files Are Scaffold, Not Fabrication-Ready](docs/adr/0003-kicad-files-are-scaffold-not-fabrication-ready.md)**
*   **[ADR-0004: Crate IQ Files Are Archival Inputs](docs/adr/0004-crate-iq-files-are-archival-inputs.md)**
*   **[ADR-0005: Sonic ID Code Is a Sandbox Prototype](docs/adr/0005-sonic-id-code-is-sandbox-prototype.md)**
*   **[ADR-0006: Yocto Layer Is a Build Scaffold](docs/adr/0006-yocto-layer-is-build-scaffold.md)**
*   **[ADR-0007: Component BOM Is Conflicted and Needs Reconciliation](docs/adr/0007-component-bom-is-conflicted-and-needs-reconciliation.md)**
*   **[ADR-0008: Obsidian Metadata Must Reflect Status](docs/adr/0008-obsidian-metadata-must-reflect-status.md)**
*   **[ADR-0009: Generators Must Not Overwrite Hand-Authored Work](docs/adr/0009-generators-must-not-overwrite-hand-authored-work.md)**
*   **[ADR-0010: CONTEXT and ADR Are Required Handoff Nodes](docs/adr/0010-context-and-adr-are-required-handoff-nodes.md)**
*   **[ADR-0011: Provisional V1 Physical Direction Assumptions](docs/adr/0011-provisional-v1-physical-direction-assumptions.md)**

---

## 🚀 2. Active Development Files on Disk

Your physical workspace includes active code, CAD projects, and BSP overlay metadata. You can navigate them inside your system terminal or file browser:

*   **`hardware/yadiggg.kicad_pro`** — KiCad project shell; scaffold status, not fabrication-ready.
*   **`hardware/yadiggg.kicad_sch`** — KiCad hierarchical schematic shell; scaffold status, not real schematic capture yet.
*   **`hardware/yadiggg.kicad_pcb`** — Board outline scaffold with comments; no routed PCBA yet.
*   **`src/sonic_id/olaf.c` / `olaf.h`** — Sonic ID sandbox prototype; compiles locally but not hardware-validated.
*   **`src/sonic_id/yadiggg_capture.c`** — Capture/matching prototype with macOS mock path and Linux ALSA path.
*   **`src/sonic_id/Makefile`** — Prototype build file.
*   **`src/sonic_id/asound.conf`** — Target ALSA configuration draft.
*   **`yocto-meta/meta-yadiggg/`** — Yocto build scaffold; not verified by a completed BitBake image yet.
*   **`yadiggg.db`** — Local SQLite test database generated from schema; should be regenerated from `yadiggg_schema.sql` when needed.

---

## 🧠 3. Pro Obsidian Tips for this Vault
1.  **Toggle the Local Graph View**: Select `Open local graph` on any markdown file. You will see visual spiderwebs linking your physical hardware layouts back to your database schemas, firmware states, and adversarial tests!
2.  **Open Code Blobs**: Since Obsidian supports full code-syntax highlighting, you can open and edit our C-source files, SQL schemas, and shell scripts right inside the note editor.
3.  **Cross-linking**: When taking notes inside Obsidian during prototyping, you can link back to any engineering spec dynamically by simply typing `[[yadiggg_brand_identity_and_design_guidelines]]` or `[[yadiggg_hardware_and_electrical_integration]]`.
