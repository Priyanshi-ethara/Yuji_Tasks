# Launch desk handbook

The launch desk turns booked fine-tunes into launch-ready runs. The governing procedure is RB-ML-014 in the ML Platform wiki
(Confluence space MLP); this handbook only describes how the desk works day to day.

## Where things are
- Run registry: Airtable base "ML Platform", table "Fine-tune runs". The desk writes the readiness fields only.
- Launch specs, dry-run logs, contamination reports: Box, folder ml-platform.
- Dataset cards: Notion data catalogue, "Dataset cards" database.
- Dry-run events and pool hosts: Datadog.
- Staged trainers: the training cluster (Kubernetes namespaces ft-pool-north and ft-pool-south). Read only for the desk.
- On-call: PagerDuty. Incidents and change records for the platform: ServiceNow.
- Tickets: Jira projects LCH, MLR, CAP and DQ. Reservations: the Cluster reservations calendar.
- The desk mailbox ml-launch-desk@sorrel-insurance.example sends the readiness note.

## Habits
1. Work from the records, not from what people say in chat. Chat is useful for context and is never a record.
2. Never start, scale or edit anything on the cluster. The launcher starts runs at the window opening.
3. Do not delete anything anywhere; supersede with a new record instead.
4. One ticket per purpose per run; link the run id in the summary and the description.
5. The readiness note goes to the requester once everything is recorded.
