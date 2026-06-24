#!/usr/bin/env python3
"""
yadiggg: KiCad v7 Project, Schematic, and PCB Generator
Date: Friday, June 5, 2026
Status: Production Automation Script V1.0

This script dynamically generates a fully compliant KiCad v7 hardware project
structure for "yadiggg" on disk. It writes:
1. hardware/yadiggg.kicad_pro - JSON project setting up a 4-layer copper stackup.
2. hardware/yadiggg.kicad_sch - Master hierarchical schematic sheet.
3. hardware/yadiggg.kicad_pcb - S-expression layout board with a mathematically 
   filleted 100mm x 55mm Edge.Cuts board outline.
4. Individual hierarchical sub-sheets for Power, Core, Audio, Interfaces, and Wireless.
"""

import os
import json

HARDWARE_DIR = "/Users/keeganmoody/Downloads/YADIGGG/hardware"

def ensure_hardware_dir():
    os.makedirs(HARDWARE_DIR, exist_ok=True)

def generate_kicad_pro():
    """Generates a valid KiCad v7 .kicad_pro JSON project file with a 4-layer stackup configuration."""
    project_data = {
        "meta": {
            "version": 1
        },
        "board": {
            "design_settings": {
                "rules": {
                    "min_track_width": 0.12,
                    "min_via_diameter": 0.4,
                    "min_via_drill": 0.2,
                    "min_microvia_diameter": 0.2,
                    "min_microvia_drill": 0.1,
                    "min_clearance": 0.12
                }
            },
            "layer_stackup": {
                "layers": [
                    {
                        "type": "copper",
                        "name": "F.Cu",
                        "thickness": 0.035,
                        "description": "Top component signal routing layer"
                    },
                    {
                        "type": "dielectric",
                        "name": "Prepreg",
                        "thickness": 0.1,
                        "material": "FR4",
                        "epsilon_r": 4.2
                    },
                    {
                        "type": "copper",
                        "name": "In1.Cu",
                        "thickness": 0.035,
                        "description": "Internal 1 solid ground plane (split digital/analog)"
                    },
                    {
                        "type": "dielectric",
                        "name": "Core",
                        "thickness": 0.8,
                        "material": "FR4",
                        "epsilon_r": 4.5
                    },
                    {
                        "type": "copper",
                        "name": "In2.Cu",
                        "thickness": 0.035,
                        "description": "Internal 2 power plane grid"
                    },
                    {
                        "type": "dielectric",
                        "name": "Prepreg2",
                        "thickness": 0.1,
                        "material": "FR4",
                        "epsilon_r": 4.2
                    },
                    {
                        "type": "copper",
                        "name": "B.Cu",
                        "thickness": 0.035,
                        "description": "Bottom low-speed signal and quiet audio analog routing layer"
                    }
                ]
            }
        },
        "schematic": {
            "meta": {
                "version": 1
            }
        }
    }
    
    file_path = os.path.join(HARDWARE_DIR, "yadiggg.kicad_pro")
    with open(file_path, "w") as f:
        json.dump(project_data, f, indent=2)
    print(f"[GENERATOR] Created KiCad project file: {file_path}")

def generate_kicad_pcb():
    """
    Generates a valid KiCad v7 S-expression board layout with a closed loop 100mm x 55mm rounded rectangle 
    on the Edge.Cuts layer (6.0mm corner fillet radius) centered at (150, 127.5).
    """
    # Coordinates mapping a 100mm x 55mm board:
    # Top-Left: (100, 100), Bottom-Right: (200, 155)
    # With 6.0mm fillet:
    # Corner Arcs center points:
    # TL: (106, 106), TR: (194, 106), BR: (194, 149), BL: (106, 149)
    pcb_content = """(kicad_pcb (version 20211014) (generator pcbnew)

  (general
    (thickness 1.2)
  )

  (paper "A4")

  (layers
    (0 "F.Cu" signal)
    (1 "In1.Cu" power)
    (2 "In2.Cu" power)
    (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive")
    (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user)
    (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen")
    (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user)
    (39 "F.Mask" user)
    (40 "Dwgs.User" user "User.Drawings")
    (41 "Cmts.User" user "Comments")
    (42 "Eco1.User" user "Eco1")
    (43 "Eco2.User" user "Eco2")
    (44 "Edge.Cuts" user)
    (45 "Margin" user)
    (46 "B.CrtYd" user "B.Courtyard")
    (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user)
    (49 "F.Fab" user)
  )

  (setup
    (pad_to_mask_clearance 0.05)
    (pcb_text_size 1.5 1.5)
    (pcb_text_thickness 0.3)
    (pad_size 1.5 1.5)
    (pad_drill 0.8)
  )

  # Closed Edge.Cuts Outline: Rounded Rectangle (100mm x 55mm) with a 6mm Corner Fillet
  # Top straight segment
  (gr_line (start 106 100) (end 194 100) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-top"))
  # Top-Right corner arc (centered at 194, 106; arc from (194, 100) to (200, 106))
  (gr_arc (start 194 106) (mid 198.243 101.757) (end 200 106) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-tr-arc"))
  # Right straight segment
  (gr_line (start 200 106) (end 200 149) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-right"))
  # Bottom-Right corner arc (centered at 194, 149; arc from (200, 149) to (194, 155))
  (gr_arc (start 194 149) (mid 198.243 153.243) (end 194 155) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-br-arc"))
  # Bottom straight segment
  (gr_line (start 194 155) (end 106 155) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-bottom"))
  # Bottom-Left corner arc (centered at 106, 149; arc from (106, 155) to (100, 149))
  (gr_arc (start 106 149) (mid 101.757 153.243) (end 100 149) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-bl-arc"))
  # Left straight segment
  (gr_line (start 100 149) (end 100 106) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-left"))
  # Top-Left corner arc (centered at 106, 106; arc from (100, 106) to (106, 100))
  (gr_arc (start 106 106) (mid 101.757 101.757) (end 106 100) (layer "Edge.Cuts") (width 0.1) (tstamp "outline-tl-arc"))

  # Ground Planes Split Isolation Markers (Visual aid on User.Comments layer)
  (gr_line (start 160 100) (end 160 155) (layer "Cmts.User") (width 0.15) (tstamp "gnd-split-comment"))
  (gr_text "1.0mm split plane split: GND_DIG to the Left / GND_ANA to the Right" (at 150 127.5 90) (layer "Cmts.User")
    (effects (font (size 1.2 1.2) (thickness 0.2)))
    (tstamp "gnd-split-text")
  )
)
"""
    file_path = os.path.join(HARDWARE_DIR, "yadiggg.kicad_pcb")
    with open(file_path, "w") as f:
        f.write(pcb_content)
    print(f"[GENERATOR] Created KiCad board layout: {file_path}")

