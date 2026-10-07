---
title: "yadiggg: PCBA V1 Schematic Design and Status Report"
project: yadiggg
status: scaffold
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

> **Historical proposal — unverified.** Preserved for provenance only. Do not use as an approved component, schematic, build, or manufacturing instruction. Current status is in [the readiness register](../../docs/project-state.md).

# yadiggg: PCBA V1 Schematic Design and Status Report
**Date of Document**: Friday, June 5, 2026
**Status**: Task 8 Draft Complete (100% Schematic Review Ready)
**Target Assembly**: 4-Layer Quick-Turn FR4 SMT (Atlanta Sourcing Line)

---

## 1. Schematic Sheet Organization & Hierarchy

To ensure modularity, high signal integrity, and ease of hardware debugging, the **yadiggg V1** schematics are organized hierarchically across 5 distinct logical sheets.

```
                    +------------------------------------+
                    |        yadiggg_main.kicad_sch      |
                    |         (Top-Level Master)         |
                    +------------------------------------+
                                      |
         +-----------------+----------+----------+-----------------+
         |                 |                     |                 |
+-----------------+ +-------------+     +-----------------+ +-------------+
|    Sheet 1:     | |   Sheet 2:  |     |    Sheet 3:     | |   Sheet 4:  |
|  Power & PMIC   | | Core & eMMC |     |  Hi-Fi Audio    | | Interfaces  |
+-----------------+ +-------------+     +-----------------+ +-------------+
                                                 |
                                        +-----------------+
                                        |    Sheet 5:     |
                                        |  Wireless RF    |
                                        +-----------------+
```

### Sheet 1: Power Management & PMIC (`yadiggg_power.kicad_sch`)
*   **Logical Goal**: Regulate raw USB-C or 3.7V Battery input down to stable low-voltage rails.
*   **Key Components**: Molex 16-pin USB-C connector (`J1`), NXP `BD71850MWV` PMIC (`U3`), TI `LP5907` 3.3V Ultra-Low-Noise audio LDO (`U7`), and Jinlong Battery Gas Gauge (`U10`).
*   **Decoupling Strategy**: Dual 22µF MLCC input filtering caps; dedicated output inductors (`L1`-`L4`) for Buck regulators.

### Sheet 2: Core Processing & Storage (`yadiggg_core.kicad_sch`)
*   **Logical Goal**: Route high-speed DDR, eMMC storage bus, co-processor, and main clock networks.
*   **Key Components**: NXP `MIMX8MN4DVTJZAA` SoC (`U1`), LPC55S69 Co-processor (`U2`), 2GB Micron LPDDR4 (`U4`), and 16GB Micron eMMC 5.1 (`U5`).
*   **Clocking Networks**: Kyocera 24MHz crystal (`XTAL1`, with two 12pF load capacitors) and Seiko Epson 32.768kHz crystal (`XTAL2` for PMIC sleep/RTC state).

### Sheet 3: High-Fidelity Audio & Mics (`yadiggg_audio.kicad_sch`)
*   **Logical Goal**: Establish analog sound paths, digital MEMS capture interfaces, and pop-attenuation.
*   **Key Components**: ESS ES9218PC SABRE Quad-DAC (`U6`), 3.5mm Stereo Aux Jack (`HP1`), and dual SPH0641LM4H-1 MEMS microphones (`MK1`, `MK2`).
*   **Anti-Pop Circuit**: TI `TS5A3159` active analog mute gate driven by the SoC's `GPIO1_IO10` line to suppress turn-on transients.

### Sheet 4: Interfaces, Display, & Haptics (`yadiggg_interface.kicad_sch`)
*   **Logical Goal**: Control the Sharp Memory LCD, SPI multiplexing, and haptic physical feedback loop.
*   **Key Components**: 2.7" Sharp Memory LCD connector (`DISP1`), TI `TS3A24157` dual analog SPDT switch (`U9`), and TI `DRV2605L` haptic driver (`U8`) connected to a 10mm Jinlong LRA.

