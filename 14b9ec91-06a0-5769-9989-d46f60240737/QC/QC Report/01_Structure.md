## VERDICT: PASS

Task 14b9ec91-06a0-5769-9989-d46f60240737 (U11, LIVE). The `qc 2/static/10_structure.md` §1 script (S1-S5) was run once,
as written, on a copy of the final authoring bundle `harness_mcp_atlas/input/14b9ec91-06a0-5769-9989-d46f60240737`
(after the rg1 grader-only rubric fix), with `TASK` exported to that copy. Raw output: `01_structure_script.txt`.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | `missing_files : none`, `empty_files : none`, `missing_dirs : none`; `world_data_json : 15 files (minimum 2)`; `data_files : 34`; `old_env.json : True`; `helper_modules : none`; `harness_owned_in_tests: none` |
| S1 rubric file | PASS | | `rubric_file : ['tests/judge.toml']`, `both_rubrics : False` (authoring shape) |
| S2 parse | PASS | | `parse_errors: none` (task.toml, judge.toml, test_weights/oracle/old_env/gt_env JSON, test_outputs.py, solve.py, 15 world_data seeds) |
| S3 task.toml | PASS | | `harness_owned_blocks: none`; `schema_version : 1.4`; `task.name : atlas/14b9ec91-06a0-5769-9989-d46f60240737`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; `mcp_servers: 15`, `apps: 5`, `apps_not_wired: []`, `wired_without_world : none`, `world_not_wired : none`; category `mcp_tool_calling`; 16 tags; gradeable True |
| S4a weights ↔ tests | PASS | | `weighted=23 defined=23 dynamic_minting=False`; phantom 0 (`weighted_but_undefined: none`); unweighted 0; `zero_or_nonnumeric_weights: none`; `positive_total=52 penalty_total=17 guards=5`; `threshold=0.7 null_floor=0.0 guard_polarity=pass_charges gate=None`; all `_ok: True` |
| S4b criteria | PASS | | `shape=authoring criteria=23`; duplicate ids/numbers none; missing description none; bad weight none; no polarity none; sign mismatch none; negate none; non-binary none; bad target none; `positive_total=52 penalty_total=11 max_single_positive=5`; `targets: {'final_answer': 23}` |
| S4c identity / canary / servers | PASS | | uuid = canary = instruction_canary = `14b9ec91-06a0-5769-9989-d46f60240737`; `folder_name_is_uuid: True`; `canary_binding_ok: True`; `gt_env_shape : flat`, 9 gt servers, `in_gt_not_world : none`; `old_env_servers : 15 not in world: none`; `in_world_not_gt` = Box, GoogleCalendar, GoogleMaps, Jira, Notion, Trello (INFO: read-only context servers the oracle never writes) |
| S5 hygiene | PASS | | no .DS_Store / __pycache__ / *.pyc / swap / node_modules printed; `du` 1.0M; no file > 20M; credential grep empty; `slug ok`; no symlinks |

## BLOCKERS
- none

## MAJOR
- none

## MINOR
- none

## Counts
- files: 67  size: 1.0M  data files: 34  world servers: 15  tests: 23 (guards 5)  criteria: 23 (20 positive, 3 penalties)
