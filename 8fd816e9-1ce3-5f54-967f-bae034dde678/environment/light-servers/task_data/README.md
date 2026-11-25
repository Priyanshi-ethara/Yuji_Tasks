# October 2026 SLO reporting pack — Reliability Office, Brightwater Payments

Prepared 2026-11-02 by the Reliability Office for the monthly attainment report. Everything in this folder is a
copy; the live records are in the systems listed in the Reliability Office handbook.

## What is here

| File | What it is |
|---|---|
| `panel-catalogue-2026-10.json` | Widget definitions of the eight service boards (two per domain), exported by `boardctl` on 1 November. |
| `export_<board>_2026-10.csv` | One file per board: the daily value of each exported panel for 1–31 October 2026 (UTC days). Column names are widget ids from the catalogue. |
| `service-catalogue.csv` | The engineering service catalogue (owner, criticality, runtime, rotation). |
| `slo-definitions.yaml` | The SLI rule of every registered SLO (what makes a minute bad). |
| `reliability-office-handbook.md` | How the office works, where records live, the monthly cycle. |
| `monthly-reporting-runbook-v4.docx` | The step list analysts follow for the monthly report. |
| `error-budget-policy.docx` | What happens when an error budget runs low or out. |
| `reliability-review-minutes-2026-10-07.docx` | Minutes of the October reliability review. |
| `slo-report-2026-09.md` | The September report as published. |
| `slo-history-2026.csv` | Monthly attainment of every SLO, January–September 2026. |
| `october-attainment-draft-trenwick.csv`, `draft-notes-trenwick.md` | Tobias Renwick's working draft for October and his notes. |
| `maintenance-calendar-2026-q4.ics` | The shared planned-maintenance calendar. |
| `release-train-2026-10.log` | Deploy pipeline log for October. |
| `incident-review-*.md` | Post-incident reviews for October. |
| `oncall-handover-2026-10.txt` | Weekly on-call handover notes. |
| `cell-traffic-share-2026-10.csv` | Daily share of customer requests by serving cell. |
| `status-page-notices-2026.csv` | Notices published on the customer status page this year. |
| `merchant-escalations-2026-10.csv` | Merchant support escalations raised in October. |
| `team-directory.csv` | Who is who. |
| `export-job-run-2026-11-01.log` | The nightly board export job's log for the run that produced the CSVs. |
| `chat-export-reliability-office-2026-10.txt` | Export of the #reliability-office channel for October. |
| `tier-review-proposals-2026-h2.csv` | Tier changes proposed for the H2 review. |
| `board-rebuild-notes-2026-09.md` | Observability team notes on the September board rebuild. |
| `sentry-weekly-digest-2026-10.txt` | Weekly error digests. |
| `customer-impact-ledger-2026-10.csv` | Finance's estimate of customer impact per incident. |

## How the exports are produced

The nightly export job (`boardctl export`, run log beside this file) opens each service board and writes the daily
value of every exported panel exactly as the board shows it. Nothing is recomputed on export; values are in the unit
the widget declares in the catalogue. Days are UTC calendar days.
