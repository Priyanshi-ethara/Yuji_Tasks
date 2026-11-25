## VERDICT: PASS

Task a6901ded-0579-5c2d-8ae3-a0649c5c5ff2, card U15 finetune-launch-readiness. This report covers the final state after the HARDEN16 pass of 2026-11-16.

The static traps are kept (trap 11, plus 16 and 10). One live event is added: the ft-launcher 4.2.2 re-measurement of the window's multi-node dry runs. Target failure: stale-read. The instruction is byte-identical to the static version.

Review history:
- A fresh independent hostile review of the hardened bytes returned FAIL: 3 Major, 5 Minor, 0 Critical.
- All eight findings were fixed in one pass (listed below).
- A confirming pass by the same reviewer returned PASS, with no Critical or Major findings remaining.

Mechanical output: `01_structure_script.txt`, `02_ruthless_mechanical.txt` and `05_simcheck.txt` in this folder. All three were re-run at final QC on a fresh copy of `harness_mcp_atlas/input/<uuid>`. That copy is byte-identical to the delivered task and to the bytes of the Opus run and the oracle/nop runs (task_checksum 5f56d8e4…b1de). The earlier mechanical run, at 16:11, came before the 16:18–16:22 fix pass. The re-run differs from it only in the rubric rows that pass changed: r-sub02-hours-arith and r-sub02-sharded replace r-sub02-seconds and r-sub02-hold-is-timing-only; r-single-node-unaffected goes 5 → 1; the positive total goes 46 → 42; there are new rubric figures 10.1, 3600 and 4000. Every claim below matches the re-run. Hardening notes: `_kit/qc/<uuid>/HARDEN_NOTES.md`; they are not part of the delivered QC Report.

## Constraint Results
- **C1 (grounded expected values): PASS.**
  - Every expected value is read from `oracle.json["reported"]` (`EXP()`). The seed comes from `old_env.json`.
  - §1c lists 22 figures in the rubric text. None is hard-coded in the tests ("of those, hard-coded in test_outputs.py: none").
  - Two of them are absent from oracle.json:
    - 480 is a declared wrong figure (`wrong_figures`, the penalty twin p-window-480). It appears nowhere in data/ or world_data/ as anyone's figure.
    - 4000 is FT-SUB-02's step count. It is a seed fact: the registry row in world_data/LightAirtable.json, plus the request and checklist in data/. It is used only in the arithmetic of r-sub02-hours-arith.
  - Arithmetic, re-done:
    - FT-CLM-07: 16 GPUs / 2 = 8 replicas; 4 × 8 × 8 = 256 ≠ 512, so accumulation 16. The 4.2.2 dry run gives 5.80 s at accumulation 8, scaled to 11.60 s. 3600 × 11.6 / 3600 = 11.6, rounded up to 12 h. 12 × 16 = 192 > 160.
    - FT-SUB-02: 4000 × 9.10 / 3600 = 10.11, rounded up to 11 h. 11 × 16 = 176 > 160, so Held — capacity approval.
    - FT-FNOL-11: tokens per update +25%, so LR 3.35e-5. 5000 × 7.6 / 3600 = 10.56, rounded up to 11 h. 11 × 8 × 2.0 = 176.
    - Window: 192 + 176 + 176 = 544.
- **C2 (every test reads agent evidence): PASS.**
  - §1a: 20 weighted tests (14 positive, 6 guards). Every test reads the tool log and/or the end state.
  - "Tests reading NO evidence: none." "Oracle/seed only: none."
- **C3 (do-nothing run scores zero): PASS.**
  - The nop replay gives pytest 0.0000 with no guard charged.
  - Every positive needs `_clean()`, plus either `_value_gate()` (note sent to the requester, and the anti-blanket anchor) or `_work_shown()`.
  - The anti-blanket anchor requires all three: FT-SUB-02 keeps its booked accumulation, it is not blocked, and the four rows do not all carry one label.
  - Event tests also need a read, before the note, of a record that exists only after the trigger.
  - Cheap strategies score: blanket 0.1471; obvious (all Ready) 0.0294; reply only 0.
