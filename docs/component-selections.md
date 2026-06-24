---
title: "yadiggg: Component Selections and Sourcing Map"
project: yadiggg
status: completed
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

# yadiggg: Component Selections and Sourcing Map
**Date of Document**: Wednesday, June 3, 2026
**Status**: Official Part Sourcing & LCSC BOM Register (V1.0)

This document maps out the elite commercial component selections for the **yadiggg PCBA V1**, including specific manufacturers, part numbers, package layouts, and LCSC/Digikey identifiers to align with our local Atlanta quick-turn manufacturing targets.

---

## 1. Core Processor & Power Management

| RefDes | Component Description | Manufacturer | Part Number | Package | Sourcing ID (LCSC/Digikey) | Est. Unit Cost (1k) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **U1** | NXP i.MX 8M Nano Quad-core ARM | NXP | `MIMX8MN4DVTJZAA` | BGA-486 | `MIMX8MN4DVTJZAA-ND` | \$14.50 |
| **U2** | ARM Cortex-M7 Real-Time MCU | NXP | `MIMXRT1015DAF5B` | LQFP-100 | `C394541` (LCSC) | \$4.20 |
| **U3** | System Power Management IC (PMIC)| NXP | `BD71850MWV` | QFN-56 | `C513410` (LCSC) | \$3.15 |
| **U4** | 2GB LPDDR4 Memory Chip | Micron | `MT53E512M32D1ZW` | WLCSP | `MT53E512M32D1ZW-ND` | \$6.50 |
| **U5** | 16GB eMMC 5.1 Flash Storage | Micron | `MTFC16GAPALBH-IT` | FBGA-153 | `MTFC16GAPALBH-IT-ND`| \$5.00 |

---

## 2. High-Fidelity Analog & Sensor Interfaces

| RefDes | Component Description | Manufacturer | Part Number | Package | Sourcing ID (LCSC/Digikey) | Est. Unit Cost (1k) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **U6** | SABRE 32-bit Quad Headphone DAC | ESS Technology | `ES9218PC` | QFN-40 | `ES9218PC` (Direct ESS) | \$3.80 |
| **U7** | Ultra-Low-Noise LDO Regulator | TI | `LP5907MFX-3.3` | SOT-23-5 | `C112253` (LCSC) | \$0.18 |
| **MK1** | Digital MEMS Microphone (Left) | Knowles | `SPH0641LM4H-1` | LGA-5 | `SPH0641LM4H-1-ND` | \$1.05 |
| **MK2** | Digital MEMS Microphone (Right) | Knowles | `SPH0641LM4H-1` | LGA-5 | `SPH0641LM4H-1-ND` | \$1.05 |
| **U8** | LRA Haptic Driver Controller | TI | `DRV2605LDGSR` | VSSOP-10 | `C114512` (LCSC) | \$0.85 |

---

## 3. Display, Wireless, & Passives

| RefDes | Component Description | Manufacturer | Part Number | Package | Sourcing ID (LCSC/Digikey) | Est. Unit Cost (1k) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DISP1**| 2.7" Sharp Memory LCD Screen | Sharp | `LS027B7DH01` | FPC Connector | `LS027B7DH01-ND` | \$8.50 |
| **ANT1** | 2.45GHz Ceramic Chip Antenna | Johanson | `2450AT18A100E` | SMD-1206 | `712-1007-1-ND` | \$0.22 |
| **XTAL1**| 24MHz High-Precision Crystal | Kyocera | `CX3225SB24000D0` | SMD-3225 | `C115456` (LCSC) | \$0.12 |
| **XTAL2**| 32.768kHz RTC Crystal | Seiko Epson | `FC-135 32.7680KA` | SMD-3215 | `C32312` (LCSC) | \$0.08 |

---

## 4. Key Sourcing & Layout Constraints
1.  **Passive Sizing**: All resistors, capacitors, and inductors must strictly use **0402 package sizing** or larger to enable reliable, high-yield pick-and-place operation on local Atlanta short-run SMT lines.
2.  **Impedance-Controlled Lines**: High-speed memory traces between U1 (i.MX 8M) and U4 (LPDDR4) require **40-ohm single / 80-ohm differential** trace geometries.
3.  **Analog Decoupling**: The ESS Quad-DAC (`ES9218PC`) analog voltage rail (`V_ANA_DAC`) must be isolated with dedicated **decoupling ferrite beads (Murata BLM15AG121SN1D)** and low-ESR ceramic caps to block any processor-induced high-frequency power grid noise.

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]

*   **Sister Spec**: [[yadiggg_hardware_and_electrical_integration]]
*   **Sister Spec**: [[schematic-status]]
*   **Sister Spec**: [[yadiggg_pcba_v1_layout_guidelines]]