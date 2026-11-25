# Oracle / nop report: af4ffc91-76d8-5138-83e5-ba2e89fbf7b0

## VERDICT: PASS (oracle 1.0 > 0.95; nop exactly 0 on pytest, rubric and reward)

- **Run:** `PARALLEL=1 JUDGE=codex caffeinate -i bash qc_oracle_nop.sh TASKS/18Nov_Tasks/af4ffc91-76d8-5138-83e5-ba2e89fbf7b0`, launched through `_kit/traj/regrade18.sh` (tag f3) on the final task bytes after the grader-only fix recorded in solution/TRUTH.md. ONDIR = `/tmp/qc/oracle_nop_20261119_112548` (durable copy `_kit/traj/qcsave/18/af4ffc91-76d8-5138-83e5-ba2e89fbf7b0/oracle_nop_20261119_112548`). The raw harbor jobs are copied flat into `Oracle run/` and `Nop run/` (job.log, lock.json, result.json, config.json, the harbor log as oracle.log / nop.log, summary.tsv and the trial directory).
- **Judge:** oracle {ran: True, model: gpt-5.6-sol, transport: codex}; nop {ran: True, model: gpt-5.6-sol, transport: codex}.

| agent | trial | pytest | rubric | reward | guards tripped | exception |
|---|---|---|---|---|---|---|
| oracle | DrPJZaD | 1.0 | 1.0 | 1.0 | [] | None |
| nop | Qfte3Yw | 0.0 | 0.0 | 0.0 | [] | None |

`summary.tsv`:
```
uuid	agent	pytest	rubric	reward	result
af4ffc91-76d8-5138-83e5-ba2e89fbf7b0	oracle	1.0	1.0	1.0	PASS
af4ffc91-76d8-5138-83e5-ba2e89fbf7b0	nop	0.0	0.0	0.0	PASS
```

## Checksums
- oracle trial result.json: `a5dbe4c4fc744cceba972af37d4fb81d597d93c49dcc70be8be303a63d99d41d`
- nop trial result.json: `a5dbe4c4fc744cceba972af37d4fb81d597d93c49dcc70be8be303a63d99d41d`
- delivered Opus run `af4ffc91-76d8-5138-83e5-ba2e89fbf7b0-opus-5-20261117-101558-regraded` (trial U5kgfBg) result.json: `a5dbe4c4fc744cceba972af37d4fb81d597d93c49dcc70be8be303a63d99d41d`

All three match: the oracle, the nop and the shipped trajectory were graded on the same task bytes.
