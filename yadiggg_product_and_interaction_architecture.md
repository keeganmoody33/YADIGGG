---
title: "yadiggg: Product and Interaction Architecture"
project: yadiggg
status: completed
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

# yadiggg: Product and Interaction Architecture
**Date of Document**: Wednesday, June 3, 2026
**Time of Document**: 04:08 AM EDT
**Status**: Master Product Specification (V2.0 - Core Product & UX)
**Authors**: yadiggg Core Team & Accio Product Architecture Suite

---

## 1. The Overall Soul of yadiggg

### 1.1 The Philosophy of "Offline Soul" and "Disappearing Hardware"
In an era dominated by notifications, subscriptions, and always-on algorithmic feeds, **yadiggg** is an intentional rebellion. It is a dedicated, pocketable, physical instrument designed for vinyl digging enthusiasts ("crate diggers"). Its core philosophy is centered on **preserving the "Offline Soul" of the digging experience**. 

The record is the hero—**yadiggg** is merely a transparent lens that reveals its history. 
*   **The Disappearing Device**: Unlike a smartphone, which sucks the user into an endless digital loop of texts, social media, and emails, **yadiggg** is designed for a single physical gesture: *Aim, Scan, Reveal, and Pocket*. It is a tool of fast retrieval that immediately disappears back into a pocket, keeping the digger grounded in the tactile world of vinyl.
*   **Facts-Only Music Intelligence**: **yadiggg** rejects the "smart companion" bloat of modern devices. It does not recommend, rank, rate, or attempt to sell you music. It provides objective, structured, metadata: Who played on this? Who produced it? Where was it recorded? What samples are embedded in this groove? By stripping away subjective reviews and rankings, it forces the user to make their own artistic and aesthetic judgments.

### 1.2 YouTube Studies: Grounding yadiggg in Real-World Vinyl Digging
The design of **yadiggg** is directly informed by observational studies of vinyl diggers on platforms like YouTube (e.g., *Crate Digging* documentaries, *Vinyl Me, Please* store tours, producer sessions). 

In these videos, several friction points consistently emerge:
1.  **The Small-Print Struggle**: Diggers constantly squint at the back of obscure, vintage records or tiny center labels in dimly lit record store basements, attempting to read micro-credits for known session players or sampleable breaks.
2.  **The Private Press Mystery**: Private press, bootleg, or white-label promos often have no legible tracklists or databases, leaving diggers blind-buying records based solely on the cover art or a matrix run-out engraving.
3.  **Smartphone Distraction**: Diggers who use their phones to look up records on Discogs or search engines are constantly pulled out of the "flow state" of crate digging by incoming texts, low-battery warnings, and poor cellular reception in concrete basements.
4.  **Turntable Sharing Friction**: In high-traffic record shops, listening stations are either occupied, have broken needles, or have long lines. Diggers need a discrete way to hear what a record sounds like without waiting in line.

**yadiggg** solves every one of these problems with a single pocketable tool that operates entirely offline in concrete basements, resolving small-print via localized OCR and identifying private-press tracks via acoustic fingerprinting.

---

## 2. Core Product Features (In-Scope)

*   **Offline OCR Engine**: Point-and-shoot text capture optimized for circular vinyl labels, small-print back covers, and handwritten matrix run-outs.
*   **Local Metadata Database**: An on-device SQLite database containing over 1,000,000 index files, mapping artists, catalog numbers, release labels, session musicians, studio locations, and sample lineage.
*   **"Facts-Only" Narrative**: A minimalist, clean text layout showing only objective data points (No scores, no "similar to" recommendation engines).
*   **Sonic ID (Acoustic Fingerprinting)**: A "reverse identification" engine. When a label is too worn, torn, or represents a private press with no text, the user can hold a physical "record" button and let the device's high-SNR built-in microphones listen to 5–10 seconds of the track playing from a turntable speaker to identify the release.
*   **Audio Previews (The Wishlist Sync)**: Local eMMC storage capacity (32GB) holding up to 50,000 30-second high-quality audio previews (compressed at 128kbps in OGG/MP3 format). Users can listen to these previews via a physical 3.5mm headphone jack.
*   **Wired-First Updates**: Complete software and database sync occurring via a high-speed USB-C connection to a companion desktop client. No cellular contracts, no cloud requirements.

---

## 3. App Flow & User Experience

```
  +--------------------------------------------------------------+
  |                        PHYSICAL UX FLOW                      |
  +--------------------------------------------------------------+
  |                                                              |
  |   [ AIM ]  =======>  [ HOLD ORANGE ] =======> [ REVEAL ]     |
  |  Rear camera          Hold side button         2.7" LCD screen|
  |  pointing at          initiates OCR scan        pops open text |
  |  label (10-15cm)      and haptic tap          data instantly  |
  |                                                              |
  +--------------------------------------------------------------+
```

### 3.1 The "Aim-Scan-Reveal" Core Loop
1.  **AIM**: Point the rear pinhole camera (using an ON Semi 13MP sensor with macro-autofocus) at the center label, back-cover credit, or matrix run-out from a distance of 10–15 cm (4–6 inches).
2.  **SCAN**: Press and hold the physical Orange Silicone Button on the side. The device wakes up, performs sub-100ms autofocus, captures the frame, and triggers a subtle, mechanical-feeling haptic "click" (via a 10mm linear resonant actuator) to confirm capture.
3.  **REVEAL**: The 2.7" Sharp Memory LCD instantly reveals the metadata payload (sub-1.5s latency from button press). The user uses a physical, knurled side-dial or tactile mechanical toggle to scroll through deep credits.
4.  **EXIT**: Release the button or double-click to save to "Digging List". Slip the device back into your pocket.

