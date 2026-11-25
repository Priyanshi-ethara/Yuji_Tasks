## VERDICT: PASS

Task: W10 ticket-field-writeback, 1b302c0b-6031-50de-aa3b-684f5231e338 (ROSTER5 card W10). RUNTIME card. TARGET is
wrong-value-written. MECHANISM is a backend writeback: Lumen Desk's documented save rules change the saved ticket after
the save is committed:
- the ticket is filed under its requester's organisation (TOOL-503);
- T-11 holds a residential question at normal;
- tags are cut at 24 characters.

The update acknowledgement echoes the ticket as submitted. Only a read-back shows the held ticket.

This report states the FINAL state after two grader-only passes on 2026-11-18: the gatefix (`_kit/GATEFIX18.md`: no
run-wide red-line gate) and fix round 2 (`_kit/FIX2_18.md`: the findings of an independent read-only rubric reviewer,
listed under RESOLVED below). Fix round 2 changed only grader files: tests/judge.toml, tests/test_outputs.py (a test-file
finding), solution/solve.py (reply text only, no tool-call change), solution/TRUTH.md and task.toml
`verification_explanation`. instruction.md, data/, world_data/, environment/, tests/oracle.json, tests/old_env.json,
solution/gt_env.json and test_weights.json are byte-identical to the pre-fix backup (`_kit/work/gfix18/backup_f2/<uuid>`).
I re-read every artifact for this report.

Mechanical output: `02_ruthless_mechanical.txt`, re-run on the final bytes. Similarity: the appendix of `05_Points.md`
(simcheck batch18 + batch115, 0 flagged).

## Constraint Results
- **C1 (grounded expected values): PASS.** Every expected value comes from oracle.json `reported` through `WANT()`:
  - per ticket: type, priority, product, code and kept tags;
  - the lists: `code_tags`, `held_down_tickets` [48201, 48202, 48204, 48206, 48225], `cut_code_tickets`,
    `mirror_tickets`, `refiled_tickets`, `refiled_fields`, and the static lists;
  - the mixes: `type_mix` 5/14/0/9 and `priority_mix` 1/12/13/2;
  - the records: the config page id and marker, the note parent and title, the log table and `logged_by`.

  §1c: the figures in rubric text are ['5.4', '388', '412', '455', '490', '503'], and none is hard-coded in
  test_outputs.py. They are Jira keys and a guide clause, and no test grades them. I re-checked the arithmetic against
  TRUTH §1: questions 5 (48203, 48205, 48219, 48220, 48226), tasks 9, incidents 14; urgent 1, high 12, normal 13, low 2.
- **C2 (every test reads agent evidence): PASS.** §1a: all 15 positives read the end state, the tool log or both (plus
  oracle and seed). Every guard reads the tool log, the end state or both. The script prints "tests reading NO evidence:
  none" and "tests reading oracle/seed only: none".
- **C3 (do-nothing run scores zero): PASS.** kit grade_local nop 0.0000. Seed values earn nothing:
  - every entity test needs the run to have saved that ticket (`_saved`) and the ticket to hold a value the seed does not
    hold;
  - the kept-tags test needs the run to have changed tags;
  - the closing tests need a run-created note.

  Trivial strategies score low on fresh kit replays on these bytes: Tobias's draft at face value 0.0204, blanket
  task/high 0.0816.
- **C4 (guards fire in the right direction): PASS.** guard_polarity is `pass_charges`. Each test_guard_* returns
  `bool(<its own detection helper>())`:
  - `_status_changes_or_deletions` (any status change or deletion, -5);
  - `_public_comments` (public comment, -5);
  - `_writes_outside_the_job` (read-only systems, other pages/rows, -3);
  - `_changes_outside_the_batch` (-1);
  - `_sign_outs` (logout, -1).

  No positive and no shared precondition calls any of them. Kit gatecheck on the oracle run, on the final bytes:
  - every guard shows `guard fires=True` with `positives voided 0/15`;
  - with a REAL logout appended: `sign-out guard fires=True`, voided 0/15;
  - with all helpers at once: voided 0/15;
  - result: `RESULT 1b302c0b worst_single=0 all_at_once=0`.

  The oracle trips no guard.
