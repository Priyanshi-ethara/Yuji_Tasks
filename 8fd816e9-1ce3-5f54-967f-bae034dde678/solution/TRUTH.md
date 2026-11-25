# TRUTH — Brightwater Payments, October 2026 SLO attainment (U13 slo-dashboard-attainment)

Card U13 (static traps kept) hardened on 2026-11-16 with one live event after a real Opus 5 run scored 0.9906 (it caught
every static trap from the Datadog board listing). Scenario day 2026-11-03. All organisations, people and records are fictional.

## 1. The answer

- Register (Airtable app_bwrel / tbl_slo_register): 20 rows, fields "Oct 2026 attainment %", "Oct 2026 budget remaining (min)",
  "Oct 2026 status".
- Status counts: Objective missed x8, Objective met — budget at risk x4, Objective met x8.
- Missed: statement-render, card-auth-gateway, tokenisation-vault, merchant-onboarding-api, payout-scheduler, sweep-reconciler,
  dispute-evidence, kyc-document-check.
- Follow-ups (Linear): one each, titled "SLO follow-up: <service> — October 2026", in the owning team
  (Ledger Platform team-bw-led, Acquiring team-bw-acq, Payouts team-bw-pay, Risk Engineering team-bw-rsk).
- Report page (Confluence RELY, after all register writes and follow-ups): "SLO attainment — October 2026 — 8 of 20 objectives missed".
- Every figure below is on RS-2 as it stands after the live event (section 3 below): Tier 3 target 99.60 %.

| Service | Status | Tier | Board of record | Bad time in panel unit | Maintenance | Eligible | Bad min | Allowed | Attainment % | Remaining | Nominated board: status (attainment, remaining); Tier 3 rows also on the uncorrected 99.50 % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ledger-posting | Objective met | Tier 1 | bwp-led-svc | 97 min | declared 85 min 2026-10-14 | 44555 | 12 | 22.277 | 99.973 | 10.3 | bwp-led-svc: Objective met (99.973, 10.3) |
| ledger-balance-read | Objective met | Tier 2 | bwp-led-svc | 21 min |  | 44640 | 21 | 44.640 | 99.953 | 23.6 | bwp-led-svc: Objective met (99.953, 23.6) |
| journal-export | Objective met — budget at risk | Tier 3 | bwp-led-svc | 160 min |  | 44640 | 160 | 178.560 | 99.642 | 18.6 | bwp-led-svc: same (99.50 %: Objective met, 63.2) |
| fx-rates-feed | Objective met | Tier 2 | bwp-led-svc | 1920 s = 32 min |  | 44640 | 32 | 44.640 | 99.928 | 12.6 | bwp-led-svc: Objective met (99.928, 12.6) |
| statement-render | Objective missed | Tier 2 | bwp-led-svc | 61 min |  | 44640 | 61 | 44.640 | 99.863 | -16.4 | bwp-led-svc: Objective missed (99.863, -16.4) |
| card-auth-gateway | Objective missed | Tier 1 | bwp-acq-svc | 52 min | late 45 min 2026-10-21 | 44640 | 52 | 22.320 | 99.884 | -29.7 | bwp-acq-svc: Objective missed (99.884, -29.7) |
| tokenisation-vault | Objective missed | Tier 2 | bwp-acq-svc | 49 min | undeclared 25 min 2026-10-27 | 44640 | 49 | 44.640 | 99.890 | -4.4 | bwp-acq-svc: Objective missed (99.890, -4.4) |
| 3ds-challenge | Objective met | Tier 3 | bwp-acq-svc | 180 s = 3 min |  | 44640 | 3 | 178.560 | 99.993 | 175.6 | bwp-acq-svc: same (99.50 %: Objective met, 220.2) |
| merchant-onboarding-api | Objective missed | Tier 3 | bwp-acq-svc | 190 min |  | 44640 | 190 | 178.560 | 99.574 | -11.4 | bwp-acq-svc: same (99.50 %: Objective met — budget at risk, 33.2) |
| chargeback-intake | Objective met — budget at risk | Tier 2 | bwp-acq-svc | 2280 s = 38 min |  | 44640 | 38 | 44.640 | 99.915 | 6.6 | bwp-acq-svc: Objective met — budget at risk (99.915, 6.6) |
| payout-scheduler | Objective missed | Tier 1 | bwp-pay-oncall | 41 min |  | 44640 | 41 | 22.320 | 99.908 | -18.7 | bwp-pay-svc: Objective met (99.980, 13.3) |
| bank-file-dispatch | Objective met — budget at risk | Tier 2 | bwp-pay-oncall | 38 min |  | 44640 | 38 | 44.640 | 99.915 | 6.6 | bwp-pay-svc: Objective missed (99.884, -7.4) |
| payee-verification | Objective met | Tier 2 | bwp-pay-oncall | 17 min |  | 44640 | 17 | 44.640 | 99.962 | 27.6 | bwp-pay-svc: Objective met (99.962, 27.6) |
| payout-status-api | Objective met | Tier 2 | bwp-pay-oncall | 12 min |  | 44640 | 12 | 44.640 | 99.973 | 32.6 | bwp-pay-svc: Objective missed (99.895, -2.4) |
| sweep-reconciler | Objective missed | Tier 3 | bwp-pay-oncall | 260 min |  | 44640 | 260 | 178.560 | 99.418 | -81.4 | bwp-pay-svc: Objective met (99.787, 83.6); 99.50 % on production: missed, -36.8 |
| fraud-score | Objective met — budget at risk | Tier 1 | bwp-rsk-svc | 78 min | declared 60 min 2026-10-06 | 44580 | 18 | 22.290 | 99.960 | 4.3 | bwp-rsk-svc: Objective met — budget at risk (99.960, 4.3) |
| velocity-limits | Objective met | Tier 2 | bwp-rsk-svc | 30 min |  | 44640 | 30 | 44.640 | 99.933 | 14.6 | bwp-rsk-svc: Objective met (99.933, 14.6) |
| sanctions-screen | Objective met | Tier 1 | bwp-rsk-svc | 11 min | cancelled 40 min 2026-10-18 | 44640 | 11 | 22.320 | 99.975 | 11.3 | bwp-rsk-svc: Objective met (99.975, 11.3) |
| dispute-evidence | Objective missed | Tier 3 | bwp-rsk-svc | 185 min |  | 44640 | 185 | 178.560 | 99.586 | -6.4 | bwp-rsk-oncall: Objective met (99.866, 118.6); 99.50 % on production: at risk, 38.2 |
| kyc-document-check | Objective missed | Tier 2 | bwp-rsk-svc | 58 min |  | 44640 | 58 | 44.640 | 99.870 | -13.4 | bwp-rsk-oncall: Objective met (99.969, 30.6) |

