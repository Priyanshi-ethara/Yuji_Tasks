# Brackmoor control room - systems guide (rating desk extract)

| What | System | Notes |
|---|---|---|
| Next-Day Ratings register | Airtable base "Northfell Control Room", table "Next-Day Ratings" | one row per circuit; the desk writes the rating fields |
| Protection settings | same base, table "Protection Settings" | Protection Engineering only (P-11) |
| Rating issue log | same base, table "Rating Issue Log" | maintained by the shift manager |
| Rating standard and tables | Confluence space RAT | NGS-RT-04 Issue 3 |
| Station forecasts | MetDesk station forecast service | live; reissued by MetDesk |
| MetDesk amendments | rating desk mailbox (ratings-desk@) | AMD-<mmdd>-<nn> |
| Series elements | ServiceNow change requests | state 3 Closed = in service; -2 Scheduled; -1 Implement; 4 Canceled |
| Loads | Datadog event stream | latest day-ahead issue |
| SO on duty | PagerDuty "SO Desk" schedules | day 07:00-19:00, night 19:00-07:00 |
| Control room chat | Slack #grid-control | day-ahead notice is posted here |
| Public outage notices | Slack #customer-outage-notices, outage-notices@ | Customer Communications only |
| Handover notes | Notion "Shift handovers" | written by the outgoing desk |
| Working files | Box "Rating Desk" | drafts, certificates |
