# Categoriser FAQ (Desk Quality)

Q: The customer pressed 'voice fault' but asks how to set up a divert. Type?
A: question. The IVR option is not the type.

Q: Customer's broadband is down because of an exchange outage. Problem?
A: No - the NOC parent is the problem; the customer's ticket is an incident linked to it.

Q: The audit flag says 'priority to check'. Do I keep the priority if it looks fine?
A: Work it out from the matrix every time; flags are hints.

Q: Two products on the account, the bill is wrong. Product?
A: prod_account_general (guide 4.2).

Q: Do I add a note explaining my changes?
A: Not required. If you do, it must be internal.

Q: Can I use my colleague's draft?
A: As a starting point. The guide decides; the draft is not the record.

Q: A speed complaint where the line is fine?
A: Still an incident while open; the contact reason carries the cause (Annex B 'use when').

Q: A customer on Business Assure asks a billing question. Raise the priority?
A: No. Business Assure raises incidents only (guide 5.2); enquiries, billing questions and owed actions stay at the matrix.

Q: An engineer visit is booked but the customer still has no service?
A: incident while the service is down (guide 3.5). It becomes a task only once the service works and the ticket just
   tracks the visit.

Q: The ticket still has a pre-June product tag.
A: Replace it with the catalogue tag (guide 4.1 and the migration note). Never keep both.

Q: One fault takes broadband, phone and TV down together?
A: Tag the access product - the line the others run over (guide 4.3).

Q: The customer asks for paper bills.
A: A preference change: question, low, product prod_account_general, the paper-bills reason from Annex B.

Q: The ticket is in Welsh.
A: Keep lang_cy as found; categorise exactly as any other ticket. The Welsh rota is notified by Lumen Desk on its own.

Q: What goes in the Recategorisation log?
A: One row per ticket with what you filed: the type, product, priority and contact reason the ticket carries after your
   update, the batch date, and your Logged by name.
