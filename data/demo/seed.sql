-- Illustrative seed data only. The fingerprint is synthetic and is not a usable identification reference.
INSERT OR IGNORE INTO roles (id, name, role_group) VALUES
('role_artist', 'Primary Artist', 'vocals'),
('role_bass', 'Double Bass / Electric Bass', 'musician'),
('role_drums', 'Drums / Percussion', 'musician'),
('role_vibes', 'Vibraphone', 'musician'),
('role_synth', 'Synthesizer', 'musician'),
('role_keys', 'Keyboards', 'musician'),
('role_producer', 'Producer', 'production'),
('role_engineer', 'Recording Engineer', 'engineering');

INSERT OR IGNORE INTO contributors (id, name, sort_name, type, discogs_id) VALUES
('person_roy_ayers', 'Roy Ayers', 'Ayers, Roy', 'person', 2265),
('person_william_allen', 'William Allen', 'Allen, William', 'person', 151532),
('person_dennis_davis', 'Dennis Davis', 'Davis, Dennis', 'person', 135850),
('person_philip_woo', 'Philip Woo', 'Woo, Philip', 'person', 391157);

INSERT OR IGNORE INTO releases (id, title, year, label, catalog_number, country, barcode, discogs_id) VALUES
('rel_ayers_sunshine', 'Everybody Loves The Sunshine', 1976, 'Polydor', 'PD-1-6070', 'US', '075021321014', 85552);

INSERT OR IGNORE INTO tracks (id, release_id, title, position, duration_ms) VALUES
('track_sunshine_title', 'rel_ayers_sunshine', 'Everybody Loves The Sunshine', 'A3', 241000);

INSERT OR IGNORE INTO credits (track_id, contributor_id, role_id, source) VALUES
('track_sunshine_title', 'person_roy_ayers', 'role_artist', 'Discogs'),
('track_sunshine_title', 'person_roy_ayers', 'role_vibes', 'Discogs'),
('track_sunshine_title', 'person_roy_ayers', 'role_producer', 'Discogs'),
('track_sunshine_title', 'person_william_allen', 'role_bass', 'Discogs'),
('track_sunshine_title', 'person_dennis_davis', 'role_drums', 'Discogs'),
('track_sunshine_title', 'person_philip_woo', 'role_synth', 'Discogs');

INSERT OR IGNORE INTO track_fingerprints (track_id, fingerprint, num_frames) VALUES
('track_sunshine_title', x'55555555AAAAAAA078563412F0DEBC9AFF00FF00', 5);
