# Structure QC: 6f161651-3192-5a25-8109-ffb0d8b6f198 (U10 submission-toc-versions, LIVE)

I ran `qc 2/static/10_structure.md` §1 as written on a copy of the final authoring source,
`harness_mcp_atlas/input/6f161651-3192-5a25-8109-ffb0d8b6f198`, with `TASK=<scratch copy>`. The copy was taken after the
grader-only judge.toml fixes (02_Ruthless, Fixed 7 and 8). The raw output is in `01_structure_script.txt` next to this
report.

## VERDICT: PASS

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | missing_files none, empty_files none, missing_dirs none. world_data_json 15 files (minimum 2). data_files 36. old_env.json True. helper_modules none. harness_owned_in_tests none. |
| S1 rubric file | PASS | | `['tests/judge.toml']` (authoring shape); both_rubrics False |
| S2 parse | PASS | | parse_errors: none (task.toml, judge.toml, test_weights, oracle, old_env, gt_env, test_outputs.py, solve.py, 15 world_data seeds) |
| S3 task.toml | PASS | | harness_owned_blocks none. schema_version 1.4. task.name `atlas/6f161651-…`. description present. authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`. mcp_servers 15, apps 9, apps_not_wired []. wired_without_world none, world_not_wired none. category mcp_tool_calling, tags 16, gradeable True. |
| S4a weights ↔ tests | PASS | | weight_shape=flat weighted=26 defined=26 dynamic_minting=False; phantom none, unweighted none, zero_or_nonnumeric none; positive_total=59 penalty_total=17 guards=5; threshold=0.7 null_floor=0.0 guard_polarity=pass_charges gate=None; all *_ok True, guards_without_polarity False |
| S4b criteria | PASS | | shape=authoring criteria=22. duplicate_ids, duplicate_numbers, missing_description, bad_weight, no_polarity, sign mismatch, negate, non_binary and bad_target are all none. positive_total=47 penalty_total=7 max_single_positive=5. targets {'final_answer': 22}. |
| S4c identity / canary / servers | PASS | | The identity uuid, canary and instruction_canary all equal the folder name. folder_name_is_uuid True. One instruction canary was found. canary_binding_ok True. gt_env flat with 9 servers. in_gt_not_world none. old_env_servers 15, none missing from world. |
| S5 hygiene | PASS | | No .DS_Store, __pycache__, .pyc, swap files, checkpoints or node_modules. No file over 20M (folder 1.3M). The secret grep is empty. `slug ok`. No symlinks. |

## BLOCKERS
- None.

## MAJOR
- None.

## MINOR
- None.

## INFO
- `in_world_not_gt`: LightDropbox, LightGmail, LightGoogleCalendar, LightGoogleDrive, LightMicrosoftTeams, LightSlack.
  These are read-only or decoy servers that the oracle never writes, so they are absent from gt_env. This is expected.
- `harbor_canary_carriers` lists 12 files. The harbor canary GUID equals the task UUID, so every file that names the
  task carries it. This is informational only.
- `helper_modules`: none. There is no tests/task_lib.py. The built bundle's tests/ holds only the harness-owned
  claims_lib.py, ctrf_pytest_plugin.py, test.sh, Dockerfile(s) and reward/.

## Counts
- files: authoring source 1.3M; data files: 36; world servers: 15; tests: 26 (guards 5); criteria: 22 (19 positive, 3 penalties)
