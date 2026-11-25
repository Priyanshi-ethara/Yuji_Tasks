## VERDICT: PASS

Script: `qc 2/static/10_structure.md` §1, run as written with `TASK` = a copy of `harness_mcp_atlas/input/1b302c0b-6031-50de-aa3b-684f5231e338`. This is the authoring layout of the final bytes after the gatefix of 2026-11-18 and the fix round 2 of the same day (independent rubric review: decoy penalties whose counterpart pytest grades deleted, the worklist-count split removed, the completion precondition taken off the non-closing tests; task_checksum `dc3f8fd6…483b`). Raw output: `01_structure_script.txt`.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | missing_files none, empty_files none, missing_dirs none. 15 world_data seeds (minimum 2), 34 data files. old_env.json True. helper_modules none. harness_owned_in_tests none. |
| S1 rubric file | PASS | | `['tests/judge.toml']` (authoring shape); both_rubrics False |
| S2 parse | PASS | | parse_errors: none (task.toml, judge.toml, test_weights, oracle, old_env, gt_env, test_outputs.py, solve.py, 15 world seeds) |
| S3 task.toml | PASS | | harness_owned_blocks none; schema_version 1.4; name `atlas/1b302c0b-…`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; 15 mcp_servers, 7 apps; apps_not_wired []; wired_without_world none; world_not_wired none; category mcp_tool_calling; 18 tags; gradeable True |
| S4a weights ↔ tests | PASS | | weighted=20 defined=20 dynamic_minting=False; phantom none; unweighted none; zero/non-numeric none; positive_total=49, penalty_total=15, 5 guards; threshold 0.7, null_floor 0.0, guard_polarity pass_charges, gate=None (all ok) |
| S4b criteria | PASS | | n=20 (authoring shape); duplicate ids/numbers none; missing_description none; bad_weight none; no_polarity none; sign mismatch none; negate none; non-binary none; bad_target none; positive_total=34 penalty_total=0 max_single_positive=5; targets final_answer 20 |
| S4c identity / canary / servers | PASS | | identity uuid = canary = instruction_canary = folder name. One instruction canary, binding ok. gt_env flat with 4 servers (Airtable, Confluence, Salesforce, Zendesk); in_gt_not_world none. old_env has 15 servers, none outside world. |
| S5 hygiene | PASS | | no .DS_Store, __pycache__, *.pyc, swap or node_modules (a solution/__pycache__ left by the kit oracle run was removed before this run; deliver18.sh also prunes it). Size 1.0M, no file > 20M. No credential pattern, slug ok, no symlink. |

## BLOCKERS
- none

## MAJOR
- none

## MINOR
- none

## INFO
- in_world_not_gt: 11 servers (LightDatadog, LightGmail, LightGoogleCalendar, LightIntercom, LightJira, LightNotion, LightOkta, LightPagerDuty, LightSlack, LightStripe, LightTwilio). The oracle only reads them or leaves them alone, as the instruction's read-only scope requires.
- The delivered bundle (`TASKS/18Nov_Tasks/1b302c0b-…`) is the harness build of this folder. In that build, data/ → `environment/light-servers/task_data`, world_data/ → `environment/light-servers/world_data`, and the verifier files (`tests/test.sh`, `reward/`, `claims_lib.py`, `ctrf_pytest_plugin.py`, Dockerfiles) are added by the build. That is why S1 is run on the authoring copy, as §0 prescribes.

## Counts
- files: 66 (authoring copy)  size: 1.0M  data files: 34  world servers: 15  tests: 20 (guards 5)  criteria: 20
