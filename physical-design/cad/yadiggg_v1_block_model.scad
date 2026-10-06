// yadiggg V1 Block Model
// Status: active-draft / spatial proof only
// Units: millimeters
// Source: physical-design/cad-block-model-brief.md
//
// This is NOT production CAD. It is a fast parametric block model for
// checking the canonical 105 x 60 x 15mm-class visual/mechanical envelope.

$fn = 48;

// -----------------------------
// Global parameters
// -----------------------------
body_w = 60;
body_h = 105;
body_d = 15;
corner_r = 6;
shell_alpha = 0.36;

// Front features
display_w = 48;
display_h = 38;
display_y = 22;
display_bezel = 2;
display_depth = 0.6;

// Internal blocks
pcba_w = 52;
pcba_h = 86;
pcba_d = 1.6;
battery_w = 38;
battery_h = 48;
battery_d = 5;

// Side control
control_w = 2.2;
control_h = 22;
control_d = 7;
control_y = 12;

// Back camera
camera_dia = 7;
camera_y = 25;

// Ports
usb_w = 9.5;
usb_h = 3.5;
jack_dia = 6.5;

// -----------------------------
// Helpers
// -----------------------------
module rounded_box(w, h, d, r) {
    linear_extrude(height=d, center=true)
        hull() {
            translate([ w/2-r,  h/2-r]) circle(r=r);
            translate([-w/2+r,  h/2-r]) circle(r=r);
            translate([ w/2-r, -h/2+r]) circle(r=r);
            translate([-w/2+r, -h/2+r]) circle(r=r);
        }
}

module rounded_rect_panel(w, h, t, r) {
    linear_extrude(height=t, center=true)
        hull() {
            translate([ w/2-r,  h/2-r]) circle(r=r);
            translate([-w/2+r,  h/2-r]) circle(r=r);
            translate([ w/2-r, -h/2+r]) circle(r=r);
            translate([-w/2+r, -h/2+r]) circle(r=r);
        }
}

// -----------------------------
// Main shell
// -----------------------------
module body_shell() {
    color([0.18, 0.20, 0.20, shell_alpha])
        rounded_box(body_w, body_h, body_d, corner_r);
}

module display_assembly() {
    // black bezel
    color([0.02, 0.02, 0.02, 1.0])
        translate([0, display_y, body_d/2 + 0.15])
            rounded_rect_panel(display_w + display_bezel*2, display_h + display_bezel*2, display_depth, 2.5);

    // LCD face
    color([0.78, 0.82, 0.74, 1.0])
        translate([0, display_y, body_d/2 + 0.5])
            rounded_rect_panel(display_w, display_h, 0.25, 1.5);

    // simple waveform placeholder
    color([0.02, 0.02, 0.02, 1.0])
        translate([0, display_y, body_d/2 + 0.66])
            cube([34, 0.6, 0.1], center=true);
}

module internal_blocks() {
    // main PCBA
    color([0.02, 0.16, 0.08, 0.75])
        translate([0, -5, 1.0])
            cube([pcba_w, pcba_h, pcba_d], center=true);

    // lower shield zone
    color([0.03, 0.03, 0.03, 0.85])
        translate([-10, -24, 3.5])
            cube([24, 24, 2.0], center=true);

    // battery rear/lower volume
    color([0.12, 0.12, 0.12, 0.70])
        translate([8, -25, -3.6])
            cube([battery_w, battery_h, battery_d], center=true);
}

module side_control() {
    color([1.0, 0.55, 0.05, 1.0])
        translate([body_w/2 + 0.35, control_y, 0])
            rotate([90, 0, 0])
                rounded_rect_panel(control_d, control_w, control_h, 1.2);
}

module rear_camera() {
    color([0.01, 0.01, 0.01, 1.0])
        translate([0, camera_y, -body_d/2 - 0.15])
            cylinder(h=0.5, d=camera_dia, center=true);
}

module mic_ports() {
    color([0.01, 0.01, 0.01, 1.0]) {
        translate([-4, body_h/2 - 8, -body_d/2 - 0.15]) cylinder(h=0.45, d=1.0, center=true);
        translate([0, body_h/2 - 8, -body_d/2 - 0.15]) cylinder(h=0.45, d=1.0, center=true);
        translate([4, body_h/2 - 8, -body_d/2 - 0.15]) cylinder(h=0.45, d=1.0, center=true);
    }
}

module bottom_ports() {
    // USB-C opening representation on bottom edge
    color([0.01, 0.01, 0.01, 1.0])
        translate([-8, -body_h/2 - 0.2, 0])
            cube([usb_w, 0.5, usb_h], center=true);

    // optional 3.5mm jack representation on bottom edge
    color([0.01, 0.01, 0.01, 1.0])
        translate([10, -body_h/2 - 0.2, 0])
            rotate([90, 0, 0])
                cylinder(h=0.6, d=jack_dia, center=true);
}

module rf_keepout_zone() {
    color([0.6, 1.0, 0.2, 0.18])
        translate([body_w/2 - 9, body_h/2 - 10, -1.0])
            cube([12, 14, 6], center=true);
}

module yadiggg_block_model() {
    body_shell();
    internal_blocks();
    display_assembly();
    side_control();
    rear_camera();
    mic_ports();
    bottom_ports();
    rf_keepout_zone();
}

yadiggg_block_model();
