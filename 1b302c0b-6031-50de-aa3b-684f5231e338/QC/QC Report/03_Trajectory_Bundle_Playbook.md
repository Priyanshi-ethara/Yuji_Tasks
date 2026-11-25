# QC Report — 1b302c0b-6031-50de-aa3b-684f5231e338   layout: full   runs: 1   model(s): opus-5

**What was run.** Every bash block of `qc 2/traj/10_bundle_playbook.md` (blocks 1-8), as written, with `BUNDLE` = a copy
of `TASKS/18Nov_Tasks/1b302c0b-6031-50de-aa3b-684f5231e338` without QC/, after the gatefix and fix round 2 of 2026-11-18 (grader-only). The raw output is
in `03_playbook_script.txt`; every figure below is quoted from it. §2.5 has no script; its checks were run by hand.

**Which run.** `trajectories/opus-5/run_1` is the h2b Opus 5 agent run (original job `…-opus-5-20261118-054121`, trial
7jfiPS7), regraded by the harness on the fix-round-2 tests and rubric (2026-11-19): job
`1b302c0b-6031-50de-aa3b-684f5231e338-opus-5-20261118-054121-regraded`. The agent trajectory is unchanged; only the
verifier ran again. task_checksum `dc3f8fd6…483b` equals the judged oracle/nop (ONDIR `oracle_nop_20261119_112242`).
Playbook 1.6g lists exactly one job, `…-054121-regraded`, with 1 trial (an earlier h2 attempt that failed at agent setup
is kept out, in `_kit/traj/qcsave/18/1b302c0b-…/failed_setup`).

## §1 Model
- run_1 ✅: folder `opus-5`; config `anthropic/claude-opus-5`; trajectory steps `['anthropic/claude-opus-5']`;
  "distinct models after normalising ['opus-5'] ok", "models seen mid-run 1 ok".
- `schema_version ATIF-v1.5 ok`; agent `{'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`;
  reasoning_effort high.

## §1.5 Score sanity (per run)
- **1.5a** reward 0.4223 in reward.json, report.final_reward, result.verifier_result and pass_summary: `spread=0.0 ok`.
  reward.json is trimmed to `{"reward": 0.4223}`.
- **1.5b** `0.2857 vs reported 0.2857 ok`; weighted=20, ledger=20, no drift, no test raised, 0 guards tripped, 7 missed.
- **1.5c** judge `ran=True model=gpt-5.6-sol`; `0.5588 vs reported 0.5588 / channel 0.5588 ok`; `n=20 yes=9 no=11`, raw
  values yes/no only; judge.toml vs graded: nothing missing, extra or drifted.
- **1.5e** `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.4223 vs reward 0.4223 ok`.
- **1.5f** no exception, not errored; final_message.md = last agent text (5294 chars, `same=True`); final_metrics
  6,514,353 prompt / 65,870 completion tokens, $6.32.
- No BLOCKER.

## §1.6 Aggregates
- runs=1, completed=1, errored=0, per_run=1, folders=1: ok; threshold 0.7 everywhere; averages 0.4223 / 0.2857 / 0.5588
  match; pass@1 passed 0, histogram `{'partial': 1}`. No BLOCKER.

## §2 Failure classification (per run)

| run | passed | reward vs threshold | bucket | sub-label |
|---|---|---|---|---|
| run_1 | False | 0.4223 < 0.7 (pytest 0.2857, rubric 0.5588), failure_mode partial | **B (model/agent)** | **`wrong-value-written`** (= the card's TARGET in ROSTER5 W10) |

**Bucket A ruled out:** end_env.json shipped; no exception; judge ran; `total=104 mcp=91 local=13`; `tool results that
look like server errors 0`.

**Evidence for `wrong-value-written`:**
1. **The run wrote question/high and the desk held normal.** The five residential Priority Assistance enquiries were
   written `ticket_type: question, priority: high` (steps 67, 72, 74, 76, 94); T-11 held each at normal (ack at step 67
   echoes high, get_ticket at step 68 returns normal; end_env holds 48201/48202/48204/48206/48225 question/normal).
   Missed (2.2e): the five `…_is_held_at_its_assistance_priority` tests and both note mixes.
2. **It saw the reset and kept the wrong value.** Step 69: "a genuine conflict between the guide and the platform set-up
   … I can't change the set-up myself under guide 2.2"; step 99: not re-set "since the platform would likely just
   reduce them again". It quotes guide 5.4 in the reply but never changed the type.
3. **The rubric misses follow from it.** The judge found no general statement that the self-service worklist takes
   questions only (c-worklist-questions-only, 3); the reply told Carys "Seven enquiries reach the residential worklist"
   and "Her two people are still about right", which pytest charges through the note's type and priority mixes. It
   also missed the draft-provenance items (10 November extract, Annex B as written, Business Assure unchecked).

**Why not another sub-label:** not `guard-tripped` (2.2d none); not `gave-up-early` (28 updates, 28 log rows, the note);
not `tool-surface-tunnel-vision` (page 520102, the guide and the precedents were read); not `instruction-ignored`
(every deliverable done; the error is the held value).

## §2.5 Isolation and leakage (per run)
- result.json `verifier_environment_mode: "separate"`.
- Grader paths touched by the agent: none (grep of every tool-call argument for `/tests`, test_outputs.py,
  test_weights.json, judge.toml, solution/, TRUTH.md, gt_env.json, oracle.json: 0 hits).
- Leakage: the held mixes (5/14/0/9, 1/12/13/2) appear in no seeded record or data file.
- Trivial-solution credit: n/a; the judged nop on the same bytes scores 0.0 / 0.0 / 0.0.

## §3 Reasoning
- `agent steps / with reasoning 105 / 28 (40888 chars)`, field `thought`; reasoning_effort high. Verdict ✅ present.

## §4 Overlap
- 20 tests vs 20 criteria: `DOUBLE-COUNTED=0 PARTIAL=0 INDEPENDENT=20 redundancy=0%`; `RUBRIC-ONLY (no test reaches
  0.5): 20 of 20`. The earlier PARTIAL pair (priority-mix test ↔ m-t11-rule, shared literal "priority") no longer
  registers after the priority-mix test was rewritten in fix round 2 (note vs oracle mix and vs the mix the desk holds).
- Lost weight on run_1: pytest positive lost 35/49 = 71.4 %, guards charged 0.0; rubric positive lost 0.4412 = 44.1 %,
  penalties charged 0.0000 (the rubric has no penalties after fix round 2).
- Recommendation: keep both.

## §5 False pytests
- `0/20 tests carry a flag; BLOCKER flags: 0`; 5.2 no assert/return line carries a rubric figure.

## Verdict
- **SIGNED.** §1, §1.5, §1.6 and §2.5 have no BLOCKER; §2 Bucket B `wrong-value-written`; §3 present; §4 DOUBLE-COUNTED 0;
  §5 BLOCKER flags 0.
- PLAYBOOK HARD BAR: `BLOCKER flags: 0` (§5) and `DOUBLE-COUNTED=0` (§4), both in `03_playbook_script.txt`.
