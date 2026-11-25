# Paraphrase sets — how they are built

Paraphrase sets widen the phrasing a model sees for the same intent. The data-pipelines job `paraphrase_build` takes:

- `--source <dataset id>`: the dataset whose questions are sampled;
- `--sample <n>`: how many questions to sample;
- `--rewriter rw-3`: the rewrite model (temperature 0.7, three candidates, best kept by a fluency filter);
- `--regen-answers <manual>` or `--keep-answers`: whether answers are regenerated against a manual or kept from the source pairs.

The job's log stays with the data-pipelines runner; the owner records the source on the dataset card.
Rewritten questions keep the intent and entities of the source question while changing most of the wording; typical 5-gram
Jaccard between a rewrite and its source is 0.15 to 0.35.

Paraphrase sets published in 2026: claims-faq-paraphrase-v1 (retired), uw-faq-paraphrase-v1, claims-faq-paraphrase-v2.
