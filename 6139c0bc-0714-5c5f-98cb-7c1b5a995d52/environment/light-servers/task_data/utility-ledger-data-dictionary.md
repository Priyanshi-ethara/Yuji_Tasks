# Utility invoice ledger — data dictionary (Facilities shared services)

Owner: Facilities Shared Services, Accounts Payable interface team. Version 7, 2026-04-02.
Applies to: the FY2026 electricity invoice ledger filed in Box ("Facilities — Utility invoices FY2026") and every CSV
export taken from it (the monthly exports the sustainability desk keeps are working copies of the same table).

| # | Field | Type | Meaning |
|---|-------|------|---------|
| 1 | site_code | text | Talvik site code, TPC-01 … TPC-22 (site register) |
| 2 | account_no | text | Supplier account number as printed on the invoice |
| 3 | supplier | text | Supplier trading name |
| 4 | invoice_no | text | Supplier invoice number; a reissued invoice carries the prefix of the supplier followed by RE |
| 5 | period_start / period_end | date | Billing period, inclusive, ISO 8601 |
| 6 | read_type | code | A = actual meter read by the supplier; E = estimated by the supplier; C = customer read (not used in FY2026) |
| 7 | consumption_kwh | number | Billed active energy for the period, as billed (see note 3) |
| 8 | amount | number | Invoice total excluding VAT/sales tax, in `currency` |
| 9 | currency | ISO 4217 | Invoice currency |
| 10 | posted_on | date | Date AP posted the invoice to the ledger |

Notes

1. One row per supplier invoice. Credit notes are not carried in this ledger; a supplier correction arrives as a
   reissued invoice and is filed next to the ledger in the same Box folder, never as an edit of the original row.
2. Amounts are not converted to USD. Do not use `amount` for any consumption estimate.
3. Unit of `consumption_kwh`: the loader copies the billed quantity unchanged. Every account is billed in kWh
   except account BGS-PL-40917 (Baltic Grid Supply, Gdańsk), whose supplier bills in MWh to one decimal place; for
   that account the column holds MWh as billed. The column was not renamed because the AP interface schema is shared
   with 41 other entities (change request FSS-CR-2291 declined 2025-11-14).
4. Odra Energia (account OEN-PL-11930, Wrocław) moved to kWh billing in 2024; its rows are kWh like every other account.
5. Estimated invoices (`read_type` = E) are trued up by the supplier on a later actual read for some suppliers only;
   in FY2026 none of the five E invoices was trued up in the ledger.
6. `posted_on` is the AP posting date, not the supplier's issue date.
