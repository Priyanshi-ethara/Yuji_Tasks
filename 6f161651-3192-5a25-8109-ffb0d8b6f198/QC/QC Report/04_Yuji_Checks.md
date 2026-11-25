# Yuji checks: 6f161651-3192-5a25-8109-ffb0d8b6f198 (U10 submission-toc-versions, LIVE)

I applied `yuji_checks_image_analysis.md` item by item to the final delivery folder `TASKS/16Nov_Tasks/6f161651-…`.
That folder holds the built bundle and run_1 from job `…-095646-regraded`, with task_checksum `df81ab49…8b50`.

## VERDICT: PASS (15/15 items)

### General checks (items 1–8)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric | PASS | The bundle has the standard built layout, the same as the batch's other 16Nov deliveries: instruction.md, task.toml, environment/ (Dockerfile, docker-compose.yaml, light-servers/ with task_data 36 files and world_data 15 seeds), solution/ (solve.py, solve.sh, gt_env.json, TRUTH.md), tests/ (test_outputs.py, test_weights.json, oracle.json, old_env.json, harness verifier files, reward/), trajectories/opus-5/ and QC/. Structure QC passes (01_Structure.md), and so does playbook §1.5 ("judge.toml vs graded: missing=[] extra=[] drift=[]"). |
| 2 | Rubric judge.toml, weights, instruction-following rubrics | PASS | The authoring judge.toml has 22 criteria. Their weights are {1: 10, 5: 5, 3: 4, −3: 2, −1: 1}, all in (1, 3, 5, −1, −3, −5). All are final_answer and every one traces to a reply bullet the instruction asks for (02_Ruthless C5): revisions and their records, departures from the draft, N/A reasons, gap reasons, the page-total method, glossary exclusions, document-control follow-ups. The compiled `tests/reward/rubric/judge.toml` carries the same 22, normalised by the harness (positives sum 1.0). |
| 3 | Testcases semantic, no hard-code, weights ±1/3/5, no always-failing test | PASS | test_weights.json has {1: 11, 5: 9, 3: 1, −5: 2, −3: 2, −1: 1}. Every expected value comes from `oracle.json["reported"]` via `ref()`, and 02_Ruthless §1c finds no rubric figure hard-coded. Playbook §5 flags 0 of 26. No test always fails: the harbor oracle passes 21/21 positives (earned 59/59). |
| 4 | ctrf.json only pass/fail | PASS | run_1 `verifier/ctrf.json` statuses: {failed: 15, passed: 11}. The summary reports pending 0, skipped 0, other 0. |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Harbor via `qc_oracle_nop.sh` (JUDGE=codex) on the final bytes, `/tmp/qc/oracle_nop_20261116_160552`: oracle 1.0/1.0/1.0, nop 0.0/0.0/0.0. Raw jobs are in QC/Oracle run and QC/Nop run. |
| 6 | Graded correctly over pytest and rubric; combined score correct | PASS | Playbook §1.5: pytest (11 − 0)/59 = 0.1864, recompute ok. The rubric Σ weight·value = 0.2128, recompute ok. 0.5·0.1864 + 0.5·0.2128 = 0.1996, the same in all four files. I checked the judge verdicts against final_message.md. The 9 positives judged no are all event-dependent and the reply is stale on each; for example it cites "DOC-1047 Rev E" and never names CHG0041187. The 10 judged yes match the reply's static explanations. All three penalties were judged no. Criteria 20 and 22 now carry the "quoted only as the draft's figure" carve-out (02_Ruthless Fixed 8); the 828 penalty no longer misfires on the reply's comparison table. |
| 7 | No answer leaks anywhere in the bundle | PASS | 02_Ruthless C8: CHG0041187, v_KS3_1047_6, 784 and "23 complete" appear only inside the patched server event blocks (fired after rows 1 and 29) and in solution/ and tests/. tests/ and solution/ are not mounted for the agent (Dockerfile copies only state_capture.py). Playbook §2.5: those strings appear 0 times in the observations Opus received, and the agent made 0 tool calls on grader paths. |
| 8 | Task doable; run on Harbor before delivery | PASS | The harbor oracle reaches 1.0 through the same MCP tools: Drive list_versions, Monday get_board_items and ServiceNow list_change_requests, re-read after the 30th row. The Opus run is a real harbor run (job `…-095646`, trial `h3hb9wf`, 87 tool calls, 0 server errors). |

### File-specific checks

| # | File → check | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory → schema version, not truncated, final message, tokens, step ids | PASS | `schema_version: ATIF-v1.5`, session_id `harbor-session`, agent openhands-sdk 1.59.0. 90 steps, ids 1–90 contiguous, last step source `agent` with text. final_message.md matches the last agent text (9742 chars, playbook 1.5f). `final_metrics`: 4,890,921 prompt / 35,410 completion / 4,703,466 cached tokens, $4.41. |
| 2 | Reward.json → only the combined reward | PASS | `verifier/reward.json` = `{"reward": 0.1996}`. The channels stay in report.json and reward-details.json. |
| 3 | Config.json → reasoning effort high | PASS | `{'name': 'openhands-sdk', 'model_name': 'anthropic/claude-opus-5', 'kwargs': {'reasoning_effort': 'high'}}` |
| 4 | Report.json → judge model (5.6 Sol), tokens, cost | PASS | `judge: {ran: True, model: gpt-5.6-sol, transport: codex}`. Usage: 39,074 total tokens, cost_usd 0.128. Agent tokens and cost are in result.json `agent_result`. |
| 5 | result.json / reward-details / report.json → path masking | PASS | The `path` fields are masked as `***/6f161651-…` and `***/<job>/<trial>`. `grep -rl /Users/mac` over run_1 finds nothing. |
| 6 | Task.toml → author aligned with task | PASS | `authors = [{name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai"}]`, the sole author. authoring_date 2026-11-16. |
| 7 | Task.toml → only L4 | PASS | `capability_level = "L4"`, the only capability level in the file. |
