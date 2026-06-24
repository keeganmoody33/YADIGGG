-- yadiggg: Official SQL Database Schema Script
-- Optimized for SQLite 3 running on ARM Cortex-A53 (Embedded Yocto Linux)
-- Author: yadiggg Engineering Suite & Accio Sourcing Toolkit
-- Date: June 3, 2026
-- Version: V2.0 (Core Graph & High-Performance Indexes)

PRAGMA foreign_keys = ON;

-- ====================================================================
-- 1. DATABASE TABLES Definition
-- ====================================================================

-- TABLE: contributors
-- Represents artists, session players, producers, and recording engineers
CREATE TABLE IF NOT EXISTS contributors (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    sort_name TEXT,
    type TEXT CHECK(type IN ('person', 'group', 'orchestra', 'choir')),
    mbid TEXT UNIQUE,
    discogs_id INTEGER UNIQUE
);

-- TABLE: releases
-- Represents LPs, EPs, 7" singles, and promo vinyl
CREATE TABLE IF NOT EXISTS releases (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER,
    label TEXT,
    catalog_number TEXT NOT NULL, -- Key index for OCR scan matches
    country TEXT,
    barcode TEXT,                -- Key index for scanner matches
    discogs_id INTEGER UNIQUE,
    mbid TEXT UNIQUE
);

-- TABLE: tracks
-- Individual songs contained on a physical release
CREATE TABLE IF NOT EXISTS tracks (
    id TEXT PRIMARY KEY,
    release_id TEXT NOT NULL,
    title TEXT NOT NULL,
    position TEXT,                -- e.g., 'A1', 'B3' (physical vinyl position)
    duration_ms INTEGER,
    FOREIGN KEY(release_id) REFERENCES releases(id) ON DELETE CASCADE
);

-- TABLE: roles
-- Normalized engineering, production, and performance roles
CREATE TABLE IF NOT EXISTS roles (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    role_group TEXT NOT NULL CHECK(role_group IN ('musician', 'production', 'engineering', 'vocals', 'visual'))
);

-- TABLE: credits (The Core Graph Edge)
-- Highly queried join table linking contributors to tracks via roles
CREATE TABLE IF NOT EXISTS credits (
    track_id TEXT NOT NULL,
    contributor_id TEXT NOT NULL,
    role_id TEXT NOT NULL,
    source TEXT NOT NULL,         -- e.g., 'MusicBrainz', 'Discogs', 'TIDAL'
    confidence REAL DEFAULT 1.0,  -- Match confidence (0.0 - 1.0)
    PRIMARY KEY(track_id, contributor_id, role_id),
    FOREIGN KEY(track_id) REFERENCES tracks(id) ON DELETE CASCADE,
    FOREIGN KEY(contributor_id) REFERENCES contributors(id) ON DELETE CASCADE,
    FOREIGN KEY(role_id) REFERENCES roles(id) ON DELETE RESTRICT
);

-- TABLE: sample_relationships (The Lineage Edge)
-- Bidirectional sample mapping tree (WhoSampled-style direct link)
CREATE TABLE IF NOT EXISTS sample_relationships (
    id TEXT PRIMARY KEY,
    source_track_id TEXT NOT NULL,  -- The track that contains/uses the sample
    sampled_track_id TEXT NOT NULL, -- The original track that was sampled
    type TEXT NOT NULL CHECK(type IN ('direct_sample', 'interpolation', 'cover', 'remix')),
    description TEXT,               -- e.g., 'vocal hook', 'drum break loop'
    confidence REAL DEFAULT 1.0,
    FOREIGN KEY(source_track_id) REFERENCES tracks(id) ON DELETE CASCADE,
    FOREIGN KEY(sampled_track_id) REFERENCES tracks(id) ON DELETE CASCADE
);

-- TABLE: recording_locations
-- Represents physical studios or spaces where sessions occurred
CREATE TABLE IF NOT EXISTS recording_locations (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    state TEXT,
    country TEXT
);

-- TABLE: track_locations
-- Links tracks to specific recording location enclaves
CREATE TABLE IF NOT EXISTS track_locations (
    track_id TEXT NOT NULL,
    location_id TEXT NOT NULL,
    PRIMARY KEY(track_id, location_id),
    FOREIGN KEY(track_id) REFERENCES tracks(id) ON DELETE CASCADE,
    FOREIGN KEY(location_id) REFERENCES recording_locations(id) ON DELETE CASCADE
);

-- TABLE: external_links
-- Launch URIs for immediate listening sessions
CREATE TABLE IF NOT EXISTS external_links (
    id TEXT PRIMARY KEY,
    track_id TEXT,
    release_id TEXT,
    platform TEXT NOT NULL CHECK(platform IN ('youtube', 'tidal', 'spotify', 'apple_music')),
    url TEXT NOT NULL,
    FOREIGN KEY(track_id) REFERENCES tracks(id) ON DELETE CASCADE,
    FOREIGN KEY(release_id) REFERENCES releases(id) ON DELETE CASCADE
);

