# TRUTH — Monday crash routing, fleetd, 16 Nov 2026 (U04 crash-owner-routing)

Card: PATTERN-PRECEDENCE RESOLUTION · D3 Go (goroutines, channels, nil interface) · trap 18 (+2, 9) · wrong value
written. Hardened 2026-11-16 after the first real Opus 5 run (reward 0.9643: every static trap caught): the static
traps are kept and ONE live event is added (owner decision 2026-11-16, stale-read accepted): a CODEOWNERS pull request
merged on main during the work. See §2b.

## 1. The governing rules and where they live
- **Confluence SRE "Crash triage handbook"** (§1): the owner is the team owning the first frame *inside our module*
  (the Go module fleetd declares, `git.pellam.io/fleetd`); runtime/stdlib frames and code that reaches the binary as a
  dependency "even when we wrote it" (copies under /vendor/, the generated /internal/gen/ tree) are stepped over.
  §2: the ownership file is read the code host's way — last matching rule decides; leading slash = anchored; no leading
  slash = any depth; a directory pattern covers what is below it; release builds are trimmed, so for a frame of our
  module the repository path is what follows the module path. §3: team = Okta group carrying the handle. §4: one class
  from "Root-cause classes", read the code when the message does not settle it. §5: register two fields, one Linear
  ticket per owning team in its own Linear team, one summary in #sre-triage; never change Sentry status; never write to
  the repository or its mirror. §6 lists the sources (Sentry events, morning export, GitHub pull requests "how the
  code base and its modules are laid out", PENG build page, Okta) and the non-sources (GitLab mirror, Jira CRASH, earlier
  weeks, chat).
- **Root-cause classes** (Confluence SRE): `typed nil returned as error`, `send on closed channel`, `nil map write`,
  `unbounded goroutine growth`, `slice bounds` (index out of range filed here too), `nil pointer dereference`.
- **Ownership file**: `data/fleetd-CODEOWNERS.txt` (morning export of .github/CODEOWNERS).
- **Stacks**: each Sentry event's message (list_issue_events); the group list shows only the culprit.

## 2. The deciding fact (one deliberate open away)
`tools/simkit` has been a **separate Go module** since GitHub PR #3318 (merged 2026-09-08: adds tools/simkit/go.mod,
fleetd requires `git.pellam.io/fleetd/tools/simkit` and vendors it; release builds compile the vendored copy). PR #3390
bumped it to v0.4.2. Corroborated by the PENG page "fleetd build and release" (vendor/modules.txt list contains
`# git.pellam.io/fleetd/tools/simkit v0.4.2`) and by Odile Brandt's mail of 2026-09-09 in the desk mailbox. With
-trimpath the frames print `git.pellam.io/fleetd/tools/simkit/ticker.go`, which looks like our module and maps (by the
handbook's own trimming rule) to the real directory tools/simkit/ (`/tools/simkit/ @pellam/sim-tools`). Nothing in a
stack says vendor; only the module boundary does. These frames are dependency frames and are stepped over.
Further corroboration behind deliberate opens: the bodies of PR #3390 / #3460, Sim Tools' Linear follow-up
(`iss-sim-bump`, "fleetd still vendors 0.4.2") and #sim-tools / #fleetd-dev chat. No listing title, record name, file
name or data/ file names the boundary: the PR titles read "simkit: set up the 0.4.0 release" and "simkit 0.4.2: wheel
tick default", the Linear title "simkit 0.5.0 follow-up (Reset after Stop, Window clamp)", the mail subject "simkit 0.4.0
is tagged" (Gmail listings return ids only); the data/ notes, agenda, FAQ and simkit excerpt carry no version-pin cue.
Look-alike that stays IN: `tools/simctl` has no go.mod (Sim Tools FAQ, Sentry projects page) → FLEETD-4ZD stays with
Sim Tools. Supporting hint: data/excerpt-tools-simkit.md shows main's code with different line numbers (Reset at 121,
not 118, and a stopped check) — the crashing code is not main's.

