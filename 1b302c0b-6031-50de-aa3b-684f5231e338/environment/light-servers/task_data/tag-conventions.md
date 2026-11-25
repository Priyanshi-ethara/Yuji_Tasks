# Lumen Desk tag conventions (Desk Quality)

Families
- channel_<phone|web|email|chat|internal> - set by the channel on creation.
- lang_<en|cy> - customer's language; lang_cy also notifies the Welsh rota.
- sla_<res_std|biz_std|biz_assure> - the SLA policy family; set by the account sync.
- noc_<incident> - link to a NOC parent (for example noc_wk04).
- acct_<number> - on organisations, from the account sync.
- prod_<product> - the Product drop-down (one per ticket, catalogue names).
- cr_<reason> - the Contact reason drop-down (one per ticket, Annex B).

Rules
1. Lowercase, words joined with underscores, no spaces.
2. Desk Quality changes only prod_ and cr_ tags. All other families are kept exactly as found.
3. Lumen Desk's update replaces the whole tag list: always send the kept tags with the new prod_/cr_ pair.
4. Never invent a tag family. Unknown tags found on a ticket are kept and reported to Desk Tooling.

Worked example (phone contact, Welsh speaker, residential, during the WK-04 outage)
- Found: channel_phone, lang_cy, sla_res_std, noc_wk04, prod_fttp_150, cr_fault_intermittent
- Filed: channel_phone, lang_cy, sla_res_std, noc_wk04, prod_fibre_home_150, cr_fault_no_service
  (pre-June product tag replaced from the catalogue; contact reason by meaning - no connection at all is no service;
  channel, language, SLA and NOC tags sent back exactly as found).

Families retired in June 2026
- prod_fttp_*, prod_adsl, prod_pstn, prod_mesh, prod_iptv, prod_sim and the other pre-June product names are replaced by
  the catalogue names (see product-tag-migration-2026-06 and the Q4 catalogue's pre_june_tag column).
- reason_* tags from the 2025 drop-down were removed from all open tickets during the migration; if one appears, treat it
  as an unknown tag (rule 4).

What is not a ticket tag
- Account number, segment and Business Assure live on the organisation, from the Salesforce sync. The desk never edits
  organisations and never copies organisation tags onto tickets.
- Macros add their own internal notes, never tags, apart from the NOC link (noc_ tags), which only the NOC macros set.
