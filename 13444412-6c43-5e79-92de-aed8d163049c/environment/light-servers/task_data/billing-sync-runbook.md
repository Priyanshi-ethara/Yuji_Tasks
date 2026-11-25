# Nightly billing sync - runbook (Platform team)

At 18:00 Europe/London the sync reads every Change orders row whose Disposition is "Change scheduled" and whose
Effective date is today or later, and queues the change in Stripe for that date: price from New plan, quantity from
Seats. Unit price (GBP) is checked against the price book price for the period the change starts in; a mismatch
raises a sync exception that Finance has to clear by hand. Rows with any other disposition are ignored. Cancellation
rows are informational; Stripe's own cancel_at_period_end flag ends the subscription.

Validation: New plan must be one of Line/Grid/Mosaic Monthly/Annual; Seats a whole number >= 1; Effective date
YYYY-MM-DD; Unit price a number with two decimals at most.