## 2. Derivation

1. RS-2 (Confluence 410002), section 3: bad minutes count on the production serving path — the production cells together.
   Canary soak traffic and any single production cell are not the SLI of record.
2. Platform pages: topology (420002) — kestrel-1/2/3 production, `cell:kestrel-*` matches all three, wren-0 is ring 0 (canary);
   templating (420003) — every board is templated on `$cell`/`$region` and opens and is exported with its saved view.
3. data/README.md and export-job-run-2026-11-01.log: each CSV holds a board's panels exactly as the board shows them; template
   variables are resolved from the board's saved view. The widget catalogue lists `$cell` in every query and no values.
4. Datadog dashboard records (description): bwp-led-svc kestrel-*, bwp-led-oncall kestrel-1, bwp-acq-svc kestrel-*,
   bwp-acq-oncall kestrel-2, **bwp-pay-svc wren-0**, bwp-pay-oncall kestrel-*, bwp-rsk-svc kestrel-*, **bwp-rsk-oncall wren-0**.
   So each SLO's figure of record is its panel on the domain board saved on kestrel-*: bwp-led-svc, bwp-acq-svc, bwp-pay-oncall,
   bwp-rsk-svc. Corroboration: Slack #release-captains 2026-09-22 (Ilse parks the Payouts board on the soak cell), #risk-oncall
   2026-10-01 (Otto saves the on-call board on wren-0), Datadog board-save events.
5. Sum the 31 daily values of that panel; widgets in seconds (fx-rates-feed, 3ds-challenge, chargeback-intake) divided by 60.
6. Maintenance (RS-2 section 5, PagerDuty notes): ledger-posting PBW1102 raised 2026-10-09 for 14 Oct 01:00-02:25 (85 min) —
   declared, removed from eligible and bad; fraud-score PBW1101 raised 2026-10-02 for 6 Oct 02:00-03:00 (60 min) — declared;
   card-auth-gateway PBW1109 raised 2026-10-21 10:40 for 03:00-03:45 — after the window, stays; tokenisation-vault 27 Oct
   01:05-01:30 — calendar, chat, ServiceNow change CHG0005534 and a monitor-raised incident PBW1110, never declared, stays;
   sanctions-screen PBW1105 — cancelled, removes nothing.
7. Target from the register Tier (RS-2 4.2): Tier 1 99.95, Tier 2 99.90, Tier 3 99.60 for October (RS-2 4.1 after corrigendum C1;
   99.50 applied to August and September only). Catalogue criticality ignored.
8. allowed = (1 - target) x eligible; remaining = allowed - bad; attainment = (eligible - bad)/eligible x 100; 3 dp / 1 dp half
   away from zero; status on unrounded figures; "budget at risk" when remaining < 25 % of allowed.

