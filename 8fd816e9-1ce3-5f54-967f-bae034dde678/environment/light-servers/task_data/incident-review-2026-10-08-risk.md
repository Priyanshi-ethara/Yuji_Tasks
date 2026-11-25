# Post-incident review — KYC and dispute evidence uploads failing, 8 October 2026

Author: Ruth Okonjo · Reviewed: 13 Oct 2026 · Severity: SEV-2 · PagerDuty: PBW1103

## Summary
A storage-class change on the document bucket (applied by Terraform at 06:40 UTC) made new objects unreadable for the
kyc-document-check and dispute-evidence services on the production cells for about 35 minutes; dispute-evidence also
had two later windows of failed evidence bundling while its queue drained.

## Timeline (UTC)
- 06:40 bucket policy change applied (platform change PLAT-CHG-5521).
- 06:44 kyc-document-check 5xx above 1% on kestrel-1, -2, -3.
- 07:18 change reverted; kyc recovers.
- 07:20–09:05 dispute-evidence bundling retries fail intermittently.

## Actions
1. Policy test for bucket storage-class changes (PLAT-611).
2. dispute-evidence retry budget (RSK-151).
