Done — register, tickets and the one Slack post are complete. Still logged in to every app.

## What I did

**1. Register** (Airtable → SRE Triage → Open crash groups): filled `Owner team` and `Root cause` on all 22 rows, nothing else. Verified by re-reading the table: titles, counts, releases and `Synced` are untouched, no rows added or removed, Routing history left alone.

**2. Tickets**: 8 routing tickets, one per owning team, each in that team's own Linear team — DSP, REL, MSG, BIL, PLT, MAP, ING, SIM (MER-213 … MER-220). No ticket in SRE Desk or the retired Geo Services. Nothing pre-existing in Linear was edited, commented on or closed.

**3. Summary**: one message in `#sre-triage`.

## Groups per team

| Team | Groups |
|---|---|
| Messaging | 5 — 3S6, 4H6, 4Q9, 5M2, 5R3 |
| Billing & Settlement | 3 — 4J1, 4W6, 4X2 |
| Fleet Reliability | 3 — 4P2, 4T7, 5KQ |
| Maps & Routing | 3 — 3R1, 4M5, 5T9 |
| Platform Foundations | 3 — 4K8, 4S3, 5P7 |
| Dispatch Core | 2 — 3N4, 4V1 |
| Telematics Ingest | 2 — 3P8, 5V4 |
| Sim Tools | 1 — 4ZD |
| **API Contracts** | **0** — no ticket |

API Contracts is named in the ownership file (`/api/`, `/internal/gen/`) but owns nothing: the one group whose top frame is in `internal/gen` (4M5) has that frame stepped over as generated code. Driver Comms exists in Okta and Linear but is *not* in the ownership file, so it could not receive anything either. Team names are the Okta group names — so "Maps & Routing" (not the `@pellam/geo` handle), "Telematics Ingest" (not `ingest`), "Platform Foundations", "Billing & Settlement".

## Groups that did not land with their top frame

**The simkit ruling (6 groups).** Tobin's draft treats a simkit top frame as Sim Tools' own. That was true before September. PR #3318 added `tools/simkit/go.mod` declaring `module git.pellam.io/fleetd/tools/simkit`, so simkit is no longer part of the fleetd module; `vendor/modules.txt` for 4.12.x pins `git.pellam.io/fleetd/tools/simkit v0.4.2`, and the PENG build page confirms release builds are `-mod=vendor`. So the running simkit code arrives as a vendored dependency. Handbook §1 steps over "code that reaches the fleetd binary as a dependency, even when we wrote it", and sends the crash to the team that called in:

| Group | Stepped-over top frame | Deciding frame | Team |
|---|---|---|---|
| 5KQ | `simkit.(*Ticker).Reset` | `internal/dispatch/lease/renewer.go:64` | Fleet Reliability |
| 5V4 | `simkit.(*Ticker).Reset` | `internal/ingest/gateway/heartbeat.go:36` | Telematics Ingest |
| 5M2 | `simkit.(*Wheel).Schedule` | `internal/notify/digest/scheduler.go:60` | Messaging |
| 5P7 | `simkit.(*Ring).Window` | `internal/telemetry/exporter/batch.go:68` | Platform Foundations |
| 5R3 | `simkit.(*Scheduler).After` + runtime frames | `internal/billing/queue/flush.go:99` | Messaging |
| 5T9 | `simkit.(*Clock).Now` | `internal/geo/eta/estimator.go:45` | Maps & Routing |

**Other stepped-over frames.** 4H6 — `segmentio/kafka-go` → `internal/notify/outbox/publisher.go:74` (Messaging). 4J1 — `jackc/pgx/v5/pgxpool` → `internal/billing/ledger/store.go:47` (Billing & Settlement). 4K8 — `pellam-oss/queue` → `internal/platform/logging/sink.go:47` (Platform Foundations); it's an external module despite being ours. 4M5 — generated `internal/gen/fleetpb` → `internal/geo/planner/handler.go:35` (Maps & Routing). 3S6, 4T7, 5R3 also step over Go runtime frames (`runtime.newproc` etc.).

**4ZD stayed put.** Its top frame is `tools/simctl/replay` — simctl was *not* split out, it's absent from the vendored module list and builds from the fleetd module, so that frame is ours: Sim Tools, the only group they own.

## Precedence rulings (last matching rule wins)

