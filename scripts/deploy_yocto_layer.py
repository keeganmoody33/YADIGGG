#!/usr/bin/env python3
"""
yadiggg: Yocto Custom Layer & Recipe Deployer
Date: Friday, June 5, 2026
Status: Production Automation Script V1.0

This script automates the layout of our custom 'meta-yadiggg' Yocto BSP overlay layer.
It creates all directory trees, writes the layer config, image recipe, and application recipe,
and copies our tested C-source files, ALSA conf, and Makefile directly into the recipe's
'files/' subdirectory so Bitbake can immediately compile them out-of-the-box.
"""

import os
import shutil

WORKSPACE_DIR = "/Users/keeganmoody/Downloads/YADIGGG"
YOCTO_META_DIR = os.path.join(WORKSPACE_DIR, "yocto-meta")
LAYER_DIR = os.path.join(YOCTO_META_DIR, "meta-yadiggg")

def create_directory_structure():
    directories = [
        os.path.join(LAYER_DIR, "conf"),
        os.path.join(LAYER_DIR, "recipes-core", "images"),
        os.path.join(LAYER_DIR, "recipes-apps", "yadiggg-capture", "files")
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("[DEPLOYER] Created Yocto directory structure.")

def write_layer_conf():
    content = """# meta-yadiggg/conf/layer.conf
# We have a packages directory, add to BBPATH
BBPATH .= ":${LAYERDIR}"

# We have recipes-* directories, add to BBFILES
BBFILES += "${LAYERDIR}/recipes-*/*/*.bb \\
            ${LAYERDIR}/recipes-*/*/*.bbappend"

BBFILE_COLLECTIONS += "meta-yadiggg"
BBFILE_PATTERN_meta-yadiggg = "^${LAYERDIR}/"
BBFILE_PRIORITY_meta-yadiggg = "9"

LAYERSERIES_COMPAT_meta-yadiggg = "scarthgap"

# Enforce immediate build dependency on Freescale and OpenEmbedded core
LAYERDEPENDS_meta-yadiggg = "core freescale-layer openembedded-layer"
"""
    file_path = os.path.join(LAYER_DIR, "conf", "layer.conf")
    with open(file_path, "w") as f:
        f.write(content)
    print(f"[DEPLOYER] Created: {file_path}")

def write_image_recipe():
    content = """# meta-yadiggg/recipes-core/images/yadiggg-image.bb
SUMMARY = "yadiggg Core Offline Music Companion Monolithic OS Image"
DESCRIPTION = "Ultra-lightweight Linux kernel and RootFS with instant-on PDM capture and offline lookups."
LICENSE = "MIT"

IMAGE_FEATURES = "read-only-rootfs"

inherit core-image

# Core system applications
IMAGE_INSTALL:append = " \\
    packagegroup-core-boot \\
    sqlite3 \\
    sqlite3-cli \\
    tesseract \\
    tesseract-lang-eng \\
    alsa-utils \\
    libasound \\
    yadiggg-capture \\
"

# Force compression using SquashFS with LZ4 for instant, block-level partition mounting
IMAGE_FSTYPES = "squashfs-lz4"

# Set RAM memory optimization thresholds
IMAGE_OVERHEAD_FACTOR = "1.1"
IMAGE_ROOTFS_MAXSIZE = "65536" # Cap rootfs size at 64MB to guarantee microsecond eMMC read speeds
"""
    file_path = os.path.join(LAYER_DIR, "recipes-core", "images", "yadiggg-image.bb")
    with open(file_path, "w") as f:
        f.write(content)
    print(f"[DEPLOYER] Created: {file_path}")

def write_app_recipe():
    content = """# meta-yadiggg/recipes-apps/yadiggg-capture/yadiggg-capture_1.0.bb
SUMMARY = "yadiggg Sonic ID PDM Capture & Offline Matching Daemon"
DESCRIPTION = "Cross-compiles the OLAF DSP engine and links with ALSA/SQLite3 for offline record lookups."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

# Build dependencies
DEPENDS = "alsa-lib sqlite3"

# Runtime dependencies
RDEPENDS:${PN} = "libasound sqlite3"

# Source files fetched from local work directories
SRC_URI = " \\
    file://yadiggg_capture.c \\
    file://olaf.c \\
    file://olaf.h \\
    file://Makefile \\
    file://asound.conf \\
    file://yadiggg-init \\
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

FILES:${PN} += " \\
    ${bindir}/yadiggg_capture \\
    ${sysconfdir}/asound.conf \\
    ${sysconfdir}/init.d/yadiggg-init \\
"
"""
    file_path = os.path.join(LAYER_DIR, "recipes-apps", "yadiggg-capture", "yadiggg-capture_1.0.bb")
    with open(file_path, "w") as f:
        f.write(content)
    print(f"[DEPLOYER] Created: {file_path}")

def write_init_script():
    content = """#!/bin/sh
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
"""
    file_path = os.path.join(LAYER_DIR, "recipes-apps", "yadiggg-capture", "files", "yadiggg-init")
    with open(file_path, "w") as f:
        f.write(content)
    print(f"[DEPLOYER] Created: {file_path}")

def copy_source_files():
    src_files = [
        "yadiggg_capture.c",
        "olaf.c",
        "olaf.h",
        "Makefile",
        "asound.conf"
    ]
    src_dir = os.path.join(WORKSPACE_DIR, "src", "sonic_id")
    dest_dir = os.path.join(LAYER_DIR, "recipes-apps", "yadiggg-capture", "files")
    
    for filename in src_files:
        src_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"[DEPLOYER] Copied source file to recipe files: {filename}")
        else:
            print(f"[ERROR] Source file missing: {src_path}")

def main():
    print("==================================================")
    print("📦  YADIGGG custom YOCTO LAYER DEPLOYER DAEMON")
    print("==================================================")
    create_directory_structure()
    write_layer_conf()
    write_image_recipe()
    write_app_recipe()
    write_init_script()
    copy_source_files()
    print("\n🎉 Success! Custom meta-yadiggg layer deployed successfully.")

if __name__ == "__main__":
    main()
