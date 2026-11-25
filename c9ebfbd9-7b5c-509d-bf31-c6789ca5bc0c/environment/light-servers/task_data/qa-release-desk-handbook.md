# NDC QA release desk handbook

Maintained by Ines Calloway (QA Operations Lead). Last revised 2 November 2026.

## The round board
Each weekly release round has its own Trello board, "QA Release - Round R-<year>-<week>". Every lot of the round has a card
in **To review** when the round opens, named "<lot> - <product> - <shipment>". The outcome lists are Release,
Release with deviation, Quarantine, Reject and QA Head sign-off. Cards are never created or deleted by reviewers;
the round opener creates them from the ERP receipt list.

## Where the evidence is
- ERP mirror (read-only for QA): Lots, Shipments (handover and NDC receipt scans, assigned logger), Stability budget ledger.
- Brightline logger exports: downloaded from the Brightline portal into the round's data pack.
- Polar Arc logger exports: only in the Polar Arc carrier drop folder (the carrier does not use the portal since September).
- Product stability specifications: the Notion database "Product stability specifications".
- Calibration certificates: the Box folder of Metrology.
- The SOP in force: the Quality Assurance space of the wiki.

## Desk habits
- Raise the deviation first, then write the card, so the card can cite the key.
- The round closes with one note in #qa-release-desk. Nothing is posted in #coldchain-ops by reviewers.
- The release mailbox is for reading carrier and QA correspondence; reviewers do not send from it.
