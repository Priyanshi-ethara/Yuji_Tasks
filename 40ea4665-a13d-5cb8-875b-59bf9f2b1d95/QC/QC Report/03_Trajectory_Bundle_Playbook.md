# QC Report — 40ea4665-a13d-5cb8-875b-59bf9f2b1d95   layout: full   runs: 1   model(s): opus-5

`qc 2/traj/10_bundle_playbook.md` was run on a copy of the delivered bundle (`export BUNDLE=<copy>`, with QC/
removed). Every script ran as written (loader, §1, §1.5, §1.6, §2, §3, §4, §5). The raw output is in
`03_playbook_script.txt`. `run_1` is job `40ea4665-a13d-5cb8-875b-59bf9f2b1d95-opus-5-20261116-112639`, trial
C9Cx4WD, task_checksum `4b0823a2…0d5e`. That checksum matches the delivered task and the harbor oracle and nop.
`verifier/reward.json` is trimmed to `{"reward": 0.1615}`. The channels come from `report.json.channels`, as the
loader states.

## §1 Model
- ✅ config / result / report / trajectory agree. `config.agent.model_name anthropic/claude-opus-5`,
  `result.agent_info.model_info.name claude-opus-5`, `report.model / model_full opus-5 / anthropic/claude-opus-5`,
  `trajectory.steps[].model_name ['anthropic/claude-opus-5']`. Result: `distinct models after normalising ['opus-5'] ok`,
  `models seen mid-run 1 ok`.
- `schema_version ATIF-v1.5 ok`; agent `openhands-sdk / openhands-sdk v1.59.0 / {'name': 'openhands-sdk',
  'tool_definitions': None, 'version': '1.59.0'}`; `reasoning_effort high`.

## §1.5 Score sanity (per run)
- 1.5a `{'reward.json/channels': 0.1615, 'report.final_reward': 0.1615, 'result.verifier_result': 0.1615,
  'pass_summary.per_run.combined': 0.1615}  spread=0.0  ok`.
- 1.5b `source=grade_report.json rows=22 earned=9.0 penalty=0.0 total_positive=42 guard_polarity=pass_charges`.
  Recompute `0.2143 vs reported 0.2143 ok`. Weighted 22 = ledger 22, no weight drift, `guards tripped [] / 7 missed`,
  `tests that raised none`.
- 1.5c `judge ran=True model=gpt-5.6-sol reason=None`. Recompute `0.1087 vs reported 0.1087 / channel 0.1087 ok`.
  `n=25 yes=13 no=12 raw values=['no', 'yes'] errors=0`. `judge.toml vs graded missing_in_graded=[] extra_in_graded=[]
  weight_or_text_drift=[]`. `report.rubric count 25 (ok)`.
- 1.5d `polarity mismatches none`; source weights `positive=46 penalty=17`, normalised positives sum 1.0.
- 1.5e `weights={'pytest': 0.5, 'rubric': 0.5} -> 0.1615 vs reward 0.1615 ok`.
- 1.5f `exception_info=None errored=False state_capture_failed=None agent_steps=101 last_step_source=agent`.
  `final_message.md=11938 chars, last agent text=11938 chars, same=True`. `final_metrics={'total_prompt_tokens':
  9019982, 'total_completion_tokens': 65494, 'total_cached_tokens': 8691882, 'total_cost_usd': 8.0338035}`.
- No BLOCKER. No MAJOR.

## §1.6 Aggregates
- `runs=1 completed=1 errored=0 per_run=1 folders=1 ok`.
- Threshold 0.7 in pass_summary, test_weights and pass@N: ok.
- Pass bits: no violations. Averages: combined 0.1615, pytest 0.2143, rubric 0.1087, all recomputed ok.
- `pass@N.json passed=0 (recomputed 0) pass_rate=0.0`. Histogram `{'partial': 1}` sum 1, ok.
- `jobs.json [('40ea4665-…-opus-5-20261116-112639', 1)]`.
- Flags: `runs_without_rubric=[] runs_with_state_capture_failed=[] errored_run_indices=[]
  judge_models=['gpt-5.6-sol']`.

## §2 Failure classification (per run)
- `2.0 passed False reward=0.1615 threshold=0.7 failure_mode=partial`.
- Environment evidence (2.1), all clean:
  - `2.1a state capture failed=None note=None end_env.json=shipped`
  - `2.1b None / False`
  - `2.1c judge ran=True … rubric_judge_failed.txt=absent`
  - `2.1d total=100 mcp=79 local=21 ok`
  - `2.1e tool results that look like server errors 0`
- Three calls came back `status: failed`. Each was caused by the agent's own input, and the agent recovered from each:
  - step 13: a SOQL `LIMIT` query. The agent recovered with `list_records Account` at step 15.
  - step 49: Box folder `0`. The agent recovered with folders 720002–720004 at steps 50–52.
  - step 92: a QuickBooks `WHERE TxnDate` verification query, made after all drafts existed. The agent checked
    locally at step 93 and ran `get_invoice` at step 94.
  None of them is on the path the event tests depend on.
