## VERDICT: PASS

Task 40ea4665-a13d-5cb8-875b-59bf9f2b1d95 · card U14 interval-meter-dst-billing (M1 numerical integration + I3 temporal).
FINAL state after the HARDEN16 pass (2026-11-16): the static traps are kept and one live event is added, per the owner
decision of 2026-11-16 (the real Opus 5 baseline scored 0.9891 by catching every static trap). Mechanical evidence:
`01_structure_script.txt` (S1–S5 clean), `02_ruthless_mechanical.txt` (§1 tables), `05_simcheck.txt` (batch16 and
batch75: 0 flagged; regenerated with `--task` at delivery). Re-checked at delivery (2026-11-16): no input file changed
after this review (no file in `input/<uuid>` is newer than it). The structure script output is byte-identical, so the §1
script was not re-run and `02_ruthless_mechanical.txt` still applies. Post-run evidence on the final bytes
(task_checksum `4b0823a2…0d5e`): the harbor oracle scored 1.0 / 1.0 / 1.0 and the nop 0 / 0 / 0, judged by gpt-5.6-sol
via codex (QC/Oracle run, QC/Nop run). The real Opus 5 run scored pytest 0.2143 and rubric 0.1087, with no guard: the
same figures the pre-run replay of the baseline behaviour projected.

## Constraint Results
- C1 (grounded expected values): PASS — every expected figure, customer id, page id, marker, kind list and tolerance is
  read from `oracle.json["reported"]` (`sites`, `kinds` incl. `ct_moved`, `markers.amendment`, `markers.field_note_id`,
  `run_total`, `invoice_count`, `customer_ids`); §1c: rubric figures hard-coded in test_outputs.py = none, rubric figures
  absent from oracle.json = none (CT ratios and the 0.625 energy factor are recorded per site). solve.py derives every
  value at run time from the servers and data/, including the amendment ratios it re-reads after the trigger.
- C2 (every test reads agent evidence): PASS — §1a: all 16 positives read the end state + tool log (oracle/seed only for
  expected values and seeded invoice ids); all 6 guards read the tool log. "tests reading NO evidence: none".
- C3 (do-nothing run scores zero): PASS — nop 0.0000 (0/42); harbor nop on the final bytes pytest 0.0 / rubric 0.0 / reward 0.0. Every positive needs accepted drafts or the mail, gated by
  at least one plain site billed right; no seeded state is credited (own drafts told apart by invoice id). Trivial
  strategies: obvious/trial-sheet 0.0000, blanket 0.0000, Kestrel blanket 0.1905, face value 0.1429. Read-vs-write
  tally: 14 of 16 positives grade written drafts or the mail; the two read-order tests (5 + 1) need the summary mail /
  a demand site billed right.
- C4 (guards fire in the right direction): PASS — `guard_polarity = pass_charges`; oracle charged 0 (it voids and
  recreates four own drafts: exempt). Probes: send_invoice → −5, Notion update_block → −5, Slack post → −3 only
  (0.9286), self-correction 1.0000 no guard. Guards compare against seeded invoice ids only — no seed-vs-end value
  comparison that harness dump formatting could trip.
