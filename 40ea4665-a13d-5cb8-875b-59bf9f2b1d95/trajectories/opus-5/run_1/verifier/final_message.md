Imogen — BR-2611 is drafted. 22 drafts in QuickBooks (IDs 9223–9244), invoice date 16 Nov 2026, due 30 Nov 2026, one per site against the ledger customer its site Account names. One summary mail sent to you only. Nothing sent, issued, emailed or collected; no payment raised; nothing touched in Xero or Stripe; no meter reading, meter record or platform bill altered; no customer contacted. Still signed in everywhere.

**Summary mail subject sent:** `BR-2611 drafts ready: 22 invoices, £254015.70`

---

## 1. Per site

| Site | Name | QB | kWh Ed6 | kWh Ed7 | kWh total | MD Ed6 (kW) | MD Ed7 (kW) | Net total |
|---|---|---|---|---|---|---|---|---|
| HMS-1047 | Calloway Mill Bakery | 9223 | 14,446.838 | 11,527.706 | 25,974.544 | 96.93 | 96.29 | £5,730.40 |
| HMS-1052 | Ostrey Lane Medical Centre | 9224 | 7,645.565 | 6,092.111 | 13,737.676 | 48.84 | 48.80 | £3,752.99 |
| HMS-1068 | Pellingford Community School | 9225 | 7,069.669 | 7,943.715 | 15,013.384 | 72.10 | 72.97 | £4,059.44 |
| HMS-1073 | Quenby Print Works | 9226 | 27,451.057 | 21,713.286 | 49,164.343 | 135.48 | 127.69 | £12,905.70 |
| HMS-1081 | Saltash Row Garage | 9227 | 4,946.045 | 4,142.011 | 9,088.056 | 37.27 | 36.85 | £2,562.91 |
| HMS-1094 | Thornaby Wharf Cold Store | 9228 | 39,110.499 | 31,355.986 | 70,466.485 | 151.92 | 149.94 | £17,139.72 |
| HMS-1102 | Harrowmere Leisure Pool | 9229 | 47,201.461 | 38,542.764 | 85,744.225 | 168.45 | 166.88 | £21,526.95 |
| HMS-1115 | Wendle Street Offices | 9230 | 10,368.154 | 8,748.577 | 19,116.731 | 64.06 | 67.47 | £5,147.46 |
| HMS-1123 | Marlpit Garden Centre | 9231 | 6,547.170 | 1,904.737 | 8,451.907 | 42.41 | 42.92 | £2,257.25 |
| HMS-1139 | Brookhay Brewery Taproom | 9232 | 7,451.785 | 9,904.230 | 17,356.015 | 84.68 | 86.04 | £4,573.64 |
| HMS-1146 | Ashgrove Plastics Moulding | 9233 | 83,398.569 | 66,071.134 | 149,469.703 | 314.66 | 304.58 | £36,344.39 |
| HMS-1158 | Fenwick Lane Data Hall | 9234 | 75,121.994 | 62,332.518 | 137,454.512 | 218.33 | 211.64 | £32,896.10 |
| HMS-1160 | Gorsebrook Laundry Services | 9235 | 33,575.537 | 27,423.910 | 60,999.447 | 145.09 | 145.66 | £15,863.39 |
| HMS-1177 | Hollin Bridge Sawmill | 9236 | 19,436.215 | 16,533.225 | 35,969.440 | 179.90 | 180.90 | £9,462.70 |
| HMS-1183 | Kittering Foods Packing | 9237 | 59,499.431 | 47,346.295 | 106,845.726 | 228.55 | 229.47 | £27,147.82 |
| HMS-1191 | Wexcombe Craft Studios | 9238 | 2,499.054 | 2,096.256 | 4,595.310 | 17.58 | 18.03 | £1,330.43 |
| HMS-1204 | Lanyon Quay Fish Market | 9239 | 22,297.503 | 18,281.102 | 40,578.605 | 107.72 | 109.13 | £9,562.67 |
| HMS-1212 | Merrowby Care Home | 9240 | 21,361.434 | 17,890.834 | 39,252.268 | 82.96 | 84.63 | £9,810.21 |
| HMS-1229 | Netherfold Veterinary Hospital | 9241 | 25,510.576 | 20,518.392 | 46,028.968 | 90.52 | 87.70 | £11,420.66 |
| HMS-1235 | Orchard Rise Hotel | 9242 | 32,423.088 | 27,308.651 | 59,731.739 | 157.72 | 157.81 | £14,957.05 |
| HMS-1248 | Penhallow Tool Hire | 9243 | 4,451.623 | 3,632.466 | 8,084.089 | 30.17 | 29.47 | £2,233.00 |
| HMS-1256 | Ravensworth Bowls Club | 9244 | 6,665.724 | 5,377.005 | 12,042.729 | 48.44 | 47.97 | £3,330.82 |

