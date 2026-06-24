---
title: "yadiggg: 4-Layer PCBA V1 Physical Layout & Routing Guidelines"
project: yadiggg
status: completed
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

# yadiggg: 4-Layer PCBA V1 Physical Layout & Routing Guidelines
**Date of Document**: Friday, June 5, 2026
**Status**: Official Layout Specification (V1.0)
**Board Dimensions**: 100mm x 55mm (4.0" x 2.16"), 1.2mm board thickness, 4-Layer FR4

This document defines the physical PCB layout routing rules, copper stackup, high-speed differential geometries, analog isolation zones, and antenna trace matching for the **yadiggg V1 PCBA**. It translates our Task 8 electrical schematics into a physically robust, electromagnetic-compatible (EMC) hardware design.

---

## 1. 4-Layer Copper Stackup Spec

To maintain signal integrity on high-speed memory and RF traces while isolating sensitive audio components, we employ a defined 4-layer FR4 stackup:

```
        Layer 1 [TOP]:   Signal (LPDDR4, RF, Components)   <-- 0.5 oz (18µm + Plating)
        ================ Prepreg: 0.1mm (Dielectric 4.2)
        Layer 2 [INT1]:  Solid Ground Plane (GND_DIG / GND_ANA) <-- 1.0 oz (35µm)
        ================ Core: 0.8mm (Dielectric 4.5)
        Layer 3 [INT2]:  Power Planes (Split Power Grid)   <-- 1.0 oz (35µm)
        ================ Prepreg: 0.1mm (Dielectric 4.2)
        Layer 4 [BOT]:   Signal (Audio Analog, Low-Speed)  <-- 0.5 oz (18µm + Plating)
```

### Critical Stackup Decisions:
1.  **Ultra-Thin Top Dielectric**: The 0.1mm Prepreg thickness between Layer 1 and Layer 2 allows for narrow, impedance-controlled trace widths (e.g., **0.12mm** width for a 50-ohm single-ended coplanar waveguide), maximizing density in our tiny 100mm x 55mm board area.
2.  **Continuous Reference Planes**: High-speed digital traces on Layer 1 refer directly to the solid ground plane on Layer 2, minimizing the return loop area and preventing electromagnetic radiation.

---

## 2. High-Speed LPDDR4 Memory Routing (Layer 1)

The LPDDR4 memory bus runs at **1600MHz (3200 MT/s)**. It is the most critical digital routing block on the board and is placed directly adjacent to the i.MX 8M Nano SoC to minimize trace lengths.

```
       [i.MX 8M BGA-486]                         [Micron LPDDR4 WLCSP]
     +-------------------+                      +---------------------+
     |                   |  ==== Data Lane0 === |                     |
     |  DDR_DQ0 - DQ7    |  ---- Match <1mm --- |  DQ0 - DQ7          |
     |                   |                      |                     |
     |  DDR_CK_P / CK_N  |  == Diff Pair (80R)  |  CK_P / CK_N        |
     |                   |  ---- Match <0.5mm - |                     |
     |                   |                      |                     |
     |  DDR_CA0 - CA5    |  === Control Bus === |  CA0 - CA5          |
     |                   |  ---- Match <2mm --- |                     |
     +-------------------+                      +---------------------+
     ==================================================================
                             LAYER 2 [GND_DIG PLANE]
```

### Routing Rules:
*   **Trace Impedance**:
    *   Single-Ended (Data, Address, Control): **40 ohms** (Trace width: **0.15mm**).
    *   Differential Pairs (`DDR_CK_P`/`N`, `DDR_DQS0_P`/`N` to `DQS3_P`/`N`): **80 ohms** (Trace width: **0.12mm**, Air-Gap: **0.15mm**).
*   **Length Matching & Skew Control**:
    *   **Data Lanes (Byte-level)**: Match the length of all data bits (`DQ0`-`DQ7`) within each byte lane to their respective strobe pair (`DQS0_P`/`N`) to within **5ps (approx. 0.75mm)**.
    *   **Address/Control Bus**: Match all command/address traces (`CA0`-`CA5`) to the main clock differential pair (`CK_P`/`N`) to within **10ps (approx. 1.5mm)**.
*   **No Reference Plane Split Crossing**: Under no circumstances should any LPDDR4 trace cross a split in the Layer 2 ground plane. Any impedance discontinuity will cause signal reflections, resulting in memory write-errors (Test FW-04).

---

## 3. High-Fidelity Audio Analog Isolation Layout (Layers 1, 2, & 4)