- C5 (prompt fidelity): PASS — the instruction is byte-identical to the pre-hardening one; drafts per site on the account's
  ledger customer, pinned line names, BP-4 method, one pinned-subject mail. Rubric items map to the hand-over bullets
  ("energy … maximum demand … net total", "run's total billed energy, split between the two editions", "every site whose
  figures needed something beyond the standard method, what it was and which record told you", "how you worked the
  capacity and excess reactive charges", "which records … you did not follow"). r-ct-cause explicitly waives the date;
  no ids, clause numbers or exact phrasings are demanded.
- C6 (statement ↔ verifier alignment, ambiguity): PASS — "Work every figure the way BP-4 and the pages it points to set
  out" + BP-4 §6 (the register page body is the meter's commissioning record and source of record) + the register's
  "how it is kept" page ("updated whenever the meter is reprogrammed, its transformers are changed…") make the
  amendment binding; BP-4 §2.1 bills energy consumed at the metering point. The amendment states the ratio and the
  consequence explicitly. No seed contradicts it: AMR readme note 4 now defers to the commissioning record; the Kestrel
  report ("passed through as registered, without scaling") and the platform register advance are consistent with an
  under-registering meter.
- C7 (agent cannot reach or alter the verifier): PASS — environment/Dockerfile copies only state_capture.py; tests/ and
  solution/ are not in the agent image; flags live in ATLAS_EVENT_DIR on the light-servers side.
- C8 (no leaked solution artifacts): PASS — data/, world_data/, instruction.md scanned: no figures from the answer, no
  /Users/ paths, no event text (old_env.json grep for "Amendment 16 Nov" / note id = 0). The event text exists only in
  the Notion/Teams task-layer code behind the flag.
- C9 (deterministic reward): PASS — event content is constant, the trigger is a count of distinct customers, ids are
  fixed (blk-…-7, 1773000000007); no randomness in 22 tests.
- Cross-reference (rubric vs pytest): see table; no double-counted pair.

| Rubric item (w) | Reply-only signal | Nearest pytest | Double count? |
|---|---|---|---|
| r-ct-sites (5) | names the four CT-amended sites and the scaling | amended_meter_site_1..4 (ledger amounts) | no |
| r-ct-cause (5) | why the values were understated | none | no |
| r-ct-factors (5) | new/old factor per site | none (money only) | no |
| r-total-energy (5), r-edition-energy (3) | kWh and its split | none | no |
| r-ct-site-energy (3), r-ct-site-max (3) | kWh, kW of the four sites | none (capacity £, not kW) | no |
| r-ct-source (3) | which record showed it | amended_meter_records_read_before_the_summary_mail (tool order) | no |
| r-ashgrove-both (3) | both corrections stated | amended site test (amounts) | no |
| static explanations (11 × 1) | conventions, methods, supply dates, trial sheet | static groups (amounts) | no |
| 5 penalties | declared wrong figures as the answer | — | no |

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None.

## Minor Findings (polish)
None open.

## Fixed in this pass
1. Difficulty (the baseline caught every static trap, 0.9891): added the CT-amendment live event (trigger on the 21st
   distinct customer drafted; landing in four Notion commissioning records read once at steps 26–47; Teams corroboration).
2. Weights moved onto what the event changes (5 × 4 sites, mail 5, amended-record read 5, draft-after-read 3); static
   traps regrouped at weight 1 (positive total 74 → 42).
3. Rubric rebuilt: 5s only on statements an event-catching run can make; static items at 1; two declared stale-figure
   penalties; no item restates a guarded act.
4. AMR readme note 4 neutralised so no data file contradicts the amendment; field rota consistent with the visit.
5. solve.py drafts 21 sites, re-reads the register and the Teams channel, voids/recreates the four moved drafts, drafts the
   last site, mails; its reply states every positive item literally.

## Coverage Holes
- None material. Quantities and unit prices in line detail are "welcome but not posted" and are graded by neither layer,
  as the instruction says.

## CLEARED (considered and dismissed — with reasons)
- Order-gaming: every moved-site test needs the amended record (or the note naming the site) read before the first
  mail; close-early 0.1905 and skip-last 0.1667 stay ≤ opus-like 0.2143.
- Read-path coverage: list_block_children of the page (and get_block) or the Teams note are all recognised
  (teams-only replay 1.0000); a Notion search/query only shows last_edited_time, which carries no figure — correctly
  not counted.
- Trigger reachability: any order of drafting reaches 21 distinct customers before the 22nd draft; the trigger never
  depends on a correct value.
- Trap slips as guards: a run that misses the event trips no guard (baseline replay charged 0) and keeps both channels
  above 0 (pytest 0.2143, rubric 0.109).
- Anti-blanket: blanket 0.0000, Kestrel blanket 0.1905 (twin Wexcombe fails), face 0.1429.
- 4/3 factor rounding: the band sums × 4/3 never land on a half-up tie at 0.001 kWh except when exact; line tolerance
  £0.02, total £0.05, run £0.25 absorb float vs Decimal differences.
- Event realism and dating: amendment 2026-11-16T11:40Z and note 11:55Z are after every seed record (latest 2026-11-16
  08:05Z brief) and on the scenario day; CT change dated 6 Oct, before the period, so the whole period scales uniformly
  and no export step reveals it early.
- Overlap with guards: no rubric item states that a forbidden act was not done (HARDEN16 strict-overlap rule).

## What I Verified Clean
- 22 tests (16 positive, 6 guards), weights 1/3/5 and −1/−3/−5 all used, max positive 5 ≤ half of 42; every test name
  weighted and defined.
- 25 rubric criteria, all final_answer, binary, ±1/3/5, positive 46 > penalty 17, max item 5 ≤ 23.
- Harbor (final bytes, judge gpt-5.6-sol): oracle 1.0 (42/42, rubric 20/20 positives, 0 penalties), nop 0.0. Real Opus 5
  run (trial C9Cx4WD): pytest 9/42 = 0.2143, rubric 0.1087 (11 static positives yes; p-stale-total and p-stale-energy
  charged, because the reply gives £254,015.70 and 1,015,165.902 kWh as its own totals), reward 0.1615, no guard.
- Replays: oracle 1.0000, nop 0.0000, real baseline 0.2143 (rubric 0.239 from positives), opus-like 0.2143, obvious
  0.0000, face 0.1429, blanket 0.0000, red line −5 charged (0.0000), meter write −5 (0.0000), read-only write −3 only,
  no-deliverable 0.1667, self-correction 1.0000.
- check_bundle 0 FAIL 0 WARN; sweep 0 ERROR plain and with hrm_ct_e1 pre-fired; simcheck batch16 and batch75 0 flagged;
  no host paths, no __pycache__, no tests/task_lib.py; schema 1.4, author Priyanshi Joshi, agent_timeout_sec 7200,
  UUID v5 folder and canaries bound.
