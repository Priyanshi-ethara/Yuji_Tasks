## VERDICT: PASS

Structure QC (`qc 2/static/10_structure.md`) on the final bytes of 205f473f-c7e1-5bff-88b5-09e0e89b5356 (U04
crash-owner-routing, hardened to LIVE).

- **What was checked:** a copy of the authoring layout `harness_mcp_atlas/input/205f473f-c7e1-5bff-88b5-09e0e89b5356`.
  The copy folder is named after the UUID, and `TASK` was exported to it.
- **How:** the §1 script (S1-S5) ran once, as written. Its raw output is in `01_structure_script.txt`.
- **Same bytes as the delivery:** the input's `tests/test_outputs.py`, `test_weights.json`, `oracle.json`,
  `old_env.json`, `solution/*` and `instruction.md` are byte-identical to the built task that was delivered.
  `dirhash` of the delivered task is `e0e779d4…f77a`, the same as the run's `task_checksum`.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | `missing_files: none`, `empty_files: none`, `missing_dirs: none`; `world_data_json: 15 files`; `data_files: 43`; `old_env.json: True`; `helper_modules: none`; `harness_owned_in_tests: none` |
| S1 rubric file | PASS | | `rubric_file: ['tests/judge.toml']` (authoring shape), `both_rubrics: False` |
| S2 parse | PASS | | `parse_errors: none` (task.toml, judge.toml, test_weights/oracle/old_env/gt_env JSON, test_outputs.py, solve.py, 15 world_data JSON files) |
| S3 task.toml | PASS | | `harness_owned_blocks: none`; `schema_version: 1.4`; `task.name: atlas/205f473f-…`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; `mcp_servers: 15`, `apps: 7`, `apps_not_wired: []`, `wired_without_world: none`, `world_not_wired: none`; category `mcp_tool_calling`, 17 tags, gradeable True |
| S4a weights ↔ tests | PASS | | `weighted=21 defined=21 dynamic_minting=False`; phantom 0, unweighted 0, zero/non-numeric none; `positive_total=46 penalty_total=17 guards=5`; `threshold=0.7 null_floor=0.0 guard_polarity=pass_charges`; all `_ok: True`, `guards_without_polarity: False` |
| S4b criteria | PASS | | `shape=authoring criteria=22`; duplicate ids/numbers none; no missing description, bad weight, missing polarity, sign mismatch, negate, non-binary scoring or bad target; `positive_total=43 penalty_total=11 max_single_positive=5` (5 < 21.5); `targets: {'final_answer': 22}` |
| S4c identity / canary / servers | PASS | | identity uuid = canary = instruction_canary = `205f473f-…5356`; `folder_name_is_uuid: True`; `canary_binding_ok: True`; `gt_env_shape: flat`, 7 gt servers, `in_gt_not_world: none`; `old_env_servers: 15 not in world: none` |
| S5 hygiene | PASS | | No `.DS_Store`, `__pycache__`, `*.pyc`, swap files, checkpoints or node_modules. Size 1.0M, with no file over 20M. No credential pattern matches, no symlinks, `slug ok`. |

## BLOCKERS
- None.

## MAJOR
- None.

## MINOR
- None.

## INFO
- `in_world_not_gt`: LightDatadog, LightGitlab, LightGmail, LightGoogleDrive, LightJira, LightMicrosoftTeams, LightNotion
  and LightPagerDuty. These are wired, read-only context and decoy servers that the oracle does not write. This is
  expected; the decision table lists it as INFO.
- `harbor_canary_carriers`: .identity.json, environment/Dockerfile, instruction.md, solution/gt_env.json, solution/solve.py,
  solution/solve.sh, task.toml, tests/old_env.json, tests/oracle.json and tests/test_outputs.py.
- The pre-run copy of this check (`_kit/qc/<uuid>/01_structure_script.txt`) ran on a folder named `qc_copy`, so it printed
  `folder_name_is_uuid: False`. This run uses a copy named after the UUID and prints `True`. Every other line is
  unchanged.

## Counts
- files: 75  size: 1.0M  data files: 43  world servers: 15  tests: 21 (guards 5)  criteria: 22
