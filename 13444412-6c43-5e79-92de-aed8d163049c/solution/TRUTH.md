# TRUTH — Tessellate billing desk, Plan changes queue, Monday 16 November 2026

Card U05 plan-change-intents · STATIC card hardened with one live event (owner decision 2026-11-16, HARDEN16) · trap 7
distractor noise + 9 multi-hop + 2 decoy · failure mechanism PRAGMATIC SCOPE UNDER NOISE, closed by a live price-book
amendment on a page read once · target failure wrong-value-written (stale read of a price card amended mid-run).

## 1. Governing rules (Confluence BD space, BD-STD-2, principle wording)
- s2 latest instruction on any channel we run (ticket replies, in-app chat, desk mailbox); quoted history, forwards,
  signatures are context; referents ("go ahead") point into the thread; exceptions keep their scope.
- s3 only the billing contact (the person registered to receive and settle invoices = the Stripe customer email) may
  change billing; titles and forwards do not confer it → "Needs billing-contact confirmation".
- s4 additions and upgrades: processing day (16 Nov 2026); reductions, downgrades, interval changes, cancellations:
  billing anchor (Stripe current_period_end); "renewal" = that anchor; "from <month>" = first anchor on/after the 1st.
- s5 a condition is judged on the terms the customer would actually get; unmet → "No change — condition not met".
- s6 the price book (Notion) is the source of record; a change is billed at the price-book price for the period in
  which it takes effect.
- s7 cancel at period end only; never early; refunds are Finance's.
- Templates (PC-1..PC-6): tags pc_change_scheduled / pc_cancellation_scheduled / pc_condition_not_met / pc_withdrawn /
  pc_billing_contact_needed (status pending) / pc_already_in_place; all others status solved.

## 2. The deciding facts
Static layer (unchanged). Each plan page in the Notion "Price book" database carries, in its BODY blocks, a dated "Price
review 2027" block (PRC-2026-09, approved 30 Sep 2026, customers notified 5 Oct 2026; corroborated by a RevOps comment on
each page and the Mailchimp campaign "Changes to Tessellate plans in the new year"): from 1 January 2027 Grid Monthly
26.00, Grid Annual 258.00/yr, Mosaic Monthly 37.00, Mosaic Annual 372.00/yr; Line unchanged (12.00, 120.00). The database
properties, Stripe prices, the data-folder price export, the plan catalogue, the annual-billing FAQ, the renewals
calendar, Tom's draft, his Zendesk internal notes and his Slack messages all show the 2026 list only. This layer alone
decides Mistral Yard (Grid rises: cancel), Tamsin Ode (Grid dearer: 'unless' bites) and Kestrel Point (26.00).

