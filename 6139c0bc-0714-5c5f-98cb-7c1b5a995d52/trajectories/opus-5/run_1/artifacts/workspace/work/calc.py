"""FY2026 Scope 2 inventory — SCP-02 Rev 4, EFS-2025 rev 2025.2."""
import csv
from collections import defaultdict
from decimal import Decimal as D

DATA = "/workspace/data/"

# ---- Factors: EFS-2025 CSV (rev 2025.1) overlaid with Erratum 2 (-> rev 2025.2) ----
loc, res = {}, {}
with open(DATA + "emission-factor-set-EFS-2025.1.csv") as f:
    for r in csv.DictReader(f):
        if r["factor_type"] == "location":
            loc[r["region"]] = D(r["value"])
        elif r["factor_type"] == "residual_mix" and r["value"]:
            res[r["region"]] = D(r["value"])
STEAM_DEFAULT = D("66.33")  # kg CO2e/MMBtu, unchanged by Erratum 2

# Erratum 2 of 2026-02-17 (wiki child page of the EFS page)
loc["US-TX4"] = D("0.4127")
res["PL"] = D("0.8466")
res.pop("US-SE3")  # withdrawn: no residual mix published for US-SE3 in rev 2025.2

# Clause 7.3: no residual mix published for a region -> use that region's location factor
def residual(region):
    return res.get(region, loc[region])

# ---- Site register ----
sites = {}
order = []
with open(DATA + "site-register-fy2026.csv") as f:
    for r in csv.DictReader(f):
        sites[r["site_code"]] = r
        order.append(r["site_code"])

# ---- Electricity: Box invoice ledger of record (clause 4.1) ----
# Clause 4.5 / dictionary note 3: account BGS-PL-40917 is billed in MWh, all others kWh.
MWH_BILLED_ACCOUNTS = {"BGS-PL-40917"}

# Clause 4.3: an invoice month with read type E is replaced by metered consumption of the
# same period = difference of the main meter's month-end register reads bounding the period.
# Verified against the energy platform (month-end registers).
METERED_E = {
    ("TPC-06", "2025-12-01"): D(6689555) - D(6299685),    # 389,870 kWh
    ("TPC-08", "2026-04-01"): D(9785133) - D(9373796),    # 411,337 kWh
    ("TPC-10", "2026-01-01"): D(9552781) - D(9211531),    # 341,250 kWh
    ("TPC-10", "2026-02-01"): D(9857661) - D(9552781),    # 304,880 kWh
    ("TPC-17", "2026-06-01"): D(15521883) - D(15293353),  # 228,530 kWh
}

# Clause 4.4: reissued invoices filed in the Box invoice folder on 2026-11-11, before the strike.
# They replace the invoice they correct for the whole of its billing period.
REISSUED = {
    ("TPC-19", "2026-08-01"): (D(371200), "KEV-RE-26-0819"),  # replaces KEV-26-0819 (464,000), CT ratio
    ("TPC-18", "2026-09-01"): (D(650310), "KEV-RE-26-0918"),  # replaces KEV-26-0918 (588,810), off-peak register
}

elec_mwh = defaultdict(lambda: D(0))
elec_detail = defaultdict(list)
with open(DATA + "utility-invoice-ledger-export-2026-10-06.csv") as f:
    for r in csv.DictReader(f):
        if not (r["period_start"] >= "2025-10-01" and r["period_end"] <= "2026-09-30"):
            raise SystemExit("row outside FY2026: " + str(r))
        sc, key = r["site_code"], (r["site_code"], r["period_start"])
        if key in REISSUED:
            kwh, reissue_no = REISSUED[key]
            r["invoice_no"] = reissue_no
            src = "reissued invoice (cl.4.4)"
        elif r["read_type"] == "E":
            kwh = METERED_E[key]
            src = "metered (cl.4.3)"
        elif r["account_no"] in MWH_BILLED_ACCOUNTS:
            kwh = D(r["consumption_kwh"]) * 1000
            src = "invoice (MWh billed)"
        else:
            kwh = D(r["consumption_kwh"])
            src = "invoice"
        elec_mwh[sc] += kwh / 1000
        elec_detail[sc].append((r["period_start"], r["invoice_no"], r["read_type"], src, kwh))

# ---- Thermal carriers (clause 5) ----
# Enthalpy per clause 5.3 from the supplier's enthalpy note for the period.
ENTHALPY = {"TPC-01": D("1047.5"),   # RDE, closed-loop (condensate_return=Yes) -> net delivered
            "TPC-07": D("1190.0")}   # Old Port Thermal, open discharge -> total enthalpy
# Clause 5.4: supplier plant factor for the market-based figure only if third-party verified.
STEAM_MKT = {"TPC-01": D("58.20"),   # RDE 2025 factor, ISAE 3410 verified by Arden 2026-03-20
             "TPC-07": STEAM_DEFAULT}  # OPT 44.10 is preliminary/unverified -> EFS default
