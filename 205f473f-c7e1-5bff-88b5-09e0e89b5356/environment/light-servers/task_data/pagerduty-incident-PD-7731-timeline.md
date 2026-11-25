# PD-7731 — push provider 5xx, retries piling up (13 Nov 2026)

| UTC | What |
|---|---|
| 14:02 | Push provider starts returning 503. notify/push marks every send for retry. |
| 14:20 | First OOM on fleetd-workers-2 (settlement queue flusher: one scheduler callback goroutine per item). |
| 16:40 | Second OOM: notify retry backoff, one sleeping goroutine per failed push. |
| 17:00 | Third OOM: fan-out hub broadcast goroutines. |
| 18:02 | Provider partially back; retries drain slowly. |
| 19:31 | Resolved. Workers restarted twice. |

Responders: Juno Takahara (Fleet Reliability on call), Cassius Ferreira (Messaging), Sade Akintola (SRE desk).
Follow-ups: bound the backoff (Fleet Reliability, retry/ is theirs); bound the hub; bound the flusher's callbacks.
