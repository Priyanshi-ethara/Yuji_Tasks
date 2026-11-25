# Product tag migration - June 2026

Desk Tooling and Desk Quality replaced the product tags with the catalogue names on 16 June 2026. Tickets opened before then,
and tickets logged since by agents using old macros, may still carry the old tag. Open tickets get the new tag when they are
next categorised; closed tickets keep the old tag (TOOL-495 will archive them).

| Old tag | New tag | Product |
|---|---|---|
| prod_fttp_150 | prod_fibre_home_150 | Fibre Home 150 |
| prod_fttp_500 | prod_fibre_home_500 | Fibre Home 500 |
| prod_fttp_900 | prod_fibre_home_900 | Fibre Home 900 |
| prod_adsl | prod_copper_bb | Copper Broadband |
| prod_pstn | prod_home_phone | Home Phone (digital voice) |
| prod_mesh | prod_wifi_max | Wi-Fi Max |
| prod_iptv | prod_lumen_tv | Lumen TV |
| prod_sim | prod_mobile_sim | Lumen Mobile SIM |
| prod_handset | prod_mobile_handset | Lumen Mobile Handset |
| prod_bfttp_300 | prod_biz_fibre_300 | Business Fibre 300 |
| prod_bfttp_1g | prod_biz_fibre_1g | Business Fibre 1G |
| prod_bizvoice | prod_biz_voip | Business Voice |
| prod_bizsim | prod_biz_mobile | Business Mobile |
| prod_account | prod_account_general | Account (no single product) |
| prod_fttp_70 | prod_fibre_home_150 | Fibre Home 70 (withdrawn, migrated) |
| prod_stb_classic | prod_lumen_tv | Lumen TV Classic box |
| prod_tvsport | prod_lumen_tv | Sport boost |
| prod_pstn_plus | prod_home_phone | Calls bundle |

Notes
- The old tags prod_sim and prod_handset were often swapped by the IVR; read the contact, not the old tag.
- prod_pstn becomes prod_home_phone: the PSTN switch-off moved every home phone to digital voice over the router.
- Nothing else about tags changed in the migration.
