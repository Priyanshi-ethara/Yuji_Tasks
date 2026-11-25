## VERDICT: PASS

Structure QC (`qc 2/static/10_structure.md`, §1 script run as written) on a copy of the authoring layout of the final
task, `harness_mcp_atlas/input/40ea4665-a13d-5cb8-875b-59bf9f2b1d95` (`export TASK=<copy>`). This is the layout the
delivered build (task_checksum `4b0823a2…0d5e`) was built from. Raw output: `01_structure_script.txt`. It is
byte-identical to the pre-run output: no input file changed after the hardening pass.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | `missing_files: none`, `empty_files: none`, `missing_dirs: none`; `data_files: 34`; `old_env.json: True`; `helper_modules: none`; `harness_owned_in_tests: none` |
| S1 rubric file | PASS | | `rubric_file: ['tests/judge.toml']`, `both_rubrics: False` (authoring shape) |
| S2 parse | PASS | | `parse_errors: none` (task.toml, judge.toml, test_weights/oracle/old_env/gt_env JSON, test_outputs.py, solve.py, 16 world_data files) |
| S3 task.toml | PASS | | `harness_owned_blocks: none`; `schema_version: 1.4`; `task.name: atlas/40ea4665-…`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; `mcp_servers: 16`, `apps: 8`; `apps_not_wired: []`; `wired_without_world: none`; `world_not_wired: none`; category `mcp_tool_calling`; 18 tags; gradeable True |
| S4a weights ↔ tests | PASS | | `weight_shape=flat weighted=22 defined=22 dynamic_minting=False`; phantom 0, unweighted 0, zero/non-numeric 0; `positive_total=42 penalty_total=18 guards=6`; `threshold=0.7 null_floor=0.0 guard_polarity=pass_charges`; all `_ok` True |
| S4b criteria | PASS | | `shape=authoring criteria=25`; dup ids/numbers none; missing description none; bad weight none; polarity none; sign mismatch none; negate none; non-binary none; bad target none; `positive_total=46 penalty_total=17 max_single_positive=5`; targets `{'final_answer': 25}` |
| S4c identity / canary / servers | PASS | | `folder_name_is_uuid: True`; `canary_binding_ok: True` (one canary, `40ea4665-…`); gt_env flat, 9 servers; `in_gt_not_world: none`; `in_world_not_gt` = 7 decoy servers (INFO); `old_env_servers: 16 not in world: none` |
| S5 hygiene | PASS | | no .DS_Store / __pycache__ / *.pyc / swap files printed; no file > 20M; 3.3M total; secret grep empty; `slug ok`; no symlinks |

## BLOCKERS
- None.

## MAJOR
- None.

## MINOR
- None.

## INFO
- `in_world_not_gt`: LightDatadog, LightGmail, LightGoogleCalendar, LightJira, LightSlack, LightStripe, LightXero.
  These are wired decoy or read-only servers that the oracle never writes. This is expected.

## Counts
- files: 68  size: 3.3M  data files: 34  world servers: 16  tests: 22 (guards 6)  criteria: 25
