# fleetd — repository layout (README, section 2)

Repository `pellam/fleetd`, default branch `main`. fleetd is Pellam Logistics' dispatch back end: one Go code base
that builds the `fleetd` server and the `simctl` replay tool.

| Path | What lives there |
|---|---|
| `cmd/fleetd/` | the server binary: flags, wiring, worker start-up (`cmd/fleetd/app`) |
| `cmd/simctl/` | the replay CLI used by dispatch analysts and Sim Tools |
| `api/` | protobuf contracts (`api/fleet/v2/*.proto`) |
| `internal/gen/` | code generated from `api/` by `buf generate` (protoc-gen-go, -go-grpc, -validate) |
| `internal/dispatch/` | assignment board, planner, dispatch HTTP API, vehicle leases (`lease/`) |
| `internal/manifest/` | manifest model and validation |
| `internal/billing/` | quotes, invoices, ledger store, settlement worker, settlement queue (`queue/`) |
| `internal/ingest/` | vehicle gateway sessions (`gateway/`) and frame decoding (`decode/`) |
| `internal/geo/` | ETA estimator (`eta/`), tile cache (`tiles/`), route planner (`planner/`) |
| `internal/notify/` | outbox publisher, digests, fan-out hub, push sender, retry backoff |
| `internal/telemetry/` | span batching and export |
| `internal/platform/` | logging sink, config, feature flags |
| `internal/httpx/` | HTTP server plumbing, problem+json responses |
| `tools/simkit/` | simulation clock, tickers, timing wheel, ring buffer and scheduler used across the server |
| `tools/simctl/` | the replay engine behind `cmd/simctl` |
| `third_party/` | patched forks kept in-tree (currently empty after the 2026-07 clean-up) |
| `vendor/` | vendored dependencies (`go mod vendor`) |
| `docs/` | design notes |

Building: `make build` (see the build and release page in the PENG space for flags). Tests: `make test`.
Ownership: `.github/CODEOWNERS`, reviewed by Platform Foundations; triage reads it as the SRE handbook says.
