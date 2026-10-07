# Yocto layer and build notes

**Status:** build scaffold; no BitBake image or target hardware has been verified. This file documents repository paths and a reviewable build entrypoint, not a validated board configuration or boot/performance claim.

## Source ownership

- Canonical prototype source, Makefile, and ALSA configuration: `src/sonic_id/`.
- Layer: `yocto-meta/meta-yadiggg/`.
- Capture recipe: `yocto-meta/meta-yadiggg/recipes-apps/yadiggg-capture/yadiggg-capture_1.0.bb`.
- Image recipe: `yocto-meta/meta-yadiggg/recipes-core/images/yadiggg-image.bb`.
- Recipe-local init script: `yocto-meta/meta-yadiggg/recipes-apps/yadiggg-capture/files/yadiggg-init`.

The application recipe prepends `${THISDIR}/../../../../src/sonic_id:` to `FILESEXTRAPATHS`. BitBake stages the native files from that directory; the recipe `files/` directory contains only the init script. Do not copy or edit a second C/Makefile/ALSA implementation there. `python3 scripts/validate_yocto_layer.py` checks this invariant without writing files.

## Build outline

Prerequisites are a compatible, initialized Yocto/OpenEmbedded build environment, the layers declared by `conf/layer.conf`, and a machine configuration chosen for actual target hardware. This repository does not select a validated production machine or BSP.

After adding `yocto-meta/meta-yadiggg` to an existing build configuration:

```sh
bitbake yadiggg-image
```

This command has not been run in a Yocto environment. The image recipe and package have `LICENSE = "CLOSED"` because this repository does not establish code redistribution rights; this is not permission to distribute them.

## What remains unverified

No target board, audio-card configuration, boot image, camera/display driver, image size, boot timing, battery behavior, programming/recovery flow, or functional test is validated. The native C code is a prototype and the image recipe must not be used as a production firmware release. See the [manufacturer handoff](../manufacturing/handoff.md) and [readiness register](../docs/project-state.md).
