# QC Report: c9ebfbd9-7b5c-509d-bf31-c6789ca5bc0c   layout: full   runs: 1   model(s): opus-5

**How the playbook was run.** Playbook: `/Users/mac/Desktop/Trinity_Final/qc 2/traj/10_bundle_playbook.md`.
- I extracted all eight bash blocks verbatim: the loader, §1, §1.5, §1.6, §2, §3, §4 and §5. Each is byte-identical
  (`cmp`) to the copy used for the earlier pass. I ran them unchanged, from a scratch working directory.
- `BUNDLE` was exported to a fresh scratch copy of the final delivery folder `30_tasks/c9ebfbd9-…` (QC/ excluded).
- The copy was taken after `run_1/verifier/reward.json` was trimmed to `{"reward": 0.2928}`.
- Run date: 2026-11-12, about 15:35 IST. Every script exited 0. Raw output is in `03_playbook_script.txt`.

**Which run and which tests.** run_1 is the regraded trial: job
`c9ebfbd9-7b5c-509d-bf31-c6789ca5bc0c-opus-5-20261112-080111-regraded`, trial `6r24bG2`.
- Its source trial is `…-opus-5-20261112-080111/6r24bG2`. It was regraded on the final task bytes, after grader-only fixes,
  at 09:37:52Z–09:39:57Z.
- The shipped `jobs.json` and run_1 `result.json` carry task_checksum `66aea4de…2089d`. The final oracle and nop trials
  carry the same checksum (`/tmp/qc/oracle_nop_20261114_203752/c9ebfbd9-…/`, trials bmbeCAW / zpRTYE8). So the run is
  graded by the tests that ship.

**The agent-visible inputs did not change between the run and the final bundle.**
- The source trial ran on the build with task_checksum `56cd3e12…dcc7`: started 08:01:15Z, agent phase 08:02:48Z–08:18:05Z.
- The oracle/nop calibration `/tmp/qc/oracle_nop_20261112_132628` carries that same checksum. Its
  `_copies/c9ebfbd9-…` is therefore the exact build the agent ran on.
- `diff -rq` between that copy and the delivered bundle lists only four files:
  - `tests/test_outputs.py`;
  - `solution/TRUTH.md`;
  - `solution/gt_env.json`: only `LightSlack/output/messages[15]/ts` differs;
  - `task.toml`: only `verification_explanation` differs.
- These are byte-identical: `instruction.md`, all of `environment/` (the six patched servers, task_data and world_data
  included), `tests/test_weights.json`, `tests/oracle.json`, `tests/old_env.json` and the compiled `judge.toml`.
- The regrade reused the source trial's evidence. `agent/trajectory.json`, `verifier/final_message.md`, `end_env.json`,
  `agent_trajectory.json` and `server_tool_calls.log` are all `cmp`-identical to the source trial's.

## §1 Model
- opus-5/run_1: ✅ **identity confirmed.** The model is the same in every file:
  - the folder is `opus-5`, and pass_summary.model is `opus-5`;
  - config.agent.model_name is `anthropic/claude-opus-5`;
  - result model_info is `claude-opus-5`;
  - report is `opus-5 / anthropic/claude-opus-5`;
  - every agent step has `['anthropic/claude-opus-5']`.
  - Output: `distinct models after normalising ['opus-5'] ok`, `models seen mid-run 1 ok`.
- **ATIF and agent version.** `schema_version ATIF-v1.5 ok`. Agent:
  `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`.
  `reasoning_effort` is `high`. `tool_definitions` is None, which is INFO because the bridge does not record it. There is no
  "unknown" version.

## §1.5 Score sanity (per run)
- **1.5a.** reward 0.2928 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run:
  `spread=0.0 ok`. reward.json is trimmed to `{reward}`, so the channels come from `report.json.channels`, as the loader
  allows.
- **1.5b.** From grade_report.json:
  - rows=30, earned=20.0, penalty=0.0, total_positive=58, guard_polarity=pass_charges, gate=None;
  - `pytest recompute 0.3448 vs reported 0.3448 ok`;
  - weighted tests vs ledger rows 30/30, no weight drift;
  - guards tripped `[]`, 8 missed; no test raised.
- **1.5c.** The judge ran (`ran=True model=gpt-5.6-sol`).
  - `rubric recompute 0.2407 vs reported 0.2407 / channel 0.2407 ok`.
  - n=26: 15 yes and 11 no, raw values `['no', 'yes']`, 0 errors.
  - The 15 yes are 14 positives (16 points) and one penalty: p-stale-outcomes, −3.
  - judge.toml vs graded: none missing, none extra, no weight or text drift. report.rubric count 26 (ok).
