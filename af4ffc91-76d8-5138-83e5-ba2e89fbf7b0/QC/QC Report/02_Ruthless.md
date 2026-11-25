## VERDICT: PASS

Task af4ffc91-76d8-5138-83e5-ba2e89fbf7b0 (W08 laytime-demurrage-statement, STATIC, TARGET wrong-value-written,
MECHANISM distractor-saturated event logs). This is a review of the FINAL bytes after round 3 of 2026-11-18 (FIX3_18),
following `qc 2/static/20_ruthless.md`. These are the bytes the recorded Opus run was regraded on (job
`af4ffc91-76d8-5138-83e5-ba2e89fbf7b0-opus-5-20261117-101558-regraded`, trial U5kgfBg, task_checksum `a5dbe4c4…d41d`, equal on
the regraded run, the judged oracle and the judged nop).

**Delivered run (pass_summary.json): pytest 0.2821, rubric 0.6154, reward 0.4487** (< 0.60; both channels > 0 and < 1; no guard
tripped; failure_mode `partial`).

Three grader-only passes ran that day:
- **GATEFIX18** removed the run-wide red-line gate from tests/test_outputs.py, renamed the anti-blanket precondition
  `_value_preconditions()`, made the summary-page precondition gate only the closing tests, and gave every guard a dedicated
  detection helper.
- **FIX2_18** followed an independent rubric review (three decoy penalties and nine borderline items removed).
- **FIX3_18** followed a confirming review. It rewrote tests/judge.toml (20 criteria, positives 26, no penalties) and changed
  only the reply text in solution/solve.py (no tool call) and solution/TRUTH.md. instruction.md, task.toml, data/, world_data/,
  environment/, tests/test_outputs.py, test_weights.json, oracle.json, old_env.json and gt_env.json are byte-identical to the
  pre-FIX3 input. Rule D: the review found the test file clean; nothing changed there.

I re-ran the §1 mechanical script on a UUID-named copy of `harness_mcp_atlas/input/af4ffc91-…` (raw output in
`02_ruthless_mechanical.txt`), regenerated the oracle with kit `oracle_local.py`, replayed the oracle, the nop and the delivered
Opus run through the pytest ledger (kit `grade_local.py`), and ran the client's dynamic gate check (`work/fix1118/gatecheck.py`).

## Constraint Results
- **C1 (grounded expected values): PASS.** Every expected figure, id and label comes from `oracle.json["reported"]` via `KEY()`,
  and solve.py derives each one at run time. §1c: "of those, hard-coded in test_outputs.py: none". No rubric item carries a graded
  figure.
- **C2 (every test reads agent evidence): PASS.** §1a: "tests reading NO evidence: none"; "tests reading oracle/seed only: none".
- **C3 (do-nothing run scores zero): PASS.** The nop replay gives `pytest = 0.0000 (earned 0.0 / 39, charged 0.0)`; the judged
  nop scores 0 / 0 / 0.
- **C4 (guards fire in the right direction): PASS.** `pass_charges`; the oracle trips none (39/39, charged 0). gatecheck on the
  delivered bundle: every guard `guard fires=True` with `positives voided 0/15`; a REAL appended logout (LightConfluence) fires the
  sign-out guard with `positives voided 0/15`; `RESULT af4ffc91 worst_single=0 all_at_once=0`.
- **C5 (prompt fidelity): PASS.** Every rubric item maps to a reply bullet of the instruction:
  - **"the basis: when laytime started"**: r-start-rule, r-nor-any-time, r-start-each-call.
  - **"what was excepted and why"**: r-shifting-rule, r-meal-surveys-count, r-exceptions-each-call.
  - **"which weather entries you did and did not take as weather time, with the reason"**: r-clause17-test, r-genuine-closures,
    r-hourly-figures, r-fog-continuing, r-ambient-weather-remarks, r-light-rain-noise, r-weather-sheet-closures-only,
    r-port-weather-notes, r-kpi-dashboard, r-weather-each-call.
  - **"for each dispute, what the owners did differently"**: r-disputes-explained, r-owners-not-source.
  - **"the four quarter totals"**: r-no-conversion, r-totals-merrow-figures.
