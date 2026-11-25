# QC Report — af4ffc91-76d8-5138-83e5-ba2e89fbf7b0   layout: full (reward.json trimmed)   runs: 1   model(s): opus-5

I ran `qc 2/traj/10_bundle_playbook.md` on an rsync copy of the delivered bundle
`TASKS/18Nov_Tasks/af4ffc91-76d8-5138-83e5-ba2e89fbf7b0` (QC/ excluded), with `BUNDLE` exported to the copy. Its eight
script blocks (loader, §1, §1.5, §1.6, §2, §3, §4, §5) ran as written, in order. Raw output, with the scratch path
masked to `<copy>`: `03_playbook_script.txt`. The only run is `trajectories/opus-5/run_1`: job
`af4ffc91-…-opus-5-20261117-101558-regraded`, trial U5kgfBg, task_checksum `a5dbe4c4…d41d`. That is the h1 run
(job `…-101558`) regraded on the final bytes after round 3 of 2026-11-18 (FIX3_18). A confirming review was followed
by one grader-only fix: the rubric was rewritten (20 criteria, positives 26, no penalties) and only the oracle reply
text changed. The tests are unchanged since GATEFIX18, and so are the agent's actions. jobs.json lists only that job.
Pytest is unchanged at 0.2821. The rubric moved from 0.6786 (FIX2_18 regrade) to 0.6154, and the reward from 0.4803 to
0.4487.

## §1 Model
- run_1: config / result / report / trajectory agree. ✅ `distinct models after normalising ['opus-5'] ok`,
  `models seen mid-run 1 ok`. config `anthropic/claude-opus-5`, result `claude-opus-5`, report
  `opus-5 / anthropic/claude-opus-5`, every agent step `anthropic/claude-opus-5`.
- `schema_version ATIF-v1.5 ok`. Agent: `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk',
  'tool_definitions': None, 'version': '1.59.0'}`. `reasoning_effort high`. session_id `harbor-session`.

## §1.5 Score sanity (per run)
- 1.5a: reward 0.4487 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run;
  `spread=0.0 ok`. reward.json is trimmed to `{"reward": 0.4487}`, so the channels are read from
  report.json.channels.
- 1.5b: `source=grade_report.json rows=20 earned=11.0 penalty=0.0 total_positive=39 guard_polarity=pass_charges`.
  `pytest recompute 0.2821 vs reported 0.2821 ok`. Weighted 20 = ledger 20, no weight drift, `guards tripped [] / 6
  missed`, `tests that raised none`.
- 1.5c: judge `ran=True model=gpt-5.6-sol`. `rubric recompute 0.6154 vs reported 0.6154 / channel 0.6154 ok`. `n=20 yes=14 no=6`
  (14 of 20 positives yes; there are no penalties), raw values only yes/no, 0 errors. judge.toml vs graded: nothing missing,
  extra or drifted. report.rubric count 20 ok.
- 1.5d: polarity mismatches none. Source weights `positive=26 penalty=0`, and the normalised positives sum to 1.0.
- 1.5e: `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.4487 vs reward 0.4487 ok`.
- 1.5f: `exception_info=None errored=False state_capture_failed=None agent_steps=63 last_step_source=agent`.
  final_message.md 14147 chars, `same=True`. final_metrics: 7,816,037 prompt / 43,865 completion / 7,545,246 cached
  tokens, $6.56.
- No BLOCKER. `SIGNOFF_BLOCKED` is not tagged.

## §1.6 Aggregates
- `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`. Threshold 0.7 everywhere. No per_run mismatch and no
  pass-rule violation. Averages 0.4487 / 0.2821 / 0.6154 recompute ok.
- pass@1.json: `passed=0 (recomputed 0) pass_rate=0.0`, reward_per_run no drift, `failure_mode_histogram
  {'partial': 1} … ok`. jobs.json `[('af4ffc91-…-opus-5-20261117-101558-regraded', 1)]`. Failure modes `['partial']`.
- Flags: runs_without_rubric [], runs_with_state_capture_failed [], errored_run_indices [], judge_models
  ['gpt-5.6-sol'].

## §2 Failure classification (per run)
- run_1: `passed False reward=0.4487 threshold=0.7 failure_mode=partial`.
- **Bucket A ruled out.** `2.1a state capture failed=None … end_env.json=shipped`; `2.1b None / False`; `2.1c judge
  ran=True`; `2.1d tool calls total=62 mcp=54 local=8 ok`; `2.1e tool results that look like server errors 0`.
  Every call the task needs returned data: Box search/folder items/12 downloads, Airtable bases/tables/records,
  Confluence list_content (desk method body), and Gmail list plus 17 messages.
