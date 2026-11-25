# QC Report: 6139c0bc-0714-5c5f-98cb-7c1b5a995d52   layout: full   runs: 1   model(s): opus-5

Playbook: `/Users/mac/Desktop/Trinity_Final/qc 2/traj/10_bundle_playbook.md`. I extracted all eight bash blocks verbatim (the loader plus §1, §1.5, §1.6, §2, §3, §4 and §5) and ran them unchanged. `BUNDLE` was exported to a scratch copy of the final delivery folder `30_tasks/6139c0bc-…` (QC/ excluded), taken after `run_1/verifier/reward.json` was trimmed to `{"reward": 0.3226}`. Run date: 2026-11-12. Every script exited 0. Raw output is in `03_playbook_script.txt`.

run_1 is the regraded trial: job `6139c0bc-0714-5c5f-98cb-7c1b5a995d52-opus-5-20261112-081015-regraded`, trial `2dR7WYs`. The source trial `…-opus-5-20261112-081015/2dR7WYs` was regraded on the final task bytes after grader-only fixes. The shipped `jobs.json` carries task_checksum `d873c0ec…89c5`. That is the same checksum as the oracle and nop trials in `/tmp/qc/oracle_nop_20261114_203752`, so the run is graded by the tests that ship.

The agent-visible inputs did not change between the run and the final bundle. I ran `diff -rq` between the pre-run build copy (`/tmp/qc/oracle_nop_20261112_133602/_copies/6139c0bc-…`, built 08:03:00Z; the run started 08:10:19Z) and the delivered bundle. It lists only `tests/test_outputs.py`, `solution/TRUTH.md` and `task.toml`, and the task.toml change is in `verification_explanation` only. `instruction.md` and all of `environment/` are byte-identical, and so is the compiled `judge.toml`. The regrade reused the original trial's trajectory, final message and end_env: all three are byte-identical to the source trial (`cmp`).

## §1 Model
- opus-5/run_1: ✅ identity confirmed. The folder is `opus-5`; pass_summary.model is `opus-5`; config.agent.model_name is `anthropic/claude-opus-5`; result model_info is `claude-opus-5`; report is `opus-5 / anthropic/claude-opus-5`; every agent step has `['anthropic/claude-opus-5']`. Output: `distinct models after normalising ['opus-5'] ok`, `models seen mid-run 1 ok`.
- `schema_version ATIF-v1.5 ok`. Agent: `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`. `reasoning_effort` is `high`. `tool_definitions` is None, which is INFO per the table: the bridge does not record it. There is no "unknown" version.

## §1.5 Score sanity (per run)
- 1.5a: reward 0.3226 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run, `spread=0.0 ok`. reward.json is trimmed to `{reward}`, so the channels come from `report.json.channels`, as the loader allows.
- 1.5b: from grade_report.json, rows=35, earned=29.0, penalty=0.0, total_positive=84, guard_polarity=pass_charges, gate=None. `pytest recompute 0.3452 vs reported 0.3452 ok`. Weighted tests vs ledger rows are 35/35, with no weight drift. Guards tripped: [] and 11 missed. No test raised.
- 1.5c: the judge ran (`ran=True model=gpt-5.6-sol`). `rubric recompute 0.3 vs reported 0.3 / channel 0.3 ok`. n=31: 18 yes and 13 no (10 positives no, 3 penalties no), raw values `['no', 'yes']`, 0 errors. judge.toml vs graded: none missing, none extra, no weight or text drift. report.rubric count is 31 (ok).
- 1.5d: polarity mismatches none. Source weights are positive=60 and penalty=7, and the normalised positives sum to 1.0.
- 1.5e: `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.3226 vs reward 0.3226 ok`.
- 1.5f: exception_info=None, errored=False, 132 agent steps, last step source `agent`. final_message.md is 10,707 chars; the last agent text is 10,707 chars; `same=True`. final_metrics: 9,888,230 prompt / 66,444 completion / 9,595,512 cached tokens, $8.29.
- No BLOCKER and no MAJOR, so no `SIGNOFF_BLOCKED`.

## §1.6 Aggregates
- Counts: `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`. Threshold 0.7 in pass_summary, test_weights and pass@1 (ok). per_run.combined equals the run reward. Pass-rule violations: none (passed=false, 0.3226 < 0.7).
- Averages recomputed: combined 0.3226, pytest 0.3452, rubric 0.3, all ok. Flags: runs_without_rubric [], runs_with_state_capture_failed [], errored_run_indices [], judge_models ['gpt-5.6-sol'].
- pass@1.json: passed 0 (recomputed 0), pass_rate 0.0, reward_per_run has no drift, histogram `{'partial': 1}` sums to 1 (ok). jobs.json is `[('…-opus-5-20261112-081015-regraded', 1)]`. No `AGGREGATE_UNRELIABLE`.

