All four deliverables are in place, in order. Sessions left open as you asked.

---

## 1. Section counts by Completeness

| | Count | Sections |
|---|---|---|
| **Complete** | **22** | S01–S07, S09–S15, S17–S21, S24, S25, S30 |
| **Gap** | **4** | S16, S22, S23, S29 |
| **Not applicable** | **4** | S08, S26, S27, S28 |

Subject line sent: `Kestrel-3 TF readiness: 22 complete, 4 gap, 4 not applicable, 767 pages`

## 2. Revisions where the choice wasn't the obvious one

| Section | Cited | Why, and the record that makes it the version in force |
|---|---|---|
| **S20** DOC-1111 | **Rev C**, 29 pp | Rev C is the *highest* revision but the register still shows Rev B. **ServiceNow CHG0041102 is Closed, implemented 2026-11-12** → approved from the moment of release under rule 4.2(b) / QA-SOP-007 6.4. The register entry follows at the Friday sync. |
| **S07** DOC-1133 | **Rev F**, 64 pp | Rev G (68 pp, 0 placeholders) sits in the store as *routed for approval* and the **register shows it "In approval"** → not approved (4.3). No change request covers it. Rev F is the highest Approved revision (CHG0040611). |
| **S15** DOC-1102 | **Rev C**, 33 pp | Rev D (58 pp) is routed for approval, **register "In approval"**, and its release **CHG0041150 is still "Scheduled"**, not closed → not approved under either limb of 4.2. Rev C is Approved (CHG0040611). |
| **S29** DOC-1200 | **None in force**, 0 pp | Rev A was released under CHG0040990, but the **register records the approval withdrawn 2026-11-11 under CAPA-0912** → not in force (4.4), and a withdrawal does not reinstate an earlier revision. There is no earlier revision anyway. |
| **S16** DOC-1103 | **Rev C**, 87 pp | Rev C *is* in force (register Approved, CHG0040877) — the non-obvious part is that it is still a **Gap**, because the store records 1 open placeholder. Pages still count. |
| **S22** DOC-1188 | **Rev B**, 24 pp | Same shape: Rev B in force (register Approved, CHG0040815) but 2 open placeholders → Gap, pages still count. |
| **S23** DOC-1120 | **None in force**, 0 pp | Rev A is a **working draft** in the store, **register "Draft"**, and the early-release **CHG0041004 was Canceled** → nothing approved (4.3, 4.7). |

Everywhere else the highest store revision is the one the register shows Approved.

## 3. Departures from Ines's working draft

Seven rows, plus her totals:

| Row | Ines | Mine | Record that made me depart |
|---|---|---|---|
| **S15** | DOC-1102 **Rev D**, 58 pp, Complete | **Rev C**, 33 pp, Complete | Register: Rev D "In approval"; store: "routed for approval"; CHG0041150 "Scheduled". Her note said "Rev D is the current architecture" — current is not approved. |
| **S16** | Rev C, 87, **Complete** | Rev C, 87, **Gap** | Store version history for Rev C: `open placeholders: 1`; CHG0040877 names it (penetration test annex). Rule 4.6. |
| **S17** | **DOC-1047** Rev E, 46 pp | **DOC-1074** Rev D, 39 pp | **DHF master index**: S17 is satisfied by DOC-1074 Usability Engineering File. DOC-1047 is the risk management report (the digits are transposed). Her note read "usability file". |
| **S20** | **Rev B**, 27 pp | **Rev C**, 29 pp | CHG0041102 Closed/implemented 2026-11-12. Her note "register shows Rev B" was right about the register but the register lags the sync; 4.2(b) governs. |
| **S25** | **N/A**, Not applicable | **DOC-1162 Rev A**, 26 pp, Complete | STD-014 §5 and §5.1: S25 applies to near-patient testing by health professionals, which is exactly the Kestrel-3 intended use (DHF master index, submission hub). Her note "home/self-test - n/a" conflated near-patient with self-testing. |
| **S29** | Rev A, 22 pp, **Complete** | **None in force**, 0 pp, **Gap** | Register: "Approval withdrawn", 2026-11-11, CAPA-0912. Her note "approved 29 Sep" pre-dates the withdrawal. |
| **S30** | **N/A**, Not applicable | **DOC-1205 Rev B**, 11 pp, Complete | STD-014 **Edition 3** §5: SSP applies to class C and D. Her note cited the Edition 2 rule ("class D only"); Edition 2 is superseded. |
| Totals | 828 pp; 22/2/6 | **767 pp; 22/4/4** | Consequences of the above, plus the shared-document rule 4.9. |

Her Complete count coincidentally also came to 22, but it is a different set of sections.

## 4. Not-applicable sections and reasons

- **S08 Instructions for use – lay user** — STD-014 §5: self-testing devices only. Kestrel-3 is professional near-patient testing; the IFU is written for professionals. The Home-concept lay IFU **DOC-1134** is an uncontrolled draft for a possible future product and does not make S08 applicable (§5.1).
- **S26 Self-testing – lay-user performance study** — §5: self-testing devices only. Same reasoning; **DOC-1161** is an uncontrolled Home-concept draft.
- **S27 Companion diagnostic – medicinal product consultation** — §5: companion diagnostics only. No Kestrel-3 assay selects patients for a medicinal product (DHF master index; device summary).
- **S28 Batch verification by an EU reference laboratory** — §5: class D only. Kestrel-3 is **class C** under classification rule 3 (DHF master index; DOC-1003).

