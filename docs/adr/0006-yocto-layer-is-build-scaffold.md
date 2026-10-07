---
title: "ADR-0006: Yocto Layer Is a Build Scaffold"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, yocto, build]
---

# ADR-0006: Yocto Layer Is a Build Scaffold

## Status
Accepted

## Context
The repository contains a `yocto-meta/meta-yadiggg` layer and BitBake recipes. The layer has not been proven by a completed BitBake build in this workspace.

## Decision
Treat the Yocto layer as a build scaffold, not a proven kernel/rootfs image.

## Consequences
- Keep `src/sonic_id/` as the only maintained capture-source tree; the recipe stages it through `FILESEXTRAPATHS`.
- Do not describe it as producing a verified image until `bitbake yadiggg-image` succeeds and output artifacts are recorded.
- Use `python3 scripts/validate_yocto_layer.py` to check source staging; this is not a BitBake validation.
