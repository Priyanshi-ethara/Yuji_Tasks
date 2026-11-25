"""BR-2611 BHH billing run — computed per BP-4 v7 and the records it names."""
import csv
import datetime as dt
import json
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from zoneinfo import ZoneInfo

DATA = "/workspace/data"
UK = ZoneInfo("Europe/London")
UTC = dt.timezone.utc

PERIOD_START = dt.date(2026, 10, 15)
PERIOD_END = dt.date(2026, 11, 14)

# Edition pages (BILL space): Ed6 covers consumption 1 Apr - 31 Oct 2026, Ed7 from 1 Nov 2026.
ED6_LAST = dt.date(2026, 10, 31)

RATES = {
    6: dict(standing=Decimal("3.95"), peak=Decimal("34.812"), day=Decimal("24.375"),
            night=Decimal("16.940"), capacity=Decimal("4.800"), reactive=Decimal("2.415")),
    7: dict(standing=Decimal("4.32"), peak=Decimal("37.905"), day=Decimal("25.610"),
            night=Decimal("16.940"), capacity=Decimal("5.350"), reactive=Decimal("2.780")),
}

# CRM site accounts (Salesforce): supply dates + ledger customer.
SITES = [
    # site_ref, site_name, qb_customer_id, ledger_customer, supply_start, supply_end
    ("HMS-1047", "Calloway Mill Bakery", "7101", "Calloway Mill Bakery Ltd", None, None),
    ("HMS-1052", "Ostrey Lane Medical Centre", "7102", "Ostrey Lane Medical Centre Ltd", None, None),
    ("HMS-1068", "Pellingford Community School", "7103", "Pellingford Community School (Trust)", None, None),
    ("HMS-1073", "Quenby Print Works", "7104", "Quenby Print Works Ltd", None, None),
    ("HMS-1081", "Saltash Row Garage", "7105", "Saltash Row Garage Ltd", None, None),
    ("HMS-1094", "Thornaby Wharf Cold Store", "7106", "Thornaby Wharf Cold Store Ltd", None, None),
    ("HMS-1102", "Harrowmere Leisure Pool", "7107", "Harrowmere Leisure Pool (Council Trust)", None, None),
    ("HMS-1115", "Wendle Street Offices", "7108", "Wendle Street Offices Ltd", None, dt.date(2026, 12, 31)),
    ("HMS-1123", "Marlpit Garden Centre", "7109", "Marlpit Garden Centre Ltd", None, dt.date(2026, 11, 5)),
    ("HMS-1139", "Brookhay Brewery Taproom", "7110", "Brookhay Brewery Taproom Ltd", dt.date(2026, 10, 22), None),
    ("HMS-1146", "Ashgrove Plastics Moulding", "7111", "Ashgrove Plastics Moulding Ltd", None, None),
    ("HMS-1158", "Fenwick Lane Data Hall", "7112", "Fenwick Lane Data Hall Ltd", None, None),
    ("HMS-1160", "Gorsebrook Laundry Services", "7113", "Gorsebrook Laundry Services Ltd", None, None),
    ("HMS-1177", "Hollin Bridge Sawmill", "7114", "Hollin Bridge Sawmill Ltd", None, None),
    ("HMS-1183", "Kittering Foods Packing", "7115", "Kittering Foods Packing Ltd", None, None),
    ("HMS-1191", "Wexcombe Craft Studios", "7116", "Wexcombe Craft Studios Ltd", None, None),
    ("HMS-1204", "Lanyon Quay Fish Market", "7117", "Lanyon Quay Fish Market Ltd", None, None),
    ("HMS-1212", "Merrowby Care Home", "7118", "Merrowby Care Home Ltd", None, None),
    ("HMS-1229", "Netherfold Veterinary Hospital", "7119", "Netherfold Veterinary Hospital Ltd", None, None),
    ("HMS-1235", "Orchard Rise Hotel", "7120", "Orchard Rise Hotel Ltd", None, None),
    ("HMS-1248", "Penhallow Tool Hire", "7121", "Penhallow Tool Hire Ltd", None, None),
    ("HMS-1256", "Ravensworth Bowls Club", "7122", "Ravensworth Bowls & Social Club", None, None),
]

