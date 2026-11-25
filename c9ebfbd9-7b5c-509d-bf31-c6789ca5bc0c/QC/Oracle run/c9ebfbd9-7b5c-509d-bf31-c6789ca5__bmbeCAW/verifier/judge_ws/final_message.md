Round R-2026-45 is closed. R-2026-45 closed: 7 Release, 6 Release with deviation, 1 Quarantine, 1 Reject, 3 Referred to QA Head.

SOP in force: QA-SOP-114 Revision 7 from the Quality Assurance wiki space, in force since 15 October 2026. The Revision 6 desk copy in the data pack (custody to proof of delivery, logger flags excluding readings, 90 % referral, freezing only below 0.0 C) was set aside as withdrawn.

Per lot (outcome, MKT, lane TOR, cumulative TOR, budget used, deviation key):
- CVM-260412 (TB-201, HX4-41188): Release with deviation; MKT 5.48 C; lane TOR 2.25 h; cumulative TOR 12.75 h of 72 h; budget used 17.71 %; deviation QAD-406.
- PLM-260377 (TB-118, HX4-41188): Release with deviation; MKT 5.49 C; lane TOR 2.25 h; cumulative TOR 24.25 h of 120 h; budget used 20.21 %; deviation QAD-407.
- FRT-260221 (TB-305, HX4-41190): Release; MKT 4.67 C; lane TOR 0.00 h; cumulative TOR 8.00 h of 48 h; budget used 16.67 %; deviation none.
- OSV-260090 (TB-440, HX4-41190): Release; MKT 4.67 C; lane TOR 0.00 h; cumulative TOR 18.00 h of 36 h; budget used 50.00 %; deviation none.
- PLM-260381 (TB-118, HX4-41195): Quarantine; MKT 8.14 C; lane TOR 9.00 h; cumulative TOR 50.00 h of 120 h; budget used 41.67 %; deviation QAD-408.
- CVM-260415 (TB-201, HX4-41199): Release; MKT 5.02 C; lane TOR 0.00 h; cumulative TOR 3.00 h of 72 h; budget used 4.17 %; deviation none.
- FRT-260224 (TB-305, HX4-41199): Release; MKT 5.01 C; lane TOR 0.00 h; cumulative TOR 20.00 h of 48 h; budget used 41.67 %; deviation none.
- OSV-260094 (TB-440, HX4-41203): Referred to QA Head; MKT 5.54 C; lane TOR 1.00 h; cumulative TOR 27.25 h of 36 h; budget used 75.69 %; deviation QAD-409.
- CVM-260419 (TB-201, HX4-41203): Release with deviation; MKT 5.55 C; lane TOR 1.00 h; cumulative TOR 6.00 h of 72 h; budget used 8.33 %; deviation QAD-410.
- CVM-260417 (TB-201, HX4-41207): Release with deviation; MKT 5.43 C; lane TOR 1.33 h; cumulative TOR 15.33 h of 72 h; budget used 21.30 %; deviation QAD-411.
- FRT-260230 (TB-305, HX4-41207): Release with deviation; MKT 5.41 C; lane TOR 1.33 h; cumulative TOR 35.83 h of 48 h; budget used 74.65 %; deviation QAD-412.
- OSV-260097 (TB-440, HX4-41207): Referred to QA Head; MKT 5.42 C; lane TOR 1.33 h; cumulative TOR 35.83 h of 36 h; budget used 99.54 %; deviation QAD-413.
- PLM-260385 (TB-118, HX4-41211): Release with deviation; MKT 4.42 C; lane TOR 0.67 h; cumulative TOR 60.67 h of 120 h; budget used 50.56 %; deviation QAD-414.
- CVM-260421 (TB-201, HX4-41211): Referred to QA Head; MKT 4.42 C; lane TOR 0.67 h; cumulative TOR 71.67 h of 72 h; budget used 99.54 %; deviation QAD-415.
- FRT-260233 (TB-305, HX4-41215): Release; MKT 5.03 C; lane TOR 0.00 h; cumulative TOR 30.00 h of 48 h; budget used 62.50 %; deviation none.
- PLM-260389 (TB-118, HX4-41215): Release; MKT 5.04 C; lane TOR 0.00 h; cumulative TOR 12.00 h of 120 h; budget used 10.00 %; deviation none.
- CVM-260425 (TB-201, HX4-41219): Release; MKT 4.91 C; lane TOR 0.00 h; cumulative TOR 0.00 h of 72 h; budget used 0.00 %; deviation none.
- OSV-260101 (TB-440, HX4-41223): Reject; MKT 4.06 C; lane TOR 1.25 h; cumulative TOR 7.25 h of 36 h; budget used 20.14 %; deviation QAD-416.

Records that moved under me during the round:
- Late logger segment: when I first read the Polar Arc drop, logger TK9-5521 on HX4-41207 was missing segment 2 (5 Nov 02:00-07:50 UTC), a data gap, so its three lots first came out as Quarantine. Before closing I checked the drop again as SOP 3.3 requires: Polar Arc had uploaded TK9-5521_HX4-41207_seg2.csv, recovered from the logger flash. With it the gap is gone, and the segment contains an excursion above 8 degC (12 readings at 10-minute intervals between 8.4 and 10.4 C, 2.00 h before any exclusion). I re-evaluated the three lots CVM-260417, FRT-260230 and OSV-260097 with it rather than leaving them in Quarantine for a data gap.
- Reissued calibration certificate: after the cards were written I downloaded Metrology's certificates again. Metrology has reissued the calibration certificate of logger TK9-5521 (TML-CC-2026-1196 issue 2, 10 Nov 2026, superseding issue 1 of 8 Nov) because the recovered segment came with the logger's diagnostic trace; the reissued certificate records a sensor-fault window on 5 November 2026 from 03:20 to 03:50 UTC, confirmed by Priya Venkataraman's mail to the QA release mailbox. Under SOP 4.2 the recovered-segment readings inside that window (4 readings at 10-minute intervals, 0.67 h of time out of range) were excluded from the MKT and time out of range of the HX4-41207 lots, which leaves 1.33 h of lane TOR for them.
- What the reissued certificate shifted: counting the recovered segment in full would make FRT-260230 Referred to QA Head and OSV-260097 Reject; with the fault window excluded FRT-260230 is Release with deviation and OSV-260097 is Referred to QA Head. CVM-260417 stays Release with deviation with lower figures.
- Deviations: when the HX4-41207 lots' outcomes changed, I corrected their existing deviations (QAD-411, QAD-412, QAD-413: summary and priority) rather than raising new deviations, and then rewrote their cards.