## §2 Failure classification (per run)
- opus-5/run_1 did not pass: reward 0.3226 against threshold 0.7, failure_mode `partial`. **Bucket B (model/agent), sub-label `stale-read`.**
- The environment was healthy:
  - end_env.json shipped and state capture did not fail; there was no exception, and the judge ran.
  - 131 tool calls: 116 MCP and 15 local. `2.1e tool results that look like server errors 0`.
  - The wired-but-never-called servers (DocuSign, GoogleCalendar, MicrosoftTeams, Notion, ServiceNow, Trello, Xero) are read-only or decoy servers the task does not need. The final message does not say they were unavailable.
- Evidence:
  1. The four LightEnergy `list_readings` calls (steps 36–39, on meters mtr-t02-06/10/08/17) all come before the first board write at step 45. The 22nd distinct site item is written at step 108, and that write fires event C (the MDV-2026-11 register validation). It is present in `run_1/verifier/end_env.json`, in the LightEnergy registers and in the mailbox (message AAMkT02msg0098).
  2. After the board was complete, Opus re-read Box (steps 111, 113–114) and Airtable (112, 115), and so caught events A and B. It never called LightEnergy or LightOutlook again. Its step-111 thought lists "the Box invoice folder …, the Airtable registry mirror, the Confluence errata and protocol pages, and the district energy statements", and the energy platform is not on that list.
  3. The 11 missed positives (2.2e) are all event C: the 8 `*_on_the_validated_registers` site tests, both struck totals and `test_energy_platform_read_again_before_the_strike` ("validated registers never read before the strike"). Rubric criteria 1–8 are no for the same reason: the reply reports the stale E-month kWh, for example Salem February 304,880 instead of 322,880.
- Criteria 21 and 25 (1 point each) are no on judge literalness, not on substance (see 02_Ruthless, Minor).

## §2.5 Isolation and leakage (per run)
- `verifier_environment_mode` is `separate`.
- Grader paths touched by the agent: none. Over all tool-call arguments, I counted occurrences of `/tests`, `test_outputs`, `test_weights`, `judge.toml`, `solution/`, `TRUTH.md`, `gt_env`, `oracle.json` and `reward`. Every count is 0.
- Leakage in tool results: none. The struck totals 45854.1 / 41571.4 (both plain and comma forms), the event-moved cells 2977.5 / 1105.7, "TRUTH" and "oracle" do not appear in any observation.
- Trivial-solution credit: N/A. The run made 116 MCP calls and 76 writes. The calibration nop scores 0.0 / 0.0 / 0.0 on the final bytes (`/tmp/qc/oracle_nop_20261114_203752`).

## §3 Reasoning
- 26 of 132 agent steps carry reasoning (19,298 chars) in the field `thought`; reasoning_effort is `high`. Verdict: ✅ present.
- Per-step metrics are present on 0 of 132 steps. That is INFO: the bridge records totals in `final_metrics`.

## §4 Overlap
- 35 tests vs 31 criteria: **0 DOUBLE-COUNTED**, 10 PARTIAL, 25 INDEPENDENT, redundancy 0%. RUBRIC-ONLY: 31 of 31.
- I read the 10 PARTIAL rows. Each scores 0.50 on S2 only, because the test shares one or two identifiers with the criterion (a site id or certificate id such as TPC-11 or NRR-2025-1420-WND), and S1 is 0.12–0.19. The test grades a board cell in tCO2e, or the instrument set. The criterion grades the clause given as the reason, or an activity quantity, in the reply. These are different signals, and none is double-counted.
- Lost-weight ratios: pytest positives lost 55/84 = 65.5%, guards charged 0.0. Rubric positives lost 0.7000/1.0000 = 70.0%, penalties charged 0.0000.
- Recommendation: `keep both`.

## §5 False pytests
- I scanned 35 tests: 0/35 carry a flag, and the BLOCKER-class flags count is 0. There are no NO_VERDICT, CONST_VERDICT, SELF_COMPARE, OR_TRUE, SWALLOWED_EXCEPT, WILDCARD_IN, NO_AGENT_EVIDENCE or ANSWER_LITERAL hits. 5.2 found no assert/return line carrying a rubric figure.
- Pass bits match the trajectory: 19 positives passed, 11 positives failed, and the 5 guards were not charged.

## Answers to the six questions
1. **Which model:** `anthropic/claude-opus-5` (opus-5) in every file and on every step. openhands-sdk 1.59.0, ATIF-v1.5.
2. **Is the score arithmetic honest:** yes. reward 0.3226 = 0.5·0.3452 + 0.5·0.3000. pytest = 29/84 from the ledger, and rubric = Σ weight·value over 31 criteria. The value agrees across all four files and the aggregates.
3. **Is the failure genuine:** yes. Bucket B, stale-read. The environment was healthy, and the only lost work is the late register validation, which Opus never re-read.
4. **Is the reasoning present:** yes. 26 steps carry `thought` (19,298 chars).
5. **Do the rubric and pytests double-count:** no. 0 double-counted, and the 10 partial rows were read and dismissed.
6. **Are any pytests false or hard-coded:** no. 0/35 flagged.

## Verdict
- **SIGNED.** There is no BLOCKER in §1, §1.5, §1.6 or §2.5, and no MAJOR or MINOR in §3, §4 or §5. §2 classifies the run as Bucket B (`stale-read`).
