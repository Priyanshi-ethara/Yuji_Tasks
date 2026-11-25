# Billing desk glossary

- **Seat** - an editor seat; one named person who edits boards. Viewers are free.
- **Billing anchor** - the point at which a subscription's paid period ends and the next begins. Stripe shows it as the
  subscription's current_period_end (a UTC timestamp). Monthly subscriptions keep the same day of the month.
- **Renewal** - the next billing anchor. For an annual plan that is the end of the annual term; for a monthly plan,
  the end of the current month's period.
- **Pro-rating** - charging part of a period when seats or plan go up mid-period.
- **Committed term** - a minimum period an account agreed to in a signed order form. It is a contract term, not a
  billing interval: a monthly-billed account can have a 24-month committed term.
- **Billing contact** - the person an account registered with us to receive and settle its invoices.
- **Change order** - the desk's row in the Billing Desk base that the nightly billing sync applies.
- **Unit price** - the per-seat price for a plan's billing interval: per month on monthly plans, per year on annual.
- **Monthly equivalent** - an annual per-seat price divided by twelve; customers often compare plans this way.
- **Price book** - Revenue Operations' price cards in Notion, one per plan and interval.
