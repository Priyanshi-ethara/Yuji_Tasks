## VERDICT: PASS

Task f487e5dd-4b6a-5589-bf99-346f3dc18122 (T49 pv-string-design-review), slot-6 v2, final bytes (2026-11-14).

**The trap.** It is static: a required conditional step.
- DS-6 Edition 4, clause 9.3: "An Approved design is released for installation on the reviewer's signature when it keeps its margin in hand: T_min is the coldest morning its roof will see, and its Voc,max is no more than 95 % of the inverter's maximum DC input". Otherwise the reviewer raises a countersign request in Linear team DESIGN, assigned to the Head of Engineering.
- Clause 2.3 makes T_min the coldest morning "of the open ground the station stands on".
- Four approvals within 95 % (Penhale, Nancarrow, Jenkin, Spargo) have roofs in valley bottoms 40–65 m below their station. Only the field sheets at `/Design Desk/W46/Site surveys/Field sheets/FS-46xx.md` record this.
- Correct line: `Released: 5`. Target sub-label: `instruction-ignored`.

**Review method.**
- This pass replaces the 03:21 report. That report was written before the hardener's final bytes had a second fresh review.
- A fresh, independent reviewer (a subagent that did not author the task) re-derived everything from the bytes. It was told not to trust TRUTH.md, REDESIGN_NOTES.md or the earlier report. It followed ZERO_MINOR6.md §1 (REVIEW2_PROMPT, 10_structure, 20_ruthless, BRIEF_ADDENDUM2, without the live-event items).
- I then checked its findings against the bytes and against the delivered Opus trajectory.
- One fix pass was made, and it was re-validated on the final bytes.
- Raw output: `02_ruthless_mechanical.txt`, regenerated, with every block preceded by its exact command and a re-validation block at the end.

## Fixed in this pass
1. **[task.toml line 97, `verification_explanation`] MINOR: the stray-rule wording did not match the code.**
   - The text said pytest charges a countersign on "a design neither in low ground nor above 95 % of its limit as the run recorded it".
   - tests/test_outputs.py `_stray_countersigns` (lines 259–277; `below_station` at line 274) exempts any roof below its station's level (`roof_below_station_m > 0`). That includes Curnow (11 m below, open slope) and Pascoe-Hart (3 m below), which are not "low ground".
   - Fix: the wording now reads "a design whose roof stands at or above its station's level and whose string Voc as the run recorded it is not above 95 % of its limit, or a design the run itself returned for overvoltage". It was applied to `$H/input/<uuid>/task.toml` and `$H/out/packaged/<uuid>/task.toml`, and so to the delivered copy.
   - It is metadata only: no test, weight, criterion or agent-visible byte changed. The fix is in the final build (fin9, task_checksum `fa6ce188…`). The regraded Opus job, the fin9 oracle and the fin9 nop all carry that checksum, and the regrade left every score and every yes/no unchanged (0.1834 = 0.5·0.2 + 0.5·0.1667). See the stale-build finding in 02_Ruthless.md.

2. **[harness build / solution/solve.py] MAJOR (packaging): a stale build was delivered.**
   - **Finding.** After fix 1, the 03:55 finalize regrade, its oracle and its nop still carried task_checksum `973dbca1…`. `out/build/<uuid>/task.toml` was dated 03:28, before the 03:48 source edit, and the refreshed packaged bundle still had the old wording.
   - **Cause.** The harness refused the input because 2.1 % of the text under solution/ overlapped agent-readable text, over the 2 % limit. `deliver.sh` swallowed the refusal and shipped the old build.
   - **Fix (coordinator).**
     - The oracle reply's 9.3/2.3 sentence in `solution/solve.py` was paraphrased. The new wording: "Under 9.3 my signature alone is enough only if two things hold: the station figure is really the lowest temperature this roof gets, and the string stays at or under 95 % of what the inverter accepts. The 2.3 figure describes the station's own level, open site, so a roof sitting lower can be colder …"
     - `deliver.sh` now aborts on a refused or stale build.
   - **"Head of Engineering" restored.** The first fin8 oracle fell to 0.9405 because the paraphrase dropped "Head of Engineering", which the rubric looks for in the reply. The phrase was put back in solve.py (`grep -c` gives 5), and the fin9 harbor oracle is 1.0/1.0/1.0.
   - **Now.** The input validates ("input ok"). tests/oracle.json, old_env.json and gt_env.json are byte-identical to before. Only `solution/solve.py` changed: a diff of the previous delivery against the fin9 packaged bundle lists no other file, outside trajectories/.
   - **Agent-visible bytes are unchanged.** The regraded Opus run (task_checksum `fa6ce188…`) scores the same: 0.1834, with the same tests missed and the same criteria judged no.
   - Local re-check on the final source: check_bundle 0 FAIL 0 WARN; grade_local oracle 1.0000, nop 0.0000 (02_ruthless_mechanical.txt, block "FINAL BYTES (fin9 …)").

