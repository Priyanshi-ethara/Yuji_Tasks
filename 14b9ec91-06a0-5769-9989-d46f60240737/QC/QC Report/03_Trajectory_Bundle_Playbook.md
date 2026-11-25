# QC Report: 14b9ec91-06a0-5769-9989-d46f60240737   layout: full   runs: 1   model(s): opus-5

This run applies `qc 2/traj/10_bundle_playbook.md` to a copy of the delivered bundle
(`TASKS/16Nov_Tasks/14b9ec91-06a0-5769-9989-d46f60240737`, without QC/), with `BUNDLE` exported to that copy. Every
script (§0 loader, §1, §1.5, §1.6, §2, §3, §4, §5) ran as written, from a scratch working directory. The raw output is in
`03_playbook_script.txt`. The only run is `trajectories/opus-5/run_1`: job
`14b9ec91-06a0-5769-9989-d46f60240737-opus-5-20261116-094920-regraded`, trial zQ2c5Ef. This is the 2026-11-16 Opus 5
agent run, re-verified on the final grader bytes (rg1 rubric fix). `verifier/reward.json` is trimmed to `{"reward": 0.0961}`.
The channels are read from report.json, as §0 allows.

## §1 Model
- **opus-5/run_1: ✅ agree.** folder `opus-5`; pass_summary `opus-5`; config `anthropic/claude-opus-5`; result
  `claude-opus-5`; report `opus-5 / anthropic/claude-opus-5`; steps `['anthropic/claude-opus-5']`. The script prints
  `distinct models after normalising ['opus-5'] ok` and `models seen mid-run 1 ok`.
- **Agent:** `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`.
- **Schema and effort:** `schema_version ATIF-v1.5 ok`; `reasoning_effort high`.

## §1.5 Score sanity (per run)
- **1.5a:** the reward is 0.0961 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run
  (`spread=0.0 ok`).
- **1.5b:** ledger from grade_report.json. 23 rows, earned 7.0, penalty 0.0, total_positive 52, `pass_charges`, gate
  None. Recompute `0.1346 vs reported 0.1346 ok`. Weighted 23 = ledger 23, weight drift none, guards tripped `[]`,
  11 missed, no test raised.
- **1.5c:** judge `ran=True model=gpt-5.6-sol`. Rubric recompute `0.0577 vs reported 0.0577 / channel 0.0577 ok`. 23 answers
  (13 yes, 10 no), raw values `['no', 'yes']`, 0 errors. judge.toml vs graded: none missing, none extra, no drift.
  report.rubric count 23 ok.
- **1.5d:** polarity mismatches none. Source weights +52 / −11; the normalised positives sum to 1.0.
- **1.5e:** `{'pytest': 0.5, 'rubric': 0.5} -> 0.0961 vs reward 0.0961 ok`.
- **1.5f:** `exception_info=None errored=False state_capture_failed=None agent_steps=89 last_step_source=agent`.
  final_message.md has 9881 chars and is identical to the last agent text (`same=True`). Tokens: 10,954,347 prompt
  (10,771,869 cached), 38,687 completion, $7.49.
- **Result:** no BLOCKER.

## §1.6 Aggregates
- **Counts:** `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`.
- **Threshold:** 0.7 in pass_summary, test_weights and pass@1.
- **Pass bits and averages:** no violations; the averages (0.0961 / 0.1346 / 0.0577) match.
- **pass@1.json:** passed 0, pass_rate 0.0, reward_per_run without drift, histogram `{'partial': 1}` sums to 1.
- **jobs.json:** lists only the regraded job, with 1 trial. Flags: no run without a rubric, no run with failed state
  capture; judge_models `['gpt-5.6-sol']`.
- **Result:** no BLOCKER.

## §2 Failure classification (per run)
- **opus-5/run_1:** passed False, reward 0.0961 < 0.7, failure_mode `partial`.
- **2.1 environment:** none. The trial ran with end_env.json shipped, no exception, and the judge ran. It made 88 tool
  calls (74 MCP), and 0 tool results look like server errors.
- **Bucket B, sub-label `stale-read`.** Evidence (`trajectories/opus-5/run_1/agent/trajectory.json`, `report.json`):
  1. **Every read came before the first write.** The run made all 7 `LightOpenWeather_get_forecast` calls (steps 24-30)
     and every Gmail read (steps 34-38) before its first register write (step 65). It then made 22
     `LightAirtable_update_record` calls (steps 65-86) and one `list_records` of the register (step 87), and posted and
     mailed (steps 88-89). It never read OpenWeather or Gmail again after a write. Both MetDesk changes land only after
     row writes (the Skelwith Edge reissue after row 1, the warm-front amendment after row 21).
  2. **The missed tests are the re-read tests.** `test_revised_circuit_a-d_*`, `test_revised_forecast_read_before_the_notice`,
     `test_revised_circuits_carry_the_revised_ambient_band`, `test_reissued_circuit_a/b_*`, both CONSTRAINED tests and
     the whole-register test (11 missed, report.json `pytest.missed`). All 7 static-rule tests pass (cables, mirror, Fell
     conductors, two-station inputs, wind bands, write order, subject).
  3. **The reply is built on the early values.** final_message.md says "Coldfell Moor | 4.2 °C … unchanged" and gives
     Skelwith Edge as "8.0 kn" with a reissue "still awaited". The judge answered no on #1-#9 and charged
     p-draft-constrained-list (−5) and p-coldfell-pre-revision (−3).