SUPPLY_NO_TO_SITE = {
    "HM1944707830": "HMS-1146", "HM1945077883": "HMS-1158", "HM1945447936": "HMS-1160",
    "HM1945817989": "HMS-1177", "HM1946188042": "HMS-1183", "HM1946558095": "HMS-1191",
    "HM1946928148": "HMS-1204", "HM1947298201": "HMS-1212", "HM1947668254": "HMS-1229",
    "HM1948038307": "HMS-1235", "HM1948408360": "HMS-1248", "HM1948778413": "HMS-1256",
}

# Metering asset register (Notion) — commissioning records.
# Kestrel wave-2 meters programmed to register MEAN DEMAND (kW/kvar) per half-hour, not energy:
# energy in a period = mean demand x 0.5 h.  MOPS-1184.
MEAN_DEMAND_METERS = {"K24C10417", "K24C10452", "K24C10488", "K24C10519"}
# K24C10503 (Hollin Bridge) and K24C10541 (Wexcombe) kept energy programming.


def read_half_hours():
    """Return {site_ref: {period_start_utc: (kwh, kvarh)}} at full precision."""
    out = defaultdict(dict)

    for fn in ("amr-hh-export-br2611-batch-a.csv", "amr-hh-export-br2611-batch-b.csv"):
        with open(f"{DATA}/{fn}") as fh:
            for r in csv.DictReader(fh):
                ts = dt.datetime.strptime(r["period_start_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)
                site = r["site_ref"]
                assert ts not in out[site], (site, ts)
                out[site][ts] = (Decimal(r["kwh"]), Decimal(r["kvarh"]))

    with open(f"{DATA}/kestrel-hh-delivery-HRM-2611.csv") as fh:
        for r in csv.DictReader(fh):
            # Schedule 2: ts_utc is the period START, channels passed through as registered.
            ts = dt.datetime.strptime(r["ts_utc"], "%Y-%m-%d %H:%M").replace(tzinfo=UTC)
            site = SUPPLY_NO_TO_SITE[r["mpan"]]
            a, rr = Decimal(r["a_plus"]), Decimal(r["r_plus"])
            if r["msn"] in MEAN_DEMAND_METERS:
                a, rr = a / 2, rr / 2
            assert ts not in out[site], (site, ts)
            out[site][ts] = (a, rr)

    with open(f"{DATA}/varden-sched3-HRM-20261115.csv") as fh:
        for r in csv.DictReader(fh):
            # Schedule 3: READ_TS_UTC is the period END; shift back 30 min to get the start.
            end = dt.datetime.strptime(r["READ_TS_UTC"], "%Y%m%d%H%M").replace(tzinfo=UTC)
            ts = end - dt.timedelta(minutes=30)
            site = SUPPLY_NO_TO_SITE[r["MPAN"]]
            assert ts not in out[site], (site, ts)
            out[site][ts] = (Decimal(r["AI"]), Decimal(r["RI"]))

    return out


def band_of(local):
    """BP-4 4.1 / Time-of-use bands page: band of the half-hour in which it begins, UK civil time."""
    t = local.hour * 60 + local.minute
    if t < 7 * 60:
        return "night"
    if local.weekday() < 5 and 16 * 60 <= t < 19 * 60:
        return "peak"
    return "day"


def q(x, places):
    return x.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def main():
    hh = read_half_hours()
    results = []

    for site_ref, name, cust_id, ledger, sup_start, sup_end in SITES:
        first = max(sup_start, PERIOD_START) if sup_start else PERIOD_START
        last = min(sup_end, PERIOD_END) if sup_end else PERIOD_END

        # per edition: band energies, max demand, excess reactive, set of civil days seen
        agg = {6: dict(energy=defaultdict(Decimal), md=Decimal(0), rx=Decimal(0), days=set(), n=0),
               7: dict(energy=defaultdict(Decimal), md=Decimal(0), rx=Decimal(0), days=set(), n=0)}

        for ts, (kwh, kvarh) in hh[site_ref].items():
            local = ts.astimezone(UK)
            cday = local.date()
            if cday < first or cday > last:
                continue  # outside the run period or off supply (BP-4 5.1, export margin)
            ed = 6 if cday <= ED6_LAST else 7
            a = agg[ed]
            a["energy"][band_of(local)] += kwh
            a["days"].add(cday)
            a["n"] += 1
            demand = kwh * 2
            if demand > a["md"]:
                a["md"] = demand
            excess = kvarh - Decimal("0.33") * kwh
            if excess > 0:
                a["rx"] += excess

        lines = []
        detail = {}
        for ed in (6, 7):
            a = agg[ed]
            if not a["days"]:
                continue
            rate = RATES[ed]
            days = len(a["days"])
            md = q(a["md"], "0.01")
            qty = {b: q(a["energy"][b], "0.001") for b in ("peak", "day", "night")}
            rx = q(a["rx"], "0.001")

            charges = [
                ("Standing charge", Decimal(days), rate["standing"], Decimal(days) * rate["standing"]),
                ("Peak unit charge", qty["peak"], rate["peak"], qty["peak"] * rate["peak"] / 100),
                ("Day unit charge", qty["day"], rate["day"], qty["day"] * rate["day"] / 100),
                ("Night unit charge", qty["night"], rate["night"], qty["night"] * rate["night"] / 100),
                ("Capacity charge", md * days, rate["capacity"], md * days * rate["capacity"] / 100),
                ("Excess reactive charge", rx, rate["reactive"], rx * rate["reactive"] / 100),
            ]
            for cname, cqty, crate, amount in charges:
                amt = q(amount, "0.01")
                if amt == 0:
                    continue
                lines.append(dict(desc=f"{cname} (Edition {ed})", amount=float(amt),
                                  qty=float(cqty), unit=float(crate)))
            detail[ed] = dict(days=days, md=str(md), periods=a["n"],
                              peak=str(qty["peak"]), day=str(qty["day"]), night=str(qty["night"]),
                              rx=str(rx),
                              kwh=str(q(qty["peak"] + qty["day"] + qty["night"], "0.001")))

        net = sum(Decimal(str(l["amount"])) for l in lines)
        results.append(dict(site_ref=site_ref, name=name, cust_id=cust_id, ledger=ledger,
                            first=str(first), last=str(last),
                            lines=lines, net=str(q(net, "0.01")), detail=detail))

    with open("/workspace/br2611_results.json", "w") as fh:
        json.dump(results, fh, indent=1)

    total = Decimal(0)
    tot_kwh = {6: Decimal(0), 7: Decimal(0)}
    for r in results:
        total += Decimal(r["net"])
        print(f"{r['site_ref']} {r['name'][:30]:<30} supply {r['first']}..{r['last']} net {r['net']:>12}")
        for ed, d in r["detail"].items():
            tot_kwh[ed] += Decimal(d["kwh"])
            print(f"    Ed{ed}: periods={d['periods']:4d} days={d['days']:2d} md={d['md']:>8} "
                  f"peak={d['peak']:>11} day={d['day']:>11} night={d['night']:>11} "
                  f"kWh={d['kwh']:>11} rx={d['rx']:>10}")
        for l in r["lines"]:
            print(f"      {l['desc']:<34} {l['amount']:>10.2f}  (qty {l['qty']}, rate {l['unit']})")
    print(f"\nDRAFTS: {len(results)}   NET TOTAL: {q(total,'0.01')}")
    print(f"Ed6 kWh {q(tot_kwh[6],'0.001')}  Ed7 kWh {q(tot_kwh[7],'0.001')}  "
          f"all {q(tot_kwh[6]+tot_kwh[7],'0.001')}")


main()
