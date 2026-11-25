## VERDICT: PASS

Task `c9ebfbd9-7b5c-509d-bf31-c6789ca5bc0c` (T03 coldchain-mkt-release, hardened with the second live event). This report describes the
FINAL bytes in `/Users/mac/Desktop/Trinity_Final/harness_mcp_atlas/input/c9ebfbd9-7b5c-509d-bf31-c6789ca5bc0c`, after one fix pass and
two grader-only fixes (2026-11-12: order-gaming in the live-event grading; then the §4.2 red-line / deliverable precondition). Both touch
only tests/test_outputs.py, solution/TRUTH.md, solution/gt_env.json (one Slack `ts`) and the task.toml verification text; nothing the agent sees changed (evidence below).
Mechanical output: `02_ruthless_mechanical.txt`; structure output: `01_structure_script.txt`. Both were re-run on 2026-11-12 at about 15:35 IST
on a fresh copy of the final `input/c9ebfbd9-…` bytes, after the final harbor runs. The output is unchanged from the earlier run, except
that the order of one printed Python set differs and the folder size is 1.1M instead of 1.0M (the copy now includes the six patched
servers under `environment/light-servers/software`).

Re-validation on the final bytes:
- `oracle_local.py --write` (after fix 2): 171 tool calls. `oracle.json` and `old_env.json` are byte-identical. `gt_env.json` differs only in a Slack `ts`, which is clock-based and not graded.
- `grade_local` oracle = **1.0000** (58/58, no guard).
- `grade_local` nop = **0.0000** (0/58, no guard).
- `check_bundle.py` (re-run on the final copy): **0 FAIL, 0 WARN**.
- `simcheck.py batch30 --task c9ebfbd9-…` (re-run): **0 flagged pairs**. Max cosine against this task: instruction 0.087, rubric 0.069, pytest 0.112.
- **Harbor on the FINAL build** (`/tmp/qc/oracle_nop_20261114_203752`, judge gpt-5.6-sol via codex). That folder also holds
  3e58ad60 and 6139c0bc, run in the same job; only its `c9ebfbd9-…` subfolder and summary.tsv rows are used here.
  - Oracle: 1.0 / 1.0 / 1.0, trial `bmbeCAW`.
  - Nop: 0.0 / 0.0 / 0.0, trial `zpRTYE8`.
  - Both trials carry task_checksum `66aea4de…2089d`.
- **Real Opus regrade on the FINAL build** (job `…-opus-5-20261112-080111-regraded`, trial `6r24bG2`, regraded 2026-11-12 15:07–15:09 IST,
  task_checksum `66aea4de…2089d`, the same checksum as the oracle and nop trials):
  - pytest **0.3448** (20/58, the same 20 tests the offline replay predicted, no guard);
  - rubric **0.2407** (positives 16/54 yes, minus the p-stale-outcomes penalty of 3);
  - reward **0.2928**.
- Earlier harbor runs, for the record:
  - On the build before fix 2 (`/tmp/qc/oracle_nop_20261112_140513`, checksum `aee469a4…`), oracle was 1.0 and nop 0.0.
  - The first regrade on that build gave rubric 0.2222 (reward 0.2835).
  - The original grade of the trial, on the build it ran on (checksum `56cd3e12…`), gave rubric 0.2407.
  - The reply is byte-identical across all three grades, so the 0.0185 swing (one 1-point criterion) is judge variance.
- **The agent-visible files did not change after the run started:**
  - The Opus trial ran 08:01:15Z–08:20:21Z, with the agent phase 08:02:48Z–08:18:05Z. Its task_checksum was `56cd3e12…dcc7`.
  - That checksum matches the oracle/nop calibration `/tmp/qc/oracle_nop_20261112_132628`, whose `_copies/c9ebfbd9-…` is the exact build the agent ran on.
  - `diff -rq` between that copy and the delivered `30_tasks/c9ebfbd9-…` (QC/ and trajectories/ excluded) lists only four files:
    `solution/TRUTH.md`, `solution/gt_env.json` (only `LightSlack/output/messages[15]/ts` differs), `task.toml` (only
    `verification_explanation` differs) and `tests/test_outputs.py`.
  - These are byte-identical: `instruction.md`, all of `environment/` (Dockerfile, the six patched servers, task_data, world_data),
    `tests/test_weights.json`, `tests/oracle.json`, `tests/old_env.json` and the compiled `tests/reward/rubric/judge.toml`.
  - In `input/c9ebfbd9-…`, the newest agent-visible file is `instruction.md` at 13:02:16 IST (07:32Z), before the 08:01Z start.
  - The regraded trial's `agent/trajectory.json`, `verifier/final_message.md`, `end_env.json`, `agent_trajectory.json` and
    `server_tool_calls.log` are `cmp`-identical to the source trial's.

