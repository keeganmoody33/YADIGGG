SUMMARY = "yadiggg experimental audio-capture prototype"
DESCRIPTION = "Unvalidated prototype capture application; not a production firmware image."
LICENSE = "CLOSED"

DEPENDS = "alsa-lib sqlite3"
RDEPENDS:${PN} = "alsa-lib sqlite3"

# Keep the repository's native source as the only maintained copy.
FILESEXTRAPATHS:prepend := "${THISDIR}/../../../../src/sonic_id:"
SRC_URI = " \
    file://yadiggg_capture.c \
    file://olaf.c \
    file://olaf.h \
    file://Makefile \
    file://asound.conf \
    file://yadiggg-init \
"

S = "${WORKDIR}"

inherit update-rc.d

INITSCRIPT_NAME = "yadiggg-init"
INITSCRIPT_PARAMS = "defaults 30"

do_compile() {
    oe_runmake -f Makefile
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 yadiggg_capture ${D}${bindir}/yadiggg_capture

    install -d ${D}${sysconfdir}
    install -m 0644 asound.conf ${D}${sysconfdir}/asound.conf

    install -d ${D}${sysconfdir}/init.d
    install -m 0755 yadiggg-init ${D}${sysconfdir}/init.d/yadiggg-init
}

FILES:${PN} += " \
    ${bindir}/yadiggg_capture \
    ${sysconfdir}/asound.conf \
    ${sysconfdir}/init.d/yadiggg-init \
"