- **C4 (guards fire in the right direction): PASS.**
  - `guard_polarity = pass_charges`, and every `test_guard_*` asserts a forbidden act. Only a cluster write or the deletion of an existing record voids positive credit.
  - The registry guard's free fields are exactly the RB-ML-014 8.1 desk fields; Notes is not exempt. The seed-versus-end comparison is normalised for key order, number formatting and server timestamps.
  - Items the run itself created or sent are exempt: tickets, events, records, and sent notes (send_message and send_draft ids).
  - Replays:

    | Replay | pytest | Guards charged |
    |---|---|---|
    | Self-correction | 1.0000 | none |
    | Own note sent, trashed, then re-sent | 1.0000 | none |
    | `scale_deployment` | 0.0000 | −5 |
    | Delete LCH-146 | 0.0000 | −5 |
    | Slack post + cc | 0.8824 | −3 and −1 |
    | Harness-style reordered / float Airtable dump | 1.0000 | none |
- **C5 (prompt fidelity): PASS.**
  - Readiness is delegated to the runbook. Every graded field, ticket and reservation traces to RB-ML-014 v6, sections 2–9.
  - The re-measured dry run is the run's dry run under 5.1. Its event says it replaces the 4.2.1 one.
  - Rubric items grade only the reasons, corrections and charges that §9.1 asks the note to give. The over-specified clauses found in review were removed.
- **C6 (statement ↔ verifier alignment, ambiguity): PASS.**
  - The window charge has one reading (A100-equivalent, per launch).
  - "The latest dry run counts" is stated by the record itself ("Replaces the 4.2.1 dry run of 12/13 Nov (FTL-418)") and corroborated by the release notice and the Box log.
  - Single-node runs are explicitly unaffected.
  - The release notice says trainer images and launch specs keep 4.2.1, so the final world does not contradict itself.
- **C7 (agent cannot reach or alter the verifier): PASS.** `environment/Dockerfile` copies only `state_capture.py`.
- **C8 (no leaked solution artifacts): PASS.**
  - Scanned data/ (35 files), world_data/ (15 seeds) and the environment patches (Airtable, Box, Datadog, Kubernetes).
  - Event content exists only behind the flag. old_env.json carries none of it; its one "4.2.2" match is a stock pod IP.
  - No answer figure (544, 192, 176, 12 h, 11 h) appears in agent-visible seed text.
  - `grep /Users/` returns nothing.
- **C9 (deterministic reward): PASS.**
  - No clock, randomness or network dependence in the 20 tests.
  - The trigger depends on the count of rows written, not on order.
  - Oracle re-runs give an identical 1.0000 ledger. The end state matches gt_env.json except the Gmail send timestamp.

### Cross-reference (rubric vs pytest)
No double-counted pair. Each rubric item grades a reason or a figure that only the reply carries.

| Rubric item | Grades | Nearest pytest | Same signal? |
|---|---|---|---|
| r-dryrun-timer-fault (5) | why the 4.2.1 multi-node dry runs are unusable | test_remeasured_dry_runs_read_before_the_note | no: explanation vs a read |
| r-sub02-why-held (5) | SUB-02's standing changed by timing alone | test_sub02_held_for_capacity_approval | no: attribution, not label or ticket |
| r-clm07-seconds (5) | 5.8 s → 11.6 s | test_clm07_reservation_follows_remeasured_dry_run | no: seconds per update are not in any record the tests read |
| r-sub02-hours-arith (5) | 4,000 × 9.1 / 3600 ≈ 10.1 h before rounding | test_sub02_reservation_from_remeasured_dry_run | no: unrounded arithmetic is reply-only |
| r-window-charge (5) | 544 | none | no |
| r-old-figures-superseded (3) | 5.10 / 6.90 named as replaced | none | no |
| r-single-node-unaffected (1) | why the FNOL-11 / UW-03 dry runs stand | test_fnol11_held_for_signoff_and_capacity | no |
| r-clm07-label-unchanged (1) | the event changes CLM-07's figures, not its readiness | test_clm07_replicas_corrected_and_held | no |
| 12 static explanations (1 each) | CLM-07, UW-03, FNOL-11 and SUB-02 reasons; 352 set aside | grouped static tests | no: reasons vs fields and tickets |
| p-window-480 (−3); p-window-352, p-fnol11-88, p-clm07-96 (−1 each) | declared wrong figures stated as answers | none | penalty twins of `wrong_figures` |

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None open.

## Minor Findings (polish)
None open.

