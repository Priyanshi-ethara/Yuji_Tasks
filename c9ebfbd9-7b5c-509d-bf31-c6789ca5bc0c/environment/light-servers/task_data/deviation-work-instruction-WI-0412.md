# WI-0412 Deviation records for cold-chain outcomes

Work instruction, Quality Systems. Revision 3, effective 15 October 2026 (aligned with QA-SOP-114 Rev 7).
Revision 2 (May 2026) mapped Quarantine to Medium; that mapping is withdrawn.

## 1 Where deviations live
Cold-chain deviations are raised in the deviation tracker, project key **QAD** ("Quality Deviations"). The QMS project holds
change controls and is not used for deviations. Issue type: **Deviation**.

## 2 Priority by outcome (Rev 3)

| Outcome on the lot card | Priority |
|---|---|
| Reject | Highest |
| Referred to QA Head | Highest |
| Quarantine | High |
| Release with deviation | Medium |
| Release | no deviation is raised |

## 3 Content
3.1 One deviation per lot per round. Describe the shipment, the logger, the lane TOR, the cumulative TOR and the reason.
3.2 When an outcome changes before the round closes, correct the summary and the priority of the existing deviation;
never open a duplicate and never delete a deviation (closed rounds are audited on the tracker history).
3.3 The QA Head is the assignee of referred lots; leave the assignee empty for the other outcomes, Quality Systems triages them.

## 4 History notes
- Q3 2026 audit (IA-2026-07): two duplicate deviations for the same lot in R-2026-31; root cause, reviewers raising a new
  deviation after an outcome changed instead of correcting the open one.
