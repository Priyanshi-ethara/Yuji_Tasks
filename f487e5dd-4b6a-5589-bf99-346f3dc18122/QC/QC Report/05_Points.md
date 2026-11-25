# Owner points — f487e5dd-4b6a-5589-bf99-346f3dc18122 (T49 pv-string-design-review, slot 6)

**Verdict: PASS on every point.** The delivered run is job `f487e5dd-…-opus-5-20261113-215846-regraded`, trial fwYYGti: reward 0.1834 (pytest 0.2, rubric 0.1667), guards [].

| # | Point | Result | Evidence |
|---|---|---|---|
| 1 | No rubric/pytest overlap | PASS | Playbook §4: 0 double-counted, 25 independent, 1 partial. The partial is the verdict/length test against criterion 6 (released arithmetic in the reply): a different outcome in a different channel, so independent. The rubric grades only the reply (final_answer); pytest grades app state and calls. |
| 2 | No hard-coded paths in pytest | PASS | check_bundle: "hard-coded in test_outputs.py: none". Paths and file names (field sheets included) come from oracle.json and old_env.json, not from literals. |
| 3 | Weights only ±1/3/5 (test_weights.json, judge.toml) | PASS | test_weights {−5, −3, −1, 1, 3, 5}; judge.toml source weights {5, 3, 1, −1, −3} |
| 4 | final_message.md and end_env.json both in the run | PASS | Both are in run_1/verifier/: final_message.md is 9741 chars; end_env.json is shipped. |
| 5 | Weights absolute and distributed | PASS | Tests: 20 positive totalling 50 (four 5s, four 3s, one 5 for the line, one 3 for the read, ten 1s), 6 guards. Rubric: 20 positive totalling 42 (5×5, 1×3, 14×1), 4 penalties. No item exceeds half its channel. |
| 6 | gt_env present | PASS | solution/gt_env.json is present. The oracle's fresh replay equals it exactly (02_ruthless_mechanical.txt). |
| 7 | end_env present in the run | PASS | run_1/verifier/end_env.json; state_capture_failed none |
| 8 | No guard tripped | PASS | guards_tripped [] (grade_report.json); penalty 0.0 |
| 9 | No red line tripped | PASS | No deal stage or amount change, no customer mail, no Shippo or QuickBooks call, no logout (2.2a inventory). Writes: only 20 update_deal, 11 create_issue in team DESIGN and 1 update_project. |
| 10 | schema_version 1.4 | PASS | task.toml `schema_version = "1.4"` |
| 11 | ATIF-v1.5 | PASS | trajectory.json schema_version `ATIF-v1.5` |
| 12 | UUID v5 | PASS | `uuid.UUID("f487e5dd-4b6a-5589-bf99-346f3dc18122").version == 5` |
| 13 | Model anthropic/claude-opus-5 | PASS | config and every step: `anthropic/claude-opus-5`; result `claude-opus-5`; folder `opus-5` |
| 14 | No "unknown" version in trajectory.json | PASS | agent `{'name': 'openhands-sdk', 'version': '1.59.0'}`; session_id `harbor-session` |
| 15 | No cross-task near-duplicates | PASS | `python3 $KIT/simcheck.py $KIT/batch30 --task f487e5dd…`: 0 flagged pairs. Max cosine: instruction 0.088, rubric 0.049, pytest 0.105 (05_simcheck.txt). |
| 16 | Author Priyanshi Joshi <priyanshi.joshi@ethara.ai> | PASS | task.toml authors |
| 17 | No guardrail violations | PASS | Same as rows 8–9. The run stayed signed in (no logout call), and every write is inside the instruction's write scope. |
| 18 | Pytest: no image, file-size or content checks; no delivered-file loading; no unpinned file names | PASS | Tests read only oracle.json, old_env.json, end state and trajectory. The workspace is not loaded (artifacts/workspace is empty and no test reads it). Playbook §5: 0 flags. |
| 19 | Logical functionality and tool calls checked | PASS | Tests check deal properties against the oracle, Linear issues (title grammar, team, assignee, cancelled counts as withdrawn), the project line posted after every write, and the Dropbox `download_file` of a held design's field sheet before the line. |
| 20 | Reward < 0.35 | PASS | 0.1834 |
| 21 | Failure type: §2 sub-label is not `stale-read` | PASS | `instruction-ignored`, Bucket B (03 §2) |
| 22 | **Failure type differs from the 60 stale-read tasks** | PASS | See below. |
| 23 | Run not timed out or truncated | PASS | 10 min 17 s of 7200 s. exception None. The last step is an agent step with the full reply. |
| 24 | No tests/task_lib.py | PASS | tests/ holds test_outputs.py, test_weights.json, oracle.json, old_env.json and the harness files only. |
| 25 | Genuine model failure | PASS | See below. |

