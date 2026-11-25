# Yuji checks — f487e5dd-4b6a-5589-bf99-346f3dc18122 (applied item by item to the delivery folder)

**Verdict: PASS. 15 of 15 items pass, and none is open.**

## Main checklist
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Schema / task structure symmetric | PASS | The delivered layout matches the other 30_tasks bundles: environment/, instruction.md, solution/, task.toml, tests/ (with reward/), trajectories/opus-5/run_1, QC/. The structure script on the authoring source passes every check (01_Structure.md). |
| 2 | Rubric judge.toml, weights, instruction-following rubrics | PASS | 24 criteria, all final_answer. Source weights are {5, 3, 1, −1, −3}. Criteria 13–20 grade the reply bullets the instruction asks for: edition, the draft set aside, AR-6.0 limit and source, coefficient units, T_min per returned design, limits, requests set aside. |
| 3 | Testcases semantic, no hard-code, weights ±1/3/5, no always-failing test | PASS | test_weights values are {−5, −3, −1, 1, 3, 5}. check_bundle reports "hard-coded in test_outputs.py: none", and every expected value comes from oracle.json. Playbook §5 flagged 0 of 26. The oracle passes 50/50, so no test always fails. |
| 4 | ctrf.json only pass/fail | PASS | run_1/verifier/ctrf.json statuses: Counter({failed: 16, passed: 10}), with no other value. |
| 5 | Oracle (1 or > 0.95) and nop (0) run | PASS | Harbor oracle 1.0 / 1.0 / 1.0; nop 0.0 / 0.0 / 0.0 (QC/Oracle run, QC/Nop run). |
| 6 | Graded correctly; combined score correct | PASS | pytest (10 − 0)/50 = 0.2. Rubric Σ weight·value = 0.1667. 0.5·0.2 + 0.5·0.1667 = 0.1834. That matches all four files (playbook §1.5a–e). |
| 7 | No answer leaks anywhere in the bundle | PASS | `Released: 5`, the held list and the countersign issues appear nowhere in task_data or world_data. "Countersign" occurs only in the DS-6 clause text. The answer lives only in solution/ and tests/, which the agent cannot reach (no grader path in any tool call; verifier mode `separate`). |
| 8 | Task doable; run on Harbor | PASS | The harbor oracle scored 1.0. The real Opus 5 run on harbor finished cleanly with 0 tool errors, and at step 34 it listed the deciding records. |

## File-specific checks
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Trajectory: schema version, not truncated, final message, tokens, step ids | PASS | `ATIF-v1.5`; 113 steps with contiguous ids; the last step is an agent step. final_message.md (9741 chars) equals the last agent text. final_metrics: prompt 7 094 237, completion 41 631, cached 6 866 194, cost $5.90. The run took 21:58:49 to 22:09:07, well inside the 7200 s limit. |
| 2 | Reward.json only final combined reward | PASS | `{"reward": 0.1834}` |
| 3 | Config.json reasoning effort high | PASS | `agent.kwargs = {'reasoning_effort': 'high'}`; model `anthropic/claude-opus-5` |
| 4 | Report.json judge model (5.6 sol), tokens, cost | PASS | report.json judge: ran true, model `gpt-5.6-sol`, transport `codex`. Usage: 40 992 tokens (38 719 in, 2 273 out), cost $0.2003. The agent's tokens and cost are in result.json agent_result. |
| 5 | Result.json / reward-details / report.json path masking | PASS | A grep for `/Users/` and `/home/` in result.json, report.json, reward-details.json and config.json is empty. Only container paths such as /logs/verifier appear. |
| 6 | Task.toml author aligned | PASS | authors = Priyanshi Joshi <priyanshi.joshi@ethara.ai>; task.name atlas/f487e5dd-4b6a-5589-bf99-346f3dc18122 |
| 7 | Task.toml only L4 | PASS | metadata.capability_level = `L4`, and it is the only level field. |
