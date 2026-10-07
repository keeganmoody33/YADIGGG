import ast
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RepositoryChecks(unittest.TestCase):
    def test_local_markdown_links_resolve(self):
        link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
        failures = []
        for markdown in ROOT.rglob("*.md"):
            if ".git" in markdown.parts or "historical-proposals" in markdown.parts:
                continue
            text = markdown.read_text(encoding="utf-8")
            for raw_target in link_pattern.findall(text):
                target = raw_target.strip().split()[0].strip("<>")
                if not target or target.startswith(("#", "http:", "https:", "mailto:")):
                    continue
                target = target.split("#", 1)[0].split("?", 1)[0]
                if not target:
                    continue
                resolved = (markdown.parent / target).resolve()
                if not resolved.exists():
                    failures.append(f"{markdown.relative_to(ROOT)} -> {target}")
        self.assertEqual(failures, [])

    def test_python_sources_parse(self):
        for source in (ROOT / "scripts").glob("*.py"):
            with self.subTest(source=source.name):
                ast.parse(source.read_text(encoding="utf-8"), filename=str(source))

    def test_recipe_uses_only_canonical_source_tree(self):
        validator = load_script("validate_yocto_layer")
        self.assertEqual(validator.validate(), [])

    def test_schema_is_separate_from_demo_seed(self):
        connection = sqlite3.connect(":memory:")
        connection.executescript((ROOT / "data/schema.sql").read_text(encoding="utf-8"))
        self.assertEqual(connection.execute("SELECT count(*) FROM releases").fetchone()[0], 0)
        connection.executescript((ROOT / "data/demo/seed.sql").read_text(encoding="utf-8"))
        self.assertEqual(connection.execute("SELECT count(*) FROM releases").fetchone()[0], 1)
        self.assertEqual(connection.execute("SELECT count(*) FROM track_fingerprints").fetchone()[0], 1)
        connection.close()

    def test_draft_bom_has_traceable_unverified_candidates(self):
        with (ROOT / "manufacturing/draft-bom.csv").open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source))
        self.assertTrue(rows)
        for row in rows:
            self.assertEqual(row["record_type"], "candidate")
            self.assertEqual(row["verification_status"], "unverified-proposal")
            for provenance in row["provenance"].split("; "):
                with self.subTest(provenance=provenance):
                    self.assertTrue((ROOT / provenance).is_file())

    def test_confirmed_duplicate_renders_and_build_outputs_stay_removed(self):
        duplicate_assets = [
            ROOT / "assets/reference/A2c312300cbc241a593033cc604f7deb5N (1).png",
            ROOT / "archive/rendered-pages/Ya Diggg Advanced Specs (1)_p1.png",
            ROOT / "archive/rendered-pages/Ya Diggg Advanced Specs (1)_p2.png",
            ROOT / "archive/rendered-pages/Ya Diggg Sonic Id Spec (1)_p1.png",
        ]
        generated_outputs = [
            ROOT / "src/sonic_id/olaf.o",
            ROOT / "src/sonic_id/yadiggg_capture.o",
            ROOT / "src/sonic_id/yadiggg_capture",
            ROOT / "yadiggg_capture",
            ROOT / "hardware/yadiggg.kicad_prl",
        ]
        for path in duplicate_assets + generated_outputs:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertFalse(path.exists())

    def test_shell_init_script_syntax(self):
        bash = shutil.which("bash")
        if not bash:
            self.skipTest("bash is unavailable")
        init_script = ROOT / "yocto-meta/meta-yadiggg/recipes-apps/yadiggg-capture/files/yadiggg-init"
        subprocess.run([bash, "-n", str(init_script)], check=True)

    def test_synthetic_input_c_build(self):
        if not shutil.which("make") or not shutil.which("gcc") or not Path("/usr/include/sqlite3.h").is_file():
            self.skipTest("make, gcc, or SQLite development headers are unavailable")
        try:
            subprocess.run(
                ["make", "-C", str(ROOT / "src/sonic_id"), "MOCK_CAPTURE=1"],
                check=True,
                capture_output=True,
                text=True,
            )
        finally:
            subprocess.run(
                ["make", "-C", str(ROOT / "src/sonic_id"), "clean"],
                check=True,
                capture_output=True,
                text=True,
            )

    def test_kicad_generator_refuses_to_overwrite_existing_files(self):
        generator = ROOT / "scripts/generate_kicad_project.py"
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "hardware"
            command = [sys.executable, str(generator), "--output-dir", str(output_dir)]
            subprocess.run(command, check=True, capture_output=True, text=True)
            project = output_dir / "yadiggg.kicad_pro"
            project.write_text("hand-authored\n", encoding="utf-8")
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(project.read_text(encoding="utf-8"), "hand-authored\n")

    def test_review_package_records_revision_and_checksums(self):
        packager = load_script("package_handoff")
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "review.zip"
            packager.package(ROOT, output, "engineering-review", require_clean=False)
            with zipfile.ZipFile(output) as bundle:
                names = bundle.namelist()
                self.assertIn("package-manifest.json", names)
                self.assertNotIn("archive/README.md", names)
                self.assertFalse(any(name.endswith(".o") for name in names))
                package_manifest = json.loads(bundle.read("package-manifest.json"))
                self.assertEqual(package_manifest["source_revision"], packager.git_revision(ROOT))
                self.assertEqual(
                    package_manifest["package_status"],
                    "UNRELEASED ENGINEERING REVIEW — NOT FOR PRODUCTION",
                )
                for artifact in package_manifest["artifacts"]:
                    digest = hashlib.sha256(bundle.read(artifact["path"])).hexdigest()
                    self.assertEqual(digest, artifact["sha256"])

    def test_production_package_fails_closed_on_current_register(self):
        packager = load_script("package_handoff")
        manifest = packager.load_manifest(ROOT)
        with self.assertRaisesRegex(packager.PackageError, "production_release_eligible"):
            packager.check_production_release(ROOT, manifest, packager.git_revision(ROOT))

    def test_populated_status_template_without_evidence_still_fails(self):
        packager = load_script("package_handoff")
        manifest = packager.load_manifest(ROOT)
        manifest["production_release_eligible"] = True
        for item in manifest["required_production_evidence"]:
            item["status"] = "verified"
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "docs").mkdir()
            (root / "docs/project-state.md").write_text(
                "| Workstream | Status | Evidence |\n|---|---|---|\n"
                "| Electrical | Closed | No evidence supplied |\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(packager.PackageError, "no evidence artifacts"):
                packager.check_production_release(root, manifest, "revision")


if __name__ == "__main__":
    unittest.main()
