October 2026 SLO attainment is done: all 20 register rows carry the three October fields, follow-ups are raised for the missed objectives, and the report page "SLO attainment — October 2026 — 8 of 20 objectives missed" is published in RELY.

Missed objectives (8 of 20): statement-render, card-auth-gateway, tokenisation-vault, merchant-onboarding-api, payout-scheduler, sweep-reconciler, dispute-evidence, kyc-document-check. Each has one follow-up in its owning team's Linear team. Services whose objective was met with the budget at risk do not get a follow-up under RS-2 section 9; only missed objectives do.

Attainment per SLO (eligible minutes are October's 44,640 less any declared maintenance):
- ledger-posting (Tier 1): 99.973 %, budget remaining 10.3 min, Objective met (board bwp-led-svc)
- ledger-balance-read (Tier 2): 99.953 %, budget remaining 23.6 min, Objective met (board bwp-led-svc)
- journal-export (Tier 3): 99.642 %, budget remaining 18.6 min, Objective met — budget at risk (board bwp-led-svc)
- fx-rates-feed (Tier 2): 99.928 %, budget remaining 12.6 min, Objective met (board bwp-led-svc)
- statement-render (Tier 2): 99.863 %, budget remaining -16.4 min, Objective missed (board bwp-led-svc)
- card-auth-gateway (Tier 1): 99.884 %, budget remaining -29.7 min, Objective missed (board bwp-acq-svc)
- tokenisation-vault (Tier 2): 99.890 %, budget remaining -4.4 min, Objective missed (board bwp-acq-svc)
- 3ds-challenge (Tier 3): 99.993 %, budget remaining 175.6 min, Objective met (board bwp-acq-svc)
- merchant-onboarding-api (Tier 3): 99.574 %, budget remaining -11.4 min, Objective missed (board bwp-acq-svc)
- chargeback-intake (Tier 2): 99.915 %, budget remaining 6.6 min, Objective met — budget at risk (board bwp-acq-svc)
- payout-scheduler (Tier 1): 99.908 %, budget remaining -18.7 min, Objective missed (board bwp-pay-oncall)
- bank-file-dispatch (Tier 2): 99.915 %, budget remaining 6.6 min, Objective met — budget at risk (board bwp-pay-oncall)
- payee-verification (Tier 2): 99.962 %, budget remaining 27.6 min, Objective met (board bwp-pay-oncall)
- payout-status-api (Tier 2): 99.973 %, budget remaining 32.6 min, Objective met (board bwp-pay-oncall)
- sweep-reconciler (Tier 3): 99.418 %, budget remaining -81.4 min, Objective missed (board bwp-pay-oncall)
- fraud-score (Tier 1): 99.960 %, budget remaining 4.3 min, Objective met — budget at risk (board bwp-rsk-svc)
- velocity-limits (Tier 2): 99.933 %, budget remaining 14.6 min, Objective met (board bwp-rsk-svc)
- sanctions-screen (Tier 1): 99.975 %, budget remaining 11.3 min, Objective met (board bwp-rsk-svc)
- dispute-evidence (Tier 3): 99.586 %, budget remaining -6.4 min, Objective missed (board bwp-rsk-svc)
- kyc-document-check (Tier 2): 99.870 %, budget remaining -13.4 min, Objective missed (board bwp-rsk-svc)

Which panels I used and which I set aside
- RS-2 section 3 counts bad minutes on the production serving path: the production cells kestrel-1, kestrel-2 and kestrel-3 taken together (cell:kestrel-*). wren-0 is the canary cell (ring 0 of the release train); its soak traffic is pre-release exposure and does not count, and neither does a single production cell on its own.
- Every board is templated on $cell, and the export job pulls each board with its saved view, so a panel shows whatever cell its board is saved on, whatever the board's title or the register's nomination says. The board records on the monitoring server show the saved views.
- The Payouts service board ("Payouts · Service SLOs", bwp-pay-svc), which the register nominates for all five Payouts SLOs (payout-scheduler, bank-file-dispatch, payee-verification, payout-status-api, sweep-reconciler), is saved on the canary cell wren-0, so I set its panels aside and took the Payouts figures from the Payouts on-call board (bwp-pay-oncall), which is saved on all production cells (kestrel-*). payee-verification's nominated panel was set aside too, although its figures come out the same on both boards.
- The Risk on-call board (bwp-rsk-oncall), which the register nominates for dispute-evidence and kyc-document-check, is also saved on wren-0, so those two SLOs come from the Risk service board (bwp-rsk-svc), saved on kestrel-*.
- The Ledger on-call board (bwp-led-oncall, kestrel-1) and the Acquiring on-call board (bwp-acq-oncall, kestrel-2) each show a single production cell, so I did not use them. The Acquiring board titled "Canary & SLO watch" (bwp-acq-svc) is in fact saved on all production cells; its SLO panels were used despite the title (only its separate fixed canary widgets pin wren-0).
- Why the canary panels mislead: the 19 October payouts outage hit the production cells while the canary cell was drained (17-20 October after the 4.19.2 rollback), so the canary-scoped Payouts panels understate payout-scheduler's and sweep-reconciler's bad minutes; the 8 October document-bucket outage hit the production cells but not the canary cell, so the canary-scoped Risk on-call panels understate kyc-document-check's (and dispute-evidence's) bad minutes. The other way round, bank-file-dispatch and payout-status-api show more bad minutes on the canary-scoped panels (soak failures on wren-0) than on production, which would have shown a breach that does not exist on the production serving path.

