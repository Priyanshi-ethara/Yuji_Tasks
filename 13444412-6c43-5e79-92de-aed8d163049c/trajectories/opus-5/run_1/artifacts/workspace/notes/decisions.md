# Queue decisions — 2026-11-16 (today). Anchor = Stripe current_period_end.
# Price rule (BD-STD-2 s6): price-book price for the period the change STARTS in.
#   effective < 2027-01-01 -> pre-2027 card; effective >= 2027-01-01 -> 2027 card.

T     Account                     cus_/sub_              Disposition                     NewPlan        Seats Eff         Unit
5201  Ashgrove Atelier            ashgrove               Change scheduled                Grid Monthly   12    2026-11-24  24.00
5202  Bramley Kite Studio         bramley                Needs billing-contact confirmation  -          -     -           -
5203  Cobalt Wren Design          cobaltwren             No change — condition not met   -              -     -           -
5204  Dunmore Lane Architects     dunmore                No change — condition not met   -              -     -           -
5205  Elderfield Print Co         elderfield             Change scheduled                Grid Annual    11    2026-12-03  240.00
5206  Fernhill Motion Ltd         fernhill               No change — withdrawn           -              -     -           -
5207  Gannet Row Studio           gannetrow              Needs billing-contact confirmation  -          -     -           -
5208  Hollis Marlow Partners      hollismarlow           No change — condition not met   -              -     -           -
5209  Inkwell Harbour             inkwell                Change scheduled                Line Monthly   6     2026-11-30  12.00
5210  Juniper Vale Design         junipervale            Change scheduled                Mosaic Annual  8     2027-01-15  372.00
5211  Kestrel Point Creative      kestrel                Change scheduled                Grid Monthly   16    2027-01-31  26.00
5212  Larchmont Type Foundry      larchmont              Change scheduled                Mosaic Annual  7     2026-12-12  348.00
5213  Mistral Yard                mistral                Cancellation scheduled          -              -     2027-03-01  -
5214  Northgate Signal            northgate              Change scheduled                Line Annual    24    2027-02-02  120.00
5215  Oriel Glasshouse            oriel                  No change — already in place    -              -     -           -
5216  Pemberton Hale Architecture Ltd  pha_ltd           Change scheduled                Line Monthly   3     2026-12-01  12.00
5217  Rowan Quay Media            rowanquay              Change scheduled                Grid Monthly   18    2026-12-10  24.00
5218  Saltmarsh Collective        saltmarsh              Change scheduled                Grid Monthly   2     2026-11-28  24.00
5219  Tamsin Ode Studio           tamsinode              No change — condition not met   -              -     -           -
5220  Umber & Lime                umberlime              Change scheduled                Grid Monthly   14    2026-11-18  24.00
5221  Vellum Street               vellum                 Change scheduled                Grid Annual    5     2027-01-27  258.00
5222  Wickham Forge               wickham                Change scheduled                Mosaic Annual  4     2026-12-07  348.00
5223  Yarrow Bright               yarrow                 Change scheduled                Grid Monthly   8     2026-11-16  24.00
5224  Zephyr Lantern Studio       zephyr                 Cancellation scheduled          -              -     2026-12-14  -

TALLY: changes 14, cancellations 2, condition-not-met 4, withdrawn 1, already-in-place 1, awaiting-contact 2 = 24
STRIPE WRITES (cancel_at_period_end=true): sub_tsl_mistral, sub_tsl_zephyr  — nothing else.

## Where I depart from Tom's draft sheet
5203 Cobalt Wren: he scheduled Mosaic Annual @£29/mo (under their £30). The move starts 2027-01-08,
      a 2027 period: Mosaic Annual is £372/yr = £31.00/mo >= £30 -> condition NOT met.
5208 Hollis Marlow: he scheduled Grid Annual @£20/mo (<= their £21). Starts 2027-01-19:
      £258/yr = £21.50/mo > £21 -> condition NOT met.
5213 Mistral Yard: he said Grid price unchanged -> no cancellation. Grid Annual DOES rise
      £240 -> £258 for periods from 1 Jan 2027; their renewal 2027-03-01 is such a period
      -> condition MET -> cancellation scheduled at 2027-03-01. (Hugo's hold request declined.)
5219 Tamsin Ode: he dropped them to Grid. "unless Grid is getting more expensive next year" —
      Grid Annual £240->£258 (and Monthly £24->£26) -> unless-condition holds -> stay on Mosaic.
5210 Juniper Vale: price 348 -> 372 (effective 2027-01-15, a 2027 period).
5211 Kestrel Point: price 24 -> 26 (effective 2027-01-31).
5221 Vellum Street: price 240 -> 258 (effective 2027-01-27). Condition (<£22) still met at £21.50.
5216 Pemberton Hale: he booked cus_tsl_pha_arch (Grid Annual, 12 seats, Julian Hale).
      Correct account is Pemberton Hale Architecture Ltd / cus_tsl_pha_ltd (Line Monthly, 5 seats,
      billing contact Ruth Adeyemi = the requester; Ruth's Zendesk org is 9116 PHA Architecture Ltd).
5220 Umber & Lime: he used the anchor 2026-12-06. Seat ADDITIONS are immediate (s4); customer asked
      for Wednesday 2026-11-18 ("from day one"), a later point than today -> 2026-11-18 governs.
5217 Rowan Quay: same outcome, different reason. Leo (Producer) is not the billing contact and his
      emailed copy adds nothing; Nadia Pereira (billing contact) gave the go-ahead herself in
      Intercom on 13 Nov -> authorised under s2/s3.
