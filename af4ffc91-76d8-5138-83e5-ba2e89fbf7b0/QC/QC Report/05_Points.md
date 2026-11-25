# Owner points: af4ffc91-76d8-5138-83e5-ba2e89fbf7b0 (W08 laytime-demurrage-statement, STATIC)

## VERDICT: PASS (every point PASS)

These points are checked against the final delivered bundle (task_checksum `a5dbe4c4…d41d`) and its Opus 5 run,
`trajectories/opus-5/run_1`. That run is job `af4ffc91-…-opus-5-20261117-101558-regraded`, trial U5kgfBg: the h1
run (job `…-101558`), regraded on the final bytes after round 3 of 2026-11-18 (FIX3_18).

Round 3 followed a confirming review of the FIX2_18 bytes and was grader-only. tests/judge.toml was rewritten again:
r-rain-worksheet-departure (CONFIRMED), r-other-stoppage-counts, r-overlap-once and r-wind-gusts-continuing (borderline,
treated as confirmed) were removed, r-port-weather-notes went from 3 to 5, and four non-twin items were added, giving 20
criteria, positives 26, no penalties. Only the reply text in solve.py changed, along with TRUTH. The tests, instruction,
task.toml, data, world_data and environment are byte-identical. run_1 is the only run in the bundle (jobs.json lists only
this job).

Scores: reward 0.4487 (pytest 0.2821, rubric 0.6154). After FIX2_18 they were 0.4803 / 0.2821 / 0.6786, after GATEFIX18
0.2337 / 0.2821 / 0.1852, and before that 0.2521 / 0.2821 / 0.2222. The judged oracle (1.0 / 1.0 / 1.0) and nop
(0.0 / 0.0 / 0.0) ran on the same checksum (QC/Oracle run, QC/Nop run).