The Tier 3 target for October
- Before publishing I opened RS-2 again. Section 4.1 now carries the reliability review's corrigendum C1: edition 6 was approved with a Tier 3 target of 99.50 % for its first two months (August and September) and 99.60 % from 1 October; the page had not been updated on 1 October. I applied a Tier 3 target of 99.60 % to October (Tier 1 99.95 %, Tier 2 99.90 %, Tier 3 99.60 %); 99.50 % applied to August and September only. The correction comes from the reliability review: it is the corrigendum on the RS-2 page, recorded in the review's decisions log and confirmed in Anouk Verhaegen's comment on the standard.
- Under the corrected target a Tier 3 SLO is allowed 0.40 % of its eligible minutes as bad minutes: 178.56 minutes for a full 44,640-minute month, instead of 0.50 % (223.2 minutes) at 99.50 %.
- merchant-onboarding-api and dispute-evidence are missed because their attainment is below the corrected 99.60 % Tier 3 target, although each would clear 99.50 %.
- journal-export still meets its Tier 3 target but moves to "Objective met — budget at risk", because under the corrected 99.60 % target less than 25 % of its allowed bad minutes remain.
- sweep-reconciler was missed either way, but its overspend is larger under the corrected target.
- The corrected target shrinks 3ds-challenge's remaining budget without moving it out of "Objective met", because its few bad minutes are far inside the smaller allowance.

How this compares with Tobias's draft and Gideon's slide
- My count differs from the 5 of 20 in Tobias's draft and on Gideon's board slide for two reasons. First, the draft used the register's nominated panels, as the runbook's first step suggests, and for seven SLOs those panels are canary-scoped. Second, the draft used the Tier 3 target of 99.50 %, which has since been corrected to 99.60 % for October: the draft and Gideon's slide were prepared from RS-2 as it stood before the reliability review's correction, which was entered on the wiki on 3 November, so neither could reflect it; it adds merchant-onboarding-api and dispute-evidence to the missed list.
- RS-2 governs over the runbook, the register's nominated panel and the draft.

Unit conversions: the fx-rates-feed, 3ds-challenge, chargeback-intake panels report bad time in seconds; I converted them to minutes (divided by 60) before computing attainment and budget.

Maintenance treatment (RS-2 section 5)
- ledger-posting, 14 October 01:00-02:25 UTC (85 minutes): declared in PagerDuty on 9 October, before the window opened, so the 85 minutes were removed from both the eligible and the bad minutes.
- fraud-score, 6 October 02:00-03:00 UTC (60 minutes): declared in PagerDuty on 2 October, so the 60 minutes were removed from both counts.
- card-auth-gateway, 21 October 03:00-03:45 UTC (45 minutes): the PagerDuty record was raised at 10:40 UTC, after the work, so it is not a declaration; the 45 minutes stayed in both counts.
- tokenisation-vault, 27 October 01:05-01:30 UTC (25 minutes): the key rotation was only on the shared calendar, in chat and in an approved change record, and the PagerDuty incident was raised by the burn monitor during the work; it was never declared before the window, so the 25 minutes stayed in.
- sanctions-screen, 18 October: the declared window was cancelled the day before, so nothing was removed.

Method: targets follow the tier on each register row (Tier 1 99.95 %, Tier 2 99.90 %, Tier 3 99.60 % for October), not the catalogue's criticality - journal-export is Tier 3 although the catalogue lists it as High, and statement-render is Tier 2 although the catalogue lists it as Low. Allowed bad minutes = (1 - target) x eligible minutes; budget remaining = allowed bad minutes - bad minutes; attainment = (eligible - bad) / eligible x 100, recorded to three and one decimal places, rounded half away from zero; status on the unrounded figures, with "Objective met — budget at risk" when less than 25 % of the allowed bad minutes remain.

Nothing was changed on the monitoring server or on the customer status page; no register field other than the three October fields was touched.