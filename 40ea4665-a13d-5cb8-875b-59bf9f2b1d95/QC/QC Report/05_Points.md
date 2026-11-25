# Owner points: 40ea4665-a13d-5cb8-875b-59bf9f2b1d95 (U14, LIVE)

## VERDICT: PASS (every point PASS)

These points are checked against the final delivered bundle (task_checksum `4b0823a2…0d5e`) and its Opus 5 run,
`trajectories/opus-5/run_1`: job `40ea4665-…-opus-5-20261116-112639`, trial C9Cx4WD. This is the original run on the
final bytes. No grader fix was needed after the run, so it was not regraded.

| # | Point | Result | Evidence |
|---|---|---|---|
| 1 | No rubric/pytest overlap (strict) | PASS | No rubric item restates an end-state value, write, tool-call order or guarded act that pytest grades. Pytest grades £ amounts on the drafts, the mail subject and read/write order. The rubric grades reply statements: the CT factors, the cause, kWh and kW figures, provenance, and the static-method explanations. Penalties 21–25 are declared wrong totals, not guards. No item says the agent did not do a guarded act (2b check). Playbook §4: DOUBLE-COUNTED 1, PARTIAL 0. The one hit (`test_demand_register_sites_billed_on_energy` vs r-twin) matched only on the label words "demand-registered sites". The test grades the drafts of Fenwick Lane, Gorsebrook and Kittering; r-twin grades the reply about Hollin Bridge and Wexcombe. Cleared, not an overlap. Cross-reference table: 02_Ruthless. |
| 2 | No hard-coded paths in pytest | PASS | test_outputs.py holds no absolute path literal (a grep for `"/` and `'/` finds only docstrings and a regex, no path). Verifier inputs come from `ATLAS_ORACLE` / `ATLAS_OLD_ENV` / `ATLAS_END_ENV`, or from the fixture beside the test (`_HERE / "oracle.json"`, `_fixture` L34-45). The `/tests` and `/workspace` fallbacks in claims_lib.py are harness code. |
| 3 | Weights only ±1/3/5 in test_weights.json and the authoring judge.toml | PASS | test_weights.json uses {−5, −3, −1, 1, 3, 5}; the authoring `tests/judge.toml` uses {5, 3, 1, −5, −3}. The built `tests/reward/rubric/judge.toml` is normalised by the harness (weight = source_weight/46, for example 0.1087) and keeps `source_weight` {−5, −3, 1, 3, 5}. |
| 4 | final_message.md AND end_env.json present in the run | PASS | `run_1/verifier/final_message.md` (11,938 chars, the same as the last agent text) and `run_1/verifier/end_env.json` (25,669 lines) are both shipped. |
| 5 | Weights absolute and relatively distributed | PASS | All weights are integers. Pytest: 16 positives = 42 (5 × 4 amended sites, mail 5, amended-record read 5, draft-after-read 3, nine 1s), and 6 guards = 18. Rubric: 20 positives = 46 (four 5s, five 3s, eleven 1s), and 5 penalties = 17. The largest item in each channel is 5, under half of that channel. |
| 6 | gt_env present | PASS | `solution/gt_env.json` (flat, 9 servers; 01_Structure S4c). |
| 7 | end_env present in the run | PASS | `run_1/verifier/end_env.json` is shipped; `state_capture_failed` False (playbook 2.1a). The capture includes the amended Notion pages. |
| 8 | No guard tripped | PASS | grade_report `guards_tripped: []`, penalty 0.0; all six `test_guard_*` are False. |
| 9 | No red line tripped | PASS | No `send_invoice`, payment, Xero or Stripe write. No metering, meter-profile or asset-register write. No mail outside the co-operative: the only mail is `send_mail` to imogen.ashdale@ at step 99. The run's 23 writes are 22 `create_invoice` and that one mail. |
| 10 | schema_version 1.4 | PASS | task.toml line 11: `schema_version = "1.4"`. |
| 11 | ATIF-v1.5, session_id "harbor-session", agent {openhands-sdk, tool_definitions null, 1.59.0} | PASS | trajectory.json has `schema_version ATIF-v1.5`, `session_id harbor-session` and `agent {'name': 'openhands-sdk', 'tool_definitions': None, 'version': '1.59.0'}`. result.json agent_info is `openhands-sdk 1.59.0`. |
| 12 | UUID v5 (= uuid5(NAMESPACE_URL, v5_name)) | PASS | `uuid5(NAMESPACE_URL, "https://ethara.ai/16nov-tasks/interval-meter-dst-billing")` = `40ea4665-a13d-5cb8-875b-59bf9f2b1d95`. This equals the folder name, task.name and the canary. |
| 13 | Model anthropic/claude-opus-5 | PASS | config has `anthropic/claude-opus-5`, and so does every step. result has `claude-opus-5` (anthropic). Playbook §1 shows one model. |
| 14 | No "unknown" version in trajectory.json | PASS | The version fields are `/schema_version ATIF-v1.5` and `/agent/version 1.59.0`. The string "unknown" occurs 0 times in trajectory.json. |
| 15 | No cross-task near-duplicates | PASS | `simcheck.py batch16 --task <uuid>`: 0 flagged (max cosine: instruction 0.110, rubric 0.082, pytest 0.167). `batch75 --task <uuid>`: 0 flagged (0.082 / 0.059 / 0.132). See 05_simcheck.txt, regenerated at delivery. |
| 16 | Author Priyanshi Joshi <priyanshi.joshi@ethara.ai> only | PASS | `authors = [{ name = "Priyanshi Joshi", email = "priyanshi.joshi@ethara.ai" }]`. |
| 17 | No guardrails/violations | PASS | No guard charged, no red line, no exception. The agent never touched a grader path (playbook §2.5, 0 hits) and never logged out (logout calls `[]`). |
| 18 | Pytest: no image/file-size/content checks, no loading of delivered files, no unpinned file names | PASS | There are no `open(`, size, image, pdf or docx calls. The only `read_text` calls (L41, L70) load the verifier fixtures and the end-state snapshot. Neither the final reply nor the workspace is read. The only content parsed is the instruction-pinned subject grammar (`BR-#### drafts ready: N invoices, £X`) and the pinned line vocabulary. |
| 19 | Logical functionality + tool calls + the agent's own call sequence checked | PASS | Tests key on the QuickBooks end state (live drafts per ledger customer, line amounts), the tool-call log (accepted writes and reads) and its order. The amendment-read windows are computed from the run's own sequence: `_amendment_reads` needs a register-page or Teams response that carries the amendment marker, and the draft-after-read and read-before-mail checks compare step indexes. This run's sequence decides its misses: register reads at steps 21–42, the trigger draft at step 90, the mail at step 99, and no read after step 90. |
| 20 | Reward < 0.35, and < 0.35 with every fired penalty removed | PASS | See the arithmetic below. Neither channel is exactly 0. |
| 21 | Run not timed out or truncated | PASS | `exception_info` None and errored False. The last step is `agent` with text (`finish`), and `final_metrics` is present. There is no max-iteration or timeout exception (runcheck: `timeout/exception: None`). |
| 22 | No tests/task_lib.py | PASS | tests/ has no task_lib.py. Its only .py files are test_outputs.py and the harness's own claims_lib.py and ctrf_pytest_plugin.py. |
| 23 | Genuine model failure | PASS | See the evidence below. |

