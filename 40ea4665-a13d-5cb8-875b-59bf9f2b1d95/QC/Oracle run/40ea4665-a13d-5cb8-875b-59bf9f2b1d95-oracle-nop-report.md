# Oracle / nop report: 40ea4665-a13d-5cb8-875b-59bf9f2b1d95 (U14, LIVE)

## VERDICT: PASS (oracle 1.0 > 0.95; nop exactly 0 on pytest, rubric and reward)

- **Run:** harbor oracle and nop runs on the final task bytes (the same bytes as the delivered Opus run). Judge on.
  ONDIR = `/tmp/qc/oracle_nop_20261116_165300`. Each raw harbor job is copied flat into `Oracle run/` and `Nop run/`
  (job.log, lock.json, result.json, config.json, the harbor log as `oracle.log` / `nop.log`, summary.tsv and the trial
  directory). /tmp is wiped on reboot, so these copies are the record.
- **Judge:** gpt-5.6-sol via codex on both runs. Each `judge.json` has
  `{'ran': True, 'model': 'gpt-5.6-sol', 'transport': 'codex', 'reason': None}`.

| agent | trial | pytest | rubric | reward | detail | exception |
|---|---|---|---|---|---|---|
| oracle | iuiLQpy | 1.0 | 1.0 | 1.0 | ledger earned 42/42, 0 charged, no guard tripped. All six event tests pass (`test_amended_meter_site_1..4_*`, `test_amended_meter_records_read_before_the_summary_mail`, `test_amended_sites_drafted_after_their_amendment_was_read`). Rubric: 20/20 positives yes, 0 of 5 penalties. | null |
| nop | fkeJ58T | 0.0 | 0.0 | 0.0 | ledger earned 0/42, 0 charged; rubric 0 positives, 0 penalties | null |

`summary.tsv`:
```
uuid	agent	pytest	rubric	reward	result
40ea4665-a13d-5cb8-875b-59bf9f2b1d95	oracle	1.0	1.0	1.0	PASS
40ea4665-a13d-5cb8-875b-59bf9f2b1d95	nop	0.0	0.0	0.0	PASS
```

Harbor tables. Oracle: `Trials 1 │ Exceptions 0 │ Pytest 1.000 │ Reward 1.000 │ Rubric 1.000`. Nop:
`Trials 1 │ Exceptions 0 │ Pytest 0.000 │ Reward 0.000 │ Rubric 0.000`.

## Checksums
- oracle `result.json`: `4b0823a2a526c545756384c74109e5a390e00555b0782dbc44f902ebcffc0d5e`
- nop `result.json`: `4b0823a2a526c545756384c74109e5a390e00555b0782dbc44f902ebcffc0d5e`
- the delivered Opus run (`40ea4665-…-opus-5-20261116-112639`, trial C9Cx4WD) `result.json` and `jobs.json`:
  `4b0823a2a526c545756384c74109e5a390e00555b0782dbc44f902ebcffc0d5e`

All three match, so the oracle, the nop and the shipped trajectory were graded on the same task bytes. The delivered
task folder is byte-identical to `out/build/<uuid>`: `diff -rq` excluding QC/ and trajectories/ is empty.

## Notes
- The nop verifier has `state_capture_failed.txt` ("collect hook shipped no end_env.json / server_tool_calls.log").
  This is expected for a do-nothing agent that never opens an app. Every positive test fails closed and no guard is
  charged.
- The oracle's reply states every positive rubric item, including the CT amendment it read after the trigger
  (the 21st distinct customer drafted): "the commissioning records of Quenby Print Works, Thornaby Wharf Cold Store,
  Ashgrove Plastics Moulding, Hollin Bridge Sawmill … carried a 16 November 2026 amendment". So the live records were
  served correctly on these bytes.
