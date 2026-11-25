All three deliverables are done and verified. Here's my hand-back.

Morning Marisol — batch 2026-11-18 is filed, logged and the note is published.

One note on delivery: you asked for a short reply but also said no mail, so I've written it here rather than emailing you. Say the word if you'd rather have it in your inbox.

**What's where**
- Lumen Desk: all 28 tickets (48201–48228) recategorised. Status, assignee and requester untouched, every `channel_`/`lang_`/`sla_`/`noc_` tag sent back as found, exactly one `prod_` and one `cr_` each. No comments added to any ticket — the job didn't need one.
- Recategorisation log: 28 rows, Batch `2026-11-18`, Logged by `Desk Quality Analyst`. Earlier batches untouched.
- Wiki: *Queue health - 2026-11-18*, child of Queue health notes in DESK.

**The mix (as the tickets are held after the batch)**
```
Type mix: question 10 · incident 14 · problem 0 · task 4
Priority mix: urgent 1 · high 7 · normal 18 · low 2
```

**Where I differ from Tobias's draft**

Substantive, seven tickets:

| Ticket | Draft | Filed | Why |
|---|---|---|---|
| 48214 | high | **urgent** | Business Assure incident, whole-site loss: 5.1 high + 5.2 one step. Calder Freight is the BA account on WK-04 |
| 48215 | normal | **high** | Total loss ("router lights red, nothing connects") — 5.1, not degraded |
| 48215 | prod_fibre_home_150 | **prod_fibre_home_500** | See the account-mapping note below |
| 48216 | prod_fibre_home_150 | **prod_fibre_home_500** | Same |
| 48217 | prod_mobile_sim | **prod_mobile_handset** | Flickering/black screen with calls and data fine — the handset, not the network (4.4; the migration note warns these two were IVR-swapped) |
| 48219 | normal | **low** | Marketing opt-out is a preference change (5.1) |
| 48221 | normal | **high** | Business Assure incident, degraded: normal + one step |
| 48224 | normal | **high** | No picture on any channel is total loss (5.1), box itself working |

Same code, different form — four reasons filed as Annex B short forms because the platform silently truncates tags at 24 characters: **48207** `cr_b03`, **48209** `cr_m02`, **48211** `cr_f04`, **48213** `cr_p02`. The full tags are 33/32/29/30 characters and would have been cut mid-word with no warning. 6.2 allows either form and reporting maps both to the same code.

Tobias also missed the Priority Assistance flag on **48206** (Mabry, registered 12 Nov) and **48225** (Holt, registered 16 Nov). I filed both at high per 5.3 — but see below, they aren't held there.

**Two things I'd like you to look at**

1. **The PA floor is not surviving the save.** Eight tickets are from PA customers. Five are residential enquiries — 48201, 48202, 48204, 48206, 48225 — and I filed all five as question/high per 5.3. Trigger T-11 reset every one to normal on save, silently. They are *held* at normal, so that's what the log and the note show, per 2.1. The practical effect: the SLA clock runs 24 hours on them instead of the four hours PA is promised. The only two PA enquiries holding at high are the two on business organisations (48203, 48205), which T-11 isn't in scope for. This is the guide against the configuration, not a filing choice — 5.4 says a ticket is never held below its matrix priority and T-11 holds it below. I've changed nothing in the set-up (2.2) and raised nothing with Desk Tooling; it's yours and Femi's to settle.

2. **Account mapping moved under me.** TOOL-503 went live today: a ticket is re-filed under its *requester's* organisation on every save. Five tickets changed account when I saved them — 48203, 48215, 48216, 48221, 48222 — so I read Business Assure and segment from the account each ticket landed on, which is what the SLA policy, the views and reporting read. That's why **48221 takes the BA uplift and 48222 does not**, which is the opposite of what those two tickets' `sla_` tags say. Those tags are now stale on both; they're set by the account sync so I left them exactly as found (tag rule 2) — worth a word to Desk Tooling. The same re-filing is why 48215 and 48216 take the Fibre Home 500 plan rather than the 150 on the near-duplicate household accounts.

**For Carys, before she staffs Thursday**

- **Seven enquiries reach the residential worklist, not ten**: 48201, 48202, 48204, 48206, 48219, 48220, 48225. The other three are business and go to the business desk (48203, 48205, 48226). Her two people are still about right on her one-per-five rule, but she's planning against the wrong figure — she emailed yesterday assuming Tobias's ten.
- **Five of those seven are Priority Assistance customers** (48201, 48202, 48204, 48206, 48225) and every one of them is held at normal because of T-11. The priority field will not flag them, so the worklist gives her no visible signal. They're still owed a four-hour callback.
- **48204 is Welsh** (`lang_cy` kept as found) and the customer asked for large print or phone — Eleri covers Thursday.
- 48225 is an upgrade enquiry from a customer whose contract has ended, tagged to what he holds now (`prod_copper_bb`) per 4.3.

Everything else stayed read-only: no Slack, no mail, no Salesforce/Jira/Notion/Stripe edits, no changes to existing wiki pages or log rows, nothing touched outside the 28. All five apps are still logged in for the desk to collect.