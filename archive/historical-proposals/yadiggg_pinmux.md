---
title: "yadiggg: MIMX8MN4DVTJZAA Pinmux Assignment Spec"
project: yadiggg
status: active-draft
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
---

> **Historical proposal — unverified.** This document is preserved for provenance, not as a current requirement, approved component selection, validated engineering result, or manufacturing instruction. Current status is in `docs/project-state.md`.

# yadiggg: MIMX8MN4DVTJZAA Pinmux Assignment Spec
**Date of Document**: Friday, June 5, 2026
**Status**: Active Draft (requires verification against official NXP pin tables before schematic capture)
**Target Silicon**: NXP i.MX 8M Nano Quad-Core SoC (486-pin BGA) & NXP LPC55S69 (Cortex-M33) Co-Processor

This specification defines the exact physical pins, multiplexed functions (ALT modes), and signal routings for the **yadiggg PCBA V1**. It guarantees complete hardware-level compatibility between our high-performance A53-based Linux cores, the real-time Cortex-M33 co-processor core, and our specialized visual/audio peripherals.

---

## 1. System Pinmux Allocation Matrix

| i.MX 8M Pad Name | Ball | Function (ALT) | Target Signal | Peripheral | Voltage Rail | Description / Design Constraints |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ECSPI1_SCLK** | B1 | ECSPI1_SCLK (ALT0) | `LCD_SCLK` | Sharp LS027B7DH01 | VCC_3V3 | High-frequency SPI clock to Sharp Memory LCD |
| **ECSPI1_MOSI** | A2 | ECSPI1_MOSI (ALT0) | `LCD_MOSI` | Sharp LS027B7DH01 | VCC_3V3 | Master Out Slave In (Data Input to LCD) |
| **ECSPI1_SS0** | B2 | ECSPI1_SS0 (ALT0) | `LCD_SCS` | Sharp LS027B7DH01 | VCC_3V3 | Serial Chip Select (Active High for Sharp) |
| **GPIO1_IO08** | C4 | GPIO1_IO08 (ALT0) | `LCD_EXTCOMIN` | Sharp LS027B7DH01 | VCC_3V3 | External Com Invert signal (50Hz toggle) |
| **GPIO1_IO09** | D4 | GPIO1_IO09 (ALT0) | `LCD_DISP_ON` | Sharp LS027B7DH01 | VCC_3V3 | General display on/off hardware enable gate |
| **I2C3_SCL** | H4 | I2C3_SCL (ALT0) | `I2C3_SCL` | TI DRV2605L / Haptics| VCC_3V3 | Dedicated I2C clock for haptic wave generation |
| **I2C3_SDA** | J4 | I2C3_SDA (ALT0) | `I2C3_SDA` | TI DRV2605L / Haptics| VCC_3V3 | Dedicated I2C data for haptic wave generation |
| **GPIO1_IO12** | E4 | GPIO1_IO12 (ALT0) | `HAPTIC_INT` | TI DRV2605L / Haptics| VCC_3V3 | Haptic driver trigger interrupt line |
| **SAI5_RXC** | K3 | PDM_CLK (ALT3) | `PDM_CLK` | Knowles SPH0641LM4H | VCC_1V8 | Shared 1.8V PDM clock driven by SoC decimate |
| **SAI5_RXD0** | L3 | PDM_BIT_STREAM0 (ALT3)| `PDM_DATA_L` | Knowles SPH0641LM4H | VCC_1V8 | PDM Data line for Left Mic (Select = GND) |
| **SAI5_RXD1** | M3 | PDM_BIT_STREAM1 (ALT3)| `PDM_DATA_R` | Knowles SPH0641LM4H | VCC_1V8 | PDM Data line for Right Mic (Select = VDD) |
| **SAI3_MCLK** | N1 | SAI3_MCLK (ALT0) | `DAC_MCLK` | ESS ES9218PC Sabre | VCC_1V8 | Ultra-low jitter Master Clock (audio source) |
| **SAI3_TXC** | P1 | SAI3_TXC (ALT0) | `DAC_BCLK` | ESS ES9218PC Sabre | VCC_1V8 | I2S Bit Clock (Serial Clock for audio frames)|
| **SAI3_TXFS** | R1 | SAI3_TXFS (ALT0) | `DAC_LRCK` | ESS ES9218PC Sabre | VCC_1V8 | Word Select / Frame Sync (44.1kHz Left/Right) |
| **SAI3_TXD0** | T1 | SAI3_TXD0 (ALT0) | `DAC_SDATA` | ESS ES9218PC Sabre | VCC_1V8 | Stereo Audio Output Digital Serial Stream |
| **I2C2_SCL** | F3 | I2C2_SCL (ALT0) | `DAC_SCL` | ESS ES9218PC Sabre | VCC_1V8 | I2C Control clock for Sabre register map |
| **I2C2_SDA** | G3 | I2C2_SDA (ALT0) | `DAC_SDA` | ESS ES9218PC Sabre | VCC_1V8 | I2C Control data for Sabre register map |
| **GPIO1_IO15** | F4 | GPIO1_IO15 (ALT0) | `DAC_RESET` | ESS ES9218PC Sabre | VCC_1V8 | Active-Low hardware reset pin for Sabre DAC |

