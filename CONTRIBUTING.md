# Contributing

Before proposing changes:

1. Read the [product specification](physical-design/final-product-source-of-truth.md), [readiness register](docs/project-state.md), and relevant ADRs.
2. Run `python3 -m unittest discover -s tests -v` and `python3 scripts/validate_yocto_layer.py`.
3. Keep source files canonical; do not copy maintained firmware into the Yocto recipe.
4. Record provenance and verification state for new parts or engineering evidence. Never promote proposal data to an approved BOM without engineering review.
5. Label concept, prototype, and measured results accurately. Do not add mock Gerbers, STEP, approvals, or test results.

No project-wide license or redistribution permission is established in this repository. Confirm licensing and attribution before adding or distributing third-party material.
