# Output Contract

This page defines compact, source-backed output shapes.

## Mode Selection And Budgets

Use explicit `mode: chat | lean | full` first. Otherwise route general why,
explain, outlook, and prediction questions to `chat`; save/update/ingest/refresh
requests to `lean`; and explicit full/deep-dive/archive or legacy full-chain
requests to `full`.

| Output | Chat | Lean | Full |
|---|---:|---:|---:|
| Chat response | <=400 words | <=200 words after writes | <=200 words after writes |
| Entity narrative | no write | 250-400 words changed | <=700 words |
| Valuation narrative | no write | <=500 words | <=900 words |
| Decision memo | no write | 400-500 words | <=800 words |
| Charts | 0 | <=1 | <=3 |

Source and normalized tables are exempt. Budgets apply to narrative. Omit empty
or unsupported optional sections.

## Single Source Of Truth

| Layer | Owns | Other layers use |
|---|---|---|
| `raw/imports/` | Raw evidence, source map, extraction gaps | local links |
| `raw/financials/` | Normalized numbers, ratios, period-compatible chart data | compact metric references |
| `wiki/entities/` | Living company summary and unresolved ticker-level gaps | links to facts/reports |
| `wiki/analysis/valuations/` | Assumptions and calculations | valuation conclusion/link |
| `wiki/analysis/decisions/` | Action and decision-changing evidence | links to prior layers |

Do not copy full tables, source maps, bull/bear cases, or gap lists across
layers.

## Language

Use Thai-first narrative. Keep headings, keys, filenames, tickers, source
labels, table columns, formulas, and precise finance terms in English. Preserve
source meaning and language in raw notes.

## Source Note

```text
raw/imports/TICKER_source_kind_YYYY-MM-DD.md
raw/imports/TICKER_latest_results_source.md
```

Required: frontmatter, `Source Map`, `Reporting Scope`, `Currency / Units`,
`Extracted Facts`, extraction-specific `Missing / Unverified Data`, and
`Handoff For Ingest`. Add transcript or financial tables only when relevant.
The minimal profile extracts only fields needed downstream; full profile is for
explicit archival requests.

## Financial Facts

```text
raw/financials/TICKER_fundamentals.md
```

Required: `Snapshot`, `Provenance`, `Reporting Scope`, `Financial Table`,
supported `Key Ratios`, and normalization gaps. Add only supported comparison
sections and the most decision-relevant chart within the mode limit. Market
quotes belong in a dated market source or decision/valuation check, not the
normalized company facts file.

`TICKER_fundamentals.json` is opt-in when requested or needed by a downstream
machine workflow.

## Entity

```text
wiki/entities/TICKER.md
```

Use `wiki/reference/entity-template.md`. The entity is a thin living hub, not a
copy of fundamentals or analysis memos. Update only changed sections.

## Valuation

```text
wiki/analysis/valuations/TICKER DCF Valuation YYYY-MM-DD.md
```

Create when a source-backed calculation succeeds. Include `Bottom Line`,
compact source links, inputs, assumptions, calculation/projection, valuation
summary, sensitivity when meaningful, sanity checks, valuation blockers, and
change triggers. If calculation cannot proceed, put a short blocker in the
decision memo unless the user explicitly requests a valuation-gap memo.

## Decision

```text
wiki/analysis/decisions/TICKER Decision Memo YYYY-MM-DD.md
```

Use `Action Read`, current market-data check, decision-changing evidence,
compact valuation read, key assumption/falsifier, action-relevant gaps, and
local report/source links. Reference the entity's bull/bear case instead of
restating it unless the decision changed it.

## General Research Routing

```text
wiki/analysis/catalysts/TICKER Market Move YYYY-MM-DD.md
wiki/overview/themes/THEME.md
wiki/overview/macro/TOPIC.md
```

Market-move notes contain the move check, up to three evidence-labelled
drivers, thesis impact, and falsifiers. Theme and macro files are living notes
with current thesis, causal map, scenario table, signposts, falsifiers, compact
sources, and a dated delta log. Do not create a generic discussion folder.

## Sentiment And Audits

Sentiment and scoped audits default to chat. Save a sentiment memo when asked
or when it changes durable follow-up. Save an audit memo for a requested
durable audit or applied fixes.
