# Stock Second Brain Agent Rules

This project is an Obsidian-native stock research second brain. The agent's job
is to maintain durable, source-backed investment knowledge in files, not just
answer in chat.

## Mission

Maintain a compounding research vault where:

- `raw/imports/` stores source notes, filing extracts, transcript digests, and
  source-backed raw inputs.
- `raw/financials/` stores normalized company financial facts.
- `wiki/entities/` stores one living company page per ticker.
- `wiki/analysis/` stores category folders for decisions, valuations,
  earnings, catalysts, comparisons, sentiment, and source audits.
- `wiki/overview/` stores portfolio, sector, theme, and dashboard notes.
- `index.md` stays useful as the main dashboard.
- `log.md` records every meaningful ingest or maintenance event.

## Source Integrity Rules

1. Source before writing. Collect the source fact first, then write the durable
   note.
2. Do not invent, smooth, backfill, or complete missing financial values.
3. Every durable number must have a URL, local path, filing reference, or shown
   calculation from sourced inputs.
4. Separate facts, calculations, assumptions, and judgment.
5. If a value cannot be verified, write `ไม่พบข้อมูลที่ยืนยันได้` or
   `not disclosed`.
6. If sources conflict, record the conflict and either choose the higher-quality
   source with explanation or keep both.
7. Prices, valuation multiples, analyst targets, news, laws, and current market
   data must be freshly checked before use.
8. During ingest, preserve the source's meaning. Do not add new factual claims
   unless separately sourced.

## Source Priority

Use the user's selected priority order:

1. SEC filings and official company filings
2. Earnings transcripts and call materials
3. Financial statements and metrics
4. News and web research
5. X/Twitter sentiment and market chatter only as lower-priority context.

Investor relations pages are preferred discovery surfaces when they host the
official filings, releases, presentations, transcripts, or data tables.

## Language Standard

Use a hybrid Thai/English research style for future durable outputs:

- Write narrative analysis, thesis, risks, catalysts, action reads, caveats, and
  final chat answers primarily in Thai.
- Keep standard headings, frontmatter keys, JSON keys, filenames, ticker names,
  source titles, table column labels, formulas, and metric names in English.
- Keep finance and valuation terms in English when translation could reduce
  precision or searchability, including `valuation`, `DCF`, `FCF`, `WACC`,
  `terminal growth`, `margin of safety`, `upside/downside`, `multiple`,
  `drawdown`, `net debt`, `free cash flow`, `capex`, and `guidance`.
- Preserve raw source meaning and quoted/source-derived wording in the source's
  original language. Translate or summarize only as analysis, not as a
  replacement for the source fact.
- Prefer one language per sentence where possible, with English finance terms
  embedded only when they carry the precise meaning.
- Do not translate durable field names so Obsidian search, links, and future
  automation remain stable.

## Git Completion Workflow

When an agent completes a user prompt that creates or modifies durable project
files, finish with a git commit before the final chat answer.

Required behavior:

- Inspect `git status --short` before staging so pre-existing user changes are
  visible.
- Stage only files changed for the completed prompt. Do not stage unrelated
  dirty files or user work that was already present.
- Run the relevant lightweight verification for the change when practical.
- Commit after the work is complete with a concise message that describes the
  delivered outcome, for example `docs: add git completion workflow`.
- If there are no file changes, or the prompt was read-only, do not create an
  empty commit; state that no commit was needed.
- If git commit fails because the repository is not configured or the working
  tree contains conflicting user changes, report the blocker clearly and leave
  the user's unrelated work untouched.

## Operating Modes

### latest-results

Use when the user asks for latest results, latest quarter, recent earnings, or
current official source discovery.

Required behavior:

- Use `.codex/skills/latest-results-web/SKILL.md`.
- Create a source note in `raw/imports/`.
- Hand off to `financial-facts-ingest` when the user asks to ingest.

### ingest

Use when the user asks to ingest a source file, filing excerpt, transcript,
financial table, Markdown note, or CSV.

Required behavior:

- Use `.codex/skills/financial-facts-ingest/SKILL.md`.
- Confirm the input exists.
- Normalize only verified source fields.
- Update `raw/financials/`, `wiki/entities/`, and `log.md`.

### research

Use when the user asks for a company deep dive, thesis update, earnings review,
or ticker analysis.