-- TABLE: wishlist
-- User's local saved tracks, "crates", and wishlist items
CREATE TABLE IF NOT EXISTS wishlist (
    id TEXT PRIMARY KEY,
    release_id TEXT,
    track_id TEXT,
    scanned_at TEXT NOT NULL,     -- ISO 8601 Timestamp
    notes TEXT,
    audio_preview_path TEXT,      -- Local path to cached 30s audio loop
    FOREIGN KEY(release_id) REFERENCES releases(id) ON DELETE SET NULL,
    FOREIGN KEY(track_id) REFERENCES tracks(id) ON DELETE SET NULL
);

-- TABLE: track_fingerprints
-- Stores compressed binary OLAF hashes (array of uint32_t) for offline Sonic ID matches
CREATE TABLE IF NOT EXISTS track_fingerprints (
    track_id TEXT PRIMARY KEY,
    fingerprint BLOB NOT NULL,    -- Packed array of 32-bit hashes
    num_frames INTEGER NOT NULL,  -- Number of 32-bit hashes in blob
    FOREIGN KEY(track_id) REFERENCES tracks(id) ON DELETE CASCADE
);

-- ====================================================================
-- 2. HIGH-PERFORMANCE SEARCH INDEXES (Sub-50ms lookup on Cortex-A53)
-- ====================================================================

CREATE INDEX IF NOT EXISTS idx_releases_catalog ON releases(catalog_number);
CREATE INDEX IF NOT EXISTS idx_releases_barcode ON releases(barcode);
CREATE INDEX IF NOT EXISTS idx_tracks_release ON tracks(release_id);
CREATE INDEX IF NOT EXISTS idx_credits_track ON credits(track_id);
CREATE INDEX IF NOT EXISTS idx_credits_contributor ON credits(contributor_id);
CREATE INDEX IF NOT EXISTS idx_samples_source ON sample_relationships(source_track_id);
CREATE INDEX IF NOT EXISTS idx_samples_sampled ON sample_relationships(sampled_track_id);

-- ====================================================================
-- 3. REFERENCE SEED DATA (Roy Ayers - Everybody Loves The Sunshine)
-- ====================================================================

-- Inserts Roles
INSERT OR IGNORE INTO roles (id, name, role_group) VALUES 
('role_artist', 'Primary Artist', 'vocals'),
('role_bass', 'Double Bass / Electric Bass', 'musician'),
('role_drums', 'Drums / Percussion', 'musician'),
('role_vibes', 'Vibraphone', 'musician'),
('role_synth', 'Synthesizer', 'musician'),
('role_keys', 'Keyboards', 'musician'),
('role_producer', 'Producer', 'production'),
('role_engineer', 'Recording Engineer', 'engineering');

-- Inserts Contributors
INSERT OR IGNORE INTO contributors (id, name, sort_name, type, discogs_id) VALUES 
('person_roy_ayers', 'Roy Ayers', 'Ayers, Roy', 'person', 2265),
('person_william_allen', 'William Allen', 'Allen, William', 'person', 151532),
('person_dennis_davis', 'Dennis Davis', 'Davis, Dennis', 'person', 135850),
('person_philip_woo', 'Philip Woo', 'Woo, Philip', 'person', 391157);

-- Inserts Release
INSERT OR IGNORE INTO releases (id, title, year, label, catalog_number, country, barcode, discogs_id) VALUES 
('rel_ayers_sunshine', 'Everybody Loves The Sunshine', 1976, 'Polydor', 'PD-1-6070', 'US', '075021321014', 85552);

-- Inserts Track
INSERT OR IGNORE INTO tracks (id, release_id, title, position, duration_ms) VALUES 
('track_sunshine_title', 'rel_ayers_sunshine', 'Everybody Loves The Sunshine', 'A3', 241000);

-- Inserts Track Credits
INSERT OR IGNORE INTO credits (track_id, contributor_id, role_id, source) VALUES 
('track_sunshine_title', 'person_roy_ayers', 'role_artist', 'Discogs'),
('track_sunshine_title', 'person_roy_ayers', 'role_vibes', 'Discogs'),
('track_sunshine_title', 'person_roy_ayers', 'role_producer', 'Discogs'),
('track_sunshine_title', 'person_william_allen', 'role_bass', 'Discogs'),
('track_sunshine_title', 'person_dennis_davis', 'role_drums', 'Discogs'),
('track_sunshine_title', 'person_philip_woo', 'role_synth', 'Discogs');

-- Inserts Track Fingerprints (OLAF Mock Fingerprint Blob)
-- Represents 5 frames of logarithmic sub-band hashes: [0x55555555, 0xAAAAAAA, 0x12345678, 0x9ABCDEF0, 0x00FF00FF]
-- SQLite hex literal represents packed 32-bit little-endian hashes
INSERT OR IGNORE INTO track_fingerprints (track_id, fingerprint, num_frames) VALUES 
('track_sunshine_title', x'55555555AAAAAAA078563412F0DEBC9AFF00FF00', 5);