- **C6 (statement ↔ verifier alignment): PASS.** Clause 17 reads "unless, and only for so long as, weather actually prevents";
  desk method §5 gives the but-for test. New items are true per the data: the close timetable says "The KPI dashboard draft is
  built from the agents' sheets and is not used for the accrual" and the draft's own header says "auto-built from agents' sheets";
  the instruction and desk method §1 say the owners' statement "is never a source for our figure"; the timetable says "Disputed
  calls are accrued at Merrow's figure, not the owners'"; every call's non-weather exceptions follow TRUTH's derivation notes.
- **C7 (agent cannot reach or alter the verifier): PASS.** `environment/Dockerfile` copies only `state_capture.py`.
- **C8 (no leaked solution artifacts): PASS.** Nothing agent-visible changed.
- **C9 (deterministic reward): PASS.** The local replay of the delivered run is `pytest = 0.2821 (earned 11.0 / 39, charged 0.0)`,
  the same as before all three passes.

## Rubric ↔ Pytest Cross-Reference (twin rule)

| Rubric item | w | What it grades | Nearest pytest test | Same signal? |
|---|---|---|---|---|
| r-port-weather-notes | +5 | provenance: the port notes describe the port area, not the work on board | none (data file, never read-tested) | No |
| r-weather-sheet-closures-only | +3 | provenance: the agents' sheet and footers list closures only | none (data file, never read-tested) | No |
| r-kpi-dashboard | +1 | provenance: the KPI draft is built from the agents' sheets | none (data file, never read-tested) | No |
| r-clause17-test, r-genuine-closures, r-hourly-figures | +1 each | the weather clause as stated; genuine closures while working; hourly figures as evidence | none | No: method only |
| r-fog-continuing, r-ambient-weather-remarks, r-light-rain-noise | +1 each | look-alike remarks present in every statement, not taken | none | No |
| r-meal-surveys-count, r-shifting-rule, r-start-rule, r-nor-any-time | +1 each | standing rules given as the basis; no call or charter named | group tests (values) | No: method only |
| r-start-each-call, r-exceptions-each-call, r-weather-each-call, r-disputes-explained | +1 each | coverage of the asks; no value checked | none reads the reply | No |
| r-owners-not-source, r-totals-merrow-figures, r-no-conversion | +1 each | how the owners' figures and totals were used; no figure | Owners Figure / status, summary money lines | No: method only |

Penalties: none. No positive names a call, call group, charter group or summary figure that pytest grades, states a rule or
look-alike that only one graded call or group carries, restates a guarded act, gates on the trajectory or world events, or asks
whether a record was read. Playbook §4: `DOUBLE-COUNTED=0 PARTIAL=1 INDEPENDENT=19`; the PARTIAL row
(test_rain_closures_inside_other_stoppages_disputed_calls ↔ r-totals-merrow-figures, S1 0.10, S2 0.50) is a literal-word
match only: the test grades the claim records of two rain-group calls, the item grades that the totals are made of Merrow's own
figures; no shared entity or decision.

## 4.2 — "can a run cross a red line and pass?" (recorded openly)
Yes, by design. The client ruling of 2026-11-18 governs this question: a red line costs only its own guard weight, and positives
are never voided run-wide. Kit replay of the oracle plus one owner mail: pytest (39 − 5)/39 = 0.8718. The oracle plus an owner mail
and a Xero invoice: 0.7436 (both guards charged, no positive missed). With a full rubric that run clears the 0.7 threshold. Under
the binding ruling this is not a defect.

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None.

## Minor Findings (polish)
None.

## Coverage Holes
None. Pytest grades the claim records field by field, the dispute notes, the summary page (six lines, written last), the
statement-of-facts reads before writes, both red lines, the read-only rule and sign-out. The rubric grades only what the reply
reports that pytest cannot see.

## RESOLVED — confirming review of 2026-11-18 (FIX3_18), one pass

