#!/usr/bin/env bash
# yadiggg: Official Yocto Embedded Linux Setup Script
# Configures the build environment for NXP i.MX 8M Nano SoC
# Optimized for sub-2s cold-boot latency and monolithic kernel architecture.
# Date: June 3, 2026
# Version: V1.0

set -euo pipefail

echo "===================================================================="
echo "Initializing yadiggg Yocto BSP Build Configuration Environment"
echo "Target Platform: NXP i.MX 8M Nano SoC (Cortex-A53 Quad + Cortex-M7)"
echo "===================================================================="

# 1. DEFINE WORKSPACE PATHS
YOCTO_DIR="${HOME}/yadiggg-yocto"
BUILD_DIR="${YOCTO_DIR}/build"
CONF_FILE="${BUILD_DIR}/conf/local.conf"
BBLAYERS_FILE="${BUILD_DIR}/conf/bblayers.conf"

mkdir -p "${YOCTO_DIR}"
cd "${YOCTO_DIR}"

# 2. CLONE POKY AND ESSENTIAL METADATA LAYERS (Scarthgap release)
echo "[INFO] Cloning Yocto Core and BSP Layers (Release: Scarthgap)..."
git clone -b scarthgap git://git.yoctoproject.org/poky.git poky_repo || true
git clone -b scarthgap https://github.com/Freescale/meta-freescale.git meta-freescale_repo || true
git clone -b scarthgap https://github.com/openembedded/meta-openembedded.git meta-openembedded_repo || true

# 3. INITIALIZE TEMPLATE BUILD ENVIRONMENT
echo "[INFO] Sourcing build environment setup..."
# Poky's oe-init-build-env script initializes the build directory
source poky_repo/oe-init-build-env "${BUILD_DIR}"

# 4. CONFIGURING LOCAL.CONF (Optimized for boot speed and stripped kernel footprint)
echo "[INFO] Modifying local.conf with custom yadiggg configurations..."
cat << 'EOF' > "${CONF_FILE}"
# yadiggg Build Configurations

# Define Target Machine (BSP support for i.MX 8M Nano EVK)
MACHINE = "imx8mn-evk"

# Distro configuration - custom minimal configuration
DISTRO = "poky"

# Strip all non-essential packages and package groups
IMAGE_FEATURES = "read-only-rootfs"

# Remove heavy system features to reduce memory overhead and boot delays
DISTRO_FEATURES:remove = "x11 wayland vulkan opengl 3g bluez nfc systemd-resolved"
DISTRO_FEATURES:append = " alsa pam"

# Use SysVinit instead of Systemd to optimize boot-to-init speed
DISTRO_FEATURES_BACKFILL_CONSIDERED = "systemd"
VIRTUAL-RUNTIME_init_manager = "sysvinit"

# Strip build down to custom lightweight target packages
IMAGE_INSTALL:append = " \
    sqlite3 \
    sqlite3-cli \
    tesseract \
    tesseract-lang-eng \
    alsa-utils \
    libasound \
"

# Compression setup - LZ4 SquashFS is used for instant partition mounting
IMAGE_FSTYPES = "squashfs-lz4"

# Optimizing compiler flags for ARM Cortex-A53 cores (optimize for size and speed)
EXTRA_OEMAKE:append = " -Os"
EOF

# 5. CONFIGURING BBLAYERS.CONF
echo "[INFO] Registering meta-layers in bblayers.conf..."
cat << EOF > "${BBLAYERS_FILE}"
# POKY_BBLAYERS_CONF_VERSION is increased when bblayers.conf format changes
POKY_BBLAYERS_CONF_VERSION = "2"

BBPATH = "\${TOPDIR}"
BBFILES ?= ""

BBLAYERS ?= " \\
  ${YOCTO_DIR}/poky_repo/meta \\
  ${YOCTO_DIR}/poky_repo/meta-poky \\
  ${YOCTO_DIR}/poky_repo/meta-yocto-bsp \\
  ${YOCTO_DIR}/meta-freescale_repo \\
  ${YOCTO_DIR}/meta-openembedded_repo/meta-oe \\
  ${YOCTO_DIR}/meta-openembedded_repo/meta-multimedia \\
"
EOF

# 6. EXPLAINING KERNEL DEFCONFIG FOR SUB-2S BOOT (Stripped monolithic kernel)
echo "[SUCCESS] Base configs generated successfully in: ${BUILD_DIR}/conf/"
echo ""
echo "===================================================================="
echo "yadiggg Kernel defconfig Stripping Guide:"
echo "===================================================================="
echo "To achieve a <1.8s cold boot, you MUST strip the Linux kernel."
echo "Modify: meta-freescale/recipes-kernel/linux/files/imx8mn_defconfig"
echo ""
echo "1. Disable Virtual Filesystem features you do not need:"
echo "   # CONFIG_NTFS_FS is not set"
echo "   # CONFIG_MSDOS_FS is not set"
echo ""
echo "2. Compile drivers MONOLITHICALLY (no modprobe overhead):"
echo "   CONFIG_MMC_SDHCI_ESDHC_IMX=y"
echo "   CONFIG_SPI_IMX=y"
echo "   CONFIG_I2C_IMX=y"
echo "   CONFIG_SND_SOC_IMX_ES9218=y"
echo "   CONFIG_SND_SOC_KNOWLES_PDM=y"
echo ""
echo "3. Strip all unused subsystems (Network, USB, Graphics):"
echo "   # CONFIG_NET is not set           <-- Completely removes IP stack"
echo "   # CONFIG_USB_SUPPORT is not set   <-- Disable USB host (M7 handles USB client)"
echo "   # CONFIG_DRM is not set           <-- Bypasses graphic framework overhead"
echo "===================================================================="
EOF
chmod +x "${YOCTO_DIR}/yadiggg_yocto_setup.sh" || true
