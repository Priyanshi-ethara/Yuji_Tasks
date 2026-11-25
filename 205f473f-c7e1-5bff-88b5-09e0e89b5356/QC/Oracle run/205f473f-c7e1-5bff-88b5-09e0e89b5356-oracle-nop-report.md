# Oracle / nop report: 205f473f-c7e1-5bff-88b5-09e0e89b5356 (U04 crash-owner-routing, hardened to LIVE)

## VERDICT: PASS (oracle 1.0 > 0.95; nop exactly 0 on pytest, rubric and reward)

- **Run:** the harbor oracle and nop jobs on the final task bytes (the same build the Opus run used). ONDIR =
  `/tmp/qc/oracle_nop_20261116_163724`. Both raw jobs are copied flat into `Oracle run/` and `Nop run/`
  (job.log, lock.json, result.json, config.json, the trial folder, and the harbor log as `oracle.log` / `nop.log`),
  because /tmp is wiped on reboot.
- **Judge:** gpt-5.6-sol via codex on both runs. Both `judge.json` files read
  `{'ran': True, 'model': 'gpt-5.6-sol', 'transport': 'codex', 'reason': None}`.

| agent | trial | pytest | rubric | reward | detail | exception |
|---|---|---|---|---|---|---|
| oracle | ooThF6W | 1.0 | 1.0 | 1.0 | ledger earned 46/46, penalty 0, no guard tripped, no test errors; rubric 19/19 positives yes, 0 of 3 penalties | null |
| nop | caLsG3f | 0.0 | 0.0 | 0.0 | ledger earned 0/46, penalty 0, no guard tripped (all 16 positive tests in `missed`); rubric 0/19 positives, 0 of 3 penalties | null |

`summary.tsv`:
```
uuid	agent	pytest	rubric	reward	result
205f473f-c7e1-5bff-88b5-09e0e89b5356	oracle	1.0	1.0	1.0	PASS
205f473f-c7e1-5bff-88b5-09e0e89b5356	nop	0.0	0.0	0.0	PASS
```

Harbor tables. Oracle: `Trials 1 │ Exceptions 0 │ Pytest 1.000 │ Reward 1.000 │ Rubric 1.000` (runtime 1m 41s).
Nop: `Trials 1 │ Exceptions 0 │ Pytest 0.000 │ Reward 0.000 │ Rubric 0.000` (runtime 1m 29s).

## Checksums
- oracle trial `result.json` task_checksum: `e0e779d4e95a7678daf1d71487b47c5987679dd3b0a8a1edd1bc02b99af9f77a`
- nop trial `result.json` task_checksum: `e0e779d4e95a7678daf1d71487b47c5987679dd3b0a8a1edd1bc02b99af9f77a`
- delivered Opus run (job `205f473f-…-opus-5-20261116-111050`, trial TDTmhge) `run_1/result.json` and `jobs.json`:
  `e0e779d4e95a7678daf1d71487b47c5987679dd3b0a8a1edd1bc02b99af9f77a`
- `dirhash(sha256)` of the delivered task folder (QC/ and trajectories/ excluded) and of `out/build/<uuid>`:
  `e0e779d4e95a7678daf1d71487b47c5987679dd3b0a8a1edd1bc02b99af9f77a`

All match, so the oracle, the nop and the shipped trajectory were graded on the delivered task bytes.

## Notes
- The nop verifier has `state_capture_failed.txt` ("collect hook shipped no end_env.json / server_tool_calls.log").
  This is expected for a do-nothing agent that never opens an app. Every positive test fails closed and no guard is
  charged.
- The rubric has 22 criteria, 19 positive (+43 in authoring weights) and 3 penalties (-11). The counts above are over
  the compiled set the judge ran.
