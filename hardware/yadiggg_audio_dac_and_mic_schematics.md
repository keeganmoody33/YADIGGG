---
title: "yadiggg: Premium Audio Subsystem & Digital Microphone Array Schematics"
project: yadiggg
status: active-draft
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

# yadiggg: Premium Audio Subsystem & Digital Microphone Array Schematics
**Date of Document**: Friday, June 5, 2026
**Status**: Release V1.0 (Production Engineering Spec)
**Scope**: Hi-Fi Analog Output Routing, Knowles MEMS PDM Array, and Electromagnetic Isolation

This specification defines the low-level schematic wiring, passive component selections, filtering networks, and board layout rules for the **yadiggg V1 audio subsystem**. It is designed to satisfy our ultra-strict acoustic fingerprinting capture requirements while maintaining high-fidelity, studio-grade headphone playback isolated from processor and power-rail noise.

---

## 1. ESS ES9218PC SABRE Hi-Res DAC Circuit

The **ES9218PC** is a highly integrated 32-bit Stereo Quad-DAC with a high-performance headphone amplifier. It operates with a ground-referenced charge pump, allowing direct DC-coupled connection to the 3.5mm Aux jack without bulky and distorting AC-coupling capacitors.

### 1.1 Schematic Connection Diagram (ASCII representation)

```
                       +-----------------------------------+
                       |        ESS ES9218PC SABRE DAC     |
                       +-----------------------------------+
                       |                                   |
    [I2S/SAI3 Bus]     |                                   |  [Analog Outputs]
    DAC_MCLK --------> | 14 MCLK                   OUT_L 3 | ----------+-------------> HP_OUT_L
    DAC_BCLK --------> | 15 BCLK                           |           | (Ferrite + TVS)
    DAC_LRCK --------> | 16 LRCK                   OUT_R 4 | ------+---+-------------> HP_OUT_R
    DAC_SDATA -------> | 17 SDIN                           |       |   |
                       |                                   |       v   v
    [I2C Control]      |                                   |     [FB1] [FB2] (BLM15AG121)
    DAC_SCL --------<> | 18 SCL                     VCCA 5 | <---+---+-- [C1] [C2] (10uF/0.1uF)
    DAC_SDA --------<> | 19 SDA                            |         | (Clean V_ANA_DAC)
                       |                                   |         v
    [System Pins]      |                                   |        GND_ANA
    DAC_RESET -------> | 20 nRESET                 GNDA 32 | <=======(Analog Ground Plane)
                       |                                   |
                       +-----------------------------------+
```

### 1.2 Passive Filter & Power Decoupling Specifications
1.  **Ultra-Low-Noise LDO**: The analog supply pin (`VCCA`, 3.3V) is driven by a dedicated, high-PSR **TI LP5907MFX-3.3** LDO. It is strictly isolated from the digital `VCC_3V3` plane.
2.  **Analog Power Isolation Network**:
    *   A high-impedance ferrite bead **Murata BLM15AG121SN1D** (`FB1`, 120 ohms @ 100MHz) is placed in series between the LDO output and the `VCCA` pin.
    *   Direct decoupling is achieved via a **10µF X5R ceramic capacitor** (`C1`, Murata GRM155R60J106ME15D) in parallel with a **100nF high-frequency ceramic bypass capacitor** (`C2`, Murata GRM155R71H104KE14D). These must be placed within **2.0mm** of pin 5 on the physical layout.
3.  **Output Path Filtering and ESD Protection**:
    *   To block high-frequency delta-sigma modulator noise, place a passive RC reconstruction filter on `OUT_L` and `OUT_R` using a **10-ohm 1% resistor** in series and a **100pF COG/NPO capacitor** to `GND_ANA`.
    *   To safeguard against static discharge (ESD) from standard headphones, integrate **Semtech µClamp0511Z** bidirectional TVS protection diodes directly on the headphone line trace immediately adjacent to the physical 3.5mm Aux jack pin pad.

---

## 2. Dual Knowles Digital MEMS Microphone Array

The acoustic capture system uses two **Knowles SPH0641LM4H-1** high-SNR digital PDM (Pulse Density Modulation) microphones. They are connected in a stereo configuration over a shared clock line, utilizing the native PDM hardware decimation filters on the i.MX 8M Nano SoC.

### 2.1 Stereo PDM Connection Schematic

```
      VCC_1V8
         |
      +--+------------------------+---------------------------------------+
      |  |                        |  |                                    |
     [C3] [C4] (1uF/0.1uF)       [C5] [C6] (1uF/0.1uF)                    |
      |  |                        |  |                                    |
    +----+-----------+          +----+-----------+                        |
    |  SPH0641LM4H-1 |          |  SPH0641LM4H-1 |                        |
    |  LEFT MIC (MK1)|          | RIGHT MIC (MK2)|                        |
    |                |          |                |                        |
    | 5 VDD          |          | 5 VDD          |                        |
    | 4 CLK  <-------+----------+ 4 CLK          | <======================+-- PDM_CLK (SAI5_RXC)
    | 1 DATA --------+----------+ 1 DATA         | <======================+-- PDM_DATA (SAI5_RXD0)
    | 2 SELECT       |          | 2 SELECT       |                        |
    | 3 GND          |          | 3 GND          |                        |
    +----+-----------+          +----+-----------+                        |
         |                           |                                    |
        ===                         ===                                   |
        GND                       VCC_1V8                                 v
   (SELECT tied to             (SELECT tied to                        (SoC Decimate
    GND: Left channel,          VDD: Right channel,                    Digital Inputs)
    Data on Fall Edge)          Data on Rise Edge)
```