- **The record was reachable.** The judged oracle on the same bytes scored 1.0, reading the reissued forecasts after the
  trigger. No tool error occurred on any call the task needs.
- **Never-called servers:** LightGoogleCalendar, LightGoogleMaps and LightTrello are context-only, and the final message
  never says they were unavailable, so this is not tunnel vision.
- **2.2d:** no guard tripped.

## §2.5 Isolation and leakage (per run)
- **Verifier mode:** `verifier_environment_mode`: `"separate"`.
- **Grader paths touched by the agent:** none. The pattern
  `/tests|test_outputs.py|test_weights.json|judge.toml|reward|solution/|TRUTH.md|gt_env.json|oracle.json` has 0 hits
  across the arguments of all 88 tool calls.
- **Leakage in tool results:** none. The changed figures (6.8 C, 5.9 C, 4.0 kn) arrive only from the live OpenWeather
  service after the triggers, and the run never received them. No seeded record or file holds the oracle reply.
- **Trivial-solution credit:** none. The run wrote 22 rows, one post and one mail. The judged nop on the same bytes scored 0/0/0.

## §3 Reasoning
- 89 agent steps, 29 of them with reasoning (11,830 chars), field `thought`; reasoning_effort `high`. Verdict: ✅ present.
- Per-step metrics are on 0 of 89 steps (INFO: the totals are in `final_metrics`).

## §4 Overlap
- **Matcher counts:** 23 tests vs 23 criteria. `DOUBLE-COUNTED=0 PARTIAL=0 INDEPENDENT=23 redundancy=0%`, and all 23
  criteria are rubric-only. The highest composite is 0.26 (`test_cable_sections_limit_where_lower` vs #4, S1 0.19 / S2 0.33). Next is 0.24
  (`test_cable_section_above_the_line_rating_does_not_limit` vs #12). Both are well under the 0.3 PARTIAL line.
- **Lost weight:** pytest positive lost 45/52 = 86.5%, guards charged 0.0. Rubric positive lost 0.7885 = 78.8%,
  penalties charged 0.1538.
- **Manual strict read (owner rule):** no rubric item restates a register value, write, tool call or guarded act.
  - #19 and #20 now grade the BRTN-1 / OXFD-2 forecast loads and percentages (560 A, about 92 %; 600 A, about 94 %).
    Pytest never sees a load or a percentage.
  - The two refusal items that restated the protection and public-notice guards were removed in the rg1 fix (02_Ruthless item 11).
- **Recommendation:** `keep both`.

## §5 False pytests
- **Scan:** 23 tests, 6 flagged `CONST_VERDICT` (`test_revised_circuit_a/b/c/d_*`, `test_reissued_circuit_a/b_*`). The
  script counts them as blocker-class, which §5 reports as MAJOR. 5.2 finds no assert or return line that carries a
  rubric figure.
- **Disposition: false positives, cleared.**
  - Each flagged test is a one-line call to `_revised_circuit(k)` (test_outputs.py L339-346) or `_reissued_circuit(k)`
    (L349-356), followed by `return True`.
  - The helpers do the asserting. They call `_ready()` (red-line, deliverable and anti-blanket asserts, L333-336), then
    assert the register fields and a post-trigger read (`_saw_change`, L290).
  - The AST scan looks only at the test body, so it misses asserts inside helpers.
  - All 6 failed in this run with real reasons, for example "CFHG-1 not issued on the revised forecast". All 6 passed in
    the judged oracle and failed in the nop. None passed trivially (`PASSED_TRIVIALLY` is absent).
- **Remaining flags:** no NO_VERDICT, SELF_COMPARE, OR_TRUE, SWALLOWED_EXCEPT, WILDCARD_IN, NO_AGENT_EVIDENCE or
  ANSWER_LITERAL flag.

## Verdict
- **SIGNED.**
  - No BLOCKER in §1, §1.5, §1.6 or §2.5.
  - §2 is Bucket B `stale-read`, a genuine model failure with no guard tripped (not guard-tripped, not gave-up-early).
  - §3 reasoning is present. §4 has 0 double-counted items. §5's 6 flags are scanner false positives, disproved by the
    run's own failures.
