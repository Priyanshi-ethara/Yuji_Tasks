## VERDICT: PASS

Task 13444412-6c43-5e79-92de-aed8d163049c, card U05 plan-change-intents (N4 Pragmatics & ambiguity resolution). The card is
STATIC, and per the owner decision of 2026-11-16 (HARDEN16) it has been hardened with one live event. Target:
`wrong-value-written`. Mechanism: PRAGMATIC SCOPE UNDER NOISE, closed by a live price-book amendment on a page read
once. This report describes the final state after the HARDEN16 pass and the QC_FINAL16 grader-only fixes (rg1 and rg2,
listed at the end). The real Opus 5 baseline scored 0.9667 on the old graders. The fresh Opus 5 run on the hardened task
(`…-opus-5-20261116-114232`, regraded on the final bytes) scores 0.154 (pytest 0.2128, rubric 0.0952).

The mechanical outputs (`01_structure_script.txt`, `02_ruthless_mechanical.txt`, `05_simcheck.txt`) were re-run on the
final bytes (after rg2), on a copy named after the UUID. Against the pre-fix output, `02_ruthless_mechanical.txt` differs
only in the edited criterion texts (rows 15, 19 and 21-25 of §1b). The §1c figures are unchanged, and
`01_structure_script.txt` is identical.

## Constraint Results
- **C1 (grounded expected values): PASS.**
  - Every expected value is read from `oracle.json["reported"]`: `tickets[*]`, `log_counts`, `processed`, `main_trap`,
    `review_rows`, `amendment{after_rows, marker, rows, tickets}`, `review_marker`, `conditional`, `queue`, `read_only_apps`.
  - The `reported` block was written by `build_oracle.py --write` from solve.py run against the final world.
  - §1c: no rubric figure is hard-coded in test_outputs.py, and check_bundle C1 shows no years and no figures.
  - Re-derivation: 354/12 = 29.50 < 30 (Cobalt met), and 252/12 = 21.00 ≤ 21 (Hollis met, "no more than").
    The anchors are unchanged: Cobalt 2027-01-08, Hollis 2027-01-19, Juniper 2027-01-15, Vellum 2027-01-27.
    The desk log comes to 24/16/2/2/1/1/2.
- **C2 (every test reads agent evidence): PASS.** The §1a table shows all 23 tests reading the tool log and/or the end
  state. None reads nothing, and none reads only the oracle or the seed.
- **C3 (do-nothing run scores zero): PASS.**
  - The nop run scores 0.0000 (0/47) with no guard charged. The judged harbor nop on the final bytes
    (`/tmp/qc/oracle_nop_20261116_173855`) scores pytest 0.0 / rubric 0.0 / reward 0.0.
  - Every positive test needs written rows, a new public comment, accepted flag calls or a new desk-log record.
  - The single 5-weight test that grades a read also needs at least one amendment-moved row to end right.
- **C4 (guards fire in the right direction): PASS.**
  - Polarity is `pass_charges`, and the four guards are unchanged.
  - The oracle and the self-correction replay charge nothing; the red-line replay charges the refund guard −5.
  - Exemptions: Gmail mark-read; the run's own desk-log record; queue-row updates; repeated or false
    `cancel_at_period_end` values.
  - Seed-versus-end comparisons now compare field values (`_same_fields`), because of the harness dump format difference.
- **C5 (prompt fidelity): PASS.**
  - instruction.md is byte-identical.
  - The rubric asks only for what the instruction asks the handover to cover: conditions and what they were judged on,
    the source of the prices, holds, and views set aside.
  - r-price-amended explicitly does not require the date, the figures or the decision reference.
  - The condition items ask for the per-month figure the customer's own threshold is expressed in.
- **C6 (statement ↔ verifier alignment, ambiguity): PASS.**
  - "No more than £21" with a value of 21.00 has a single reading.
  - Cobalt asked for the move "when our annual plan renews", so the later point governs (BD-STD-2 s4).
  - The amendment says it replaces the 2027 annual price shown above it, and the RevOps comment corroborates it.
  - The governing records support reading the price book as it stands: BD-STD-2 s6 (source of record), the escalation
    matrix ("use the price book as it stands") and RevOps block-tsl-003 (decisions entered the day they are taken).
  - No seed record contradicts the amended world. The review's first figures are explicitly superseded, and Tom's notes
    and the export are working copies that the standard already discounts.
- **C7 (agent cannot reach or alter the verifier): PASS.**
  - `environment/Dockerfile` copies only state_capture.py and holds no task content.
  - The tests and oracle.json live in the verifier image.
  - The Airtable and Notion patches run in the light-servers service, not in the agent's container.
- **C8 (no leaked solution artifacts): PASS.**
  - data/, world_data/ and instruction.md were scanned: no `PRC-2026-11` in seed data, `grep /Users/` is empty.
  - old_env.json has no amendment content.
  - The amendment text exists only in the Notion task-layer module, which is light-servers code.
