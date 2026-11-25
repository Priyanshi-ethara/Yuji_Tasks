## VERDICT: PASS

Task c9ebfbd9-7b5c-509d-bf31-c6789ca5bc0c (T03 coldchain-mkt-release).

**How the script was run.** I extracted the `qc 2/static/10_structure.md` §1 script verbatim from the doc. It is
byte-identical (`cmp`) to the copy used earlier. I ran it unchanged on 2026-11-12 at about 15:35 IST, with `TASK` set to a
fresh scratch copy of `harness_mcp_atlas/input/c9ebfbd9-…`, taken after grader fix 2 and after the final harbor runs. That
folder is the authoring-layout source of the delivered bundle. Raw output is in `01_structure_script.txt`. It matches the
earlier run except for the `du -sh` line: 1.1M now against 1.0M before, because this copy includes the six patched servers
under `environment/light-servers/software`.

**The source matches the delivered bundle.** Against `30_tasks/c9ebfbd9-…`:
- These files are byte-identical (`cmp`): `instruction.md`, `tests/test_outputs.py`, `tests/test_weights.json`,
  `tests/oracle.json`, `tests/old_env.json`, `solution/solve.py`, `solution/solve.sh`, `solution/gt_env.json` and
  `solution/TRUTH.md`.
- `diff -rq` is empty for `data/` against `environment/light-servers/task_data/`, and for `world_data/` against
  `environment/light-servers/world_data/`.
- `environment/Dockerfile` and the six patched server files are byte-identical to their built copies.
- `task.toml` differs only by the harness-owned blocks the build adds (`[agent]`, `[verifier]`, `[environment]`, artifacts).

| Check | Result | Code | Evidence |
|---|---|---|---|
| S1 required files/dirs | PASS | | `missing_files: none`, `empty_files: none`, `missing_dirs: none`; `data_files: 35`; `world_data_json: 16 files`; `old_env.json: True`; `helper_modules: none`; `harness_owned_in_tests: none` |
| S1 rubric file | PASS | | `rubric_file: ['tests/judge.toml']`, `both_rubrics: False` (authoring shape) |
| S2 parse | PASS | | `parse_errors: none` |
| S3 task.toml | PASS | | `harness_owned_blocks: none`; `schema_version: 1.4`; `task.name: atlas/c9ebfbd9-7b5c-509d-bf31-c6789ca5bc0c`; description present; authors `[{'name': 'Priyanshi Joshi', 'email': 'priyanshi.joshi@ethara.ai'}]`; `metadata.mcp_servers: 16`, `metadata.apps: 8`, `apps_not_wired: []`, `wired_without_world: none`, `world_not_wired: none`; category `mcp_tool_calling`; 16 tags; `gradeable: True` |
| S4a weights ↔ tests | PASS | | `weight_shape=flat weighted=30 defined=30 dynamic_minting=False`; phantom 0 (`weighted_but_undefined: none`); unweighted 0 (`defined_but_unweighted: none`); `zero_or_nonnumeric_weights: none`; `positive_total=58 penalty_total=14 guards=4`; `threshold=0.7 null_floor=0.0 guard_polarity=pass_charges gate=None`; threshold_ok / null_floor_ok / guard_polarity_ok all True; `guards_without_polarity: False` |
| S4b criteria | PASS | | `shape=authoring criteria=26`; duplicate ids/numbers none; missing_description, bad_weight, no_polarity, weight_sign_vs_polarity_mismatch, negate_used, non_binary_scoring, bad_target all none; `positive_total=54 penalty_total=8 max_single_positive=5`; `targets: {'final_answer': 26}` |
| S4c identity / canary / servers | PASS | | identity uuid = canary = instruction_canary = `c9ebfbd9-7b5c-509d-bf31-c6789ca5bc0c`; `folder_name_is_uuid: True`; `instruction_canaries_found` is this UUID only; `canary_binding_ok: True`; `gt_env_shape: flat` over 9 servers; `in_gt_not_world: none`; `old_env_servers: 16 not in world: none` |
| S5 hygiene | PASS | | The stray-file find printed nothing. `du -sh` is 1.1M, and no file is over 20M. The secret grep printed nothing. `slug ok`. The symlink find printed nothing. |

## BLOCKERS
- none

## MAJOR
- none

## MINOR
- none

## INFO
- `in_world_not_gt`: LightDatadog, LightFedEx, LightMicrosoftTeams, LightPagerDuty, LightSalesforce, LightServiceNow,
  LightZendesk. The prompt makes every system read-only except the round's cards, the QAD deviations, the one Slack
  message and the CSV. These servers are wired as read-only or decoy surfaces, and the oracle leaves them unchanged, so
  this is expected.
- `harbor_canary_carriers`: 11 files carry the task canary, as the build stamps it: `.identity.json`,
  `environment/Dockerfile`, `instruction.md`, `solution/gt_env.json`, `solution/solve.py`, `solution/solve.sh`,
  `task.toml`, `tests/judge.toml`, `tests/old_env.json`, `tests/oracle.json` and `tests/test_outputs.py`.

## Counts
- files: 70 · size: 1.1M · data files: 35 · world servers: 16 · tests: 30 (4 guards) · criteria: 26
