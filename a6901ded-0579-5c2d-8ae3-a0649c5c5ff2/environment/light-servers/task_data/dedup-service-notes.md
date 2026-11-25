# dedup-svc 3.1 — how contamination checks are produced

dedup-svc compares an evaluation set with each training source a run lists and writes one report per run into Box
(ml-platform/dedup-reports).

1. Normalisation: lower-case, Unicode NFKC, whitespace and punctuation folded.
2. Exact pass: hash of the normalised text of each item; any shared hash is an exact match.
3. Near-duplicate pass: MinHash LSH over 5-gram word shingles, 128 permutations, candidate pairs verified at Jaccard >= 0.80.
4. Report: per-source counts of exact and near-duplicate matches, the highest Jaccard seen, and PASS when both counts are zero.

Operational notes
- Reports are produced from the training sources as listed in the registry row at the time of the check.
- The 0.80 threshold has been unchanged since dedup-svc 2.0 (March 2026).
- Runtime for a 2,600-item evaluation set against 100k training rows is about 6 minutes.