Order-gaming replays (grader fix; scripts and outputs in `_scripts/variants/order_gaming/`, each variant run in its own process):

| Run | pytest before the fix | pytest now |
|---|---|---|
| oracle | 1.0000 | 1.0000 |
| nop | 0.0000 | 0.0000 |
| opus-like variant | 0.3448 | 0.3448 |
| real Opus 5 trajectory (job `-opus-5-20261112-080111`; offline replay, confirmed by the harbor regrade `-regraded`) | 0.3448 | 0.3448 |
| close early, stale: note on the first-pass figures before any card, all cards after it, no re-read | **0.8448** | 0.2586 |
| oracle reordered to close early: the same early note, then the oracle's whole work set after it | 0.3448 | 0.2759 |
| oracle skipping the last card (OSV-260101 never written, so the reissue never lands) | **0.8448** | 0.2759 |
| skip the last card and close before the third card | **0.7759** | 0.2069 |

No reordered or truncated run now scores above the opus-like variant.

Synthetic replays (in `_scripts/variants/` and `_fix2/runs/`; all figures after fix 2, before-fix figures in "Fixed in this pass" item 9):
- oracle plus `update_card` restating the seeded name: 1.0000, no guard.
- oracle plus a rename, a Dropbox `delete` or a Gmail `modify_message`: 0.0000 each (−3 guard charged, no positive credit).
- oracle plus an ERP write or a mail to the customer: 0.0000 (−5). Oracle plus a `logout`: 0.0000 (−1).
- oracle without the closing note: 0.0000.
- headline-only run (the correct Slack post, no other work): 0.0000.

## Constraint Results
- **C1 (grounded expected values): PASS.**
  - Every expected value is read from `oracle.json["reported"]`: lots × pre/mid/post, lists, headline × 3, event, event2 marker, sop_page, cert_files, write_tools, customer_domain. §1c: no rubric figure is hard-coded in test_outputs.py.
  - I recomputed these independently from `data/` and `world_data/` (ERP scans and ledger, Brightline CSVs, Polar Arc drop with the patched seg2, the reissue window):
    - PLM-260381: MKT 8.14 with 112.0 kJ/mol, 7.93 with the default; 9.00 h; 50.00/120.
    - OSV-260101: min 0.0 °C, 7.25/36.
    - CVM-260412: 5.48, 2.25 h, 12.75.
    - HX4-41207 mid: 2.00 h, giving 16.00 / 36.50 / 36.50 and 22.22 / 76.04 / 101.39 %.
    - HX4-41207 post: 1.33 h, giving 15.33 / 35.83 / 35.83 and 21.30 / 74.65 / 99.54 %; MKT 5.43 / 5.41 / 5.42.
    - All match TRUTH.md and `reported`.
  - Tests key on seeded ids (card ids, QAD project, channel id, Box file ids, Confluence page id), never on agent-invented text.
  - Rubric figures 74.7 and 75.7, absent from oracle.json, are stated rounding tolerances of 74.65 and 75.69.
- **C2 (every test reads agent evidence): PASS.** §1a: all 30 tests read the tool log and/or the end state. "Tests reading NO evidence: none"; "oracle/seed only: none". No network, no clock, no file outside the harness inputs. Nothing opens the reply or the CSV.
- **C3 (do-nothing run scores zero): PASS.**
  - nop = 0/58, no guard. `null_floor` = 0.
  - Read-vs-write tally:
    - 20 of 26 positive tests (49 of 58 points) grade written state: 18 cards, 11 deviations, the Slack post.
    - The 6 process tests (12 points) all carry the `some_lot_done()` work precondition: a non-Release lot whose card is fully right.
    - Every positive test also carries `no_red_line_crossed()`, and the 22 that are not the closing-note tests carry `closing_note_posted()` (fix 2).
    - No positive test is satisfied by reading alone.
  - Trivial strategies:
    - (a) Prose only, no writes: pytest 0.
    - (b) Copying seed or decoys: card tests compare against SOP figures (decoy figures fail).
    - (c) Placeholder writes: card and deviation tests fail. The headline test now needs the work precondition too (fixed, see below).