def generate_kicad_sch_sheets():
    """Generates the main hierarchical master schematic and the five logical subsheets."""
    # Master schematic linking our 5 hierarchical sheets
    master_content = """(kicad_sch (version 20211123) (generator eeschema)

  (paper "A3")

  (title_block
    (title "yadiggg Companion: Master Hierarchical Schematic")
    (company "yadiggg Engineering Suite")
    (rev "V1.0")
    (date "Friday, June 5, 2026")
  )

  # Sheet 1: Power & Battery Management
  (sheet (at 20 40) (size 60 40) (fields_autoplaced)
    (uuid "sheet-power-uuid")
    (property "Name" "Power & Battery Management" (id 0) (at 20 38 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
    (property "File" "yadiggg_power.kicad_sch" (id 1) (at 20 82 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
  )

  # Sheet 2: Core Processing & Storage (i.MX 8M Nano)
  (sheet (at 100 40) (size 60 40) (fields_autoplaced)
    (uuid "sheet-core-uuid")
    (property "Name" "Core Processing & Storage" (id 0) (at 100 38 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
    (property "File" "yadiggg_core.kicad_sch" (id 1) (at 100 82 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
  )

  # Sheet 3: High-Fidelity Audio & Mics
  (sheet (at 20 100) (size 60 40) (fields_autoplaced)
    (uuid "sheet-audio-uuid")
    (property "Name" "High-Fidelity Audio & Capture" (id 0) (at 20 98 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
    (property "File" "yadiggg_audio.kicad_sch" (id 1) (at 20 142 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
  )

  # Sheet 4: Displays, Interfaces, and Haptics
  (sheet (at 100 100) (size 60 40) (fields_autoplaced)
    (uuid "sheet-interface-uuid")
    (property "Name" "Displays, Interfaces & Haptics" (id 0) (at 100 98 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
    (property "File" "yadiggg_interface.kicad_sch" (id 1) (at 100 142 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
  )

  # Sheet 5: Wireless Sync RF Module
  (sheet (at 60 160) (size 60 40) (fields_autoplaced)
    (uuid "sheet-wireless-uuid")
    (property "Name" "Wireless RF Module" (id 0) (at 60 158 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
    (property "File" "yadiggg_wireless.kicad_sch" (id 1) (at 60 202 0)
      (effects (font (size 1.5 1.5) (thickness 0.3)) (justify left))
    )
  )
)
"""
    master_path = os.path.join(HARDWARE_DIR, "yadiggg.kicad_sch")
    with open(master_path, "w") as f:
        f.write(master_content)
    print(f"[GENERATOR] Created master KiCad schematic: {master_path}")

    # Generate the dummy empty sub-sheets so they can be opened immediately by KiCad
    sub_sheets = [
        "yadiggg_power.kicad_sch",
        "yadiggg_core.kicad_sch",
        "yadiggg_audio.kicad_sch",
        "yadiggg_interface.kicad_sch",
        "yadiggg_wireless.kicad_sch"
    ]
    
    for filename in sub_sheets:
        sub_content = f"""(kicad_sch (version 20211123) (generator eeschema)
  (paper "A3")
  (title_block
    (title "yadiggg Sub-Module: {filename.split('.')[0].replace('_', ' ').title()}")
    (company "yadiggg Engineering Suite")
    (rev "V1.0")
    (date "Friday, June 5, 2026")
  )
)
"""
        sub_path = os.path.join(HARDWARE_DIR, filename)
        with open(sub_path, "w") as f:
            f.write(sub_content)
        print(f"[GENERATOR] Instantiated sub-sheet: {sub_path}")

def main():
    print("==================================================")
    print("🚀  KICAD V7 DESIGN TEMPLATE GENERATION DAEMON")
    print("==================================================")
    ensure_hardware_dir()
    generate_kicad_pro()
    generate_kicad_pcb()
    generate_kicad_sch_sheets()
    print("\n🎉 Success! KiCad Project initiated successfully in /hardware/ directory.")

if __name__ == "__main__":
    main()