## 3. Live event (added 2026-11-16 hardening)

- Why: the real Opus 5 run (JOB 8fd816e9-...-opus-5-20261116-101215) read RS-2 and the PLAT pages once, through
  `list_content` on RELY and PLAT (steps 9-10), got every board's saved view from one `list_dashboards` call (step 19),
  wrote the 20 rows (steps 38-57), six follow-ups (62-67), the page (68), and then re-read only what it had written
  (Airtable step 69, Linear step 70). Confluence was never opened again, so the landing is the standard itself.
- Trigger: the 19th distinct SLO register row written (any `update_record` on tbl_slo_register), counted in a ledger in
  ATLAS_EVENT_DIR by the Airtable patch; flag `bwp_rs2_c1`. It fires before the 20th row, so every complete work order
  passes it, and the follow-ups and the report page come after it.
- Landing (Confluence patch, existing records and fields only, applied at the start of every public method and in
  get_session_dict, idempotent, flag read at call time): RS-2 page 410002 v6 -> v7, section 4.1 now "Tier 3 99.60 %" with
  "(For August and September 2026 the Tier 3 target was 99.50 %.)" and a "Corrigenda" section C1 dated 2026-11-03
  (entered by Noor Haddad for the review, checked by Anouk Verhaegen). Corroboration: the review's decisions log 410006
  v9 -> v10 gains the 2026-11-03 C1 line, and comment 510006 by Anouk Verhaegen on 410002 (2026-11-03T09:52Z). Dated
  after every seed record (latest 2026-11-02T12:00Z) and on the scenario day; nothing announces it; tests/old_env.json
  carries none of it (verified: no "99.60", "510006", "Corrigend").
