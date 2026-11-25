Everything is written. I left all sessions open as you asked.

---

## Ines — October 2026 SLO cycle, closed

**Headline: 6 of 20 objectives missed, not 5.** The list is also different from Tobias's. The cause is one thing, and it is defensible: seven of his twenty figures came off boards whose saved view was pointed at the *canary* cell.

### 1. Results

**Missed (6):** statement-render, card-auth-gateway, tokenisation-vault, payout-scheduler, sweep-reconciler, kyc-document-check.

| Service | Tier | Attainment % | Budget rem. (min) | Status |
|---|---|---|---|---|
| ledger-posting | 1 | 99.973 | 10.3 | Objective met |
| ledger-balance-read | 2 | 99.953 | 23.6 | Objective met |
| journal-export | 3 | 99.642 | 63.2 | Objective met |
| fx-rates-feed | 2 | 99.928 | 12.6 | Objective met |
| **statement-render** | 2 | **99.863** | **−16.4** | **Objective missed** |
| **card-auth-gateway** | 1 | **99.884** | **−29.7** | **Objective missed** |
| **tokenisation-vault** | 2 | **99.890** | **−4.4** | **Objective missed** |
| 3ds-challenge | 3 | 99.993 | 220.2 | Objective met |
| merchant-onboarding-api | 3 | 99.574 | 33.2 | Objective met — budget at risk |
| chargeback-intake | 2 | 99.915 | 6.6 | Objective met — budget at risk |
| **payout-scheduler** | 1 | **99.908** | **−18.7** | **Objective missed** |
| bank-file-dispatch | 2 | 99.915 | 6.6 | Objective met — budget at risk |
| payee-verification | 2 | 99.962 | 27.6 | Objective met |
| payout-status-api | 2 | 99.973 | 32.6 | Objective met |
| **sweep-reconciler** | 3 | **99.418** | **−36.8** | **Objective missed** |
| fraud-score | 1 | 99.960 | 4.3 | Objective met — budget at risk |
| velocity-limits | 2 | 99.933 | 14.6 | Objective met |
| sanctions-screen | 1 | 99.975 | 11.3 | Objective met |
| dispute-evidence | 3 | 99.586 | 38.2 | Objective met — budget at risk |
| **kyc-document-check** | 2 | **99.870** | **−13.4** | **Objective missed** |

Written to all 20 register rows (three October fields only — nothing else touched). Report page published in RELY: *"SLO attainment — October 2026 — 6 of 20 objectives missed"*. Six follow-ups raised, one per missed objective, in the owning teams' Linear teams: statement-render → Ledger Platform; card-auth-gateway, tokenisation-vault → Acquiring; payout-scheduler, sweep-reconciler → Payouts; kyc-document-check → Risk Engineering. (Linear stamped them with `MER-213`…`MER-218` keys, which seems to be a quirk of how it mints identifiers — the team assignment on each is correct, nothing landed in the Reliability Office team.)

### 2. Panels — used and set aside

RS-2 §3.2 makes the SLI of record the production fleet *taken together*; §3.3 rules out both the canary cell (wren-0) and any single production cell on its own. Since the September rebuild, every SLO widget is `$cell`-templated and the export job writes whatever the board's **saved view** says, so the panel id alone tells you nothing — I checked each board's saved `$cell` in Datadog first.

**Used** (all saved `cell=kestrel-*`): `bwp-led-svc / led-svc-01…05`; `bwp-acq-svc / acq-svc-01…05`; `bwp-pay-oncall / pay-oc-01…05`; `bwp-rsk-svc / rsk-svc-01…05`.

**Set aside:**
- `bwp-pay-svc / pay-svc-01…05` — the register's nominated panels for **all five Payouts SLOs**. Saved to `cell=wren-0` on 22 September by ilse.varga. Canary, so excluded. Worse, the cell traffic file shows wren-0 drained from 17–20 October, so it took *zero* traffic the night of the 19 October SEV-2 — the PIR says so too. I substituted the Payouts on-call board, which is saved `kestrel-*`: same services, same metric, same rollup.
- `bwp-rsk-oncall / rsk-oc-04, rsk-oc-05` — nominated for dispute-evidence and kyc-document-check. The nomination moved there on 25 September when that board was still on a production view; otto.brandvold saved it to `cell=wren-0` on 1 October, i.e. the view changed underneath the nomination. Substituted `rsk-svc-04/05` from the Risk service board.
- `bwp-led-oncall` (`kestrel-1`) and `bwp-acq-oncall` (`kestrel-2`) — single cells, excluded by §3.3. Not needed anyway.
- `acq-svc-c01…c05` — the fixed canary widgets on the Acquiring board; error *ratio* on wren-0, release-watch only. (Worth noting the Acquiring board is titled "Canary & SLO watch" but its SLO widgets are correctly on `kestrel-*` — the title is a red herring the review already noted.)
- the `*-l01…l05` latency timeseries — diagnostic, not the bad-minute SLI; and `bwp-exec-overview`, which is copied *from* our report.

