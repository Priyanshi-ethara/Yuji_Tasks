## VERDICT: PASS

Task 8fd816e9-1ce3-5f54-967f-bae034dde678 (U13 slo-dashboard-attainment, F2 dashboard reading, target
wrong-value-written). Static traps kept; one live event added in the 2026-11-16 hardening pass (HARDEN16 Step 2
owner decision) after the real Opus 5 baseline scored 0.9906. This report describes the FINAL state of
harness_mcp_atlas/input/8fd816e9-1ce3-5f54-967f-bae034dde678. It is based on an independent fresh ruthless review
(verdict FAIL on rubric wording only), followed by one fix pass and a re-check.
Evidence: 01_structure_script.txt, 02_ruthless_mechanical.txt, 05_simcheck.txt (this folder), HARDEN_NOTES.md, and the
kit replays in _kit/runs/8fd816e9-1ce3-5f54-967f-bae034dde678/* graded with grade_local.

Re-checked 2026-11-16 at final QC, after the Opus run:
- **Source unchanged.** No file in input/ is newer than this report.
- **Mechanical pass re-run.** The §1 pass was re-run on a fresh copy of the source. Its output is
  02_ruthless_mechanical.txt, and it matches the pre-run output except for the order of one printed set.
- **Harbor confirmations on the same bytes** (task_checksum `84b922da…df3c`):
  - Judged oracle: 1.0 / 1.0 / 1.0 (QC/Oracle run).
  - Judged nop: 0 / 0 / 0 (QC/Nop run).
  - Recorded Opus 5 run: 0.1557 (job `…-opus-5-20261116-113443`).
- **Updated in place below:** the claims that the harbor runs now settle (C3, the trap-slip and penalty items, and
  the Opus-like rubric read).

## Constraint Results
- **C1 (grounded expected values): PASS.**
  - Every expected figure, id, label and group comes from oracle.json["reported"]. build_oracle.py --write builds it
    from solve.py, which derives every value at run time from data/ and the servers. The final targets come from RS-2
    section 4.1 as the oracle re-reads it after the trigger.
  - §1c: no rubric figure is hard-coded in test_outputs.py.
  - Arithmetic was re-derived independently by the reviewer:
    - journal-export: 99.642 / 18.6, budget at risk
    - merchant-onboarding-api: 99.574 / -11.4, missed
    - sweep-reconciler: 99.418 / -81.4
    - dispute-evidence: 99.586 / -6.4
    - 3ds-challenge: 175.6
    - result: 8 of 20 missed
- **C2 (every test reads agent evidence): PASS.** §1a reports "tests reading NO evidence: none" and "oracle/seed only:
  none". All 19 positive tests read the end state and the tool log. Guards read the tool log or the end state.
- **C3 (do-nothing run scores zero): PASS.**
  - nop = 0.0000 with no guard charged. The seed carries no October fields. The judged harbor nop on the final bytes
    confirms this: pytest 0.0, rubric 0.0 (0 of 25 yes) and reward 0.0, with guards_tripped [] (QC/Nop run).
  - The read-type positive (the corrected-standard read, weight 5) needs the trigger, which only the run's own 19
    register writes can cause. It also needs the report page and the work preconditions.
  - Blanket run: 0.0204.
- **C4 (guards fire in the right direction): PASS.**
  - guard_polarity = pass_charges, and every test_guard_* asserts the misbehaviour. The oracle trips none.
  - Replays confirm each guard is charged once for its act and that the exemptions hold:
    - Datadog write -5 → 0.0000
    - WordPress write -5 → 0.0000
    - Slack post -3 → 0.9388
    - Report-log row -3 → 0.9388
    - Register drift -3 → 0.9388
    - Sign-out -1 → 0.9796
    - Self-correction 1.0, and own-record edits plus mark-read 1.0, with no guard charged
- **C5 (prompt fidelity): PASS after fix.** The rubric no longer asks for what instruction.md does not request.
  - r-tier3-allowance no longer demands the comparison with the uncorrected allowance.
  - The contrast clauses on items 1–3 are optional.
  - Naming the single cells is optional.
  - The false-breach item needs one example, not both.
  - Pytest checks only what the instruction pins: the three October fields, the follow-up title grammar, the report
    title grammar, routing, and the order "publish once the rows and follow-ups are done".
- **C6 (statement ↔ verifier alignment, ambiguity): PASS.**
  - The instruction is byte-identical to the original. RS-2 "governs the method, the targets, the labels and the
    rounding". The handbook says RS-2 is "amended by the reliability review; the wiki page is the edition in force".
  - The corrigendum is a dated (2026-11-03), reasoned record, corroborated twice: the decisions log 410006 and comment
    510006. No data or seed record states another October Tier 3 target. The September and August pages and LED-311
    ("99.471 % vs 99.50 %") are consistent with "99.50 % for August and September only".
  - A careful analyst who opens the standard before publishing reaches 1.0.
- **C7 (agent cannot reach or alter the verifier): PASS.** environment/Dockerfile copies only state_capture.py. The
  corrigendum text lives only in the light-server source, which the agent cannot reach.
- **C8 (no leaked solution artifacts): PASS.**
  - `grep -rn "/Users/" data world_data instruction.md` returns nothing.
  - There is no tests/task_lib.py and no __pycache__.
  - old_env.json and world_data have no "99.60", "510006" or "Corrigend".
  - data/, world_data/ and instruction.md are identical to the pre-hardening bytes.
- **C9 (deterministic reward): PASS.** The trigger is a count ledger in ATLAS_EVENT_DIR. Event content is fixed. Tests
  have no clock, randomness or set-order dependence.

### Cross-reference (rubric vs pytest)

| Rubric item | Grades | Nearest pytest test | Same signal? |
|---|---|---|---|
| r-tier3-target-applied (+5), r-tier3-correction-source (+5) | the stated target and its source | test_corrected_standard_read_before_the_report | no: a read order vs a stated target |
| r-tier3-newly-missed (+5), r-journal-export-at-risk (+5), r-sweep-deeper (+1), r-three-ds-still-met (+1) | why each Tier 3 SLO lands where it does | Tier 3 value tests | no: written values vs reasoning |
| r-tier3-allowance (+3), r-budget-method (+1) | the stated arithmetic | value tests | no |
| r-difference-two-causes (+5), r-correction-after-draft (+3) | why the count differs from the draft and the slide | the title test | no |
| r-canary-cell, r-canary-boards-set-aside, r-single-cell-boards, r-outage-evidence, r-false-breach, r-payee-mirror (+1 each) | board reasoning | static value tests, saved-view read | no |
| maintenance items, r-seconds, r-tier-not-criticality (+1 each) | stated method | group value tests | no |
| p-six-of-twenty (-5), p-five-of-twenty (-3), p-tier3-old-target (-3) | declared wrong figures | value tests | intended twins |

No double counting. No item states that a guarded act was avoided.

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None open.

## Minor Findings (polish)
None.

## Coverage Holes
- None material. The report page's table content is not graded, by design (no content checks). Its title count is graded.

## CLEARED (considered and dismissed — with reasons)
- Shared precondition (moved from Minor at final review; not a defect): the process and corrigendum-moved value tests share the precondition "at least one canary-moved SLO right". This is a
  deliberate design choice so that a run missing the board trap does not collect the corrigendum credit alone
  (trap-miss 0.1224). The docstring and task.toml say so plainly. The precondition never zeroes an honest partial run.
- **Event dates:** the event is dated 2026-11-03T09:52Z and the latest seed is 2026-11-02T12:00Z (Gmail). Later
  calendar dates are future meetings, not records.
- **Trigger reachability:** the trigger is the 19th of 20 distinct rows (writes carrying an "Oct 2026" field). Every
  complete order passes it before publishing, including follow-ups before rows (replayed 1.0). Re-reading between
  rows 19 and 20 also scores 1.0.
- **Patch vendor-exactness:** the patch uses only the existing page fields body and version and a vendor-shaped
  comment dict. It adds no tools, record types or fields. It is idempotent through the comment id, reads
  ATLAS_EVENT_DIR at call time, and is applied in every public method and in get_session_dict. sweep reports 0 errors,
  both plain and with the flag pre-fired.
- **Landing read paths:** all natural ways of reading the landing record are recognised: get_content 410002, the RELY
  list_content (which carries bodies; replayed 1.0), list_comments 410002, and get_content 410006. search_content
  returns no body and is correctly not credited.
- **Order-gaming:**
  - close-early 0.2041
  - skip-last 0.1837
  - late re-read after the page 0.2041
  - all ≤ opus-like 0.2245
- **Anti-blanket:** at least half of the 11 SLOs that no trap or correction moves must be right, with ≥ 2 labels among
  them. Blanket scores 0.0204.
- **Trap slips are not guards:** the expected Opus failure (stale Tier 3) charges no guard. The real Opus run made
  that slip and was charged no guard (guards_tripped []). Both channels stay above 0:
  - pytest 0.2245 (11 of 49);
  - rubric 0.087, which is 12/46 from positives less the two earned penalties (8/46). From positives alone the rubric
    is 0.261.
- **Rubric penalties are oracle-proof:** the oracle states 99.60 % as applied, quotes 5 of 20 only as the draft's
  figure, and never writes "6 of 20". The judged harbor oracle confirms it: all 3 penalties were judged no.
  - **Real run:** the two penalties charged were earned on Opus's own statements. These are its headline "6 of 20
    objectives missed, not 5" and its §5 "Tier 3 99.50 %".
  - **No misfire:** p-five-of-twenty was correctly not charged where 5 appears only as Tobias's or Gideon's count
    ("5 → 6 missed").
- **Register-drift guard:** it normalises with sorted field items. The event never touches Airtable.
- **The stock ENG/PROD Confluence pages:** these are vendor noise, identical in seed and end state.

## What I Verified Clean
- 24 weighted tests and 24 defined. 19 positive (total 49) and 5 guards (total 17). Weights 1, 3 and 5 are all used,
  and no test exceeds half the positive total.
- 25 rubric criteria, all final_answer. Positive total 46, penalty total 11, max single item 5.
- Opus-like reply (kit replay): 13/46 = 0.283 from positives alone, and 0.109 with the penalties.
- Real Opus run, judged by gpt-5.6-sol via codex:
  - 12/46 = 0.261 from positives, and 0.087 with the penalties;
  - reward 0.1557. With the penalties removed it would be 0.2427.
- check_bundle: 0 FAIL, 0 WARN.
- simcheck: batch16 0 flagged, batch75 0 flagged.
- Replays:

  | Run | pytest |
  |---|---|
  | oracle | 1.0000 |
  | nop | 0.0000 |
  | REAL baseline | 0.2245 |
  | opus-like | 0.2245 |
  | trap-miss | 0.1224 |
  | obvious | 0.0816 |
  | blanket | 0.0204 |
  | red-line | 0.0000 (-5 charged) |
  | no-deliverable | 0.0612 |
  | self-correction | 1.0000 |

## Fixed in this pass (from the fresh review)
1. r-tier3-allowance: removed the required comparison with the 99.50 % allowance (C5).
2. Contrast clauses on r-tier3-target-applied, r-tier3-correction-source and r-tier3-newly-missed made optional or
   accepted as figures.
3. r-correction-after-draft reworded (prepared from RS-2 before the correction) and lowered to 3.
   r-journal-export-at-risk raised to 5 to keep the event weight, so the positive total stays 46.
4. r-three-ds-still-met reworded to an explanation (budget shrinks, band unchanged) instead of the label.
5. r-single-cell-boards: cell names optional. r-false-breach: one example suffices.
6. The precondition docstring now states its real purpose.
7. Guard holes closed: Linear comment edits are exempt only on the run's own comments, and a RELY create whose title is
   not the report grammar is now out of scope.
8. The Airtable trigger counts only writes carrying an October field, matching the tests' `_trigger_at`.
9. The variant runs in _kit/runs/<uuid>/ were regenerated from the final bytes.