- `queue/` (no leading slash, any depth, added by #3415) sits after `/internal/billing/` → **4Q9 and 5R3 to Messaging**, not Billing.
- `retry/` (#3441) sits after `/internal/notify/` → **4T7 to Fleet Reliability**, not Messaging.
- `/internal/telemetry/` → platform sits after the narrow `/internal/telemetry/exporter/` → ingest (#3433 deliberately appended rather than deleting) → **4S3 and 5P7 to Platform Foundations**, not Telematics Ingest.
- `/internal/dispatch/lease/` (#3402) sits after `/internal/dispatch/` → **4P2 and 5KQ to Fleet Reliability**, not Dispatch Core.
- `/internal/manifest/` → dispatch-core put **4V1 with Dispatch Core** even though the crash surfaces through `internal/httpx` (Platform's) — the deciding frame is the first *our-module* frame, `manifest/errors.go:21`.

## Root-cause classes

slice bounds **6** (3P8, 4H6, 4M5, 4S3, 4ZD, 5P7 — index-out-of-range folded in per the classes page) · send on closed channel **5** (3R1, 4K8, 4Q9, 5KQ, 5V4) · nil map write **3** (3N4, 4P2, 5M2) · unbounded goroutine growth **3** (3S6, 4T7, 5R3) · nil pointer dereference **3** (4J1, 4X2, 5T9) · typed nil returned as error **2** (4V1, 4W6).

**The five nil-pointer panics** share one message but split three/two, because the class follows the code at the deciding frame:

- **4V1 → typed nil returned as error.** `manifest/validate.go` declares `var verr *ValidationError` and returns it for a *good* manifest; `httpx.writeProblem` receives a non-nil interface holding a nil pointer (visible in the frame args as `{0x2140f20, 0x0}`), passes `err == nil`, and calls `Error()`.
- **4W6 → typed nil returned as error.** Same shape: `invoice/builder.go` `rate()` returns a nil `*RateError` through `error`, and `Build` does `if err := b.rate(l); err != nil { … err.Error() }`.
- **4X2 → nil pointer dereference.** Looks identical from the title — an `Error()` method on top — but `quote/service.go` `explain()` calls `s.last.Error()` directly on a concrete `*DeclineError` field that stays nil until a carrier declines. No interface conversion, so it's the plain class. Tobin's cheat-sheet rule "top frame is an `Error()` method ⇒ typed nil" would have misfiled this one; reading the code is what separated it.
- **4J1 → nil pointer dereference.** `ledger.Store.Post` calls `s.pool.Acquire` with a nil `*pgxpool.Pool` (the settlement worker builds `Store{}` directly instead of `Open()`); the nil is used directly.
- **5T9 → nil pointer dereference.** `eta.Estimator.Arrival` calls `e.clock.Now()` on a nil `*simkit.Clock` (the planner builds `&Estimator{Model: m}`, skipping `New`). Direct nil pointer, no interface.

## Things I was handed or told and did not follow

- **Tobin's draft and cheat sheet** (`triage-draft-culprits.csv`, `root-cause-cheatsheet.md`) — the shortcuts "simkit on top = Sim Tools", "owner from the culprit column", and "vendored library ⇒ Platform, they own /vendor/" all conflict with handbook §1. Sim Tools gets 1, not 7; the vendored-library groups went to their callers, not Platform. His own note says the cheat sheet never opens the code.
- **His Slack message** in `#sre-triage` ("Sim Tools gets 7 again") and **Odil's reply** ("drop them in our queue like last week") — chat opinion is explicitly a non-source, and your own message in-channel says the same.
- **Kofi's request** (twice: `#sre-triage` and `#billing-eng`, with a threat to raise it at the review) that `internal/billing/queue` crashes come to Billing. The file's `queue/` rule is the later match, so 4Q9 and 5R3 went to Messaging. Ilse's reading in `#billing-eng` matches the file. The review agenda item 6 says the same: the file is the answer unless someone changes it by PR, which I can't and didn't do.
- **The simkit source excerpt in the data folder** — it's exported from `main`, which already has the Reset-after-Stop no-op and the `Window` clamp heading for 0.5.0 (#3460), while production runs the vendored 0.4.2 (bump PR targets 27 Nov). Its line numbers don't match the stacks, so I didn't use it to classify. It made no difference, since simkit frames are stepped over anyway.
- **Earlier weeks' routing** (`routing-history-2026-q4.csv`, the week-45 summary copy, the Routing history table) — non-sources per the handbook, read only to understand the ticket format.
- **Nils's "Platform has it"** for the exporter happens to be right, but I decided 4S3/5P7 on the ownership file, not on the channel.
- **Ticket priority.** The local convention file suggests priority 1 for any group over 1,000 events/7d. You asked for title and description only, and the same file says teams don't mind it unset, so I left priority unset rather than write a field you didn't ask for. Groups over 1,000 this week, for your agenda item 2: 3P8 (4,410), 5P7 (3,410), 5V4 (2,290), 5KQ (1,874), 3N4 (1,203).
- **No writes anywhere else**: no Sentry status changes (including the four already-resolved/ignored fleetd groups), nothing to GitHub or the GitLab mirror (I only read `pellam/fleetd` PRs, which the handbook names as the record of the module layout), nothing to Jira/Okta/PagerDuty/Datadog/Drive/Notion/Teams/the mailbox, and no Confluence edits.
- The three `dispatch-web` groups (DWEB-1JK/1JN/1KA) are in the Sentry org but not on the register and are the web team's, so I left them alone.

One correction worth flagging: I initially created the Billing ticket with an HTML-escaped ampersand in the title and immediately fixed it to `Crash routing 2026-11-16 — Billing & Settlement`. That edit was to a ticket I had just created, not to anything pre-existing.