## Row 22: failure type differs from the 60 stale-read tasks
- **Sub-label:** `instruction-ignored`, meaning a required conditional step was skipped.
- **Mechanism (REDESIGN_NOTES.md).** DS-6 9.3 releases an Approved design on one signature only if T_min (2.3: the coldest morning of the station's open ground) is the coldest morning its roof will see, and Voc,max ≤ 95 %. Otherwise a countersign request goes to the Head of Engineering in Linear DESIGN. Four roofs are in valley bottoms below their station, recorded only on the field sheets one subfolder down. The trap is static, with no live event: end_env differs from the seed only by the run's own writes (20 HubSpot deals, 11 Linear issues).
- **Trajectory evidence:**
  - **Step 34:** Opus states it will check "whether any survey notes that the site's elevation or frost-hollow conditions differ from the station's". Its recursive list of /Design Desk returns `/Design Desk/W46/Site surveys/Field sheets/FS-4604.md … FS-4653.md`.
  - **Steps 35–54:** it downloads the 20 SS surveys only. It never opens FS-4604, FS-4621, FS-4650 or FS-4653, the deciding records.
  - **Step 55:** "I've confirmed the surveys match the register".
  - **Steps 108–110:** it raises countersigns for 7302107, 7302133 and 7302136 only (the 95 % half).
  - **Skipped act:** the countersigns for 7302104, 7302121, 7302150 and 7302153.
  - **Step 112:** it posts `Released: 9`.

## Row 25: genuine model failure
- **Tests missed (40 of 50):**
  - 4 × held_design_has_countersign_request (5 each)
  - 4 × held_request_routed_to_head_of_engineering (3 each)
  - week_line_counts_released_designs (5)
  - field_sheet_read_before_the_line (3)
- **Rubric:**
  - Criteria 1–10 were judged no: the roof-held designs are absent from the not-released list, and the 9.3 roof half was never applied.
  - Penalty 21 was charged for `Released 9`.
  - The 10 earned criteria include edition, units, limits and the draft set aside.
- **Why this is the model's error:**
  - DS-6 9.3 and 2.3 state the rule.
  - The tool returned the sheet paths at step 34, and `download_file` returns their text (the oracle reads them).
  - 0 tool errors; no empty discovery.
  - The instruction names the Dropbox site surveys as the source for "where".
  - The model voiced the right question and then did not open the subfolder.
- **No task defect:** no record contradicts the sheets (02_Ruthless.md, trap fairness).

## Grader-side change made in this QC (regrade done)
- task.toml `verification_explanation` (line 97): the stray-rule wording was changed to match tests/test_outputs.py `_stray_countersigns` (line 274, `roof_below_station_m > 0`).
- Metadata only. No test, weight, rubric or agent-visible byte changed.
- The fix is in the final build (fin9, task_checksum `fa6ce188…`). The regraded Opus job, the fin9 oracle and the fin9 nop all carry that checksum, and the regrade left every score and every yes/no unchanged (0.1834 = 0.5·0.2 + 0.5·0.1667). See the stale-build finding in 02_Ruthless.md.
