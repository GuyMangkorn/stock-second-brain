# Research Queue Operations

## Intake

```bash
python3 scripts/research_queue.py intake --tickers "VIG,DGRO" --type ETF
python3 scripts/research_queue.py intake --input-file watchlist.md --dry-run
```

## Human controls

```bash
python3 scripts/research_queue.py hold --card-id <CARD_ID> --reason "..."
python3 scripts/research_queue.py unblock --card-id <CARD_ID>
python3 scripts/research_queue.py cancel --card-id <CARD_ID>
```

## Scheduled processing

The scheduler must pass `count`, `execution_profile: scheduled-inline`, and a
single project-local checkout. Claim cards with `claim-next`, renew at phase
boundaries, call the explicit workflow, and route only the complete seven-field
`research_handoff`. See [[Research Queue Monitor.base]] for the operational
projection.
