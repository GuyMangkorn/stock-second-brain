# Stock Second Brain Agent Rules

This project is an Obsidian-native stock research second brain. Maintain
durable, source-backed investment knowledge without turning every question into
a file-writing workflow.

## Mission And Ownership

- `raw/imports/`: source notes, filing extracts, transcripts, and raw evidence.
- `raw/financials/`: normalized company financial facts and ratios.
- `wiki/entities/`: one thin living company hub per ticker.
- `wiki/analysis/`: decisions, valuations, earnings, catalysts, comparisons,
  sentiment, and audits.
- `wiki/overview/themes/` and `wiki/overview/macro/`: living cross-company and
  macro notes.
- `index.md`: current dashboard. `log.md`: chronological durable-work history.

Use links instead of copying another layer's tables or narrative.

## Source Integrity Rules

1. Source before writing; never invent, smooth, backfill, or complete values.
2. Every durable number needs a URL, local path, filing reference, or shown
   calculation from sourced inputs.
3. Separate facts, calculations, assumptions, scenarios, and judgment.
4. Write `ไม่พบข้อมูลที่ยืนยันได้` or `not disclosed` when a value is not
   verified.
5. Record source conflicts and explain any source-quality choice.
6. Freshly check prices, multiples, targets, news, laws, and market data.
7. Preserve raw source meaning during ingest.

## Source Priority

1. SEC and official company filings
2. Earnings transcripts and call materials
3. Financial statements and metrics
4. News and web research
5. X/Twitter and market chatter as lower-priority context

Prefer Investor Relations for discovery and the underlying filing, release,
transcript, or data table as evidence.

## Language Standard

Use Thai-first narrative with English headings, frontmatter/JSON keys,
filenames, ticker/source labels, formulas, table columns, and precise finance
terms such as `DCF`, `FCF`, `WACC`, `valuation`, `margin of safety`,
`upside/downside`, `multiple`, `net debt`, `capex`, and `guidance`. Preserve
source-derived wording in the source language.

## Output Modes

Mode precedence:

1. Explicit `mode: chat | lean | full`
2. `full`, `deep dive`, `archive`, or a legacy full-chain request -> `full`
3. `save`, `update`, `ingest`, `refresh`, or `memo` -> `lean`
4. `why`, `explain`, `outlook`, `predict`, or a general question -> `chat`

| Mode | Contract |
|---|---|
| `chat` | At most 400 words; do not write files. |
| `lean` | Entity delta 250-400 narrative words; valuation at most 500; decision 400-500; at most one chart. |
| `full` | Entity at most 700 narrative words; valuation at most 900; decision at most 800; at most three charts. |

Source and normalized tables are exempt from narrative budgets. After durable
work, keep the final chat response under 200 words.

Promote `chat` to `lean` only when verified evidence materially changes an
existing thesis, risk, catalyst, or valuation watch item. Write only a compact
catalyst note, entity delta, and one `log.md` workflow bullet.

## Prompt Aliases

| Alias | Meaning |
|---|---|
| P1 | latest source discovery |
| P4 | financial ingest |
| P6 | new-ticker deep dive |
| P7 | existing-ticker thesis refresh |
| P10 | source integrity audit |
| P11 | valuation |
| P13 | decision memo |

Keep legacy prompts working, but prefer skill names and output modes in new
documentation.

## Operating Modes

### market-move

Use `.codex/skills/explain-market-move/SKILL.md` for why an asset moved today
or over a recent dated window. Default to chat. Save only a thesis-changing or
explicitly requested memo in `wiki/analysis/catalysts/`.

### scenario-research

Use `.codex/skills/market-scenario-research/SKILL.md` for technology or
supply-chain bottlenecks, country economies, monetary policy, FX, and market
scenarios. Default to chat; save requested living notes under
`wiki/overview/themes/` or `wiki/overview/macro/`.

### latest-results

Use `.codex/skills/latest-results-web/SKILL.md`. Create a source note before
ingest and use the minimal extraction profile unless full archival extraction
is explicit.

### ingest

Use `.codex/skills/financial-facts-ingest/SKILL.md`. Normalize verified fields,
make JSON opt-in, update the thin entity by delta, and append one workflow log
bullet.

### research

Use `.codex/skills/official-source-stock-research/SKILL.md`. Choose `chat`,
`thesis-delta`, or `deep-dive`; do not run a deep dive for a general question.

### valuation

Use `.codex/skills/dcf-valuation/SKILL.md`. Freshly verify market data and use
source-backed FCF, cash, debt, shares, and guidance. Create a valuation memo
only when a calculation succeeds or the user explicitly asks for a gap memo.

### decision-pipeline

Use `.codex/skills/stock-decision-pipeline/SKILL.md`. Read existing vault
context first, use the lightest sufficient flow, update the entity once, and do
not create a valuation-gap memo when P11 cannot calculate a valuation.

### sentiment

Use `.codex/skills/x-research/SKILL.md`. Treat sentiment as context, default to
chat, and save only when requested or when it changes a durable follow-up.

### query

Read `index.md`, then relevant entity, financial, and analysis notes. Answer
from vault context first. Default to chat.

### lint

Use `.codex/skills/source-integrity-audit/SKILL.md` for uncited numbers,
conflicts, stale data, chart/table mismatches, orphan pages, missing links,
duplicates, and unresolved gaps. A scoped check may be chat-only.

## Filename Rules

```text
raw/imports/TICKER_source_kind_YYYY-MM-DD.md
raw/imports/TICKER_latest_results_source.md
raw/financials/TICKER_fundamentals.md
raw/financials/TICKER_fundamentals.json
wiki/entities/TICKER.md
wiki/analysis/earnings/TICKER Earnings Transcript Digest YYYY-MM-DD.md
wiki/analysis/catalysts/TICKER Catalyst Update YYYY-MM-DD.md
wiki/analysis/catalysts/TICKER Market Move YYYY-MM-DD.md
wiki/analysis/comparisons/Theme Memo Title YYYY-MM-DD.md
wiki/analysis/valuations/TICKER DCF Valuation YYYY-MM-DD.md
wiki/analysis/decisions/TICKER Decision Memo YYYY-MM-DD.md
wiki/analysis/sentiment/TICKER X Sentiment YYYY-MM-DD.md
wiki/analysis/audits/Source Integrity Audit YYYY-MM-DD.md
wiki/overview/themes/THEME.md
wiki/overview/macro/TOPIC.md
```

## Entity Page Standard

Use the thin hub in `wiki/reference/entity-template.md`: compact snapshot,
source/report links, business model, thesis/key debate, risks, catalysts,
valuation watch items, follow-up, and unresolved ticker-level gaps. Link to
normalized tables and charts instead of copying them.

## Missing-Data Ownership

- source note: extraction gaps
- fundamentals: normalization and period-compatibility gaps
- entity: unresolved ticker-level gaps
- valuation: valuation blockers only
- decision: action-relevant gaps only

## Log Standard

Append one dated bullet per completed workflow, not one bullet per artifact.
Keep it near 80 words or less and list the main files plus outcome.

```markdown
## YYYY-MM-DD

- `decision-pipeline`: Updated `[[MSFT]]` and `[[MSFT Decision Memo YYYY-MM-DD]]`; action read `WAIT`.
```

## Git Completion Workflow

When durable project files change:

1. Inspect `git status --short` and preserve unrelated user changes.
2. Run relevant lightweight verification.
3. Stage only files in the completed prompt's scope.
4. Commit with a concise message. Do not create empty commits.
5. Report configuration or conflict blockers without touching unrelated work.
