# Harrowmere AMR — half-hourly export format (in-house collection)

Owner: Data Collection (Bertrand Ilsley). Applies to files named `amr-hh-export-*.csv` produced by the in-house
automatic meter reading (AMR) head-end. Other collectors deliver in their own formats under their data
collection agreements; this note does not describe them.

| Column | Meaning |
|---|---|
| site_ref | Harrowmere site reference (HMS-nnnn) as held on the site account |
| msn | meter serial number |
| period_start_utc | UTC instant at which the half-hour settlement period BEGINS (ISO 8601, `Z`) |
| kwh | active import energy in the period, kWh, three decimals |
| kvarh | reactive import energy in the period, kvarh, three decimals |
| read_status | A = actual read retrieved from the meter, E = estimated by the head-end |

Notes
1. The head-end clock is UTC all year. It does not observe British Summer Time; a local-time view has to be
   derived when a rule is written in civil time.
2. Each run's export carries a margin of a few hours before and after the billing period so that late
   periods are not cut off. The margin rows are not part of the billing period.
3. A site that joins or leaves supply part-way through a period is exported for every period the head-end
   could read. Whether a period is billable is decided by the site account, not by the export.
4. Values are as read from the meter. The meter applies the CT ratio it is programmed with (recorded in its
   commissioning record); the head-end applies no multiplier of its own.
5. File checksums are posted to the collector deliveries table in the metering operations base.
