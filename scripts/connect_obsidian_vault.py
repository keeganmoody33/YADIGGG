#!/usr/bin/env python3
"""
yadiggg: Obsidian Vault Inter-Connector Daemon
Date: Monday, June 8, 2026
Status: Production Automation Script V1.0

This script automatically scans all markdown (.md) files in the yadiggg workspace.
It injects a standardized YAML frontmatter block and a 'Related Specifications' 
backlink section at the bottom of each file. 

This weaves a tight, highly-connected semantic web, fully resolving isolated 
nodes (yellow dots) in the Obsidian Graph View!
"""

import os
import re

WORKSPACE_DIR = "/Users/keeganmoody/Downloads/YADIGGG"

# Mapping of file paths/names to categories and relevant sister documents
SISTER_LINKS = {
    # Brand and Product
    "yadiggg_brand_identity_and_design_guidelines.md": [
        "yadiggg_product_and_interaction_architecture.md",
        "yadiggg_hardware_and_electrical_integration.md"
    ],
    "yadiggg_product_and_interaction_architecture.md": [
        "yadiggg_brand_identity_and_design_guidelines.md",
        "yadiggg_firmware_and_update_architecture.md"
    ],
    
    # Hardware and Layout
    "yadiggg_hardware_and_electrical_integration.md": [
        "hardware/yadiggg_pcba_v1_layout_guidelines.md",
        "docs/component-selections.md",
        "docs/schematic-status.md"
    ],
    "yadiggg_pcba_v1_layout_guidelines.md": [
        "yadiggg_hardware_and_electrical_integration.md",
        "docs/component-selections.md",
        "docs/schematic-status.md",
        "yadiggg_pinmux.md",
        "yadiggg_audio_dac_and_mic_schematics.md"
    ],
    "yadiggg_pinmux.md": [
        "yadiggg_hardware_and_electrical_integration.md",
        "yadiggg_audio_dac_and_mic_schematics.md",
        "yadiggg_pcba_v1_layout_guidelines.md"
    ],
    "yadiggg_audio_dac_and_mic_schematics.md": [
        "yadiggg_hardware_and_electrical_integration.md",
        "yadiggg_pinmux.md",
        "yadiggg_pcba_v1_layout_guidelines.md"
    ],
    "component-selections.md": [
        "yadiggg_hardware_and_electrical_integration.md",
        "schematic-status.md",
        "yadiggg_pcba_v1_layout_guidelines.md"
    ],
    "schematic-status.md": [
        "yadiggg_hardware_and_electrical_integration.md",
        "component-selections.md",
        "yadiggg_pcba_v1_layout_guidelines.md"
    ],

    # Firmware and DSP Code
    "yadiggg_firmware_and_update_architecture.md": [
        "yadiggg_product_and_interaction_architecture.md",
        "yadiggg_hardware_and_electrical_integration.md",
        "hardware/yadiggg_sonic_id_and_olaf_port.md",
        "hardware/yadiggg_yocto_recipe_and_image_build.md"
    ],
    "yadiggg_sonic_id_and_olaf_port.md": [
        "yadiggg_firmware_and_update_architecture.md",
        "yadiggg_yocto_recipe_and_image_build.md",
        "yadiggg_audio_dac_and_mic_schematics.md"
    ],
    "yadiggg_yocto_recipe_and_image_build.md": [
        "yadiggg_firmware_and_update_architecture.md",
        "yadiggg_sonic_id_and_olaf_port.md",
        "yadiggg_yocto_setup.sh" # reference link
    ],

    # QA and Test
    "yadiggg_adversarial_testing_and_validation_protocol.md": [
        "yadiggg_firmware_and_update_architecture.md",
        "yadiggg_hardware_and_electrical_integration.md",
        "yadiggg_schema.sql"
    ]
}

def get_clean_wikilink_path(filepath):
    """Formats raw filepaths to clean, relative Obsidian wiki-links (e.g. [[hardware/yadiggg_pinmux]] or [[yadiggg_brand]])"""
    # Remove workspace root
    rel_path = os.path.relpath(filepath, WORKSPACE_DIR)
    # Strip extension
    base, ext = os.path.splitext(rel_path)
    # Standardize path separators to forward slash
    return base.replace("\\", "/")

def get_markdown_files():
    md_files = []
    for root, dirs, files in os.walk(WORKSPACE_DIR):
        # Ignore hidden/git directories and node_modules
        if any(ignored in root for cls in [".git", ".accio", "node_modules", "poky_repo", "yocto_meta"] for ignored in [cls]):
            continue
        for file in files:
            if file.endswith(".md") and file != "CONTEXT.md" and file != "yadiggg_vault_overview.md":
                md_files.append(os.path.join(root, file))
    return md_files

def inject_obsidian_infrastructure(filepath):
    """Parses a markdown file, adds YAML frontmatter at the top, and backlink section at the bottom."""
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. CLEAN EXISTING FRONTMATTER AND FOOTERS TO ENABLE IDEMPOTENT RUNS
    # Strip existing frontmatter block if it exists
    content = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)
    # Strip existing backlinks footer block if it exists
    content = re.sub(r"\n\n---\n\n## 🕸️ Related Specifications and Backlinks.*$", "", content, flags=re.DOTALL)
    content = content.strip()

    # Extract first header as title fallback
    header_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = header_match.group(1).strip() if header_match else filename.split(".")[0].replace("_", " ").title()

    # 2. CONSTRUCT NEW YAML FRONTMATTER
    frontmatter = f"""---
title: "{title}"
project: yadiggg
status: completed
type: system_specification
tags: [yadiggg, system_engineering, modular_design]
backlinks:
  - "[[yadiggg_vault_overview]]"
  - "[[CONTEXT]]"
---
"""

    # 3. CONSTRUCT RELATED SISTER BACKLINKS FOOTER
    sister_wikilinks = []
    
    # Try finding mapped connections based on matching either filename or partial path
    matched_key = None
    for key in SISTER_LINKS:
        if filename == key or filename == os.path.basename(key):
            matched_key = key
            break

    if matched_key:
        for sister in SISTER_LINKS[matched_key]:
            sister_base = os.path.splitext(sister)[0]
            sister_wikilinks.append(f"*   **Sister Spec**: [[{sister_base}]]")

    # Always backlink to the Core Glossary and Vault Dashboard MOC
    backlinks_footer = f"""

---

## 🕸️ Related Specifications and Backlinks
*   **Glossary & Core Domain Language**: [[CONTEXT]]
*   **Main Vault Dashboard (MOC)**: [[yadiggg_vault_overview]]
"""
    if sister_wikilinks:
        backlinks_footer += "\n" + "\n".join(sister_wikilinks)

    # 4. WRITE UPDATED SECURELY BACK TO DISK
    updated_content = frontmatter + "\n" + content + backlinks_footer
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print(f"[OBSIDIAN] Fully linked & formatted node: {filename}")

def main():
    print("==================================================")
    print("🕸️  YADIGGG OBSIDIAN GRAPH VIEW CONNECTOR DAEMON")
    print("==================================================")
    
    md_files = get_markdown_files()
    print(f"[INFO] Identified {len(md_files)} markdown files in vault.")
    
    for filepath in md_files:
        inject_obsidian_infrastructure(filepath)
        
    print("\n🎉 Success! Every node has been systematically backlinked and categorized.")
    print("[INFO] Open Obsidian Graph View to see your connected system mapping spiderweb!")

if __name__ == "__main__":
    main()
