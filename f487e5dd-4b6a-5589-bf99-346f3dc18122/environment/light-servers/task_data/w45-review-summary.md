# W45 design review — summary (closed Friday 6 November 2026)
Reviewed against DS-6 Edition 4. 16 designs.

| Verdict | Count |
|---|---|
| Approved | 11 |
| Redesign – overvoltage | 3 |
| Redesign – below MPPT | 1 |
| Redesign – overcurrent | 1 |

Worked notes kept for the record:
- 7301962 (Kestrel KP-470 × 12, Volta 8K, Gwennap Moor GWN, T_min −17.9 °C): coefficient −138 mV/°C per clause 4.2, per-module Voc at T_min = 50.90 + (−138/1000)(−42.9) = 56.82 V; 12 × 56.82 = 681.8 V > 600 V. Recommended 10 (568.2 V).
- 7301975 (Corvane CV-440B × 13, Volta 5K, Lostock Bridge LSK, T_min −11.7 °C): 13 × 39.80 × (1 + 0.0025 × 36.7) = 564.9 V, passes clause 4; approved.
- 7301993 (Halcyon HX-405M × 11, two strings per tracker on a BL-10): 2 × 13.80 × 1.25 = 34.5 A > 30 A → overcurrent; string length unchanged at 11 because clauses 4 and 5 pass at 11.
- 7301981 (Brava BR-390 × 7 on a Volta 8K HV): Vmp,min = 7 × 29.80 × (1 − 0.0030 × 45) = 180.4 V < 250 V → below MPPT; nearest passing length 10.
