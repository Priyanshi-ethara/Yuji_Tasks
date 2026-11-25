# Document control - how the register is kept (note for RA, Pieter Vandamme, 2026-09-01)

- The **controlled store** (Drive, "Kestrel-3 Technical File (controlled)") holds every released file. Its version
  history is the release record: revision, released / routed for approval / working draft, pages, open placeholders.
- The **Document Control Register** (Monday) is the source of record for approval status. I reconcile it from the
  closed change requests every Friday at the register sync.
- Between two syncs a revision released under a change request that is **closed as implemented** is already
  approved (QA-SOP-007 6.4). Look at the change request, not at the register, for anything released since the last sync.
- Exports of the register (CSV) are snapshots for audits. They go stale the moment anything changes.
- An approval withdrawn by QA is recorded in the register only. The envelope stays "completed" in DocuSign for the
  audit trail; do not read it as an approval.
