# Datadog monitors that feed the desk (notes, Nov 2026)

- **fleetd-workers goroutines > 250k** (id 74012): alerted 13 Nov 14:18 and 16:35. Correlates with the three OOM
  groups of that afternoon. Stack-based attribution is done in Sentry, not here.
- **fleetd exporter frame overflow > 0** (id 74019): warn since 11 Nov; counts `exporter.frame.overflow`.
- **tile cache publish after close** (id 74023): no data; metric was never emitted.
- **gateway session churn** (id 74031): ok.
The monitors tag `team:` from the service catalogue, which is per service, not per package; do not route on tags.
