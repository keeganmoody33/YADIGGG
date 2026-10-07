# yadiggg

`yadiggg` is a pocket field recorder and crate-digging assistant concept. Its intended workflow is to capture a record in a shop or collection and help the listener identify it and explore its music and credits, without relying on a phone during the search.

The current visual concept is portrait-first, with a smoke-clear enclosure, a monochrome display, and an amber side control. The image below is concept art, not a dimensional or manufacturing reference.

![Concept rendering of yadiggg](assets/product/yadiggg-studio-hero.png)

## Intended and implemented

- **Intended:** a portable, one-handed record-discovery workflow with audio identification and optional record-label capture.
- **Prototype:** experimental C audio-fingerprinting/capture code and an unvalidated Yocto layer scaffold.
- **Not implemented or validated:** complete product electronics, camera/OCR, production UI, target-board operation, and a production enclosure. The display, camera, control mechanism, connectors, electronics, and battery remain undecided.

The proposed `105 × 60 × 15 mm` envelope is provisional, not approved geometry. Renderings and the OpenSCAD block model are concepts; the KiCad project is an incomplete scaffold.

## Engineering status

This repository is suitable for engineering review and prototype planning only. It is **not a production release**: the schematic, PCB, enclosure fit, BOM, firmware/OS, assembly outputs, functional testing, and applicable safety/regulatory work remain open. See the [readiness register](docs/project-state.md) and [manufacturer handoff](manufacturing/handoff.md) before using any engineering artifact.

Crate IQ was an earlier product iteration. Its source material is preserved separately in the [archive](archive/README.md); those decisions do not define the current yadiggg design.

## Repository map

| Path | Contents |
|---|---|
| `physical-design/` | Current concept direction, placement notes, and provisional block model |
| `hardware/` | KiCad scaffold and engineering notes |
| `src/sonic_id/` | Canonical experimental C implementation |
| `yocto-meta/` | Yocto layer and application recipe consuming the canonical source |
| `docs/` | Readiness register, ADRs, and engineering notes |
| `data/` | Production SQL schema and separate illustrative demo seed |
| `manufacturing/` | Supplier handoff, draft BOM, and review-package manifest |
| `assets/` | Selected concept art, brand references, and historical visual references |
| `archive/` | Preserved historical source material and migration record |
| `tests/` | Repository-level regression checks |

## Development checks

From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_yocto_layer.py
bash -n yocto-meta/meta-yadiggg/recipes-apps/yadiggg-capture/files/yadiggg-init
```

The Linux ALSA prototype build requires a C compiler, GNU Make, SQLite development files, and ALSA development files. The synthetic-input compile is suitable for host-side source checks only; it does not validate audio hardware:

```sh
make -C src/sonic_id
make -C src/sonic_id clean
make -C src/sonic_id MOCK_CAPTURE=1
make -C src/sonic_id clean
```

For a configured Yocto/BitBake environment with the layer added, the image recipe is `yadiggg-image`. This scaffold has not been verified with BitBake or on target hardware. See [firmware build notes](hardware/yadiggg_yocto_recipe_and_image_build.md).

To create a clearly marked engineering-review bundle (not a production package):

```sh
python3 scripts/package_handoff.py --profile engineering-review --output /tmp/yadiggg-review.zip
```

The `production-release` profile is intentionally blocked until the readiness register and required evidence are complete.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep concept, prototype, validated evidence, and released-for-manufacture status distinct; do not add unverified part selections or fabrication outputs as if approved.