## Constraint Results
- **C1 (grounded): PASS.** Every expected value is read from oracle.json `reported` (held, near_limit, week_line, countersign share, assignee_refs, roof_colder_than_station, roof_below_station_m). There are no literal answer figures or file names in test bodies (check_bundle: "hard-coded in test_outputs.py: none").
- **C2 (agent evidence): PASS.** All 26 tests read the tool log and/or the end state (mechanical table: "end state, oracle, seed, tool log").
- **C3 (do-nothing scores 0): PASS.**
  - nop 0.0000.
  - Every positive test goes through `_value_gate`: no red line, and at least half the verdicts and half the returns right.
  - The roof tests and the field-sheet read test also need the week line (`_closing_gate`).
- **C4 (guards): PASS.**
  - Six guards under pass_charges (−5/−5/−3/−3/−1/−1). The oracle trips none.
  - Self-correction (a stray issue moved to Canceled) scores 1.0000 with no charge.
- **C5 (prompt fidelity): PASS.**
  - "follow its procedure" plus 9.3 ground the countersigns. "issues in the Linear team DESIGN" is inside the write scope.
  - "the site surveys on Dropbox for what was submitted and where" grounds the field-sheet read.
  - No clause number, id or full name is required.
- **C6 (ambiguity): PASS.**
  - No design sits on the 95 % edge (Bolitho 95.9 %, Opie 93.4 %).
  - The roof sheets are bimodal. The four held roofs are 40–65 m below their station, in a valley bottom, with frost lying. Every other approved roof is on open ground within 11 m of its station, with "No frost lay at the house".
  - Tregear (vale bottom) is returned for overvoltage. 9.3 covers Approved designs only, so it gets no countersign.
- **C7 / C8 / C9: PASS.**
  - The verifier runs separately (`verifier_environment_mode: separate`).
  - No seeded W46 countersign, held list or week line exists. "Countersign" appears only in the DS-6 clause text.
  - The tests are deterministic.
- **Cross-reference: PASS.** Rubric and pytest do not overlap. The rubric grades reasons, T_min values, units, revisions and limits in the reply. Pytest grades app state and tool calls. Playbook §4 found 0 double-counted, 1 partial (read and dismissed in 03) and 25 independent.

## Trap fairness (decided on the merits)
- **The rule is current and stated plainly.**
  - Confluence 461002 is DS-6 Edition 4, in force from 1 Oct 2026, and states both halves of 9.3 and the 2.3 definition.
  - If the roof condition were always true, the clause's first half would say nothing. A careful designer therefore has to ask whether each roof sees colder mornings than the station's open ground. That is a fair expert inference: frost hollows and cold-air drainage are core PV cold-temperature knowledge.
  - The delivered Opus run proves the inference is reachable. At step 34 its own reasoning says: "The DS-6 and 9.3 definitions tie a station's extreme minimum to the open ground it sits on and the roof's coldest morning, so I'm checking whether any survey notes that the site's elevation or frost-hollow conditions differ from the station's."
- **The field sheets are reachable and plainly named.**
  - The instruction names "the site surveys on Dropbox". The sheets are in a folder named `Field sheets` inside `Site surveys`.
  - A recursive `list_folder` of `/Design Desk` (Opus step 34) returns the folder and all 20 `FS-46xx.md` paths. `download_file` returns their text.
  - Each sheet says "Filed with site survey SS-46xx".
  - FS-4604 reads: "The house stands at the bottom of the combe … ground rises on three sides … Ground level at the house: 61 m AOD. Climate station … ASH — Ashcombe, on open ground at 117 m … Ground frost lay white on the garden and the roof until late morning, after the fields above had cleared."
- **Corroboration.**
  - Airtable station elevations: ASH 117, CRS 236, KLD 52, FNS 163 m.
  - Airtable recCN0004 (2025): "Every station in the list is sited on open, level ground …; its figures are open-ground figures."
  - Morwenna Penrose is "Head of Engineering" in the DS-6 header and the climate memo, and is a Linear user.
- **Nothing contradicts the sheets.**
  - The reviewer grepped every world_data app and every data/ file, including the docx. Maps carries geocodes only, with no elevations.
  - The SS survey files carry no terrain data.
  - The sheets are dated 2026-10-09 to 2026-10-27, with no reissue or amendment framing. This is not stale data in disguise.
- **The expert gets 1.0.** The oracle's 114-call replay equals solution/gt_env.json exactly, and harbor scored it 1.0/1.0.

## Live events: none
- `grep ATLAS_EVENT|after_writes|event_dir` over the 15 wired servers' software, tests, task.toml and solve.py is empty.
- The task layer carries only stock-crash fixes, with output shape kept.
- The delivered run's end_env differs from tests/old_env.json only by the run's own writes:
  - HubSpot: 20 deals × {design_status, max_string_voc, modules_per_string, updatedAt, lastmodifieddate}.
  - Linear: 11 issues added.
  - Airtable, Box, Confluence, Dropbox, Gmail, Notion, Outlook and Slack are identical to the seed.