| id | finding | action |
|---|---|---|
| r-rain-worksheet-departure (+1) | CONFIRMED: restates the rain-trap group's defining feature (closures inside other stoppages deducted in full) graded by test_rain_closures_inside_other_stoppages_agreed_calls / _disputed_calls | deleted |
| r-other-stoppage-counts (+1) | BORDERLINE, leans confirmed: the Charterers'-side stoppage rule is what the rain groups and the gale stand-down trap turn on; no honest clearing line | treated as CONFIRMED, deleted |
| r-overlap-once (+1) | BORDERLINE: the only overlapping exception in the quarter is PC-3105's holiday Saturday, a graded call (a rule only one graded entity carries) | treated as CONFIRMED, deleted |
| r-wind-gusts-continuing (+5) | BORDERLINE: the "gusting 8 — loading continues" lines sit beside each wind stand-down of the graded wind calls (PC-3101/3103/3109/3112, plus PC-3111) and exist only in read-tested statements; no honest clearing line | treated as CONFIRMED, deleted |
| r-port-weather-notes | weight 3 → 5 (the family's data-file provenance item; no test reads the port notes) | re-weighted so 5 is used |
| (replacements) | criteria count fell to 16 | added r-exceptions-each-call (coverage of "what was excepted and why"), r-kpi-dashboard (provenance of a data file), r-owners-not-source and r-totals-merrow-figures (how the owners' figures and the totals were used); none grades a value or names a call |

Earlier rounds (FIX2_18, GATEFIX18): see solution/TRUTH.md "Rubric vs pytest".

## CLEARED (considered and dismissed, with reasons)
- **r-weather-sheet-closures-only (3):** provenance of a data file no test reads; it names no call, group or stoppage, and a reply
  passes it without identifying any graded stand-down or closure (it fits equally the sheet's genuine closures).
- **r-fog-continuing (1):** fog-with-work-continuing lines appear in ten of the twelve Q3 statements and in the Q2 ones, so they are
  no graded group's defining feature; the item grades a weather judgment, not reading a record, and names no call.
- **r-ambient-weather-remarks (1):** "reported in port" / forecast / barometer / "sky clearing" remarks appear in all sixteen
  statements (Q3 and Q2); not any graded group's feature; names no call; grades a judgment, not a read.
- **r-hourly-figures (1):** the hourly cargo figures are in every statement and are the evidence for every stoppage, genuine or
  not; the item names no call and asks no figure, so it is method, not the decision any test grades.
- **r-weather-each-call, r-start-each-call (1 each):** coverage of explicit reply asks; any start time and any listing of weather
  time passes, so neither requires a graded value or the input that fixes it.
- **Rule D:** the review found the test file clean; no change.
- **r-clause17-test:** it states the charter clause itself; a reply can state it and still deduct every closure.
- **Considered and not added:** the charters' turn times and SHINC terms (they name charters a per-charter test grades), the
  owners' individual errors, despatch at half rate and laytime allowed (not in the reply bullets), statement-only formalities
  (bunkering, PSC, customs: content only in read-tested statements).
- **Real run's rubric (0.6786 → 0.6154):** the judge said no on r-port-weather-notes (5), r-kpi-dashboard, r-nor-any-time,
  r-exceptions-each-call, r-owners-not-source and r-totals-merrow-figures (1 each). No item was tailored to the run.
- **Reply-only strategy (C3 a):** pytest 0; even with the whole rubric reward ≤ 0.50 < 0.7.
- **Summary-page precondition:** it gates only the summary-line, count and summary-last tests (no-page replay 30/39 = 0.7692).

## What I Verified Clean
- **Tests:** 20, unchanged. 15 positives total 39 (5,5,5,5,5,3,3,1×8); 5 guards total 17 (−5,−5,−3,−3,−1). Settings:
  pass_charges, threshold 0.7, null_floor 0.0, gate None. No test exceeds half the positives.
- **Rubric:** 20 criteria, all final_answer and binary. Positive weights 5 ×1, 3 ×1, 1 ×18 = 26, penalties 0. The largest item is
  5, under half (13).
- **Oracle reply:** regenerated by `oracle_local.py` with reply-text changes only (a per-call "Excepted other than weather" clause,
  a totals sentence and a sources sentence); it states every positive literally.
- **Replays:** oracle `pytest = 1.0000 (earned 39.0 / 39, charged 0.0)`; nop `0.0000`; delivered Opus run `0.2821` (unchanged).
- **Harness** (ONDIR `oracle_nop_20261119_112548`): oracle 1.0 / 1.0 / 1.0, nop 0.0 / 0.0 / 0.0; regraded run pytest 0.2821,
  rubric 0.6154, reward 0.4487, guards_tripped [].
- **Kit checks:** check_bundle `0 FAIL, 0 WARN`. gatecheck `RESULT af4ffc91 worst_single=0 all_at_once=0`. simcheck batch18
  (rubric max cosine 0.072) and batch115 (0.053): `0 flagged pair(s)`.
- **Hygiene:** no `/Users/` path in the agent-visible tree; no __pycache__; no tests/task_lib.py.
