# Structure QC: 8fd816e9-1ce3-5f54-967f-bae034dde678 (U13 slo-dashboard-attainment, hardened to LIVE)

I ran `qc 2/static/10_structure.md` §1 as written, with `TASK` set to a scratch copy of the final authoring source,
`harness_mcp_atlas/input/8fd816e9-1ce3-5f54-967f-bae034dde678`. The raw output is in `01_structure_script.txt` next to
this report.

- **Source is unchanged since the pre-run review.** No file in input/ is newer than 02_Ruthless.md (16:31). The newest
  file is tests/oracle.json (16:30:16).
- **Output matches the pre-run review.** The output agrees line for line with the pre-run `01_structure_script.txt`,
  apart from the scratch path in the `du` line.
- **The delivered task is the built form of the same source.** The task part of the delivered bundle (everything except
  trajectories/ and QC/) is byte-identical to `out/build/<uuid>` and `out/packaged/<uuid>`. Its `dirhash(sha256)` is
  `84b922da…df3c`, which is the run's task_checksum.

## VERDICT: PASS

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | missing_files none, empty_files none, missing_dirs none. world_data_json has 15 files (minimum 2). data_files 35. old_env.json True. helper_modules none. harness_owned_in_tests none. |
| S1 rubric file | PASS | | `['tests/judge.toml']` (authoring shape). both_rubrics False. |
| S2 parse | PASS | | parse_errors: none. Checked: task.toml, judge.toml, test_weights, oracle, old_env, gt_env, test_outputs.py, solve.py and the 15 world_data seeds. |
| S3 task.toml | PASS | | harness_owned_blocks none. schema_version 1.4. task.name `atlas/8fd816e9-…`. description present. authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`. mcp_servers 15, apps 6, apps_not_wired []. wired_without_world none, world_not_wired none. category mcp_tool_calling, tags 17, gradeable True. |
| S4a weights ↔ tests | PASS | | weight_shape=flat, weighted=24, defined=24, dynamic_minting=False. Phantom none, unweighted none, zero_or_nonnumeric none. positive_total=49, penalty_total=17, guards=5. threshold=0.7, null_floor=0.0, guard_polarity=pass_charges, gate=None. All *_ok True; guards_without_polarity False. |
| S4b criteria | PASS | | shape=authoring, criteria=25. None of these fire: duplicate_ids, duplicate_numbers, missing_description, bad_weight, no_polarity, sign mismatch, negate, non_binary, bad_target. positive_total=46, penalty_total=11, max_single_positive=5. targets {'final_answer': 25}. |
| S4c identity / canary / servers | PASS | | Identity uuid, canary and instruction_canary all equal the folder name. folder_name_is_uuid True. One instruction canary found; canary_binding_ok True. gt_env flat, 5 servers. in_gt_not_world none. old_env_servers 15, none missing from world. |
| S5 hygiene | PASS | | No .DS_Store, __pycache__, .pyc, swap files, checkpoints or node_modules. No file over 20M (folder 956K). The secret grep is empty. `slug ok`. No symlinks. |

## BLOCKERS
- None.

## MAJOR
- None.

## MINOR
- None.

## INFO
- `in_world_not_gt` lists 10 servers: LightBox, LightGmail, LightGoogleCalendar, LightGoogleDrive, LightJira, LightOkta,
  LightSentry, LightServiceNow, LightSlack and LightWordPress. The oracle never writes these read-only and decoy
  servers, so they are absent from gt_env. This is expected.
- `harbor_canary_carriers` lists 11 files. The harbor canary GUID equals the task UUID, so every file that names the
  task carries it. This is informational only.
- `helper_modules`: none. There is no tests/task_lib.py. The built bundle's tests/ holds only the harness-owned
  claims_lib.py, ctrf_pytest_plugin.py, test.sh, the Dockerfiles and reward/.

## Counts
- files: 66 in the authoring source (956K)
- data files: 35
- world servers: 15
- tests: 24 (5 guards)
- criteria: 25 (22 positive, 3 penalties)