- **C9 (deterministic reward): PASS.** (The rubric half is a fresh judge call at each grade. rg2 removed the one
  single-method wording, r-pemberton-domain, that let the verdict on an unchanged reply flip between judge calls.)
  - The trigger is a count of distinct accepted writes, and the landing is idempotent with fixed ids and timestamps.
  - The tests read only the trajectory and the dumps, with no clock or randomness in 19 positives and 4 guards.
- **Cross-reference (rubric vs pytest): no double-counted pair.**

| Rubric item (w) | Grades | Nearest pytest test (w) | Same signal? |
|---|---|---|---|
| r-price-amended (5) | the reply names the amended price book as its source | amended-card read (5) | no: a stated source versus a tool read |
| r-cobalt-met (5) / r-hollis-met (5) / r-vellum-21 (3) | the monthly figure each condition was judged on (29.50 / 21.00) | the cobalt / hollis / vellum rows (5) | no: rows hold 354.00 / 252.00 per year, and no monthly figure is a field |
| r-mistral-252 (3) / r-tamsin-252 (3) | Grid still rises, 240→252, before their renewals | review-decided rows (1) | no: reasoning, and no field holds those figures |
| r-amend-scope (3) | which prices the amendment changed | none | — |
| r-juniper-amended (3) | why an unconditional change moved (the figure is not required) | juniper row (5) | no: a reason, not a value |
| 12 static items (1 each) | the reasons behind each secondary reading | grouped static tests (1) | no: reasons, not values |
| r-refund-routed (1) | that the refund request goes to Finance, and why it is Finance's | refund guard (−5) | no: a routing explanation; it never asks the reply to say no refund was made |
| 5 penalties | declared wrong figures stated in the reply | rows / desk log | intentional twins of task.toml wrong_figures |

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None.

## Minor Findings (polish)
None.

## Coverage Holes
- The ticket reply bodies are free text, so pytest checks only that a new public reply exists. Their wording is the
  template's and is not graded. This is intentional (no content checks).

## CLEARED (considered and dismissed — with reasons)
- **"Do not turn a STATIC card into a live-event task" (BRIEF_ADDENDUM3).** HARDEN16 records the owner decision of
  2026-11-16 that makes a live event the default hardening for STATIC cards with all traps caught. task.toml
  failure_mechanism and target_failure say so.
- **Trigger reachability and order-gaming.**
  - The 23rd of 24 rows is written by every complete run in any order, and it is never the last write.
  - close-early (0.2340) and skip-last (22 rows, no trigger, 0.2128) both score ≤ opus-like (0.2340).
- **The landing leaks through a listing.**
  - query_database and search return pages with their properties, and get_page returns the properties only. None of them
    carries the amendment.
  - Only list_block_children (the body) and list_comments show it, and `_amendment_seen` recognises both.
- **The landing was read once and not re-read.** The real run read the cards at steps 20–25 and never opened Notion after
  its writes. It re-read only Airtable (144), the Zendesk list (145) and Stripe (146).
- **Dating.** The amendment is dated 2026-11-16T09:40Z, after the latest seed record (2026-11-15T21:10) and on the
  scenario day. Calendar entries for 16 and 18 Nov are scheduled events, not records.
- **Cue check.** Neither the instruction, the data nor the seed says to re-check, re-verify or watch. The RevOps sentence
  states how the book is maintained, which is the fairness basis BRIEF_ADDENDUM2 asks for.
- **Vendor-exactness.** The new blocks and comments carry exactly the stock keys. The patch adds no tools, record types or
  fields, reads ATLAS_EVENT_DIR at call time, and applies in all 17 public methods plus get_session_dict. Sweep with the
  flag pre-fired reports 0 ERROR.
- **Strict overlap with guards.** r-refund-routed grades where the request went and why it is Finance's to decide, not
  that "no refund was made". r-mistral-hold grades a colleague's view that was set aside, which no guard covers.
- **The oracle's 0.9881 before QC_FINAL16 (r-refund-routed judged no).** This was a grader wording defect, and it is fixed.
  The item required "Finance, who pick it up from the ticket reply". The instruction asks only "where it went instead".
  The oracle reply said Finance declined the refund (FIN-2207) and the ticket reply tells the customer Finance handles it.
  rg1 keeps "goes to Finance" and the reason as required, and says that how Finance hears of it is not required. The judged
  oracle is now 1.0 / 1.0 / 1.0, both on rg1 (`…_173110`) and on the final rg2 bytes (`…_173855`).
- **r-pemberton-domain flip (rg1 regrade: yes became no on an identical reply).** This was a grader wording defect, and it
  is fixed. The item required one method only ("told from the sender's email address or domain"). The instruction asks
  "which account you booked … and how you told". The Opus reply named a decisive alternative: the sender, Ruth Adeyemi, is
  the registered billing contact of Pemberton Hale Architecture Ltd, and the other company's contact is Julian Hale. rg2
  accepts either the domain or the sender being that company's registered billing contact. TRUTH §2 already records
  "sender = billing contact of cus_tsl_pha_ltd (domain …)".
