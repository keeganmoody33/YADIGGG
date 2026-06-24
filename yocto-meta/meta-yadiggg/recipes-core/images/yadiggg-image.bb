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