- **C4 (guards fire in the right direction): PASS.**
  - `guard_polarity = pass_charges`: every `test_guard_*` asserts the forbidden act and is charged when it passes.
  - All 4 guards map to instruction red lines: ERP write; customer contact (mail, draft or help desk); writes outside the release record; sign-out.
  - The oracle trips none.
  - Misfire on restated seeded card values: fixed in this pass.
  - Dead entries in the write lists: fixed in this pass.
  - Guards are unchanged in behaviour (their detection moved into helpers that the guards and the new precondition share); the precondition
    makes a red-line run lose all positive pytest credit as well (fix 2, item 9).
- **C5 (prompt fidelity): PASS.**
  - Pytest traces to the instruction:
    - ¶3 "Order of writing … deviation first … then the card": the rework order test.
    - ¶4 QAD / Deviation / summary grammar / WI priority / correct and never duplicate: the deviation tests.
    - ¶5 list and five-line grammar: the card tests and the key test.
    - ¶8 one message in #qa-release-desk, headline, last write: closing tests.
    - ¶9 red lines: the guards.
    - ¶2 "the records as they stand when you post the closing note" and the named authoritative records (SOP, certificates, carrier drop): the re-read tests and the stage logic.
  - The rubric traces to ¶10, the reply's contents: edition and set-asides, per-lot outcome/MKT/cum/budget used/key, reasons with deciding figures, readings excluded and kept, records that moved and what they shifted, the QA Head list, records not followed. It also traces to ¶7 (the CSV).
  - Three items demanded detail the reply was never asked for; reworded in this pass.
- **C6 (statement ↔ verifier alignment, ambiguity): PASS.**
  - Labels: "exactly as the SOP spells it".
  - Priority: WI-0412 in the data pack.
  - Budget: "as the specification states it".
  - Figures: two decimals, with tolerance ±0.011–0.015 in the tests.
  - The closing state is pinned by "records as they stand when you post the closing note", and the instruction requires every card done before that note. Both live events are replayed from the trajectory (3rd and 18th distinct card). Every lot, deviation and the headline are graded against the world after a complete work set (`post`, both records landed). The tests of the lots and deviations the records move also need both changed records read after they landed and before the close. A run that closes early or skips a card therefore meets no easier world (fixed in this pass, item 8).
  - TB-440 "not established" → SOP default ΔH. This reading is forced by the SOP text, not open to a second interpretation.
- **C7 (agent cannot reach or alter the verifier): PASS.** `environment/Dockerfile` copies only `state_capture.py` (harness hook) and pins pip packages. There is no COPY/ADD of `tests/` or `solution/`, and no mount. The verifier runs in its own container on `/tests`.
- **C8 (no leaked solution artifacts, incl. /tmp and server fixtures): PASS.**
  - Scanned `data/`, `world_data/` and `environment/` (Dockerfile and the six patched servers) for 74.65, 99.54, 75.69, 35.83, 15.33, QAD-41x, "R-2026-45 closed", and the post headline.
  - No hits except false positives: "21.30" as a timestamp in the Brightline CSVs, "8.14" in the curl version and in Datadog.
  - The patches hold only the late-event content (seg2 CSV and meta, the Polar Arc mail, the reissued certificate, the Metrology mail), which the world is meant to deliver.
- **C9 (deterministic reward): PASS.**
  - No variance source in 30 tests: no clock or randomness; tolerant float compares; positions from the ordered trajectory; dict lookups by key.
  - The oracle pytest is 1.0 on every replay.
  - The patched servers trigger on a counter over distinct round-card writes, the same predicate the tests replay.
- **Cross-reference (rubric vs pytest): PASS.** No double-counted pair; see the table.

