# Yuji checks: 14b9ec91-06a0-5769-9989-d46f60240737 (U11)

## VERDICT: PASS (15/15 items PASS, 0 FAIL)

These checks follow `yuji_checks_image_analysis.md` item by item, applied to the delivered bundle
`TASKS/16Nov_Tasks/14b9ec91-06a0-5769-9989-d46f60240737`. The run is `trajectories/opus-5/run_1` (job
`…-opus-5-20261116-094920-regraded`, trial zQ2c5Ef). The final task_checksum is `b1d7cf49…e479`.

## General checks (1-8)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric across tasks | PASS | All 15 bundles in 16Nov_Tasks have the same top level (`environment instruction.md solution task.toml tests`, 11 entries in tests/). This one also has `trajectories/` (its delivered run) and QC/. Structure QC S1-S5: 0 BLOCKER/MAJOR/MINOR (01_Structure.md). |
| 2 | Rubric `judge.toml`: weights, instruction-following rubrics, structure | PASS | Authoring `tests/judge.toml`: 23 criteria, weights {+5, +3, +1, −5, −3} (only ±1/3/5), +52 / −11, largest item 5. The built `tests/reward/rubric/judge.toml` keeps `source_weight` {−5, −3, 1, 3, 5}; its `weight` is normalised by the harness (for example 0.0962 = 5/52). Every criterion traces to an instruction reply bullet (02_Ruthless C5). Categories: factual_accuracy 12, reasoning_quality 10, completeness 1. All target final_answer. |
| 3 | Testcases semantic, no hard-coding unless the prompt states it, weights ±1/3/5, no always-failing test | PASS | `test_weights.json` values are {−5, −3, −1, 1, 3, 5}. Expected values come from `oracle.json["reported"]`. Ruthless §1c: no rubric figure is hard-coded in test_outputs.py. The only pinned literals are those the instruction pins (the CONSTRAINED line and the subject). No test always fails: the judged oracle passes 18/18 positives (52/52) and the nop passes 0. |
| 4 | `ctrf.json`: pytest only passed or failed | PASS | run_1 `verifier/ctrf.json`: statuses `{'failed': 16, 'passed': 7}`; summary `pending 0, skipped 0, other 0`. |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Judged harbor runs on the final bytes (`/tmp/qc/oracle_nop_20261116_155522`, copied to QC/Oracle run and QC/Nop run): oracle pytest 1.0 / rubric 1.0 / reward 1.0; nop 0.0 / 0.0 / 0.0. Judge gpt-5.6-sol via codex. Checksum `b1d7cf49…` on both. |
| 6 | Graded correctly over pytest and rubric; combined score correct | PASS | Playbook §1.5. Pytest 7/52 = 0.1346 (recompute ok, 0 charged). Rubric Σ weight·value = 0.0577, from 11 positives × 1/52 − (5+3)/52 (recompute ok). 0.5·0.1346 + 0.5·0.0577 = 0.0961, the same in all four files (spread 0.0). |
| 7 | No answer leaks in the bundle | PASS | `environment/Dockerfile` copies only `state_capture.py`. The event values (AMD-1116-02, the four-circuit CONSTRAINED list) appear only in the light-server patches (`software/LightOpenWeather/openweather.py`, `software/LightGmail/gmail.py`). Those run in the separate light-servers service, which the agent container cannot read. Nothing in task_data/, world_data/ or instruction.md. No `/Users/` paths. `solution/` and `tests/` are never mounted for the agent (verifier mode `separate`; no grader path appears in the agent's tool calls, §2.5). |
| 8 | Task is doable; run on Harbor before delivery | PASS | The harbor oracle scores 1.0 with the judge. The Opus 5 run is a full harbor agent run (openhands-sdk 1.59.0, 88 tool calls, no exception), regraded on the final grader bytes. |

## File-specific checks (1-7)

| # | File | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory: schema version, not truncated, final message, tokens, step ids | PASS | `schema_version` ATIF-v1.5; `session_id` harbor-session. 91 steps with contiguous step_id 1…91; the last step is an `agent` step with text. `final_message.md` (9881 chars) = last agent text. `final_metrics`: 10,954,347 prompt / 38,687 completion / 10,771,869 cached tokens, $7.49. No timeout or max-iteration exception. |
| 2 | `reward.json`: only the final combined reward | PASS | `trajectories/opus-5/run_1/verifier/reward.json` = `{"reward": 0.0961}`. The channels stay in report.json and reward-details.json. |
| 3 | `config.json`: reasoning effort high | PASS | `agent.kwargs = {'reasoning_effort': 'high'}`, model `anthropic/claude-opus-5`. |
| 4 | `report.json`: judge model 5.6 Sol, tokens, cost | PASS | `judge = {'ran': True, 'transport': 'codex', 'model': 'gpt-5.6-sol', …}`. Usage: 46,632 input / 2,309 output / 48,941 total tokens, `cost_usd` 0.1714 (litellm_estimate). Rewardkit 0.2.3, codex-cli 0.154.0. |
| 5 | `result.json` / reward-details / report.json: paths masked | PASS | 0 occurrences of `/Users/` in result.json, report.json, config.json, reward-details.json, trajectory.json, grade_report.json and judge.json. |
| 6 | `task.toml`: author aligned with the task | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]` (only one); `authoring_date = "2026-11-16"`. |
| 7 | `task.toml`: only L4 | PASS | `capability_level = "L4"` (only one level). `failure_mechanism` and `target_failure = "stale-read"` are set. |