- **Bucket B, sub-label `wrong-value-written`.** This is the card's TARGET, and the evidence supports it.
  1. The writes happened but carry the decoy values. `2.2e positive tests missed 6`:
     `test_coal_loader_stood_down_in_gale_despatch_call`, `…_demurrage_call`, `test_cranes_laid_up_in_gale_discharge_call`,
     `test_ore_loader_stood_down_in_gale_outcome_turns`, `test_quarter_summary_money_lines`, `test_quarter_summary_counts`.
     The local replay prints the stored values. PC-3101 Despatch 3984.38 Agreed (right: 5,000.00, Disputed). PC-3103
     Demurrage 9270.83 (right: 7,187.50). PC-3109 EUR 3020.83 Agreed (right: 3,687.50, Disputed). PC-3112
     Demurrage 1000.00 Agreed (right: Despatch 1,166.67, Disputed). Summary "Demurrage USD: 73338.54",
     "Disputed calls: 5".
  2. The deciding records were read and returned correctly. Box `download_file` at steps 20, 23, 29 and 32 returned
     PC-3101/3103/3109/3112. Each response contains "on terminal order", "gusting 9" and "Extra moorings". The desk
     method's "The test is one of cause" and "any other cause" came back at step 12. All SOF reads came before the
     first claim write (step 54).
  3. The model saw the trap and wrote the wrong value anyway. The step 21 thought reads: "the loader stopped because
     of the wind rather than for an unrelated reason. That makes it look like genuine weather time". At step 34 it
     changes course: "I'm leaning toward no deduction. That matches the owners' agreed figures … which looks like the
     intended treatment". The final message (2.2f/2.2g) calls each stand-down "a terminal stoppage on our side of
     clause 22, not a clause 17 weather stoppage". The round-3 rubric grades nothing pytest grades, so the wind miss
     shows only in pytest. The judge said no to six items: #1 r-port-weather-notes (5), #9 r-kpi-dashboard, #13
     r-nor-any-time, #15 r-exceptions-each-call, #18 r-owners-not-source and #19 r-totals-merrow-figures (1 each).
  - Not `guard-tripped` (`2.2d guards tripped none`). Not `gave-up-early`: every deliverable was written (12 claim
    records in 2 `create_records`, 5 LTD issues, the summary page, a read-back, and the full reply). Not
    `tool-surface-tunnel-vision`: the run did not open Notion (corroboration only), but the deciding record is the
    statement of facts, which it read, and it does not claim any app was unavailable. Not `stale-read`: this is a
    static card with no re-delivery.
  - `2.2c wired servers never called`: LightDocuSign, LightDropbox, LightGoogleCalendar, LightGoogleMaps, LightHR,
    LightMeet, LightNotion, LightOutlook, LightSlack, LightXero. These are red-line, decoy or context apps, and none
    is needed for a positive.

## §2.5 Isolation and leakage (per run)
- `verifier_environment_mode`: `separate` (run_1 result.json).
- Grader paths touched by the agent: none. A grep of every tool-call argument for `/tests`, `test_outputs`,
  `test_weights`, `judge.toml`, `solution/`, `TRUTH`, `gt_env`, `oracle.json` gives 0 hits (runcheck: "/tests
  mentioned: False").
- Leakage in tool results: none. The right figures (5,000.00, 7,187.50, 3,687.50, 1,166.67, 70,255.21, 8,916.67,
  9,812.50) occur in no seeded app record and no data file (grep of task_data, world_data, software,
  instruction.md: 0).
- Trivial-solution credit: none. The judged nop is 0.0 / 0.0 / 0.0 (QC/Nop run).

## §3 Reasoning
- `agent steps / with reasoning 63 / 28 (28077 chars) field(s) used: ['thought']`; effort high; verdict
  `present`. Per-step metrics 0 of 63 (INFO: the bridge records totals in final_metrics).

## §4 Overlap
- 20 tests vs 20 criteria: `DOUBLE-COUNTED=0 PARTIAL=1 INDEPENDENT=19 redundancy=0%`. `RUBRIC-ONLY (no test reaches
  0.5): 20 of 20`.
- The PARTIAL row is `test_rain_closures_inside_other_stoppages_disputed_calls` vs #19 r-totals-merrow-figures (S1 0.10,
  S2 0.50): a literal-word match only ("Merrow", "disputed", "calls"). The test grades the claim records of two rain-group
  calls; the item grades that the quarter totals are made of Merrow's own figures. No shared entity, value or decision;
  keep.
- Other rows reached S2 0.50 on literals alone (`test_quarter_summary_counts` vs #3 r-clause17-test,
  `test_rain_closures_inside_other_stoppages_agreed_calls` vs #18 r-owners-not-source, the five guards vs #15
  r-exceptions-each-call), with S1 0.00-0.06 and generic shared words. All INDEPENDENT.
- Lost weight on run_1: pytest positive lost 28/39 = 71.8%, guards charged 0. Rubric positive lost 0.3846/1.0 =
  38.5% (10/26: r-port-weather-notes 5, r-kpi-dashboard, r-nor-any-time, r-exceptions-each-call, r-owners-not-source,
  r-totals-merrow-figures 1 each), penalties charged 0.
- The rubric has no penalties (round 2 deleted the three decoy-figure penalties). Round 3 deleted r-rain-worksheet-departure,
  r-other-stoppage-counts, r-overlap-once and r-wind-gusts-continuing as twins or group-only rules. Nothing is
  double-charged.

## §5 False pytests
- 20 scanned. `0/20 tests carry a flag; BLOCKER flags: 0`. "5.2 assert/return lines carrying a rubric figure": none
  printed.

## Verdict
- **SIGNED.** §1, §1.5, §1.6 and §2.5 have no BLOCKER. §3 is present. §4 and §5 are clean. §2 classification: Bucket
  B, `wrong-value-written`, which is the card's TARGET. The failure is genuine: the deciding records were read and
  returned correctly, and the model saw the wind cause and then deferred to the owners' figures. Reward 0.4487 < 0.60,
  and both channels are fractional (pytest 0.2821, rubric 0.6154).
