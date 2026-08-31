# 02: Complete batch Intake and duplicate handling

**What to build:** Expand Intake into the approved general entry point for ETF batches, with deterministic parsing, validation, dry runs, and duplicate policy. Preserve the Stock-ready domain model while rejecting Stock creation until a supported processor exists.

**Blocked by:** 01

**Status:** ready-for-agent

- [ ] Intake accepts comma-separated tickers, bullet lists, Markdown tables, and a project-relative input document.
- [ ] A mixed ETF/Stock input is accepted only when every item has an explicit Type value; ambiguous mixed input fails without partial writes.
- [ ] Tickers and types are normalized, duplicate input rows are collapsed, and cards are produced in deterministic order.
- [ ] A dry run returns the proposed batch and card actions without changing durable files.
- [ ] Repeating an instrument/workflow pair with an active Ready, In Progress, or Blocked card reuses that active card instead of creating another.
- [ ] A new refresh card may be created for an instrument/workflow pair whose earlier cards are terminal.
- [ ] ETF items route to ETF performance; Stock items fail with a clear unsupported-processor result in V1 and create no card.
- [ ] Batch results distinguish created cards, reused active cards, rejected items, and dry-run proposals.
- [ ] Behavioral tests cover every accepted input form, invalid mixed input, deterministic order, active duplicate reuse, and refresh after terminal state.
