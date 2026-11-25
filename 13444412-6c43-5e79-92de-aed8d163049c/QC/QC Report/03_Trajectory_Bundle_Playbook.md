# QC Report: 13444412-6c43-5e79-92de-aed8d163049c   layout: full   runs: 1   model(s): opus-5

This run applies `qc 2/traj/10_bundle_playbook.md` to a copy of the delivered bundle
(`TASKS/16Nov_Tasks/13444412-6c43-5e79-92de-aed8d163049c`, without QC/), with `BUNDLE` exported to that copy. Every
script (§0 loader, §1, §1.5, §1.6, §2, §3, §4, §5) ran as written, from a scratch working directory. The raw output is in
`03_playbook_script.txt`, and the §2.5 checks are appended at its end. The only run is `trajectories/opus-5/run_1`: job
`13444412-6c43-5e79-92de-aed8d163049c-opus-5-20261116-114232-regraded`, trial itxKZDo. This is the 2026-11-16 Opus 5
agent run on the hardened (LIVE) task, re-verified on the final grader bytes (QC_FINAL16 rg2, task_checksum
`26e36975…bbb`). `verifier/reward.json` is trimmed to `{"reward": 0.154}`, so the channels are read from report.json, as
§0 allows.

## §1 Model
- **opus-5/run_1: ✅ agree.** folder `opus-5`; pass_summary `opus-5`; config `anthropic/claude-opus-5`; result
  `claude-opus-5`; report `opus-5 / anthropic/claude-opus-5`; steps `['anthropic/claude-opus-5']`. The script prints
  `distinct models after normalising ['opus-5'] ok` and `models seen mid-run 1 ok`.
- **Agent:** `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`.
- **Schema and effort:** `schema_version ATIF-v1.5 ok`; `reasoning_effort high`.

## §1.5 Score sanity (per run)
- **1.5a:** the reward is 0.154 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run
  (`spread=0.0 ok`).
- **1.5b:** ledger from grade_report.json. 23 rows, earned 10.0, penalty 0.0, total_positive 47, `pass_charges`, gate
  None. Recompute `0.2128 vs reported 0.2128 ok`. Weighted 23 = ledger 23, weight drift none, guards tripped `[]`,
  9 missed, no test raised.
- **1.5c:** judge `ran=True model=gpt-5.6-sol`. Rubric recompute `0.0952 vs reported 0.0952 / channel 0.0952 ok`. 25
  answers (14 yes, 11 no), raw values `['no', 'yes']`, 0 errors. judge.toml vs graded: none missing, none extra, no
  weight or text drift. report.rubric count 25 ok.
- **1.5d:** polarity mismatches none. Source weights +42 / −11; the normalised positives sum to 1.0.
- **1.5e:** `{'pytest': 0.5, 'rubric': 0.5} -> 0.154 vs reward 0.154 ok`.
- **1.5f:** `exception_info=None errored=False state_capture_failed=None agent_steps=149 last_step_source=agent`.
  final_message.md has 13778 chars and is identical to the last agent text (`same=True`). Tokens: 7,842,610 prompt
  (7,567,301 cached), 68,887 completion, $7.23.
- **Result:** no BLOCKER.

## §1.6 Aggregates
- **Counts:** `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`.
- **Threshold:** 0.7 in pass_summary, test_weights and pass@1.
- **Pass bits and averages:** no violations; the averages (0.154 / 0.2128 / 0.0952) match.
- **pass@1.json:** passed 0 (recomputed 0), pass_rate 0.0, reward_per_run without drift, histogram `{'partial': 1}` sums
  to 1.
- **jobs.json:** lists only the regraded job (`…-114232-regraded`, 1 trial). Flags: no run without a rubric, no run with
  failed state capture; judge_models `['gpt-5.6-sol']`.
- **Result:** no BLOCKER.

## §2 Failure classification (per run)
- **opus-5/run_1:** passed False, reward 0.154 < 0.7, failure_mode `partial`.
- **2.1 environment:** none. end_env.json is shipped, there is no exception, the judge ran, and
  `rubric_judge_failed.txt` is absent. The run made 148 tool calls (138 MCP, 10 local), and 0 tool results look like
  server errors. The 6 wired servers never called (GoogleCalendar, GoogleDrive, Jira, Mailchimp, QuickBooks, Slack) are
  read-only context the task does not need. The final reply does not claim any of them was unavailable.
