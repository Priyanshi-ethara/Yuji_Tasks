# Copy of the week 45 routing summary (posted in #sre-triage on Mon 9 Nov by Tobin Marsh)

Routed 17 open fleetd groups. Per team: Sim Tools 5, Messaging 3, Dispatch Core 3, Platform Foundations 3,
Telematics Ingest 1, Maps & Routing 1, Billing & Settlement 1.
Classes: send on closed channel 6, nil map write 4, slice bounds 4, unbounded goroutine growth 1,
typed nil returned as error 2.
Notes: simkit-topped groups to Sim Tools as before; vendored-library tops to Platform.
