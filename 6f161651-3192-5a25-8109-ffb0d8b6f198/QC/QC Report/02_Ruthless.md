## VERDICT: PASS

Task 6f161651-3192-5a25-8109-ffb0d8b6f198 (U10 submission-toc-versions, LIVE, R6 Index / glossary / ToC completeness).
This was a fresh independent review: one fix pass, then re-validation. The post-run QC (QC_FINAL16) added two grader-only
fixes, Fixed 7 and Fixed 8, to judge.toml. This report describes the final state of the bundle (task_checksum
`df81ab49…8b50`).

Mechanical output is in the same folder: 01_structure_script.txt, 02_ruthless_mechanical.txt and 05_simcheck.txt.
§1 was re-run on the final bytes. The only change is criteria 20 and 22, whose text now carries the Fixed 8 carve-outs.

Harbor evidence on the final bytes:
- oracle 1.0/1.0/1.0 and nop 0/0/0, judge gpt-5.6-sol via codex (`/tmp/qc/oracle_nop_20261116_160552`, copied to
  QC/Oracle run and QC/Nop run);
- the recorded Opus run regraded to reward 0.1996 (pytest 0.1864, rubric 0.2128), with no guard and no penalty charged.

## Constraint Results
- C1 (grounded expected values): PASS. Every expected value comes from `oracle.json["reported"]` through `ref()`: rows, mail
  figures, markers, sections, the director's address, tool lists. §1c reports that no rubric figure is hard-coded in
  test_outputs.py. Section ids (S13, S22) are seeded record keys, not answer figures. I checked the arithmetic myself:
  23 distinct documents with a version in force, DOC-1047 counted once, add up to 784. Before event 2 the total is 771
  (−6 for DOC-1047 Rev E, −7 for DOC-1188 Rev B), and with neither event it is 767 (−4 for S07 Rev F). Counts are
  23/3/4 (22/4/4 before event 2). Tests key on seeded ids (record ids, base/table id, `db-ks3-term-index`, project
  KTF) and on the instruction's fixed grammar (`TF-GAP <Sxx>`, the subject template, the title template).
- C2 (every test reads agent evidence): PASS. In the §1a table all 21 positive tests read the end state and the tool
  log (plus oracle and seed), and the 5 guards read the tool log. No test reads only the oracle or the seed.
- C3 (do-nothing run scores zero): PASS. The nop replay scores 0.0000 with no guard charged, and `null_floor` = 0. Every
  positive test calls `gate_values()`: a clean run plus the anti-blanket spread, meaning at least half the routine rows
  right plus one right Gap row and one right N/A row. Trivial strategies: blanket 0.0000, obvious (Ines's draft copied)
  0.0508, prose only with no writes 0. Read vs write tally: one positive test (5) is a process read
  (`test_store_rechecked_after_the_late_release`). It also needs the ToC written, the mail sent and a clean run, so
  browsing alone earns nothing.
- C4 (guards fire in the right direction): PASS. `guard_polarity = pass_charges`, and every `test_guard_*` asserts that
  the act was found. In the red-line replay (one DocuSign update_envelope) the −5 guard is charged and pytest is 0. The
  oracle and the self-correction replay (wrong S13 row first, then a wrong index page deleted) charge nothing. Built-in
  exemptions: the run's own Notion pages and blocks, its own Jira issues, Outlook mark-read (update_message without
  subject), Gmail modify_message (not in the list), ToC fields re-written to their seeded value, and the OpenHands
  `summary` argument (never read). Every guarded act is forbidden in words in the instruction.
- C5 (prompt fidelity): PASS (after the fix pass). Every rubric item traces to a reply bullet: "the revision you cite
  … and the record that makes it the version in force", "every row where you depart from Ines's working draft, and
  which record made you depart", "the not-applicable sections, each with its reason", "the gaps, each with the reason",
  "how you arrived at the page total", "which glossary terms you left out … and why", "anything document control needs
  to pick up". No item now asks for timing ("while the work was under way"), a before/after delta or a counterfactual
  (see Fixed). The post-trigger read test traces to the standard. §2.5 says "The controlled store and change control
  are updated as releases happen"; §7.1 says the gap tickets are "raised once the ToC is complete"; §8.1 says the
  readiness statement goes out "when the ToC, the index and the gap list are in place … P the file page total of 4.9
  … the last act of the compilation". The submission hub and the instruction name the store and ServiceNow as
  sources. Any honest run that states the version in force when it closes must look at the store or the change
  request after its ToC writes. Nothing in the instruction, data or seeds cues a re-check. "I'd rather have it right
  than fast" is generic, and the QA note "look at the change request, not at the register, for anything released
  since the last sync" is a rule about which source governs, not a timing cue.
