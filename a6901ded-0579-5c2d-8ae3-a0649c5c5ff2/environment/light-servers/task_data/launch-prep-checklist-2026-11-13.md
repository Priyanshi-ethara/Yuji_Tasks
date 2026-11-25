# Thursday 19 Nov — launch prep checklist (first pass)

Prepared by Emeka Rowntree, platform analyst, Fri 13 Nov 2026 15:00 UTC. First pass from the registry rows, the recipe register and the
dry-run events. Not the record: the registry and RB-ML-014 are.

## Geometry (micro-batch x accumulation x GPUs)
- FT-CLM-07: 4 x 8 x 16 = 512. RCP-CLM-3 = 512. OK. Same geometry CLM-06 launched with on 5 Nov.
- FT-UW-03: 8 x 4 x 8 = 256. RCP-UW-2 = 256. OK.
- FT-FNOL-11: 8 x 2 x 8 = 128. RCP-FNOL-4 = 128. OK.
- FT-SUB-02: 2 x 8 x 16 = 256. RCP-SUB-1 = 256. OK.

## Tokens per update
- FT-FNOL-11 runs 2560 tokens against the recipe's 2048, so tokens per update rise 25%. Needs Ifeoma's sign-off; LR to rescale.
- Everything else matches its recipe.

## Data
- Contamination reports: PASS for all four (dedup-svc 3.1, Box).
- PII: Bastien's sweep says Pass for every dataset booked.

## Hours (dry-run seconds per update from Datadog)
| Run | Steps | s/update | Hours (rounded up) | GPUs | GPU-h |
|---|---|---|---|---|---|
| FT-CLM-07 | 3600 | 5.10 | 6 | 16 | 96 |
| FT-UW-03 | 4000 | 3.70 | 5 | 8 | 40 |
| FT-FNOL-11 | 5000 | 7.60 | 11 | 8 | 88 |
| FT-SUB-02 | 4000 | 6.90 | 8 | 16 | 128 |
| Window | | | | | 352 |

All four sit under the 160 per-launch allowance; no CAP requests needed by my count.

## Still to do
- MLR ticket for FNOL-11. Change tickets for all four. Reservations. Note to Odile.
