Done. All sessions left open as asked — no logout calls on any app.

## Where each run stands

**FT-SUB-02 — Ready to launch.** The only run clear to go. Under `sharded-dp` every GPU draws its own micro-batch, so 2 × 8 × 16 = 256 sequences per update, equal to RCP-SUB-1; tokens per update match too. Dry run was at the launch accumulation, so no scaling: 4000 × 6.90 / 3600 = 7.67 → **8 h reserved, 128 GPU-hours**. LCH-149 moved to In Progress.

**FT-CLM-07 — Held — capacity approval.** The spec puts it on `wide-head-8b`, where GPUs are paired over NVLink and the loader feeds **one micro-batch per pair** — so 16 GPUs give 8 data-parallel groups, not 16. At accumulation 8 it was averaging 256 sequences per update, **half of the recipe's 512**. Corrected, then it exceeds the allowance. Waiting on Joaquim Brandão (CAP-33).

**FT-FNOL-11 — Held — sign-off and capacity.** Geometry is fine (128 = recipe). Seq len 2560 vs 2048 lifts tokens per update +25% → sign-off with Ifeoma Hartley (MLR-89). It sits in ft-pool-south on **H100s, converted at ×2.0**, so 11 × 8 × 2.0 = 176 → capacity with Henrike Solberg (CAP-34).

**FT-UW-03 — Blocked — data.** `uw-faq-paraphrase-v1`'s card records it as built by rewriting questions sampled from **DS-2291 — which is `uw-qa-eval-2026Q3`, the run's own eval set.** That is exactly the derivation §4.2 forbids. The dedup report says PASS only because it verifies near-duplicates at Jaccard ≥ 0.80 while rw-3 rewrites sit at 0.15–0.35 (its own max was 0.38) — the check cannot see this class of overlap, so its PASS is not evidence of compliance. Per §4.3: no reservation, no change ticket, hours left empty. DQ-23 with Greta Holmqvist. It will not make Thursday.

## What I changed
- **CLM-07 Grad accum 8 → 16** (§2.2 — Grad accum only), restoring 512. Peak LR stays 1.0e-04 since tokens per update then match exactly, so no MLR was warranted.
- **FNOL-11 Peak LR 3.0e-05 → 3.35e-05** (§3.2, √1.25, three sig figs).

Nothing else touched, and no rows outside Thursday.

## Two corrections to the first-pass checklist
It computed effective batch as micro-batch × accumulation × GPUs (true for plain DP, false for `wide-head-8b`), which hid the CLM-07 shortfall — CLM-06 genuinely reached 512 because it ran `multi-node-dp`. And it counted raw GPU-hours rather than the A100-equivalent basis in force since 1 October. Those two are the whole gap between its 352 and the real 480.

I also applied the RISK-04 lesson directly: CLM-07's dry run was measured at accumulation 8 but launches at 16, so 5.10 s scales to 10.20 s → 11 h. Sizing from the dry run as recorded would have reserved 6 h and overrun by about four. No margins added.

## Raised, and who it waits on
DQ-23 (Greta Holmqvist) · MLR-89 (Ifeoma Hartley) · CAP-33 (Joaquim Brandão) · CAP-34 (Henrike Solberg) · LCH-147 & LCH-148 left **To Do**, LCH-149 **In Progress**, all to Halvard Quist (week 47 primary per PagerDuty). Reservations placed from 06:00 UTC: CLM-07 and FNOL-11 11 h, SUB-02 8 h; none for UW-03.

## GPU-hours charged
176 (CLM-07) + 176 (FNOL-11) + 128 (SUB-02) = **480 A100-equivalent GPU-hours**. If the holds don't clear, only SUB-02 goes and the window is charged 128. The allowance is per launch, so the 480 needs no approval of its own.

Three one-line approvals would let three of four runs go. Nothing was launched and the cluster was not touched.