# Clause 5.5: measured annual COP from the supplier's annual statement, else Schedule B default 4.0
COP = {"TPC-12": D("5.2"),  # Capitol Campus measured annual COP (nameplate 6.1 not used)
       "TPC-14": D("4.0")}  # Legacy DC publishes no measured COP -> Schedule B default

steam_lb = defaultdict(lambda: D(0))
cw_tonh = defaultdict(lambda: D(0))
with open(DATA + "district-energy-statements-fy2026.csv") as f:
    for r in csv.DictReader(f):
        if not (r["period_start"] >= "2025-10-01" and r["period_end"] <= "2026-09-30"):
            continue
        if r["carrier"] == "steam":
            steam_lb[r["site_code"]] += D(r["quantity"])
        else:
            cw_tonh[r["site_code"]] += D(r["quantity"])

steam_mmbtu, cw_mwh = {}, {}
for sc in order:
    steam_mmbtu[sc] = (steam_lb[sc] * ENTHALPY[sc] / D(1000000)) if steam_lb[sc] else D(0)
    if cw_tonh[sc]:
        kwh = cw_tonh[sc] * D(12000) / D("3412.14") / COP[sc]
        cw_mwh[sc] = kwh / 1000
    else:
        cw_mwh[sc] = D(0)

# ---- Contractual instruments (clause 6), status from the Airtable registry mirror ----
# site -> list of (certificate id, MWh on the certificate)
# Re-read at the strike: NRR-2026-0091-SOL is now Retired (TPC-06 qualifies);
# NRR-2026-0233-SOL is now "Retirement reversed" and fails 6.4 (TPC-08 drops to residual mix).
QUALIFYING = {
    "TPC-04": [("NRR-2025-1187-WND", D(9000))],
    "TPC-05": [("NRR-2025-1302-WND", D(3000))],
    "TPC-06": [("NRR-2026-0091-SOL", D(5000))],
    "TPC-16": [("AIB-NL-2025-40388", D(4200))],
    "TPC-18": [("AIB-DE-2026-11873", D(6500))],
    "TPC-21": [("REGO-R0091-2026-0442", D(5000))],
}

rows = []
tot_loc = tot_mkt = D(0)
for sc in order:
    reg = sites[sc]["efs_region"]
    lf, rf = loc[reg], residual(reg)
    e, cw, st = elec_mwh[sc], cw_mwh[sc], steam_mmbtu[sc]

    # clause 7.1
    lb = (e + cw) * lf + st * STEAM_DEFAULT / D(1000)
    # clause 6.9: an instrument covers only its site, up to that site's purchased electricity
    certs = QUALIFYING.get(sc, [])
    covered = min(e, sum(v for _, v in certs)) if certs else D(0)
    # clause 7.2
    mb = (e - covered) * rf + cw * rf + st * STEAM_MKT.get(sc, STEAM_DEFAULT) / D(1000)

    lb_r, mb_r = round(lb, 1), round(mb, 1)
    tot_loc += lb_r
    tot_mkt += mb_r
    instr = "; ".join(sorted(c for c, _ in certs)) if certs else "Residual mix"
    rows.append(dict(site=sc, name=sites[sc]["site_name"], region=reg, loc_f=lf, res_f=rf,
                     elec=e, cw=cw, steam=st, covered=covered,
                     lb=lb_r, mb=mb_r, instr=instr))

hdr = f"{'site':7} {'name':11} {'reg':7} {'elecMWh':>10} {'cwMWh':>9} {'steamMMBtu':>11} {'covMWh':>8} {'LOC':>10} {'MKT':>10}  instrument"
print(hdr)
for r in rows:
    print(f"{r['site']:7} {r['name']:11} {r['region']:7} {r['elec']:10.1f} {r['cw']:9.1f} "
          f"{r['steam']:11.1f} {r['covered']:8.0f} {r['lb']:10.1f} {r['mb']:10.1f}  {r['instr']}")
print(f"\nLocation-based total: {tot_loc} tCO2e")
print(f"Market-based total:   {tot_mkt} tCO2e")

with open("/workspace/work/results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["site_code", "site", "efs_region", "electricity_mwh", "chilled_water_mwh_eq",
                "steam_mmbtu", "instrument_mwh_applied", "location_tco2e", "market_tco2e",
                "instrument_applied", "location_factor", "residual_factor"])
    for r in rows:
        w.writerow([r["site"], r["name"], r["region"], f"{r['elec']:.1f}", f"{r['cw']:.1f}",
                    f"{r['steam']:.1f}", f"{r['covered']:.0f}", f"{r['lb']:.1f}", f"{r['mb']:.1f}",
                    r["instr"], r["loc_f"], r["res_f"]])

# electricity audit trail
with open("/workspace/work/electricity_detail.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["site_code", "period_start", "invoice_no", "read_type", "source", "kwh_used"])
    for sc in order:
        for d in elec_detail[sc]:
            w.writerow([sc, *d])