- **1.5d.** Polarity mismatches: none. Source weights positive=54 and penalty=8; the normalised positives sum to 1.0.
- **1.5e.** `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.2928 vs reward 0.2928 ok`.
- **1.5f.** The run completed:
  - exception_info=None, errored=False, state_capture_failed=None;
  - 138 agent steps, last step source `agent`;
  - final_message.md is 8,538 chars, the same as the last agent text (`same=True`);
  - final_metrics: 16,881,971 prompt / 68,417 completion / 16,601,221 cached tokens, $11.77, equal to `agent_result`.
- No BLOCKER and no MAJOR, so no `SIGNOFF_BLOCKED`.

## §1.6 Aggregates
- **Counts and pass rule.** `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`. Threshold is 0.7 in pass_summary,
  test_weights and pass@1 (ok). per_run.combined equals the run reward. Pass-rule violations: none (passed=false,
  0.2928 < 0.7).
- **Averages, recomputed.** combined 0.2928, pytest 0.3448, rubric 0.2407, all ok. Flags: runs_without_rubric `[]`,
  runs_with_state_capture_failed `[]`, errored_run_indices `[]`, judge_models `['gpt-5.6-sol']`.
- **pass@1.json and jobs.json.** passed 0 (recomputed 0), pass_rate 0.0, reward_per_run has no drift, and the histogram
  `{'partial': 1}` sums to 1 (ok). jobs.json is `[('…-opus-5-20261112-080111-regraded', 1)]`. No `AGGREGATE_UNRELIABLE`.

## §2 Failure classification (per run)
- opus-5/run_1 did not pass: reward 0.2928 against threshold 0.7, failure_mode `partial`.
  **Bucket B (model/agent), sub-label `stale-read`.**
- **The environment was healthy:**
  - end_env.json shipped and state capture did not fail; there was no exception; the judge ran.
  - 137 tool calls: 111 MCP and 26 local. `2.1e tool results that look like server errors 0`.
  - I also searched for `"status":"failed"` results, which the 2.1e regex does not match. There are exactly 2: Jira
    `create_issue` at steps 96 and 97, both answered `Invalid assignee`. Opus had added an optional `assignee` the prompt
    never asks for ("Dr Rowan Achterberg", then "rowan.achterberg@tarnwick-bio.example"). It dropped the field at step 98,
    and QAD-409 was created. This is the agent's own argument error, recovered in one step. It costs no graded item (the
    deviation tests pass) and is not an environment fault.
  - The wired-but-never-called servers (Datadog, FedEx, MicrosoftTeams, PagerDuty, Salesforce, ServiceNow, Zendesk) are
    read-only or decoy surfaces the task does not need. The final message does not say they were unavailable.
- **Evidence:**
  1. **Event 2 fired, and its records are in the end state.** It triggers on the 18th distinct round-card write, which Opus
     made at step 125 (`update_card` 62d2…4518, OSV-260101). `run_1/verifier/end_env.json` holds Box file 50450006 as
     "As-found certificate, logger TK9-5521 (issue 2, 2026-11-10)", modified 2026-11-10T13:05Z. It also holds the Metrology
     mail `msg-twk-4512` ("I have reissued the certificate … sensor-fault window 2026-11-05T03:20Z to 2026-11-05T03:50Z"),
     still `is_unread: true`.
  2. **Opus never re-read the certificate or the mailbox after the 18th card.** Its only Box `download_file` calls are at
     steps 34–43, before any card write. Its Gmail reads are at steps 50–59, 104 and 107. Its step-135 thought plans the
     final checks as "re-check the Polar Arc drop … re-check the live ERP ledger … confirm the lot statuses are untouched".
     Metrology's certificates, which the instruction names as an authoritative record, are not on that list. It then
     posted the closing note at step 137.
  3. **All 8 missed positives (2.2e) are event 2:**
     - the three HX4-41207 card tests (CVM-260417, FRT-260230, OSV-260097);
     - the two re-worded-deviation tests;
     - the rework order;
     - the headline counts;
     - `test_certificates_read_again_before_closing`.
     Rubric criteria 1–7 and 9 are no for the same reason. The reply reports FRT-260230 as Referred at 76.04 % and
     OSV-260097 as Reject at 36.50 h / 101.39 %, which are the declared `wrong_figures` for "ignoring the reissued TK9-5521
     certificate's fault window". So p-stale-outcomes (−3) was correctly charged.
