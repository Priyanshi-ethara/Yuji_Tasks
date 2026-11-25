# Yuji checks: 205f473f-c7e1-5bff-88b5-09e0e89b5356 (U04, LIVE)

## VERDICT: PASS (15/15 items PASS, 0 FAIL)

These checks follow `yuji_checks_image_analysis.md` item by item.

- **Bundle checked:** the delivered bundle `TASKS/16Nov_Tasks/205f473f-c7e1-5bff-88b5-09e0e89b5356`.
- **Run:** `trajectories/opus-5/run_1` (job `…-opus-5-20261116-111050`, trial TDTmhge).
- **Checksum:** task_checksum `e0e779d4…f77a`, which equals the `dirhash` of the delivered task folder.

## General checks (1-8)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric across tasks | PASS | All 15 bundles in 16Nov_Tasks have the same top level (`environment instruction.md solution task.toml tests`), with 12 entries in tests/ (including `.dockerignore`). This one also carries `trajectories/` (its delivered run) and QC/. Structure QC S1-S5 finds 0 BLOCKER, MAJOR or MINOR (01_Structure.md). |
| 2 | Rubric `judge.toml`: weights, instruction-following rubrics, structure | PASS | The authoring `tests/judge.toml` has 22 criteria. Weights are {+5 ×5, +3 ×2, +1 ×12, −5 ×1, −3 ×2}, so only ±1/3/5, totalling +43 / −11, with a largest item of 5. The built `tests/reward/rubric/judge.toml` keeps `source_weight` with the same set; its `weight` is normalised by the harness (5/43 = 0.1163). Every criterion traces to a reply bullet of the instruction (02_Ruthless C5). Every criterion targets final_answer. Types: reasoning_quality, completeness and factual_accuracy (the 3 penalties). |
| 3 | Testcases semantic, no hard-coding unless the prompt states it, weights ±1/3/5, no always-failing test | PASS | `test_weights.json` values are {5 ×7, 3 ×1, 1 ×8, −5 ×2, −3 ×2, −1 ×1}. Every expected owner, class, team, channel and marker is read from `oracle.json["reported"]`. Ruthless §1c finds no rubric figure in the tests. The group ids in test bodies are seeded register keys. No test always fails: the judged oracle passes 16/16 positives (46/46) and the nop passes 0. |
| 4 | `ctrf.json`: pytest only passed or failed | PASS | run_1 `verifier/ctrf.json` has statuses `{'failed': 12, 'passed': 9}`, with summary `pending 0, skipped 0, other 0`. The 12 failures are the 7 missed positives plus the 5 guards that did not fire (pass_charges). |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Both are judged harbor runs on the final bytes (`/tmp/qc/oracle_nop_20261116_163724`, copied flat to QC/Oracle run and QC/Nop run). Oracle: pytest 1.0, rubric 1.0, reward 1.0. Nop: 0.0, 0.0, 0.0. Judge gpt-5.6-sol via codex. Both carry checksum `e0e779d4…`. |
| 6 | Graded correctly over pytest and rubric; combined score correct | PASS | Playbook §1.5. Pytest is 11/46 = 0.2391 (recompute ok, 0 charged). Rubric is Σ weight·value = 12/43 − 3/43 = 0.2093 (recompute ok). 0.5 × 0.2391 + 0.5 × 0.2093 = 0.2242, the same in all four files (spread 0.0). |
| 7 | No answer leaks in the bundle | PASS | `environment/Dockerfile` copies only `state_capture.py` (L33). The event content (PR #3490 and the merge note) exists only in the patch blocks of `software/LightGithub/github.py` and `software/LightSlack/slack.py`. Those run in the separate light-servers service and apply only after the flag fires. `grep 3490` over task_data/, world_data/ and instruction.md finds nothing, and the Driver Comms seed records are neutral. There are no `/Users/` paths. `solution/` and `tests/` are never mounted for the agent: verifier mode is `separate`, and no grader path appears in the agent's tool calls (playbook §2.5). |
| 8 | Task is doable; run on Harbor before delivery | PASS | The harbor oracle scores 1.0 with the judge. The Opus 5 run is a full harbor agent run (openhands-sdk 1.59.0, 78 tool calls, no exception). |

## File-specific checks (1-7)

| # | File | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory: schema version, not truncated, final message, tokens, step ids | PASS | `schema_version` is ATIF-v1.5 and `session_id` is harbor-session. The 81 steps have contiguous step_id 1…81, and the last step is an `agent` step with text. `final_message.md` equals the last agent text (`same=True`, 9284 chars). `final_metrics` shows 3,538,099 prompt, 36,452 completion and 3,340,686 cached tokens, $3.82. There is no timeout or max-iteration exception. |
| 2 | `reward.json`: only the final combined reward | PASS | `trajectories/opus-5/run_1/verifier/reward.json` is `{"reward": 0.2242}`. The channels stay in report.json and reward-details.json. |
| 3 | `config.json`: reasoning effort high | PASS | `agent.kwargs = {'reasoning_effort': 'high'}`, model `anthropic/claude-opus-5`. |
| 4 | `report.json`: judge model 5.6 Sol, tokens, cost | PASS | `judge = {'ran': True, 'transport': 'codex', 'model': 'gpt-5.6-sol', 'reason': None, …}`. Usage is 36,828 input, 2,266 output and 39,094 total tokens; `cost_usd` is 0.1327 (litellm_estimate). Rewardkit 0.2.3, codex-cli 0.154.0. |
| 5 | `result.json` / reward-details / report.json: paths masked | PASS | `/Users/` occurs 0 times in result.json, report.json, config.json, reward-details.json, trajectory.json, grade_report.json and judge.json. config.json shows the task path as `***/205f473f-…`. |
| 6 | `task.toml`: author aligned with the task | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]`, the only author. `authoring_date = "2026-11-16"`. |
| 7 | `task.toml`: only L4 | PASS | `capability_level = "L4"` is the only capability level. `failure_mechanism` and `target_failure` are set, and `target_failure` names the stale-read live change. |