Required behavior:

- Use `.codex/skills/official-source-stock-research/SKILL.md`.
- Prefer official filings and transcripts before secondary context.
- Update the entity page when the result is durable.

### valuation

Use when the user asks for fair value, intrinsic value, DCF, price target,
upside/downside, undervalued, or overvalued analysis.

Required behavior:

- Use `.codex/skills/dcf-valuation/SKILL.md`.
- Verify current price and market data freshly.
- Use source-backed FCF, cash, debt, shares, and guidance.
- Save durable valuation work in `wiki/analysis/valuations/`.
- Update entity valuation watch items only when the valuation changes the thesis.

### decision-pipeline

Use when the user asks to chain P1 -> P4 -> P6 -> P11 -> P13, run a
decision-grade workflow from a ticker, or refresh a decision memo with the
current stock price.

Required behavior:

- Use `.codex/skills/stock-decision-pipeline/SKILL.md`.
- For new tickers, run source discovery before ingest: P1 -> P4 -> P6 -> P11
  -> P13.
- For existing tickers, read vault context first and choose the lightest
  sufficient flow: P13 only, P11 -> P13, P7 -> P11 -> P13, or P1 -> P4 -> P7
  -> P11 -> P13 when new results exist.
- Freshly verify current price and market data before decision or valuation
  work.
- Save durable decision memos in `wiki/analysis/decisions/` and append
  `log.md`.

### sentiment

Use when the user asks for X/Twitter sentiment, public chatter, CT/fintwit, or
what people are saying about a stock/event.

Required behavior:

- Use `.codex/skills/x-research/SKILL.md`.
- Treat sentiment as context, not financial fact.
- Save durable sentiment work in `wiki/analysis/sentiment/` when useful.

### query

Use when the user asks a question against the vault.

Required behavior:

- Read `index.md` first.
- Read relevant entity, financial, and analysis notes.
- Answer from vault context first.
- Offer or perform a save/update when the insight is durable and the user asks
  for it.

### lint

Use to health-check the vault.

Required behavior:

- Use `.codex/skills/source-integrity-audit/SKILL.md`.

Check for:

- uncited numbers
- source conflicts
- stale thesis notes
- orphan pages
- entity pages without normalized financial facts
- raw source notes not linked to entities
- duplicated ticker pages
- unresolved follow-up tasks

## Filename Rules

Source notes:

```text
raw/imports/TICKER_source_kind_YYYY-MM-DD.md
raw/imports/TICKER_latest_results_source.md
```

Financial facts:

```text
raw/financials/TICKER_fundamentals.md
raw/financials/TICKER_fundamentals.json
```

Entity pages:

```text
wiki/entities/TICKER.md
```

Analysis memos:

```text
wiki/analysis/earnings/TICKER Earnings Transcript Digest YYYY-MM-DD.md
wiki/analysis/catalysts/TICKER Catalyst Update YYYY-MM-DD.md
wiki/analysis/comparisons/Theme Memo Title YYYY-MM-DD.md
wiki/analysis/comparisons/Screener Triage YYYY-MM-DD.md
wiki/analysis/valuations/TICKER DCF Valuation YYYY-MM-DD.md
wiki/analysis/decisions/TICKER Decision Memo YYYY-MM-DD.md
wiki/analysis/sentiment/TICKER X Sentiment YYYY-MM-DD.md
wiki/analysis/audits/Source Integrity Audit YYYY-MM-DD.md
```

## Entity Page Standard

Each ticker page should include:

- `# TICKER - Company Name`
- `## Snapshot`
- `## Source Map`
- `## Business Model`
- `## Segments / Revenue Mix`
- `## Financial Facts`
- `## Charts`
- `## Transcript / Management Commentary`
- `## Thesis`
- `## Risks`
- `## Catalysts`
- `## Valuation Watch Items`
- `## Reports / Source Notes`
- `## Follow-Up`
- `## Missing / Unverified Data`

## Log Standard

Append a dated entry to `log.md` for every ingest, entity update, analysis memo,
source audit, or structural maintenance pass.

Use:

```markdown
## YYYY-MM-DD

- `ingest`: Created `raw/financials/MSFT_fundamentals.md`, updated `[[MSFT]]`.
```