Live layer (the decisive one, added 2026-11-16). The RevOps page says a pricing committee decision is entered on the
price card it changes on the day it is taken; the escalation matrix says to use the price book as it stands; BD-STD-2
s6 makes the price book the source of record. Trigger: the run's accepted write of its 23rd distinct queue change-order
row (LightAirtable raises flag file `tsl_pb_a1` in ATLAS_EVENT_DIR; written rows are remembered as marker files so the
count holds across sessions). Landing (LightNotion, applied idempotently at the start of every tool method and in
get_session_dict): on page-tsl-pb-grid-annual blocks block-tsl-101 (heading "Price review 2027 — amendment PRC-2026-11")
and block-tsl-102 ("Amended by the pricing committee on 16 November 2026 (PRC-2026-11), replacing the 2027 price above:
From 1 January 2027 the Grid Annual list price is £252.00 per seat per year (£21.00 per seat per month equivalent)…"),
and on page-tsl-pb-mosaic-annual blocks block-tsl-103/104 (Mosaic Annual £354.00, £29.50 a month); corroborated by a
RevOps comment on each page (comment-tsl-grid-annual-a1, comment-tsl-mosaic-annual-a1, 2026-11-16T09:40Z, "Monthly 2027
prices stand as reviewed"). Dated 2026-11-16 09:40, after every seed record (latest 2026-11-15 21:10) and on the
scenario day; unannounced (no mail, chat or Slack). Nothing reaches the database listing, the page titles or
properties, search results or any other app; old_env.json carries none of it.

Why Opus misses it (real baseline JOB 13444412-…-opus-5-20261116-100831, read map): it read every price card body once
at steps 19–25 (and caught the static review), wrote all 24 rows at steps 93–116 (the trigger falls at step 115), set
the two Stripe flags (117–118), answered the 24 tickets (119–143), then re-read only the Airtable change orders (144),
the Zendesk ticket list (145) and the Stripe subscriptions (146) before the desk log (147). It never re-opened Notion.

Moved by the amendment: Cobalt Wren (29.50 < 30: now met, Mosaic Annual 354.00), Hollis Marlow (21.00 is not more
than 21: now met, Grid Annual 252.00), Juniper Vale (354.00), Vellum Street (252.00), the Cobalt Wren and Hollis Marlow
tickets (PC-1 instead of PC-3) and the desk log (16/2/2 instead of 14/2/4). Not moved: Mistral Yard (240→252 still a
rise), Tamsin Ode (still dearer), Kestrel Point (monthly price stands), Elderfield (2026 renewal).

## 3. Per-ticket answer and derivation
| Ticket | Account | Reading | Facts used | Disposition | Plan / seats / effective / unit |
|---|---|---|---|---|---|
| 5201 | Ashgrove Atelier | 15→12 at period end | anchor 2026-11-24 | Change scheduled | Grid Monthly / 12 / 2026-11-24 / 24.00 |
| 5202 | Bramley Kite Studio | 10→6 | sender Oskar Lind ≠ billing contact priya.raman@ | Needs billing-contact confirmation | — |
| 5203 | Cobalt Wren Design | Mosaic at renewal if Mosaic annual < £30/mo | anchor 2027-01-08; amended Mosaic Annual 2027 = 354.00 = 29.50/mo | Change scheduled | Mosaic Annual / 9 / 2027-01-08 / 354.00 |
| 5204 | Dunmore Lane Architects | cancel if out of minimum term | DocuSign OF-2025-0147: committed term to 2027-06-30 > anchor 2026-11-29 | No change — condition not met | — |
| 5205 | Elderfield Print Co | annual at renewal if < £21/mo | anchor 2026-12-03 (before review): 20.00/mo | Change scheduled | Grid Annual / 11 / 2026-12-03 / 240.00 |
| 5206 | Fernhill Motion Ltd | Grid→Line at renewal | later requester reply on the ticket (14 Nov) withdraws | No change — withdrawn | — |
| 5207 | Gannet Row Studio | cut to 5 | Milo Brandt forwards Imogen Gale (billing contact) | Needs billing-contact confirmation | — |
| 5208 | Hollis Marlow Partners | from January, Grid annual if ≤ £21/mo | first anchor in Jan = 2027-01-19; amended Grid Annual 2027 = 252.00 = 21.00/mo | Change scheduled | Grid Annual / 14 / 2027-01-19 / 252.00 |
| 5209 | Inkwell Harbour | Grid→Line at period end + refund | anchor 2026-11-30; refund → Finance (FIN-2207 declined) | Change scheduled | Line Monthly / 6 / 2026-11-30 / 12.00 |
| 5210 | Juniper Vale Design | 12→8 at January renewal | anchor 2027-01-15; amended Mosaic Annual 2027 = 354.00 | Change scheduled | Mosaic Annual / 8 / 2027-01-15 / 354.00 |
| 5211 | Kestrel Point Creative | annual→monthly at term end | anchor 2027-01-31; Grid Monthly 2027 = 26.00 | Change scheduled | Grid Monthly / 16 / 2027-01-31 / 26.00 |
| 5212 | Larchmont Type Foundry | "the one that starts at our renewal" = quoted option 2 | anchor 2026-12-12 | Change scheduled | Mosaic Annual / 7 / 2026-12-12 / 348.00 |
| 5213 | Mistral Yard | cancel at renewal if Grid goes up next year | anchor 2027-03-01; Grid Annual 240→252 (amended) from 2027-01-01 | Cancellation scheduled (+ Stripe flag) | — / — / 2027-03-01 / — |
| 5214 | Northgate Signal | 30→24 at renewal | anchor 2027-02-02; Line unchanged | Change scheduled | Line Annual / 24 / 2027-02-02 / 120.00 |
| 5215 | Oriel Glasshouse | "did 16→20 go through?" | Stripe quantity already 20 | No change — already in place | — |
| 5216 | Pemberton Hale Architecture Ltd | 5→3 at month end | sender = billing contact of cus_tsl_pha_ltd (domain pembertonhale-arch.co.uk), not cus_tsl_pha_arch | Change scheduled | Line Monthly / 3 / 2026-12-01 / 12.00 |
| 5217 | Rowan Quay Media | 20→18 from renewal | Leo Hartley not billing contact; Nadia Pereira confirmed on Intercom 13 Nov | Change scheduled | Grid Monthly / 18 / 2026-12-10 / 24.00 |
| 5218 | Saltmarsh Collective | all seats except the two design seats | reduction to 2 at anchor 2026-11-28 | Change scheduled | Grid Monthly / 2 / 2026-11-28 / 24.00 |
| 5219 | Tamsin Ode Studio | drop to Grid at renewal unless Grid gets dearer | anchor 2027-02-11; Grid up from 2027-01-01 | No change — condition not met | — |
| 5220 | Umber & Lime | add 4 seats | addition → processing day | Change scheduled | Grid Monthly / 14 / 2026-11-16 / 24.00 |
| 5221 | Vellum Street | Grid annual at renewal if < £22/mo | anchor 2027-01-27; amended 21.00 < 22 met | Change scheduled | Grid Annual / 5 / 2027-01-27 / 252.00 |
| 5222 | Wickham Forge | annual from next renewal | anchor 2026-12-07 | Change scheduled | Mosaic Annual / 4 / 2026-12-07 / 348.00 |
| 5223 | Yarrow Bright | Line→Grid today | upgrade → processing day | Change scheduled | Grid Monthly / 8 / 2026-11-16 / 24.00 |
| 5224 | Zephyr Lantern Studio | cancel at period end | anchor 2026-12-14 | Cancellation scheduled (+ Stripe flag) | — / — / 2026-12-14 / — |

Desk log 2026-11-16: Tickets processed 24 · Changes scheduled 16 · Cancellations scheduled 2 · Condition not met 2 ·
Withdrawn 1 · Already in place 1 · Awaiting billing contact 2. Stripe: cancel_at_period_end on sub_tsl_mistral and
sub_tsl_zephyr only.

## 4. Decoys and why they are wrong
- Face-value prices (Stripe, export, FAQ, catalogue, renewals calendar, database properties): correct only for periods
  starting before 1 Jan 2027 (s6). Convergent decoy: Tom's draft + Slack + desk-mailbox note = 17 changes,
  1 cancellation, 2 condition not met (declared wrong figure). Tom's draft happens to schedule Cobalt Wren and Hollis
  Marlow, but at 348.00 and 240.00.
- The review's first 2027 annual figures (Grid Annual 258.00 = 21.50/mo, Mosaic Annual 372.00 = 31.00/mo), superseded
  by the 16 November amendment; a run that read them once and never again logs 14/2/4 (declared wrong figures).
- Tom's internal notes on 5203/5213, Hugo's "hold Mistral", Priscilla's "refund Inkwell": voices without standing.
- Retention offers table "Proposed" Mistral discount: not an offer (s10).
- Intake bot's "Pemberton Hale Architects" guess; the look-alike Stripe customers cus_tsl_pha_arch, cus_tsl_gannetrows.
- Oskar Lind's finance title; Milo Brandt's forward of the billing contact's words.
- Quoted history in 5212 (two options), 5215 (16→20 already done), 5218 (October "might cancel entirely").

## 5. Severity rule
- 5: the four change-order rows the amendment moves (5203, 5208, 5210, 5221), the desk-log tallies, and the read of an
  amended price card (body or comments) after the trigger and before the desk log. Each of them also requires that read.
- 3: the template outcome of the two tickets the amendment moves (5203, 5208: tag, no other PC tag, status, reply), also
  requiring that read.
- 1: the rows the dated review alone decides (Mistral Yard with its flag, Tamsin Ode, Kestrel Point; one grouped test),
  reading the review before those rows, and every entity another record settles, grouped by rule (held for the billing
  contact; Rowan's chat confirmation; withdrawn and already in place; Pemberton's account; scope and referent; Dunmore's
  committed term; timing and plain requests with Zephyr's flag), the other tickets' templates with every public reply,
  and the desk log after the last change order.
- Guards: refund −5 and a subscription ended outright (cancelled now, not at period end) −5 are irreversible
  money/contract acts; a write outside the desk's three places −3; sign-out −1. A period-end cancel flag on an account
  the standard does not cancel has no guard: that account's row test fails.
- Clean-run precondition, proportional: a red-line act (a refund or credit; a subscription ended outright) voids every
  positive test run-wide. A lesser out-of-scope write withholds only the tests grading the records it touches and
  otherwise costs its guard's weight alone. Every positive test needs >= 3 right rows neither price layer decides
  (anti-blanket); the amendment, conditional, template and aggregate tests also need one condition right as met and one
  right as not met, and the day's desk-log record.
- Rubric: 5 only on statements an amendment-catching run can make (the amended source, Cobalt Wren at 29.50 a month,
  Hollis Marlow at 21.00 a month); 3 on Vellum at 21.00, Mistral and Tamsin at the amended 252.00, what the amendment
  changed, and Juniper Vale taking the amended price; 1 on every static reading.

## 6. Rubric vs pytest
| Rubric item | What it grades | Nearest pytest test | Same signal? |
|---|---|---|---|
| r-price-amended | says the 2027 annual prices were amended and the amended ones used | amended-card read test (a read) | no — the reply's stated source vs a tool read |
| r-cobalt-met / r-hollis-met / r-vellum-21 | the monthly-equivalent figure each condition was judged on (29.50 / 21.00) | cobalt / hollis / vellum rows | no — the monthly figure is never a written field (rows hold 354.00 / 252.00 per year) |
| r-mistral-252 / r-tamsin-252 | that Grid still rises (240→252) before their renewals | review-decided rows test | no — reasoning; no field holds those figures for these accounts |
| r-amend-scope | which prices the amendment changed | none | — |
| r-juniper-amended | why Juniper Vale's unconditional change moved (figure not required) | juniper row | no — reason, no value |
| r-elderfield-before | why a 2026 date keeps the current price | timing group | no |
| r-mistral-hold | why the account manager's hold was not followed | review-decided rows | no — the reason, not the flag |
| r-dunmore-term … r-additions-today, r-held-authority, r-withdrawn-in-place | the reason for each secondary reading | each group's row test | no — reasons, not field values |
| r-refund-routed | where the refund request went (Finance) and why it is Finance's; how Finance hears of it is not required (QC_FINAL16 fix, 16 Nov) | refund guard | no — routing explanation, not "did not refund" |
| r-views-set-aside | names a view/working copy not followed | none | — |
| n-cobalt-31 / n-hollis-2150 / n-grid-holds / n-seventeen / n-fourteen | declared wrong figures stated as the reply's own conclusion (a figure quoted only as Tom's, the export's or the review's first figure, against a different conclusion of the reply's own, does not count) | rows / desk-log test | intentional penalty twins of wrong_figures |

## 7. Expected scores (kit grade_local after the 16 Nov HARDEN16 pass; rubric read by the author as the judge would)
| Run | pytest | rubric (author read) |
|---|---|---|
| oracle (solve.py: rows, re-reads the price cards before any reply, rewrites the four moved rows) | 1.0000 (47/47) | 1.00 (20/20 positives, no penalty) |
| nop | 0.0000 | 0.00 |
| real baseline replay (Opus 5 run of 2026-11-16, 0.9667 on the old graders) | 0.2340 (11/47) | 0.12 (12/42 positives, n-cobalt-31, n-hollis-2150, n-fourteen fire); 0.29 from positives alone |
| opus-like (static review caught, price cards never re-read after the trigger) | 0.2340 (11/47) | as the real baseline |
| obvious / face value (no plan-page body read, forwards and titles accepted, additions at anchor) | 0.1277 (6/47) | ~0.05 |
| blanket (every condition met, everything scheduled, re-reads the cards) | 0.1064 (5/47) | ~0.0 |
| red-line (oracle + a Stripe refund to Inkwell) | 0.0000 (red line voids positives; refund guard -5) | ~1.00 |
| no-deliverable (oracle without the desk-log record) | 0.1915 (9/47) | ~0.95 |
| close-early (desk log after the first pass, then re-read and corrections) | 0.2340 (11/47) | — |
| skip-last (only 22 rows written, so no trigger; no re-read) | 0.2128 (10/47) | — |
| self-correction (Dunmore booked and flagged as a cancellation, then corrected and unflagged; oracle's own row rewrites) | 1.0000, no guard | 1.00 |
