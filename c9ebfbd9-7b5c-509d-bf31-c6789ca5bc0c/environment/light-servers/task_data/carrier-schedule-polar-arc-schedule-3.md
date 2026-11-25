# Polar Arc Logistics - Schedule 3 to the cold-chain services agreement (Tarnwick Biologics)

Revision 5, effective 1 September 2026.

3.1 Data delivery. Polar Arc delivers logger data through the shared carrier drop folder "Polar Arc - Tarnwick drop", one
sub-folder per release round and per logger. Each logger folder holds the CSV segments and the logger's metadata file
(<logger>_meta.json). The metadata file is the statement of the export's unit and logging interval.
3.2 Segments. A logger's data may arrive in segments. A segment that fails to upload is recovered from the logger flash and
delivered to the same folder within 5 working days; Polar Arc notifies the QA release mailbox when it does.
3.3 Format. CSV columns timestamp_utc, reading, record_flag. Timestamps are UTC. From firmware 4.2.1 (fleet roll-out
20 October 2026) the TK9 Pro exports in the unit configured on the device, and Polar Arc configures the fleet in degF to
match its US customers; the metadata file says so. Logging interval 10 minutes.
3.4 Boundary records. When a segment is cut, up to three records at the boundary can be transmitted in both segments.
3.5 Polar Arc does not judge product quality and its staff are not authorised to advise on release.
