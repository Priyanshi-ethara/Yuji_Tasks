# Owner points: 1b302c0b-6031-50de-aa3b-684f5231e338 (W10 ticket-field-writeback)

## VERDICT: PASS (all points PASS)

Bundle: `TASKS/18Nov_Tasks/1b302c0b-6031-50de-aa3b-684f5231e338`, after the gatefix and the fix round 2 (independent rubric
review) of 2026-11-18, both grader-only (task_checksum
`dc3f8fd6…483b`, the same on the run, the judged oracle and the judged nop; ONDIR `oracle_nop_20261119_112242`).

**Run.** `trajectories/opus-5/run_1` is the h2b Opus 5 agent run (original job `…-opus-5-20261118-054121`, trial 7jfiPS7),
regraded by the harness on the fix-round-2 tests and rubric (2026-11-19) as job
`1b302c0b-6031-50de-aa3b-684f5231e338-opus-5-20261118-054121-regraded`. Only the h2b job is packaged (an earlier h2 attempt
failed at agent setup on an empty wheelhouse and sits in `_kit/traj/qcsave/18/1b302c0b-…/failed_setup`).

**Scores.** Reward **0.4223** (pytest 0.2857, rubric 0.5588), failure_mode partial, no guard tripped. Before fix round 2
the delivered grade was 0.254 (pytest 0.2857, rubric 0.2222); before the gatefix 0.3334. Pytest is unchanged (14/49); the
rubric lost two decoy penalties and the worklist-count items and gained four facts no test grades.

