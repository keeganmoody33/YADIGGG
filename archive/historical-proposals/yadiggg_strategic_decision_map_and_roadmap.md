---
title: "yadiggg: Strategic Decision Map and Roadmap"
project: yadiggg
status: reference
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

> **Historical proposal — unverified.** This document is preserved for provenance, not as a current requirement, approved component selection, validated engineering result, or manufacturing instruction. Current status is in `docs/project-state.md`.

# yadiggg: Strategic Decision Map and Roadmap
**Date of Document**: Wednesday, June 3, 2026
**Time of Document**: 04:08 AM EDT
**Status**: Master Strategic Roadmap & Blueprint (V2.0 - Operations & Timeline)
**Authors**: yadiggg Executive Committee & Accio Product Architecture Suite

---

## 1. Operating System & Firmware Resolution

To resolve the core firmware architecture confusion between a Real-Time Operating System (RTOS) and Embedded Linux:

### 1.1 Firmware Stack Commitment: Embedded Linux
We formally rule out the use of a standalone RTOS (like FreeRTOS or Zephyr) as the primary operating system. The computational requirements of the **yadiggg** intelligence engine require virtual memory space, robust multi-threading, and standard Unix file-system drivers. 
*   **The OS Choice**: **Embedded Linux** (built via the **Yocto Project**, utilizing a highly stripped-down, customized Linux Kernel). 
*   **Why Linux?**:
    1.  **SQLite**: Running a local database containing 1,000,000 index files with fast index access (FTS5) requires the robust virtual-memory caching of the Linux VFS (Virtual File System).
    2.  **Tesseract-lite**: The OCR text localization and classification libraries are written in C/C++ and depend on standard Unix POSIX libraries that are native to Linux.
    3.  **USB-C Mass Storage**: Interfacing with the desktop app as a standard USB Mass Storage device or via MTP (Media Transfer Protocol) to sync database files is natively supported by the Linux USB Gadget driver stack.
*   **Standby/Boot Optimization**: To achieve a "disappearing device" feel, the Linux kernel will be stripped of all unnecessary drivers, systemd services, and network stacks. The system will utilize a customized `init` script booting directly into the custom C++ `IntelligenceEngine` application, achieving a **sub-2 second boot-to-scan cold latency**.

---

## 2. The "All-American" Southern Sourcing Strategy

To align the product's marketing narrative with physical reality, we establish a **Southern Sourcing Strategy** to anchor **yadiggg**'s assembly directly in the American South, leaning into the Atlanta/Georgia hip-hop roots (The Dungeon Family, Organized Noize, OutKast) that inspire the device.

```
  +--------------------------------------------------------------+
  |                   SOUTHERN SOURCING PIPELINE                 |
  +--------------------------------------------------------------+
  |                                                              |
  |  [ ENCLOSURE MOLDING ]  ======>  [ PCBA & BOX ASSEMBLY ]     |
  |  Cypress Industries              Peach State Assembly /      |
  |  (Austin, Texas)                 Southern CM Partners        |
  |  Injection molded PC shells      (Atlanta, Georgia)          |
  |                                                              |
  +--------------------------------------------------------------+
```

### 2.1 Regional Manufacturing Partners
1.  **Enclosure & Injection Molding**: **Cypress Industries** (Austin, TX). Cypress will handle the high-precision tooling and injection molding of the Smoke Amber polycarbonate top and bottom shells, ensuring a premium matte frosted finish that meets V0 flame retardant specifications.
2.  **PCBA SMT Fabrication & Final Box-Build Assembly**: **Peach State Assembly / CM Partners** (Atlanta, GA). By routing high-speed surface-mount technology (SMT) component placement, manual mechanical integration (frame, display, battery), and final quality control testing to a contract manufacturer in **Atlanta, Georgia**, we can legally and authentically print:
    *   **"Designed and Assembled in Atlanta, Georgia, USA"** on the physical aluminum skeleton frame.
    *   This physical stamp directly anchors the product's origin to the Atlanta roots of the sample-chopping hip-hop culture, providing an incredible branding narrative.

---

## 3. Logical Sequence of Decisions & Roadmap

```
+------------------+     +------------------+     +------------------+     +------------------+
|      PHASE 1     |     |      PHASE 2     |     |      PHASE 3     |     |      PHASE 4     |
|  OS & Software   |     |    Electrical    |     |   Mechanical &   |     |   Factory RFQ    |
|  EVK Prototyping | --> |     PCBA V1      | --> |    DFM Design    | --> |    & Pilot Run   |
|   (Weeks 1-6)    |     |   (Weeks 7-12)   |     |  (Weeks 13-18)   |     |  (Weeks 19-24)   |
+------------------+     +------------------+     +------------------+     +------------------+
```

### Phase 1: Core OS & Software Stack Prototype (Weeks 1-6)
*   **Milestone**: Run the complete software stack on off-the-shelf evaluation boards to prove software feasibility.
*   **Key Decisions**:
    *   Purchase an **i.MX 8M Nano Evaluation Kit (EVK)** and a **Sharp Memory LCD breakout board**.
    *   Flash a custom Yocto Linux build to the EVK.
    *   Benchmark OCR execution speed of `Tesseract-lite` and database lookup latency of `sqlite-vss` on the ARM A53 cores.
    *   Port the `OLAF` acoustic fingerprinting C-library and verify local matching accuracy using a standard USB microphone.