---

## 4. Grounded User Stories

### Story 1: Marcus — The Hip-Hop Producer ("The Sample Hunter")
*   **User Profile**: Hip-hop producer looking for rare, un-shazamed soul, funk, and international breaks to chop into beats.
*   **The Environment**: A crowded, dusty record fair in a concrete community center basement with zero cellular service.
*   **The Interaction**: 
    *   Marcus finds an obscure 1974 Nigerian funk record with a damaged cover and a faded center label. 
    *   He pulls **yadiggg** from his pocket. The matte frosted translucent amber casing feels premium and secure in his hand.
    *   He points the rear pinhole camera at the matrix run-out etched on the inner groove of the vinyl and holds the Orange Button.
    *   The device performs an instant offline OCR capture and triggers a sharp haptic tap.
    *   On the high-contrast 1-bit Sharp Memory LCD, the screen populates with the track's DNA: 
        *   *Artist: The Funkees*
        *   *Producer: Organized Noize (Linage)*
        *   *Sample Warning: Contains a 2-second drum break loop used in 1996 OutKast sessions.*
    *   Marcus holds down the button labeled "Record" on the screen while holding **yadiggg** near the turntable listening station speaker. The device captures 5 seconds of the drum break. The offline Sonic ID database matches it against Tier-1 local fingerprints, verifying it is the rare original pressing, not the 1990s bootleg reissue.
    *   Marcus double-clicks the orange button to save it to his local "Wishlist" and slides **yadiggg** back into his pocket to keep digging.

### Story 2: Sarah — The Jazz Collector ("The Blind-Buy Specialist")
*   **User Profile**: High-end jazz purist who collects archival Blue Note, Prestige, and private press releases. She focuses heavily on session musicians (e.g., who played trumpet or bass on a specific pressing).
*   **The Environment**: A dimly lit, narrow aisle of a boutique record shop.
*   **The Interaction**:
    *   Sarah finds an archival jazz record with no credits listed on the outer sleeve—only a generic tracking list.
    *   She holds **yadiggg** over the small print of the center label and holds the Orange Button.
    *   The high-performance macro-autofocus lens resolves the tiny 6pt Helvetica text.
    *   The monochrome screen immediately formats the credits using the Swiss geometric 'Crate-Sans' bitmap font system:
        *   *Trumpet: Miles Davis*
        *   *Double Bass: Paul Chambers*
        *   *Recorded At: Van Gelder Studio, Hackensack, NJ (1956)*
    *   Sarah uses the knurled, physical side-dial to scroll smoothly through the engineering details. She sees that Rudy Van Gelder himself was the lacquer-cutter for this specific catalog run.
    *   She plugs her headphones into the 3.5mm headphone jack of **yadiggg**, presses the orange button, and listens to a crisp, high-fidelity 30-second audio preview of the opening track (pre-cached during her last desktop USB-C sync) driven by the high-end ESS DAC.
    *   Sarah buys the record, completely confident in its historical lineage.

---

## 5. Screen Layout & Display Specifications

The **2.7-inch Sharp Memory LCD (LS027B7DH01)** features a resolution of **400x240 pixels (1-bit monochrome)**. This requires a highly specialized, non-anti-aliased, pixel-perfect bitmap typography layout to remain crisp and readable under bright record-fair spotlights or dim basements.

### 5.1 The 'Crate-Sans' Typography System
*   **Font Family**: `Crate-Sans` (A custom Swiss-geometric, pixel-aligned bitmap font).
*   **Minimum Stroke Width**: 2 pixels to guarantee high contrast.
*   **Hierarchy**:
    *   *Header (Title & Artist)*: 16px Bold, Uppercase (Max 24 characters per line).
    *   *Body (Credits & Lineage)*: 11px Regular, Left-Aligned (Max 36 characters per line).
    *   *Footer (Label, Cat #, Year)*: 9px Mono, Constant Position (Bottom 15 pixels of the screen).

### 5.2 Screen Template Wireframe
```
+------------------------------------------+ (0,0)
| [STANKONIA] - OUTKAST                    | <-- 16px Bold Header
|------------------------------------------| <-- 1px solid separator line
| PRODUCER: EARTH-TONE III                 | <-- 11px Regular Body
| VOCALS: ANDRE 3000, BIG BOI              |
| STUDIO: STANKONIA STUDIOS, ATLANTA       |
| SAMPLE: "DISCO LADY" BY J. TAYLOR        |
|                                          |
|                                          |
|                                          |
|------------------------------------------| <-- 1px solid separator line
| ARISTA RECORDS  |  CAT: 29007  |  2000   | <-- 9px Mono Footer
+------------------------------------------+ (400,240)
```

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]

*   **Sister Spec**: [[yadiggg_brand_identity_and_design_guidelines]]
*   **Sister Spec**: [[yadiggg_firmware_and_update_architecture]]