To prevent audio popping and background hum, the physical layout separates the sensitive analog audio circuitry from high-speed digital switching noise.

```
             DIGITAL REGION                        ANALOG ISOLATION REGION
     +-----------------------------+        |        +---------------------+
     |                             |        |        |                     |
     |      i.MX 8M Nano SoC       |        |        |  ESS ES9218PC DAC   |
     |     (GND_DIG Return)        |        |        |  (GND_ANA Return)   |
     |                             |  1.0mm |        |                     |
     +-----------------------------+  Split |        +---------------------+
     ==============================|========|==============================
          LAYER 2 GND_DIG          | Barrier|           LAYER 2 GND_ANA
     ==============================|========|==============================
                                   |        |
                                 [NT1] Net-Tie (Single-Point Bridge near PMIC)
```

### Layout Strategy:
1.  **The 1.0mm Isolation Barrier**: A strict **1.0mm wide split** is carved into Layer 2 (Ground) and Layer 3 (Power), separating the digital ground (`GND_DIG`) from the analog ground (`GND_ANA`).
2.  **No Split-Crossing Traces**: No digital signal lines (including I2C lines to control the DAC or the digital PDM microphone clock) are permitted to cross the 1.0mm analog barrier on any layer, except at the physical bridge.
3.  **Single-Point Ground Bridge**: The split is bridged at a single point using a small surface-mount **Net-Tie** (`NT1`) placed physically adjacent to the PMIC (`BD71850MWV`) main ground landing pad. This prevents circulating digital ground loops from injecting noise into the DAC's charge pump.
4.  **DAC and Jack Placement**: The ES9218PC DAC (`U6`), passive RC low-pass filters, LP5907 regulator (`U7`), and the 3.5mm Aux jack (`HP1`) are clustered tightly together on the bottom-right corner of the board, isolated from high-speed memory switching lines.

---

## 4. 2.45GHz RF Antenna Co-planar Waveguide (Layer 1)

The wireless module (Murata Type 1DX) operates at 2.4GHz. The trace connecting the module's RF pin to the Johanson Ceramic Chip Antenna must be routed as a low-loss, matched transmission line.

```
       Layer 1:  [GND]----(0.12mm Gap)----[ RF TRACE: 0.15mm ]----(0.12mm Gap)----[GND]
                 =====================================================================
       Layer 2:  ====================== SOLID GND_DIG PLANE ==========================
```

### Layout Specifications:
1.  **Coplanar Waveguide with Ground (CPWG)**: Route the RF trace on Layer 1. The trace width must be **0.15mm**, bounded by a **0.12mm air-gap** to Layer 1 ground fill, and referencing a continuous, solid `GND_DIG` plane on Layer 2. This structure achieves a precise **50-ohm characteristic impedance** at 2.45GHz.
2.  **Antenna Copper-Free Clearance Zone**:
    *   Underneath and around the ceramic chip antenna (`ANT1`), there must be a **5.0mm x 4.0mm clearance zone** completely free of copper on all 4 layers.
    *   No power traces, ground fills, or signal vias are permitted inside this zone, preventing antenna detuning and degradation of wireless range during updating cycles.
3.  **Stitching Vias**: Place a dense row of ground stitching vias (spaced every **1.0mm**) along the Layer 1 ground shields bordering the RF trace. This forms a virtual metal shielding cage, confining the high-frequency 2.4GHz RF signals within the waveguide channel.

---

## 5. Physical Microphone Isolation Grommets

*   **Vibration Abatement (Test MECH-05)**: Since the device features an integrated heavy-duty 10mm LRA haptic actuator, physical motor vibrations could travel through the FR4 fiberglass board and slam into the Knowles MEMS microphones, creating severe acoustic clipping.
*   **The Slot Cut Solution**: In the layout, the dual SPH0641 microphones are positioned on **isolated finger-tabs** of the PCB, separated from the main board body by a **0.8mm routed slot**.
*   **Mechanical Isolation**: Custom-molded, soft silicone rubber grommets (40 Durometer Shore A) wrap around these finger-tabs, suspending the micro-sensors in space and blocking physical board-level shear waves from traveling into the acoustic ports.

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]

*   **Sister Spec**: [[yadiggg_hardware_and_electrical_integration]]
*   **Sister Spec**: [[docs/component-selections]]
*   **Sister Spec**: [[docs/schematic-status]]
*   **Sister Spec**: [[yadiggg_pinmux]]
*   **Sister Spec**: [[yadiggg_audio_dac_and_mic_schematics]]