Standing-charge days are 17 (Ed 6) + 14 (Ed 7) for every site except Marlpit (17 + 5) and Brookhay (10 + 14).

## 2. Run totals
- Edition 6 (consumption 15–31 Oct): **558,478.991 kWh**
- Edition 7 (consumption 1–14 Nov): **456,686.911 kWh**
- Total billed energy: **1,015,165.902 kWh**
- Run net total: **£254,015.70**

## 3. Editions and the clock change
Each half-hour was priced at the edition in force when its energy was consumed (BP-4 3.1; audit finding 1), not by bill date. I derived each half-hour's UK civil start time from its UTC start, then used the civil date of that start to pick the edition (Ed 6 to 31 Oct, Ed 7 from 1 Nov per the edition pages and the index) and the civil start time to pick the band (Peak 16:00–19:00 Mon–Fri, Night 00:00–07:00, Day otherwise).

The clock change fell on Sunday 25 October, clocks back at 02:00 BST / 01:00 UTC. Working in civil time from UTC start instants gives that day 50 half-hours automatically, with the 01:00–02:00 hour occurring twice — 16 half-hours in the Night window rather than 14, all Night, and no Peak because it is a Sunday. That is what I got, and it matches the bands page and the clock-change calendar. The Ed 6 part is therefore 818 half-hours over 17 days and the Ed 7 part 672 over 14 days; 1,490 per full-period site, which agrees with the MDM staging expectation. The clock change does not move the band boundaries — they stay at civil 16:00/19:00 and 00:00/07:00.

## 4. Sites needing more than the standard method

**Four Kestrel meters register demand, not energy (biggest adjustment).** The commissioning records in the asset register for K24C10417 (Ashgrove), K24C10452 (Fenwick Lane), K24C10488 (Gorsebrook) and K24C10519 (Kittering) say the A+ and R+ registers were programmed under MOPS-1184 to record the **mean demand** over each half-hour (kW on A+, kvar on R+) for the capacity dashboard, and that the energy in a period is mean demand × 0.5 h. KDS-HRM-2026 Schedule 2 §2.3 confirms Kestrel passes channel values through exactly as the meter registers them, with no scaling, and the Kestrel service report repeats it. So for those four sites I halved both channels to get kWh and kvarh. Demand then comes straight back out as the registered value, which is why their maximum demands look sane against the energy.
- The other two Kestrel meters, K24C10503 (Hollin Bridge) and K24C10541 (Wexcombe), have records saying they kept **energy** programming because those customers cancelled/declined the capacity-monitoring order, so their channels were used unchanged.

**All six Varden sites are end-stamped.** The commissioning records for E18H72206, E20H45573, E19H38861, E21H09946, E20H52708 and E19H64413 all state Varden's Schedule 3 files stamp each period at its **end**, UTC, and VMS-DCA-2026 Schedule 3 §3.2 spells out the period-ending convention. I shifted every Varden timestamp back 30 minutes to get the period start before banding. Cross-check: after the shift all three collectors cover exactly the same 1,500 half-hours (start 14 Oct 21:00 UTC to 15 Nov 02:30 UTC), which is the two-hour margin either side the delivery note describes. Unshifted, the Varden sites would have been banded half an hour late.

**Brookhay Brewery Taproom (HMS-1139)** — new connection. The site Account gives Supply start 22 Oct 2026, so I billed 22 Oct – 14 Nov: 10 Ed 6 days and 14 Ed 7 days, 482 + 672 half-hours. The export carries the full period, but BP-4 5.1 puts the decision with the site account, and the AMR readme §3 says the same. The customer's email claims the supply "transferred this week" (23 Oct) and the meter was fitted 14 Oct; I went with the account's 22 Oct.

**Marlpit Garden Centre (HMS-1123)** — change of supplier. The site Account gives Supply end 5 Nov 2026 with the loss reason "new supplier registered from 6 Nov 2026 00:00", so I billed to 5 Nov inclusive: 17 Ed 6 days and 5 Ed 7 days. The customer's email says the switch completes "on or around 6 November", which is vaguer; the account date governed.