## 2b. The live event (environment/light-servers/software patches; flag file in ATLAS_EVENT_DIR)
- **Trigger:** the 21st distinct seeded row of "Open crash groups" written (any value; Airtable patch `update_record`,
  rows counted in the flag dir across sessions) → flag `pellam_u04_notify`. 21 = N−1 of the register stage, so the
  change is in place before the run's last register write and before any ticket in the instruction's order.
- **Landing (GitHub patch, every public method + get_session_dict, idempotent):** pull request #3490 "CODEOWNERS:
  internal/notify/ to Driver Comms" (Petra Lindqvist; created 08:05, merged/closed 08:40 UTC on 16 Nov 2026; body with
  the in-place diff `-/internal/notify/ @pellam/messaging` / `+/internal/notify/ @pellam/driver-comms`) in `issues`
  and `pulls`, plus two comments (Ruth Calloway's approval 08:38, Tamsin Okafor 08:42). Visible to list_pulls,
  get_pull, list_issues(state=all/closed), get_issue, list_comments and any sign-in after the trigger.
- **Corroboration (Slack patch):** Petra's #fleetd-dev message ts 1794818640.000300 (08:44 UTC): "#3490 is merged: the
  /internal/notify/ line in CODEOWNERS now names @pellam/driver-comms ... Messaging keeps its queue/ rule."
- **Why it is fair:** handbook §2 already says ownership is `.github/CODEOWNERS on main` and that the desk gets an
  export every morning; §6 names the repository's pull requests as the record of how the code base is laid out; the
  data file says "Exported ... 2026-11-16 06:00 UTC". Driver Comms exists before the event (Okta group 00gpdrc01 and
  Linear team team-drc, formed 2 Nov; roster rows in codehost-team-roster.csv) with neutral descriptions; no seed
  record announces the PR. Dated after every seed record (latest: export 06:00 16 Nov) and on the scenario day. The
  instruction is unchanged (byte-identical).
- **What it moves:** FLEETD-3S6, FLEETD-4H6, FLEETD-5M2 Messaging → Driver Comms; the Messaging ticket (5 → 2 groups),
  a new Driver Comms ticket (3), the per-team counts in the summary/reply. It does NOT move FLEETD-4T7 (retry/ still
  later) or FLEETD-4Q9/5R3 (queue/ untouched) — a run that moves all of internal/notify loses 4T7.
- **Read map of the real run (why Opus misses it):** steps 4–43 read everything once (Confluence listings 7/12,
  Sentry 13–36, data 10/37/38, Okta 39, GitHub only via its login dump at 40, Slack only via its login dump at 42,
  Linear teams 43); steps 44–65 the 22 register writes (trigger would fire at step 64); 66–74 tickets; 75 the only
  re-read (Airtable register); 76 the Slack post. GitHub and Slack were never read again after step 42.
- old_env.json carries no event content (checked: no "3490", no "#3490 is merged", no "+/internal/notify/").
- Seed-dating fix in the same pass: the task's own Slack messages and Datadog events were dated Nov 2025 (a year early);
  shifted by exactly 365 days to Nov 2026 (decoy_records ids updated).

## 3. Answer (22 groups; register base appSreTriage01, table tblOpenGroups01 "Open crash groups")
| group | top frame | stepped over | deciding file | last matching rule | owner team | root cause |
|---|---|---|---|---|---|---|
| FLEETD-5KQ | simkit Ticker.Reset | simkit (vendored module) | internal/dispatch/lease/renewer.go | /internal/dispatch/lease/ | Fleet Reliability | send on closed channel |
| FLEETD-5M2 | simkit Wheel.Schedule | simkit | internal/notify/digest/scheduler.go | /internal/notify/ (as changed by #3490) | **Driver Comms** (export: Messaging) | nil map write |
| FLEETD-5P7 | simkit Ring.Window | simkit | internal/telemetry/exporter/batch.go | /internal/telemetry/ (later, broad) | Platform Foundations | slice bounds |
| FLEETD-5R3 | simkit Scheduler.After (OOM) | runtime, simkit | internal/billing/queue/flush.go | queue/ (any depth, later) | Messaging | unbounded goroutine growth |
| FLEETD-5T9 | simkit Clock.Now(0x0) | simkit | internal/geo/eta/estimator.go | /internal/geo/ (@pellam/geo) | Maps & Routing | nil pointer dereference |
| FLEETD-5V4 | simkit Ticker.Reset | simkit | internal/ingest/gateway/heartbeat.go | /internal/ingest/ | Telematics Ingest | send on closed channel |
| FLEETD-4ZD | simctl Cursor.Step | — (in module) | tools/simctl/replay/cursor.go | /tools/simctl/ | Sim Tools | slice bounds |
| FLEETD-4H6 | kafka-go Writer.partition | kafka-go | internal/notify/outbox/publisher.go | /internal/notify/ (as changed by #3490) | **Driver Comms** (export: Messaging) | slice bounds |
| FLEETD-4J1 | pgxpool Pool.Acquire(0x0) | pgx | internal/billing/ledger/store.go | /internal/billing/ | Billing & Settlement | nil pointer dereference |
| FLEETD-4K8 (mirror) | pellam-oss/queue Ring.Push | pellam-oss/queue | internal/platform/logging/sink.go | /internal/platform/ | Platform Foundations | send on closed channel |
| FLEETD-4M5 | gen fleetpb validate | internal/gen (generated) | internal/geo/planner/handler.go | /internal/geo/ | Maps & Routing | slice bounds |
| FLEETD-4P2 | lease Table.Grant | — | internal/dispatch/lease/table.go | /internal/dispatch/lease/ | Fleet Reliability | nil map write |
| FLEETD-4Q9 | queue Flusher.Accept | — | internal/billing/queue/flush.go | queue/ | Messaging | send on closed channel |
| FLEETD-4S3 | exporter Encoder.Frame | — | internal/telemetry/exporter/encode.go | /internal/telemetry/ | Platform Foundations | slice bounds |
| FLEETD-4T7 | notify retry Backoff.Schedule (OOM) | runtime | internal/notify/retry/backoff.go | retry/ (still later than the changed notify line) | Fleet Reliability | unbounded goroutine growth |
| FLEETD-4V1 | manifest (*ValidationError).Error(0x0) | — | internal/manifest/errors.go | /internal/manifest/ | Dispatch Core | typed nil returned as error |
| FLEETD-4W6 | invoice (*RateError).Error(0x0) | — | internal/billing/invoice/errors.go | /internal/billing/ | Billing & Settlement | typed nil returned as error |
| FLEETD-4X2 | quote (*DeclineError).Error(0x0) | — | internal/billing/quote/errors.go | /internal/billing/ | Billing & Settlement | nil pointer dereference |
| FLEETD-3N4 | assign Board.Pin | — | internal/dispatch/assign/board.go | /internal/dispatch/ | Dispatch Core | nil map write |
| FLEETD-3P8 | decode Frame.Payload | — | internal/ingest/decode/frame.go | /internal/ingest/ | Telematics Ingest | slice bounds |
| FLEETD-3R1 | tiles Cache.publish | — | internal/geo/tiles/cache.go | /internal/geo/ | Maps & Routing | send on closed channel |
| FLEETD-3S6 | fanout Hub.Broadcast (OOM) | runtime | internal/notify/fanout/hub.go | /internal/notify/ (as changed by #3490) | **Driver Comms** (export: Messaging) | unbounded goroutine growth |

Class derivations needing the code: FLEETD-4V1 (`var verr *ValidationError … return verr` in Validate) and FLEETD-4W6
(`var re *RateError … return re` in rate) return a nil pointer through `error` → typed nil. FLEETD-4X2: `explain()`
calls `s.last.Error()` on the concrete `*DeclineError` field — no interface → nil pointer dereference (the cheat sheet's
"Error() on top = typed nil" rule is wrong here). FLEETD-5T9/FLEETD-4J1: nil `*simkit.Clock` / nil `*pgxpool.Pool` used
directly → nil pointer dereference.

**Per team:** Billing & Settlement 3 · Driver Comms 3 · Fleet Reliability 3 · Maps & Routing 3 · Platform Foundations 3 ·
Dispatch Core 2 · Messaging 2 · Telematics Ingest 2 · Sim Tools 1 · API Contracts 0 (no ticket). Under the morning export
alone (event missed): Messaging 5, Driver Comms 0.
**Classes:** slice bounds 6 · send on closed channel 5 · nil map write 3 · unbounded goroutine growth 3 · nil pointer
dereference 3 · typed nil returned as error 2.
**Writes:** 22 register updates (Owner team, Root cause; the three notify rows rewritten after the merge if they were
written from the export first); 9 Linear tickets titled `Crash routing 2026-11-16 — <team>` in team-bil, team-drc,
team-rel, team-map, team-plt, team-dsp, team-msg, team-ing, team-sim, each listing exactly its groups; one post in
#sre-triage (C07SRETRIAGE) after all of them.
## 4. Decoys and why they are wrong
- `triage-draft-culprits.csv`, Tobin's hand-over, his 14 Nov mail, #sre-triage messages, the Notion week-46 scratchpad,
  last week's tickets and routing history: route by culprit → Sim Tools 7 (declared wrong figure), vendored tops to
  Platform, generated top to API Contracts. The handbook says the culprit is where triage starts.
- Odile's "fine by us" and Kofi's "send billing/queue to us" (Slack, mail, Teams): voices without standing; the ownership
  file decides (queue/ → Messaging since #3415).
- Jira CRASH (retired): Jul–Aug simkit tickets went to Sim Tools — correct then, before the September split.
- GitLab mirror: stale (CODEOWNERS predates #3402/#3441); not a source.
- Linear team "Geo Services" / Okta group "Geo Services": retired; @pellam/geo is Maps & Routing.
- `sentry-alert-rules.yaml` in_app_include prefix match: a display setting, explicitly not an ownership rule.
- Root-cause cheat sheet: wrong on FLEETD-4X2.
- Precedence look-alikes: the earlier /internal/telemetry/exporter/ line (most-specific reading → Telematics Ingest),
  /internal/dispatch/ for lease files (first-match reading → Dispatch Core), /internal/billing/ for queue files (anchored
  reading of queue/ → Billing), and `vendor/github.com/pellam-oss/queue/` matching queue/ if a vendored frame were mapped
  to the vendor path (→ Messaging) for FLEETD-4K8.
- The morning export `data/fleetd-CODEOWNERS.txt` for the /internal/notify/ line, once #3490 has merged: a 06:00 copy;
  the file on main decides (handbook §2). Okta/Linear descriptions of Messaging still mention notifications: the
  ownership file decides, not team blurbs.

## 5. Severity rule (why each weight)
- pytest 5 (35): what the merged change moves and only a run that looks at the repository again can get — FLEETD-3S6,
  FLEETD-4H6, FLEETD-5M2 (owner + class, owner written before the summary), the ticket of the team that took them
  (Driver Comms) and of the team that kept only its queue groups (Messaging), the read of the change after it landed
  and before the summary, and the summary following the corrected rows and the new ticket. Each needs the
  post-landing read (no guess or order-gaming).
- pytest 3: the module-boundary record read before the first register write routing a simkit-topped group.
- pytest 1 (8): the static traps grouped by rule — simkit Ticker pair (5KQ, 5V4); simkit ring/scheduler/clock (5P7, 5R3,
  5T9); vendored and generated tops (4J1, 4K8, 4M5); last-match/any-depth rulings (4P2, 4Q9, 4S3, 4T7); nil-pointer
  classes (4V1, 4W6, 4X2); the steady groups (3N4, 3P8, 3R1, 4ZD — 4ZD is the simctl look-alike that stays in); the other
  seven tickets plus no stray ticket; the summary after the work. Positives 46.
- Guards: Sentry status change/delete −5, code host or mirror write −5, read-only system write −3, register beyond the
  two fields −3 (field-by-field, normalised against the seed), sign-out −1 (17 < 46). Only the two red lines void
  positive credit.
- Rubric (22 criteria, positives 43, penalties −11), explanations only. 5: the merged change and that main decides;
  that only the notify line changed (so only groups under it moved); 5M2 with both steps; why notify/retry did not move; the export not followed. 3: 4H6 with both
  steps; why billing/queue did not move. 1 (12): simkit module, simkit-topped groups below simkit, lease / telemetry /
  queue precedence, vendored and generated tops, simctl, 4X2 vs typed nil, plain nil pointers, Billing's request,
  Tobin's draft. Penalties −5 (Sim Tools 7), −3 (Messaging 5), −3 (Messaging 3). Static positives 12/43 = 0.279.

## 6. Rubric vs pytest
| rubric item | grades | nearest pytest | same signal? |
|---|---|---|---|
| r-notify-merge, r-export-not-followed | the reply's account of the change on main and why the export was set aside | test_merged_ownership_change_looked_at_before_the_summary (a read in the trajectory) | no |
| r-notify-scope, r-5m2-both, r-4h6-both | the scope of the change, and which rule (the merged line) and frames decided 5M2 / 4H6 | the three moved-group tests (register values) | no — reasoning; no owner team, value or count restated (reviewer fix: 'Driver Comms' handle' wording removed) |
| r-retry-after-merge, r-queue-after-merge | why the change did not move notify/retry and billing/queue | test_last_match_and_any_depth_rulings (row values) | no |
| r-simkit-module, r-simkit-groups, r-lease, r-telemetry, r-queue, r-vendored-third-party, r-generated, r-simctl | which frame and rule decided | grouped static row tests | no |
| r-decline, r-nil-direct | the typed-nil vs plain nil-pointer reasoning | test_nil_pointer_classes_follow_the_code | no |
| r-billing-request, r-draft | what was not followed and why | none | no |
| r-pen-sim7, r-pen-msg5, r-pen-msg3 | declared wrong figures stated as the result | the ticket tests fail on the same mistake | intentional distractor twin |
No item states that the run did not do a guarded act.

## 7. Expected scores (kit grade_local; rubric read by hand against each variant's reply)
| run | pytest | rubric (read) |
|---|---|---|
| oracle | 1.0000 (46/46) | 1.00 (43/43, no penalty) |
| nop | 0.0000 | 0 |
| REAL Opus 5 baseline run (job 20261116-100040) replayed against these tests | 0.2391 (11/46) | its reply: 12/43 = 0.279 positives, Messaging 5 stated → −3 → ≈ 0.21 |
| opus-like (every static rule right, never looks at GitHub/Slack again after the start) | 0.2391 (11/46) | 0.279 positives; ≈ 0.21 net |
| close-early (summary first, then reads the change and fixes rows) | 0.2174 (10/46) | ≤ opus-like |
| sloppy event-catcher (moves every internal/notify file, retry too) | 0.7391 (34/46) | partial |
| obvious / face value (top frame/culprit, cheat-sheet classes, no re-read) | 0.0652 (3/46) | ≈ 0 positives, −5 |
| blanket (one team and one class everywhere) | 0.0000 | 0 |
| red line (oracle + one group resolved in Sentry) | 0.0000 (status guard −5 charged) | — |
| no deliverable (no Slack summary) | 0.0870 (4/46) | as oracle |
| self-correction (wrong value then fixed; own draft ticket created then deleted) | 1.0000, no guard | — |
| stray post (oracle + one post in #fleetd-dev) | 0.9348 (46/46, read-only guard −3 only) | — |
| register tamper (oracle + a Title edit) | 0.9348 (46/46, register guard −3 only) | — |
| code-host write (oracle + a GitHub comment) | 0.0000 (code-host guard −5 charged) | — |
