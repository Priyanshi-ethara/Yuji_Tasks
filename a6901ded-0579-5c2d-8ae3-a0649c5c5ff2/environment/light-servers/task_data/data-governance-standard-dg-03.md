# DG-03 Training data handling (excerpt for ML Platform)

Owner: Bastien Achterberg · version 3.2, 1 September 2026

3.1 Every dataset used for training carries a dataset card in the data catalogue with its owner, version, row count and PII scan result.
3.2 The PII scan is run with the current pii-scan release on the exact version that will be trained on. A card shows Pass or Fail;
    a Fail blocks training on that version.
3.3 Dataset owners keep their cards current, including how the dataset was produced.
3.4 Evaluation sets are frozen and owned by the evaluation lead (Paloma Reyes-Hart). Their independence from training data is checked at launch
    readiness under RB-ML-014; DG-03 does not repeat that rule.
3.5 Data is never deleted to resolve a problem; a corrected version is published under a new version and the old one retired.
