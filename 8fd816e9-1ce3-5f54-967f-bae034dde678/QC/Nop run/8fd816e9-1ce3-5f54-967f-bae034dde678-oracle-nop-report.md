# Harbor nop run: 8fd816e9-1ce3-5f54-967f-bae034dde678

## VERDICT: PASS: nop exactly 0 on pytest, rubric and reward, with no guard charged

The source is `/tmp/qc/oracle_nop_20261116_170046/8fd816e9-1ce3-5f54-967f-bae034dde678/nop`, run by `qc_oracle_nop.sh` (JUDGE=codex) on the final delivered bytes, the same bytes the
Opus run used. This folder holds the full raw job copied flat: the trial dir `8fd816e9-1ce3-5f54-967f-bae034dd__gcUxiFT`,
job.log, lock.json, result.json and config.json. It also holds nop.log (the harbor log), reward.json (the trial
verifier's), summary.tsv and summary.txt.

| Check | Result | Evidence |
|---|---|---|
| summary.tsv row | ok | `8fd816e9-1ce3-5f54-967f-bae034dde678 nop 0.0 0.0 0.0 PASS` |
| reward.json | ok | {"pytest": 0.0, "rubric": 0.0, "reward": 0.0} |
| oracle > 0.95 / nop exactly 0 | PASS | Both come from the same ONDIR: oracle 1.0/1.0/1.0, nop 0.0/0.0/0.0 |
| judge gpt-5.6-sol via codex ran | PASS | judge.json: {'ran': True, 'model': 'gpt-5.6-sol', 'transport': 'codex', 'reason': None} |
| task_checksum matches the delivered Opus run | PASS | task_checksum `84b922da…df3c` is the same here, in trajectories/opus-5/run_1/result.json and in jobs.json (job `…-opus-5-20261116-113443`) |
| run healthy | PASS | verifier_environment_mode: separate, exception_info: None |
| ledger | PASS | grade_report: earned 0.0, penalty 0.0, total_positive 49, guards_tripped [], 19 missed (every positive) |
| rubric | PASS | rubric 0.0: 0 of 25 judged yes, and no penalty was judged yes |
