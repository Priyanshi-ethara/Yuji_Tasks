# Yuji checks: 40ea4665-a13d-5cb8-875b-59bf9f2b1d95 (U14, LIVE)

## VERDICT: PASS (15/15 items PASS, 0 FAIL)

These checks follow `yuji_checks_image_analysis.md` item by item. They apply to the delivered bundle
`TASKS/16Nov_Tasks/40ea4665-a13d-5cb8-875b-59bf9f2b1d95` and its run `trajectories/opus-5/run_1` (job
`40ea4665-…-opus-5-20261116-112639`, trial C9Cx4WD). The final task_checksum is `4b0823a2…0d5e`.

## General checks (1-8)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric across tasks | PASS | All 15 bundles in 16Nov_Tasks have the same top level (`environment instruction.md solution task.toml tests`) and 11 entries in tests/. This one also has `trajectories/` (its delivered run) and `QC/`. Structure QC S1-S5: 0 BLOCKER, 0 MAJOR, 0 MINOR (01_Structure.md). |
| 2 | Rubric `judge.toml`: weights, instruction-following rubrics, structure | PASS | The authoring `tests/judge.toml` has 25 criteria with weights {+5, +3, +1, −5, −3} (only ±1/3/5): +46 / −17, largest item 5. The built `tests/reward/rubric/judge.toml` keeps `source_weight` {−5, −3, 1, 3, 5}; its `weight` is normalised by the harness (for example 0.1087 = 5/46). Every criterion maps to a hand-over bullet of the instruction (02_Ruthless C5). Categories: reasoning_quality 12, factual_accuracy 10, completeness 2, instruction_following 1. All 25 target final_answer. |
| 3 | Testcases semantic, no hard-coding unless the prompt states it, weights ±1/3/5, no always-failing test | PASS | `test_weights.json` values are {−5, −3, −1, 1, 3, 5}. Every expected figure, site, marker and tolerance is read from `oracle.json["reported"]` (02_Ruthless C1). The playbook §5 scan flags 0 of 22 tests, and no assert or return carries a rubric figure. The only pinned literals are the subject grammar and line vocabulary that the instruction pins. No test always fails: the judged oracle passes 16/16 positives (42/42), and the nop passes none. |
| 4 | `ctrf.json`: pytest only passed or failed | PASS | run_1 `verifier/ctrf.json` statuses are `{'failed': 13, 'passed': 9}`; summary `pending 0, skipped 0, other 0`. The 13 failures are 7 positives missed and 6 guards not charged (guard_polarity `pass_charges`). |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Judged harbor runs on the final bytes (`/tmp/qc/oracle_nop_20261116_165300`, copied flat into QC/Oracle run and QC/Nop run). Oracle: pytest 1.0, rubric 1.0, reward 1.0. Nop: 0.0, 0.0, 0.0. Judge gpt-5.6-sol via codex. Checksum `4b0823a2…` on both. |
| 6 | Graded correctly over pytest and rubric; combined score correct | PASS | Playbook §1.5. Pytest: 9/42 = 0.2143 (recompute ok, 0 charged). Rubric: Σ weight·value = 0.1087 = (11 × 1 − 3 − 3)/46 (recompute ok, no drift against judge.toml). Combined: 0.5·0.2143 + 0.5·0.1087 = 0.1615, the same in all four files (spread 0.0). |
| 7 | No answer leaks in the bundle | PASS | `environment/Dockerfile` copies only `state_capture.py`. The event text ("Amendment 16 Nov 2026 …", the new CT ratios) exists only in the light-server patches (`software/LightNotion/notion.py`, `software/LightMicrosoftTeams/microsoft_teams.py`). These run in the separate light-servers service behind a flag, and the agent cannot read them. Nothing of the event is in task_data/, world_data/ or instruction.md (02_Ruthless C8). The answer figures sit only in grader or metadata files the agent never sees: `solution/` (TRUTH.md, solve.py, gt_env.json), `tests/oracle.json`, and the `wrong_figures`/scenario text of task.toml. In the run, no observation carries an amended figure (playbook §2.5), and the verifier mode is `separate`. The one `/Users/user/…` string is the stock LightObsidian corpus vault path; that server is not wired. |
| 8 | Task is doable; run on Harbor before delivery | PASS | The harbor oracle scores 1.0 with the judge and passes all six event tests. The Opus 5 run is a full harbor agent run (openhands-sdk 1.59.0, 100 tool calls, no exception). |

## File-specific checks (1-7)

| # | File | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory: schema version, not truncated, final message, tokens, step ids | PASS | `schema_version` ATIF-v1.5; `session_id` harbor-session. 103 steps with contiguous step_id 1…103; the last step is an `agent` step with text (the `finish` message). `final_message.md` (11,938 chars) = last agent text. `final_metrics`: 9,019,982 prompt / 65,494 completion / 8,691,882 cached tokens, $8.03. No timeout or max-iteration exception. |
| 2 | `reward.json`: only the final combined reward | PASS | `trajectories/opus-5/run_1/verifier/reward.json` = `{"reward": 0.1615}`. The channels stay in report.json and reward-details.json. |
| 3 | `config.json`: reasoning effort high | PASS | `agent.kwargs = {'reasoning_effort': 'high'}`, model `anthropic/claude-opus-5`. |
| 4 | `report.json`: judge model 5.6 Sol, tokens, cost | PASS | `judge = {'ran': True, 'transport': 'codex', 'model': 'gpt-5.6-sol', 'reason': None, 'criteria': 25, …}`. Usage: 38,197 input / 2,531 output / 40,728 total tokens, `cost_usd` 0.1412 (litellm_estimate). Rewardkit 0.2.3, codex-cli 0.154.0. |
| 5 | `result.json` / reward-details / report.json: paths masked | PASS | 0 occurrences of `/Users/` in result.json, report.json, config.json, reward-details.json, trajectory.json, grade_report.json and judge.json. config.json shows `"path": "***/40ea4665-…"` and `"trials_dir": "***"`. |
| 6 | `task.toml`: author aligned with the task | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]` (only one author); `authoring_date = "2026-11-16"`. |
| 7 | `task.toml`: only L4 | PASS | `capability_level = "L4"` (the only level). `target_failure = "wrong-value-written (stale read of an amended meter record)"`. |
