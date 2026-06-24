---
title: "ADR-0005: Sonic ID Code Is a Sandbox Prototype"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, sonic-id, prototype]
backlinks:
  - "[[CONTEXT]]"
  - "[[hardware/yadiggg_sonic_id_and_olaf_port]]"
---

# ADR-0005: Sonic ID Code Is a Sandbox Prototype

## Status
Accepted

## Context
The workspace includes C files for an OLAF-like audio fingerprinting pipeline, a SQLite schema extension, a mock fingerprint seed, and a macOS emulated capture path. These files compile locally, but they are not validated against real OLAF, real PDM hardware, production audio corpora, or target Yocto builds.

## Decision
Treat `src/sonic_id/` as a sandbox prototype until it is validated with real audio, target ALSA devices, and reference fingerprints.

## Consequences
- The code can remain useful for interface exploration and build-system shape.
- It should not be called production-ready.
- Future work should add tests, sample fixtures, real reference fingerprints, and a target-hardware validation log.