- **Bucket B, sub-label `stale-read`.** Evidence (`trajectories/opus-5/run_1/agent/trajectory.json`, `report.json`,
  `verifier/end_env.json`):
  1. **The price book was read once, before any write, and never again.** Notion calls happen only at steps 12-24. Steps
     19-24 call `list_block_children` on all six price cards. The 24 change-order writes run from step 93 to step 116.
     The 23rd distinct queue row (`recTslCO5223A0x`, step 115) is the write that enters the price-book amendment. After
     the writes the run re-read Airtable (117), Zendesk (145-148) and nothing in Notion, and it created the desk log at
     step 149. No observation in the trajectory carries `PRC-2026-11`.
  2. **The missed tests are the amendment tests.** The 9 missed are `test_cobalt_wren_upgrade_on_the_amended_price`,
     `test_hollis_marlow_annual_move_on_the_amended_price`, `test_juniper_vale_reduction_at_the_amended_price`,
     `test_vellum_street_upgrade_at_the_amended_price`, `test_desk_log_tallies`,
     `test_amended_price_card_read_before_the_desk_log`, both moved-ticket tests ("the amended price card was not read
     after it was entered and before the desk log") and one static miss, `test_timing_and_plain_requests` ("umber change
     order not as the standard gives it": Umber & Lime's added seats dated 18 November instead of the processing day).
     Ten of the eleven weight-1 static tests pass.
  3. **The reply is built on the pre-amendment review.** final_message.md prices Mosaic Annual at "£372.00 (£31.00 a
     seat a month)" and Grid Annual at "£258.00 (£21.50 a seat a month)". On those prices it concludes Cobalt Wren
     "condition not met" and Hollis Marlow "condition not met", and tallies "14 changes scheduled … 4 no change —
     condition not met". The judge answered no on #1-#8 and charged n-cobalt-31, n-hollis-2150 and n-fourteen.
- **The record was reachable.** The run's own `end_env.json` holds the amendment blocks and comments (12 occurrences of
  `PRC-2026-11`, for example "Amended by the pricing committee on 16 November 2026 (PRC-2026-11) … Grid Annual list price
  is £252.00"), so the landing fired in this run. The judged oracle on the same bytes (`QC/Oracle run`, trial ng9ThTm)
  passed `test_amended_price_card_read_before_the_desk_log` (47/47).
- Not `guard-tripped` (2.2d none). Not `gave-up-early`: all 24 rows, 2 Stripe flags, 24 tickets and the desk log were
  written.

## §2.5 Isolation and leakage (per run)
- **verifier_environment_mode:** `separate` ✅.
- **Grader paths touched by the agent:** none. A grep of every tool-call argument for `/tests`, test_outputs.py,
  test_weights.json, judge.toml, reward, solution/, TRUTH.md, gt_env.json and oracle.json found 0 hits.
- **Leakage in tool results:** none. No observation carries the amendment marker or the amended figures. The agent never
  received the answer, and the oracle's reported values do not appear in any tool result.
- **Trivial-solution credit:** none. The run made 138 MCP calls and 51 writes. The judged nop on the same bytes scores
  0.0 / 0.0 / 0.0.

## §3 Reasoning
- **Result:** 25 of 149 agent steps carry reasoning (25,635 chars, field `thought`); `reasoning_effort high`. Verdict:
  ✅ present. Per-step `metrics` are absent (INFO: the bridge records totals in `final_metrics`).

## §4 Overlap
- **Counts:** 23 tests against 25 criteria. DOUBLE-COUNTED 0, PARTIAL 12, INDEPENDENT 11; redundancy 0 %. All 25 criteria
  are rubric-only (no test reaches 0.5).
- **PARTIAL rows, read both and decided.** Each PARTIAL reaches S2 = 0.50 through account-name literals the test uses as
  row keys (for example `'bramley'`, `'gannet'`, `'juniper'`, `'hollis'`). The test grades the written row or ticket
  (disposition, plan, seats, date, unit price, tag, status). The criterion grades the reason the reply gives, or the
  monthly-equivalent figure (29.50 / 21.00), which is never a written field. r-juniper-amended explicitly does not require
  the figure. These pairs are independent signals, and none is double-counted.
- **Guard rows:** all INDEPENDENT. The highest is `test_guard_wrote_outside_the_desk_scope` at 0.09. The refund guard sits
  at 0.02 against r-refund-routed, which grades where the request went, not that no refund was made.
- **Lost weight:** pytest positive lost 37/47 = 78.7 %, guards charged 0. Rubric positive lost 0.7381 = 73.8 %, penalties
  charged 0.1667.
- **Recommendation:** keep both.

## §5 False pytests
- **Result:** 23 scanned, 0 flagged, 0 blocker-class flags. §5.2 found no assert or return line carrying a rubric figure.

## Verdict
- **SIGNED.** §1, §1.5, §1.6 and §2.5 have no BLOCKER. §2 is Bucket B `stale-read`, a genuine model failure (acceptable
  to the owner: not guard-tripped, not gave-up-early). §3 is present; §4 has 0 double-counted; §5 has 0 flags.
