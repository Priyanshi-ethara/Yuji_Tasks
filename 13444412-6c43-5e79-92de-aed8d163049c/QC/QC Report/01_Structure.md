## VERDICT: PASS

Task 13444412-6c43-5e79-92de-aed8d163049c (U05 plan-change-intents, hardened to LIVE). The `qc 2/static/10_structure.md`
§1 script (S1-S5) was run once, as written, on a copy of the final authoring bundle
`harness_mcp_atlas/input/13444412-6c43-5e79-92de-aed8d163049c`, with `TASK` exported to that copy. The copy was taken
after the QC_FINAL16 grader-only rubric fix (r-refund-routed wording and the five penalty carve-outs; see 02_Ruthless).
Raw output: `01_structure_script.txt`. The output is identical to the pre-fix run apart from the scratch path printed
by `du`. The fix touched only judge.toml text and TRUTH.md, which this script does not count.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | `missing_files : none`, `empty_files : none`, `missing_dirs : none`; `world_data_json : 15 files (minimum 2)`; `data_files : 32`; `old_env.json : True`; `helper_modules : none`; `harness_owned_in_tests: none` |
| S1 rubric file | PASS | | `rubric_file : ['tests/judge.toml']`, `both_rubrics : False` (authoring shape) |
| S2 parse | PASS | | `parse_errors: none` (task.toml, judge.toml, test_weights/oracle/old_env/gt_env JSON, test_outputs.py, solve.py, 15 world_data seeds) |
| S3 task.toml | PASS | | `harness_owned_blocks: none`; `schema_version : 1.4`; `task.name : atlas/13444412-6c43-5e79-92de-aed8d163049c`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; `mcp_servers: 15`, `apps: 6`, `apps_not_wired: []`, `wired_without_world : none`, `world_not_wired : none`; category `mcp_tool_calling`; 16 tags; gradeable True |
| S4a weights ↔ tests | PASS | | `weighted=23 defined=23 dynamic_minting=False`; phantom 0 (`weighted_but_undefined: none`); unweighted 0; `zero_or_nonnumeric_weights: none`; `positive_total=47 penalty_total=14 guards=4`; `threshold=0.7 null_floor=0.0 guard_polarity=pass_charges gate=None`; all `_ok: True` |
| S4b criteria | PASS | | `shape=authoring criteria=25`; duplicate ids/numbers none; missing description none; bad weight none; no polarity none; sign mismatch none; negate none; non-binary none; bad target none; `positive_total=42 penalty_total=11 max_single_positive=5`; `targets: {'final_answer': 25}` |
| S4c identity / canary / servers | PASS | | uuid = canary = instruction_canary = `13444412-6c43-5e79-92de-aed8d163049c`; `folder_name_is_uuid: True`; `canary_binding_ok: True`; 12 harbor-canary carriers; `gt_env_shape : flat`, 7 gt servers, `in_gt_not_world : none`; `old_env_servers : 15 not in world: none`; `in_world_not_gt` = Gmail, GoogleCalendar, GoogleDrive, Jira, Mailchimp, QuickBooks, Salesforce, Slack (INFO: read-only context servers the oracle never writes) |
| S5 hygiene | PASS | | no .DS_Store / __pycache__ / *.pyc / swap / node_modules printed; `du` 1.1M; no file > 20M; credential grep empty; `slug ok`; no symlinks |

## BLOCKERS
- none

## MAJOR
- none

## MINOR
- none

## Counts
- files: 63  size: 1.1M  data files: 32  world servers: 15  tests: 23 (guards 4)  criteria: 25 (20 positive, 5 penalties)
