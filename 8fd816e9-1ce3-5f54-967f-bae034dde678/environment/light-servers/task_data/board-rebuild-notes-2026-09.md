# Service boards v3 rebuild — notes (Soren Blackwood, Observability Platform, 2026-09-18)

## Why
Per-cell copies of every board (one per production cell plus the canary) had drifted. v3 keeps one board per
audience and adds template variables instead.

## What changed
1. Every service board has two template variables: `$cell` (values: kestrel-1, kestrel-2, kestrel-3, kestrel-*, wren-0)
   and `$region` (eu-west-1 only for now).
2. Every SLO widget's query carries `$cell` and `$region`; no widget pins a cell except the explicit canary widgets on
   the Acquiring board.
3. Board owners choose and save their boards' views; observability does not reset them.
4. The nightly export job exports SLO widgets from every service board.
5. Board ids stay the same as v2 so the SLO register's nominated panels did not need re-pointing.

## Known gaps
- Two boards per domain: the domain's service board and its on-call board. Titles are close; ids differ.
