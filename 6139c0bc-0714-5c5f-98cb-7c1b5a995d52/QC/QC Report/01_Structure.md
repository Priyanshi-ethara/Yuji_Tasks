## VERDICT: PASS

Task 6139c0bc-0714-5c5f-98cb-7c1b5a995d52 (T02 scope2-carbon-inventory). I ran the `qc 2/static/10_structure.md` §1 script exactly as written, extracting it verbatim from the doc. It ran with `TASK` set to a scratch copy of `harness_mcp_atlas/input/6139c0bc-…` taken on 2026-11-12 after grader fix 2. That folder is the authoring-layout source of the final delivered bundle. Against `30_tasks/6139c0bc-…`, these are byte-identical (`cmp`): `instruction.md`, `tests/test_outputs.py`, `tests/test_weights.json`, `tests/oracle.json`, `tests/old_env.json`, `solution/solve.py`, `solution/gt_env.json` and `solution/TRUTH.md`. `diff -rq` is also empty for `data/` against `environment/light-servers/task_data/` and for `world_data/` against `environment/light-servers/world_data/`. `task.toml` differs only because the build adds the harness-owned blocks. Raw output is in `01_structure_script.txt`, and it is unchanged from the run before the rebuild.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | `missing_files: none`, `empty_files: none`, `missing_dirs: none`; `data_files: 35`; `world_data_json: 16 files`; `old_env.json: True`; `helper_modules: none`; `harness_owned_in_tests: none` |
| S1 rubric file | PASS | | `rubric_file: ['tests/judge.toml']`, `both_rubrics: False` (authoring shape) |
| S2 parse | PASS | | `parse_errors: none` |
| S3 task.toml | PASS | | `harness_owned_blocks: none`; `schema_version: 1.4`; `task.name: atlas/6139c0bc-0714-5c5f-98cb-7c1b5a995d52`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; `metadata.mcp_servers: 16`, `metadata.apps: 7`, `apps_not_wired: []`, `wired_without_world: none`, `world_not_wired: none`; category `mcp_tool_calling`; 16 tags; `gradeable: True` |
| S4a weights ↔ tests | PASS | | `weight_shape=flat weighted=35 defined=35 dynamic_minting=False`; phantom 0 (`weighted_but_undefined: none`); unweighted 0 (`defined_but_unweighted: none`); `zero_or_nonnumeric_weights: none`; `positive_total=84 penalty_total=17 guards=5`; `threshold=0.7 null_floor=0.0 guard_polarity=pass_charges gate=None`; threshold_ok / null_floor_ok / guard_polarity_ok all True |
| S4b criteria | PASS | | `shape=authoring criteria=31`; duplicate ids/numbers none; missing_description, bad_weight, no_polarity, weight_sign_vs_polarity_mismatch, negate_used, non_binary_scoring, bad_target all none; `positive_total=60 penalty_total=7 max_single_positive=5`; `targets: {'final_answer': 31}` |
| S4c identity / canary / servers | PASS | | identity uuid = canary = instruction_canary = `6139c0bc-0714-5c5f-98cb-7c1b5a995d52`; `folder_name_is_uuid: True`; `instruction_canaries_found` is this UUID only; `canary_binding_ok: True`; `gt_env_shape: flat` over 7 servers; `in_gt_not_world: none`; `old_env_servers: 16 not in world: none` |
| S5 hygiene | PASS | | The stray-file find printed nothing. `du -sh`: 1.2M, and no file is over 20M. The secret grep printed nothing. `slug ok`. The symlink find printed nothing. |

## BLOCKERS
- none

## MAJOR
- none

## MINOR
- none

## INFO
- `in_world_not_gt`: LightDocuSign, LightGoogleCalendar, LightJira, LightMicrosoftTeams, LightNotion, LightServiceNow,
  LightSlack, LightTrello, LightXero. The prompt forbids writes on these servers and the oracle leaves them
  unchanged; they are wired as read-only and decoy servers, so this is expected.
- `harbor_canary_carriers`: 12 files carry the task canary, as the build stamps it (identity, Dockerfile,
  instruction, solution, tests, task.toml).

## Counts
- files: 70  size: 1.2M  data files: 35  world servers: 16  tests: 35 (guards 5)  criteria: 31