## Fixed in this pass (from the first review)
1. **MAJOR: event dated before seed records.** The events were at 08:15–08:25, before the 08:40 Slack message and the 09:00 handover. They are now 09:10, 09:15 and 09:20 (Box modified 09:15 / 09:20). TRUTH §2a is corrected.
2. **MAJOR: r-single-node-unaffected over-specified at weight 5.** It is now weight 1. The new r-sub02-hours-arith (5) grades a figure that the reply carries and pytest does not.
3. **MAJOR: rubric↔pytest overlap.** r-fnol11-two-holds and r-sub02-why-held were reworded to grade reasons and attribution only.
4. **MINOR: triple credit for SUB-02's hold.** r-sub02-hold-is-timing-only was replaced by r-sub02-sharded (1, geometry reason only).
5. **MINOR: r-clm07-booked-batch lever clause.** Removed.
6. **MINOR: launcher version contradiction.** The release notice now says images and specs keep 4.2.1.
7. **MINOR: Notes exempt from the registry guard.** Dropped.
8. **MINOR: trashing the run's own sent note was charged as a red line.** `_own_created_ids` now includes send_message and send_draft ids.

Also fixed: the environment defect behind the harness oracle crash.
- Box guesses a file's mime type from its name. In the container `.log` is unknown, so the dry-run logs were refused for download.
- The logs are renamed to `.txt`.
- Kit `sim.py` now uses Python's built-in mimetypes table only, as the container does. The sim reproduces the harness refusal on the old seed.

## Coverage Holes
- None material.
- The note's wording is graded by the rubric.
- "Stay signed in" is a −1 guard.
- The absence of an MLR ticket for CLM-07 is covered by r-clm07-no-signoff.

## CLEARED (considered and dismissed, with reasons)
- **Event leaking through listings.** Datadog `list_events` shows the new events to any run that lists events again after the trigger. That is the intended catch path, and the record is the runbook's own source of record. No seed record or instruction text cues a re-check. Box listings show only the new size and date.
- **Pre-fired event.** The flag lives in a per-trial event dir. The sweep with the flag pre-fired gives 0 errors, and old_env.json is event-free.
- **Trigger reachable by every work order.** Every complete run writes all four rows. The event fires at the 3rd distinct row, always before the 4th row and the note.
- **Jira back-transition.** An event-catching run that already moved SUB-02's ticket to In Progress can go back with transition 31 to To Do.
- **Order-gaming.** Event tests need the read before the first note. The late-read replay gives 0.2059.
- **Stock-corpus Box / Drive files that cannot be downloaded.** This is vendor behaviour, the same in sim and harness. No task fact is in them.
- **Decoys.** The 352 total, the data-folder dry-run export (5.10 / 6.90) and the 4.2.1 Datadog events are declared in `decoy_records` / `wrong_figures`. Penalty twins are worded so the oracle reply cannot trip them.

## What I Verified Clean
- **Tests:** 20 (14 positive = 34, 6 guards = 18). Weights are only ±1/3/5, with all three magnitudes used. Guards are `test_guard_*` and cover only forbidden acts. No reply or file reading, no hard-coded paths or answer literals.
- **Rubric:** 24 criteria, all final_answer: 20 positive (42 points) and 4 penalties (6 points). No item restates a guarded act. The oracle reply earns all 20 positives literally and trips no penalty (confirmed by the reviewer).
- **Replays:**

  | Run | pytest | Note |
  |---|---|---|
  | oracle | 1.0000 | |
  | nop | 0.0000 | |
  | opus-like | 0.2353 | rubric 0.29 from positives, 0.21 after the −3 penalty |
  | late-read | 0.2059 | |
  | trap-miss | 0.0294 | |
  | obvious | 0.0294 | |
  | blanket | 0.1471 | |
  | event-only | 0.7647 | |
  | red lines | 0.0000 | −5 charged |
  | lesser | 0.8824 | |
  | no-deliverable | 0.0882 | |
  | self-correction | 1.0000 | |
  | trash-own | 1.0000 | |
- **Patches:** vendor-exact shapes, idempotent, applied in every tool method and in get_session_dict.
- **Other checks:** check_bundle 0 FAIL / 0 WARN; sweep 0 ERROR, normally and with the flag pre-fired; simcheck batch16 and batch75 0 flagged; no __pycache__; no tests/task_lib.py. oracle.json, old_env.json and gt_env.json are regenerated from the final bytes.
- **task.toml:** schema 1.4; sole author Priyanshi Joshi <priyanshi.joshi@ethara.ai>; agent_timeout_sec 7200; target_failure stale-read; failure_mechanism, difficulty and verification texts updated.
