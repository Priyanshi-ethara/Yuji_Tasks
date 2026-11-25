# Yuji checks: 8fd816e9-1ce3-5f54-967f-bae034dde678 (U13, hardened to LIVE)

## VERDICT: PASS (15/15 items PASS, 0 FAIL)

These checks follow `yuji_checks_image_analysis.md` item by item.

- **Bundle checked:** the delivered bundle `TASKS/16Nov_Tasks/8fd816e9-1ce3-5f54-967f-bae034dde678`.
- **Run:** `trajectories/opus-5/run_1` (job `…-opus-5-20261116-113443`, trial sXjas2H).
- **Checksum:** task_checksum `84b922da…df3c`, which equals the `dirhash(sha256)` of the delivered task folder.

## General checks (1-8)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric across tasks | PASS | All 15 bundles in 16Nov_Tasks have the same top level (`environment instruction.md solution task.toml tests`), with 12 entries in tests/. This one also carries `trajectories/` (its delivered run) and QC/. Structure QC S1-S5 finds 0 BLOCKER, MAJOR or MINOR (01_Structure.md). |
| 2 | Rubric `judge.toml`: weights, instruction-following rubrics, structure | PASS | The authoring `tests/judge.toml` has 25 criteria. Weights are only ±1/3/5: {+5 ×5, +3 ×2, +1 ×15, −5 ×1, −3 ×2}. That totals +46 / −11, and the largest item is 5. The built `tests/reward/rubric/judge.toml` keeps `source_weight` with the same set; its `weight` is normalised by the harness (5/46 = 0.1087). Every criterion traces to a reply bullet of the instruction (02_Ruthless C5). All 25 target final_answer. Types: reasoning_quality 16, factual_accuracy 8, completeness 1. |
| 3 | Testcases semantic, no hard-coding unless the prompt states it, weights ±1/3/5, no always-failing test | PASS | `test_weights.json` values are {5 ×7, 3 ×1, 1 ×11, −5 ×2, −3 ×2, −1 ×1}. Every expected figure, label, title count and follow-up set is read from `oracle.json["reported"]`. Ruthless §1 finds no rubric figure in test_outputs.py ("hard-coded in test_outputs.py: none"). No test always fails: the judged oracle passes 19/19 positives (49/49) and the nop passes 0. |
| 4 | `ctrf.json`: pytest only passed or failed | PASS | run_1 `verifier/ctrf.json` has statuses `{'failed': 13, 'passed': 11}`, with summary `pending 0, skipped 0, other 0`. The 13 failures are the 8 missed positives plus the 5 guards that did not fire (pass_charges). |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Both are judged harbor runs on the final bytes (`/tmp/qc/oracle_nop_20261116_170046`, copied flat to QC/Oracle run and QC/Nop run). Oracle: pytest 1.0, rubric 1.0, reward 1.0. Nop: 0.0, 0.0, 0.0. Judge gpt-5.6-sol via codex. Both carry checksum `84b922da…`. |
| 6 | Graded correctly over pytest and rubric; combined score correct | PASS | Playbook §1.5. Pytest is 11/49 = 0.2245 (recompute ok, 0 charged). Rubric is Σ weight·value = 12/46 − 8/46 = 0.087 (recompute ok). 0.5 × 0.2245 + 0.5 × 0.087 = 0.1557, the same in all four files (spread 0.0). |
| 7 | No answer leaks in the bundle | PASS | `environment/Dockerfile` copies only `state_capture.py` (L33). The event content (Corrigendum C1, Tier 3 99.60 %, comment 510006) exists only in the patch block of `software/LightConfluence/confluence.py`. That block runs in the separate light-servers service and applies only after the `bwp_rs2_c1` flag fires. `grep` for `99.60`, `Corrigend` or `510006` over task_data/, world_data/ and instruction.md finds nothing. There are no `/Users/` paths. `solution/` and `tests/` are never mounted for the agent: verifier mode is `separate`, and no grader path appears in the agent's tool calls (playbook §2.5). |
| 8 | Task is doable; run on Harbor before delivery | PASS | The harbor oracle scores 1.0 with the judge. The Opus 5 run is a full harbor agent run (openhands-sdk 1.59.0, 61 tool calls, no exception). |

## File-specific checks (1-7)

| # | File | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory: schema version, not truncated, final message, tokens, step ids | PASS | `schema_version` is ATIF-v1.5 and `session_id` is harbor-session. The 64 steps have contiguous step_id 1…64, and the last step is an `agent` step with text. `final_message.md` equals the last agent text (`same=True`, 8772 chars). `final_metrics` shows 3,935,968 prompt, 32,924 completion and 3,751,821 cached tokens, $3.85. There is no timeout or max-iteration exception: the agent ran 11:35:40Z → 11:42:23Z (6m43s) against `agent_timeout_sec 7200`. |
| 2 | `reward.json`: only the final combined reward | PASS | `trajectories/opus-5/run_1/verifier/reward.json` is `{"reward": 0.1557}`. The channels stay in report.json and reward-details.json. |
| 3 | `config.json`: reasoning effort high | PASS | `agent.kwargs = {'reasoning_effort': 'high'}`, model `anthropic/claude-opus-5`. |
| 4 | `report.json`: judge model 5.6 Sol, tokens, cost | PASS | `judge = {'ran': True, 'transport': 'codex', 'model': 'gpt-5.6-sol', 'reason': None, …}`. Usage is 37,232 input, 2,324 output and 39,556 total tokens; `cost_usd` is 0.0917 (litellm_estimate). Rewardkit 0.2.3, codex-cli 0.154.0. |
| 5 | `result.json` / reward-details / report.json: paths masked | PASS | `/Users/` occurs 0 times in result.json, report.json, config.json, reward-details.json, trajectory.json, grade_report.json and judge.json. config.json shows the task path as `***/8fd816e9-…`. |
| 6 | `task.toml`: author aligned with the task | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]`, the only author. `authoring_date = "2026-11-16"`. |
| 7 | `task.toml`: only L4 | PASS | `capability_level = "L4"` is the only capability level. `failure_mechanism` and `target_failure` are set, and `target_failure` names the stale read of the corrected standard. |