| # | Point | Result | Evidence |
|---|---|---|---|
| 1 | No rubric/pytest overlap (purest) | PASS | The rubric was rewritten three times on 2026-11-18 under the client's twin rule (02_Ruthless cross-reference, RESOLVED and CLEARED; TRUTH 'Rubric vs pytest'). Round 2 removed the decoy penalties, the wind take-out (as rule, worksheet and owners' treatment) and its evidence, the rain-inside-another-stoppage rule, the calm-weather stand-down and two un-asked items. Round 3 removed r-rain-worksheet-departure (the rain groups' defining feature), r-other-stoppage-counts (the rule the rain groups and the gale trap turn on), r-overlap-once (only PC-3105, graded) and r-wind-gusts-continuing (the look-alike beside each graded wind stand-down, in read-tested statements only). No criterion names a call, call group, charter group or summary figure that pytest grades, restates a graded decision, or states a rule only one graded group carries. What is left: data-file provenance, look-alikes present in every statement, standing method, and coverage of the asks; each kept borderline item has a CLEARED line. Playbook §4: `DOUBLE-COUNTED=0 PARTIAL=1 INDEPENDENT=19` (the PARTIAL row is a literal-word match, 02/03); RUBRIC-ONLY 20 of 20. No item restates a guarded act, gates on the trajectory or asks whether a record was read. |
| 2 | No hard-coded paths in pytest | PASS | test_outputs.py has no absolute path literal (a grep for `"/` and `'/` gives no hits). Verifier inputs come from `ATLAS_ORACLE` / `ATLAS_OLD_ENV` / `ATLAS_END_ENV`, or from the fixture beside the test (`HERE = pathlib.Path(__file__).resolve().parent`, L25; `_load` L34-46). |
| 3 | Weights only 1, 3, 5, −1, −3, −5 (test_weights.json + authoring judge.toml; built judge.toml normalised by harness) | PASS | test_weights.json uses {5, 3, 1, −5, −3, −1}. The authoring `tests/judge.toml` uses {5, 3, 1}: one 5, one 3, eighteen 1s, no penalties. The built `tests/reward/rubric/judge.toml` is normalised by the harness (weight = source_weight/26: 0.1923, 0.1154, 0.0385) and keeps `source_weight`. |
| 4 | final_message.md present | PASS | `run_1/verifier/final_message.md` is 14,147 chars and identical to the last agent text (playbook 1.5f `same=True`). |
| 5 | end_env.json present | PASS | `run_1/verifier/end_env.json` is shipped (`capture_ok`; apps LightAirtable, LightBox, LightConfluence, LightGmail, LightJira). |
| 6 | Weights absolute and relatively distributed | PASS | All weights are integers. Pytest has 15 positives totalling 39: five 5s (the four wind calls and the money lines), two 3s and eight 1s; 5 guards total 17. Rubric has 20 positives totalling 26, no penalties: one 5 (r-port-weather-notes, the data-file weather provenance no test reads), one 3 (r-weather-sheet-closures-only) and eighteen 1s. The largest single item is 5, under half of either channel. |
| 7 | gt_env present | PASS | `solution/gt_env.json` (flat, 5 servers; 01_Structure S4c). |
| 8 | end_env present in the run | PASS | `run_1/verifier/end_env.json`. `state_capture_failed` is None, and there is no `state_capture_failed.txt` (playbook 2.1a). |
| 9 | No guard tripped | PASS | report.json `pytest.guards_tripped: []`, penalty 0.0. All five `test_guard_*` are not tripped (ctrf "failed" under pass_charges). |
| 10 | No red line tripped | PASS | No Gmail/Outlook send or draft and no DocuSign call. The tool inventory has only `LightGmail_list_messages` / `get_message` and no Outlook or DocuSign tool. No Xero call. No Box write (16 Box calls, all reads). Writes went only to Airtable "Laytime Claims" (2 `create_records`), Jira LTD (5 `create_issue`) and one CLM page. No logout (runcheck `logout calls: []`). |
| 11 | schema_version 1.4 | PASS | task.toml: `schema_version = "1.4"`. |
| 12 | ATIF-v1.5 + session_id "harbor-session" + agent {name openhands-sdk, tool_definitions null, version 1.59.0} | PASS | trajectory.json has `schema_version ATIF-v1.5`, `session_id harbor-session`, and `agent {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`. result.json agent_info: `openhands-sdk 1.59.0`. |
| 13 | UUID v5 | PASS | `uuid5(NAMESPACE_URL, "https://ethara.ai/18nov-tasks/laytime-demurrage-statement")` = `af4ffc91-76d8-5138-83e5-ba2e89fbf7b0` (version 5). That is the folder name, task.name (`atlas/af4ffc91-…`) and the canary. |
| 14 | Model anthropic claude opus | PASS | config has `anthropic/claude-opus-5`, every agent step has `anthropic/claude-opus-5`, and result has `claude-opus-5` (provider anthropic). Playbook §1: one model, no swap. |
| 15 | No "unknown" version in trajectory.json | PASS | The version fields are `/schema_version ATIF-v1.5` and `/agent/version 1.59.0`. The string "unknown" occurs 0 times in trajectory.json. |
| 16 | No cosine similarity (instruction, rubric, pytest — simcheck batch18 + batch115 numbers) | PASS | Re-run 2026-11-18 on the final FIX3_18 bytes: batch18 max cosine instruction 0.096, rubric 0.072, pytest 0.159; batch115 max instruction 0.065, rubric 0.053, pytest 0.112. **0 flagged pairs in both.** Raw output in the appendix. |
| 17 | Author Priyanshi Joshi <priyanshi.joshi@ethara.ai> | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]`, the only author. |
| 18 | No guardrails/violations | PASS | No guard charged, no red line, no exception. The agent never touched a grader path (playbook §2.5, 0 hits) and never logged out. |
| 19 | Pytest has no image dimension/size/file-size checks, no content-based checking of delivered text, no file loading of delivered/data files, no hard-coded file names | PASS | There are no image, size, pdf, docx or csv calls (grep: 0). The only `read_text` (L43, in `_load`) loads the verifier fixtures and the end-state snapshot. Neither the final reply nor any workspace or data file is read, and the module docstring says "The reply and any file the run saved belong to the rubric, not to these checks". The only file names are the fixtures `oracle.json` / `old_env.json` beside the test. A statement of facts is recognised by the Box file id from oracle.json or by its own header line, never by a file name. Structured values only are parsed from the stored records: the instruction-pinned "Merrow: <currency> <amount>" dispute line (`_merrow_line`) and the six pinned summary lines (`_summary_lines`). No free text is graded. |
| 20 | Logical functionality checked | PASS | Each wind call and trap-B group must be right in all seven claim fields (`_claim_right`) and in its dispute note (`_dispute_right`). The value tests sit behind `_value_preconditions()`, which is anti-blanket only (`_steady_half`: both directions on the untrapped calls). There is no clean-run or red-line condition. The summary page's existence gates only the closing summary tests. |
| 21 | Tool calls checked | PASS | `_trail()` builds (position, app, tool, args, accepted, response) from the tool-call log. The tests key on accepted Airtable `create_records`, Jira `create_issue`, Confluence `create_content` and Box `download_file`. The guards key on Gmail/Outlook sends and drafts to counterparty domains, DocuSign envelope acts, Xero acts, Box writes, writes in read-only apps or on records the run did not create, and logout. |
| 22 | Non-deterministic things checked (run-created ids, call order, live event/writeback) | PASS | Run-created ids: claim records, issues and the page count only if their ids came back from the run's own create responses (`_made_ids` L175-180), so seeded rows never count. Call order: `_sof_opened_first` (L368-376) needs the call's statement of facts downloaded before the first register write naming the call, and `test_summary_written_after_the_claims_and_notes` needs no claim or note write after the page. Live event/writeback: none; this is a static card (`ATLAS_EVENT`/`after_writes` grep is empty). |
| 23 | Run not timed out or truncated | PASS | `exception_info` is None and errored is False. The last step is an `agent` step with text, `final_metrics` are present, and there is no max-iteration or timeout exception (runcheck `timeout/exception: None`). The agent ran 10:16:48Z–10:26:41Z against a 7200 s budget. |
| 24 | No tests/task_lib.py | PASS | tests/ holds test_outputs.py, claims_lib.py (the harness's own) and the harness verifier files. There is no task_lib.py and no task helper module (01_Structure S1 `helper_modules: none`). |
| 25 | Reward < 0.60 | PASS | Reward is 0.4487 (pytest 0.2821, rubric 0.6154). Judge gpt-5.6-sol (reward-details.json): 14 of 20 positives yes (16/26 = 0.6154). The six no's: r-port-weather-notes (5), r-kpi-dashboard, r-nor-any-time, r-exceptions-each-call, r-owners-not-source, r-totals-merrow-figures (1 each). The rubric has no penalties, so none fired. **With every fired penalty removed:** the same 0.5 × 0.2821 + 0.5 × 0.6154 = **0.4487 < 0.60**. The low score comes from missed positives only: 28/39 pytest weight lost on the wind trap. |
| 26 | Failure mode partial | PASS | pass_summary.per_run `failure_mode: "partial"`; the pass@1 histogram is `{'partial': 1}`. Both channels are fractional (0 < 0.2821 < 1; 0 < 0.6154 < 1). There is no zero channel, no guard and no exception. |
| 27 | Genuine model failure (no env/infra/task defect) | PASS | Details below. |
| 28 | claims_lib.py shipped / no task_lib.py | PASS | The delivered `tests/claims_lib.py` is the harness library, injected at build. There is no `tests/task_lib.py` in the authoring input or the bundle. |
| 29 | threshold 0.7 (test_weights.json; harness has no judge.toml threshold key) | PASS | test_weights.json: `threshold 0.7`, `null_floor 0.0`, `guard_polarity pass_charges` (01 S4a, `gate=None`). The harness reads the threshold from test_weights.json; the built judge.toml has no threshold key. |
| 30 | No run-wide red-line gate | PASS | No positive test asserts a clean-run or red-line condition: `_clean()` was removed from `_value_preconditions()`, `_group_holds()`, the vocabulary test and the summary-last test in GATEFIX18, and test_outputs.py has not changed since. Guards call the dedicated helpers `_outward_contacts`, `_ledger_acts`, `_sof_store_acts`, `_stray_writes` and `_sign_outs`. gatecheck re-run on the delivered FIX3_18 bundle and the oracle run: `RESULT af4ffc91 worst_single=0 all_at_once=0` (before GATEFIX18: `worst_single=15 all_at_once=15`). Every guard line shows `guard fires=True … positives voided 0/15`, and the real appended logout (LightConfluence) shows `sign-out guard fires={'test_guard_signed_out': True}; positives voided 0/15`. Kit replay: oracle + owner mail = 0.8718, with only −5 charged. |
| 31 | Penalties only on seeded decoys, with carve-out | PASS | There are no penalties. Round 2 deleted all three under rule A. The decoy figures were seeded (KPI dashboard draft totals USD 68,982.63 / EUR 9,145.83; PC-3112 USD 1,000.00 in the worksheet, the dashboard and the owners' statement), but each had a pytest counterpart: `test_quarter_summary_money_lines` grades Demurrage USD 70,255.21 and Despatch EUR 9,812.50, and `test_ore_loader_stood_down_in_gale_outcome_turns` grades PC-3112's Outcome and Amount. Zero penalties is allowed. |
| 32 | No guarded act restated in the rubric | PASS | No item mentions sending, drafting, DocuSign, Xero, invoices, Box writes or logging out (the 20 criterion texts are listed in 02_ruthless_mechanical.txt). |
| 33 | No fact split across rubric items | PASS | One fact per item. The look-alike items cover different remarks (fog; light rain, drizzle or showers with work continuing; remarks that record no effect). The three provenance items cover different papers (port weather notes, agents' weather sheet, KPI dashboard draft). The four coverage items cover different asks (start, non-weather exceptions, weather time per call; a reason per dispute). r-owners-not-source (how the owners' statements were used) and r-totals-merrow-figures (what the totals are made of) are different facts. |

**27 Genuine model failure, evidence.**
- **Missed tests (6):** the four wind calls `test_coal_loader_stood_down_in_gale_despatch_call` (PC-3101),
  `test_coal_loader_stood_down_in_gale_demurrage_call` (PC-3103), `test_cranes_laid_up_in_gale_discharge_call` (PC-3109),
  `test_ore_loader_stood_down_in_gale_outcome_turns` (PC-3112), plus `test_quarter_summary_money_lines` ("Demurrage USD:
  73338.54") and `test_quarter_summary_counts` ("Disputed calls: 5"). All 9 other positives pass (11/39), including
  trap B, every static rule and the statements-of-facts-before-claims order.
- **Missed rubric items (round-3 rubric):** #1 r-port-weather-notes (5), #9 r-kpi-dashboard, #13 r-nor-any-time,
  #15 r-exceptions-each-call, #18 r-owners-not-source and #19 r-totals-merrow-figures (1 each), 10/26 in all. The rubric grades nothing pytest grades, so the trap miss shows in pytest.
- **Trajectory:** Box `download_file` for all 12 statements at steps 20-32; desk method read at step 12
  (`list_content` returned the §5 cause test and §6). Claim records were written at steps 54-55, LTD-6…LTD-10 at
  steps 57-61, and the summary page at step 63, so every write came after the reads.
- **Values are exactly the decoy ones.** End state: PC-3101 Despatch 3,984.38 Agreed, PC-3103 Demurrage 9,270.83,
  PC-3109 EUR 3,020.83 Agreed, PC-3112 Demurrage 1,000.00 Agreed. These are the declared `wrong_figures`, which are
  also the owners' and worksheet values. The right values are 5,000.00 Disputed, 7,187.50, 3,687.50 Disputed, and
  Despatch 1,166.67 Disputed.
- **The deciding record was reachable and returned correctly.** The four Box responses (steps 20, 23, 29, 32) contain
  "on terminal order", "gusting 9" and "Extra moorings". The model read them correctly: step 21 says "the loader
  stopped because of the wind rather than for an unrelated reason. That makes it look like genuine weather time". It
  then reversed at step 34, "That matches the owners' agreed figures … which looks like the intended treatment",
  against the instruction's "their amount is the owners' figure, and it is not evidence of anything". The judged
  harbor oracle on the same bytes scored 1.0 / 1.0 / 1.0 and passed all four wind tests.
- **Tool health:** 0 tool errors (runcheck `tool errors: 0`; playbook 2.1e: 0 server-error results). There was no
  empty discovery: `search`, `get_folder_items` (2), `list_bases`, `list_tables`, `list_records`, `list_content`,
  `list_messages` and the Jira `search` all returned data the run used.
- **Classification:** Bucket B `wrong-value-written` (playbook §2), the card's TARGET. Not guard-tripped, not
  gave-up-early.

## Appendix — simcheck raw output (batch18 + batch115)

Verbatim output of `simcheck.py` for this task, re-run 2026-11-18 on the final (FIX3_18) bytes.

```text
$ python3 simcheck.py batch18 --task af4ffc91-76d8-5138-83e5-ba2e89fbf7b0   (then batch115)
== instruction: 20 tasks, max cosine 0.096
        af4ffc91 ~ e41d6fd0: cosine 0.096, shared 6-grams 0
        a5cfe344 ~ af4ffc91: cosine 0.093, shared 6-grams 4
        936239be ~ af4ffc91: cosine 0.089, shared 6-grams 6
        94ed0c83 ~ af4ffc91: cosine 0.086, shared 6-grams 3
        54c653aa ~ af4ffc91: cosine 0.086, shared 6-grams 1
        86b00a8e ~ af4ffc91: cosine 0.083, shared 6-grams 4
        a90a31ca ~ af4ffc91: cosine 0.083, shared 6-grams 2
        af4ffc91 ~ f544cb12: cosine 0.083, shared 6-grams 0
