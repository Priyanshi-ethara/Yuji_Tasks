# QC Report: 205f473f-c7e1-5bff-88b5-09e0e89b5356   layout: full   runs: 1   model(s): opus-5

This report applies `qc 2/traj/10_bundle_playbook.md` to a copy of the delivered bundle
(`TASKS/16Nov_Tasks/205f473f-c7e1-5bff-88b5-09e0e89b5356`, without QC/), with `BUNDLE` exported to that copy.

- **Scripts:** every script ran as written, from a scratch working directory: the §0 loader, §1, §1.5, §1.6, §2, §3, §4
  and §5. The raw output is in `03_playbook_script.txt`.
- **The run:** the only run is `trajectories/opus-5/run_1` (job
  `205f473f-c7e1-5bff-88b5-09e0e89b5356-opus-5-20261116-111050`, trial TDTmhge). It is the Opus 5 agent run on the
  final task bytes, with task_checksum `e0e779d4…f77a`, equal to the `dirhash` of the delivered task.
- **Reward file:** `verifier/reward.json` is trimmed to `{"reward": 0.2242}`, so the channels are read from report.json,
  as §0 allows. Every other file of the full layout is present.

## §1 Model
- **opus-5/run_1: ✅ agree.**
  - The folder and pass_summary say `opus-5`.
  - config says `anthropic/claude-opus-5`, result `claude-opus-5`, and report `opus-5 / anthropic/claude-opus-5`.
  - Every step says `['anthropic/claude-opus-5']`.
  - The script prints `distinct models after normalising ['opus-5'] ok` and `models seen mid-run 1 ok`.
- **Agent:** `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`.
- **Schema and effort:** `schema_version ATIF-v1.5 ok`; `reasoning_effort (config.agent.kwargs) high`.

## §1.5 Score sanity (per run)
- **1.5a:** the reward is 0.2242 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run
  (`spread=0.0 ok`).
- **1.5b:** the ledger is read from grade_report.json.
  - 21 rows, earned 11.0, penalty 0.0, total_positive 46, `pass_charges`, gate None.
  - Recompute: `0.2391 vs reported 0.2391 ok`.
  - Weighted 21 = ledger 21. No weight drift, guards tripped `[]`, 7 missed, no test raised.
- **1.5c:** the judge ran (`ran=True model=gpt-5.6-sol reason=None`).
  - Recompute: `0.2093 vs reported 0.2093 / channel 0.2093 ok`.
  - 22 answers (13 yes, 9 no), raw values `['no', 'yes']`, 0 errors.
  - judge.toml against the graded set: none missing, none extra, no weight or text drift. report.rubric count is 22 (ok).
- **1.5d:** no polarity mismatches. The source weights are +43 / −11, and the normalised positives sum to 1.0.
- **1.5e:** `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.2242 vs reward 0.2242 ok`.
- **1.5f:** `exception_info=None errored=False state_capture_failed=None agent_steps=79 last_step_source=agent`.
  - final_message.md has 9284 chars of text and is identical to the last agent text (`same=True`).
  - Tokens: 3,538,099 prompt (3,340,686 cached), 36,452 completion, $3.82, the same in final_metrics and agent_result.
- **Result:** no BLOCKER.

## §1.6 Aggregates
- **Counts:** `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`.
- **Threshold:** 0.7 in pass_summary, test_weights and pass@1.
- **Pass bits and averages:** no violations. The averages (0.2242 / 0.2391 / 0.2093) match the recomputed means.
- **pass@1.json:** passed 0 (recomputed 0), pass_rate 0.0, no reward_per_run drift, histogram `{'partial': 1}` summing to 1.
- **jobs.json:** lists only `…-opus-5-20261116-111050`, with 1 trial.
- **Flags:** `runs_without_rubric=[]`, `runs_with_state_capture_failed=[]`, `errored_run_indices=[]`, judge_models
  `['gpt-5.6-sol']`.
- **Result:** no BLOCKER.

