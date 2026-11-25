# Yuji checks: 1b302c0b-6031-50de-aa3b-684f5231e338 (W10 ticket-field-writeback)

## VERDICT: PASS (15/15 items PASS, 0 FAIL)

These checks follow `yuji_checks_image_analysis.md` item by item, on the delivered bundle
`TASKS/18Nov_Tasks/1b302c0b-6031-50de-aa3b-684f5231e338` after the gatefix and fix round 2 of 2026-11-18 (grader-only). The run is
`trajectories/opus-5/run_1`, the h2b Opus 5 agent run (trial 7jfiPS7, original job `…-opus-5-20261118-054121`), regraded on
the final tests and rubric as job `1b302c0b-6031-50de-aa3b-684f5231e338-opus-5-20261118-054121-regraded`. task_checksum
`dc3f8fd6…483b` is the same on the run, the oracle and the nop (ONDIR `oracle_nop_20261119_112242`). The run_1 slot holds
only the h2b job (an earlier h2 attempt failed at agent setup on an empty wheelhouse and is kept out, in
`_kit/traj/qcsave/18/1b302c0b-…/failed_setup`).

## General checks (1-8)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric across tasks | PASS | Top level `environment instruction.md solution task.toml tests` (+ `trajectories/`, `QC/`), as in the other 18Nov bundles; tests/ holds the harness's claims_lib.py and no task_lib.py. 01_Structure S1-S5 PASS. |
| 2 | Rubric `judge.toml`: weights, instruction-following rubrics, structure | PASS | Authoring `tests/judge.toml`: 20 criteria, weights {+5, +3, +1} (only ±1/3/5, all three used), +34, no penalties, largest 5. Includes an instruction-following item (c-staff-from-note). The built `tests/reward/rubric/judge.toml` is normalised by the harness (0.1471 = 5/34, 0.0882 = 3/34, 0.0294 = 1/34) and keeps `source_weight` 5/3/1 (playbook 1.5d: positive=34 penalty=0). 01_Structure S4b: no structural defect. |
| 3 | Testcases semantic, no hard-coding unless the prompt states it, weights ±1/3/5, no always-failing test | PASS | `test_weights.json` {−5, −3, −1, 1, 3, 5}; expected values from `oracle.json["reported"]`; ruthless §1c: no rubric figure hard-coded; playbook §5: 0/20 flagged; the judged oracle passes all 15 positives (49/49). |
| 4 | `ctrf.json`: pytest only passed or failed | PASS | run_1 `verifier/ctrf.json` `{'tests': 20, 'passed': 8, 'failed': 12, 'pending': 0, 'skipped': 0, 'other': 0}`. Under `pass_charges` the 5 guards are "failed" (not tripped) and 7 positives missed. |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Judged harbor runs on the final bytes (`/tmp/qc/oracle_nop_20261119_112242`, copied flat into QC/Oracle run and QC/Nop run; durable copy in `_kit/traj/qcsave/18/<uuid>/`): oracle 1.0 / 1.0 / 1.0, nop 0.0 / 0.0 / 0.0, judge gpt-5.6-sol via codex, `ran: True`; summary.tsv holds only this task's rows. |
| 6 | Graded correctly over pytest and rubric; combined score correct | PASS | Playbook §1.5: pytest 14/49 = 0.2857 (recompute ok, 0 charged); rubric 19/34 positives, no penalties = 0.5588 (recompute ok, n=20 yes=9 no=11); 0.5·0.2857 + 0.5·0.5588 = 0.4223 in all four files (spread 0.0). |
| 7 | No answer leaks in the bundle | PASS | `environment/Dockerfile` copies only `state_capture.py`. The writeback rules live in the LightZendesk task-layer patch (rules, not answers; page 520102 publishes the same rules). task_data (incl. docx text), world_data, software and instruction.md: 0 hits for the held mixes. No `/Users/` path except the stock LightObsidian corpus on an unwired server. Playbook §2.5: no grader path touched. |
| 8 | Task is doable; run on Harbor before delivery | PASS | Harbor oracle 1.0 with the judge. The Opus 5 run is a full harbor agent run (openhands-sdk 1.59.0, 104 tool calls, 91 MCP, no exception), regraded through the harness on the final tests. |

## File-specific checks (1-7)

| # | File | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory: schema version, not truncated, final message, tokens, step ids | PASS | `schema_version` ATIF-v1.5; `session_id` harbor-session; 107 steps, the last an `agent` step with text; final_message.md = last agent text (1.5f `same=True`); final_metrics 6,514,353 prompt / 65,870 completion / 6,267,440 cached tokens, $6.32. |
| 2 | `reward.json`: only the final combined reward | PASS | `run_1/verifier/reward.json` = `{"reward": 0.4223}`; channels in report.json and reward-details.json. |
| 3 | `config.json`: reasoning effort high | PASS | `agent.kwargs = {'reasoning_effort': 'high'}`, model `anthropic/claude-opus-5`. |
| 4 | `report.json`: judge model 5.6 Sol, tokens, cost | PASS | judge `{'ran': True, 'transport': 'codex', 'model': 'gpt-5.6-sol'}`; usage 34,593 input / 1,647 output / 36,240 total tokens, cost_usd 0.1133 (litellm_estimate). |
| 5 | `result.json` / reward-details / report.json: paths masked | PASS | 0 occurrences of `/Users/` in result.json, report.json, config.json, reward-details.json and trajectory.json. |
| 6 | `task.toml`: author aligned with the task | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]` (only one); `authoring_date = "2026-11-18"`. |
| 7 | `task.toml`: only L4 | PASS | `capability_level = "L4"`; `target_failure = "wrong-value-written"`, `failure_mechanism` backend writeback, matching ROSTER5 W10. |