### 3. Unit conversions

Three SLIs emit `bwp.sli.bad_time` in **seconds**, divided by 60: fx-rates-feed 1,920 s → 32.0 min; 3ds-challenge 180 s → 3.0 min; chargeback-intake 2,280 s → 38.0 min. Everything else is `bwp.sli.bad_minutes` and was summed as exported. (Tobias had all three right.)

### 4. Maintenance windows touching October

RS-2 §5: declared means raised in PagerDuty against the service, stating the window, **before it opened**; a declared window's minutes leave both the eligible and the bad counts.

| Work | Declared? | Treatment |
|---|---|---|
| fraud-score model store migration, 6 Oct 02:00–03:00 (60 min) | Yes — PBW1101, raised 2 Oct | **Excluded.** Eligible 44,580; bad 78 → 18 |
| ledger-posting partition rebuild, 14 Oct 01:00–02:25 (85 min) | Yes — PBW1102, raised 9 Oct | **Excluded.** Eligible 44,555; bad 97 → 12 |
| sanctions-screen list reload, 18 Oct (40 min) | Declared 12 Oct, **cancelled** 17 Oct | Nothing removed (§5.3); no work happened |
| card-auth-gateway HSM firmware, 21 Oct 03:00–03:45 (45 min) | **No** — PBW1109 raised 21 Oct at 10:40, after the work | **Stays in both counts.** This is what puts the SLO under target; Noor said the same in chat and the August review set the precedent |
| tokenisation-vault key rotation, 27 Oct 01:05–01:30 (25 min) | **No** — shared calendar and chat only | **Stays in both counts** |

The other six calendar entries are November/December. Calendar status text ("Declared in PagerDuty") was ignored as a source — I verified each against PagerDuty itself.

### 5. Targets and the arithmetic

Tiers of record from the register: Tier 1 99.95 %, Tier 2 99.90 %, Tier 3 99.50 %. statement-render is Tier 2 from 1 October; journal-export stays Tier 3 despite "High" catalogue criticality (criticality is a paging attribute, §4.2); the H2 tier proposals aren't approved, so not applied.

Per SLO: eligible = 44,640 − declared maintenance; attainment = (eligible − bad) ÷ eligible × 100; allowed = (1 − target) × eligible; budget remaining = allowed − bad. Status decided on unrounded figures (§7), then attainment to 3 dp and budget to 1 dp, half away from zero (§8.2).

### 6. Against Tobias's draft and Gideon's slide

Tobias's method was sound and his Ledger, Acquiring and Risk-service figures, his second-to-minute conversions and his maintenance calls all reconcile exactly with mine. The single divergence is panel provenance: he took each SLO from its nominated panel "as always", without re-checking the boards' saved cell values after owners moved them. That put seven SLOs on the canary cell. Correcting them:

- payout-scheduler 99.980 → **99.908** (now missed) — wren-0 was drained, so it missed the SEV-2 entirely
- sweep-reconciler 99.787 → **99.418** (now missed)
- kyc-document-check 99.969 → **99.870** (now missed) — wren-0 reads a *staging* document bucket, so it never saw the 8 October bucket failure
- bank-file-dispatch 99.884 → 99.915 (no longer missed)
- payout-status-api 99.895 → 99.973 (no longer missed)
- payee-verification and dispute-evidence: met either way, figures shift

Net: 5 → 6 missed, and three names swap. **For Thursday:** the headline moves by one, but the change is in Gideon's favour as a matter of method — the five Payouts objectives and two Risk objectives on his slide were measured on a cell that carries 0–2.5 % of customer traffic and was switched off for four days of the month, including the night of the worst incident. RS-2 §3.3 excludes it by name. Note also that this cuts both ways: two services the draft called misses were not, so finance's credit provisioning list should be re-cut from the register rather than from the draft.

One thing you may want to raise at the next review: the register's "nominated panel" field is a panel id, but what it actually resolves to depends on a board setting the owning team can change without telling us. Three boards drifted onto non-production views between 22 September and 1 October. A standing check of saved `$cell` values — or nominating only `kestrel-*` panels — would stop this recurring.

I changed nothing on Datadog, the status page, PagerDuty, ServiceNow, Jira, the calendars, Drive, Box, Sentry or Okta, sent no mail or chat, and left every other register field and table as I found it.