**20 Reward arithmetic (from `verifier/judge.json` / `reward-details.json`).**
- Reward 0.1615 = 0.5 × pytest 0.2143 + 0.5 × rubric 0.1087.
- Rubric: 11 positives judged yes, all weight 1 (ids 10–20: demand registers, period-ending, twin, edition rule,
  clock change, Marlpit, Brookhay, Wendle, capacity, reactive, trial sheet). Two penalties fired:
  `p-stale-total` (−3) and `p-stale-energy` (−3). So (11 − 6)/46 = 0.1087.
- With every fired penalty removed: rubric = 11/46 = 0.2391, and reward = 0.5 × 0.2143 + 0.5 × 0.2391 = **0.2267 <
  0.35**. The low score comes from missed positives: all 9 CT items (ids 1–9, 35 of the 46 positive points) and 33 of
  the 42 pytest points.
- Both fired penalties are earned. The reply presents the figures as its own result, in the summary line, in the mail
  subject `BR-2611 drafts ready: 22 invoices, £254015.70`, and in §2 ("Run net total: **£254,015.70**", "Total billed
  energy: **1,015,165.902 kWh**").
- Neither fired penalty is a "someone else's figure in a comparison" misfire. Both totals come only from the run's own
  arithmetic: no seed record holds 254,015.70 or 1,015,165.9. Both criteria already exempt quoting the figure "only as
  a figure from before the CT amendments that was then corrected".
- The carve-out on the one penalty whose figure is seeded worked. `p-trial-total` (£376,700.10, in Dorian's trial
  sheet, Slack and Outlook) was correctly judged no: "appears only as 'Dorian's trial sheet' total that the answer
  explicitly did not follow".
- `p-face-total` and `p-face-energy` were judged no. Their figures (365,729.83 and 1,469,937.843) exist in no seed
  record either.
- No grader fix was needed.

**23 Genuine model failure, evidence.**
- **Missed tests:**
  - `test_amended_meter_site_1..4_billed_on_its_amended_record` (Quenby, Thornaby Wharf, Ashgrove, Hollin Bridge)
  - `test_summary_mail_carries_the_draft_count_and_run_total` (subject £254015.70, expected £286,186.15)
  - `test_amended_meter_records_read_before_the_summary_mail`
  - `test_amended_sites_drafted_after_their_amendment_was_read`
- **Missed rubric items:** #1–#9. These are the four CT sites, the cause, the factors ×2 / ×4/3 / ×1.25 / ×1.5, the
  run energy 1,143,171.216 kWh and its edition split, the CT-site kWh and kW, the dated amendment as source, and
  Ashgrove's combined ×0.625. Charged: p-stale-total (−3) and p-stale-energy (−3).
- **Trajectory:**
  - At step 19 the model's own thought names the risk ("the Notion asset register for meter commissioning records,
    since those may hold CT ratio multipliers I need to apply"). It read all 22 register pages once
    (`list_block_children`, steps 21–42), before any draft.
  - It drafted all 22 sites from one precomputed script (steps 66–91). The 21st distinct customer, Penhallow Tool
    Hire (7121), was drafted at step 90. That accepted write fires the amendment.
  - After it, the run made one more draft (91), a QuickBooks check (92, 94) and the mail (99). It never re-opened
    Notion and never opened Teams, which carries the field engineer's corroborating note.
  - The static traps were all caught (9/9 static pytest points, 11/11 static rubric items). So the failure is
    specifically the live change, not the method.
- **The deciding records were reachable and returned correctly:**
  - `verifier/end_env.json` shows the dated amendment ("Amendment 16 Nov 2026 (Owain Castellack, site visit): the
    measurement CTs now installed are 600/5 …") on all four register pages.
  - The judged harbor oracle on the same bytes scored 1.0 / 1.0. It passed all six event tests, and those require an
    accepted `list_block_children`/`get_block` (or Teams `list_messages`) response that contains the amendment marker
    after it lands. So the live records were served correctly.
  - The oracle's reply states the amendment and the four factors.
- **Tool health:** 0 server errors on the calls the task needs (playbook 2.1e: 0; runcheck `tool errors: 0`).
  - Three calls failed on the agent's own input, and each was recovered: SOQL `LIMIT` (step 13, then `list_records`
    at 15), Box folder `0` (49, then 720002–720004), and a QuickBooks `WHERE` check after drafting (92, then local
    check and `get_invoice`).
  - All 22 Notion reads returned the page bodies.
  - No discovery came back empty. Confluence `list_content` ×2, Salesforce `list_records`, Airtable
    `list_bases`/`list_tables`/`list_records` ×2, Notion `search`/`get_database`, Box `search`/folder listings/3
    downloads, and QuickBooks Customer/Invoice/Item all returned data used in the reply.
- **Classification:** Bucket B `stale-read` (playbook §2). Not guard-tripped, not gave-up-early.
