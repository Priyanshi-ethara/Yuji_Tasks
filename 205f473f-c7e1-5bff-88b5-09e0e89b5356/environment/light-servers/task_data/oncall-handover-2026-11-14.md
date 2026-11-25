# Triage desk hand-over — Friday 14 Nov 2026 (Tobin Marsh -> Ines Varga)

**Open groups on the register:** 22 for fleetd (the register in Airtable is the list; the Sentry list view also
shows four old groups that are resolved or ignored and three dispatch-web groups, none of them ours this week).

**What I did:** exported the list view and drafted owners from the culprit column into
`triage-draft-culprits.csv`. Six groups have simkit on top and one is the simctl replay crash, so the draft has seven for Sim Tools again; Odile said
in #sre-triage they will take them like last week. Three groups have a vendored library on top (kafka-go, pgx, the
pellam-oss queue) and I parked those with Platform, who own /vendor/. The generated validator one I gave to API
Contracts because the culprit is in internal/gen.

**Not done:** none of the Monday steps. Register still blank, no team tickets, no summary in #sre-triage.

**Things that happened this week**
- fleetd 4.12.0 went out on Mon 10 Nov (exporter batch size raised to 512, digest scheduler rewrite), 4.12.1 on
  Thu 13 Nov (lease renewer change, quote page).
- 13 Nov 14:00–19:30 UTC: push provider outage. Retries piled up; three OOM groups that afternoon (two in notify,
  one in the settlement queue). PagerDuty incident PD-7731.
- Billing (Kofi) asked again that anything under internal/billing goes to Billing, queue included. I told him the
  desk follows the ownership file and the handbook, not requests in chat.
- Datadog goroutine monitor for fleetd-workers alerted twice; export of the counts is in the folder.

**Reminder:** the handbook in Confluence (SRE space) is what the desk follows; my draft is a starting point only.