No applicable section was marked Not applicable to hide a gap.

## 5. Gaps and reasons

- **S16** (KTF-7) — DOC-1103 **Rev C in force** but with **1 open placeholder**, the penetration test annex. Gap by 4.6, not by absence.
- **S22** (KTF-8) — DOC-1188 **Rev B in force** with **2 open placeholders** (18-month real-time data §6.3; in-use stability at 30 °C §7.2). Both data sets now exist, so this closes as soon as document control releases the next revision.
- **S23** (KTF-9) — DOC-1120 has **no version in force**: the only revision is a working draft (74 pp, 6 placeholders), register "Draft", and the early-release change request was cancelled. Database lock is planned 9 December.
- **S29** (KTF-10) — DOC-1200 Rev A **approval withdrawn** under CAPA-0912, nothing earlier to fall back on. Rev B is being drafted.

Tickets open with `TF-GAP S16` / `S22` / `S23` / `S29` respectively. No ticket for Complete or Not-applicable rows.

## 6. How I arrived at the page total — 767

Rule 4.9: sum, over the **distinct documents cited with a version in force**, of that version's pages. **23 distinct documents**:

1001 **28** · 1002 **9** · 1003 **12** · 1004 **16** · 1005 **14** · 1130 **22** · 1133 **64** · 1020 **41** · 1021 **18** · 1030 **57** · 1046 **15** · **1047 46** · 1102 **33** · 1103 **87** · 1074 **39** · 1080 **63** · 1110 **34** · 1111 **29** · 1112 **31** · 1188 **24** · 1121 **48** · 1162 **26** · 1205 **11** = **767**

Three things drive it:
- **DOC-1047 Rev E (46 pp) counts once**, though cited by both S13 and S14 — the Edition 3 addition to 4.9. Ines's 828 double-counted it.
- **S16 (87) and S22 (24) do count** — they are gaps because of placeholders, but a version *is* in force, and 4.9 keys on "version in force", not on Completeness.
- **S23 and S29 add nothing** (no version in force), and the four N/A rows add nothing.

Page counts are the store's, not the September dry-run's.

## 7. Glossary terms left out of the index

Five of the twenty-one, and 16 indexed:

- **Reagent pack** — register status **Retired** (2026-11-05, replaced by Cartridge). §6.2.
- **Measuring interval** — register status **Retired** (2026-10-22). §6.2.
- **Residual risk acceptability matrix** — register status **Proposed**, not adopted. §6.2.
- **Lay user** — Active, but its source document **DOC-1134** is cited by no section of the ToC (S08 is Not applicable and carries "N/A"). §6.2.
- **Self-test result** — Active, but its source document **DOC-1161** is likewise cited by no section (S26 N/A). §6.2.

I read the **Notion register**, not the 30 October CSV export in the data folder — the export predates the Reagent pack and Measuring interval retirements and would have put two retired terms in the index.

Two judgement calls inside the index worth flagging: **Hazardous situation** and **Benefit-risk ratio** are both filed under **S13**, the lowest-numbered applicable section citing DOC-1047 (§6.3), not S14. **Shelf life | S22 | DOC-1188** and **Post-market surveillance | S29 | DOC-1200** are indexed even though those sections are gaps, as §6.2 requires.

## 8. For document control to pick up

1. **Register sync owed for DOC-1111 Rev C** — released 12 November under CHG0041102; the register still shows Rev B as Approved. Pieter is on leave 13–18 November and the Friday sync may slip, so this may still be outstanding when Nordmark reads the ToC. The ToC cites Rev C on the change request; it would read better if the register agreed.
2. **DOC-1133 Rev G** — envelope env-ks3-1133g sent 12 November, awaiting your signature and Rafaela's. If it completes before Wednesday, S07 moves to Rev G / 68 pp and the total to 771. I have not touched the envelope.
3. **DOC-1102 Rev D** — envelope sent 5 November; release CHG0041150 still Scheduled. Four review comments (RC-004, 008, 012, 016, 020, 024) are still open on Rev D, so it may not be imminent.
4. **DOC-1188 Rev C** — both placeholder data sets are complete and in spec per Yannick's 9 November status; only the release under a change request is missing. Cheapest gap to close before Wednesday.
5. **DOC-1200 Rev B** — needed to close S29 under CAPA-0912.
6. **DOC-1103** — the penetration test annex is the only thing between S16 and Complete.
7. **KTF-4** (glossary clean-up) is still In Progress; the index I built reflects the register as it stands today, so if any term status changes before Wednesday the index needs a re-run.

Nothing was written outside the four places you named. No DocuSign action, no register change, no re-statusing, nothing to the NB 2291 Dropbox folder, and the only mail sent was the readiness statement to you. I did not sign out of anything.