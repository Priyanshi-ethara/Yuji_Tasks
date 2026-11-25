# a6901ded-0579-5c2d-8ae3-a0649c5c5ff2 — oracle / nop report

## VERDICT: PASS

Source: the harbor oracle and nop jobs in `/tmp/qc/oracle_nop_20261116_164054/a6901ded-0579-5c2d-8ae3-a0649c5c5ff2/`.
- Run through `qc_oracle_nop.sh` with JUDGE=codex.
- Run on the final task bytes delivered here, which are the same bytes as the delivered Opus run.

Each raw harbor job is copied FLAT into its folder, following the owner's reference layout (`final_ready_to_go/9cdfe4ec-…/QC/Oracle run`). Each folder holds:
- job.log, lock.json, result.json and config.json;
- the harbor log, as `oracle.log` or `nop.log`;
- summary.tsv;
- the trial dir (`a6901ded-0579-5c2d-8ae3-a0649c5c__3hYpk4i` for the oracle, `…__RQAQ7rc` for the nop), with agent/, artifacts/, verifier/, lock.json, result.json, config.json and trial.log.

There is no raw_job subfolder. The copies are complete because /tmp is wiped on reboot.

| Check | Oracle | Nop | Bar | Result |
|---|---|---|---|---|
| pytest | 1.0 (earned 34 / 34, penalty 0, guards []) | 0.0 (earned 0 / 34, penalty 0, guards []) | oracle > 0.95, nop exactly 0 | PASS |
| rubric | 1.0 (20/20 positives, 0/4 penalties) | 0.0 | oracle > 0.95, nop exactly 0 | PASS |
| reward | 1.0 | 0.0 | oracle > 0.95, nop exactly 0 | PASS |
| summary.tsv | `oracle 1.0 1.0 1.0 PASS` | `nop 0.0 0.0 0.0 PASS` | | PASS |
| judge (verifier/judge.json) | ran true, transport codex, model gpt-5.6-sol, reason null | ran true, transport codex, model gpt-5.6-sol, reason null | gpt-5.6-sol via codex ran | PASS |
| trial | 3hYpk4i, exception_info None | RQAQ7rc, exception_info None | | PASS |
| task_checksum | 5f56d8e467890f42a5f676a0fadbd3e7f68ae7df3af2dce5685a7bf0656cb1de | same | equals the Opus run's | PASS |

- **Same bytes as the run.** The delivered Opus run records the same task_checksum, 5f56d8e4…b1de, in `trajectories/opus-5/run_1/result.json` (job `…-opus-5-20261116-111429`, trial WLTLZ4J) and in jobs.json. The delivered task files are also byte-identical to the `_copies/` snapshot that the oracle/nop runs used (`diff -rq`: no difference). So the oracle, the nop and the Opus run all used identical bytes.
- **Oracle and the live event.** After its four registry writes, the oracle trial's `mcp__LightDatadog__list_events` returns events 880105–880107: the ft-launcher 4.2.2 notice and the 5.80 s and 9.10 s re-measurements. Its Box downloads return the 4.2.2 logs. This shows the trigger fires and that the re-measured records reach a caller in the harness container.
- **Nop.** `verifier/state_capture_failed.txt` reads "collect hook shipped no end_env.json / no server_tool_calls.log". That is expected for the nop agent, which opens no session. The state-reading tests fall back to the seed, every positive test fails closed (0/34), and the judge gives 0 on the empty reply.
- **Extra files at the folder root.**
  - `reward.json`: the trial verifier's reward.json.
  - `summary.txt`: the summary.tsv row, plus judge.json transport and model, plus task_checksum.
  - `<uuid>-oracle-nop-report.md`: this report.
