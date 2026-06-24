/**
 * @file olaf.h
 * @brief Offline Lightweight Audio Fingerprinting (OLAF) Core Engine
 * @date Friday, June 5, 2026
 * @status Production Release V1.0 (NXP i.MX 8M Nano / Cortex-A53 Optimized)
 *
 * This header defines the data structures, signal-processing constants,
 * and core function prototypes for the yadiggg offline acoustic
 * fingerprint extraction and matching subsystem (Sonic ID).
 */

#ifndef YADIGGG_OLAF_H
#define YADIGGG_OLAF_H

#include <stdint.h>
#include <stddef.h>

#define OLAF_SAMPLE_RATE      44100   // Target input sample rate (Hz)
#define OLAF_FFT_SIZE         2048    // STFT window size
#define OLAF_OVERLAP          1024    // STFT frame overlap size (50%)
#define OLAF_NUM_BANDS        32      // Number of logarithmic frequency sub-bands (300Hz - 2000Hz)
#define OLAF_MIN_FREQ         300.0f  // Low-frequency cutoff for vinyl vocal/melody range
#define OLAF_MAX_FREQ         2000.0f // High-frequency cutoff for vinyl acoustic range

/**
 * @struct olaf_fingerprint
 * @brief Compressed representation of an audio track's acoustic signature.
 */
typedef struct {
    uint32_t *hashes;                 // Array of 32-bit sub-fingerprint hashes
    size_t length;                    // Number of frames/hashes in the fingerprint
} olaf_fingerprint_t;

/**
 * @struct olaf_match_result
 * @brief Output parameters returned by a database fingerprint search.
 */
typedef struct {
    char track_id[64];                // Matches track_id in yadiggg_schema.sql
    float confidence;                 // Alignment score from 0.0 to 1.0 (normalized Hamming match)
    uint32_t offset_sec;              // Best temporal offset where the match was identified (seconds)
} olaf_match_result_t;

/**
 * @brief Initialize the OLAF engine's internal windowing functions and FFT tables.
 * @return 0 on success, negative value on error.
 */
int olaf_init(void);

/**
 * @brief Generate a list of 32-bit acoustic hashes from a raw 16-bit PCM audio stream.
 * 
 * @param pcm_samples Pointer to raw 16-bit signed integer PCM audio samples (44.1kHz).
 * @param num_samples Total number of audio samples.
 * @param out_fp Pointer to the fingerprint structure to populate.
 * @return 0 on success, negative error code on failure.
 */
int olaf_extract_fingerprint(const int16_t *pcm_samples, size_t num_samples, olaf_fingerprint_t *out_fp);

/**
 * @brief Calculate the normalized similarity score between two OLAF fingerprints.
 * 
 * Slides the query fingerprint along the reference fingerprint to find the highest
 * alignment score, compensating for timing offsets.
 * 
 * @param query Pointer to the newly recorded query fingerprint.
 * @param reference Pointer to the pre-compiled database reference fingerprint.
 * @param out_offset Pointer to store the identified matching offset frame.
 * @return float Normalized confidence score from 0.0 (no match) to 1.0 (perfect match).
 */
float olaf_compare_fingerprints(const olaf_fingerprint_t *query, const olaf_fingerprint_t *reference, uint32_t *out_offset);

/**
 * @brief Free heap memory allocated inside an olaf_fingerprint_t structure.
 * 
 * @param fp Pointer to the fingerprint structure to release.
 */
void olaf_free_fingerprint(olaf_fingerprint_t *fp);

#endif // YADIGGG_OLAF_H
