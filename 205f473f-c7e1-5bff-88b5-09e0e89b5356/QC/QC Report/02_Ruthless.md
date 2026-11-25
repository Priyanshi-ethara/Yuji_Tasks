## VERDICT: PASS

**Task:** U04 crash-owner-routing (`harness_mcp_atlas/input/205f473f-c7e1-5bff-88b5-09e0e89b5356`). It is a STATIC card hardened under HARDEN16 (2026-11-16): the static traps are kept and one live ownership change is added, following the owner decision that a stale-read failure is acceptable.

**How the review was done:** this report describes the final, delivered bytes (task_checksum `e0e779d4e95a7678daf1d71487b47c5987679dd3b0a8a1edd1bc02b99af9f77a`). An independent fresh reviewer first returned FAIL on three Major rubric findings, all fixed in the hardening pass (see "Fixed in this pass").

The final QC re-read this report against the delivered bundle and its harbor runs. The task bytes have not changed since the review: the newest input file is from 16:26:05, the mechanical outputs are from 16:26, and the judged oracle/nop and Opus runs started at 16:37 and 16:40. The §1 script was re-run on a UUID-named copy of the final bytes. Its output is byte-identical to the pre-run `02_ruthless_mechanical.txt` (`diff` is empty).

The judged harbor runs below replace the earlier replay estimates. The two pre-run Minor findings were re-assessed against the instruction text and are now listed under CLEARED, with their reasons. Neither needs a change.

### Judged harbor runs on the final bytes (gpt-5.6-sol via codex, checksum `e0e779d4…f77a` on all three)

| Run | pytest | rubric | reward | detail |
|---|---|---|---|---|
| oracle (`/tmp/qc/oracle_nop_20261116_163724`, trial ooThF6W) | 1.0 (46/46) | 1.0 (19/19 positives, 0 of 3 penalties) | 1.0 | no guard, no exception |
| nop (same ONDIR, trial caLsG3f) | 0.0 (0/46) | 0.0 | 0.0 | no guard; state_capture_failed is expected for a nop |
| Opus 5 (`…-opus-5-20261116-111050`, trial TDTmhge) | 0.2391 (11/46) | 0.2093 (12/43 positives, −3 for r-pen-msg5) | 0.2242 | no guard, 0 tool errors; matches the replay prediction below |

### Re-validation on the final bytes (kit `grade_local`, before the harbor runs)

| Run | pytest | rubric (read) |
|---|---|---|
| oracle | 1.0000 (46/46) | 43/43, no penalty |
| nop | 0.0000 | 0 |
| real Opus 5 baseline run, replayed | 0.2391 (11/46) | 12/43 positives = 0.279; Messaging 5 is stated, so −3 brings it to about 0.21 (the harbor run confirmed 0.2093) |
| opus-like (statics right, event missed) | 0.2391 | about 0.21 |
| close-early | 0.2174 | at or below opus-like |
| obvious / face value | 0.0652 | about 0 |
| blanket | 0.0000 | 0 |
| red line (Sentry resolve) | 0.0000 | −5 guard charged |
| code-host comment | 0.0000 | −5 guard charged |
| no summary | 0.0870 | |
| self-correction | 1.0000 | no guard |
| stray post | 0.9348 | −3 guard only |
| register tamper | 0.9348 | −3 guard only |
| sloppy event-catcher (moves notify/retry too) | 0.7391 | |

### Other checks
- check_bundle: 0 FAIL, 0 WARN.
- sweep: 0 ERROR, both plain and with `pellam_u04_notify` pre-fired.
- simcheck, regenerated at final QC because other batch tasks changed since: batch16 0 flagged (max cosine 0.124 / 0.076 / 0.195), batch75 0 flagged (0.090 / 0.052 / 0.140).
- No `/Users/` paths in data, world_data or instruction.md.
- No `__pycache__` and no `tests/task_lib.py`.
- old_env.json, gt_env.json and oracle.json were regenerated.
- old_env.json has no event content (0 hits for 3490 or the markers).

## Constraint Results

- **C1 (grounded expected values): PASS.**
  - Every owner, class, team, channel, marker and trigger count is read from `oracle.json["reported"]`.
  - Group ids in test bodies are seeded register keys, not answer figures.
  - The rubric holds no hard-coded figures (the §1c list is empty).

- **C2 (every test reads agent evidence): PASS.**
  - All 21 tests read the tool log and/or the end state (§1a table).
  - None reads the reply or a delivered file.

