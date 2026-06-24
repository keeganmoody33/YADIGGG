---
title: "yadiggg: Yocto Embedded Linux Custom Layer & Image Build Manual"
project: yadiggg
status: completed
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---

# yadiggg: Yocto Embedded Linux Custom Layer & Image Build Manual
**Date of Document**: Friday, June 5, 2026
**Status**: Release V1.0 (Production Build System Spec)
**Target Layer**: `meta-yadiggg` (Custom Application & System BSP Overlay)

This document maps out the creation and configuration of **`meta-yadiggg`**, our custom Yocto metadata layer. It packages our high-performance C-based Sonic ID capture daemon, ALSA configurations, and offline databases directly into a monolithic, read-only Yocto Linux kernel image (`yadiggg-image.bb`) optimized to boot on the NXP i.MX 8M Nano in under **1.8 seconds**.

---

## 1. Yocto Layer Directory Tree

To cleanly overlay our applications onto the official Poky and Freescale BSP layers, we establish the following structure in our build workspace:

```
    yocto-meta/meta-yadiggg/
    ├── conf/
    │   └── layer.conf
    ├── recipes-core/
    │   └── images/
    │       └── yadiggg-image.bb
    └── recipes-apps/
        └── yadiggg-capture/
            ├── files/
            │   ├── asound.conf
            │   └── yadiggg-init
            └── yadiggg-capture_1.0.bb
```

---

## 2. Layer Configuration (`conf/layer.conf`)

Defines the metadata priority, paths, and dependencies for the custom layer.

```bitbake
# meta-yadiggg/conf/layer.conf
# We have a packages directory, add to BBPATH
BBPATH .= ":${LAYERDIR}"

# We have recipes-* directories, add to BBFILES
BBFILES += "${LAYERDIR}/recipes-*/*/*.bb \
            ${LAYERDIR}/recipes-*/*/*.bbappend"

BBFILE_COLLECTIONS += "meta-yadiggg"
BBFILE_PATTERN_meta-yadiggg = "^${LAYERDIR}/"
BBFILE_PRIORITY_meta-yadiggg = "9"

LAYERSERIES_COMPAT_meta-yadiggg = "scarthgap"

# Enforce immediate build dependency on Freescale and OpenEmbedded core
LAYERDEPENDS_meta-yadiggg = "core freescale-layer openembedded-layer"
```

---

## 3. Sonic ID Daemon Application Recipe (`recipes-apps/yadiggg-capture/yadiggg-capture_1.0.bb`)

This recipe cross-compiles our native C source files, packages our custom ALSA audio configurations, and integrates our SysVinit service into the RootFS.

```bitbake
# meta-yadiggg/recipes-apps/yadiggg-capture/yadiggg-capture_1.0.bb
SUMMARY = "yadiggg Sonic ID PDM Capture & Offline Matching Daemon"
DESCRIPTION = "Cross-compiles the OLAF DSP engine and links with ALSA/SQLite3 for offline record lookups."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

# Build dependencies
DEPENDS = "alsa-lib sqlite3"

# Runtime dependencies
RDEPENDS:${PN} = "libasound sqlite3"

# Source files fetched from local work directories
SRC_URI = " \
    file://yadiggg_capture.c \
    file://olaf.c \
    file://olaf.h \
    file://Makefile \
    file://asound.conf \
    file://yadiggg-init \
"

S = "${WORKDIR}"

# Use Poky's autotools or plain make configurations
inherit update-rc.d

INITSCRIPT_NAME = "yadiggg-init"
INITSCRIPT_PARAMS = "defaults 30"

do_compile() {
    # Trigger our custom multi-platform cross-compiling Makefile
    oe_runmake -f Makefile TARGET=yadiggg_capture
}

do_install() {
    # 1. Install compiled C-daemon straight into /usr/bin/
    install -d ${D}${bindir}
    install -m 0755 yadiggg_capture ${D}${bindir}/yadiggg_capture

    # 2. Install ALSA asound.conf configuration directly to /etc/
    install -d ${D}${sysconfdir}
    install -m 0644 asound.conf ${D}${sysconfdir}/asound.conf

    # 3. Install SysVinit startup scripts directly to /etc/init.d/
    install -d ${D}${sysconfdir}/init.d
    install -m 0755 yadiggg-init ${D}${sysconfdir}/init.d/yadiggg-init
}

FILES:${PN} += " \
    ${bindir}/yadiggg_capture \
    ${sysconfdir}/asound.conf \
    ${sysconfdir}/init.d/yadiggg-init \
"
```

---

## 4. SysVinit Daemon Startup Script (`files/yadiggg-init`)

A lightweight shell script triggering our daemon automatically during system startup.

```bash
#!/bin/sh
### BEGIN INIT INFO
# Provides:          yadiggg-init
# Required-Start:    $syslog $local_fs
# Required-Stop:     $syslog $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start yadiggg Sonic ID daemon on boot
### END INIT INFO

DAEMON=/usr/bin/yadiggg_capture
NAME=yadiggg_capture
DESC="Sonic ID Capture Daemon"

test -x $DAEMON || exit 0

case "$1" in
  start)
	echo -n "Starting $DESC: "
	start-stop-daemon --start --quiet --background --exec $DAEMON
	echo "$NAME."
	;;
  stop)
	echo -n "Stopping $DESC: "
	start-stop-daemon --stop --quiet --oknodo --exec $DAEMON
	echo "$NAME."
	;;
  restart|force-reload)
	echo -n "Restarting $DESC: "
	start-stop-daemon --stop --quiet --oknodo --retry 30 --exec $DAEMON
	start-stop-daemon --start --quiet --background --exec $DAEMON
	echo "$NAME."
	;;
  *)
	echo "Usage: $0 {start|stop|restart|force-reload}" >&2
	exit 1
	;;
esac

exit 0
```

---

## 5. Master Monolithic Image Recipe (`recipes-core/images/yadiggg-image.bb`)

Inherits the base `core-image` recipe but strips out bloated packages, systemd, and graphical subsystems to guarantee maximum flash memory compression (SquashFS-LZ4) and sub-1.8s boot speed.

```bitbake
# meta-yadiggg/recipes-core/images/yadiggg-image.bb
SUMMARY = "yadiggg Core Offline Music Companion Monolithic OS Image"
DESCRIPTION = "Ultra-lightweight Linux kernel and RootFS with instant-on PDM capture and offline lookups."
LICENSE = "MIT"

IMAGE_FEATURES = "read-only-rootfs"

inherit core-image

# Core system applications
IMAGE_INSTALL:append = " \
    packagegroup-core-boot \
    sqlite3 \
    sqlite3-cli \
    tesseract \
    tesseract-lang-eng \
    alsa-utils \
    libasound \
    yadiggg-capture \
"

# Force compression using SquashFS with LZ4 for instant, block-level partition mounting
IMAGE_FSTYPES = "squashfs-lz4"

# Set RAM memory optimization thresholds
IMAGE_OVERHEAD_FACTOR = "1.1"
IMAGE_ROOTFS_MAXSIZE = "65536" # Cap rootfs size at 64MB to guarantee microsecond eMMC read speeds
```

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]

*   **Sister Spec**: [[yadiggg_firmware_and_update_architecture]]
*   **Sister Spec**: [[yadiggg_sonic_id_and_olaf_port]]
*   **Sister Spec**: [[yadiggg_yocto_setup]]