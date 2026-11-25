# Reliability Office handbook (rev. 7, 2026-09-29)

Owner: Ines Calloway, Head of Reliability Office. Analysts: Tobias Renwick, Noor Haddad.

## 1. What the office does
1.1 Publishes the monthly SLO attainment report for every SLO in the SLO register.
1.2 Raises one follow-up per missed objective in the owning team's Linear team.
1.3 Keeps the SLO register current (tiers, owners, nominated panels) between reviews.
1.4 Does not operate services, does not run incidents and does not speak to customers.

## 2. Where things live (systems of record)
| Record | System | Notes |
|---|---|---|
| Reliability standard RS-2 (targets, measurement, labels) | Confluence, space RELY | The only governing text for attainment. Amended by the reliability review; the wiki page is the edition in force. |
| SLO register | Airtable base "Reliability Office", table "SLO register" | Source of record for tier, owning team and nominated panel. Maintained live by the office. |
| Service boards, monitors | Datadog | Owned by the service teams and the observability platform. The office reads them and never edits them. |
| Maintenance declarations and incidents | PagerDuty | Declared windows are raised there by the owning team. |
| Change records | ServiceNow | Change approval. Owned by the change advisory board. |
| Planned maintenance calendar | Google Calendar (shared) | Planning only. |
| Cell topology, board conventions | Confluence, space PLAT | Owned by the platform team. |
| Follow-ups | Linear, one team per domain | Ledger Platform, Acquiring, Payouts, Risk Engineering. The office's own team (Reliability Office) is for office work, not follow-ups. |
| Monthly report | Confluence, space RELY | One page per month. |
| Customer status page | WordPress (status.brightwater-payments.example) | Owned by Customer Communications. Never written by the office. |

## 3. Monthly cycle
- Day 1–2: the export job runs; analysts check the pack.
- Day 2–4: compute attainment per RS-2, write the register's month fields, raise follow-ups.
- Day 5: publish the report page; the head of office replies to the VP Engineering.

## 4. Conventions
4.1 The register's month fields are numbers (attainment as a percentage, budget remaining in minutes) and a status
label copied from RS-2.
4.2 A nominated panel is the panel an owning team chose to display its SLO on its board. Teams change their boards
without telling us; the register lags.
4.3 Since the September rebuild (board-rebuild-notes-2026-09.md) every service board is templated; see the platform
team's conventions page.
4.4 Analysts work from the exports in the pack; the monitoring server is there to answer questions about them.

## 5. History that explains a convention
- Until June 2026 attainment was request-based; RS-2 moved to bad minutes in July 2026 so that low-traffic services
  are not flattered by quiet nights.
- Tier 3 was introduced in August 2026 for back-office services.
- In September 2026 statement-render moved from Tier 3 to Tier 2 (customer statements are now on the merchant
  dashboard); the register carries the change from 1 October.
