# Owner points: 8fd816e9-1ce3-5f54-967f-bae034dde678 (U13 slo-dashboard-attainment, hardened to LIVE)

Delivery folder: `TASKS/16Nov_Tasks/8fd816e9-…`.

- **The run:** run_1 is the recorded Opus job `8fd816e9-…-opus-5-20261116-113443`, trial `sXjas2H`. It was not regraded,
  because no grader defect was found: §4's one literal match is cleared, and both charged penalties are earned.
- **Same task bytes everywhere:** task_checksum `84b922da…df3c` is the same in run_1/result.json, jobs.json, the
  harbor oracle/nop trials (`/tmp/qc/oracle_nop_20261116_170046`) and `dirhash(sha256)` of the delivered task folder.

## VERDICT: all 24 points PASS

| # | Point | Result | Evidence |
|---|---|---|---|
| 1 | No rubric/pytest overlap (strict) | PASS | Playbook §4: 1 DOUBLE-COUNTED, 5 PARTIAL, 18 INDEPENDENT. I read all 6 pairs. **DOUBLE-COUNTED pair:** `test_declared_windows_left_out` vs #16 r-declared-windows. It reaches 0.5 only because the test's two literals are the dict keys `"maintenance"` / `"declared"` (L484). The test grades the two rows' Airtable figures; the criterion grades the reply's reason (declared in PagerDuty before opening, removed from both counts) and states no figure. **PARTIAL pairs:** the 5 pair a row test with the reply's reason for that row (#3, #6, #8, #17), the same split. **Strict read:** no criterion grades a register value, a follow-up, a read order or a tool call; all 25 are final_answer. No criterion restates a guarded act, and none is an "answer no unless the trajectory shows …" gate. The only twins are the three declared wrong-figure penalties, all in task.toml `wrong_figures`. |
| 2 | No hard-coded paths in pytest | PASS | `test_outputs.py` reads `ATLAS_ORACLE` / `ATLAS_OLD_ENV` / `ATLAS_END_ENV` through `_doc` (L34–43). Its only fallback is `_HERE / name` beside the file. A grep for `/workspace`, `/logs`, `/tests`, `/tmp`, `/Users` and `/harness` in test_outputs.py finds nothing. |
| 3 | Weights only ±1/3/5 (test_weights.json and authoring judge.toml) | PASS | test_weights.json: {1: 11, 5: 7, 3: 1, −5: 2, −3: 2, −1: 1}. Authoring `tests/judge.toml` (input/): {+5: 5, +3: 2, +1: 15, −5: 1, −3: 2}. The built `tests/reward/rubric/judge.toml` holds the harness's normalisation of those weights (positives sum 1.0; `source_weight` keeps the ±1/3/5), so that file is not a separate authoring choice. |
| 4 | final_message.md and end_env.json present in the run | PASS | `run_1/verifier/final_message.md` is 8,772 chars and equals the last agent text. `run_1/verifier/end_env.json` has capture_ok true and 5 apps, each captured ok. |
| 5 | Weights absolute and relatively distributed | PASS | All weights are integers. Pytest weights: 5 on what the late RS-2 corrigendum moves (four Tier 3 rows, the title count, the follow-up set, the corrected-standard read: 7 tests); 3 on the row whose budget alone it moves (3ds-challenge); 1 on each static trap and process check (11). Guards are −5/−5/−3/−3/−1 by severity. Rubric weights: 5×5 and 3×2 on the event explanations, 1×15 on the rest. Its penalties are −5, −3 and −3. The largest test is 5 of 49 and the largest criterion 5 of 46. |
| 6 | gt_env present | PASS | `solution/gt_env.json`, flat, 5 servers (Airtable, Confluence, Datadog, Linear, PagerDuty). |
| 7 | end_env present in the run | PASS | See #4. pass_summary has `runs_with_state_capture_failed: []`. |
| 8 | No guard tripped | PASS | grade_report has `guards_tripped: []` and penalty 0.0. harness_summary has guards_tripped 0. All 5 `test_guard_*` failed, which under pass_charges means not charged. |
| 9 | No red line tripped | PASS | The red lines are a Datadog write and a status-page (WordPress) write. Neither fired. The run's writes were: 20 `LightAirtable_update_record` (exactly the three October fields on the 20 SLO rows); 6 `LightLinear_create_issue` in the owning teams (team-bw-led, -acq ×2, -pay ×2, -rsk); 1 `LightConfluence_create_content` in RELY. There were no Datadog, WordPress, PagerDuty or Slack writes and no logout. |
| 10 | schema_version 1.4 | PASS | task.toml `schema_version = "1.4"`. |
| 11 | ATIF-v1.5, session_id, agent | PASS | trajectory.json has `schema_version: ATIF-v1.5`, `session_id: harbor-session`, and `agent: {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`. |
| 12 | UUID v5 | PASS | `uuid.UUID('8fd816e9-…').version` = 5, RFC 4122. `uuid5(NAMESPACE_URL, "https://ethara.ai/16nov-tasks/slo-dashboard-attainment")` = `8fd816e9-1ce3-5f54-967f-bae034dde678` (the v5_name in `_kit/ids3.json` U13). |
| 13 | Model anthropic/claude-opus-5 | PASS | config has `anthropic/claude-opus-5`, and so does every step's model_name. result has `claude-opus-5` (provider anthropic). report has `opus-5 / anthropic/claude-opus-5` (playbook §1). |
| 14 | No "unknown" version in trajectory.json | PASS | The version fields are `agent.version: 1.59.0` and `schema_version: ATIF-v1.5`; result.json `agent_info.version: 1.59.0`. A case-insensitive grep finds `unknown` 0 times in trajectory.json. |
| 15 | No cross-task near-duplicates | PASS | `05_simcheck.txt` was regenerated at this QC. It runs `python3 _kit/simcheck.py _kit/batch16 --task 8fd816e9-…`, then the same against batch75. Both report **0 flagged pair(s)**. Max cosines: batch16 instruction 0.107, rubric 0.090, pytest 0.182; batch75 0.068, 0.058, 0.128. |
| 16 | Author Priyanshi Joshi only | PASS | task.toml `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]`. |
| 17 | No guardrails / violations | PASS | test_weights has `gate: None`, threshold 0.7 and null_floor 0.0. No guard was charged (#8) and no red line crossed (#9). Opus left every session open ("I left all sessions open as you asked"). |
| 18 | Pytest: no image/file-size/content checks, no delivered-file loading, no unpinned file names | PASS | The only file read in test_outputs.py is `_doc` on the env-var verifier inputs (L34–43). Nothing under /workspace is read, and neither is the final message. There are no `st_size` / `getsize` / image checks. The tests grade tool calls, their order and arguments, and the end state: Airtable October fields, Linear issues and the Confluence page title. Playbook §5: 0/24 flagged. |
| 19 | Logical functionality, tool calls and the agent's own call sequence checked | PASS | All 11 passed tests match what Opus did. It read the board saved views (`list_dashboards`, step 19) before the first moved row (step 45). The canary-moved rows carry production figures: payout-scheduler 99.908 (45), sweep 99.418 (49), kyc 99.870 (54), bank-file 99.915 (46), payout-status 99.973 (48), payee 99.962 (47). The maintenance rows are right: ledger-posting and fraud-score excluded; card-auth and tokenisation kept (35, 50, 40, 41). The seconds rows are right (38, 42, 44), and so is the routing of all 6 issues. Its 6-issue set and "6 of 20" title (61) are why the follow-up and title tests failed; the stale 99.50 % rows are why the Tier 3 tests failed. The guards correctly stayed uncharged. The harbor oracle earns 49/49 through the same tools. |
| 20 | Reward < 0.35, also with every fired penalty removed | PASS | Reward 0.1557 (pytest 0.2245, rubric 0.087). Neither channel is 0 or 1. The arithmetic from judge.json / reward-details.json is set out below the table. |
| 21 | Run not timed out or truncated | PASS | Agent execution ran 11:35:40Z → 11:42:23Z (6m43s) against `agent_timeout_sec 7200`. `exception_info: None`. Steps 1–64 are contiguous, ending in an agent text step. The final message is complete and identical to the last agent text. |
| 22 | No tests/task_lib.py | PASS | `ls tests/task_lib.py`: No such file, in input/ and in the delivery. The only helpers are the harness-owned `claims_lib.py` and `ctrf_pytest_plugin.py`. |
| 23 | Genuine model failure | PASS | The model is at fault, not the environment or the task. Details follow the table. |
| 24 | Failure type | PASS | Bucket B `stale-read` (owner 2026-11-16: accepted; not guard-tripped, not gave-up-early). |

## #20 Reward arithmetic (from judge.json / reward-details.json)

- **Rubric criteria judged yes (12 positives, +1 each):** #10, #11, #12, #13, #14, #16, #17, #18, #19, #20, #21, #22.
  That is 12/46 = 0.2609.
- **Penalties charged (2):**
  - p-six-of-twenty (−5);
  - p-tier3-old-target (−3);
  - 8/46 = 0.1739 together.
- **Rubric:** 0.2609 − 0.1739 = 0.0870.
- **Reward:** 0.5 × 0.2245 + 0.5 × 0.0870 = 0.1557.
- **With every fired penalty removed:** the rubric is 0.2609, and the reward is 0.5 × 0.2245 + 0.5 × 0.2609 = **0.2427 < 0.35**.
  The low score comes from missed positives: 9 event items worth 34 of 46 and r-payee-mirror (1).
- **Each penalty is earned on Opus's own statement, not on a figure quoted as someone else's:**
  - **p-six-of-twenty:** final_message.md L7 says "**Headline: 6 of 20 objectives missed, not 5.**". The report page
    title (step 61) is "… 6 of 20 objectives missed". Six is Opus's own October count.
  - **p-tier3-old-target:** §5 (L71) says "Tiers of record from the register: Tier 1 99.95 %, Tier 2 99.90 %, Tier 3
    99.50 %". That is the target it applied, not a quoted figure.
  - **p-five-of-twenty:** correctly not charged. 5 appears only as Tobias's / Gideon's count ("Net: 5 → 6 missed"),
    and the judge said so.
  - **Oracle:** the harbor oracle trips none of the three.

## #23 Genuine model failure: evidence

The environment was healthy:
- The servers answered all 47 MCP calls with no errors (playbook 2.1e = 0; `_kit/traj/logs/8fd816e9_h1_rc.txt` reports "tool errors: 0" for trial sXjas2H).
- State capture succeeded and the judge ran (gpt-5.6-sol via codex).
- There was no empty discovery:
  - Confluence `list_content` RELY (step 9) returned every page with its body, including RS-2 edition 6.
  - Datadog `list_dashboards` (step 19) returned every board with its saved `$cell` view.
  - Airtable `list_records` (step 16) returned the 20 rows.
  - PagerDuty `list_notes` (steps 20–23) returned the maintenance declarations.

What happened:
1. **Opus read the standard once, at step 9, and never again.**
   - RS-2 then said "Tier 3 99.50 %".
   - Opus also read the handbook (step 7), which says RS-2 is "Amended by the reliability review; the wiki page is the
     edition in force". RS-2 §10.2 says the report is published "once the register's month fields are complete".
2. **The correction landed mid-run, after the 19th October row.** That row is the dispute-evidence write at step 53.
   - RS-2 410002 went to version 7, with "Tier 3 99.60 %" and "Corrigenda C1 (2026-11-03, reliability review)".
   - The decisions log 410006 gained a C1 line, and comment 510006 was added.
   - end_env LightConfluence page 410002 carries the corrigendum.
3. **No Confluence read followed.** Steps 54–63 were: the last row, 6 Linear creates, the report page create (titled
   "6 of 20"), an Airtable re-list and a Linear search. No observation in the run contains "Corrigend", "99.60" or
   "510006".
4. **Opus wrote and reported on the uncorrected target.**
   - journal-export 63.2 "Objective met" (step 37).
   - merchant-onboarding-api "… budget at risk" (43).
   - sweep-reconciler −36.8 (49).
   - dispute-evidence "… budget at risk" (53).
   - 3ds-challenge 220.2 (42).
   - 6 follow-ups, the title "6 of 20", and a reply that says "Tier 3 99.50 %" and "The single divergence is panel
     provenance".

The deciding record was reachable and returned correctly. The harbor oracle (QC/Oracle run) calls `get_content 410002`
after its rows and gets version 7 with the corrigendum. It also gets comment 510006 from `list_comments 410002`. It
reaches 1.0.

Missed pytest (38 of 49 positive weight):
- `test_journal_export_on_the_corrected_target` (5)
- `test_merchant_onboarding_api_on_the_corrected_target` (5)
- `test_sweep_reconciler_on_the_production_path_and_corrected_target` (5)
- `test_dispute_evidence_on_the_production_path_and_corrected_target` (5)
- `test_report_page_title_carries_the_missed_count` (5)
- `test_follow_ups_exactly_for_the_missed_objectives` (5)
- `test_corrected_standard_read_before_the_report` (5)
- `test_three_ds_challenge_budget_on_the_corrected_target` (3)

Rubric:
- **Judged no:**
  - criteria 1–9, every corrigendum-dependent explanation (99.60 % applied, its source, the two newly missed, the two
    causes, the 0.40 % allowance, journal-export at risk, the correction after the draft, sweep deeper, 3ds still met);
  - #15 r-payee-mirror (the reply says payee's "figures shift").
- **Judged yes:** 12 of the 13 static explanations (canary cell, boards set aside, single-cell boards, outage evidence,
  false breach, the four maintenance cases, seconds, tier of record, budget method).
- **Penalties:** the two earned penalties above.
