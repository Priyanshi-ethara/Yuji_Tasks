Crash routing for 2026-11-16 is done: all 22 open fleetd groups on the register carry an owner team and a root cause, every owning team has one routing ticket in its own Linear team, and the summary is posted in #sre-triage. Nothing was resolved, ignored or deleted in Sentry and nothing was written to the repository, its mirror or the retired Jira queue.

Groups per team:
- Billing & Settlement: 3 (FLEETD-4J1, FLEETD-4W6, FLEETD-4X2)
- Driver Comms: 3 (FLEETD-3S6, FLEETD-4H6, FLEETD-5M2)
- Fleet Reliability: 3 (FLEETD-4P2, FLEETD-4T7, FLEETD-5KQ)
- Maps & Routing: 3 (FLEETD-3R1, FLEETD-4M5, FLEETD-5T9)
- Platform Foundations: 3 (FLEETD-4K8, FLEETD-4S3, FLEETD-5P7)
- Dispatch Core: 2 (FLEETD-3N4, FLEETD-4V1)
- Messaging: 2 (FLEETD-4Q9, FLEETD-5R3)
- Telematics Ingest: 2 (FLEETD-3P8, FLEETD-5V4)
- Sim Tools: 1 (FLEETD-4ZD)
- API Contracts: 0 (no ticket filed)

Why the simkit-topped groups did not go to Sim Tools:
Six groups (FLEETD-5KQ, FLEETD-5M2, FLEETD-5P7, FLEETD-5R3, FLEETD-5T9, FLEETD-5V4) have simkit frames on top, printed as git.pellam.io/fleetd/tools/simkit/... . Those frames are not inside our module even though their import path begins with the fleetd module path git.pellam.io/fleetd (and, trimmed, would map to the tools/simkit/ directory that the ownership file gives to Sim Tools): since PR #3318 tools/simkit has its own go.mod and is a separate module, and fleetd requires it and vendors it (git.pellam.io/fleetd/tools/simkit v0.4.2 in vendor/modules.txt), so release builds (-mod=vendor -trimpath) run the vendored copy, not tools/simkit on main. Under the handbook a dependency's frames are stepped over even though we wrote it, so each of these groups is decided by the first frame of ours below the simkit frames:
- FLEETD-5KQ: skipped simkit/ticker.go; deciding frame internal/dispatch/lease/renewer.go -> rule /internal/dispatch/lease/ -> @pellam/fleet-reliability -> Fleet Reliability.
- FLEETD-5M2: skipped simkit/wheel.go; deciding frame internal/notify/digest/scheduler.go -> rule /internal/notify/ -> @pellam/driver-comms -> Driver Comms.
- FLEETD-5P7: skipped simkit/ring.go; deciding frame internal/telemetry/exporter/batch.go -> rule /internal/telemetry/ -> @pellam/platform -> Platform Foundations.
- FLEETD-5R3: skipped simkit/scheduler.go; deciding frame internal/billing/queue/flush.go -> rule queue/ -> @pellam/messaging -> Messaging.
- FLEETD-5T9: skipped simkit/clock.go; deciding frame internal/geo/eta/estimator.go -> rule /internal/geo/ -> @pellam/geo -> Maps & Routing.
- FLEETD-5V4: skipped simkit/ticker.go; deciding frame internal/ingest/gateway/heartbeat.go -> rule /internal/ingest/ -> @pellam/ingest -> Telematics Ingest.
The simctl replay crash FLEETD-4ZD stays with Sim Tools: tools/simctl has no go.mod of its own, so it is part of our module and its frame decides under the /tools/simctl/ rule.

Other groups decided below their top frame:
- FLEETD-4H6: skipped github.com/segmentio/kafka-go/writer.go (a vendored third-party library is a dependency); deciding frame internal/notify/outbox/publisher.go -> /internal/notify/ -> Driver Comms.
- FLEETD-4J1: skipped github.com/jackc/pgx/v5/pgxpool/pool.go (a vendored third-party library is a dependency); deciding frame internal/billing/ledger/store.go -> /internal/billing/ -> Billing & Settlement.
- FLEETD-4K8: skipped github.com/pellam-oss/queue/ring.go (a vendored third-party library is a dependency); deciding frame internal/platform/logging/sink.go -> /internal/platform/ -> Platform Foundations — the same team the vendored top frame would have pointed to, Platform Foundations.
- FLEETD-4M5: skipped git.pellam.io/fleetd/internal/gen/fleetpb/route.pb.validate.go (generated code under /internal/gen/ is produced by the API toolchain, not an owner); deciding frame internal/geo/planner/handler.go -> /internal/geo/ -> Maps & Routing; so it does not go to API Contracts.