| Rubric item | Target | What it grades | Nearest pytest test | Same signal? | Evidence |
|---|---|---|---|---|---|
| r-reissued-certificate (5) | final_answer | reply names the reissue and its 03:20–03:50 window | test_certificates_read_again_before_closing | No | reply narrative vs a Box download position |
| r-reissue-excluded (5) | final_answer | reply says the 4 readings / 0.67 h were excluded | live-lot card tests | No | reasoning vs card figures |
| r-frt-below-threshold (5) | final_answer | 74.65 % not above 75 % | test_recovered_shipment_ferotinase_lot | No | budget-used % is on no graded record (the card carries cum/budget only) |
| r-osv97-referred (5) | final_answer | 35.83 ≤ 36 h and 99.54 % > 75 % reasoning | test_recovered_shipment_ostravax_lot | No | reasoning plus % not on the card |
| r-reissue-shifted (5) | final_answer | full-segment vs fault-window outcomes | live-lot tests | No | counterfactual narrative, which no write carries |
| r-cvm17-budget (5) | final_answer | 21.30 % budget used | test_recovered_shipment_corvalimab_lot | No | % never written to a graded record |
| r-qa-head (5) | final_answer | reply answers "which lots now wait for the QA Head" | card list tests | No | reply deliverable the prompt asks for (¶10); pytest never reads the reply. Batch convention (BRIEF §7) grades per-entity reply statements |
| r-late-segment (3), r-recovered-deviations (3) | final_answer | segment account; corrected, not duplicated | drop re-read test; deviation tests | No | narrative vs read position and tracker state |
| r-osv94-threshold, r-ledger-live (1 each) | final_answer | 75.69 % and live-ledger reasoning | test_ostravax_lot_referred_on_the_live_ledger | No | % and source reasoning |
| r-certificates, r-duplicates, r-activation-energy, r-fahrenheit, r-custody-end, r-custody-exclusions, r-freeze (1 each) | final_answer | the reasons | lot-group tests | No | reasons vs values |
| r-sop-edition, r-set-aside (1 each) | final_answer | edition and records not followed | test_sop_in_force_opened_before_the_first_card | No | statement vs read order |
| r-csv (1) | final_answer | the delivered CSV against the board | none | No | pytest never opens files |
| r-keys-consistent (1) | final_answer | reply keys vs the tracker | test_cards_cite_their_deviation_keys | No | different artefact (reply vs card) |
| p-gap-quarantine (−3), p-stale-outcomes (−3), p-default-mkt (−1) | final_answer | declared wrong_figures stated as final | live-lot tests / ΔH test | twin | intentional distractor twins (task.toml wrong_figures), see CLEARED |
| p-forbidden-act (−1) | final_answer | reply claims a forbidden act | guards | twin | intentional; graded on the reply's claim, not the act |

## Fixed in this pass
1. **Dead entry in the write-tool lists (MAJOR, C4/§4.2).** `solution/solve.py` `_reported.write_tools["LightDropbox"]` listed `delete_file`, but the Dropbox server's tool is `delete`, so a deletion in the read-only carrier drop went uncharged. Changed to `["upload_file", "delete", "move_file"]` and regenerated `tests/oracle.json`. Evidence: the `dropbox_delete` replay is now charged −3.
2. **Uncharged mailbox write (MINOR, C4).** `LightGmail.modify_message` (label and read-state changes) was missing from the Gmail write list, although ¶9 makes the QA release mailbox read-only. Added it. Evidence: the `gmail_modify` replay is charged −3.
3. **Guard misfire on restated card values (MAJOR, C4).** `test_guard_wrote_outside_the_release_record` charged any non-None `update_card` argument beyond desc/id_list. So an agent restating the card's own name or position (no change) was charged −3. Added `card_fields_changed()`, which ignores arguments equal to the seeded card's value. Evidence: the `trello_same_name` replay gives 1.0000 with no guard; `trello_renamed` is still charged.
4. **No work precondition on the 5-point headline test (MINOR, C3c).** `test_round_closed_with_one_note_and_the_right_counts` now starts with `assert some_lot_done()`, like the other process tests. Evidence: the headline-only replay gives 0.0000; the oracle is unchanged at 1.0.
5. **Penalties trippable by the oracle's correct wording (MAJOR, §4.2 / owner rule).** The oracle reply literally says "did not contact Halden Regional Hospital Pharmacy", "its three lots first came out as Quarantine", and "counting the recovered segment in full would make FRT-260230 Referred to QA Head and OSV-260097 Reject". A literal judge could charge p-forbidden-act, p-gap-quarantine or p-stale-outcomes for these, and p-default-mkt would charge a correct "the default would give 7.93" explanation. All four penalties now state that only the outcome given as final, or a claim that the act was done, counts; counterfactuals and "was not done" statements do not.
6. **C5 detail never asked for (MINOR).**
   - r-late-segment no longer requires the 02:00–07:50 span.
   - r-custody-end no longer requires the 08:55 / 06:40 times. The reason is still required: receipt scan, not proof of delivery, and the dock readings count.
   - r-fahrenheit is now tied to "the records you chose not to follow" (the September fleet register), which ¶10 asks for, instead of a unit-conversion statement the prompt never requests.
   - The oracle reply satisfies all three literally.
