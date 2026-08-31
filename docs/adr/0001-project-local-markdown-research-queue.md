---
status: accepted
---

# Use a Project-Local Markdown Research Queue

Replace Trello as the operational state owner with one project-local Research
Queue backed by stable Markdown Research Card files. Obsidian Bases and Base
Board project those files into Intake and Monitor views, while deterministic
project-scoped skills and scripts own creation, claiming, result routing, lease
recovery, and validation. This keeps the queue inspectable and versioned with
the research vault without making an Obsidian plugin or board note a second
source of truth.

## Considered Options

- Keep Trello: familiar lanes and remote coordination, but state remains outside
  the vault and requires connector-specific skills, identities, and mutations.
- Use classic Obsidian Kanban as the state owner: convenient visually, but its
  board note duplicates the state of one-file-per-job cards.
- Create separate Stock and ETF queues: simpler initial filters, but duplicates
  lifecycle behavior and makes new Research Workflows harder to add.
- Use one card per instrument: fewer files, but conflates independent workflows,
  retries, blockers, and durable outcomes for the same instrument.

## Consequences

- A Research Card represents one instrument plus one explicit Research Workflow;
  active duplicates for the same pair are rejected, while completed work may be
  refreshed by a new card.
- Research Cards share `ready`, `in-progress`, `blocked`, `done`, and `cancelled`
  states. Humans own intake, manual holds, and unblocking; automation owns claims
  and durable completion.
- A two-hour renewable project lease serializes scheduled work in one checkout.
  Fencing stops an expired owner from mutating state. Safe stale claims return to
  Ready; ambiguous partial writes become Blocked.
- `research-card-intake` and `research-queue-manager` are project-scoped skills.
  Deterministic scripts own the file protocol, and downstream research must return
  a validated structured handoff before a terminal transition.
- V1 processes ETF performance only while keeping the card and batch vocabulary
  general. Stock workflow routes are a later extension.
- One terminal card transition and its scoped research outputs are committed
  together. Done and Cancelled cards retain stable paths for history and links.
- Existing Trello tickers are a one-time seed into Intake. There is no permanent
  Trello importer, provenance schema, synchronization, or post-seed mutation;
  the old board remains inert history after automation cutover.

This decision supersedes the Trello-owned workflow in
`2026-08-15-trello-etf-skill-decomposition.md`.
