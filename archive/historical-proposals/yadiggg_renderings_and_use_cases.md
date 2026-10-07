---
title: "yadiggg: Visual Renderings & Product Use Cases"
project: yadiggg
status: reference
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

> **Historical proposal — unverified.** This document is preserved for provenance, not as a current requirement, approved component selection, validated engineering result, or manufacturing instruction. Current status is in `docs/project-state.md`.

# yadiggg: Visual Renderings & Product Use Cases
**Date**: Saturday, June 6, 2026  
**Status**: Official Product Visual Showcase (V1.0)  
**Authors**: yadiggg Design Group & Accio Product Architecture Suite

---

## 1. Visual Narrative & Design Language

The visual system of **yadiggg** (formerly **Crate IQ**) translates its core philosophy of the **"Offline Soul"** and **"Disappearing Hardware"** into physical, tactile aesthetic assets. 

By exposing the internal architecture of the device through a translucent dark smoke-grey polycarbonate shell, the physical hardware mirrors its factual, un-bloated digital soul. The preferred industrial-design direction is the **Rendering 2 scale**: a very small, slim, second-pocket object that feels smaller than a phone and never reads as a bulky walkie-talkie. A prominent physical orange slide-button sits on the side, providing high tactility, while the overall design stays focused on high efficiency and zero distractions.

The official logo direction is grounded in the source sketch `yadigggsketch.pdf` / `yadigggsketch_rendered.png` and represents the **shovel and speaker converging**: from a distance, the silhouette reads as a shovel digging downward into a record or ground surface; on closer inspection, the head contains a red-highlighted speaker cone with neon light/soundwave arcs blowing back from it. This replaces the earlier generic spade/bag/box interpretation.

Below is the official collection of high-fidelity visual renderings showcasing how different users interact with **yadiggg** in real-world scenarios, now anchored around the compact Rendering 2 pocket-device direction.

---

## 2. Selected Use Cases & Renderings

### Use Case 1: Point-and-Shoot Offline OCR Scan
* **User Profile**: Marcus (The Sample Hunter)
* **Action**: Holding the side orange slide-button to initiate a sub-100ms macro autofocus scan of a physical record label.
* **Context**: A dusty, dimly lit record fair basement with zero cellular service. The device utilizes its local OCR engine (running on the NXP i.MX 8M Nano SoC) to instantly digitize and match the printed text or run-out matrix etching.
* **Visual Rendering**:
  ![Aim-Scan-Reveal OCR Capture](https://sc02.alicdn.com/kf/Aa8670a6c38f542e7b8abaca8ca3bae34U.png)

---

### Use Case 2: Compact Deep Credit Metadata Reveal & Headphone Preview — preferred direction
* **User Profile**: Sarah (The Jazz Collector)
* **Action**: Reviewing full session credits on a small, crisp monochrome display and listening to a 30-second high-fidelity cached audio preview.
* **Context**: This is the preferred physical direction: a compact, second-pocket device smaller than a phone, not a large phone-like slab and not a walkie-talkie. The 1-bit monochrome display remains legible without dominating the body. Sarah plugs headphones into the dedicated 3.5mm headphone jack, driven by the low-noise ESS ES9218PC Hi-Res DAC.
* **Visual Rendering**:
  ![Compact Rendering 2 Direction](https://sc02.alicdn.com/kf/A6b126c915a5d4c63b4526b7041c96e59M.png)

---

### Use Case 3: Sonic ID (Acoustic Fingerprinting)
* **User Profile**: Hip-Hop Producers & Collectors
* **Action**: Capturing 5–10 seconds of ambient audio via dual Knowles MEMS microphones to run a localized fingerprint match against the offline SQLite database.
* **Context**: Used when labels are worn, torn, or have zero printed text. The microphones are acoustically isolated via 40 Durometer soft silicone grommets, ensuring mechanical vibrations from haptic clicks do not distort the captured soundwave.
* **Visual Rendering**:
  ![Sonic ID Acoustic Capture](https://sc02.alicdn.com/kf/A74c156eb1b504427a7094be659eed8a0J.png)

---

## 3. Removed Direction

The previous packaging/tote ecosystem direction is no longer treated as a valid target. The bag, box, and generic spade interpretation are excluded from the current design path. Future visuals should focus on the compact pocket device, the Rendering 2 scale language, and the corrected shovel-speaker-neon-wave logo concept.

---

## 4. Hardware Alignment & Manufacturing Specifications

These visual renderings are 100% aligned with the manufacturing specifications outlined in:
* [Manufacturer handoff](manufacturing/handoff.md) (current review scope and unresolved engineering inputs)
* [yadiggg Product and Interaction Architecture](yadiggg_product_and_interaction_architecture.md) (Swiss-geometric screen layout wireframes, app flow, and user personas)
* [yadiggg Brand Identity and Design Guidelines](yadiggg_brand_identity_and_design_guidelines.md) (corrected shovel-speaker logo with red speaker cone and neon soundwave arcs, compact hardware-first direction, Amber Orange `#E07A5F`, Obsidian Charcoal `#1A1A1D`, Cream White `#F4F1DE`, Speaker Red `#D83232`, and Neon Wave Green `#72FF66`)

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]