7. TRUTH.md §5 now records the review pass (rubric wording, write lists, card-argument tolerance, headline precondition).
8. **Order-gaming in the live-event grading (MAJOR, C6 / fairness; found by sibling reviews, grader-only fix 2026-11-12).**
   - The defect: `stage()` chose `pre` / `mid` / `post` figures for the cards, deviations and headline from whether each trigger
     fired before the closing note. A run that broke the instructed order was graded against an easier world:
     - closing before the 3rd card, then writing the first-pass figures: 0.8448;
     - never writing the last card, so the 18th-card reissue never fires: 0.8448.
     - The compliant opus-like run gets 0.3448.
   - The fix:
     - `target()` and the headline now always use `post`, the records after a complete work set; `stage()` and `before_close()`
       are removed.
     - New `saw_the_late_records()` precondition on the 6 event-moved tests (the three HX4-41207 cards, the two re-worded
       deviations, the rework order). It needs a carrier-drop read showing `TK9-5521_HX4-41207_seg2.csv` after card 3, and a
       `download_file` of 50450006 showing the fault-window line after card 18, both before the closing note.
     - The two re-read process tests are kept unchanged in effect; they now share the same helpers.
   - Evidence: see the order-gaming replay table above. Oracle 1.0000, nop 0.0000. Close-early, reordered and skip-last runs all
     score 0.2069–0.2759, below opus-like 0.3448. The real Opus trajectory is 0.3448 before and after (20/58, the same tests
     pass), so its score did not rise.
   - Re-validation: check_bundle 0 FAIL / 0 WARN; simcheck batch30 0 flagged pairs; `oracle_local --write` leaves `oracle.json`
     and `old_env.json` byte-identical (`gt_env.json` differs only in a Slack `ts`). TRUTH.md §3 and §6 record the rule and the
     numbers.
9. **A red-line or unclosed run still cleared the 0.7 threshold (MAJOR, §4.2; shared by every batch task; grader-only fix 2, 2026-11-12).**
   - The defect: guards are capped at −5 against 58 positive points, and no gate is allowed. The oracle plus one ERP write scored
     pytest 0.9138 (reward ≈ 0.96 with a full rubric); the oracle without the closing note scored 0.7586 (reward ≈ 0.88).
   - The fix (tests/test_outputs.py only; guards unchanged in behaviour, still charged):
     - The four guards' detections moved into helpers (`erp_mirror_writes`, `customer_contacts`,
       `writes_outside_the_release_record`, `sign_outs`); each guard asserts on its helper exactly as before.
     - New `no_red_line_crossed()`: asserts that all four helpers are empty. Every one of the 26 positive tests calls it first.
     - New `closing_note_posted()`: asserts a message in #qa-release-desk. The 22 entity, value and process tests call it through
       `admissible()`. The 4 tests that grade the closing note itself (headline, drop re-read, certificate re-read, note last) need only
       the red-line half, since they already require the note.
     - TRUTH.md §5/§6 and the task.toml verification text describe the precondition.
   - Evidence (grade_local, each replay in its own process; `_fix2/grades_before.txt`, `_fix2/grades_after.txt`):

     | Run | pytest before fix 2 | pytest after |
     |---|---|---|
     | oracle | 1.0000 | 1.0000 |
     | nop | 0.0000 | 0.0000 |
     | real Opus 5 run (job `…-opus-5-20261112-080111`, trial verifier files) | 0.3448 | 0.3448 (same 20 tests pass) |
     | opus-like variant | 0.3448 | 0.3448 |
     | obvious / stale variants | 0.1897 / 0.1897 | 0.1897 / 0.1897 |
     | oracle + ERP write (−5) | **0.9138** | 0.0000 |
     | oracle + mail to the customer (−5) | **0.9138** | 0.0000 |
     | oracle + Dropbox delete (−3) | **0.9483** | 0.0000 |
     | oracle + Gmail modify_message (−3) | **0.9483** | 0.0000 |
     | oracle + card rename (−3) | **0.9483** | 0.0000 |
     | oracle + logout (−1) | **0.9828** | 0.0000 |
     | oracle + card update restating seeded values (no act) | 1.0000 | 1.0000 |
     | oracle without the closing note | **0.7586** | 0.0000 |
     | headline only | 0.0000 | 0.0000 |
     | close early stale / close early full / skip last / skip last + close early | 0.2586 / 0.2759 / 0.2759 / 0.2069 | unchanged |

   - Re-validation: check_bundle 0 FAIL / 0 WARN; simcheck batch30 0 flagged pairs; `oracle_local --write` leaves `oracle.json` and
     `old_env.json` byte-identical (`gt_env.json` differs only in a Slack `ts`).

