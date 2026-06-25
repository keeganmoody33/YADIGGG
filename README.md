# yadiggg

> *The record is the hero — yadiggg is merely a transparent lens that reveals its history.*

**yadiggg** is a pocketable, offline-first physical companion device for vinyl crate diggers. A dedicated, purpose-built gadget — the size of a voice recorder — that you pull out at a record fair or dusty basement shop to instantly decode any record you're holding.

No phone. No internet. No Shazam. No Discogs subscription required.

---

## The Problem

Every vinyl digger knows the pain:

- **You can't read the label** — tiny 6pt credits in a dim basement
- **The record has no tracklist** — private press, white label, mystery groove
- **Your phone is a distraction** — one Discogs search turns into 45 minutes of Instagram
- **The listening station has a line** — you're flying blind on a $40 blind buy

yadiggg kills all four of these problems with a single gesture.

---

## The Core Loop: Aim → Scan → Reveal

1. **AIM** — Point the rear 13MP pinhole camera at a vinyl center label or matrix run-out (10–15cm away)
2. **SCAN** — Hold the physical Orange Button. Sub-100ms autofocus. Haptic tap confirms capture.
3. **REVEAL** — The 2.7" Sharp Memory LCD pops the metadata payload in under **1.5 seconds**:
   - Artist, producer, session musicians, studio location
   - Sample lineage and copyright flags
   - Label, catalog number, year

No boot screen. No loading spinner. Just facts.

---

## Hardware

| Component | Details |
|---|---|
| **Main SoC** | NXP i.MX 8M Nano — Quad ARM Cortex-A53, Yocto Linux |
| **Co-Processor** | NXP LPC55S69 — Dual Cortex-M33, instant-on display & haptics |
| **Display** | Sharp LS027B7DH01 — 2.7" reflective memory LCD (400×240, 1-bit) |
| **DAC** | ESS ES9218PC SABRE — 32-bit quad headphone DAC, 3.5mm jack |
| **Microphones** | Dual Knowles SPH0641LM4H-1 MEMS PDM microphone array |
| **Storage** | 32GB eMMC — 50,000 pre-loaded 30-second audio previews |

---

## Intelligence (All Offline)

### Sonic ID — Acoustic Fingerprinting
When a label is too worn or torn to read, hold yadiggg near a playing record. The **OLAF DSP Engine** fingerprints the audio — 2048-point FFT, 32 logarithmic sub-bands, XNOR-popcount sliding correlation — against a local SQLite database. No Shazam API. No cell service. No cloud.

### Basement Scanner — OCR
Tesseract OCR resolves wrapped vinyl spines, barcodes, and catalog numbers even in low-light basement conditions.

### On-Device Database
1,000,000+ record index stored locally. Updates happen over USB-C from a companion desktop client. That's it.

---

## The Philosophy

In a world where every gadget competes for your attention, yadiggg deliberately does **one thing**. No social feed, no algorithm, no recommendations. Just objective, structured facts about the record in your hand.

The design is informed directly by watching real vinyl diggers at work — the squinting at back-cover credits, the private press mystery, the smartphone distraction spiral, the turntable queue. yadiggg is the tool that should have existed for decades.

---

## What's In This Repo

```
src/                  # Sonic ID OLAF fingerprint engine (C)
hardware/             # KiCad schematic & PCB layout scaffolds
yocto-meta/           # meta-yadiggg custom Yocto Linux layer
docs/                 # ADRs, component selections, schematic status
physical-design/      # Enclosure direction brief
yadiggg_schema.sql    # SQLite intelligence graph schema
CONTEXT.md            # Master domain glossary & architecture decisions
```

### Key Documents
- [Product & Interaction Architecture](yadiggg_product_and_interaction_architecture.md)
- [Hardware & Electrical Integration](yadiggg_hardware_and_electrical_integration.md)
- [Firmware & Update Architecture](yadiggg_firmware_and_update_architecture.md)
- [Intelligence Graph & Schema](yadiggg_intelligence_graph_and_schema.md)
- [Brand Identity & Design Guidelines](yadiggg_brand_identity_and_design_guidelines.md)
- [Strategic Roadmap](yadiggg_strategic_decision_map_and_roadmap.md)
- [Adversarial Testing Protocol](yadiggg_adversarial_testing_and_validation_protocol.md)

---

## Current Status

yadiggg is in active design and prototyping. Physical form factor not yet locked. KiCad schematics are scaffolds. BOM reconciliation in progress. Sonic ID requires hardware ALSA validation on target. Every major decision is tracked as an ADR in [`docs/adr/`](docs/adr/).

This is a serious product being built seriously.

---

*Built for the diggers.*
