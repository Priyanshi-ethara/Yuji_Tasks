# Yuji checks: 13444412-6c43-5e79-92de-aed8d163049c (U05)

## VERDICT: PASS (15/15 items PASS, 0 FAIL)

These checks follow `yuji_checks_image_analysis.md` item by item, applied to the delivered bundle
`TASKS/16Nov_Tasks/13444412-6c43-5e79-92de-aed8d163049c`. The run is `trajectories/opus-5/run_1` (job
`…-opus-5-20261116-114232-regraded`, trial itxKZDo). The final task_checksum is `26e36975…bbb`.

## General checks (1-8)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric across tasks | PASS | All 15 bundles in 16Nov_Tasks have the same top level (`environment instruction.md solution task.toml tests`, 11 entries in tests/). This one also has `trajectories/` (its delivered run) and QC/. Structure QC S1-S5: 0 BLOCKER/MAJOR/MINOR (01_Structure.md). |
| 2 | Rubric `judge.toml`: weights, instruction-following rubrics, structure | PASS | Authoring `tests/judge.toml`: 25 criteria, weights {+5, +3, +1, −3, −1} (only ±1/3/5), +42 / −11, largest item 5. The built `tests/reward/rubric/judge.toml` keeps `source_weight` {−3, −1, 1, 3, 5}; its `weight` is normalised by the harness (for example 0.1190 = 5/42). Every criterion traces to a bullet of the instruction's handover request (02_Ruthless C5). Categories: reasoning_quality 16, factual_accuracy 8, instruction_following 1. All target final_answer. |
| 3 | Testcases semantic, no hard-coding unless the prompt states it, weights ±1/3/5, no always-failing test | PASS | `test_weights.json` values are {−5, −3, −1, 1, 3, 5}. Expected values come from `oracle.json["reported"]`. Ruthless §1c: no rubric figure is hard-coded in test_outputs.py. Playbook §5: 0 of 23 tests flagged. No test always fails: the judged oracle passes 19/19 positives (47/47) and the nop passes 0. |
| 4 | `ctrf.json`: pytest only passed or failed | PASS | run_1 `verifier/ctrf.json`: statuses `{'failed': 13, 'passed': 10}`; summary `pending 0, skipped 0, other 0`. Under `pass_charges` the 4 guards are "failed" (not tripped), and 9 positives are missed. |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Judged harbor runs on the final bytes (`/tmp/qc/oracle_nop_20261116_173855`, copied to QC/Oracle run and QC/Nop run): oracle pytest 1.0 / rubric 1.0 / reward 1.0; nop 0.0 / 0.0 / 0.0. Judge gpt-5.6-sol via codex. Checksum `26e36975…` on both. The earlier 0.9881 oracle was a grader wording defect, fixed (02_Ruthless, QC_FINAL16). |
| 6 | Graded correctly over pytest and rubric; combined score correct | PASS | Playbook §1.5. Pytest 10/47 = 0.2128 (recompute ok, 0 charged). Rubric Σ weight·value = 0.0952, from 11/42 positives − 7/42 penalties (recompute ok). 0.5·0.2128 + 0.5·0.0952 = 0.154, the same in all four files (spread 0.0). |
| 7 | No answer leaks in the bundle | PASS | `environment/Dockerfile` copies only `state_capture.py`. The amendment text (PRC-2026-11, £252.00 / £354.00) appears only in the Notion task-layer patch in the light-servers service, which the agent container cannot read. Nothing in task_data/, world_data/ or instruction.md. old_env.json has no `PRC-2026-11`. Outside the light-servers patch, the marker appears only in `tests/oracle.json` and `solution/` (verifier and solution side). No `/Users/` paths in task_data, world_data or instruction.md (the only hit in environment/ is the stock LightObsidian corpus placeholder `/Users/user/Documents/…`, which is vendor data on a server this task does not wire). `solution/` and `tests/` are never mounted for the agent (verifier mode `separate`; no grader path appears in the agent's tool calls, playbook §2.5). |
| 8 | Task is doable; run on Harbor before delivery | PASS | The harbor oracle scores 1.0 with the judge. The Opus 5 run is a full harbor agent run (openhands-sdk 1.59.0, 148 tool calls, no exception), regraded on the final grader bytes. |

## File-specific checks (1-7)

| # | File | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory: schema version, not truncated, final message, tokens, step ids | PASS | `schema_version` ATIF-v1.5; `session_id` harbor-session. 151 steps with contiguous step_id 1…151; the last step is an `agent` step with text. `final_message.md` (13778 chars) = last agent text. `final_metrics`: 7,842,610 prompt / 68,887 completion / 7,567,301 cached tokens, $7.23. No timeout or max-iteration exception. |
| 2 | `reward.json`: only the final combined reward | PASS | `trajectories/opus-5/run_1/verifier/reward.json` = `{"reward": 0.154}`. The channels stay in report.json and reward-details.json. |
| 3 | `config.json`: reasoning effort high | PASS | `agent.kwargs = {'reasoning_effort': 'high'}`, model `anthropic/claude-opus-5`. |
| 4 | `report.json`: judge model 5.6 Sol, tokens, cost | PASS | `judge = {'ran': True, 'transport': 'codex', 'model': 'gpt-5.6-sol', …}`. Usage: 37,993 input / 2,268 output / 40,261 total tokens, `cost_usd` 0.1351 (litellm_estimate). Rewardkit 0.2.3, codex-cli 0.154.0. |
| 5 | `result.json` / reward-details / report.json: paths masked | PASS | 0 occurrences of `/Users/` in result.json, report.json, config.json, reward-details.json, trajectory.json, grade_report.json and judge.json. |
| 6 | `task.toml`: author aligned with the task | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]` (only one); `authoring_date = "2026-11-16"`. |
| 7 | `task.toml`: only L4 | PASS | `capability_level = "L4"` (only one level). `failure_mechanism` and `target_failure = "wrong-value-written (stale read of a price card amended mid-run)"` are set. |
