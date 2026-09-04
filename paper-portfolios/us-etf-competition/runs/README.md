# Scheduled Portfolio Runs

Each `YYYY-MM-DD.md` note records one Portfolio Run with frontmatter,
decision/reference timestamps, sources, calculations, the required decision
table, an `IN`/`OUT`/`HOLD` change log, data gaps, and the ledger event IDs
produced by that run.

Run notes are evidence, not the accounting system of record. The canonical
event stream is `../ledger/events.jsonl`.

New run notes link to one market-data batch under
`../evidence/market-data/batches/` and list the relevant `evidence_id` values.
They may also link to the compact screen cache and price-log projections. Older
run notes retain their dated per-ticker evidence links; those legacy files are
read-only and are not rewritten during the batch migration.