---

## 2. Real-Time Cortex-M33 Pinmux and Shared Memory Interface

The **LPC55S69** (co-processor) is physically routed parallel to the i.MX 8M Nano to manage instant-on display pre-initialization, power-state transition interrupts, and real-time haptic feedback routing. 

1.  **Shared SPI Bridge**: The co-processor shares access to the Sharp Memory LCD over a dual-master analog multiplexer (**TI TS3A24157**), allowing either the LPC55S69 (during boot and standby) or the i.MX 8M Nano (during active Linux browsing) to drive the display.
2.  **Shared Memory Mailbox Interface (HPI)**: Inter-processor communication (IPC) is established over an isolated, high-speed 8-bit parallel host port interface (HPI) using the following pins on the LPC55S69:
    *   `PIO0_22` -> `IPC_DATA0`
    *   `PIO0_23` -> `IPC_DATA1`
    *   `PIO0_24` -> `IPC_DATA2`
    *   `PIO0_25` -> `IPC_DATA3`
    *   `PIO0_26` -> `IPC_DATA4`
    *   `PIO0_27` -> `IPC_DATA5`
    *   `PIO0_28` -> `IPC_DATA6`
    *   `PIO0_29` -> `IPC_DATA7`
    *   `PIO0_15` -> `IPC_REQ` (Request Handshake, Interrupt-driven)
    *   `PIO0_16` -> `IPC_ACK` (Acknowledge Handshake)

---

## 3. Visual Pinmux Routing Diagram (Mux Tree)

