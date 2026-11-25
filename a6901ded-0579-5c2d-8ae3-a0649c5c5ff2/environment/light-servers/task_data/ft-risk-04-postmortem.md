# Post-mortem: FT-RISK-04 ran past its reservation (12 Nov 2026)

Author: Noor Bassi · Incident INC0042071 · Problem PRB0000311

## What happened
The reservation for FT-RISK-04 was 9 hours from 06:00 UTC. The job finished at 16:20 UTC, 1 h 20 min after the reservation ended,
and overlapped a Pricing slot on ft-pool-north.

## Why
- The dry run was taken on 5 Nov with the spec as it stood then (accumulation 2): 8.10 s per update.
- On 9 Nov the spec moved to accumulation 3 so its effective batch matched RCP-RISK-2 again (8 x 3 x 8 = 192); its warm-up change went to sign-off (MLR-87).
- The desk sized the reservation from the dry run as recorded: 3000 x 8.10 / 3600 = 6.75, rounded up to 7 h, plus a 2 h margin the owner asked for.
- At accumulation 3 each update runs three micro-batches instead of two, so the job needed about 12.15 s per update: 3000 x 12.15 / 3600 = 10.1 h.

## Actions
1. RB-ML-014 5.1 already says dry-run time scales in proportion to accumulation; the desk applies it whenever spec and dry run differ.
2. No margins on top of the rule; the rule is the reservation.
3. Owners re-run the dry run after a spec change when they can; when they cannot, the desk scales.
