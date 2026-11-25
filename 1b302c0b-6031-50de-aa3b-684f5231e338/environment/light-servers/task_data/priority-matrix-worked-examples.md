# Priority matrix - worked examples (Desk Quality, edition 4)

These examples come from past batches. Customer names removed.

1. Residential customer, broadband down completely since morning, not on Priority Assistance -> incident, high (5.1 total loss).
2. Same, but intermittent drops in the evening -> incident, normal (degraded).
3. Business customer without Business Assure, voice calls dropping a few times a day -> incident, normal.
4. Business customer with Business Assure, same symptoms -> incident, high (5.2 one step up).
5. Business Assure customer, whole site offline -> incident, urgent (5.1 high, 5.2 one step up).
6. Residential customer on Priority Assistance, home phone dead -> incident, high (5.1 already high; 5.3 is a floor, not a step).
7. Customer asks how to set up voicemail, not on Priority Assistance -> question, normal.
8. Customer says thank you to an engineer -> question, low.
9. Customer asks to stop marketing calls -> question, low (preference change).
10. Duplicate monthly payment, refund already made -> incident, normal (charge taken in error; billing errors are normal).
11. Engineer visit booked to replace a damaged socket, service still working -> task, normal (3.5).
12. Port-in late because the losing network has not released the number, the old number still works -> task, normal.
13. TV box powers on, every channel 'no signal' -> incident, high (no picture on any channel).
14. Handset screen cracked, calls fine -> incident, normal (faulty device, service works).
15. SIM swap left the customer with no network at all -> incident, high.

Common slips seen in audits
- Taking the IVR option the customer pressed as the type ('voice fault' pressed by someone asking a how-to question).
- Raising every business ticket to high; only Business Assure incidents step up.
- Forgetting that a NOC parent is the only kind of problem ticket.
