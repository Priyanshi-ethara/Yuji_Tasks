# QC Report — f487e5dd-4b6a-5589-bf99-346f3dc18122   layout: full (reward.json trimmed to {"reward"})   runs: 1   model(s): opus-5

I re-ran `qc 2/traj/10_bundle_playbook.md` after the finalize regrade with `BUNDLE` set to a scratch copy of the delivery folder D. That copy has reward.json already trimmed to `{"reward": 0.1834}`. Every script ran exactly as written, in order (loader, then §1, §1.5, §1.6, §2, §3, §4 and §5). Raw output: `03_playbook_script.txt`.

## §1 Model
- **opus-5/run_1: identity confirmed ✅.**
  - folder `opus-5`; pass_summary `opus-5`
  - config `anthropic/claude-opus-5`; result `claude-opus-5`
  - report `opus-5 / anthropic/claude-opus-5`; every step `anthropic/claude-opus-5`
  - distinct models after normalising `['opus-5']`; models seen mid-run 1
- **Format and agent:** ATIF-v1.5 (ok). Agent `openhands-sdk` v1.59.0 in result and trajectory (`{'name': 'openhands-sdk', 'version': '1.59.0'}`), with no "unknown" version. session_id `harbor-session`. reasoning_effort `high`.

## §1.5 Score sanity (per run)
- **1.5a:** reward 0.1834 in reward.json, report.final_reward, result.verifier_result and pass_summary.per_run; spread=0.0 ok.
- **1.5b:** ledger from grade_report.json, 26 rows. earned=10.0, penalty=0.0, total_positive=50, so recompute 0.2 = reported 0.2 ok. No weight drift, no weighted test unrun. Guards tripped `[]`; 10 missed; no test raised.
- **1.5c:** judge ran=True, model gpt-5.6-sol. Rubric recompute 0.1667 = reported 0.1667 ok. n=24 (11 yes, 13 no); raw values {yes, no}; errors 0. judge.toml and the graded set match (no missing, extra or drift).
- **1.5d:** polarity mismatches none. Source weights: positive 42, penalty 8.
- **1.5e:** 0.5·0.2 + 0.5·0.1667 = 0.1834 = reward ok.
- **1.5f:** exception_info None; errored False; 111 agent steps; last step is an agent step. final_message.md (9741 chars) equals the last agent text. Tokens 7 094 237 in, 41 631 out; cost $5.90.

## §1.6 Aggregates
- **Counts:** runs=1, completed=1, errored=0, per_run=1, folders=1 ok.
- **Threshold:** 0.7 in pass_summary, test_weights and pass@1 ok.
- **Pass bit:** passed=false (0.1834 < 0.7), no violation.
- **Averages:** 0.1834 / 0.2 / 0.1667 match.
- **pass@1.json:** passed 0, pass_rate 0.0, histogram {partial: 1}, sum 1 ok.
- **jobs.json:** job `…-opus-5-20261113-215846-regraded`, 1 trial (fwYYGti).
- **Flags:** runs_without_rubric [], runs_with_state_capture_failed [].
- **Checksum:** jobs.json task_checksum `fa6ce188…` matches the fin9 oracle/nop trials. The fix is in the final build (fin9, task_checksum `fa6ce188…`). The regraded Opus job, the fin9 oracle and the fin9 nop all carry that checksum, and the regrade left every score and every yes/no unchanged (0.1834 = 0.5·0.2 + 0.5·0.1667). See the stale-build finding in 02_Ruthless.md. Per §1, a checksum difference is informational.

## §2 Failure classification (per run)
- **Outcome:** passed=False; reward 0.1834 < 0.7; failure_mode `partial`.
- **Bucket: B (model/agent).** No 2.1 evidence:
  - end_env.json shipped; state capture not failed.
  - exception None; judge ran.
  - 110 tool calls (104 MCP); **0** tool results that look like server errors.
  - The 5 never-called servers (GoogleMaps, OpenWeather, QuickBooks, Shippo, Weather) are look-only background the instruction lists as "look-but-don't-touch". None is needed.