Precedence rulings in the ownership file (last matching rule decides; no leading slash = any depth):
- internal/dispatch/lease/ files go to Fleet Reliability: the later /internal/dispatch/lease/ rule overrides the earlier /internal/dispatch/ rule (FLEETD-4P2 and FLEETD-5KQ).
- internal/billing/queue/ files go to Messaging: the later queue/ rule has no leading slash, matches at any depth and overrides /internal/billing/ (FLEETD-4Q9 and FLEETD-5R3), whatever Billing asked in chat.
- internal/telemetry/exporter/ files go to Platform Foundations, not Telematics Ingest: the later, broader /internal/telemetry/ rule overrides the earlier /internal/telemetry/exporter/ line (FLEETD-4S3 and FLEETD-5P7).
- internal/notify/retry/ goes to Fleet Reliability: the later retry/ rule (any depth) overrides /internal/notify/ (FLEETD-4T7).
- The /internal/notify/ line was changed in place on main this morning (see below), so it still sits above queue/ and retry/: the change did not move internal/notify/retry, because retry/ still comes later than the changed notifications line (FLEETD-4T7 stays with Fleet Reliability), and it did not touch the settlement queue, because queue/ is a separate, later rule the change left alone (Messaging keeps FLEETD-4Q9 and FLEETD-5R3).
- The @pellam/geo handle belongs to Maps & Routing in the people directory (Geo Services is retired), so geo groups were written as Maps & Routing.

Ownership change merged during the morning:
The ownership file in the desk folder is the 06:00 export, but the file that decides is .github/CODEOWNERS on main. Pull request #3490 was merged at 08:40 UTC on 2026-11-16, after the export, and changed /internal/notify/ from @pellam/messaging to @pellam/driver-comms (Petra's merge note in #fleetd-dev says the same). So FLEETD-3S6, FLEETD-4H6, FLEETD-5M2 are decided by the changed /internal/notify/ line, i.e. Driver Comms' handle @pellam/driver-comms, rather than by the export's Messaging line. FLEETD-5M2: the vendored simkit wheel frames are stepped over and the digest scheduler (internal/notify/digest) falls under the changed line. FLEETD-4H6: the kafka-go frames are stepped over and the outbox publisher (internal/notify/outbox) falls under the changed line. FLEETD-3S6: past the runtime frames, the fanout hub (internal/notify/fanout) falls under the changed line. I had written these rows from the export first and rewrote them after reading the merge, before filing any ticket. The pull request changes only the /internal/notify/ line; no other rule of the file changed, so only groups decided by that line moved.

Root-cause classes: typed nil returned as error 2, send on closed channel 5, nil map write 3, unbounded goroutine growth 3, slice bounds 6, nil pointer dereference 3.
FLEETD-4V1 and FLEETD-4W6 are typed nil returned as error: Validate and rate return a nil *ValidationError / *RateError through the error interface, so err != nil and Error() runs on a nil receiver. FLEETD-4X2 looks the same (a nil-receiver Error() call) but is a plain nil pointer dereference: explain() calls Error() on the concrete *DeclineError field s.last directly, with no error interface involved. FLEETD-4J1 and FLEETD-5T9 are plain nil pointer dereferences too: a nil *pgxpool.Pool and a nil *simkit.Clock are used directly, with no error interface involved.

Not followed: Tobin's culprit-based draft, because the handbook decides by the first frame inside our module and the draft routes by the top frame (it sent every simkit-topped group to Sim Tools and parked the vendored and generated tops with Platform Foundations and API Contracts); last week's routing habit, for the same reason; Billing's request in chat and mail to route internal/billing/queue crashes to Billing & Settlement, because the ownership file's later queue/ rule decides those files and a request in chat does not change it; and Tobin's cheat-sheet rule that a nil-receiver Error() call is always a typed nil, because the code of FLEETD-4X2 says otherwise. The retired Jira CRASH queue and the GitLab mirror were not used as sources. I also did not follow the morning export's /internal/notify/ line (Messaging's handle) for the notifications groups, because the ownership file on main changed after the export was taken.