## §2 Failure classification (per run)
- **opus-5/run_1:** passed False; reward 0.2242 < threshold 0.7; failure_mode `partial`.
- **2.1 environment: none.** end_env.json is shipped (2.1a), there is no exception and errored is False (2.1b), and the
  judge ran (2.1c). The run made 78 tool calls (70 MCP, 8 local), and 0 tool results look like server errors (2.1e).
- **Bucket B, sub-label `stale-read`.** Evidence comes from `trajectories/opus-5/run_1/agent/trajectory.json`,
  `report.json` and `verifier/final_message.md`:
  1. **The code host was read once, before the change landed.**
     - The only GitHub call is `LightGithub_login` at step 17. Its session dump lists PRs #3290…#3474 and no #3490.
     - The 21st distinct register row, the event trigger (`oracle.json event.trigger_rows = 21`), is written at
       step 67.
     - After that the run makes 1 more row write (68), 8 `create_issue` calls and 1 `update_issue` (69-77), one
       Airtable `list_records` re-read (78), and the Slack post (79).
     - No GitHub or Slack read follows step 67. No tool observation in the run contains any event marker
       (`#3490 is merged`, `internal/notify/ to Driver Comms`, …). The end-state dump (end_env.json) does contain
       them, so the change landed.
  2. **The missed tests are exactly the event tests.** These 7 tests, worth 35 of 46 (report.json `pytest.missed`), fail:
     - `test_3s6_…`, `test_4h6_…` and `test_5m2_…_follows_the_notify_line_on_main`: the register shows Messaging; the
       oracle wants Driver Comms.
     - `test_ticket_for_the_team_that_took_the_notify_groups` and `…_kept_only_its_queue_groups`;
     - `test_merged_ownership_change_looked_at_before_the_summary`;
     - `test_summary_follows_the_corrected_rows_and_tickets`.

     All 9 static tests pass (11 points, including the 3-point module-boundary read). The run wrote the oracle class on
     all 22 rows and the oracle owner on 19 of them.
  3. **The reply is built on the export.** final_message.md L15 says "Messaging | 5 — 3S6, 4H6, 4Q9, 5M2, 5R3".
     L25 says "Driver Comms exists in Okta and Linear but is *not* in the ownership file".
     - The judge answered no on the 7 event items (#1-#7). It charged r-pen-msg5 (−3) and did not charge r-pen-sim7 or
       r-pen-msg3.
     - The run says yes to all 12 static items (#8-#19).
- **The deciding record was reachable and returned correctly.** The judged harbor oracle on the same bytes
  (`QC/Oracle run`, trial ooThF6W) scored 1.0 / 1.0.
  - After its register writes, its GitHub `list_pulls` returned PR #3490 "CODEOWNERS: internal/notify/ to Driver Comms"
    (merged, with the in-place diff).
  - Its Slack read returned Petra's "#3490 is merged" note.
  - It passed `test_merged_ownership_change_looked_at_before_the_summary`, which needs a post-landing read whose response
    carries a marker.
- **Never-called servers (2.2c):** LightDatadog, LightGitlab, LightGmail, LightGoogleDrive, LightJira,
  LightMicrosoftTeams, LightNotion and LightPagerDuty. They are read-only context and decoys, and the final message never
  calls them unavailable or unnecessary. This is not tunnel vision: the server the run needed again (LightGithub) was
  called, just too early.
- **2.2d:** no guard tripped. The sub-label is neither `guard-tripped` nor `gave-up-early`: the final message reports
  every write as done and admits no stop.

## §2.5 Isolation and leakage (per run)
- **Verifier mode:** `verifier_environment_mode` is `"separate"` (result.json).
- **Grader paths touched by the agent:** none. The pattern
  `/tests|test_outputs.py|test_weights.json|judge.toml|reward|solution/|TRUTH.md|gt_env.json|oracle.json` has 0 hits
  across the arguments of all 78 tool calls.
- **Leakage in tool results:** none.
  - The event content (PR #3490, its review comments, the #fleetd-dev merge note) lives only in the patch blocks of
    `software/LightGithub/github.py` and `software/LightSlack/slack.py`. Those apply only after the flag fires.
  - `grep` for `3490` / `is merged:` over task_data, world_data and instruction.md finds nothing.
  - The run never received the event content.
- **Trivial-solution credit:** none. The run made 22 register writes, filed 8 tickets and posted 1 summary. The judged
  nop on the same bytes scored 0 / 0 / 0.

## §3 Reasoning
- 79 agent steps, 17 of them with reasoning (14,141 chars), in field `thought`. reasoning_effort is `high`. Verdict: ✅ present.
- Per-step metrics are on 0 of 79 steps. This is INFO: the totals are in `final_metrics`.

## §4 Overlap
- **Matcher counts:** 21 tests vs 22 criteria. `DOUBLE-COUNTED=3 PARTIAL=3 INDEPENDENT=15 redundancy=14%`. 20 of the 22
  criteria are rubric-only.
- **The three DOUBLE-COUNTED rows, read both ways:** S1 (name similarity) is 0.27-0.39 on each, and S2 (literals) is
  1.00.
  - `test_nil_pointer_classes_follow_the_code` (1) vs #16 r-decline (+1). The only shared literals are the ids 4V1, 4W6
    and 4X2.
    - The test compares the register's `Root cause` with `oracle.json` (`_all_right`).
    - r-decline grades the reason in the reply ("because Error() is called directly on the concrete *DeclineError field
      … no error interface is involved"). The instruction asks for that reason separately: "for the nil-pointer
      crashes, why each got the class it got".
    - The register cannot earn r-decline, and a reply cannot earn the test.
  - `test_simkit_ticker_groups` (1) and `test_simkit_ring_scheduler_and_clock_groups` (1) vs #9 r-simkit-groups (+1).
    The shared literals are group ids.
    - The tests compare the owner and class on the register.
    - The criterion grades whether the reply names the frame below the simkit frames as the deciding one, which answers
      "which frames you stepped over and why". It states no owner.
  - **Disposition:** not double-counted. These are seeded identifiers shared between a state check and an explanation
    check. Each weighs 1 point of 46 (pytest) or 1 of 43 (rubric). §4 findings are MAJOR at most, and this one is cleared
    with the reasons above. The same pairs were cross-referenced as "no" in 02_Ruthless.
- **PARTIAL rows:** `test_vendored_and_generated_tops_stepped_over` vs #13 (0.67), and the 4H6 and 5M2 event tests vs #4
  and #3 (0.50).
  - The tests grade the register owner.
  - #3 and #4 grade that the reply connects the frame to the merged notify line on main.
  - Since the hardening pass, they carry no owner wording (02_Ruthless, "Fixed in this pass").
  - In this run both channels failed on the event pair, for different reasons: the register held Messaging, and the
    reply never mentioned the merge. That is consistent with one missed fact producing two independent signals.
- **Lost weight:** pytest positive lost 35/46 = 76.1%, guards charged 0.0. Rubric positive lost 0.7209 = 72.1%,
  penalties charged 0.0698.
- **Manual strict read (owner rule):** no rubric item restates a guarded act, a tool call, a ticket list, a per-team or
  per-class count, or an owner value. The three penalties are the declared `wrong_figures` twins.
- **Recommendation:** `keep both`.

## §5 False pytests
- **Scan:** 21 tests, 0 flagged (`0/21 tests carry a flag; BLOCKER flags: 0`). 5.2 lists no assert or return line that
  carries a rubric figure.
- **Pass bits:** the run's pass bits match the ledger. Each test also has real evidence on both sides: the judged oracle
  passes all 16 positives and the nop passes none.

## Verdict
- **SIGNED.**
  - No BLOCKER in §1, §1.5, §1.6 or §2.5.
  - §2 is Bucket B `stale-read`, a genuine model failure with no guard tripped. It is neither guard-tripped nor
    gave-up-early, and no environment or task defect was found.
  - §3 reasoning is present.
  - §4's three literal matches are cleared above (shared seeded ids, different signals).
  - §5 has 0 flags.
