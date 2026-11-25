## VERDICT: PASS

Task a6901ded-0579-5c2d-8ae3-a0649c5c5ff2 (card U15, finetune-launch-readiness, hardened to a live card).

How the check was run:
- The `qc 2/static/10_structure.md` §1 script was run exactly as written.
- `TASK` was a fresh copy of `harness_mcp_atlas/input/a6901ded-0579-5c2d-8ae3-a0649c5c5ff2`, the final authoring bytes.
- That input is identical to the delivered bundle in every file compared: tests/test_outputs.py, world_data, data, solution.
- The built bundle and the bytes that the Opus run and the oracle/nop runs used carry the same task_checksum, 5f56d8e467890f42a5f676a0fadbd3e7f68ae7df3af2dce5685a7bf0656cb1de.
- Raw output: `01_structure_script.txt`, in this folder.

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | missing_files none; empty_files none; missing_dirs none. world_data_json 15 files; data_files 35; old_env.json True. harness_owned_in_tests none; helper_modules none |
| S1 rubric file | PASS | | `['tests/judge.toml']` (authoring shape); both_rubrics False |
| S2 parse | PASS | | parse_errors: none |
| S3 task.toml | PASS | | harness_owned_blocks none; schema_version 1.4; task.name atlas/a6901ded-…; description present. authors [Priyanshi Joshi <priyanshi.joshi@ethara.ai>]. mcp_servers 15, apps 9; apps_not_wired []; wired_without_world none; world_not_wired none. category mcp_tool_calling; tags 18; gradeable True |
| S4a weights ↔ tests | PASS | | weight_shape=flat, weighted=20, defined=20, dynamic_minting=False. Phantom tests none; unweighted none; zero or non-numeric weights none. positive_total=34, penalty_total=18, guards=6. threshold=0.7, null_floor=0.0, guard_polarity=pass_charges |
| S4b criteria | PASS | | shape=authoring, criteria=24. Duplicate ids or numbers: none. missing_description, bad_weight, no_polarity, sign mismatch, negate, non_binary and bad_target: none. positive_total=42, penalty_total=6, max_single_positive=5 (≤ 21). targets {final_answer: 24} |
| S4c identity / canary / servers | PASS | | identity uuid = canary = instruction_canary = a6901ded-…; folder_name_is_uuid True; instruction_canaries_found [a6901ded-…]; canary_binding_ok True. gt_env is flat over 10 servers; in_gt_not_world none. old_env has 15 servers, none outside world |
| S5 hygiene | PASS | | No stray-file lines (.DS_Store, __pycache__, pyc, swp, checkpoints, node_modules). No file over 20M; no secret match; no symlink. Size 1.0M; slug ok |

## BLOCKERS
- none

## MAJOR
- none

## MINOR
- none

INFO:
- in_world_not_gt lists LightGoogleDrive, LightOkta, LightServiceNow, LightSlack and LightTrello. These are background servers that the oracle reads but never writes, which is expected.
- harbor_canary_carriers lists 12 files, all bound to this task's own uuid.

## Counts
- files: 67
- size: 1.0M
- data files: 35
- world servers: 15
- tests: 20 (6 guards)
- criteria: 24 (20 positive, 4 penalties)
