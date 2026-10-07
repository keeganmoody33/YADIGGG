#!/usr/bin/env python3
"""Check that the checked-in Yocto recipe uses the canonical repository sources."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
LAYER = ROOT / "yocto-meta" / "meta-yadiggg"
RECIPE = LAYER / "recipes-apps" / "yadiggg-capture" / "yadiggg-capture_1.0.bb"
SOURCE = ROOT / "src" / "sonic_id"
SOURCE_FILES = ("yadiggg_capture.c", "olaf.c", "olaf.h", "Makefile", "asound.conf")


def validate() -> list[str]:
    errors = []
    recipe = RECIPE.read_text(encoding="utf-8") if RECIPE.is_file() else ""
    expected_search_path = "${THISDIR}/../../../../src/sonic_id:"
    if expected_search_path not in recipe:
        errors.append("recipe does not stage source/sonic_id through FILESEXTRAPATHS")
    for filename in SOURCE_FILES:
        if not (SOURCE / filename).is_file():
            errors.append(f"missing canonical source: src/sonic_id/{filename}")
        if f"file://{filename}" not in recipe:
            errors.append(f"recipe does not request {filename}")
        if (LAYER / "recipes-apps" / "yadiggg-capture" / "files" / filename).exists():
            errors.append(f"duplicate maintained recipe copy exists: {filename}")
    if not (LAYER / "recipes-apps" / "yadiggg-capture" / "files" / "yadiggg-init").is_file():
        errors.append("missing recipe-local yadiggg-init")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("Yocto recipe source staging is consistent; no files were written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
