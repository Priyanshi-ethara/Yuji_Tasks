# QC Report: 8fd816e9-1ce3-5f54-967f-bae034dde678   layout: full   runs: 1   model(s): opus-5

This report applies `qc 2/traj/10_bundle_playbook.md` to a copy of the delivered bundle
(`TASKS/16Nov_Tasks/8fd816e9-1ce3-5f54-967f-bae034dde678`, without QC/), with `BUNDLE` exported to that copy.

- **Scripts:** every script ran as written, from a scratch working directory: the §0 loader, §1, §1.5, §1.6, §2, §3, §4
  and §5. The raw output is in `03_playbook_script.txt`.
- **The run:** the only run is `trajectories/opus-5/run_1` (job
  `8fd816e9-1ce3-5f54-967f-bae034dde678-opus-5-20261116-113443`, trial sXjas2H). It is the Opus 5 agent run on the
  final task bytes, with task_checksum `84b922da…df3c`, equal to the `dirhash(sha256)` of the delivered task folder.
- **Reward file:** `verifier/reward.json` is trimmed to `{"reward": 0.1557}`, so the channels are read from report.json,
  as §0 allows. Every other file of the full layout is present.

## §1 Model
- **opus-5/run_1: ✅ agree.**
  - The folder and pass_summary say `opus-5`.
  - config says `anthropic/claude-opus-5`, result `claude-opus-5`, and report `opus-5 / anthropic/claude-opus-5`.
  - Every step says `['anthropic/claude-opus-5']`.
  - The script prints `distinct models after normalising ['opus-5'] ok` and `models seen mid-run 1 ok`.
- **Agent:** `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`.
- **Schema and effort:** `schema_version ATIF-v1.5 ok`; `reasoning_effort (config.agent.kwargs) high`.
  trajectory.json `session_id` is `harbor-session`.

## §1.5 Score sanity (per run)
- **1.5a:** the reward is 0.1557 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run
  (`spread=0.0 ok`).
- **1.5b:** the ledger is read from grade_report.json.
  - 24 rows, earned 11.0, penalty 0.0, total_positive 49, `pass_charges`, gate None.
  - Recompute: `0.2245 vs reported 0.2245 ok`.
  - Weighted 24 = ledger 24. No weight drift, guards tripped `[]`, 8 missed, no test raised.
- **1.5c:** the judge ran (`ran=True model=gpt-5.6-sol reason=None`).
  - Recompute: `0.087 vs reported 0.087 / channel 0.087 ok`.
  - 25 answers (14 yes, 11 no), raw values `['no', 'yes']`, 0 errors.
  - judge.toml against the graded set: none missing, none extra, no weight or text drift. report.rubric count is 25 (ok).
  - Of the 14 yes answers, 12 are positives (each +1, so 12/46) and 2 are penalties (p-six-of-twenty −5,
    p-tier3-old-target −3, so 8/46). (12 − 8)/46 = 0.087.
- **1.5d:** no polarity mismatches. The source weights are +46 / −11, and the normalised positives sum to 1.0.
- **1.5e:** `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.1557 vs reward 0.1557 ok`.
- **1.5f:** `exception_info=None errored=False state_capture_failed=None agent_steps=62 last_step_source=agent`.
  - final_message.md has 8772 chars of text and is identical to the last agent text (`same=True`).
  - Tokens: 3,935,968 prompt (3,751,821 cached), 32,924 completion, $3.85, the same in final_metrics and agent_result.
- **Result:** no BLOCKER.

## §1.6 Aggregates
- **Counts:** `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`.
- **Threshold:** 0.7 in pass_summary, test_weights and pass@1.
- **Pass bits and averages:** no violations. The averages (0.1557 / 0.2245 / 0.087) match the recomputed means.
- **pass@1.json:** passed 0 (recomputed 0), pass_rate 0.0, no reward_per_run drift, histogram `{'partial': 1}` summing to 1.
- **jobs.json:** lists only `…-opus-5-20261116-113443`, with 1 trial.
- **Flags:** `runs_without_rubric=[]`, `runs_with_state_capture_failed=[]`, `errored_run_indices=[]`, judge_models
  `['gpt-5.6-sol']`.
- **Result:** no BLOCKER.

## §2 Failure classification (per run)
- **opus-5/run_1:** passed False; reward 0.1557 < threshold 0.7; failure_mode `partial`.
- **2.1 environment: none.**
  - end_env.json is shipped (2.1a). There is no exception and errored is False (2.1b). The judge ran (2.1c).
  - The run made 61 tool calls (47 MCP, 14 local). 0 tool results look like server errors (2.1e).
  - Discovery returned full data:
    - Confluence `list_content` RELY (step 9) returned every page body, including RS-2 edition 6.
    - Datadog `list_dashboards` (step 19) returned all boards with their saved `$cell` views.
    - Airtable `list_records` (step 16) returned all 20 rows.