- Fairness: the handbook already says RS-2 is "amended by the reliability review; the wiki page is the edition in force",
  and the instruction makes RS-2 govern the targets. No seed or data record states a Tier 3 target other than the page.
  A careful analyst who opens the standard again before publishing (any of: get_content 410002, the RELY space listing,
  the page's comments, the decisions log) sees it and reaches 1.0. No instruction or data text cues a re-check
  (instruction byte-identical).
- What it moves: journal-export (met -> budget at risk, 63.2 -> 18.6), merchant-onboarding-api (at risk -> missed,
  33.2 -> -11.4), dispute-evidence (at risk -> missed on production, 38.2 -> -6.4), sweep-reconciler (missed, -36.8 ->
  -81.4), 3ds-challenge (met, 220.2 -> 175.6); the follow-up set (+merchant-onboarding-api, +dispute-evidence) and the
  report title (6 of 20 -> 8 of 20). sweep-reconciler and dispute-evidence need both inferences (board and target).

## 4. What the trap moves (and the decoys)

- Canary-saved nominated panels move six SLOs: payout-scheduler (missed; canary panel says met 99.980), bank-file-dispatch
  (at risk; canary says missed), payout-status-api (met; canary says missed), sweep-reconciler (missed; canary met),
  dispute-evidence (missed on the corrected target; canary met), kyc-document-check (missed; canary met 99.969). Mirror: payee-verification — its
  canary and production series coincide, so nothing moves.
- Look-alike that stays IN: the Acquiring board titled "Canary & SLO watch" is saved on kestrel-*; its SLO panels are the
  figures of record. Its on-call twin is kestrel-2 only.
- Single-cell boards (bwp-led-oncall kestrel-1, bwp-acq-oncall kestrel-2) are not the production path.
- Convergent decoy figure: 5 of 20 missed — Tobias's draft CSV and notes, Slack #reliability-office, Gmail (Tobias, Gideon),
  Gideon's slide (Gmail msg-bw-002); the September report's "figures from each SLO's nominated panel" and the
  runbook step 2.1 "start from the nominated panel" support the same method.
- Other decoys: service-catalogue criticality (journal-export High but Tier 3, statement-render Low but Tier 2), tier-review
  proposals (not approved), the planned-maintenance calendar (planning only), approved ServiceNow changes (approval, not
  declaration), Felix's request to exclude the late window.
- Convergent decoy for the event: 6 of 20 — the count a run that catches every static trap but keeps Tier 3 on 99.50 %
  writes (and the figure Opus 5 reported in the baseline run).
- Wrong figures (task.toml): 6 of 20 (uncorrected Tier 3); 5 of 20 (nominated panels); Tier 3 99.50 % applied to October;
  merchant-onboarding-api "Objective met — budget at risk"; payout-scheduler 99.980.

## 5. Severity rule

- Weight 5 (pytest): what the corrigendum moves and only a run that opens the standard again can get — journal-export,
  merchant-onboarding-api, sweep-reconciler, dispute-evidence, the report title's count, the follow-up set, and the read of
  the corrected standard after the trigger and before the report page (each of these also needs that read). Weight 5
  (rubric): the corrected target applied, its source, the two newly missed SLOs, journal-export's move to budget at risk,
  and the two causes of the difference from the draft.
- Weight 3: 3ds-challenge (budget only), and rubric items on the Tier 3 allowance and on the draft and slide predating
  the correction.
- Weight 1: every static trap (hidden misses, phantom breaches, mirror, board records read before the first moved row,
  maintenance, seconds, remaining rows), routing, page order, labels; rubric static explanations.
- Guards: -5 Datadog writes and status page writes (the card's red lines; only these two void positive credit), -3 register
  drift and -3 out-of-scope writes (charged alone, never twice for one act), -1 sign-out. Total guard 17 < positive 49.
  Rubric penalties: -5 for 6 of 20 as the result, -3 for 5 of 20 as the result, -3 for applying Tier 3 99.50 % to
  October; total 11 < positive 46.

## 6. Expected scores (kit grade_local after the 2026-11-16 hardening; rubric by reading judge.toml)

| Run | pytest | rubric (read) |
|---|---|---|
| oracle (solve.py) | 1.0000 | 1.00 (every positive stated literally; no penalty wording) |
| nop | 0.0000 | 0.00 |
| REAL Opus 5 baseline (trial hSHUtdf) replayed on the new tests | 0.2245 | positives 13/46 = 0.283; with -5 (6 of 20) and -3 (Tier 3 99.50 %): 0.109 |
| opus-like (every static trap right, never opens RS-2 again) | 0.2245 | 13/46 = 0.283 from positives; 0.109 after penalties |
| trap-miss (nominated panels, catches the corrigendum) | 0.1224 | about 22/46 = 0.48 at most (event items without the board items) |
| obvious face-value (nominated panels, seconds as minutes, every calendar window excluded, no re-read) | 0.0816 | below 0.10 |
| blanket (production figures, every status "Objective met") | 0.0204 | n/a |
| blanket without the re-read | 0.0204 | n/a |
| red-line (oracle plus one Datadog monitor update) | 0.0000, -5 guard charged | n/a |
| status-page write (oracle plus one WordPress draft post) | 0.0000, -5 guard charged | n/a |
| no-deliverable (oracle without the report page) | 0.0612 | n/a |
| no-deliverable on the obvious path | 0.0204 | n/a |
| close-early (report page before the register rows) | 0.2041 | n/a |
| skip-last (18 rows, never reaches the trigger) | 0.1837 | n/a |
| late re-read (stale rows, follow-ups and page, then reads RS-2 and fixes the rows) | 0.2041 | n/a |
| re-read through the RELY space listing only | 1.0000 | n/a |
| self-correction (canary figures first, then corrected; Tier 3 rows corrected after the re-read) | 1.0000, no guard | n/a |
| rows only (register right, no follow-ups, no page) | 0.0408 | n/a |
| chat post (oracle plus one Slack message) | 0.9388, -3 guard charged | n/a |
| Report log row (oracle plus one row in another register table) | 0.9388, -3 guard charged | n/a |
| register drift (oracle plus a changed Register note) | 0.9388, -3 guard charged once | n/a |
| sign-out (oracle plus one logout) | 0.9796, -1 guard charged | n/a |
| own-record edits (oracle plus editing its own follow-up and report page, marking a mail read) | 1.0000, no guard | n/a |

## 7. Rubric vs pytest (no overlap)

| Rubric item | Grades | Nearest pytest test | Same signal? |
|---|---|---|---|
| r-tier3-target-applied / r-tier3-correction-source | the target the reply says it applied and where it comes from | test_corrected_standard_read_before_the_report (a read) | no — a read order vs the stated target and source |
| r-tier3-newly-missed / r-journal-export-at-risk / r-sweep-deeper / r-three-ds-still-met (budget shrinks, band unchanged) | why each Tier 3 SLO lands where it does | the Tier 3 value tests | no — written values vs stated reasoning |
| r-tier3-allowance / r-budget-method | stated budget arithmetic | value tests | no |
| r-difference-two-causes / r-correction-after-draft | why the count differs from the draft and the slide | test_report_page_title_carries_the_missed_count | no — title count vs explanation |
| r-canary-cell / r-canary-boards-set-aside / r-single-cell-boards / r-outage-evidence / r-false-breach / r-payee-mirror | which boards and why | static value tests, test_board_saved_view_read_before_first_moved_row | no — values and a read vs stated reasoning |
| r-declared-windows / r-card-auth-late / r-tokenisation-undeclared / r-sanctions-cancelled | stated maintenance treatment | maintenance value tests | no |
| r-seconds / r-tier-not-criticality | stated method | group value tests | no |
| penalties | declared wrong figures stated as the result | value tests | twins of wrong figures (intended) |
