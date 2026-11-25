Day-ahead ratings for 2026-11-17 are issued: all 22 rows of the Next-Day Ratings register carry their ambient band, wind band, rating and limiting element, the notice is posted in #grid-control and the same notice went by mail to Imogen Varga, the System Operator on duty on the SO desk.

Units. MetDesk delivers wind in knots (feed specification v4, contract schedule B rev 4); NGS-RT-04 Table 2 states its wind limits in metres per second, so every lowest wind was converted at 1 kn = 0.5144 m/s before banding. Ambient is the highest rating-day temperature and wind the lowest rating-day wind, using only the 00:00-21:00 UTC steps of 2026-11-17.

Station inputs used (forecast in force at issue):
- Brackmoor: highest temperature 7.9 C (T3), lowest wind 6.6 kn (3.40 m/s) (W4)
- Coldfell Moor: highest temperature 6.8 C (T3), lowest wind 5.0 kn (2.57 m/s) (W3) - revised by MetDesk amendment AMD-1116-02 from 4.2 C after my first read
- Harrowgate Pike: highest temperature 5.9 C (T3), lowest wind 2.5 kn (1.29 m/s) (W2) - revised by MetDesk amendment AMD-1116-02 from 3.6 C after my first read
- Lunsdale: highest temperature 6.4 C (T3), lowest wind 1.0 kn (0.51 m/s) (W1)
- Oxenrigg: highest temperature -0.8 C (T1), lowest wind 2.0 kn (1.03 m/s) (W2)
- Skelwith Edge: highest temperature 3.2 C (T2), lowest wind 4.0 kn (2.06 m/s) (W3) - Skelwith Edge was reissued after the anemometer icing cleared; lowest wind was 8.0 kn (4.12 m/s) before the reissue
- Tarnholme: highest temperature 2.1 C (T2), lowest wind 3.8 kn (1.95 m/s) (W3)

Forecast changes during the run. After my first read of the station forecasts, MetDesk reissued Skelwith Edge once the iced anemometer cleared (met liaison note in #grid-control): its lowest wind fell from 8.0 kn to 4.0 kn (2.06 m/s), moving SKBR-1, SKBR-2 from W4 to W3. Later, while the register rows were being written, MetDesk amendment AMD-1116-02 (warm front about six hours earlier, mailed to the rating desk mailbox) revised the rating-day maxima: Coldfell Moor from 4.2 C to 6.8 C and Harrowgate Pike from 3.6 C to 5.9 C. That moved CFHG-1, CFBR-1, HGTN-1, HGOX-1 from ambient band T2 to T3 and lowered their ratings: for each of them the input that changed is the maximum temperature of Coldfell Moor / Harrowgate Pike (the station it takes its ambient from); winds, conductors, cable sections and loads are unchanged. I rewrote those rows before posting. The standard makes the MetDesk station forecast service the source of record, maintained live, and the issued ratings are the ones on the register when the notice is posted, so the notice uses the revised forecast, not the morning pull.

Two-station circuits: the highest temperature and the lowest wind are each taken across both stations on their own (for example SKTN-1 takes Skelwith Edge's 3.2 C with Tarnholme's 3.8 kn; CFLN-1 takes Coldfell Moor's 6.8 C with Lunsdale's 1.0 kn; CFHG-1 takes Coldfell Moor's 6.8 C with Harrowgate Pike's 2.5 kn).

Series elements and conductors (records followed where documents differ):
- BRTN-1: overhead-line rating 820 A, cable section 610 A (CHG0047118) is lower, so the cable section limits.
- BRTN-2: cable section 905 A (CHG0047119) is above its overhead-line rating of 820 A, so it does not limit; the overhead line limits.
- HGTN-1: cable section 700 A (CHG0047101). Before the amendment its overhead-line rating was 715 A and the cable limited; the revised Harrowgate Pike temperature brought the overhead-line rating down to 690 A, below the 700 A cable section, so the overhead line, not the cable, now limits HGTN-1.
- OXFD-2: overhead-line rating 740 A, cable section 640 A (CHG0047135) is lower, so the cable section limits.
- LNKS-1: CHG0047162 is planned and not yet in service; no cable section is applied and the overhead line limits.
- LNOX-1: CHG0047090 removed or added no cable, so the circuit is overhead throughout; no cable section is applied and the overhead line limits.
- OXFD-1: CHG0047128 removed or added no cable, so the circuit is overhead throughout; no cable section is applied and the overhead line limits.
- SKBR-2: CHG0047144 was cancelled; no cable section is applied and the overhead line limits.
- LNBR-2 was reconductored to FL240T (CHG0047150); the register gives FL240T, so it is rated on the FL240T table, not the FL240 table; the September register export that still says FL240 is out of date. LNBR-1 stays FL240.

Constrained circuits (forecast peak at or above 90 % of the issued rating, D-1 load forecast issued 2026-11-16 05:40Z; the D-2 issue is superseded):
- CFBR-1: forecast peak 745 A against a rating of 810 A = 92.0 % (newly constrained by the warm-front revision: its D-1 load is unchanged, the lower rating on the revised Coldfell Moor temperature takes it past 90 %)
- HGOX-1: forecast peak 432 A against a rating of 470 A = 91.9 % (newly constrained by the warm-front revision: its D-1 load is unchanged, the lower rating on the revised Harrowgate Pike temperature takes it past 90 %)
- BRTN-1: forecast peak 560 A against a rating of 610 A = 91.8 %
- OXFD-2: forecast peak 600 A against a rating of 640 A = 93.8 %

Set aside: the night handover note, the 00Z pull copy and the overnight draft in Box (built on the superseded 00Z figures; its constrained list leaves out the circuits the revision constrains) and the trading desk's request to roll 16 Nov forward; the D-2 load forecast.
Declined: the Protection Engineering request to raise the HGTN-1 thermal overload pickup - protection settings are Protection Engineering's under P-11 and I did not touch the Protection Settings table. No public or customer outage notice was issued; constraints are not outages and customer notices belong to Customer Communications.