**Wendle Street Offices (HMS-1115)** — Supply end 31 Dec 2026 is after the run period, so under BP-4 5.2 it does not shorten anything. Billed the full 31 days.

**Orchard Rise Hotel (HMS-1235)** — the site Account names "Orchard Rise Hotel Ltd" as ledger customer, so the draft is against customer 7120, not the "Orchard Rise Hotels Group" parent (7191), which has no supply.

No estimated or substituted periods anywhere: AMR read_status all A, Kestrel qual all V, Varden FLAG all 0. No gaps or duplicate periods; every full-period site had its 1,490 billable half-hours. No meter exchange in the exchange log touches any of the 22 sites inside the run period.

## 5. Capacity and excess reactive charges
**Capacity.** Demand in a half-hour (kW) = that half-hour's active energy (kWh) × 2. Maximum demand is the highest such demand among the on-supply half-hours **of that edition part**, taken separately for Ed 6 and Ed 7 and rounded half up to 0.01 kW. Charge = maximum demand × days on supply in that part × that edition's rate (4.800 p/kW/day Ed 6, 5.350 p/kW/day Ed 7), converted to pounds and rounded half up to the penny. I checked my arithmetic against the worked example in the capacity-charge explainer (123.00 kW × 17 days × £0.048 = £100.37) and it reproduces.

**Excess reactive.** Half-hour by half-hour: excess = kvarh − 0.33 × that same half-hour's kWh, where positive, nil otherwise. The excesses are summed within each edition part, rounded half up to 0.001 kvarh and charged at that edition's rate (2.415 p Ed 6, 2.780 p Ed 7). No monthly-average netting — the method page records that the Editions 1–3 average approach was withdrawn in 2024, and a good month does not offset a bad half-hour. For the four mean-demand Kestrel meters the kvar channel was halved to kvarh first, so the 33% test compares like with like. Eleven sites came out with excess; the rest are nil and I left those lines off, as BP-4 8.2 allows.

Other rounding, per BP-4 7: band energy summed at full precision per edition part then rounded half up to 0.001 kWh; each line amount rounded half up to the penny; the draft net total is the sum of the line amounts.

## 6. Records and figures I did not follow
1. **Dorian's trial sheet (`br2611-draft-run-sheet-dfelbrigg.csv`, total £376,700.10).** Priced on Edition 7 throughout on the grounds that BR-2611 is the first run issued after the Ed 7 launch. That is precisely the error audit finding 1 closed, and BP-4 3.1 says the bill date does not decide the edition. The sheet also banded straight off the raw export timestamps (so UTC, not civil time, and Varden half an hour out), took the Kestrel mean-demand channels as energy, and gave every site 31 standing days at £4.32 including Brookhay and Marlpit. A trial sheet is not a source of record (audit finding 4). My run is £122,684.40 below it; most of that gap is the four Kestrel sites, which the sheet roughly doubled.
2. **Last month's run (BR-2610) and its consumption file.** Not used as input. For reference, BR-2610's figures for the four Kestrel sites look to have been built the same unhalved way, and the six Varden sites were taken "through the Varden ingest without exceptions" — you may want a separate look at whether BR-2610 needs restating, but that is outside this run and I have not touched those invoices.
3. **The Edition 6 customer price schedule** in the run folder — rates agree with the Edition 6 page, so no conflict, but I priced from the edition pages, which that schedule itself names as the edition of record.
4. **The Edition 7 price change notice (customer copy)** — used only as corroboration; rates taken from the Edition 7 page.
5. **`mdm-export-profiles.json`** — used as a column map only, as its own note says. It does not define what a channel means or which end of the period a timestamp marks; the collection agreements and commissioning records do, and they are what I followed.
6. **Customer correspondence** — the four emails in the run folder (Wendle Street, Marlpit, Brookhay, Orchard Rise) were read but not acted on and not replied to. Marlpit's and Brookhay's dates were superseded by the site accounts as above. Clara Orchard's peak-window question is for Saffron Deel.
7. **`meter-exchange-log-2026.csv` and `collector-assignment-history.csv`** — checked for in-period changes; none affect the 22 sites, and the old/new MSNs in the log do not correspond to the live meters in the asset register, so I billed on the register's meters.

Working papers (`/workspace/br2611_calc.py` and `br2611_results.json`) are left in the workspace if you or the auditors want to re-run or trace any figure. If any draft needs correcting after your review on Tuesday, tell me which and I will void mine and raise a replacement rather than edit it.