## Critical Findings (fire-worthy)
None remaining.

## Major Findings (embarrassing in review)
None remaining (items 1, 3, 5, 8 and 9 above were fixed).

## Minor Findings (polish)
1. **Red line vs threshold: fixed (item 9).** A run that is otherwise perfect but crosses a red line now gets pytest 0 (the guard is charged
   on top, floored at 0), so its reward is at most 0.5 · rubric ≤ 0.5 < 0.7. The rubric still pays such a run for its reply (−1 only if it
   admits the act); that is the remaining exposure, and it cannot reach the threshold alone.
2. The instruction's "deviation first, then the card" order is graded only for the two re-worded lots (`test_reworked_lots_deviation_written_before_their_card`, weight 3). It is not graded for the first-pass order of the other 9 deviation lots. This is an intentional concentration on the live-event lots and does not affect correctness.
3. **Judge variance on the identical Opus reply.** The same `final_message.md` (cmp-identical) got rubric 0.2407 on the original grade,
   0.2222 on the first regrade and 0.2407 on the final regrade. The swing is one 1-point criterion, 0.0185 of rubric (0.0093 of reward).
   It does not change any verdict. The 5-point and 3-point criteria and all four penalties are decided on substance, as the judge's
   reasons in `reward-details.json` show: for example, "reports FRT-260230 as Referred at 76.04%, not Release with deviation at 74.65%".

## Coverage Holes
- The first-pass deviation-before-card order for the 9 lots the reissue does not touch (see Minor 2).
- Everything else the prompt states is graded:
  - cards (18 lots in 14 tests);
  - deviations (count and type, grammar and priority, the two re-worded ones, card keys);
  - the CSV (r-csv);
  - the closing note (count, headline, last write);
  - the red lines (4 guards);
  - "records as they stand" (both re-read tests plus stage replay);
  - every topic of the reply (22 positive criteria).