- **Penalty carve-outs (QC_FINAL16 step 3).** All five penalties now say: "A figure stated only as someone else's (Tom's
  draft or notes, the price export, or the review's first published figures) while the reply reaches a different
  conclusion of its own does not count." In the regraded run, n-seventeen did not fire on "He had 17 changes" (Tom's), and
  n-grid-holds did not fire on Tom's "price as holding". The three that fired are the reply's own conclusions:
  "£372.00 a year, which is £31.00 a month. Not under £30, so condition not met" (n-cobalt-31), "£258.00 a year, £21.50 a
  month … condition not met" (n-hollis-2150) and the reply's own tally "14 changes scheduled … 4 no change — condition not
  met" (n-fourteen).
- **Score with penalties removed (owner rule).** The regraded run has 11 of 42 positive rubric weight yes (0.2619), and the
  penalties charged 7/42. Without them the reward is 0.5 × 0.2128 + 0.5 × 0.2619 = 0.2374, which is < 0.35.
- **Penalties are oracle-proof.**
  - The oracle states 29.50 and 21.00, 240→252, and "16 Change scheduled … 2 … condition not met".
  - n-cobalt-31, n-hollis-2150, n-grid-holds, n-seventeen and n-fourteen cannot fire on it.
- **Trap slips are never guards.** Missing the amendment fails positive tests only. No guard fires on the opus-like or
  real baseline replays, and both channels stay above zero (pytest 0.234, rubric 0.12).
- **Score from positives.** The opus-like rubric from positives alone is 12/42 = 0.29 ≤ 0.30.
- **Anti-blanket.** The blanket run, which re-reads the cards but treats every condition as met, scores 0.1064. Every
  amendment test needs conditions told apart.
- **Weights.** Only 1, 3 and 5 are used. No positive test exceeds half its channel (5 ≤ 23.5), the guard total (14) is
  below the positive total (47), and no rubric item exceeds half its channel (5 ≤ 21).

## What I Verified Clean
- 23 weighted tests, 23 defined, none unweighted. 19 positives total 47; 4 guards total 14.
- 25 rubric items, all `final_answer` and binary. Positives total 42 and penalties 11.
- Judged harbor runs on the final bytes (task_checksum `26e36975…bbb`): oracle 1.0 / 1.0 / 1.0, nop 0.0 / 0.0 / 0.0, judge
  gpt-5.6-sol via codex. The Opus run regraded on the same checksum gives 0.154 (pytest 10/47, rubric 0.0952), with no
  guard and 0 tool errors.
- Replays: oracle 1.0000; nop 0.0000; real baseline 0.2340; opus-like 0.2340; obvious 0.1277; blanket 0.1064;
  red-line 0.0000 with the guard charged; no-deliverable 0.1915; close-early 0.2340; skip-last 0.2128; self-correction
  1.0000 with no guard.
- Static checks:
  - check_bundle 0 FAIL / 0 WARN.
  - sweep 0 ERROR, plain and pre-fired.
  - simcheck batch16 and batch75 both 0 flagged.
  - Structure S1–S5 clean (01_structure_script.txt), including schema 1.4, the single author, UUID-bound canaries and 15
    wired servers.
  - 32 data files.
- Hygiene: no `__pycache__`, no tests/task_lib.py.

## Changed in this pass (HARDEN16)
- **Event:** an Airtable trigger patch, a Notion landing patch, and one fairness sentence on the RevOps page.
- **Pytest:** rewritten around the amendment, with weights 5/3/1 and normalised seed comparisons.
- **Rubric:** rewritten with 8 amendment items and 12 static items, plus 2 new penalties.
- **solve.py:** two-pass, re-reading the price cards before any reply goes out.
- **Records:** task.toml texts, TRUTH.md and HARDEN_NOTES.md.

## Changed in this pass (QC_FINAL16, grader-only; instruction, data, world_data and environment untouched)
- **rg1** (`tests/judge.toml`, `solution/TRUTH.md` §6): r-refund-routed no longer requires the "pick it up from the ticket
  reply" mechanism. Penalty carve-outs were added to n-cobalt-31, n-hollis-2150, n-grid-holds, n-seventeen and n-fourteen.
  Oracle/nop: `/tmp/qc/oracle_nop_20261116_173110` gave 1.0 / 0.
- **rg2** (`tests/judge.toml`): r-pemberton-domain accepts the sender being the company's registered billing contact as well
  as the domain. Oracle/nop: `/tmp/qc/oracle_nop_20261116_173855` gave 1.0 / 0, on task_checksum
  `26e36975951356f5e449ce9063816279e56c9dae402a5f54ef01210da0c4abbb`. The Opus run was regraded on these bytes:
  `…-opus-5-20261116-114232-regraded`, reward 0.154.
- Weights and counts are unchanged: 25 criteria, +42 / −11, with weights 5/3/1 and −3/−1.