== rubric: 20 tasks, max cosine 0.072
        a5cfe344 ~ af4ffc91: cosine 0.072, shared 6-grams 0
        936239be ~ af4ffc91: cosine 0.068, shared 6-grams 0
        94ed0c83 ~ af4ffc91: cosine 0.067, shared 6-grams 0
        86b00a8e ~ af4ffc91: cosine 0.067, shared 6-grams 0
        af4ffc91 ~ f544cb12: cosine 0.066, shared 6-grams 0
        42191a7e ~ af4ffc91: cosine 0.066, shared 6-grams 0
        87a8a5b1 ~ af4ffc91: cosine 0.063, shared 6-grams 0
        af4ffc91 ~ d7e72651: cosine 0.063, shared 6-grams 0
== pytest: 20 tasks, max cosine 0.159
        94ed0c83 ~ af4ffc91: cosine 0.159, shared 6-grams 261
        936239be ~ af4ffc91: cosine 0.156, shared 6-grams 240
        86b00a8e ~ af4ffc91: cosine 0.147, shared 6-grams 291
        af4ffc91 ~ e41d6fd0: cosine 0.146, shared 6-grams 265
        54c653aa ~ af4ffc91: cosine 0.137, shared 6-grams 226
        42191a7e ~ af4ffc91: cosine 0.135, shared 6-grams 234
        af4ffc91 ~ d7e72651: cosine 0.134, shared 6-grams 254
        af4ffc91 ~ f544cb12: cosine 0.131, shared 6-grams 116