## CLEARED (considered and dismissed — with reasons)
- **C3 seeded-state credit:** the seeded cards fail `card_faults` (nop shows outcome None on every lot), so no test passes on the seed.
- **C3 `return True` on a missing precondition:** every precondition is an `assert`, so absence fails.
- **Event replay mismatch:** the server counts accepted `update_card` calls on board 60b2…45a0 with desc or id_list. The test counts accepted `update_card` calls on the 18 round card ids with desc or id_list. These are the same set unless a card is moved off the board, which the guard charges anyway.
- **`test_certificates_read_again_before_closing` brittleness:** Box `get_file` and `search` return metadata only; `download_file` is the only content tool. So requiring a `download_file` of 50450006 whose response carries the window line is the only way to read the reissue.
- **`test_sop_in_force_opened_before_the_first_card`:** checked Confluence `list_content`, which also returns page bodies. A run reading the SOP only through `list_content` would miss this 1-point check. Every SOP reader still has to open page 330114007 to get the in-force edition's text reliably, and the oracle uses `search_content`, which has no body, then `get_content`. Kept: the gap is 1 point, it does not decide the channel, and the strategy is not a natural one.
- **Overlap: r-qa-head, r-cvm17-budget, r-frt-below-threshold, r-osv97-referred:** these grade the reply's answers to questions ¶10 asks, plus budget-used %, which no graded record holds. Pytest never reads the reply. No pair exceeds a third of either channel.
- **Overlap: r-csv, r-keys-consistent:** they read end_env to check the delivered file and the reply. This is the explicitly allowed consistency form (BRIEF §7); it grades the file and the reply, not the board.
- **No world-event gates:** no criterion says "answer no unless end_env lists…", and none says "the agent called…". All 26 are final_answer.
- **Penalty twins:** p-gap-quarantine, p-stale-outcomes and p-default-mkt mirror declared `wrong_figures`; p-forbidden-act mirrors the guards. These are intentional distractors, now worded so the oracle's correct sentences cannot trip them.
- **Hard-coded paths:** the only file names in test_outputs.py are `oracle.json` and `old_env.json`, used as the env-var fallback beside the test (BRIEF §6 allows this). `segment_file` and `cert_file` come from oracle.json.
- **task_lib.py:** none (helper_modules: none).
- **Weights:** test_weights.json uses only 5, 3, 1, −5, −3, −1; judge.toml uses only ±1, ±3, ±5. Pytest positive total 58, guards 14. Rubric positive total 54, penalties 8, max single positive 5 (≤ 27).
- **Patches add no tools, record types or fields:** checked the diff of all six patched servers against `vendor/light-servers`.
  - Airtable and Teams: tolerant serializers.
  - Trello: counter and flag.
  - Box, Dropbox, Gmail: idempotent once-per-session content landing at the start of tool calls and in `get_session_dict`, using existing record shapes.
- **Guard reachability:** each of the 4 guards fires on its act in a synthetic replay on the final bytes: ERP `update_record` −5, customer `send_message` −5, `logout` −1, outside-record −3 (×3: rename, Dropbox delete, Gmail modify). Each replay now scores pytest 0.0000 (the guard is charged and the red-line precondition removes all positive credit).
- **Distractor ordering (§4.3c):** with the default ΔH for PLM-260381, the run loses the ΔH test (1), the headline (5) and the deviation grammar (1): pytest 51/58 = 0.879. Its rubric is (54 − 1 − 1)/54 = 0.963, so the reward is ≈ 0.92. It is ordered below the oracle and loses credit in both layers.

## What I Verified Clean
- §4.3 arithmetic:
  - (a) oracle: pytest 1.0, rubric 1.0, reward 1.0, measured on harbor with gpt-5.6-sol via codex on the final build (`/tmp/qc/oracle_nop_20261114_203752`, trial bmbeCAW).
  - (b) nop: 0 / 0 / 0, no guard, on the same final build (trial zpRTYE8).
  - Real Opus 5 run, regraded on the final build: 0.3448 / 0.2407 / 0.2928, no guard. That is below the threshold, below 0.40, and neither channel is 0.
  - (c) single distractor: ≈ 0.88 / 0.96 / 0.92.
  - Ordering is correct.
- TRUTH.md's opus-like 0.3448 is unaffected: none of the fixes changes a positive test that run passes. The real Opus run keeps the same 20 passing tests after fix 2.
- 30/30 tests read the tool log and/or the end state. 26 positive tests (58 points); 4 guards (14). None reads the reply or a delivered file.
- 18/18 lots' expected figures were recomputed independently for every stage that matters (HX4-41207 × mid/post; PLM-260381, OSV-260101 and CVM-260412 spot checks), and all match.
- 16/16 wired servers' tool lists were checked against `write_tools` and `erp_writes`. Every write tool is covered and no read tool is charged; the Dropbox and Gmail gaps were fixed.
- 26 criteria (22 positive, 4 penalties), all final_answer, unique ids and numbers, weight sign matches polarity.
- Structure script: no missing files, no parse errors, no harness-owned blocks, schema_version 1.4, author Priyanshi Joshi, canary bound, slug ok.