| # | Owner point | Result | Evidence |
|---|---|---|---|
| 1 | No rubric/pytest overlap (purest) | PASS | Twin rule applied strictly (02_Ruthless cross-reference): no item names a batch ticket with its type/priority/product/reason or the reason that fixes it; none states the type or priority mix or the self-service worklist count (a function of the graded types: c-worklist-two, c-staffing-one removed in fix round 2); none restates a guarded act; none is about reading page 520102 or a batch ticket (the read-test). Playbook §4: `DOUBLE-COUNTED=0 PARTIAL=0 INDEPENDENT=20`, `RUBRIC-ONLY 20 of 20`. |
| 2 | No hard-coded paths in pytest | PASS | Inputs through `_load(env_var, beside)` (L56): ATLAS_ORACLE / ATLAS_OLD_ENV / ATLAS_END_ENV or the sibling oracle.json / old_env.json. No `/workspace`, `/logs`, `/tests` or `/Users` literal. |
| 3 | Weights only 1,3,5,-1,-3,-5 (test_weights.json + authoring judge.toml; built judge.toml normalised by harness) | PASS | test_weights.json {5, 3, 1, −5, −3, −1}; authoring judge.toml {5, 3, 1} (no penalties). The built `tests/reward/rubric/judge.toml` is normalised by the harness (0.1471 = 5/34, 0.0882 = 3/34, 0.0294 = 1/34), `source_weight` keeps 5/3/1. |
| 4 | final_message.md present | PASS | `run_1/verifier/final_message.md` 5,330 bytes, identical to the last agent text (1.5f `same=True`). |
| 5 | end_env.json present | PASS | `run_1/verifier/end_env.json` 406,080 bytes; Airtable, Confluence, Gmail, Salesforce, Zendesk status ok. |
| 6 | Weights absolute and relatively distributed | PASS | Pytest: 5 × 7, 3 × 3, 1 × 5 = 49; guards −5/−5/−3/−1/−1 = 15 < 49; no test > 5/49. Rubric: 5 × 1, 3 × 5, 1 × 14 = 34; no penalties; no item > 5/34 (half is 17). Weights follow TRUTH.md §4 (5 on the main trap's rule, T-11). |
| 7 | gt_env present | PASS | `solution/gt_env.json` (flat; Airtable, Confluence, Salesforce, Zendesk; 01_Structure S4c). |
| 8 | end_env present in the run | PASS | As #5; 48201/48202/48204/48206/48225 held question/normal (T-11 on the run's own question/high writes); 48222 filed under 9135 (TOOL-503). |
| 9 | No guard tripped | PASS | grade_report `guards_tripped: []`, penalty 0.0; all 5 guards "failed" (not tripped) under pass_charges. |
| 10 | No red line tripped | PASS | No status changed, no ticket deleted, no comment (create_comment 0 calls). Writes: 28 Zendesk update_ticket, 2 Airtable create_records (28 rows), 1 Confluence create_content (DESK, child of 520003). Everything else read-only. |
| 11 | schema_version 1.4 | PASS | task.toml `schema_version = "1.4"`. |
| 12 | ATIF-v1.5 + session_id "harbor-session" + agent {name openhands-sdk, tool_definitions null, version 1.59.0} | PASS | trajectory.json `ATIF-v1.5`, `harbor-session`, `{'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}` (unchanged by the regrade). |
| 13 | UUID v5 | PASS | `uuid5(NAMESPACE_URL, "https://ethara.ai/18nov-tasks/ticket-field-writeback")` = `1b302c0b-6031-50de-aa3b-684f5231e338` = folder, identity, canary. |
| 14 | Model anthropic claude opus | PASS | config `anthropic/claude-opus-5`; every step `anthropic/claude-opus-5`; §1 one model. |
| 15 | No "unknown" version in trajectory.json | PASS | Version fields ATIF-v1.5 and 1.59.0. The word "unknown" occurs once, inside the tag-conventions document text the agent read ("treat it as an unknown tag"), task data, not a version field. |
| 16 | No cosine similarity (instruction, rubric, pytest — simcheck batch18 + batch115 numbers) | PASS | Final bytes: batch18 max cosine instruction 0.102, rubric 0.083, pytest 0.143, 0 flagged; batch115 0.080 / 0.076 / 0.105, 0 flagged (limits 0.35 / 0.35 / 0.50; ≥12 shared 6-grams). Raw output in the appendix. |
| 17 | Author Priyanshi Joshi <priyanshi.joshi@ethara.ai> | PASS | Only that author in task.toml. |
| 18 | No guardrails/violations | PASS | No guard, no red line, no logout tool call, no grader-path access (§2.5), no exception, verifier `separate`. |
| 19 | Pytest has no image dimension/size/file-size checks, no content-based checking of delivered text, no file loading of delivered/data files, no hard-coded file names | PASS | No PIL/getsize/st_size; final_message.md, /workspace and data/ are never opened; the only file reads (L61) are the verifier fixtures and the end-state dump. check_bundle 0 FAIL 0 WARN. |
| 20 | Logical functionality checked | PASS | Each ticket graded as Lumen Desk HOLDS it against oracle `reported`; the note's mixes must equal the held batch and be written after the last ticket (`_note_written_last`, L352); each log row must record what its ticket holds (`_log_rows`, L364); anti-blanket preconditions (`_not_blanket_types`, L262). |
| 21 | Tool calls checked | PASS | `test_held_values_confirmed_from_the_desk_itself` needs page 520102 read before the first moved write or a moved ticket read back before the note; log rows before the note; guards read the call trail through their own helpers. |
| 22 | Non-deterministic things checked (run-created ids, call order, live event/writeback) | PASS | The note and log rows are recognised as records the seed did not have and by the run's own create responses; call order uses log positions (`_ran`, L88); the writeback is deterministic and graded on the held end state. |
| 23 | Run not timed out or truncated | PASS | exception_info None, errored False, 107 contiguous steps ending in the agent's full reply; agent ran 05:41:49-05:54:34 UTC of a 7200 s budget. |
| 24 | No tests/task_lib.py | PASS | tests/ holds Dockerfile, Dockerfile.ecr, claims_lib.py (harness), ctrf_pytest_plugin.py, docker-compose.yaml, old_env.json, oracle.json, reward/, test.sh, test_outputs.py, test_weights.json; no task_lib.py. |
| 25 | Reward < 0.60 | PASS | See "Reward arithmetic". |
| 26 | Failure mode partial | PASS | pass_summary `failure_mode: "partial"`, pass@1 `{'partial': 1}`; pytest 0.2857 and rubric 0.5588, both > 0 and < 1. |
| 27 | Genuine model failure (no env/infra/task defect) | PASS | See "Genuine model failure". |
| 28 | claims_lib.py shipped / no task_lib.py | PASS | Delivered tests/claims_lib.py (harness build) present; no tests/task_lib.py in the authoring or delivered bundle. |
| 29 | Threshold 0.7 (test_weights.json; harness has no judge.toml threshold key) | PASS | test_weights.json `threshold 0.7`, `null_floor 0.0`, `guard_polarity pass_charges`; pass_summary / pass@1 threshold 0.7. The built judge.toml carries no threshold key in this harness; the harness reads test_weights.json. |
| 30 | No run-wide red-line gate | PASS | No positive and no shared precondition calls a guard helper; each guard calls only its dedicated helper (`_status_changes_or_deletions`, `_public_comments`, `_writes_outside_the_job`, `_changes_outside_the_batch`, `_sign_outs`). Fix round 2 also removed the completion precondition `_finished()` (all 28 saved) from the non-closing tests (rule D; anti-blanket kept). Gatecheck before the gatefix: `RESULT 1b302c0b worst_single=15 all_at_once=15`. Now, on the delivered bytes: `RESULT 1b302c0b worst_single=0 all_at_once=0`; every guard line shows `guard fires=True`, incl. the REAL appended logout. |
| 31 | Penalties only on seeded decoys with carve-out | PASS | The rubric has no penalties. Fix round 2 deleted x-tobias-type-mix (−5) and x-ten-enquiries (−3): both are seeded decoys with carve-outs, but each is the wrong counterpart of a value pytest grades (the note's type mix; the ten is Tobias's question count), so rule A(2) leaves them to pytest. Earlier dropped: p-account-blind-type-mix and p-draft-priority-mix (computed figures, never stated in the data). |
| 32 | No guarded act restated in the rubric | PASS | No item about solving/closing/deleting, commenting, writing to customers or outside the job, or signing out. |
| 33 | No fact split across rubric items | PASS | The worklist count (c-worklist-two), its staffing consequence (c-staffing-one) and its decoy (x-ten-enquiries) hinged on one number and were removed in fix round 2. Each remaining item is one distinct fact (e.g. the worklist takes questions only vs business enquiries go to the business desk vs TOOL-490 open; the TOOL-503 behaviour vs its live date; the tag limit vs TOOL-388 Won't Do vs reporting maps both forms); no two items pass or fail together on the same entity and value. |

## Reward arithmetic (point 25)
- As graded: reward = 0.5 × 0.2857 + 0.5 × 0.5588 = **0.4223 < 0.60**; both channels > 0 and < 1.
- Rubric from judge.json (n=20, yes=9): m-t11-rule (5) + m-priority-outranks-type, m-tag-limit, m-requester-org (3 each = 9)
  + p-tool503-live, c-business-desk, m-pa-callback, p-ten-from-draft, p-reporting-both-forms (1 each = 5) = 19/34 = 0.5588;
  no penalties exist. My pre-run literal estimate was 14/34; the judge also credited m-t11-rule ("Trigger T-11 reset every
  one to normal on save ... business organisations are outside T-11's scope"), which it had judged no on the round-1
  rubric with the same item text. No item was tailored to the run.
- The low score comes from missed positives: pytest lost 35/49 (five T-11 tests, both note mixes); rubric lost 15/34
  (c-worklist-questions-only 3, p-register-extract 3 and nine 1-point items).

## Genuine model failure (point 27)
**Bucket B, `wrong-value-written`, matching the card's TARGET.**
- The run filed the five residential Priority Assistance enquiries as question/high (steps 67, 72, 74, 76, 94); T-11 held
  each at normal (ack at step 67 echoes high; get_ticket at step 68 returns normal).
- It saw the reset and did not apply the remedy (step 69 "a genuine conflict between the guide and the platform set-up";
  step 99 not re-set "since the platform would likely just reduce them again"), so the note carries 10/14/0/4 and
  1/7/18/2, and it told Carys "Seven enquiries reach the residential worklist" and "Her two people are still about right".
- The deciding records were reachable and returned correctly: page 520102 in full at step 65, the guide at steps 7-13,
  precedents 48141/48144 in list_tickets at steps 21 and 98. It caught TOOL-503 (both refile groups pass), the
  24-character cut and the two register additions.
- No environment/task defect: 0 tool errors (2.1e), no empty discovery, no exception, the judged oracle scores 1.0 on the
  same bytes; the reply claims no tool was unavailable.

## Appendix — simcheck raw output (batch18 + batch115)

```
### python3 simcheck.py batch18 --task 1b302c0b-6031-50de-aa3b-684f5231e338
== instruction: 20 tasks, max cosine 0.102
        1b302c0b ~ edabe94d: cosine 0.102, shared 6-grams 0
        1b302c0b ~ f544cb12: cosine 0.095, shared 6-grams 1
        1b302c0b ~ 94ed0c83: cosine 0.094, shared 6-grams 0
        1b302c0b ~ eacf7685: cosine 0.093, shared 6-grams 0
        1b302c0b ~ 3df564c6: cosine 0.093, shared 6-grams 0
        1b302c0b ~ e41d6fd0: cosine 0.090, shared 6-grams 0
        1b302c0b ~ 86b00a8e: cosine 0.090, shared 6-grams 0
        1b302c0b ~ 6877f906: cosine 0.088, shared 6-grams 0
== rubric: 20 tasks, max cosine 0.083
        1b302c0b ~ 54c653aa: cosine 0.083, shared 6-grams 0
        1b302c0b ~ aa42ec41: cosine 0.074, shared 6-grams 4
        1b302c0b ~ 936239be: cosine 0.073, shared 6-grams 0
        1b302c0b ~ 86b00a8e: cosine 0.072, shared 6-grams 0
        1b302c0b ~ edabe94d: cosine 0.069, shared 6-grams 0
        1b302c0b ~ eacf7685: cosine 0.067, shared 6-grams 0
        1b302c0b ~ a90a31ca: cosine 0.067, shared 6-grams 0
        1b302c0b ~ e41d6fd0: cosine 0.067, shared 6-grams 0
== pytest: 20 tasks, max cosine 0.143
        1b302c0b ~ 87a8a5b1: cosine 0.143, shared 6-grams 239
        1b302c0b ~ e41d6fd0: cosine 0.134, shared 6-grams 235
        1b302c0b ~ 936239be: cosine 0.132, shared 6-grams 184
        1b302c0b ~ edabe94d: cosine 0.124, shared 6-grams 56
        1b302c0b ~ f544cb12: cosine 0.123, shared 6-grams 69
        1b302c0b ~ 42191a7e: cosine 0.123, shared 6-grams 187
        1b302c0b ~ 86b00a8e: cosine 0.118, shared 6-grams 212
        1b302c0b ~ 54c653aa: cosine 0.114, shared 6-grams 167
0 flagged pair(s)

### python3 simcheck.py batch115 --task 1b302c0b-6031-50de-aa3b-684f5231e338
== instruction: 115 tasks, max cosine 0.080
        13444412 ~ 1b302c0b: cosine 0.080, shared 6-grams 0
        1b302c0b ~ 356c0b72: cosine 0.073, shared 6-grams 0
        1b302c0b ~ 21cb1222: cosine 0.072, shared 6-grams 0
        1b302c0b ~ 99548b6d: cosine 0.070, shared 6-grams 3
        10b66495 ~ 1b302c0b: cosine 0.069, shared 6-grams 0
        1b302c0b ~ 3d42f542: cosine 0.069, shared 6-grams 0
        1b302c0b ~ edabe94d: cosine 0.067, shared 6-grams 0
        1b302c0b ~ f544cb12: cosine 0.064, shared 6-grams 1
== rubric: 115 tasks, max cosine 0.076
        13444412 ~ 1b302c0b: cosine 0.076, shared 6-grams 4
        1b302c0b ~ 54c653aa: cosine 0.063, shared 6-grams 0
        1b302c0b ~ aa42ec41: cosine 0.053, shared 6-grams 4
        1b302c0b ~ 936239be: cosine 0.050, shared 6-grams 0
        1b302c0b ~ 821e7b66: cosine 0.050, shared 6-grams 0
        1b302c0b ~ cba95ebc: cosine 0.050, shared 6-grams 0
        1b302c0b ~ 8fd816e9: cosine 0.049, shared 6-grams 0
        1b302c0b ~ 205f473f: cosine 0.049, shared 6-grams 0
== pytest: 115 tasks, max cosine 0.105
        1b302c0b ~ 356c0b72: cosine 0.105, shared 6-grams 114
        13444412 ~ 1b302c0b: cosine 0.101, shared 6-grams 169
        1b302c0b ~ 87a8a5b1: cosine 0.091, shared 6-grams 239
        1b302c0b ~ 21cb1222: cosine 0.085, shared 6-grams 99
        1b302c0b ~ 936239be: cosine 0.084, shared 6-grams 184
        1b302c0b ~ e41d6fd0: cosine 0.084, shared 6-grams 235
        1b302c0b ~ e2efdf8e: cosine 0.084, shared 6-grams 97
        006f4954 ~ 1b302c0b: cosine 0.082, shared 6-grams 116
0 flagged pair(s)
```
