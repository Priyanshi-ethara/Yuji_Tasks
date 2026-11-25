# QC Report — 6f161651-3192-5a25-8109-ffb0d8b6f198   layout: full   runs: 1   model(s): opus-5

I ran `qc 2/traj/10_bundle_playbook.md` as written: the §0 loader, then the §1, §1.5, §1.6, §2, §3, §4 and §5 scripts.
They ran on a copy of the final delivery folder `TASKS/16Nov_Tasks/6f161651-…`, without QC/ and with the reward.json
trim applied, with `BUNDLE=<copy>`. The raw output is in `03_playbook_script.txt`.

run_1 is the recorded Opus job `6f161651-…-opus-5-20261116-095646`, trial `h3hb9wf`. It was regraded on the final bytes
as `…-095646-regraded`: grader-only judge.toml fixes, see 02_Ruthless Fixed 7 and 8. task_checksum `df81ab49…8b50`
matches out/build, jobs.json and the harbor oracle/nop trials.

## §1 Model
- run_1: ✅ every file agrees. The folder is `opus-5`, and pass_summary also says `opus-5`. config has
  `anthropic/claude-opus-5`, result has `claude-opus-5`, report has `opus-5 / anthropic/claude-opus-5`, and every
  step's model_name is `['anthropic/claude-opus-5']`. Distinct models after normalising: `['opus-5']`. Models seen
  mid-run: 1.
- `ATIF-v1.5` (ok). The agent is `openhands-sdk` in config and result (v1.59.0). The trajectory has
  `{'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`. reasoning_effort is `high`.

## §1.5 Score sanity (per run)
- 1.5a: reward 0.1996 in reward.json, report.final_reward, result.verifier_result and pass_summary. spread=0.0, ok.
- 1.5b: `source=grade_report.json rows=26 earned=11.0 penalty=0.0 total_positive=59 guard_polarity=pass_charges
  gate=None`. Recompute 0.1864 vs reported 0.1864, ok. Weighted 26 = ledger 26, no weight drift, no test raised.
  Guards tripped `[]`, 10 positives missed.
- 1.5c: judge `ran=True model=gpt-5.6-sol`. Recompute 0.2128 vs reported 0.2128, ok. n=22, yes=10, no=12, raw values
  yes/no only, errors 0. judge.toml vs graded: no missing criterion, no extra criterion, no weight or text drift.
  report.rubric count is 22.
- 1.5d: no polarity mismatches. Source weights: positive 47, penalty 7. Normalised positives sum to 1.0.
- 1.5e: `{'pytest': 0.5, 'rubric': 0.5} -> 0.1996 vs reward 0.1996`, ok.
- 1.5f: exception_info None, errored False, 88 agent steps, last step source `agent`. final_message.md is 9742 chars,
  the same as the last agent text (same=True). Tokens: 4,890,921 prompt, 35,410 completion, $4.41.
- No BLOCKER, so no `SIGNOFF_BLOCKED`.

## §1.6 Aggregates
- runs=1, completed=1, errored=0, per_run=1, folders=1, ok. The threshold is 0.7 in pass_summary, test_weights and
  pass@1. No per_run mismatch and no pass-rule violation.
- The three averages match their recomputes: combined 0.1996, pytest 0.1864, rubric 0.2128.
- runs_without_rubric `[]`, runs_with_state_capture_failed `[]`, judge_models `['gpt-5.6-sol']`.
- pass@1.json: passed 0 (recomputed 0), pass_rate 0.0, reward_per_run has no drift, histogram `{'partial': 1}` sums to
  1. jobs.json lists the one regraded job with 1 trial.

## §2 Failure classification (per run)
- run_1: passed False, reward 0.1996 vs threshold 0.7, failure_mode `partial`. **Bucket B, sub-label `stale-read`.**
- There is no 2.1 environment evidence:
  - end_env.json is shipped (capture_ok true, 8 apps);
  - there was no exception and the judge ran;
  - there were 87 tool calls (80 MCP), and 2.1e found 0 server errors.
