# Research Queue

This directory is the project-local operational queue. Each Markdown Research
Card under `cards/` represents one instrument plus one explicit Research
Workflow. Each authorized Intake submission has one batch under `batches/`.

## Operating surface

- [[Research Queue Intake.base]] is the Base Board projection for Ready and
  Blocked cards.
- [[Research Queue Monitor.base]] is the native Bases monitor for every card
  status and lease/result metadata.
- `python3 scripts/research_queue.py` owns the deterministic file protocol.
- `.runtime/` contains only the renewable project lease and is ignored by Git.

The frontmatter `status` property is authoritative. Base Board and Bases are
projections; classic Kanban is not part of the state machine. Humans can hold,
unblock, or cancel work. Automation alone claims In Progress and finalizes
Done after a valid `research_handoff`.

## One-time Trello seed

Immediately before cutover, read only ticker values from the live Trello Ready
and Blocked lists and pass that list to the normal Intake command with
`seed`. Do not copy descriptions, provenance, statuses, or comments, and do
not mutate Trello. The design-time checkpoint is 69 Ready plus 3 Blocked
(72 tickers); reread the live board at cutover because that checkpoint is not
authoritative. After the seed and one-card pilot, scheduled selection reads
only this directory.

## Card status vocabulary

`Ready` → `In Progress` → `Done` is the automation path. Item-level errors go
to `Blocked`; a human may move `Blocked` back to `Ready`. `Cancelled` is a
terminal human outcome. All terminal cards remain at stable paths for links and
Git history.
