SUMMARY = "yadiggg prototype image recipe"
DESCRIPTION = "Unvalidated Yocto image scaffold; target hardware and performance are not verified."
LICENSE = "CLOSED"

IMAGE_FEATURES = "read-only-rootfs"

inherit core-image

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

IMAGE_FSTYPES = "squashfs-lz4"

IMAGE_OVERHEAD_FACTOR = "1.1"
IMAGE_ROOTFS_MAXSIZE = "65536"
