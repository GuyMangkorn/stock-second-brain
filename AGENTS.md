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
- `wiki/analysis/` stores comparisons, decision memos, source audits, screener
  triage, and thesis updates.
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
- Save durable valuation work in `wiki/analysis/`.
- Update entity valuation watch items only when the valuation changes the thesis.

### sentiment

Use when the user asks for X/Twitter sentiment, public chatter, CT/fintwit, or
what people are saying about a stock/event.

Required behavior:

- Use `.codex/skills/x-research/SKILL.md`.
- Treat sentiment as context, not financial fact.
- Save durable sentiment work in `wiki/analysis/` when useful.

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
wiki/analysis/TICKER Memo Title YYYY-MM-DD.md
wiki/analysis/Theme Memo Title YYYY-MM-DD.md
wiki/analysis/TICKER DCF Valuation YYYY-MM-DD.md
wiki/analysis/TICKER X Sentiment YYYY-MM-DD.md
wiki/analysis/Source Integrity Audit YYYY-MM-DD.md
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
