# QC Report — a6901ded-0579-5c2d-8ae3-a0649c5c5ff2   layout: full packager output, reward.json trimmed to {"reward"}   runs: 1   model(s): opus-5

How the playbook was run:
- Playbook: `/Users/mac/Desktop/Trinity_Final/qc 2/traj/10_bundle_playbook.md`.
- Every script was run as written: the loader, then §1, §1.5, §1.6, §2, §3, §4 and §5.
- `BUNDLE` was a copy of the delivery folder with QC/ excluded.
- Raw output: `03_playbook_script.txt`.

The run:
- Job: `a6901ded-0579-5c2d-8ae3-a0649c5c5ff2-opus-5-20261116-111429`, trial `WLTLZ4J`. This is the Opus 5 run on the hardened, live task bytes. It was not regraded.
- task_checksum 5f56d8e467890f42a5f676a0fadbd3e7f68ae7df3af2dce5685a7bf0656cb1de. The oracle and nop trials in QC/ have the same checksum, and the delivered task files are identical to the run's.

## §1 Model
- **Identity confirmed (✅).** Every file names the same model in opus-5/run_1:

  | Source | Value |
  |---|---|
  | folder | `opus-5` |
  | pass_summary | `opus-5` |
  | config | `anthropic/claude-opus-5` |
  | result | `claude-opus-5` |
  | report | `opus-5 / anthropic/claude-opus-5` |
  | trajectory steps | `['anthropic/claude-opus-5']` |

  The script printed "distinct models after normalising ['opus-5'] ok" and "models seen mid-run 1 ok".
- ATIF: `ATIF-v1.5 ok`.
- Agent: `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`.
- reasoning_effort: `high`.

## §1.5 Score sanity (per run)
- **1.5a reward agreement: ok.** The reward is 0.2129 in all four places (reward.json, report.final_reward, result.verifier_result and pass_summary.per_run.combined); `spread=0.0`.
- **1.5b pytest: ok.**
  - Source: grade_report.json, 20 rows. earned=8.0, penalty=0.0, total_positive=34, guard_polarity=pass_charges, gate None.
  - Recompute: `0.2353 vs reported 0.2353 ok` (8 / 34).
  - weighted=20, ledger=20, nothing missing or extra; no weight drift.
  - Guards tripped `[]`; 6 tests missed; no test raised.
- **1.5c rubric: ok.**
  - Judge: `ran=True model=gpt-5.6-sol reason=None`, transport codex.
  - Recompute: `0.1905 vs reported 0.1905 / channel 0.1905 ok`.
  - n=24: yes=12, no=12. Raw values are only `['no', 'yes']`; errors 0.
  - judge.toml against the graded set: nothing missing, nothing extra, no weight or text drift. report.rubric count 24 ok.
- **1.5d polarity: ok.** No mismatches. Source weights: positive=42, penalty=6; normalised positives sum to 1.0.
- **1.5e combination: ok.** `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.2129 vs reward 0.2129 ok`.
- **1.5f the run finished.**
  - exception_info=None, errored=False, state_capture_failed=None.
  - 101 agent steps; the last step is an agent step.
  - final_message.md is 3376 chars and identical to the last agent text (`same=True`).
  - Tokens and cost are present in both final_metrics and agent_result: 7,336,933 prompt, 45,296 completion, 7,134,844 cached, $5.96.
- No BLOCKER, so no SIGNOFF_BLOCKED tag.

## §1.6 Aggregates
- Counts: runs=1, completed=1, errored=0, per_run=1, folders=1 (ok).
- Threshold 0.7 in pass_summary, test_weights and pass@1 (ok).
- per_run combined equals the run reward; no pass-rule violations.
- Averages 0.2129 / 0.2353 / 0.1905 recompute ok.
- Flags are empty; judge_models ['gpt-5.6-sol'].
- pass@1.json: passed=0 (recomputed 0), pass_rate 0.0; histogram {'partial': 1}, sum 1 (ok). jobs.json lists the one job (1 trial).
- No AGGREGATE_UNRELIABLE tag.

## §2 Failure classification (per run)
- passed False: reward 0.2129 < 0.7; failure_mode partial.
- **No Bucket A (environment) evidence.**
  - State capture worked (end_env.json shipped).
  - exception None, errored False; the judge ran.
  - 100 tool calls (88 MCP, 12 local), with **0 tool results that look like server errors** (2.1e).
  - Two agent-side call errors were read and are not environment faults. Both happened on Jira, and the agent recovered from both:
    - Step 76: `LightJira_create_issue` with empty arguments `{}`, which returned an empty result.
    - Step 77: a DQ issue with an assignee the server rejected, `{"status":"failed","output":"Invalid assignee"}`.
    - Step 78 retried and created DQ-23.
