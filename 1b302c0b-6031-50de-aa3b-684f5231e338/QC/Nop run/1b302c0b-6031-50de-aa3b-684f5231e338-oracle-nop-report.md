# Oracle / nop report: 1b302c0b-6031-50de-aa3b-684f5231e338

## VERDICT: PASS (oracle 1.0 > 0.95; nop exactly 0 on pytest, rubric and reward)

- **Run:** `PARALLEL=1 JUDGE=codex caffeinate -i bash qc_oracle_nop.sh TASKS/18Nov_Tasks/1b302c0b-6031-50de-aa3b-684f5231e338`, launched through `_kit/traj/regrade18.sh` (tag f2) on the final task bytes after the grader-only fix recorded in solution/TRUTH.md. ONDIR = `/tmp/qc/oracle_nop_20261119_112242` (durable copy `_kit/traj/qcsave/18/1b302c0b-6031-50de-aa3b-684f5231e338/oracle_nop_20261119_112242`). The raw harbor jobs are copied flat into `Oracle run/` and `Nop run/` (job.log, lock.json, result.json, config.json, the harbor log as oracle.log / nop.log, summary.tsv and the trial directory).
- **Judge:** oracle {ran: True, model: gpt-5.6-sol, transport: codex}; nop {ran: True, model: gpt-5.6-sol, transport: codex}.

| agent | trial | pytest | rubric | reward | guards tripped | exception |
|---|---|---|---|---|---|---|
| oracle | eUzxrA5 | 1.0 | 1.0 | 1.0 | [] | None |
| nop | VEpeMiv | 0.0 | 0.0 | 0.0 | [] | None |

`summary.tsv`:
```
uuid	agent	pytest	rubric	reward	result
1b302c0b-6031-50de-aa3b-684f5231e338	oracle	1.0	1.0	1.0	PASS
1b302c0b-6031-50de-aa3b-684f5231e338	nop	0.0	0.0	0.0	PASS
```

## Checksums
- oracle trial result.json: `dc3f8fd6c51357a209e1196eb18cf96570e0320902ebee063c35706e3ad9483b`
- nop trial result.json: `dc3f8fd6c51357a209e1196eb18cf96570e0320902ebee063c35706e3ad9483b`
- delivered Opus run `1b302c0b-6031-50de-aa3b-684f5231e338-opus-5-20261118-054121-regraded` (trial 7jfiPS7) result.json: `dc3f8fd6c51357a209e1196eb18cf96570e0320902ebee063c35706e3ad9483b`

All three match: the oracle, the nop and the shipped trajectory were graded on the same task bytes.
