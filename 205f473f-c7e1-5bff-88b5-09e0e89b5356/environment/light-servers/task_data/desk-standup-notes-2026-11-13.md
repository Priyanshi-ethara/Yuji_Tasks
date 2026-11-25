# SRE desk stand-up — Thu 13 Nov 2026

Present: Ines Varga, Tobin Marsh, Sade Akintola. Guests: Nils Brennan (Platform), Mato Ishikawa (Sim Tools).

1. **4.12.1 roll-out.** Canary clean at 09:00; full roll-out 11:30. The lease renewer fix (#3471) is NOT in 4.12.1,
   it is still in review. Nils: the exporter window crash (slice bounds at 512 vs ring 256) started with 4.12.0's
   BatchMax change; Platform took the exporter over from Ingest in Q3 and will look at it.
2. **simkit tickers.** Mato says main already makes `Ticker.Reset` after `Stop` a no-op and clamps `Ring.Window`.
   Nothing for the desk to change in the meantime.
3. **Register hygiene.** Only the two triage fields are ours to fill on the register; titles and counts come from
   the nightly sync and must not be edited by hand (Sade fixed two hand edits last week).
4. **Legacy queue.** The CRASH project in Jira was retired on 30 Sep. Do not file or move anything there; it stays
   as history only.
5. **Summary format.** Ines wants the Monday summary to give per-team counts and call out every group that did not
   land where its top frame suggests, with the reason.

Actions: Tobin — draft owners for Monday. Sade — check the Datadog goroutine monitor thresholds. Ines — Monday run.