- **C3 (do-nothing run scores zero): PASS.**
  - The nop run scores 0/0.
  - Every positive test needs register writes plus `_ready()`: the summary is present and at least half of the anchor groups are right.
  - Read-only tests carry 8 of the 46 positive points, and each one also needs correct writes.
  - Blanket and placeholder runs score 0.

- **C4 (guards fire in the right direction): PASS.**
  - Polarity is `pass_charges`.
  - These acts are exempt: edits, deletes and comments on the run's own tickets; edits and deletes of the run's own Slack messages; marking mail read; re-writing an unchanged Sentry status.
  - The register guard compares field by field against the seed, with values normalised. The real harness Airtable dump does not trip it.
  - The oracle trips no guard.

- **C5 (prompt fidelity): PASS.**
  - Each event item answers a reply bullet the instruction asks for:
    - which rule decided a group not routed by its top frame: r-notify-merge, r-notify-scope, r-5m2-both, r-4h6-both;
    - the precedence rulings: r-retry-after-merge, r-queue-after-merge;
    - what was not followed and why: r-export-not-followed.
  - No item asks for a PR number, a time, a handle or a clause.

- **C6 (statement ↔ verifier alignment, ambiguity): PASS.**
  - Handbook §2 says ownership "is read from the repository's ownership file (.github/CODEOWNERS on main; the desk gets a fresh export every morning)". §6 names the PRs as the record.
  - The export header reads "Exported … 2026-11-16 06:00 UTC".
  - The only reasonable reading is the file as merged when the routing is filed.

- **C7 (agent cannot reach or alter the verifier): PASS.**
  - The Dockerfile copies only `state_capture.py`.
  - The servers and the event flag dir live in the sibling `light-servers` service.

- **C8 (no leaked solution artifacts): PASS.**
  - Scanned environment/, the patches, data/ and world_data.
  - The event content exists only inside the patch blocks, which apply only after the flag fires.
  - No answer key is present.

- **C9 (deterministic reward): PASS.**
  - The tests compare sets, `_event_team` sorts its choice, and nothing uses the clock or randomness.
  - The trigger count is persisted in the flag dir across sessions.

- **Cross-reference: no double-counted pair** (table below).

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None remaining. Three were found and fixed in this pass.

## Minor Findings (polish)
None. The two items the pre-run review listed here are not defects. They were re-assessed at final QC and moved to CLEARED (first two entries there), with the instruction sentences that decide them.

## Coverage Holes
- The reply's per-team and per-class counts are graded only through the wrong-figure penalties. Grading them directly would overlap with pytest under the strict-overlap rule.
- The ticket title and the root-cause text on each ticket line are not graded; only the group ids are.
- The summary's content is not graded, only that it exists and when it was posted.

## Fixed in this pass
**Hardening:**
- Added the live event `pellam_u04_notify`:
  - Trigger: the 21st distinct register row written.
  - Landing: GitHub PR #3490, with two review comments.
  - Corroboration: a #fleetd-dev merge note.
  - Effect: FLEETD-3S6, FLEETD-4H6 and FLEETD-5M2 move to Driver Comms. The Messaging ticket drops to 2 groups, and a new Driver Comms ticket is needed.
- Seeded Driver Comms (Okta, Linear, roster CSV).
- Moved the Slack and Datadog seed dates +365 days, from Nov 2025 to Nov 2026.
- Normalised the register guard.
- Reweighted pytest and the rubric onto what the event moves.

**Reviewer fixes:**
- r-notify-merge no longer requires the PR number, time or handles.
- r-notify-groups restated the moved groups' owner, which is strict overlap. It is replaced by r-notify-scope ("only the notify line changed"), and the owner wording is removed from r-5m2-both and r-4h6-both.
- r-retry-after-merge and r-queue-after-merge are reworded to "still decided by the later rule" instead of demanding a "did not move" framing.
- The PR comment text is added as a read marker.
- r-simkit-module now accepts equivalent wording.
- The oracle reply now states the scope sentence.

## Rubric ↔ pytest cross-reference
| Rubric item | Target | What it grades | Nearest pytest test | Same signal? | Evidence |
|---|---|---|---|---|---|
| r-notify-merge, r-export-not-followed | final_answer | the account of the change on main, and why the export was set aside | test_merged_ownership_change_looked_at_before_the_summary | no | that test is a trajectory read |
| r-notify-scope | final_answer | the scope of the change | none | no | |
| r-5m2-both, r-4h6-both | final_answer | the frames stepped over and the merged rule | moved-group register tests | no | no owner value restated |
| r-retry-after-merge, r-queue-after-merge | final_answer | why the later rules still decide | test_last_match_and_any_depth_rulings | no | explanation, not the value |
| 12 static items | final_answer | frame and rule explanations | grouped static tests | no | |
| r-pen-sim7, r-pen-msg5, r-pen-msg3 | final_answer | declared wrong figures | ticket tests | intentional distractor twins | CLEARED |