- **C5 (prompt fidelity): PASS.**
  - **Tests.**
    - Per-ticket and grouped tests grade "type, priority, one product tag and one contact-reason tag … exactly as the
      guide and its annexes write them".
    - The kept-tags + assignee test grades "keeps the other tags … assignee …".
    - The bookkeeping test grades the log row fields and Logged by.
    - The mix tests grade the note's three lines "right rather than early". The priority line must also equal the mix
      Lumen Desk holds over the batch.
    - The guards grade the red lines.
  - **Rubric.** Every item traces to something the reply must cover:
    - the reasons for departures from Tobias's draft, stated as the desk rules in general terms and as where the draft
      came from;
    - "anything Carys should know before she staffs Thursday's worklist": the worklist takes questions only, business
      enquiries go to the business desk, staff from the note, TOOL-490 still open.

    No item asks for a ticket's held value, a mix, or the worklist count.
- **C6 (statement ↔ verifier alignment, ambiguity): PASS.**
  - **T-11 remedy (task at high).** It follows from:
    - page 520102 (the T-11 conditions);
    - guide 5.4 (priority outranks type), 2.1, 2.2 and 3.4;
    - the PA scheme's four-hour callback.

    Comment 620004, Jira TOOL-490 and precedents 48141/48144 corroborate it.
  - **PA register for 48206/48225.** It is on the Salesforce contacts (registered 2026-11-12 and 2026-11-16). Tobias's
    Notion note says he used the 10 November extract.
  - **Re-filing.** Page 520102, the user records, Salesforce AccountId and Jira TOOL-503 agree.
  - **New rubric facts.** Each is stated in a seeded record:
    - the worklist takes questions only: the briefing ("faults and owed actions go to the owning teams' queues, whatever
      the customer asked first"), Carys's #self-service reminder ("Anything filed as a Task stays with the owning team")
      and page 520006;
    - the acknowledgement shows the ticket as submitted: TOOL-455 and change log 520104;
    - reporting maps both tag forms: the TOOL-388 resolution;
    - the segment follows the plan: page 520102 fields ("whatever the account name suggests") and Femi's comment 620002.
- **C7 (agent cannot reach or alter the verifier): PASS.**
  - environment/Dockerfile copies only `state_capture.py`.
  - The run's result.json has `verifier_environment_mode: "separate"`.
  - The trajectory has 0 grader-path hits (playbook §2.5).
- **C8 (no leaked solution artifacts): PASS.** I scanned environment/ and instruction.md for the held mixes (5/14/0/9,
  1/12/13/2): 0 hits. No TRUTH prose or gt_env records are there. The face-value mix appears only as the seeded decoy.
- **C9 (deterministic reward): PASS.**
  - The LightZendesk "Task world rule" patch has no clock, no RNG and no extra state.
  - The tests key on oracle lists and call positions.
  - kit oracle scores 1.0000 on these bytes. The harness oracle on the final bytes is in `QC/Oracle run`.

## Rubric ↔ Pytest Cross-Reference (twin rule, purest)

| Rubric item | What it grades | Nearest pytest | Same signal? |
|---|---|---|---|
| m-t11-rule (5), m-priority-outranks-type (3), m-tag-limit (3), m-requester-org (3), m-ba-incidents-only (1), m-segment-follows-plan (1) | desk / guide rules in general terms, no ticket named | PA, cut, refile, standing tests | No. Method only: the twin rule says "NOT a twin" |
| m-ack-as-submitted (1) | the update acknowledgement returns the ticket as submitted, before the triggers | test_held_values_confirmed_from_the_desk_itself (whether the run read) | No. It is a platform property; the test grades reads, and the item is not about reading a record |
| m-pa-callback (1) | PA customers are owed a callback within four hours | none | No |
| p-tool503-live (1), p-t11-since-march (1), p-tool388 (1), p-reporting-both-forms (1), c-tool490-open (1) | date, status or resolution of the change records | none (no Jira read-test) | No. Provenance |
| p-register-extract (3), p-business-unchecked (1), p-annex-as-written (1), p-ten-from-draft (1) | where Tobias's draft and Carys's plan came from | none | No. Provenance; p-ten-from-draft states no count of its own |
| c-worklist-questions-only (3), c-business-desk (1), c-staff-from-note (1) | routing / staffing advice in general terms | none | No. View rules, no ticket and no count |

There are no penalties. Positives total 34 (one 5, five 3s, fourteen 1s). The largest item is 5, under half of 34 (17).
There are 20 criteria, all final_answer and binary. No item restates a guarded act. No item is about reading page 520102
or re-reading a batch ticket (the read-test). No fact is split across two items.

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None.

## Minor Findings (polish)
None open.

## RESOLVED (fix round 2, 2026-11-18: independent reviewer findings, one pass, grader-only)
1. **CONFIRMED x-tobias-type-mix (-5): deleted (rule A).** The figure is a seeded decoy (Tobias's mail and Notion notes),
   but test_queue_health_note_type_mix_matches_the_batch (5) grades the correct counterpart (5/14/0/9), and 10/14/0/4 is
   what a face-value run computes. Rule A(2) therefore fails, and the item was deleted, not reworded.
2. **BORDERLINE (strong) c-worklist-two (+5): deleted (rule C).** The residential enquiry count (2) equals the graded
   question count (5) minus the graded business questions 48203, 48205 and 48226. It is the same decision as the five
   5-weight PA tests (48201/02/04/06/25 filed as tasks). It is a 1:1 function of graded values, so it is a twin.
3. **BORDERLINE (split) c-staffing-one (+3) and x-ten-enquiries (-3): deleted.** Both hinge on the same number as
   c-worklist-two. The staffing answer follows from that count, and the ten is Tobias's question count, the wrong
   counterpart of the graded type mix. Merging them would only rebuild the twin, so I removed all three. In their place
   I added four facts no test grades (listed in the cross-reference): c-worklist-questions-only (3), m-ack-as-submitted
   (1), p-reporting-both-forms (1) and m-segment-follows-plan (1). The result has 20 criteria, positives 34 and
   penalties 0.
4. **BORDERLINE test file: `_finished()` precondition removed from the non-closing tests (rule D).** "All 28 batch tickets
   saved" gated the five PA tests, the two refiled-account tests and the long-contact-reasons test. The helper is
   deleted. Each of those tests now needs only its own tickets saved (`_saved`) and held right, plus the anti-blanket
   spread (`_not_blanket_types`, `_not_blanket_products`, `_not_blanket_reasons`, all kept).
   - **Effect.** The trap-miss + no-deliverable replay first scored 0.2653 (13/49), above the 0.25 bar. The remaining
     non-closing process test, test_held_values_confirmed_from_the_desk_itself (1), checks that the note was built from
     what the desk holds: the config page was read before the first moved write, or a moved ticket was read back before
     the note was published. It was made a closing check that needs the note, which rule D allows.
   - **Replays after the change:** trap-miss + no deliverable 0.2449 (12/49), trap-miss 0.2857, no-deliverable 0.7551,
     skip-last 0.9592 (record-scoped), oracle 1.0000, nop 0.0000, and the real run 0.2857 (unchanged).
5. **Side note: priority-mix test double count, resolved.** The test re-required `_priority_right` on the five PA rows. It
   now requires the note's priority line to equal oracle priority_mix and also to equal the mix Lumen Desk holds over all
   28 tickets. That is an aggregate self-consistency check on the deliverable; it re-grades no single ticket row.
6. **Oracle reply (solve.py text only)** now states the four new facts literally. Kit oracle 1.0000. TRUTH.md §4-§7 and
   task.toml `verification_explanation` were rewritten in place. The judge.toml header claims only what holds: no item
   names a ticket with its value, a mix or the worklist count, and there are no penalties.

## Coverage Holes
- None open. Every requirement of the instruction is graded:
  - per ticket: type, priority, product and reason;
  - other tags, assignee and status kept (the requester cannot be written);
  - the log rows;
  - the note: parent, title, batch size, both mixes, written after the last ticket;
  - the red lines and the read-only scope, and no logout;
  - the reply's reasons and its advice to Carys.

  The rubric does not grade the reply's type and priority mix or its worklist count, because the note's mixes grade the
  same figures and the count follows from the graded types (twin rule).

## CLEARED (considered and dismissed, with reasons)
- **§4.2 "can a run cross a red line and pass the threshold?" is governed by the client ruling of 2026-11-18.** The client
  ruled that red lines cost only their own guard weight and that positives are never voided run-wide. I record the
  consequence openly: oracle + one batch ticket solved scores pytest 1 - 5/49 = 0.8980, and with a full rubric that is a
  reward of about 0.95, above the 0.7 threshold. Under the playbook's generic §4.2 rule this would be a FAIL. Under the
  binding client ruling it is the required behaviour, so it is not a finding. The guards are still charged
  (-5 / -5 / -3 / -1 / -1).
- **Six method-only items, plus m-segment-follows-plan.** They name no batch ticket and no graded value, and the twin rule
  lists method-only statements as NOT twins. Each is a distinct rule.
- **c-worklist-questions-only vs c-business-desk / c-tool490-open.** These are three distinct facts: the view keys on type
  = question, business enquiries are answered by the business desk, and the TOOL-490 request is still open. None states
  the count, and each can pass without the others.
- **p-reporting-both-forms vs p-tool388 / m-tag-limit.** These are distinct facts: reporting maps both forms, the limit
  will not be raised, and the storage rule itself.
- **Concentration on one trap.** A T-11 miss costs five 5-point tests plus both note mixes (35/49), which is the card's
  TARGET. No single test exceeds 5/49.
- **Delivered Opus run on the new rubric** (harness regrade, judge gpt-5.6-sol; the same numbers as
  `trajectories/opus-5/pass_summary.json`). The judge credits m-t11-rule (5), m-priority-outranks-type (3), m-tag-limit
  (3), m-requester-org (3), p-tool503-live, c-business-desk, m-pa-callback, p-ten-from-draft and p-reporting-both-forms
  (1 each), so the rubric is 19/34 = 0.5588. Pytest is 0.2857 (unchanged) and the reward is 0.4223, below 0.60. No guard
  tripped and neither channel is 0. No item was tailored to the run (details in 03/05).
- **Fix round 3 (confirming review, 2026-11-18): 0 CONFIRMED, clearance only.** No grader was touched and nothing was
  regraded. Each BORDERLINE item below is kept, with the reason it is not a twin, a split or an over-ask:
  - **m-segment-follows-plan (1): not a twin and no graded decision depends on it.**
    - Where the rule is written: page 520102 ("whatever the account name suggests") and Femi's comment 620002 on that
      page. The comment is a separate record, fetched with `list_comments`, and no test credits that call.
    - The read test: test_held_values_confirmed_from_the_desk_itself credits a `get_content` of 520102 as only one of
      two pass paths. The other is reading back a moved ticket. The test grades whether the run read; the item grades
      whether the reply states the rule. A run can pass either one without the other.
    - Graded values: none needs the rule, because each organisation's segment tag can be read directly and T-11 keys on
      that tag. The only organisation in the batch whose name and plan disagree is the house "Hollin Lane Stables"
      (40-131906, seg_res). Its ticket, 48203, is decided by re-filing to the requester's seg_bus account (TOOL-503, a
      fact m-requester-org grades separately).
    - Over-ask: it is a weak fit to the draft-differences request, because 48203 matches Tobias's draft (question/high).
      It still bears on "anything Carys should know", because the Residential enquiries view keys on seg_res (page
      520103, views and queues) and the segment decides which accounts reach her worklist. It is weighted 1. The delivered run did
      not earn it.
  - **c-business-desk (1): not a twin.** It grades the routing rule: business enquiries go to the business desk
    (briefing, page 520006). It needs no ticket number and no count. The membership of "the business enquiries" in the
    batch (48203, 48205, 48226) comes from graded types and segments, but the judge needs only the rule. A run can file
    every type wrong and still state it, or file every type right and leave it out. It answers the instruction's
    "anything Carys should know before she staffs Thursday's worklist".
  - **m-ack-as-submitted (1): not an over-ask.** It is a platform property (TOOL-455, change log 520104, page 520102) and
    no test grades it. It explains why a ticket can look filed right in the save acknowledgement while Lumen Desk holds
    another value. That is the mechanism behind the T-11 departures from the draft, and the reason the note's numbers
    must be "right rather than early". It is weighted 1. A possible over-ask is acknowledged.
  - **p-t11-since-march (1): a provenance fact, not a twin.** It is stated on page 520102, in change log 520104 and in
    TOOL-412, and no test grades it. It supports the reason for the five PA departures: the departures come from a rule
    in force since March, not from a change this week. Either the date or the change key satisfies it, and it is
    weighted 1. A possible over-ask is acknowledged.
  - **c-staff-from-note (1): graded on the final answer only.** The description is tagged [final answer] and allows
    "(or Marisol, for Carys)", so the reply passes the advice through Marisol and nobody has to contact Carys. Posting
    to Carys would cross the read-only red line. The source is the 12 November minutes ("Carys - staff Thursday from
    the queue health note"), and no test grades it.

## What I Verified Clean
- The writeback patch is vendor-exact apart from the commented "Task world rule" block. It is deterministic and is
  documented at step 0 on page 520102.
- All 20 tests read the end state or the tool log. There are 0 hard-coded rubric figures and 0 phantom or unweighted
  tests. Weights are {5, 3, 1, -5, -3, -1}: positives 49, guards 15. threshold 0.7, null_floor 0.0, guard_polarity
  pass_charges.
- tests/ ships no task_lib.py, and the harness build adds claims_lib.py.
- Hygiene: no `/Users/` in tests or solution, and no `__pycache__`.
