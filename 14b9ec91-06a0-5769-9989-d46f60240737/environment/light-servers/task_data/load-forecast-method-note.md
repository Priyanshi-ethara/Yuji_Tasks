# Day-ahead load forecast - method note (Load Forecasting team)

- Issues per rating day: D-2 (two days before, 05:40Z) and D-1 (the day before, 05:40Z).
- Each issue is published as an event on the monitoring event stream, titled
  "Day-ahead load forecast <issue> for <rating day> (issued <time>)", listing each circuit's forecast peak in amperes.
- The D-1 issue supersedes the D-2 issue for the same rating day. Older issues stay on the stream for audit.
- Forecast peaks are circuit currents at the hour of system peak (17:00-18:00 local in November).