- **Bucket B — `stale-read`.** The task re-delivers data mid-run: when the 21st distinct customer's draft is accepted,
  the amendment lands in the asset-register pages of four meters. The run billed those four meters on the values it had
  read before the amendment. Evidence:
  1. `agent/trajectory.json`: the run read all 22 register pages with `LightNotion_list_block_children` at steps
     21–42. No observation in the run contains "Amendment 16 Nov" (0 hits). The 21st distinct customer's draft
     (Penhallow Tool Hire, 7121) is the `create_invoice` at step 90. After step 90 the run made one more draft (91), a
     QuickBooks query (92), `get_invoice` (94) and `send_mail` (99). It made no Notion read, and it never opened
     LightMicrosoftTeams (`2.2c wired servers never called` includes LightMicrosoftTeams).
  2. `verifier/end_env.json`: the Notion pages carry "Amendment 16 Nov 2026 (Owain Castellack, site visit): the
     measurement CTs now installed are 600/5 … 400/5 … 750/5 …" (4 pages), so the event fired.
     `verifier/final_message.md` §2 gives "Run net total: **£254,015.70**" and "Total billed energy:
     **1,015,165.902 kWh**". These are the pre-amendment figures; the amended total is £286,186.15.
  3. `2.2e positive tests missed 7`, which include the re-read tests: `test_amended_meter_records_read_before_the_summary_mail`,
     `test_amended_sites_drafted_after_their_amendment_was_read`, and `test_amended_meter_site_1..4_billed_on_its_amended_record`.
     The rubric ids 1–9 (the CT items) are judged no.
- Not guard-tripped (`2.2d guards tripped none`). Not gave-up-early: the run finished every required write (22 drafts
  and the summary mail) and ended with `finish`. Not tool-surface-tunnel-vision: the reply does not say the register or
  Teams was unavailable.

## §2.5 Isolation and leakage (per run)
- `result.json` `verifier_environment_mode`: `separate`.
- Grader paths touched by the agent: none. A grep of every tool-call argument for `/tests`, `test_outputs.py`,
  `test_weights.json`, `judge.toml`, `reward`, `solution/`, `TRUTH.md`, `gt_env.json` and `oracle.json` has 0 hits.
  runcheck: `/tests mentioned: False`, `task_lib mentioned: False`.
- Leakage in tool results: none. The amended figures (£286,186.15, 1,143,171 kWh, 98,328.686 kWh, 270.95 kW) never
  appear in any observation.
- Trivial-solution credit: none. The run made 79 MCP calls and 23 writes. Its 9 pytest points come from correctly
  billed static groups. The harbor nop on the same bytes scores 0.0 / 0.0 / 0.0.

## §3 Reasoning
- `agent steps / with reasoning 101 / 29 (11355 chars) field(s) used: ['thought']`. `reasoning_effort requested high`.
  Verdict `present`. Per-step metrics 0 of 101 (INFO: totals are in `final_metrics`).

## §4 Overlap
- 22 tests vs 25 criteria. The matcher gives DOUBLE-COUNTED=1, PARTIAL=0, INDEPENDENT=21 (redundancy 5%), and 24 of 25
  criteria are rubric-only.
- The one DOUBLE-COUNTED row is `test_demand_register_sites_billed_on_energy` (w 1) vs criterion 12 `r-twin` (+1),
  with S1 0.14 and S2 1.00. I read both. It is a false positive:
  - The test's only literals are the label strings `"demand"` and `"demand-registered sites"` passed to
    `_group_right(_unmoved("demand"), …)`, and both words occur in r-twin's text.
  - The test grades QuickBooks draft amounts for the unamended demand-registered sites (Fenwick Lane, Gorsebrook,
    Kittering).
  - r-twin grades the reply's statement that Hollin Bridge and Wexcombe, the energy-register twins, were not halved.
  - Different sites and a different signal (ledger end state vs reply prose), so not a double count.
- Strict owner check: no rubric item restates an end-state value, a write, a tool-call order, or a guarded act that
  pytest grades. The CT items (1–9) grade explanations and figures (factors, kWh, kW, provenance). Pytest grades only £
  amounts on drafts and read order. Penalties 21–25 are declared wrong figures, not guards.
- Lost weight: pytest positive lost 33/42 = 78.6%, guards charged 0.0. Rubric positive lost 0.7609/1.0000 = 76.1%,
  penalties charged 0.1304.
- Recommendation: `keep both`.

## §5 False pytests
- 22 tests scanned. `0/22 tests carry a flag; BLOCKER flags: 0`. No assert or return line carries a rubric figure
  (5.2 is empty).

## Verdict
- **SIGNED.** §1, §1.5, §1.6 and §2.5 have no BLOCKER. §2 is Bucket B `stale-read`, a genuine model miss of a live
  event. §3 reasoning is present. §4 has one matcher false positive, read and cleared. §5 has 0 flags.
