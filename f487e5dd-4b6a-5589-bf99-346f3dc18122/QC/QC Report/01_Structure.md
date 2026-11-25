## VERDICT: PASS

Task f487e5dd-4b6a-5589-bf99-346f3dc18122 (T49 pv-string-design-review, slot 6). I ran the §1 script of `qc 2/static/10_structure.md` unchanged on a scratch copy of `$H/input/f487e5dd-4b6a-5589-bf99-346f3dc18122`, which is the authoring-layout source of this bundle. The copy was taken after the one task.toml wording fix (see 02_Ruthless.md). Raw output: `01_structure_script.txt`.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | missing_files none; empty_files none; missing_dirs none; world_data_json 15 files; data_files 35; old_env.json True; helper_modules none |
| S1 rubric file | PASS | | `['tests/judge.toml']` (authoring shape); both_rubrics False |
| S2 parse | PASS | | parse_errors: none |
| S3 task.toml | PASS | | harness_owned_blocks none; schema_version 1.4; task.name atlas/f487e5dd-…; description present; authors Priyanshi Joshi <priyanshi.joshi@ethara.ai>; mcp_servers 15, apps 7; apps_not_wired []; wired_without_world none; world_not_wired none; category mcp_tool_calling; tags 13; gradeable True |
| S4a weights ↔ tests | PASS | | weighted=26 defined=26 phantom=0 unweighted=0; no zero/non-numeric weights; positive_total=50 penalty_total=18 guards=6; threshold 0.7, null_floor 0.0, guard_polarity pass_charges |
| S4b criteria | PASS | | n=24; dups 0; numbers 0; missing_description none; bad_weight none; polarity ok; negate none; all binary; targets {final_answer: 24}; positive_total=42 penalty_total=8 max_single_positive=5 (≤ 21) |
| S4c identity / canary / servers | PASS | | identity uuid = canary = instruction_canary = f487e5dd-…; folder_name_is_uuid True; canary_binding_ok True; in_gt_not_world none; old_env 15 servers, none outside world |
| S5 hygiene | PASS | | no stray files (no .DS_Store, __pycache__ or .pyc); size 1.1M; no file > 20M; no secret pattern hit; slug ok; no symlinks |

## BLOCKERS
None.

## MAJOR
None.

## MINOR
None.

INFO (decision table, not a defect): in_world_not_gt lists 8 servers (Gmail, GoogleMaps, OpenWeather, Outlook, QuickBooks, Shippo, Slack, Weather). Those are look-only servers that the oracle never writes.

## Counts
- files: task copy 1.1M; data files: 35; world servers: 15; tests: 26 (guards 6); criteria: 24