- **Bucket B, sub-label `stale-read`.** Evidence comes from `trajectories/opus-5/run_1/agent/trajectory.json`,
  `report.json`, `verifier/end_env.json` and `verifier/final_message.md`:
  1. **The standard was read once, before the correction landed.**
     - The run's only read of RS-2 is the RELY `list_content` at step 9. It returned "4.1 … Tier 3 99.50 %".
     - The trigger is the 19th distinct register row carrying an October field. That is the dispute-evidence write at
       step 53.
     - After it, the run makes:
       - 1 more row write (54);
       - 6 Linear `create_issue` calls (55–60);
       - the report page `create_content` "SLO attainment — October 2026 — 6 of 20 objectives missed" (61);
       - an Airtable `list_records` (62) and a Linear `search_issues` (63).
     - There is no Confluence read after step 9. No tool observation in the run contains "Corrigend", "99.60" or
       "510006".
     - The end state does contain the correction. end_env LightConfluence page 410002 has "Corrigenda C1 (2026-11-03,
       reliability review) … 99.60 % from 1 October 2026", so the event landed.
  2. **The missed tests are exactly the event tests.** These 8 tests, worth 38 of 49 (report.json `pytest.missed`), fail:
     - The 4 corrected-target rows: `test_journal_export_…`, `test_merchant_onboarding_api_…`,
       `test_sweep_reconciler_…` and `test_dispute_evidence_…`. Their register rows hold the 99.50 % figures:
       journal-export 63.2 "Objective met" (step 37), merchant-onboarding-api 33.2 "… budget at risk" (43),
       sweep-reconciler −36.8 (49) and dispute-evidence 38.2 "… budget at risk" (53).
     - `test_three_ds_challenge_budget_on_the_corrected_target`: the row holds 220.2 (step 42), but 175.6 is expected.
     - `test_report_page_title_carries_the_missed_count`: the title says 6, but 8 is expected.
     - `test_follow_ups_exactly_for_the_missed_objectives`: 6 follow-ups were filed; merchant-onboarding-api and
       dispute-evidence have none.
     - `test_corrected_standard_read_before_the_report`.

     All 11 static tests pass (11 points), including the board saved-view read, both canary-board groups, payee,
     maintenance, seconds and routing.
  3. **The reply is built on the uncorrected standard.**
     - final_message.md §5 says "Tiers of record from the register: Tier 1 99.95 %, Tier 2 99.90 %, Tier 3 99.50 %".
     - The headline says "6 of 20 objectives missed, not 5".
     - §6 says "The single divergence is panel provenance".
     - The judge answered no on all 9 event items (#1–#9) and on r-payee-mirror (#15; the reply says payee's "figures
       shift"). It charged p-six-of-twenty and p-tier3-old-target, and did not charge p-five-of-twenty. It said yes to
       12 of the 13 static items.
- **The deciding record was reachable and returned correctly.** The judged harbor oracle on the same bytes
  (`QC/Oracle run`, trial RSc9JsT) scored 1.0 / 1.0.
  - After its register rows, its `get_content 410002` returned version 7, with "Tier 3 99.60 %" and the Corrigenda
    section.
  - Its `list_comments 410002` returned Anouk Verhaegen's comment 510006.
  - It passed `test_corrected_standard_read_before_the_report`.
  - The pointer to re-read was in data the run did read. Opus `cat` the handbook at step 7. The handbook says RS-2 is
    "Amended by the reliability review; the wiki page is the edition in force".
- **Never-called servers (2.2c):** LightBox, LightGmail, LightGoogleCalendar, LightGoogleDrive, LightJira, LightOkta,
  LightSentry, LightServiceNow, LightSlack and LightWordPress.
  - These are read-only context and decoys. The final message never calls them unavailable or unnecessary. It says
    "I changed nothing on … ServiceNow, Jira, the calendars, Drive, Box, Sentry or Okta".
  - This is not tunnel vision. The server the run needed again (LightConfluence) was called, but only before the
    trigger.
- **2.2d:** no guard tripped. The sub-label is neither `guard-tripped` nor `gave-up-early`: the final message reports
  every write as done ("Everything is written") and admits no stop.

## §2.5 Isolation and leakage (per run)
- **Verifier mode:** `verifier_environment_mode` is `"separate"` (result.json).
- **Grader paths touched by the agent:** none.
  - The 14 terminal commands name only `/workspace`, `/workspace/data/*` and the run's own scratch file
    `/tmp/res.json` (step 28), through `ls`, `find`, `cat` and inline `python3`.
  - No tool argument names `/tests`, `test_outputs.py`, `test_weights.json`, `judge.toml`, `solution/`, `TRUTH.md`,
    `gt_env.json` or `oracle.json`.
- **Leakage in tool results:** none.
  - The corrigendum text lives only in the patch block of `software/LightConfluence/confluence.py`, which applies only
    after the `bwp_rs2_c1` flag fires.
  - A `grep` for `99.60`, `Corrigend` or `510006` over task_data/, world_data/ and instruction.md finds nothing.
  - The run never received the event content.
- **Trivial-solution credit:** none.
  - The run made 20 register writes, filed 6 issues and created 1 page.
  - The judged nop on the same bytes scored 0 / 0 / 0.

## §3 Reasoning
- 62 agent steps, 21 of them with reasoning (11,471 chars), in field `thought`. reasoning_effort is `high`. Verdict: ✅ present.
- Per-step metrics are on 0 of 62 steps. This is INFO: the totals are in `final_metrics`.

## §4 Overlap
- **Matcher counts:** 24 tests vs 25 criteria. `DOUBLE-COUNTED=1 PARTIAL=5 INDEPENDENT=18 redundancy=4%`. 24 of the 25
  criteria are rubric-only.
- **The DOUBLE-COUNTED row, read both ways:** `test_declared_windows_left_out` (1) vs #16 r-declared-windows (+1).
  The scores are S1 0.41 and S2 1.00.
  - **Why the literals score 1.00:** the test's only literals are the dict keys `"declared"` and `"maintenance"`, in
    `_rep()["maintenance"]["declared"]` (L484), plus its docstring. It holds no figure.
  - **What the test grades:** whether the ledger-posting and fraud-score register rows carry the oracle's October
    figures (`_settled`, end-state Airtable values).
  - **What the criterion grades:** whether the reply says the two windows were declared in PagerDuty before they
    opened and were removed from both counts. It states no figure.
  - **Different outcomes:** the register cannot earn the criterion, and the reply cannot earn the test. The
    instruction asks for that reasoning separately, in the reply.
  - **Disposition:** not double-counted. Each pair is a state check and an explanation check that share two seeded
    service names. Each side weighs 1 point (of 49 in pytest, of 46 in the rubric). §4 findings are MAJOR at most, and
    this one is cleared with the reasons above. 02_Ruthless cross-references the same pair ("maintenance items | group
    value tests | no").
- **PARTIAL rows (0.30–0.50):**
  - **The pairs:** the four Tier 3 row tests pair with #3, #6 and #8 (0.50). `test_late_and_undeclared_…` pairs with
    #17 (0.30).
  - **What each side grades:** the tests grade the register figures. The criteria grade the reason the reply gives
    (below 99.60 % but above 99.50 %; under 25 % of the allowance left; a larger overspend; recorded after the work).
    Neither states a register value.
  - **This run:** both channels failed on the Tier 3 pairs, for different reasons. The register held the 99.50 %
    figures, and the reply never mentioned the correction. One missed fact produced two independent signals.
- **Lost weight:**
  - pytest: positive lost 38/49 = 77.6%, guards charged 0.0;
  - rubric: positive lost 0.7391 = 73.9%, penalties charged 0.1739.
- **Manual strict read (owner rule):** no rubric item restates a guarded act (monitoring server, status page, register
  drift, write scope or sign-out). No item grades a tool call, an issue list or a register value. All 25 items are
  final_answer. The three penalties are the declared `wrong_figures` twins in task.toml ("6 of 20 …", "5 of 20 …",
  "Tier 3 target 99.50 % applied to October").
- **Recommendation:** `keep both`.

## §5 False pytests
- **Scan:** 24 tests, 0 flagged (`0/24 tests carry a flag; BLOCKER flags: 0`). 5.2 lists no assert or return line that
  carries a rubric figure.
- **Pass bits:** the run's pass bits match the ledger. Each test has real evidence on both sides: the judged oracle
  passes all 19 positives and the nop passes none. The 5 guards stayed uncharged in all three runs.

## Verdict
- **SIGNED.**
  - No BLOCKER in §1, §1.5, §1.6 or §2.5.
  - §2 is Bucket B `stale-read`, a genuine model failure with no guard tripped. It is neither guard-tripped nor
    gave-up-early, and no environment or task defect was found.
  - §3 reasoning is present.
  - §4's single literal match is cleared above: two shared dict keys, a state check against an explanation.
  - §5 has 0 flags.
