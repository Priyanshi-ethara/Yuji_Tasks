# Brightline Cold Freight - Schedule 2 (data services)

Revision 2, effective 1 January 2026.

2.1 Brightline BL-200 loggers record in degC at a 15-minute interval. Exports are downloaded by Tarnwick from the
Brightline portal (columns logger_id, reading_time_utc, value, status).
2.2 The status column carries the logger's own self-check result (OK, FAULT). A FAULT flag means the logger's self-test
raised a warning (probe contact, battery, clock); it is not a measurement verdict. Loggers that raised a FAULT flag are
returned to Tarnwick Metrology for an as-found check.
2.3 Proof of delivery is the driver's handset event when the trailer docks; it is not the consignee's receipt.
