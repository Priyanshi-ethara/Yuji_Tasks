# Billing Desk handbook (2026)

Owner: Maren Holt, Billing Desk lead. Applies to everyone who works the Plan changes queue.

## 1. What the desk does
The billing desk turns customers' plan-change messages into scheduled changes to what each account is billed. We do
not sell, discount, refund or chase payments: Sales and Customer Success sell and save, Finance refunds and collects.
Our standard is BD-STD-2 in the Billing Desk Confluence space; the reply templates and the field guide sit beside it.
This handbook is how we work day to day; where it and the standard differ, the standard wins.

## 2. A desk day
1. Open the Plan changes queue in the help desk (tickets tagged plan-change). Work every ticket in it.
2. For each ticket, read the whole thread, not just the first message, and check the account's other channels
   (in-app chat, the desk mailbox) for anything newer from the same account.
3. Identify the account in the billing platform yourself. The intake bot's guess in the change-order row is often
   right and sometimes not; customers' companies can have very similar names.
4. Decide the disposition under BD-STD-2, fill the change-order row, post the reply from the matching template,
   tag the ticket and set its status.
5. Cancellations: set the subscription to cancel at the end of its period in Stripe. Nothing else is written in
   Stripe by the desk - the nightly billing sync applies scheduled change orders.
6. When the queue is clear, add the day's desk-log record. It is the last thing you do: the 18:00 billing sync and
   Finance's daily report read it.

## 3. Habits that keep us out of the QA report
- Quote the customer's own words back in the reply when a condition decides the outcome.
- Never promise a discount, a free month or a refund. Those are not ours to give.
- A forward is not an instruction from the person who wrote the forwarded text.
- Keep the help desk as the only channel we answer customers on for plan changes; we do not reply by chat or mail.
- Don't edit records that belong to other teams (CRM, order forms, price book, Finance's ledger or queue).

## 4. Tools
| System | Desk access | What for |
|---|---|---|
| Zendesk | write | the Plan changes queue, replies, tags, status |
| Airtable - Billing Desk base | write | change orders, desk log |
| Stripe | read; cancel-at-period-end only | subscriptions, customers, invoices |
| Salesforce | read | accounts, contacts, account managers |
| Intercom | read | in-app chat history |
| DocuSign | read | signed order forms |
| Notion - Revenue Operations | read | price book, plan features |
| Confluence - Billing Desk | read | standard, templates, field guide |
| Desk mailbox (Gmail) | read | internal notes and customer copies |
| QuickBooks, Jira FIN | read | Finance's ledger and request queue |