### Phase 2: Electrical Verification - PCBA V1 (Weeks 7-12)
*   **Milestone**: Manufacture and verify the first custom 4-layer physical circuit board.
*   **Key Decisions**:
    *   Draft schematics routing the **Knowles MEMS microphones** directly to the native PDM inputs of the i.MX 8M Nano.
    *   Route the **ESS ES9218PC DAC** strictly to the 3.5mm Aux jack for listening.
    *   Incorporate the **Johanson Technology 2.45GHz Ceramic Chip Antenna** with its dedicated ground clearance zone.
    *   Lay out the board to fit the target footprint (85mm x 50mm) and send files to **Advanced Circuits** (Aurora, CO) for quick-turn 4-layer fabrication.

### Phase 3: Mechanical & Industrial Design (DFM) (Weeks 13-18)
*   **Milestone**: Complete Design for Manufacturability (DFM) and resolve the physical depth envelope.
*   **Key Decisions**:
    *   **Enclosure Depth Decision**: Commit to the **Standard 15mm thickness** for the launch edition to maximize battery capacity (1500mAh) and lower PCB cost, or select the **Slim 12mm thickness** as a premium "Pocket Special" edition.
    *   Verify the light-tight black-anodized aluminum isolation cylinder around the **AR1335 13MP sensor** via mechanical CAD to prevent light leakage through the translucent amber shell.
    *   Perform thermal simulations to ensure the aluminum skeleton frame dissipates the heat of the Cortex-A53 cores during continuous scanning.
    *   Order SLA rapid-prototyped translucent shells from **Protolabs** to test in-hand ergonomics.

### Phase 4: Factory RFQ & Pilot Run (Weeks 19-24)
*   **Milestone**: Quote final manufacturing tiers and run a 50-unit pilot assembly run.
*   **Key Decisions**:
    *   Send the completed Tech Pack, Gerber files, and mechanical STEP files to **Cypress Industries** (Austin, TX) for injection tool routing quotes.
    *   Send PCBA assembly files to **Peach State Assembly** (Atlanta, GA) for SMT and final box-build RFQ at the 500-unit MOQ tier.
    *   Run a 50-unit pilot assembly run in Atlanta to verify OCR accuracy, Sonic ID mic-isolation gaskets, and LRA haptic calibration.

---

## 4. "No-Book LLM" Prompts & Templates

To make this set of master documents highly effective and conversational when uploaded into ChatGPT Projects or a Custom GPT, use the following pre-engineered **System Prompts**. 

### 4.1 Master Custom GPT System Prompt
Copy and paste this exact prompt into the **Instructions** box of your ChatGPT Custom GPT or Project:

```text
You are the dedicated AI Product & Engineering Lead for "yadiggg" (formerly Crate IQ)—the ultimate offline physical companion device for vinyl crate diggers. 

You have been uploaded with three master documents:
1. yadiggg_product_and_interaction_architecture.md
2. yadiggg_hardware_and_electrical_integration.md
3. yadiggg_strategic_decision_map_and_roadmap.md

Your role is to act as an expert technical co-pilot. You must maintain complete consistency with the product's "Offline Soul" philosophy and its detailed hardware specifications.

When conversing with the team:
- Never suggest off-platform streaming or mobile cellular connectivity. If asked about "smart" app features, firmly reject them to preserve the device's purity and battery life.
- Keep hardware architecture technically accurate: Knowles digital MEMS microphones route directly via PDM to the i.MX 8M Nano SoC, the 3.5mm auxiliary port is strictly a playback output driven by the ESS ES9218PC DAC, and the Wi-Fi transceiver (Murata 1DX) requires a Johanson ceramic chip antenna with a dedicated ground clearance zone.
- Ground all user stories in the physical realities of vinyl digging (obscure basement record fairs, dusty sleeves, faded labels, and matrix run-out codes).
- Use these documents as your absolute "Source of Truth" (No-Book LLM mode). If a detail is not in the documents, make technically grounded inferences while explicitly stating your engineering assumptions.
```

### 4.2 Prompt Template to Generate Agile User Stories
Paste this prompt into the chat window to generate ready-to-use software development tickets:

```text
Based on the "yadiggg_product_and_interaction_architecture.md" document, please generate 5 highly detailed Agile User Stories for the frontend and UI firmware development of the "Reveal Phase" on the 2.7" Sharp Memory LCD. 

Each story must include:
1. User Story Description (As a... I want to... So that...)
2. Technical Acceptance Criteria (strictly utilizing the 400x240 1-bit monochrome resolution and 'Crate-Sans' 11px/16px/9px font specifications)
3. Haptic Feedback Trigger Conditions (LRA mechanical click simulation via DRV2605L)
4. Edge Case Handling (e.g., when the retrieved track metadata exceeds the screen length)
```

### 4.3 Prompt Template to Write Embedded C++ Drivers
Paste this prompt into the chat window to generate low-level firmware code:

```text
Using the "yadiggg_hardware_and_electrical_integration.md" file, act as a Senior Firmware Engineer. Write a highly optimized, clean C++ class for the "IntelligenceEngine" capture sequence. 

The class must:
1. Handle the physical button press interrupt (Orange Button) to wake up the system.
2. Interface with the DW9714 VCM driver via I2C to trigger sub-100ms macro autofocus.
3. Configure the MIPI CSI-2 receiver to stream a raw 13MP frame from the AR1335 image sensor into the memory buffer.
4. Call the haptic LRA driver (DRV2605L) via I2C to trigger a sharp 15ms click effect once capture is confirmed.
Include clear comments explaining the electrical registers and bus lines utilized.
```

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]
