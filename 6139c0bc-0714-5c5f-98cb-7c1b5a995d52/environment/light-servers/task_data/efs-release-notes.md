# Talvik Emission Factor Set (EFS) — release notes

Maintained by Group Sustainability Reporting (data steward: Priya Venkataraman).

## EFS-2026, revision 2026.1 — published 2026-08-14
- Grid location factors rebased on 2025 generation data for all US subregions and EU/UK countries.
- Residual mix for US-SE3 published for the first time (tracking-system coverage now sufficient).
- District steam default revised to 67.90 kg CO2e/MMBtu (updated boiler-efficiency assumption).
- Distributed as `emission-factor-set-EFS-2026.1.csv`. Which inventory year an edition serves is decided by the
  Scope 2 protocol's Schedule A, not by these notes.

## EFS-2025, revision 2025.1 — published 2025-08-29
- Grid location factors on 2024 generation data.
- Residual mix tables for US subregions from the NRR tracking system, EU countries from the AIB release, GB from the
  Ofgem fuel-mix disclosure.
- Distributed as `emission-factor-set-EFS-2025.1.csv`.

## Errata policy (since 2024)
Corrections to a published edition are issued as numbered errata. Each erratum raises the revision number of the
edition (2025.1 → 2025.2 …) and is published as a page in the Group Sustainability wiki space under the edition's
page. The distributed CSV of an edition is NOT regenerated for errata: an analyst working from the CSV must apply the
erratum rows on top of it. Erratum 1 to EFS-2025 (2025-10-03) was editorial only (unit label on the hot-water row).
