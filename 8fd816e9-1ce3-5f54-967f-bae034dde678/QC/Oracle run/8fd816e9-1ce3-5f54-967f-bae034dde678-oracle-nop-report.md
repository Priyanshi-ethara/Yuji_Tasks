# Harbor oracle run: 8fd816e9-1ce3-5f54-967f-bae034dde678

## VERDICT: PASS: oracle 1.0 on pytest, rubric and reward (above the 0.95 bar)

The source is `/tmp/qc/oracle_nop_20261116_170046/8fd816e9-1ce3-5f54-967f-bae034dde678/oracle`, run by `qc_oracle_nop.sh` (JUDGE=codex) on the final delivered bytes, the same bytes
the Opus run used. This folder holds the full raw job copied flat: the trial dir `8fd816e9-1ce3-5f54-967f-bae034dd__RSc9JsT`,
job.log, lock.json, result.json and config.json. It also holds oracle.log (the harbor log), reward.json (the trial
verifier's), summary.tsv and summary.txt.

| Check | Result | Evidence |
|---|---|---|
| summary.tsv row | ok | `8fd816e9-1ce3-5f54-967f-bae034dde678 oracle 1.0 1.0 1.0 PASS` |
| reward.json | ok | {"pytest": 1.0, "rubric": 1.0, "reward": 1.0} |
| oracle > 0.95 / nop exactly 0 | PASS | Both come from the same ONDIR: oracle 1.0/1.0/1.0, nop 0.0/0.0/0.0 |
| judge gpt-5.6-sol via codex ran | PASS | judge.json: {'ran': True, 'model': 'gpt-5.6-sol', 'transport': 'codex', 'reason': None} |
| task_checksum matches the delivered Opus run | PASS | task_checksum `84b922da…df3c` is the same here, in trajectories/opus-5/run_1/result.json and in jobs.json (job `…-opus-5-20261116-113443`). It equals `dirhash(sha256)` of the delivered task folder. |
| run healthy | PASS | verifier_environment_mode: separate, exception_info: None |
| ledger | PASS | grade_report: earned 49.0, penalty 0.0, total_positive 49, guards_tripped [], 0 missed |
| rubric | PASS | rubric 1.0: 22 of 25 criteria judged yes (all 22 positives). The 3 penalties (p-six-of-twenty, p-five-of-twenty, p-tier3-old-target) were judged no. |
| live event reached | PASS | The oracle re-opens RS-2 after its register rows (`get_content 410002` returns version 7 with "Tier 3 99.60 %" and "Corrigenda C1 (2026-11-03, reliability review)"). It reads `list_comments 410002` (comment 510006) and then creates "SLO attainment — October 2026 — 8 of 20 objectives missed". |
