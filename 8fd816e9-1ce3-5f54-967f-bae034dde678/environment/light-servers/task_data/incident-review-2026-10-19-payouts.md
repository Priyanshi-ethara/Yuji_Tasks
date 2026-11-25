# Post-incident review — Payouts degradation, 19 October 2026

Author: Marek Halloran · Reviewed: 23 Oct 2026 · Severity: SEV-2 · PagerDuty: PBW1107

## Summary
Between 00:52 and 01:19 UTC a connection-pool leak in payout-scheduler 4.19.1 starved the scheduler's database pool on
all three production cells. bank-file-dispatch, payout-status-api and sweep-reconciler queued behind it; sweep-reconciler
kept failing its reconciliation runs until 02:40 when the hotfix (4.19.2-hf1) was promoted.

## Timeline (UTC)
- 00:52 first 5xx burst on payout-scheduler (kestrel-1, kestrel-2, kestrel-3).
- 01:04 PagerDuty PBW1107 triggered (payout-scheduler), acknowledged by Celia Munro.
- 01:19 pool limit raised by config; scheduler recovers.
- 02:40 hotfix promoted to production cells.
- 02:55 sweep-reconciler backlog cleared.

## Impact
- 1,240 scheduled payouts delayed by up to 2 h 10 min. No payout lost.
- 37 merchant escalations (merchant-escalations-2026-10.csv).

## What went well / badly
- Well: the scheduler's burn monitor paged inside 12 minutes.
- Badly: the canary cell had been drained since the 16 Oct rollback of 4.19.2 and took no traffic that night, so the soak
  monitors stayed green.

## Actions
1. Pool sizing guard in payout-scheduler (PAY-412).
2. Re-check soak coverage when the canary cell is drained (PAY-413).