- Event 1, the recovered segment 2, was caught: Opus re-listed the drop at step 103 and downloaded seg2. So
  `test_carrier_drop_read_again_before_closing` (3) passed, and so did r-late-segment (3).

## §2.5 Isolation and leakage (per run)
- **Separate verification.** `verifier_environment_mode` is `separate`.
- **Grader paths touched by the agent: none.** Over all tool-call arguments in `agent/trajectory.json`, these each occur 0
  times: `/tests`, `test_outputs`, `test_weights`, `judge.toml`, `solution/`, `TRUTH.md`, `gt_env`, `oracle.json`,
  `reward`.
- **Leakage in tool results: none.**
  - 74.65, 35.83, 15.33, 21.30, "TRUTH" and "oracle" appear in no observation.
  - 99.54 appears in 6 observations. All are Opus's own figure for CVM-260421 (71.67 / 72 h = 99.54 %): terminal output
    of its own engine at steps 69/80/109, the echo of its own QAD-415 at step 127, its own CSV at step 134, and its own
    Slack post at step 137.
  - "R-2026-45 closed" appears only in the server's echo of its own Slack post at step 137.
- **Trivial-solution credit: N/A.** The run made 111 MCP calls and 33 accepted writes: 18 card updates, 11 deviations
  created (plus the 2 rejected attempts above), 3 deviation updates and 1 Slack post. The calibration nop scores 0.0 / 0.0 / 0.0 on the final bytes (`/tmp/qc/oracle_nop_20261114_203752`, trial
  zpRTYE8).

## §3 Reasoning
- 35 of 138 agent steps carry reasoning (18,176 chars), in the field `thought`. reasoning_effort is `high`.
  Verdict: ✅ present.
- Per-step metrics are present on 0 of 138 steps. That is INFO: the bridge records totals in `final_metrics`.

## §4 Overlap
- 30 tests vs 26 criteria: **0 DOUBLE-COUNTED**, 0 PARTIAL, 30 INDEPENDENT, redundancy 0%. RUBRIC-ONLY: 26 of 26.
- The highest pairs are well under the 0.3 PARTIAL line:
  - `test_dock_wait_lots_count_the_wait` against #16, S1 0.28;
  - `test_pellumab_lot_judged_with_its_own_activation_energy` against #14, S1 0.27.
  - In each pair the test grades a card value in the end state and the criterion grades the reason stated in the reply.
- The only non-zero S2 is `test_remaining_pellumab_lots` against #14 (0.50 literals, S1 0.05, composite below 0.3).
  The test reads card values for the other Pellumab lots; the criterion grades PLM-260381's explanation.
- Lost-weight ratios:
  - pytest positives lost 38/58 = 65.5%, guards charged 0.0;
  - rubric positives lost 0.7037/1.0000 = 70.4%, penalties charged 0.0556 (p-stale-outcomes).
- Recommendation: `keep both`.

## §5 False pytests
- I scanned 30 tests: 0/30 carry a flag, and there are 0 BLOCKER-class flags. There are no NO_VERDICT, CONST_VERDICT,
  SELF_COMPARE, OR_TRUE, SWALLOWED_EXCEPT, WILDCARD_IN, NO_AGENT_EVIDENCE or ANSWER_LITERAL hits. 5.2 found no
  assert/return line carrying a rubric figure.
- Pass bits match the trajectory: 18 positives passed, 8 positives failed (all event 2), and the 4 guards were not charged.
  ctrf: `passed 18, failed 12`, statuses only passed/failed.

## Answers to the six questions
1. **Which model:** `anthropic/claude-opus-5` (opus-5), in every file and on every step. openhands-sdk 1.59.0, ATIF-v1.5,
   session_id `harbor-session`.
2. **Is the score arithmetic honest:** yes. reward 0.2928 = 0.5·0.3448 + 0.5·0.2407. pytest is 20/58 from the ledger, and
   rubric is (16 − 3)/54 = Σ weight·value over 26 criteria. The value agrees across all four files and the aggregates.
3. **Is the failure genuine:** yes. Bucket B, stale-read. The environment was healthy and delivered both live events.
   Opus caught the recovered segment but never re-read the reissued certificate before closing.
4. **Is the reasoning present:** yes. 35 steps carry `thought` (18,176 chars).
5. **Do the rubric and pytests double-count:** no. 0 double-counted, 0 partial.
6. **Are any pytests false or hard-coded:** no. 0/30 flagged.

## Verdict
- **SIGNED.** There is no BLOCKER in §1, §1.5, §1.6 or §2.5, and no MAJOR or MINOR in §3, §4 or §5. §2 classifies the run as
  Bucket B (`stale-read`).
