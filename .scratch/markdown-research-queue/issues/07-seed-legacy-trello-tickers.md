# 07: Seed legacy Trello tickers through normal Intake

**What to build:** Perform the one-time Trello seed by reading only tickers from the live Ready and Blocked lists and submitting them to ordinary ETF Intake. Trello remains untouched and becomes inert after the seed.

**Blocked by:** 02, 06

**Status:** ready-for-agent

- [ ] Immediately before seeding, the live Trello board is reread and the authoritative Ready and Blocked ticker set is captured.
- [ ] Only ticker values are carried forward; Trello descriptions, status, provenance, comments, and workflow metadata are ignored.
- [ ] The captured tickers are submitted through the same normal ETF Intake used for future requests.
- [ ] Intake normalization and active-duplicate handling prevent duplicate active Research Cards.
- [ ] The local result count reconciles to the deduplicated live source set, with created, reused, and rejected totals reported separately.
- [ ] The current planning baseline of 72 Ready-plus-Blocked cards is treated only as a checkpoint; the fresh live read is authoritative.
- [ ] Seeding creates no migration-only schema, provenance fields, synchronization rules, or ongoing Trello dependency.
- [ ] No Trello card or list is created, edited, moved, archived, or deleted.
- [ ] A post-seed verification confirms that the Obsidian views show the seeded queue and Trello is no longer used for selection.