- **Bucket B: `stale-read`.** The owner accepts this sub-label (2026-11-16). Card U15 originally targeted instruction-ignored, but after hardening it is a live card. The run used every instruction step: all four registry rows, seven Jira tickets created (DQ-23, MLR-89, CAP-33, CAP-34, LCH-147/148/149) plus one transition, three reservations and one note, with no step skipped. So instruction-ignored does not fit. The miss is the live re-measurement. Evidence:
  1. **The run read the dry runs once, before the trigger.** In `agent/trajectory.json`:
     - Step 28, `LightDatadog_list_events`: the 4.2.1 dry-run events (FT-CLM-07 5.10 s, FT-SUB-02 6.90 s).
     - Steps 68–70, `LightBox_download_file` 783100/783102/783103: `dryrun-ft-*.txt` "ft-launcher 4.2.1 … median 5.10 / 7.60 / 6.90".
     - The live event fires on the 3rd distinct window row written. The run wrote recSorFt07clm4k, recSorFt03uw8b2 and recSorFt11fn2c6 at steps 72–74, so the event fired at step 74. FT-SUB-02 followed at step 75.
     - After step 74 the run made no Datadog or Box call. It re-read only Airtable (step 100) and Jira (steps 91–94), then sent the note (step 101).
  2. **The re-measured records were live and returned correctly on the same bytes.**
     - In the harbor oracle trial (QC/Oracle run, `…__3hYpk4i/verifier/agent_trajectory.json`), `mcp__LightDatadog__list_events` right after the four update_record steps returns events 880105–880107: the 4.2.2 notice and the 5.80 s and 9.10 s re-measurements.
     - The Box downloads that follow return the 4.2.2 logs (5.80 / 9.10).
     - The oracle scores 34/34.
  3. **The missed tests and criteria name the stale read.**
     - `verifier/grade_report.json`: all six missed tests (5+5+5+5+3+3 = 26) give "the re-measured dry run of FT-SUB-02 / FT-CLM-07 was not read before the note".
     - `final_message.md`: "FT-SUB-02 — Ready to launch … 4000 × 6.90 / 3600 = 7.67 → 8 h reserved, 128", "5.10 s scales to 10.20 s → 11 h" and "= 480 A100-equivalent GPU-hours".
     - Rubric 1–4, 6, 7 and 9 were judged no for that reason, and penalty 21 (p-window-480) fired.
- 2.2c wired servers never called: GoogleDrive, Kubernetes, ServiceNow, Slack and Trello.
  - These are read-only background apps. Kubernetes is the training cluster, which is a red line to write to.
  - The final message claims none of them was unavailable.
- 2.2d guards tripped: none.
- Not guard-tripped, and not gave-up-early: every deliverable was done.

## §2.5 Isolation and leakage (per run)
- verifier_environment_mode: `separate` (result.json).
- Grader paths touched by the agent: none. No tool-call argument names `/tests`, test_outputs, test_weights, judge.toml, reward, solution/, TRUTH.md, gt_env or oracle.json.
- Leakage in tool results: none.
  - The answer figures 544, 11.6, 9.10 and 5.80 never appear in any result the agent received.
  - The one "10.1" hit is the RISK-04 post-mortem's own arithmetic (3000 × 12.15 / 3600), which is unrelated.
  - No answer file was found in /workspace.
- Trivial-solution credit: N/A, because the run made 88 MCP calls and 18 writes. The calibration nop scored pytest 0.0, rubric 0.0, reward 0.0 (QC/Nop run).

## §3 Reasoning
- **Present (✅).** 33 of 101 agent steps carry reasoning (16,542 chars), in the `thought` field.
- reasoning_effort high.
- Per-step metrics are present on 0 of 101 steps. This is INFO only: totals are in final_metrics.

## §4 Overlap
- 20 tests against 24 criteria: DOUBLE-COUNTED=0, PARTIAL=0, INDEPENDENT=20, redundancy 0%. RUBRIC-ONLY: 24 of 24.
- The highest composite is test_sub02_held_for_capacity_approval against criterion 2 (S1 0.22, S2 0.33), which is below 0.3.
- They grade different things. The test checks the registry label and ticket. Criterion 2 checks that the reply attributes SUB-02's change to timing alone.
- No rubric item restates a guard; there is no "did not write to the cluster / did not delete / did not copy / did not sign out" criterion.
- The four penalties (21–24) are the declared `wrong_figures` twins. Each is stated as a figure "presented as" the answer, so none of them is a guard.
- Lost weight:
  - pytest: 26/34 positive lost (76.5%); guards charged 0.0.
  - rubric: 0.7381/1.0000 positive lost (73.8%); penalties charged 0.0714 (p-window-480).
- Recommendation: keep both.

## §5 False pytests
- 20 tests scanned; 0/20 carry a flag; 0 BLOCKER-class flags.
- §5.2 found no assert or return line that carries a rubric figure.
- Every test reads agent evidence (tool log and/or end state, transitively).
- Guards are pass_charges and assert the forbidden act. None passed (was charged) in this run.

## Verdict
- **SIGNED.**
  - §1, §1.5, §1.6 and §2.5 have no BLOCKER.
  - §2 is Bucket B `stale-read`: a genuine model failure on a healthy environment.
  - §3 present; §4 0 double-counted; §5 0 flags.
