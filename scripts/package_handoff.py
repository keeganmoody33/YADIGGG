#!/usr/bin/env python3
"""Build an auditable review archive and refuse incomplete production releases."""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = Path("manufacturing/release-manifest.json")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
EVIDENCE_SUFFIXES = {
    "electrical-schematic-erc": {".erc", ".kicad_sch", ".rpt"},
    "pcb-layout-drc-fabricator-review": {".drc", ".kicad_pcb", ".zip"},
    "mechanical-geometry-fit-materials-tolerances": {".pdf", ".step", ".stp"},
    "approved-bom-and-substitutions": {".csv"},
    "fabrication-and-assembly-outputs": {".csv", ".drl", ".gbr", ".pdf", ".zip"},
    "firmware-programming-and-recovery": {".bin", ".hex", ".pdf", ".wic"},
    "fixture-functional-test-and-calibration": {".csv", ".json", ".pdf"},
    "packaging-marking-and-traceability": {".pdf", ".svg"},
    "safety-regulatory-assessment-and-approvals": {".json", ".pdf"},
}


class PackageError(Exception):
    pass


def load_manifest(root: Path) -> dict:
    try:
        return json.loads((root / MANIFEST_PATH).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise PackageError(f"cannot read release manifest: {error}") from error


def resolve_repo_file(root: Path, relative_path: str) -> Path:
    candidate = Path(relative_path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise PackageError(f"manifest path must stay inside the repository: {relative_path}")
    root = root.resolve()
    path = root / candidate
    if any((root / Path(*candidate.parts[:index])).is_symlink() for index in range(1, len(candidate.parts) + 1)):
        raise PackageError(f"manifest path must not pass through a symlink: {relative_path}")
    if path.is_symlink() or not path.is_file():
        raise PackageError(f"referenced file is missing or not a regular file: {relative_path}")
    try:
        path.resolve(strict=True).relative_to(root)
    except (OSError, ValueError) as error:
        raise PackageError(f"manifest path resolves outside the repository: {relative_path}") from error
    return path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as content:
        for chunk in iter(lambda: content.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_revision(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise PackageError("a Git checkout with a committed source revision is required")
    return result.stdout.strip()


def ensure_clean_tree(root: Path) -> None:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode or result.stdout.strip():
        raise PackageError("commit all source changes before packaging; the working tree must be clean")


def check_production_release(root: Path, manifest: dict, revision: str) -> list[dict]:
    if manifest.get("production_release_eligible") is not True:
        raise PackageError("production release is blocked: production_release_eligible is not true")
    readiness_path = root / "docs/project-state.md"
    if not readiness_path.is_file():
        raise PackageError("production release is blocked: readiness register is missing")
    readiness_rows = [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in readiness_path.read_text(encoding="utf-8").splitlines()
        if line.lstrip().startswith("|")
    ]
    status_rows = [row for row in readiness_rows if len(row) >= 3 and row[1] in {"Open", "Closed"}]
    if not status_rows or any(row[1] != "Closed" for row in status_rows):
        raise PackageError("production release is blocked: readiness register still has open workstreams")
    evidence_items = manifest.get("required_production_evidence")
    if not isinstance(evidence_items, list) or not evidence_items:
        raise PackageError("production release is blocked: required evidence register is missing")

    validated = []
    for item in evidence_items:
        if not isinstance(item, dict) or item.get("status") != "verified":
            item_id = item.get("id", "<unknown>") if isinstance(item, dict) else "<invalid>"
            raise PackageError(f"production release is blocked: {item_id} is not verified")
        required_roles = [role.strip() for role in item.get("required_role", "").split(" and ") if role.strip()]
        artifacts = item.get("artifacts")
        if not required_roles or not isinstance(artifacts, list) or not artifacts:
            raise PackageError(f"production release is blocked: {item.get('id')} has no evidence artifacts")

        artifact_roles = set()
        for artifact in artifacts:
            if not isinstance(artifact, dict):
                raise PackageError(f"invalid evidence record for {item.get('id')}")
            path_value = artifact.get("path", "")
            path = resolve_repo_file(root, path_value)
            expected_hash = artifact.get("sha256", "")
            if not SHA256_RE.fullmatch(expected_hash) or sha256(path) != expected_hash:
                raise PackageError(f"production evidence checksum missing or incorrect: {path_value}")
            if artifact.get("revision") != revision:
                raise PackageError(f"production evidence revision does not match HEAD: {path_value}")
            allowed_suffixes = EVIDENCE_SUFFIXES.get(item.get("id"), set())
            if path.suffix.lower() not in allowed_suffixes:
                raise PackageError(f"unsupported production evidence artifact type: {path_value}")
            approvals = artifact.get("approvals", [])
            if not isinstance(approvals, list) or not approvals:
                raise PackageError(f"invalid approval record for {path_value}")
            for approval in approvals:
                if not isinstance(approval, dict):
                    raise PackageError(f"invalid approval record for {path_value}")
                approval_path = resolve_repo_file(root, approval.get("path", ""))
                approval_hash = approval.get("sha256", "")
                if not SHA256_RE.fullmatch(approval_hash) or sha256(approval_path) != approval_hash:
                    raise PackageError(f"approval evidence checksum missing or incorrect: {approval.get('path')}")
                if approval.get("revision") != revision:
                    raise PackageError(f"approval evidence revision does not match HEAD: {approval.get('path')}")
                role = approval.get("role")
                if not isinstance(role, str) or not role.strip():
                    raise PackageError(f"approval role missing for {approval.get('path')}")
                artifact_roles.add(role)
                validated.append({"path": approval.get("path"), "sha256": approval_hash})
            validated.append({"path": path_value, "sha256": expected_hash})
        if not set(required_roles).issubset(artifact_roles):
            raise PackageError(f"production release is blocked: required role approvals are missing for {item.get('id')}")
    return validated


def package(root: Path, output: Path, profile: str, require_clean: bool = True) -> Path:
    manifest = load_manifest(root)
    revision = git_revision(root)
    if require_clean:
        ensure_clean_tree(root)

    entries = manifest.get("engineering_review_artifacts")
    if not isinstance(entries, list) or not entries:
        raise PackageError("manifest has no engineering-review artifacts")
    files = []
    seen = set()
    entries = [{"path": str(MANIFEST_PATH), "status": "release-manifest"}, *entries]
    for entry in entries:
        if not isinstance(entry, dict) or not entry.get("status"):
            raise PackageError("each review artifact must include a path and status")
        relative_path = entry.get("path", "")
        if relative_path in seen:
            raise PackageError(f"duplicate manifest path: {relative_path}")
        seen.add(relative_path)
        files.append((relative_path, resolve_repo_file(root, relative_path)))

    if profile == "production-release":
        evidence = check_production_release(root, manifest, revision)
        for record in evidence:
            if record["path"] not in seen:
                files.append((record["path"], resolve_repo_file(root, record["path"])))
                seen.add(record["path"])

    resolved_output = output.resolve()
    try:
        resolved_output.relative_to(root.resolve())
    except ValueError:
        pass
    else:
        raise PackageError("write the package outside the repository working tree")
    if resolved_output.exists():
        raise PackageError(f"refusing to overwrite existing package: {resolved_output}")
    resolved_output.parent.mkdir(parents=True, exist_ok=True)

    status = (
        "PRODUCTION RELEASE"
        if profile == "production-release"
        else "UNRELEASED ENGINEERING REVIEW — NOT FOR PRODUCTION"
    )
    package_manifest = {
        "product": manifest.get("product"),
        "profile": profile,
        "package_status": status,
        "source_revision": revision,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "artifacts": [
            {"path": relative_path, "sha256": sha256(path)}
            for relative_path, path in files
        ],
    }
    with zipfile.ZipFile(resolved_output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative_path, path in files:
            archive.write(path, arcname=relative_path)
        archive.writestr(
            "package-manifest.json",
            json.dumps(package_manifest, indent=2) + "\n",
        )
    return resolved_output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--profile",
        choices=("engineering-review", "production-release"),
        required=True,
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        output = package(ROOT, args.output, args.profile)
    except PackageError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Created {output}")
    if args.profile == "engineering-review":
        print("UNRELEASED: engineering review only; not for production.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