```widget title="yadiggg_pinmux_routing"
<svg width="100%" viewBox="0 0 680 340" style="background-color:transparent;">
  <defs>
    <!-- Arrow Marker Definition -->
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1 L8 5 L2 9 Z" style="fill:var(--color-diagram-arrow)" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="340" y="25" text-anchor="middle" font-family="var(--font-sans)" font-size="14px" font-weight="600" style="fill:var(--color-text-primary);">i.MX 8M Nano Core Peripheral Pinmux Matrix</text>

  <!-- Central Processor Node -->
  <rect x="250" y="110" width="180" height="110" rx="12" style="fill:var(--color-diagram-node-emphasis);stroke:var(--color-diagram-node-emphasis-border);stroke-width:1.5px;" />
  <text x="340" y="155" text-anchor="middle" font-family="var(--font-sans)" font-size="13px" font-weight="600" style="fill:var(--color-brand-ink);">NXP i.MX 8M Nano</text>
  <text x="340" y="175" text-anchor="middle" font-family="var(--font-sans)" font-size="11px" style="fill:var(--color-brand-ink);opacity:0.85;">(Cortex-A53 Core)</text>
  <text x="340" y="195" text-anchor="middle" font-family="var(--font-sans)" font-size="10px" font-weight="500" style="fill:var(--color-brand-ink);opacity:0.75;">BGA-486 Pad Ring</text>

  <!-- Peripheral Node: LCD -->
  <rect x="40" y="45" width="140" height="50" rx="10" style="fill:var(--color-diagram-node);stroke:var(--color-diagram-node-border);stroke-width:1px;" />
  <text x="110" y="70" text-anchor="middle" font-family="var(--font-sans)" font-size="11px" font-weight="500" style="fill:var(--color-text-primary);">Sharp Memory LCD</text>
  <text x="110" y="85" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" style="fill:var(--color-text-secondary);">ECSPI1 Bus (3.3V)</text>

  <!-- Peripheral Node: Audio DAC -->
  <rect x="500" y="45" width="140" height="50" rx="10" style="fill:var(--color-diagram-node);stroke:var(--color-diagram-node-border);stroke-width:1px;" />
  <text x="570" y="70" text-anchor="middle" font-family="var(--font-sans)" font-size="11px" font-weight="500" style="fill:var(--color-text-primary);">Sabre ES9218PC DAC</text>
  <text x="570" y="85" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" style="fill:var(--color-text-secondary);">SAI3 I2S + I2C2 (1.8V)</text>

  <!-- Peripheral Node: MEMS Mics -->
  <rect x="40" y="235" width="140" height="50" rx="10" style="fill:var(--color-diagram-node);stroke:var(--color-diagram-node-border);stroke-width:1px;" />
  <text x="110" y="260" text-anchor="middle" font-family="var(--font-sans)" font-size="11px" font-weight="500" style="fill:var(--color-text-primary);">Dual SPH0641 Mics</text>
  <text x="110" y="275" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" style="fill:var(--color-text-secondary);">Native PDM Interface (1.8V)</text>

  <!-- Peripheral Node: Haptic Driver -->
  <rect x="500" y="235" width="140" height="50" rx="10" style="fill:var(--color-diagram-node);stroke:var(--color-diagram-node-border);stroke-width:1px;" />
  <text x="570" y="260" text-anchor="middle" font-family="var(--font-sans)" font-size="11px" font-weight="500" style="fill:var(--color-text-primary);">TI DRV2605L Haptics</text>
  <text x="570" y="275" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" style="fill:var(--color-text-secondary);">I2C3 Bus + GPIO (3.3V)</text>

  <!-- Routing Lines -->
  <!-- Central to LCD -->
  <path d="M 250 140 L 180 85" fill="none" style="stroke:var(--color-diagram-arrow);stroke-width:1.5px;" marker-end="url(#arrow)" />
  <!-- Central to DAC -->
  <path d="M 430 140 L 500 85" fill="none" style="stroke:var(--color-diagram-arrow);stroke-width:1.5px;" marker-end="url(#arrow)" />
  <!-- Central to Mics -->
  <path d="M 250 190 L 180 245" fill="none" style="stroke:var(--color-diagram-arrow);stroke-width:1.5px;" marker-end="url(#arrow)" />
  <!-- Central to Haptics -->
  <path d="M 430 190 L 500 245" fill="none" style="stroke:var(--color-diagram-arrow);stroke-width:1.5px;" marker-end="url(#arrow)" />

  <!-- Signal Labels inside paths -->
  <text x="210" y="105" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" font-weight="500" style="fill:var(--color-text-secondary);">MOSI, SCLK, SCS</text>
  <text x="470" y="105" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" font-weight="500" style="fill:var(--color-text-secondary);">MCLK, BCLK, LRCK</text>
  <text x="210" y="230" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" font-weight="500" style="fill:var(--color-text-secondary);">PDM_CLK, DATA</text>
  <text x="470" y="230" text-anchor="middle" font-family="var(--font-sans)" font-size="9px" font-weight="500" style="fill:var(--color-text-secondary);">SCL, SDA, INT</text>
</svg>
```

---

## 4. Signal Integrity & Board Layout Rules
1.  **ECSPI1 LCD Clock Speed**: The Sharp memory LCD is limited to a maximum SPI clock frequency of **2.0MHz**. SPI traces must be kept under 50mm and routed on Layer 1 with solid ground references on Layer 2.
2.  **PDM Microphone Clock**: Set the `PDM_CLK` to **2.4MHz** or **3.072MHz** to match Knowles operating specifications. The PDM data lines are high-speed digital lines; route them away from any analog audio trace (V_ANA_DAC or 3.5mm Aux output) by at least **1.5mm** (or separated by a ground guard trace) to prevent digital clock feedthrough into the high-end headphone path.
3.  **I2S Master Clock (MCLK)**: Since we are using an asynchronous Sabre Quad-DAC (`ES9218PC`), the Master Clock (`DAC_MCLK`) must be exceptionally stable. It is routed with a dedicated coplanar waveguide trace of **50-ohm impedance** directly from the SoC's Clock Synthesizer or generated by an external low-noise TCXO to eliminate jitter.
