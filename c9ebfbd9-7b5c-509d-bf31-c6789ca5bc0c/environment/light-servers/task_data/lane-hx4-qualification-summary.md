# Lane HX-4 qualification summary (Corran Mill fill-finish -> Northern Distribution Centre)

Document LQ-HX4-2026, Logistics Quality. Re-qualified 18 August 2026.

## Lane profile
- Distance 612 km, planned transit 26-34 h, one driver change at the Ostby cross-dock (no unloading).
- Carriers: Brightline Cold Freight (active reefer trailers, BL-200 loggers, 15-minute interval, degC) and
  Polar Arc Logistics (passive-plus-reefer, TK9 Pro loggers). Polar Arc moved its TK9 fleet to firmware 4.2.1 on
  20 October 2026; see the carrier's schedule and the firmware notes for what changed in the exports.
- Every shipment carries one logger, started at packing at Corran Mill and stopped by NDC receiving after the receipt scan.
  Loggers therefore record the packing hall before handover and the NDC dock/cold room after receipt.

## Summer/winter profiles (operational qualification, 2026)
| Season | Runs | Mean MKT (degC) | Max reading (degC) | Runs with any reading > 8 degC |
|---|---|---|---|---|
| Winter 2025/26 | 14 | 4.88 | 8.6 | 2 |
| Spring 2026 | 12 | 5.21 | 9.9 | 3 |
| Summer 2026 | 16 | 5.94 | 12.4 | 6 |
| Autumn 2026 (to date) | 9 | 5.36 | 10.8 | 3 |

## Known lane risks
1. Dock dwell at the NDC gate when the receipt scanner is down; pallets stay on the dock until scanned.
2. Polar Arc gateway restarts can delay a segment upload; the logger keeps the data in flash.
3. Ostby cross-dock in winter: short low excursions near the trailer doors.

The lane qualification does not set lot outcomes; QA-SOP-114 does.