- **Sub-label: `instruction-ignored`.** DS-6 9.3 requires a countersign request before release for every Approved design whose roof sees colder mornings than its station. The run skipped that step for all four roof-held designs, although it called the same tool for the three 95 % holds and had the deciding records listed in front of it.
  1. **The model knew what to check (agent/trajectory.json step 34).** Its reasoning says: "The DS-6 and 9.3 definitions tie a station's extreme minimum to the open ground it sits on and the roof's coldest morning, so I'm checking whether any survey notes that the site's elevation or frost-hollow conditions differ from the station's." Its recursive `LightDropbox_list_folder("/Design Desk")` at step 34 returned `/Design Desk/W46/Site surveys/Field sheets` and all 20 `FS-46xx.md` paths.
  2. **It skipped the step.**
     - Steps 35–54 downloaded only the 20 `SS-46xx_*.md` surveys. No `FS-46xx.md` was ever opened.
     - Step 55: "I've confirmed the surveys match the register", and the model moved on to Ardent serials.
     - Steps 100–110 called `LightLinear_create_issue` 11 times: 8 reworks and 3 countersigns (7302107, 7302133 and 7302136, the >95 % half only). There was none for 7302104, 7302121, 7302150 or 7302153.
     - Step 112 posted `Released: 9 | …`.
  3. **Grader confirmation.**
     - Missed tests: the 4 × `test_*_held_design_has_countersign_request` (5 each), the 4 × `test_*_held_request_routed_to_head_of_engineering` (3 each), `test_week_line_counts_released_designs` (5) and `test_field_sheet_read_before_the_line` (3).
     - Passed: `test_near_limit_approvals_have_countersign_requests` and the 9 verdict, rework and week-line tests.
     - The rubric said no to criteria 1–10 (fin9 regrade judge: "The final answer does not list Penhale/7302104 among designs held from release"). Penalty 21 (`Released 9`) was charged.
- **Why not the other labels:**
  - Not `stale-read`: there is no live event or re-delivery, and end_env differs from the seed only by the run's own writes.
  - Not `guard-tripped`: guards [].
  - Not `gave-up-early`: the final message claims a complete review.
  - Not `wrong-value-written`: `Released: 9` is the downstream effect of the skipped step. The verdicts, Voc and lengths it wrote are correct (all 10 value tests pass).
- **Genuineness.** The deciding fact was stated by the governing document (9.3 + 2.3). It was listed by the tool the run called (step 34), and `download_file` returns it correctly (the oracle reads it). The model even voiced the right question, then did not open the subfolder. This is a model error, not an environment or task defect.

## §2.5 Isolation and leakage (per run)
- verifier_environment_mode: `separate`.
- Grader paths touched by the agent: none. A grep of every tool-call argument for /tests, test_outputs.py, test_weights.json, judge.toml, reward, solution/, TRUTH.md, gt_env.json and oracle.json returned [].
- Leakage in tool results: none. No seeded W46 countersign, held list or week line exists. "Countersign" occurs only in the DS-6 clause text.
- Trivial-solution credit: none. The run made 104 MCP calls and 32 writes. The harbor nop scored 0/0/0.

## §3 Reasoning
- 111 agent steps, 24 with reasoning (9917 chars), in field `thought`. Effort `high`. Verdict: present ✅. Per-step metrics are 0 of 111 (INFO: totals are in final_metrics).

## §4 Overlap
- 26 tests against 24 criteria: DOUBLE-COUNTED 0, PARTIAL 1, INDEPENDENT 25; redundancy 0 %. Rubric-only: 24 of 24.
- **The one PARTIAL:** `test_approved_designs_verdict_and_length` (w 1) against criterion 6 (+3), composite 0.33 (S1 0.16, S2 0.50). I read both:
  - The test checks `design_status` and `modules_per_string` on the approved HubSpot deals.
  - Criterion 6 checks that the reply explains "released = approvals less every design held for countersign".
  - The only shared literal is "Approved". They are different outcomes in different channels, so the pair is INDEPENDENT.
- **Lost weight in this run:** pytest positive lost 40/50 = 80.0 %, guards charged 0; rubric positive lost 76.2 %, penalties charged 0.0714.
- **Recommendation:** keep both.

## §5 False pytests
- 26 scanned, 0 flagged, 0 blocker-class flags.
- No 5.2 assert or return line carries a rubric figure.

## Verdict
- **SIGNED.**
  - §1, §1.5, §1.6 and §2.5 have no BLOCKER.
  - §3 shows reasoning present.
  - §4 and §5 have no major or minor finding.
  - §2 is Bucket B, `instruction-ignored`, genuine. It is not stale-read, guard-tripped, gave-up-early or Bucket A.