### 2.2 Functional Configuration & Phase Alignment
1.  **Left Channel (MK1)**: The `SELECT` pin (pin 2) is hardwired directly to the digital ground plane (`GND`). This forces the microphone to drive the shared data line on the **falling edge** of the `PDM_CLK` signal.
2.  **Right Channel (MK2)**: The `SELECT` pin (pin 2) is tied directly to the `VCC_1V8` rail. This forces the microphone to drive the shared data line on the **rising edge** of the `PDM_CLK` signal.
3.  **Single-Trace Bus Consolidation**: This multiplexing scheme allows `MK1` and `MK2` to share a single, consolidated physical trace (`PDM_DATA`) routed directly to the `SAI5_RXD0` pin of the SoC, ensuring perfect stereo phase alignment for our dual-mic acoustic fingerprinting triangulation.
4.  **Local Decoupling**: Each microphone must have its own dedicated high-frequency **1uF** and **100nF** decoupling capacitors connected between VDD (pin 5) and GND (pin 3) directly underneath the LGA-5 package footprint.

---

## 3. Adversarial Quality Isolation & Thermal Rules (Test HW-03 & MECH-05)

To pass our aggressive **Adversarial Validation Protocol** (specifically testing eMMC security under thermal stress, SEC-JTAG disablement, and audio-path pop protection), the PCB schematic and layout must enforce the following strict physical boundaries:

### 3.1 Partitioned Ground Plane Layout (Zero-Interference Audio)
*   **The Mismatch**: Digital CPU switching loops create return-current ground noise that, if shared with the analog circuits, creates an audible background buzz or high-frequency digital squeal ("audio popping").
*   **The Solution**: The PCB layout features two separate ground planes: `GND_DIG` (for CPU, memory, and flash return currents) and `GND_ANA` (exclusively for the ESS Quad-DAC, LP5907 regulator, and 3.5mm Aux jack).
*   **The Single-Point Bridge**: The two ground planes are physically isolated across a 1.0mm wide split, connected together at a **single point** using a copper **Net-Tie** (or a **0-ohm SMD-0603 jumper resistor**) placed directly adjacent to the PMIC’s ground landing pad. This eliminates ground loop currents from injecting noise into the headphone amplifier.

### 3.2 Post-Programming Secure JTAG Disable (Atlanta Heist Mitigation)
*   **The Threat (Test HW-03)**: Attackers desolder the eMMC or solder onto the exposed JTAG test pads on the PCB to extract the proprietary SQLite database keys from the processor's SRAM during boot.
*   **The Solution**: Place a physical, active pull-down resistor (**4.7k-ohm 0402**) on the SoC JTAG pins (`JTAG_TCK`, `JTAG_TMS`, `JTAG_TDI`, `JTAG_TDO`).
*   **The Electronic Fuse Gate**: We route the main CPU JTAG power supply rail (`VDD_CORES_JTAG`) through a small physical SMD **Solder Bridge jumper** (labeled `SJ_JTAG_EN`). During factory QA and initial flashing, this solder bridge is closed. Once QA is complete and the bootloader keys are burned, the solder bridge is **physically blown open** or desoldered, permanently disabling physical JTAG debugging access in the field.

### 3.3 Active-Mute Anti-Popping Circuit
*   **The Threat (Test FW-04)**: During rapid sleep/wake standby power transitions, sudden voltage fluctuations in the DAC charge-pump stage create massive transient spikes (audible clicks or "pops") in the user's headphones, risking acoustic discomfort.
*   **The Solution**: Integrate an active analog mute switch (**TI TS5A3159** analog switch or an **N-channel depletion-mode MOSFET** like the `BSS123`) directly bridging `OUT_L` and `OUT_R` to ground. The gate of this mute circuit is driven by `GPIO1_IO10` (named `DAC_MUTE_CTRL`).
*   **The Firmware Handshake**: The boot firmware holds `DAC_MUTE_CTRL` active (high) during startup and power-down cycles, shorting the audio outputs to ground and absorbing the voltage spikes. The mute is only released (driven low) after the Sabre DAC registers have stabilized, ensuring a completely silent and premium user experience.

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]

*   **Sister Spec**: [[yadiggg_hardware_and_electrical_integration]]
*   **Sister Spec**: [[yadiggg_pinmux]]
*   **Sister Spec**: [[yadiggg_pcba_v1_layout_guidelines]]