- C6 (statement ↔ verifier alignment, ambiguity): PASS (after the fix pass).
  Event 1 originally created a contradiction in the standard; rule 4.3 is now fixed (see Fixed).
  After event 2 the state is unambiguous. The store holds DOC-1047 v6 "Rev F | released 2026-11-16 under CHG0041187 |
  52 pp | open placeholders: 0" and DOC-1188 v3 "Rev C | … | 31 pp | open placeholders: 0". ServiceNow CHG0041187 is
  state Closed and "implemented 2026-11-16 09:40". The register has no item for either revision, so neither is In
  approval, Draft or withdrawn, and 4.3/4.4 cannot bite. 4.2(b) ("released into the store under a change request that
  change control shows closed as implemented; the register entry for such a release follows at the next sync") makes
  both revisions the version in force. QA-SOP-007 6.4, the register sync note, Outlook msg 0002 (sync postponed to
  20 Nov), the Teams/Slack messages (sync skipped) and document-control-config.yaml (next_sync 2026-11-20) all
  corroborate this. The static S20 trap (CHG0041102, register still at Rev B) teaches the same rule.
  No seed record contradicts the post-event answer. The Slack message "won't make this submission" is a dated
  prediction, and §2.5 says chat messages are not records. Mateus's mail ("CCB 13 Nov, timing depends on Pieter")
  and Yuki's Slack/Outlook notes ("Rev C closes both placeholders") agree with the release. The register's Rev E and
  Rev B entries are still "Approved", which is consistent with "highest approved revision".
  One residual point is not a hit: CHG0041187 says QA (R. Montoya) released it while document control is on leave.
  4.2(b) and SOP 6.4 key on the closed change request, not on who released it, and SOP 6.2 gives QA authority.
  The labels, the "None in force" and "N/A" grammar, the title and subject templates and the TF-GAP prefix are all
  pinned in the instruction.
- C7 (agent cannot reach or alter the verifier): PASS. environment/Dockerfile copies only `state_capture.py` to
  /harness/atlas. There is no COPY or ADD of tests/ or solution/, and the light-servers patches hold no grader code.
- C8 (no leaked solution artifacts): PASS. I scanned data/ (36 files), world_data/ (15 seeds), instruction.md, the
  Dockerfile and the 8 patched modules. CHG0041187, v_KS3_1047_6, 784 and "23 complete" appear nowhere outside the
  patched Drive and ServiceNow event blocks, which fire only after the 29th row. `tests/old_env.json` has 0 hits for
  v_KS3_1047_6, CHG0041187 and 2026-11-16T08:52. `grep -rn "/Users/" data world_data instruction.md` is empty.
- C9 (deterministic reward): PASS. None in 26 tests: sets are sorted before comparing, there is no clock, network or
  randomness, and order is decided by trajectory step indexes. The oracle replays to 59/59 every time.
- Cross-reference (rubric vs pytest): no double-counted pair; see the table below.

| Rubric item | Target | What it grades | Nearest pytest test | Same signal? | Evidence |
|---|---|---|---|---|---|
| r-s13-released-revision (+5) | final_answer | why S13 cites Rev F not Rev E (released into the store) | test_risk_report_row_carries_the_late_revision | no | reason vs row value |
| r-s14-shared-document (+5) | final_answer | why S14 follows S13 (same document) | test_benefit_risk_row_follows_the_shared_report | no | reason vs row value |
| r-s22-released-revision (+5) | final_answer | why S22 cites Rev C not Rev B | test_stability_row_cites_the_late_revision | no | reason vs row value |
| r-change-request-evidence (+5) | final_answer | names CHG0041187 as the record making Rev F/Rev C in force | test_store_rechecked_after_the_late_release | no | stated evidence vs read step |
| r-page-total-counts-releases (+5) | final_answer | page-total account includes the two releases | test_readiness_page_total | no | method vs subject figure |
| r-register-lag-reasoning (+3) | final_answer | why the releases count though the register lags | none | — | — |
| r-s22-no-open-placeholder (+3) | final_answer | reason S22 is Complete (no open placeholder) | test_stability_row_no_longer_a_gap | no | reason vs label |
| r-register-follow-up (+3) | final_answer | document-control follow-up (register must record Rev F/Rev C) | none | — | advice only; the item no longer mentions the agent's own register writes (see Fixed 7) |
| r-ifu-approval-completed (+3) | final_answer | why S07 cites Rev G (approval completed) | test_ifu_row_follows_the_completed_approval | no | reason vs row value |
| r-not-applicable-reasons (+1) | final_answer | reason for each N/A section | test_excluded_sections_marked_not_applicable | no | reasons vs labels |
| r-lookalikes-stay-in (+1) | final_answer | why S25/S30 stay in | test_near_patient_and_ssp_rows_stay_in | no | reasons vs rows |
| r-s15 / r-s20 (+1 each) | final_answer | why those revisions | matching row tests | no | reasons vs rows |
| r-s17-usability-number (+1) | final_answer | why S17 departs from the draft (1074 vs 1047) | test_usability_row_cites_its_own_number | no | reason vs row value |
| r-s16 / r-s23 / r-s29 (+1 each) | final_answer | reason for each gap | row tests / test_gap_tickets_for_the_standing_gaps | no | reason vs label/ticket |
| r-shared-document-counted-once (+1) | final_answer | page-total method | test_readiness_page_total | no | method vs figure |
| r-index-left-out (+1) | final_answer | excluded terms + reasons | test_term_index_entries | no | reasons vs pages created |
| r-pen-* (−3, −3, −1) | final_answer | 828 / 771-as-final / S30 N/A in the reply | none | — | intentional distractor twins (all declared in wrong_figures) |

## Critical Findings (fire-worthy)
None remaining.

## Major Findings (embarrassing in review)
None remaining. The six found in this review are fixed; see "Fixed in this pass".

## Minor Findings (polish)
None remaining. Leftover observations are listed under CLEARED.

## Fixed in this pass
1. [world_data/LightConfluence.json, page 410001, rule 4.3]: C6 contradiction on event 1 (MAJOR). After the first ToC
   row, the register shows DOC-1133 Rev G "Approved" and the envelope reads completed, but the store entry
   v_KS3_1133_7 still reads "Rev G | routed for approval". The old 4.3 said "A revision that the store records as
   routed for approval … is not approved, whatever its page count or content", which directly contradicted 4.2(a)
   for the S07 answer (Rev G, 68 pp, test weight 3, rubric 3). Two careful readers could write Rev F or Rev G. New
   4.3: "A revision that the register shows as In approval or Draft, or that the store records as a working draft,
   is not approved, whatever its page count or content. A revision the store records as routed for approval is not
   approved until the register shows it as Approved (4.2(a))." This matches QA-SOP-007 6.6 and the IFU routing note,
   and it is exactly the logic solve.py `_in_force` already applied. S15 (register In approval) and S23 (working
   draft) are unaffected.
2. [tests/judge.toml items 1, 3, 5, 7, 9]: C5 over-specification (MAJOR). These items demanded detail the instruction
   never asks the reply for. Items 1, 3 and 9 required "moved while the work was under way". Item 5 required the
   "+13 pages" delta or "771 before / 784 after". Item 7 required the counterfactual "three gaps where there would
   otherwise have been four". A compliant reply that answers the instruction's bullets ("departures from the draft
   and the record", "how you arrived at the page total") could fail all five (21 of 47 positive points). Reworded:
   - items 1, 3 and 9 now grade why S13, S22 and S07 cite the new revision (released into the store, or approval
     completed), with timing explicitly optional;
   - item 5 grades a page-total account that includes the two releases (a delta is one accepted way, not the only one);
   - item 7 now grades the reason S22 is Complete (Rev C records no open placeholder).
   Ids were renamed to match: r-s13-released-revision, r-s22-released-revision, r-page-total-counts-releases,
   r-s22-no-open-placeholder. Item 6 no longer reads as requiring "rule 4.2(b)": "No rule or clause number is
   required."
3. [tests/judge.toml items 10, 14]: strict rubric↔pytest overlap (MAJOR). Item 14 ("S17 cites DOC-1074 … not
   DOC-1047") restated the end-state value that `test_usability_row_cites_its_own_number` grades. Item 10 opened by
   restating the N/A labels. Item 14 now grades the reason (the usability file is DOC-1074; DOC-1047 in the draft is
   the risk report). Item 10 now grades only the reasons.
4. [tests/test_outputs.py `saw_register_change`]: the S07 test, which event 1 moves, did not require the closing
   deliverable (MAJOR, BRIEF_ADDENDUM2 grader-integrity rule). With no mail, its read window was open-ended. A run
   that skipped the readiness mail therefore scored exactly the same as a compliant stale run (both 14/59 = 0.2373),
   so the closing mail carried no weight for a stale run. The S07 read must now fall between the first ToC row and
   the readiness mail. Result: no-deliverable 0.1864, opus-like without the mail 0.1864, and opus-like with the mail
   0.2373.
5. [tests/test_outputs.py + test_weights.json]: coverage hole (MINOR). The subject's `<N> not applicable` figure was
   parsed but graded nowhere. `test_readiness_gap_count` is now `test_readiness_gap_and_na_counts` and checks the gap
   and N/A figures. Its weight stays 5 and its preconditions are unchanged.
6. [task.toml wrong_figures]: the penalty r-pen-ssp-excluded ("S30 not applicable") was not declared (MINOR; the owner
   rule allows penalties only for declared wrong figures). Added the declared value "S30 … given as not applicable -
   the Edition 2 class-D-only reading in the working draft and Slack". The verification_explanation and
   TRUTH.md (severity rule, cross-reference, expected scores) were updated to the final design.
7. [tests/judge.toml item 8, r-register-follow-up]: strict overlap with a guard (MAJOR, QC_FINAL16 step 2b). The item
   ended "and it does not claim that the agent recorded them in the register itself". That clause grades the agent's
   own register write, the act `test_guard_approved_or_restatused_a_document` (−5) already charges. The clause is
   removed. The item now grades only the follow-up advice: the register still has to record DOC-1047 Rev F and
   DOC-1188 Rev C, for example at the next sync. The oracle reply earns it ("For document control to pick up: the
   register still needs to record DOC-1047 Rev F and DOC-1188 Rev C … at the next sync", solve.py L437–439).
   TRUTH.md §6 was updated to match. This is a grader-only change: the recorded Opus run was regraded on the new
   bytes, and harbor oracle/nop were re-run (QC/Oracle run, QC/Nop run).
8. [tests/judge.toml items 20 and 22, r-pen-working-draft-total and r-pen-ssp-excluded]: penalty misfire on a quoted
   figure (MAJOR, judge literalness). The instruction asks for "every row where you depart from Ines's working draft".
   A compliant reply therefore quotes the draft's own values. In the recorded Opus run the judge charged item 20
   (−3) twice, citing "The departures table explicitly gives Ines's total as '828 pp.'" The row it read was
   `| Totals | 828 pp; 22/2/6 | **767 pp; 22/4/4** |` (Ines column vs the reply's own), and the reply's own total
   was 767. Item 20 now ends "Quoting 828 only as the working draft's own total, for example in a comparison of the
   draft with the reply's total, is not this."
   I checked the other penalties for the same pattern. Item 22 (S30 not applicable) had the same exposure, because
   the departures table lists Ines's S30 as N/A. It now ends "Reporting only that Ines's working draft or someone
   else marked S30 not applicable, while the reply itself keeps S30 applicable, is not this." Item 21 already carries
   a carve-out ("Mentioning 771 only as the total before the late releases is not this"), and 771 is nobody's quoted
   figure, so it is unchanged.
   The oracle reply never mentions 828 and keeps S30 applicable (solve.py L419), so it trips none of the three
   penalties. TRUTH.md §5 was updated to match. Grader-only: the recorded run was regraded (rg2), and harbor
   oracle/nop were re-run on the final bytes.

## Coverage Holes
- None. Each deliverable is graded:
  - the 30 rows' four fields, per trapped row and grouped for routine rows;
  - the 16 index titles;
  - one TF-GAP ticket per gap, and no S22 ticket;
  - the subject's C, G, N and P figures;
  - the four red lines, the sign-out rule and the "only these four places" rule (guards);
  - the reply's eight bullets (rubric).
- Not graded on purpose: the free-text Notes field, the ticket summary and the mail body. The instruction leaves
  these free.

## CLEARED (considered and dismissed — with reasons)
- Patches vendor-exact: I diffed all 8 modules against harness_mcp_atlas/vendor/light-servers/software.
  - Every addition is either the commented "TASK WORLD RULE" block (helpers, a `__getattribute__` hook calling
    `_tw_apply`, the Airtable row ledger) or a line marked `# task-layer fix`.
  - No new tools, record types or fields. Drive adds `Version(vid, file_id, version_number, size_bytes, created_at,
    comment)` and sets the existing File fields. ServiceNow appends a change dict with exactly the seeded change keys.
    Monday changes `group_id` and column `text`. DocuSign changes `status`, `completed_time` and `signed_time`.
  - ATLAS_EVENT_DIR is read on each call (`_tw_dir()`).
  - Every patch is idempotent: an `_tw_ev*` flag in `__dict__`, flag files, ServiceNow's duplicate check, and
    assignment-only updates. `_tw_ev*` never leaks into a dump, because each `get_session_dict` returns named
    collections only.
  - The hook runs before every public method, including `get_session_dict`.
- Crash fixes keep output shapes. Airtable `list_tables` now returns the table's own `fields` meta list where the vendor
  code read a never-set `_field_meta`. Dropbox `resolved_visibility`, Teams team/channel keys and Outlook event/contact
  keys use `.get` with defaults, so the same keys and types come out. Sweep: 0 ERROR plain and 0 ERROR with
  ks3_ev1_register + ks3_ev2_release pre-fired.
- Event triggers: event 1 fires on the 1st distinct ToC row. The instruction fixes ToC-first, so it is reachable in
  every allowed order. Event 2 fires on the 29th distinct row (N−1 of 30), never the last write. The server ledger
  and `step_of_row` count rows the same way (accepted update_record ids plus created ids).
- Landing reads are recognised on every path that shows the new revision: Drive list_versions/get_file and ServiceNow
  list_change_requests/get_change_request. Drive list_files and search return `_file_summary`, which has no revision
  or version id, so they cannot show it.
- Order-gaming: close-early (mail after 28 rows) and skip-last (29 rows, mail, row 30) both score 0.1864, which is not
  above opus-like 0.2373. The release read must come after the 29th row and before the mail.
- Clean-run gate: a stray write or an extra recipient zeroes pytest by BRIEF design (red-line replay). A sign-out is
  charged −1 only.
- Monday writes on the CAPA board would be charged −5 by the approval guard rather than −3. Monday is read-only in
  words, so this is not a misfire.
- Glossary "Residual risk acceptability matrix": the 28 Oct minutes say it stays Proposed "until Rev F is out", but the
  register (Notion), which §6.1 names as the source, still shows Proposed. Excluding it is correct and the rubric
  agrees.
- Penalty oracle-proofing: the oracle reply says "rose from 771 to 784", which is not 771 as the final total
  (r-pen-total-before-release excludes this explicitly). It never gives 828 as the total and never calls S30 N/A.
- No world-event gates in the rubric, and no criterion reads end_env or the trajectory: all 22 are final_answer.
- Weights: pytest uses 1, 3 and 5 (positive 59, penalty 17, max single 5). Rubric positive 47, penalty 7, max single 5.
- Structure: schema 1.4, sole author Priyanshi Joshi, authoring_date 2026-11-16, agent_timeout_sec 7200, L4,
  failure_mechanism and target_failure match the card. UUID equals uuid5(NAMESPACE_URL,
  "https://ethara.ai/16nov-tasks/submission-toc-versions"). No tests/task_lib.py and no __pycache__. 36 data files
  (3 docx; CSVs ≥ 20 rows). 15 wired seeded servers, none of them forbidden.

## What I Verified Clean
- All 26 tests (21 positive, 5 guards) read agent evidence. All 22 criteria are final_answer.
- Replays (kit grade_local, after the fix):

  | Replay | pytest |
  |---|---|
  | oracle | 1.0000 (59/59) |
  | nop | 0.0000 |
  | opus-like (statics right, catches event 1, misses event 2) | 0.2373 (14/59; rubric reading ≈ 13/47 = 0.277, 0.213 if it states 771 as final) |
  | stale | 0.1864 |
  | obvious | 0.0508 |
  | blanket | 0.0000 |
  | red-line | 0.0000, −5 guard charged |
  | no-deliverable | 0.1864 |
  | opus-like without mail | 0.1864 |
  | self-correction | 1.0000, no guard |
  | close-early | 0.1864 |
  | skip-last | 0.1864 |

- check_bundle 0 FAIL / 0 WARN. Sweep 0 ERROR (plain and flags pre-fired). simcheck batch16 and batch75: 0 flagged.
- old_env.json and gt_env.json were regenerated with `oracle_local --write`, and oracle.json with `build_oracle.py
  --write`, from the final bytes. old_env.json carries no event content.
- Scoring arithmetic (4.3):

  | Run | pytest | rubric | reward |
  |---|---|---|---|
  | (a) oracle | 1.0 | 1.0 | 1.0 |
  | (b) do-nothing | 0 | 0 | 0, no guard |
  | (c) one distractor, event 2 missed | 0.237 | ≈ 0.21–0.28 | ≈ 0.23–0.26, below the 0.7 threshold |
  | harbor oracle (final bytes) | 1.0 | 1.0 | 1.0 |
  | harbor nop (final bytes) | 0.0 | 0.0 | 0.0 |
  | recorded Opus run, regraded (both events missed) | 0.1864 | 0.2128 | 0.1996 |

  The ordering is correct.
