---
title: "ADR-0006: Yocto Layer Is a Build Scaffold"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, yocto, build]
backlinks:
  - "[[CONTEXT]]"
  - "[[hardware/yadiggg_yocto_recipe_and_image_build]]"
---

# ADR-0006: Yocto Layer Is a Build Scaffold

## Status
Accepted

## Context
The workspace contains a generated `yocto-meta/meta-yadiggg` layer, BitBake recipes, copied source files, and a setup script. The layer has not been proven by a completed BitBake build in this workspace.

## Decision
Treat the Yocto layer as a build scaffold, not a proven kernel/rootfs image.

## Consequences
- Keep the Yocto layer as an active starting point.
- Do not describe it as producing a verified image until `bitbake yadiggg-image` succeeds and output artifacts are recorded.
- Future build logs should be committed as a validation note or ADR update.
