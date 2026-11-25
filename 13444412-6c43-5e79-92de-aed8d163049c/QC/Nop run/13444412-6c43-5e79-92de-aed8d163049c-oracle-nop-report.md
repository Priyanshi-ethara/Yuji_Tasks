# Oracle / nop report: 13444412-6c43-5e79-92de-aed8d163049c (U05)

## VERDICT: PASS (oracle 1.0 > 0.95; nop exactly 0 on pytest, rubric and reward)

- **Run:** `PARALLEL=1 JUDGE=codex bash qc_oracle_nop.sh TASKS/16Nov_Tasks/13444412-6c43-5e79-92de-aed8d163049c`, launched through
  `_kit/traj/regrade16.sh` (tag rg2). It ran on the final delivered bytes, after the QC_FINAL16 grader-only rubric fixes
  (r-refund-routed, r-pemberton-domain and the five penalty carve-outs; see 02_Ruthless). ONDIR =
  `/tmp/qc/oracle_nop_20261116_173855`. The raw harbor jobs are copied flat into `Oracle run/` and `Nop run/`
  (job.log, lock.json, result.json, config.json, the harbor log, summary.tsv and the trial directory), because /tmp is
  wiped on reboot.
- **Judge:** gpt-5.6-sol via codex on both runs. `judge.json` has `{'ran': True, 'model': 'gpt-5.6-sol', 'transport': 'codex', 'reason': None}`.

| agent | trial | pytest | rubric | reward | detail | exception |
|---|---|---|---|---|---|---|
| oracle | ng9ThTm | 1.0 | 1.0 | 1.0 | ledger earned 47/47, 0 charged, no guard tripped; rubric 20/20 positives yes, 0 of 5 penalties | null |
| nop | XHYFvLJ | 0.0 | 0.0 | 0.0 | ledger earned 0/47, 0 charged; rubric 0 positives, 0 penalties | null |

`summary.tsv`:
```
uuid	agent	pytest	rubric	reward	result
13444412-6c43-5e79-92de-aed8d163049c	oracle	1.0	1.0	1.0	PASS
13444412-6c43-5e79-92de-aed8d163049c	nop	0.0	0.0	0.0	PASS
```

Harbor tables. Oracle: `Trials 1 │ Exceptions 0 │ Pytest 1.000 │ Reward 1.000 │ Rubric 1.000`. Nop:
`Trials 1 │ Exceptions 0 │ Pytest 0.000 │ Reward 0.000 │ Rubric 0.000`.

## Checksums
- oracle `result.json`: `26e36975951356f5e449ce9063816279e56c9dae402a5f54ef01210da0c4abbb`
- nop `result.json`: `26e36975951356f5e449ce9063816279e56c9dae402a5f54ef01210da0c4abbb`
- the delivered Opus run (`…-opus-5-20261116-114232-regraded`, trial itxKZDo) `result.json` and `jobs.json`: `26e36975951356f5e449ce9063816279e56c9dae402a5f54ef01210da0c4abbb`

All three match, so the oracle, the nop and the shipped trajectory were graded on the same task bytes. The delivered task
folder is byte-identical to `out/build/13444412-6c43-5e79-92de-aed8d163049c`: `diff -rq` excluding QC/ and trajectories/ is empty.

## The earlier oracle at 0.9881 (why it was not accepted as-is)
- The pre-QC oracle/nop (`/tmp/qc/oracle_nop_20261116_170836`, oracle pytest 1.0 / rubric 0.9762 / reward 0.9881, nop 0)
  lost one rubric item: **r-refund-routed** (weight 1/42). The judge said the reply "does not explicitly say Finance picks
  the request up from the ticket reply, as this criterion requires". The oracle reply does say that Finance declined the
  refund (FIN-2207) and that the ticket reply tells the customer Finance handles it.
- This was a grader wording defect. The criterion required a mechanism detail ("who pick it up from the ticket reply")
  that the instruction never asks for. The instruction asks only "what a customer asked for that we did not do and where
  it went instead". The fix (rg1) keeps "goes to Finance" and the reason as required, and says that how Finance hears of the request is not required.
  The rg1 oracle (`/tmp/qc/oracle_nop_20261116_173110`) then scored 1.0 / 1.0 / 1.0.
- rg2 then loosened r-pemberton-domain, so that the sender being the company's registered billing contact counts as well
  as the email domain (see 02_Ruthless). This oracle/nop is the final one on those bytes. Both earlier ONDIRs are
  superseded and not shipped.

## Notes
- The nop verifier has `state_capture_failed.txt` ("collect hook shipped no end_env.json / server_tool_calls.log").
  This is expected for a do-nothing agent that never opens an app. Every positive test fails closed, and no guard is
  charged.