Reasons for every lot that is not a plain Release:
- FRT-260230 is Release with deviation, not referred to the QA Head: its budget used is 74.65 % (35.83 of 48 h), which is not above the 75 % referral threshold; lane TOR 1.33 h.
- OSV-260097 is Referred to QA Head, not rejected: its cumulative time out of range of 35.83 h does not exceed its 36 h budget, but its budget used of 99.54 % is above the 75 % referral threshold.
- CVM-260417 is Release with deviation: lane TOR 1.33 h; its budget used is 21.30 % (15.33 of 72 h).
- OSV-260094 is referred at 75.69 % of budget (27.25 of 36 h), above the 75 % threshold. Its prior time out of range was taken from the live ERP stability budget ledger, which holds an entry posted on 1 November 2026 that the 31 October ledger export in the data pack lacks; I did not follow the export.
- BL-3320 (HX4-41203): the logger flagged itself from 22:30 to 23:15 UTC on 4 Nov, but its calibration certificate records no sensor-fault window (low-battery self-test), so those four readings (8.4-9.1 C, 1.00 h) were kept; that is why OSV-260094 and CVM-260419 carry lane TOR. The BL-3230 certificate, which does record a fault at the same times, belongs to a different logger on lane LX-2.
- CVM-260419 is Release with deviation on the 1.00 h of kept BL-3320 readings.
- CVM-260421 (HX4-41211, TK9-5530): the records repeated at the boundary of the TK9-5530 segments (22:00, 22:10, 22:20 UTC on 5 Nov) were counted once under SOP 4.3. Its budget used is 99.54 % (71.67 of 72 h), above the 75 % threshold, so it is referred to the QA Head.
- PLM-260385 is Release with deviation on the same shipment (0.67 h lane TOR from the low excursion).
- PLM-260381 (HX4-41195) is quarantined because its MKT of 8.14 C, computed with Pellumab's own activation energy of 112.0 kJ/mol from the specification in force (Edition F), is above the 8.0 degC MKT limit.
- Custody ends at the NDC receipt scan, not the carrier's proof of delivery: HX4-41188 waited on the dock from 06:40 UTC (proof of delivery) to the 08:55 UTC receipt scan on 3 Nov, and those dock readings (up to 9.6 C, 2.25 h) count towards time out of range, so CVM-260412 and PLM-260377 are Release with deviation.
- OSV-260101 (HX4-41223) is rejected for freezing: its logger BL-3329 recorded a reading of exactly 0.0 degC on 6 Nov at 19:45 UTC, and the SOP in force rejects any reading at or below 0.0 degC.

Readings excluded and readings kept:
- Excluded: the readings inside the reissued TK9-5521 certificate's sensor-fault window (above); the readings of logger BL-3315 between 01:00 and 01:30 UTC on 4 November, because its calibration certificate records that period as a sensor-fault window (three readings, 11.8-13.9 C), so CVM-260415 and FRT-260224 are Release; the HX4-41190 readings taken before its handover scan (the packing hall, 12.1-16.8 C, before 04:00 UTC); the HX4-41219 readings during the Cold Room 2 alarm of 7 November, because they were taken after the shipment's receipt scan (20:05 UTC on 6 Nov); the repeated TK9-5530 boundary records.
- Kept: the BL-3320 self-flagged readings (no certified fault window), and every other flagged or suspicious reading inside custody.
- FRT-260233: the 9.0 h ledger entry marked Voided (BL-3188 probe fault) is not counted; posted entries give 30.00 of 48 h.
- Polar Arc TK9 readings are in degrees Fahrenheit according to the logger metadata files (firmware 4.2.1, 10-minute interval), and I converted them to degrees Celsius before every calculation; the September fleet register still shows degC/15 min for that fleet and was not used for it.

Waiting for the QA Head's sign-off: OSV-260094, OSV-260097, CVM-260421 (FRT-260230 is not among them). I gave them no disposition.
Deviation keys: CVM-260412 QAD-406, PLM-260377 QAD-407, PLM-260381 QAD-408, OSV-260094 QAD-409, CVM-260419 QAD-410, CVM-260417 QAD-411, FRT-260230 QAD-412, OSV-260097 QAD-413, PLM-260385 QAD-414, CVM-260421 QAD-415, OSV-260101 QAD-416.

Records I chose not to follow: Jonas Brandt's first-pass worksheet (default activation energy, proof of delivery as custody end, logger flags dropped); the Corvalimab (TB-201) Edition C specification copy, set aside as superseded by Edition D in the specifications database; the 31 October ledger export; the July specification register; the September fleet register for the TK9 fleet; issue 1 of the TK9-5521 certificate, superseded by issue 2; and the Revision 6 desk copy. Polar Arc's suggestion to release on the reefer controller log was not used.

I left the ERP lot status unchanged for every lot (QA Head's act after sign-off), did not contact Halden Regional Hospital Pharmacy, and saved r2026-45-outcomes.csv in the workspace.