## Critical Findings (fire-worthy)
None.

## Major Findings (embarrassing in review)
None open. The stale-build packaging finding (fix 2) is fixed: the input validates and the fin9 build carries fix 1.

## Minor Findings (polish)
None open. The one minor found in this pass (the task.toml stray-rule wording) is fixed above.

## Coverage Holes
None.
- Verdicts, Voc and lengths: seven tests.
- Rework issues: one.
- 9.3 act on the roof holds: 4 × 5 + 4 × 3.
- 95 % holds: 1.
- Field-sheet read before the line: 3.
- Week line: 5 + 1.
- Six guards.
- Rubric: 20 positive criteria for reasons and reply bullets, 4 penalties.

## CLEARED (considered and dismissed — with reasons)
- **The stray check sits inside all 8 roof tests (one stray costs 32/50).** It fires only on Kitto, Angwin or Opie: at or above station level, within 95 %, plainly releasable. Over-cautious holds of roofs below their station are exempt. It is the anti-blanket defence. The stray replay scores 0.36 against trap-miss 0.20, and no channel is zeroed.
- **W45 precedent `Released: 11` of 11.** Its documented near-limit approvals are 94.2 % (LSK) and 89.6 % (Carne). No W45 record puts a roof below its station, so it does not contradict 9.3.
- **The handbook and checklist omit 9.3.** Both are convenience extracts. Neither says to release every approval. DS-6 governs, and the instruction points to it.
- **Older decoys** (Lumen rev A, the May Airtable export, Edition 3, the AR-6.0 600 V quick reference). They are static from step 0 and named as uncontrolled by DS-6 2.1–2.3. They are not the trap under test.
- **task.toml `apps` (7) is a subset of `mcp_servers` (15).** build.py wires `mcp_servers`, and validate requires apps ⊆ servers, which holds (structure S3 apps_not_wired []).
- **oracle.json key `unmoved` (event-era name).** It is internal, not agent-visible, and now lists all 20 deals.
- **Rounding:** Curnow is 75.4 % in TRUTH.md and 0.7545 in oracle.json. It is not graded.
- **Stock filler in old_env** (/Woodworks and /SHPA files, BUG-* issues in other teams). This is the harness's vendor merge; no test reads it.
- **Sweep WARNs** are argument-guess misses and custom-attribute notes, all off the trap path. Sweep reports 0 errors.
- **Read test pays a read-but-ignore run (0.26 pytest).** REDESIGN_S6 §5 mandates the 3-point read. The required trap-miss replay (sheets never opened) gives 0.20. A read-but-ignore run's reward is about 0.21.
- **r-kestrel-units cites "−138 mV/°C".** The instruction asks "how you handled temperature coefficients, units included", so this is not over-specification.
- **`deliver.sh` was not run.** It calls `run.sh --only validate --only build`, which the coordinator's constraints forbid in this session. The delivery folder was built per QC_FINAL6 step 1 from the packaged bundle instead. check_bundle, structure and playbook all pass on it.

## What I Verified Clean (final bytes)
- **check_bundle** after the fix: 0 FAIL, 0 WARN. sweep: 0 error(s). simcheck batch30: 0 flagged (max cosine: instruction 0.088, rubric 0.049, pytest 0.105).
- **grade_local** after the fix:

  | replay | pytest |
  |---|---|
  | oracle | 1.0000 (50/50) |
  | nop | 0.0000 |
  | trap-miss (no sheets, no roof countersigns, Released 9) | 0.2000; rubric by hand (10 − 3)/42 ≈ 0.17, so both channels are > 0 and ≤ 0.25 |
  | stray on Kitto | 0.3600 |
  | self-correction | 1.0000, no charge |

- **Harbor** (coordinator's fin9 run `/tmp/qc/oracle_nop_20261114_044008`, checksum `fa6ce188…`, the same as the regraded Opus run): oracle 1.0/1.0/1.0 (trial opZ5Mkp); nop 0/0/0 (trial uBCh9hG); judge gpt-5.6-sol via codex.
- **Delivered Opus run** (job `…-215846-regraded`, trial fwYYGti): 0.1834 (pytest 0.2, rubric 0.1667), guards [], tool errors 0. It is classified `instruction-ignored` (see 03).
- **Host paths and hygiene:** the `/Users/` grep over data, world_data and instruction.md is empty. No __pycache__ in the task or the delivery.
- **Identity:** UUID v5; schema 1.4; author Priyanshi Joshi <priyanshi.joshi@ethara.ai>; agent_timeout_sec 7200; 35 text data files; 15 wired servers; no tests/task_lib.py.
- **Counts:** rubric 24 criteria (20 positive, 42 points; 4 penalties, 8 points), all final_answer, ±1/3/5. Tests: 26 (20 positive, 50 points; 6 guards), weights in {±1, ±3, ±5}.