## CLEARED (considered and dismissed, with reasons)
- **`_ticket_ok` uses exact group-set equality over title plus description** (test_outputs.py L176-182). A ticket that also names other group ids fails it.
  - Instruction step 2 pins the description: "one line per group the team owns, the group's short id (like `FLEETD-0AB`), two spaces, then its root cause".
  - A ticket that names groups the team does not own breaks that pinned format, so failing it grades a written convention (C6), not an invented one.
  - The oracle's tickets pass, and the self-correction replay (draft ticket deleted and refiled) scores 1.0.
- **`_moved_group_check` needs owner and class together** (L345-352).
  - Instruction step 1 asks for both fields on every row: "On every row fill two fields": `Owner team` and `Root cause`.
  - A moved row with the wrong class is a wrong row, so a coupled check is correct for a per-group test.
  - The real run lost these tests on the owner (it wrote Messaging), not on the class: it wrote the oracle class on all 22 rows.
- **Playbook §4 literal matches (final QC).** The bundle matcher scores three pairs at composite 1.00 only because both texts name the same seeded group ids:
  - `test_nil_pointer_classes_follow_the_code` and r-decline (4V1, 4W6, 4X2);
  - `test_simkit_ticker_groups` and `test_simkit_ring_scheduler_and_clock_groups`, both against r-simkit-groups (5KQ, 5V4, 5P7, 5R3, 5T9).

  These pairs do not grade the same signal:
  - The tests compare the register fields with `oracle.json` (`_all_right`).
  - The criteria grade the reply's explanation, which the instruction asks for in its own bullet: "for the nil-pointer crashes, why each got the class it got"; "which frames you stepped over and why".
  - r-decline is satisfied only by the reason ("because Error() is called directly on the concrete *DeclineError field … no error interface is involved"). r-simkit-groups is satisfied only by naming the frame below the simkit frames. Neither can be earned from the register, and neither names an owner team.
  - Each item weighs 1 of 43, and each test 1 of 46, far below a third of a channel.
- **Penalty misfires (final QC, against the real run).**
  - r-pen-sim7 and r-pen-msg3 say "as the routing result". In the run, the judge did not charge "Sim Tools gets 1, not 7", a figure quoted only as the draft's.
  - r-pen-msg5 fired on the run's own per-team table ("Messaging | 5 — 3S6, 4H6, 4Q9, 5M2, 5R3", final_message.md L15). That is the morning-export figure stated as the result, so the charge is earned.
  - The oracle trips no penalty (0 of 3).
- **Event fairness.**
  - The handbook already names main as the source, and the export is dated 06:00.
  - Driver Comms exists before the event with neutral descriptions.
  - Nothing announces the PR.
  - The instruction is byte-identical to the pre-hardening version.
  - The oracle and the self-correction run reach 1.0.
- **Dating.** The event is at 08:05–08:44 UTC on 16 Nov, after every seed record (latest: the 06:00 export and the 05:30 sync).
- **Trigger reachability.** All 22 rows start empty, and the instruction's order (register first) reaches the 21st row in every row order.
- **Patches.**
  - They add no new fields or record types; key sets match the seed records.
  - `ATLAS_EVENT_DIR` is read at call time.
  - The apply call runs in every public method and in `get_session_dict`, and is idempotent.
- **Order-gaming.**
  - Close-early (0.2174) is not above opus-like (0.2391).
  - Every 5-point test needs a read after the event landed and before the summary.
  - The moved rows must carry their owner before the summary.
- **Alternative paths.** Fixing or recreating its own ticket, a read through sign-in, search or comments, and rewriting rows after the read all pass.
- **Literal group ids in test bodies.** They are seeded keys, not answers.
- **No rubric item states that the run did not do a guarded act.**

## What I Verified Clean
- All 21 tests read the end state or the tool log.
- All 16 positive tests need register writes and the anti-blanket anchors.
- All 5 guards are `pass_charges` and fire only on forbidden acts.
- The rubric has 22 criteria, all `final_answer`: +43 positive, −11 penalty, no item above half of its channel, static positives 12/43 = 0.279.
- Pytest weights are 5, 3 and 1, all three used; guards total 17 against 46 positive.