- Evidence:
  1. Both live events fired. The run's own `verifier/end_env.json` has:
     - LightDrive DOC-1047 `current_version_id v_KS3_1047_6`, "Rev F | released 2026-11-16 under CHG0041187 | 52 pp";
     - DOC-1188 at `v_KS3_1188_3`;
     - Monday `item-ks3-1133g` with status Approved, "env-ks3-1133g completed 2026-11-16T08:52".
  2. `agent/trajectory.json` shows all of the run's store, register and change-control reads before the first ToC
     write (step 27):
     - the Drive login snapshot at step 8 (it shows DOC-1047 at v_KS3_1047_5 and DOC-1133 Rev G "routed for
       approval");
     - Monday get_board_items at step 15 (item-ks3-1133g "In approval");
     - ServiceNow at steps 16–17.
     It then wrote rows 27–56 (event 1 fires on the first row, event 2 on the 29th). It made no further Drive,
     Monday, ServiceNow or DocuSign call before the mail at step 89.
  3. The mail subject was `22 complete, 4 gap, 4 not applicable, 767 pages`. 767 is the declared "misses both live
     changes" figure; the expected subject is 23/3/4, 784. The 10 missed positives are exactly the event-moved tests:
     S13, S14 and S22 (×2), the S22 ticket, the readiness counts and pages, the re-read, and S07. All 11 static tests
     passed. The harbor oracle re-reads Drive list_versions, Monday get_board_items and ServiceNow
     list_change_requests after row 30 and receives the new records, so the deciding records were reachable through
     the tools Opus had.
- 2.2c: DocuSign, Dropbox, Gmail, GoogleCalendar, GoogleDrive, Teams and Slack were wired but never called. Of these,
  only DocuSign carries event 1. The register (Monday) carries it too, and Opus had used Monday. The final message does
  not claim any server was unavailable, so this is not tool-surface-tunnel-vision.
- 2.2d: guards none. 2.2g: the 9 positives judged no are criteria 1–9, all event-dependent. The judge reasoning matches
  the reply, for example "it explicitly uses 'Rev E,' not Rev F". All three penalties were judged no.

## §2.5 Isolation and leakage (per run)
- `verifier_environment_mode`: `separate`.
- Grader paths touched by the agent: none. A grep of every tool-call argument for /tests, test_outputs.py,
  test_weights.json, judge.toml, solution/, TRUTH.md, gt_env.json, oracle.json and /reward finds 0 hits.
- Leakage in tool results: none. CHG0041187, v_KS3_1047_6, "784" and "23 complete" appear 0 times in the observations
  Opus received.
- Trivial-solution credit: n/a. The run wrote 53 records, and the harbor nop scores 0/0/0 (QC/Nop run).

## §3 Reasoning
- 88 agent steps, 20 with reasoning (11,624 chars), in the `thought` field. Effort `high`. Verdict: **present**.
  Per-step metrics are absent (INFO; totals are in final_metrics).

## §4 Overlap
- 26 tests vs 22 criteria. DOUBLE-COUNTED 0, PARTIAL 8, INDEPENDENT 18, redundancy 0%. All 22 criteria are
  rubric-only: no test reaches 0.5.
- I read every PARTIAL. Seven of them pair a static row test with the criterion that grades the reply's reason for that
  row: S23, S20, S14, S17, S16, S15 and S29. For example, `test_linearity_row_takes_the_change_request_release` checks
  the Airtable S20 fields, while criterion 13 checks that the reply explains why Rev C governs. Those are different
  signals.
- `test_readiness_page_total` vs criterion 21 (−3, 771 as final) pairs the mail-subject figure with a declared
  wrong-figure penalty on the reply. It is an intentional distractor twin (task.toml `wrong_figures`).
- No criterion restates a guarded act. Item 8 lost its "does not claim the agent recorded them in the register"
  clause in Fixed 7.
- Lost weight: pytest 48/59 = 81.4% lost, 0 guard charge. Rubric 0.7872/1.0 = 78.7% lost, penalties charged 0.0000.
- Recommendation: **keep both**.

## §5 False pytests
- 26 scanned, 0 flagged, 0 blocker-class flags. 5.2: no assert or return line carries a rubric figure.

## Verdict
- **SIGNED.** §1, §1.5, §1.6 and §2.5 have no BLOCKER. §2 is a genuine Bucket B `stale-read`, which the owner accepts
  (2026-11-16); it is neither guard-tripped nor gave-up-early. §3 is present. §4 has 0 double-counted. §5 has 0
  flags.