0 flagged pair(s)

== instruction: 115 tasks, max cosine 0.065
        6d61805b ~ af4ffc91: cosine 0.065, shared 6-grams 1
        af4ffc91 ~ c3a52488: cosine 0.064, shared 6-grams 0
        af4ffc91 ~ e41d6fd0: cosine 0.064, shared 6-grams 0
        a5cfe344 ~ af4ffc91: cosine 0.063, shared 6-grams 4
        10b66495 ~ af4ffc91: cosine 0.062, shared 6-grams 0
        936239be ~ af4ffc91: cosine 0.058, shared 6-grams 6
        54c653aa ~ af4ffc91: cosine 0.058, shared 6-grams 1
        006f4954 ~ af4ffc91: cosine 0.057, shared 6-grams 0
== rubric: 115 tasks, max cosine 0.053
        8e09d104 ~ af4ffc91: cosine 0.053, shared 6-grams 0
        af4ffc91 ~ f487e5dd: cosine 0.045, shared 6-grams 0
        13444412 ~ af4ffc91: cosine 0.043, shared 6-grams 0
        a5cfe344 ~ af4ffc91: cosine 0.043, shared 6-grams 0
        6139c0bc ~ af4ffc91: cosine 0.041, shared 6-grams 0
        936239be ~ af4ffc91: cosine 0.041, shared 6-grams 0
        42191a7e ~ af4ffc91: cosine 0.041, shared 6-grams 0
        af4ffc91 ~ c3a52488: cosine 0.040, shared 6-grams 0
== pytest: 115 tasks, max cosine 0.112
        6d61805b ~ af4ffc91: cosine 0.112, shared 6-grams 259
        94ed0c83 ~ af4ffc91: cosine 0.107, shared 6-grams 261
        936239be ~ af4ffc91: cosine 0.104, shared 6-grams 240
        af4ffc91 ~ e41d6fd0: cosine 0.099, shared 6-grams 265
        86b00a8e ~ af4ffc91: cosine 0.099, shared 6-grams 291
        af4ffc91 ~ e2efdf8e: cosine 0.095, shared 6-grams 133
        54c653aa ~ af4ffc91: cosine 0.093, shared 6-grams 226
        af4ffc91 ~ d7e72651: cosine 0.089, shared 6-grams 254
0 flagged pair(s)
```
