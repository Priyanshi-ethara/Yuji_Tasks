# Reading Stripe for the desk

- customers: name, email (the address invoices go to), description (workspace id and billing contact).
- subscriptions: customer, price (a price id; list prices to see the nickname), quantity = seats,
  current_period_start / current_period_end (Unix seconds, UTC; the end is the billing anchor),
  cancel_at_period_end (true = ends at the anchor).
- prices: nickname such as "Grid Annual", unit_amount in pence per seat per interval, recurring interval.
- invoices and charges: what was billed and paid; amounts in pence.
The desk writes one thing in Stripe: cancel_at_period_end = true on a subscription whose cancellation is scheduled.
Converting a timestamp: 1793491200 is 2026-11-01T00:00:00Z.
