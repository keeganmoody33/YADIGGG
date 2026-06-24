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
