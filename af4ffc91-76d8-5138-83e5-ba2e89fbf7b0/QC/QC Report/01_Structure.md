## VERDICT: PASS

Task af4ffc91-76d8-5138-83e5-ba2e89fbf7b0 (W08 laytime-demurrage-statement, STATIC). This report covers the FINAL
bundle after round 3 of 2026-11-18 (FIX3_18: a confirming review, then one minimal fix pass). All three passes that day were
grader-only. GATEFIX18 removed the run-wide red-line gate from tests/test_outputs.py and rewrote tests/judge.toml under
the twin rule. FIX2_18 rewrote tests/judge.toml again after an independent review. FIX3_18 rewrote it a third time (20
criteria, positives 26, no penalties) and changed only the reply text in solution/solve.py and solution/TRUTH.md. No tool
call changed. instruction.md, task.toml, data/, world_data/, environment/, tests/test_outputs.py, test_weights.json and
oracle.json were not touched in FIX3_18. I ran
the `qc 2/static/10_structure.md` §1 script (S1-S5) once, as written, on a UUID-named scratch copy of
`harness_mcp_atlas/input/af4ffc91-76d8-5138-83e5-ba2e89fbf7b0`, with `TASK` exported to that copy. The raw output is in
`01_structure_script.txt`, re-run on the final bytes at packaging. The delivered folder `TASKS/18Nov_Tasks/af4ffc91-…`
is the harness build of that input.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | `missing_files: none`, `empty_files: none`, `missing_dirs: none`; world_data_json 15 files; data_files 34; `old_env.json: True`; `helper_modules: none`; `harness_owned_in_tests: none` |
| S1 rubric file | PASS | | `rubric_file: ['tests/judge.toml']` (authoring shape), `both_rubrics: False` |
| S2 parse | PASS | | `parse_errors: none` |
| S3 task.toml | PASS | | `harness_owned_blocks: none`; `schema_version: 1.4`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; mcp_servers 15, apps 8; `apps_not_wired: []`; `wired_without_world: none`; `world_not_wired: none`; category mcp_tool_calling; tags 17; gradeable True |
| S4a weights ↔ tests | PASS | | `weight_shape=flat weighted=20 defined=20 dynamic_minting=False`; weighted_but_undefined none; defined_but_unweighted none; zero/non-numeric none; `positive_total=39 penalty_total=17 guards=5`; `threshold=0.7 null_floor=0.0 guard_polarity=pass_charges gate=None` |
| S4b criteria | PASS | | `shape=authoring criteria=20`; duplicate ids/numbers none; missing_description none; bad_weight none; no_polarity none; sign mismatch none; negate none; non_binary none; bad_target none; `targets: {'final_answer': 20}`; `positive_total=26 penalty_total=0 max_single_positive=5` |
| S4c identity / canary / servers | PASS | | `folder_name_is_uuid: True`; `canary_binding_ok: True` (one instruction canary, this task's); gt_env flat (5 servers); `in_gt_not_world: none`; in_world_not_gt = 10 read-only / red-line context servers (INFO); `old_env_servers: 15 not in world: none` |
| S5 hygiene | PASS | | `find` printed no stray files (solution/__pycache__ from the local oracle replay was removed before the run); no file > 20M; folder 1.1M; no credential match; `slug ok`; no symlinks |

## BLOCKERS
None.

## MAJOR
None.

## MINOR
None.

## Counts
- files: 65  size: 1.1M  data files: 34  world servers: 15  tests: 20 (guards 5)  criteria: 20 (20 positive, 0 penalties)