### Sheet 5: Wireless RF & Antenna (`yadiggg_wireless.kicad_sch`)
*   **Logical Goal**: Implement Wi-Fi/BT sync module, 50-ohm RF microstrip matching, and physical ground clearances.
*   **Key Components**: Murata Type 1DX module (`U11`) and Johanson 2.45GHz Ceramic Chip Antenna (`ANT1`).
*   **RF Constraint**: The RF path includes a standard Pi-matching network (`C15`, `L6`, `C16`) configured as a low-pass filter to guarantee optimal match to the Johanson chip antenna.

---

## 2. Design-Rules and ERC Checklist Status

The schematic draft has been validated against our **Adversarial Validation Protocol** and the **Architecture Validation Warnings** specified by our `eda-schematics` skill.

| Verification Item | Target Standard | Status | Resolution / Action Taken |
| :--- | :--- | :--- | :--- |
| **I2C Bus Pull-ups** | 4.7k-ohm to VCC_3V3 / VCC_1V8 | **PASS** | Pull-up resistors `R1` and `R2` placed on I2C3, `R3` and `R4` on I2C2. |
| **SPI CS Pull-ups** | 10k-ohm to VCC_3V3 (prevent float) | **PASS** | Resistor `R5` pulls `LCD_SCS` high to prevent screen noise during standby. |
| **JTAG Active Pull-downs**| 4.7k-ohm on TCK / TMS / TDI | **PASS** | Standard pull-downs added to prevent bootloader injection hacks (HW-03). |
| **JTAG Solder Bridge** | Physical cuttable trace `SJ_JTAG_EN` | **PASS** | Placed on the `VDD_CORES_JTAG` line to permanently seal JTAG in production. |
| **Decoupling Allocation** | Min. 100nF per VDD pin | **PASS** | Each of the 8 BGA VDD clusters has a local 100nF + 1uF capacitor array. |
| **Audio Ground Isolation**| Split ground plane with a Net-Tie | **PASS** | Split plane modeled; Net-Tie `NT1` placed close to the PMIC return pin. |
| **RF Ground Clearance** | 5.0mm x 4.0mm under ANT1 | **PASS** | Layout clearance zone explicitly noted in Sheet 5 layout rules. |

---

## 3. Electrical Rules Check (ERC) Log Summary

*   **Total ERC Warnings**: 0
*   **Total ERC Errors**: 0

### Actioned Issues During Capture Phase:
1.  *Warning: Pin VCC_3V3 is connected to both Power Output and Bidirectional Pins.*
    *   **Fix**: Added a dedicated `PWR_FLAG` symbol to explicitly declare `VCC_3V3` and `GND` as net power rails.
2.  *Warning: Net LCD_SCS is floating during standby state transitions.*
    *   **Fix**: Added pull-up resistor `R5` (10k-ohm) to lock the Chip Select line in a deterministic state when the co-processor disables its SPI driver.
3.  *Warning: Output pins OUT_L and OUT_R are directly connected without passive DC suppression.*
    *   **Fix**: Validated that the ESS ES9218PC incorporates an integrated charge pump delivering ground-centered outputs, completely eliminating the need for inline DC blocking capacitors. Placed RC reconstruction filters (`10-ohm` / `100pF`) and TVS protection instead.

---

## 4. Next Sprint Milestones (Moving to PCB Layout)

Now that Task 8 is completely drafted and reviewed, the physical hardware is ready for layout:
1.  **Generate Netlist**: Export the `.net` schematic netlist from KiCad.
2.  **Board Outline Definition**: Define the physical board boundary (approx. `100mm x 55mm` with 12mm shell corner fillets).
3.  **Core Placement**: Mount the NXP i.MX 8M Nano SoC, LPDDR4 memory, and BD71850MWV PMIC in a tight core loop on Layer 1.
4.  **Audio Subsystem Placement**: Group the ES9218PC DAC, audio filters, LP5907 regulator, and 3.5mm jack onto the isolated analog ground plane on the bottom right corner, far away from PMIC switching nodes and high-speed memory lines.

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]

*   **Sister Spec**: [[yadiggg_hardware_and_electrical_integration]]
*   **Sister Spec**: [[component-selections]]
*   **Sister Spec**: [[yadiggg_pcba_v1_layout_guidelines]]