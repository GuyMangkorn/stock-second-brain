# Stock Second Brain Agent Rules

This project is an Obsidian-native public-equity and equity-ETF research second
brain. Maintain durable, source-backed investment knowledge without turning
every question into a file-writing workflow.

## Mission And Ownership

- `raw/imports/`: source notes, filing extracts, transcripts, and raw evidence.
- `raw/financials/`: normalized company financial facts and ratios.
- `raw/funds/`: normalized passive equity ETF facts, holdings, and methodology.
- `wiki/entities/`: thin living company and exchange-qualified ETF hubs.
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

## ETF Performance Pre-Save Verification Gate

This gate applies only to a research-bearing invocation of the
`check-etf-performance` skill that will write durable ETF performance outputs.
The evidence packet must identify `workflow: check-etf-performance`. A
read-only `mode: chat` response and every workflow that does not use this skill
must not dispatch `source_verifier`.

Before writing a durable performance page, dated source batch, region/index
update, or log entry for this workflow, the main agent must complete the
research draft and prepare an evidence packet containing the ETF identity and
exchange, return basis, benchmark, candidate performance claims, periods,
units, currencies, metric definitions, as-of dates, calculations, source
URLs/paths, unresolved gaps, and the complete proposed contents of every file
it plans to write. Apply the review route selected by `execution_profile`:

- For `interactive-delegated` (including an omitted profile), dispatch the
  project-scoped `source_verifier` sub-agent from
  `.codex/agents/source-verifier.toml` and wait for its structured review.
- For `scheduled-inline`, do not dispatch `source_verifier`, a research worker,
  reviewer, or any other sub-agent. Perform the same complete checklist locally
  in the current top-level context before writing, and record these exact lines
  in the dated source batch:

  ```text
  verification_mode: scheduled-local
  reviewer_dispatch: not-attempted-by-design
  ```

- `PASS` permits the main agent to write the planned ETF performance files.
- `CHANGES_REQUIRED` for `High` or `Medium` findings blocks all writes; the
  main agent must correct or narrow-refresh the evidence and rerun the same
  profile-specific review route before saving.
- `WARNING` for `Low` findings pauses the workflow and requires explicit user
  confirmation before saving; preserve the warning or gap in the owning
  artifact when relevant.
- The reviewer is read-only and must not edit evidence, performance pages,
  source batches, indexes, regions, or logs. The main agent remains the sole
  durable-file writer.
- Under `interactive-delegated`, if the sub-agent is unavailable, the main
  agent must perform the same checklist locally, disclose the fallback in the
  dated source batch, and apply the same blocking and confirmation rules.
- Under `scheduled-inline`, local review is required by design and must not be
  described as a reviewer-unavailability fallback.

## Source Priority

1. SEC and official company filings
2. Earnings transcripts and call materials
3. Financial statements and metrics
4. News and web research
5. X/Twitter and market chatter as lower-priority context

Prefer Investor Relations for discovery and the underlying filing, release,
transcript, or data table as evidence.

For ETFs prefer official issuer prospectus/product/factsheet and holdings,
official index methodology, then regulator/exchange material. Keep separate
as-of dates for holdings, NAV/price, AUM, distributions, performance, and
methodology.

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

### etf-research

Use `.codex/skills/official-source-etf-research/SKILL.md` for passive,
index-tracking equity ETF research, comparison, refresh, or decision handoff.
Resolve `entity_key: EXCHANGE:TICKER`; do not route an ETF through company
results, financial ingest, stock research, or DCF stages.

### etf-performance

Use `check-etf-performance` for passive index-tracking and active long-only
equity ETFs. Classify active funds from official strategy documents and assess
management evidence against an official strategy-aligned benchmark; keep raw
Total Return separate from excess return and risk-adjusted evidence.
Explicit `[Skills] TICKER` or `$check-etf-performance` invocation defaults to
`lean` and saves the performance page plus dated source batch; an implicit
natural-language performance question defaults to read-only `chat`. Explicit
`mode: chat` overrides the save default.

For active long-only equity ETFs, expose management mode, active-process
subtype, management benchmark, track-record maturity, management evidence, and
risk-evidence status. Keep `S&P 500 Total Return` as a common reference rather
than evidence of manager skill unless it is also the official
strategy-appropriate comparator. Do not call arithmetic excess return `alpha`.

For S&P 500 Total Return comparisons covering complete calendar years
`2016-2025`, reuse the skill's cached S&P 500 TR convention without a new web
search. Copy the matching cached rows into the ETF performance page and record
the cache's original URLs, USD total-return basis, window, and as-of date in the
dated source batch. Freshly verify current YTD, rolling date-to-date windows,
years outside `2016-2025`, or a newly completed calendar year.

For ETF region navigation, assign each performance page one primary region from
its underlying exposure. Keep region pages under
`wiki/analysis/comparisons/` and use `wiki/analysis/performance/` pages as the
numeric source of truth. When a new region section is needed and no matching
`<Region> ETF.md` exists, create that region file before completing the update;
do not place it under `performance/` or create a duplicate performance page.
Every region page must be a static navigation summary with wikilinks to the
affected ETF pages, link back to `[[ETF Region Index]]`, and link forward to
`[[ETF Performance Index]]`. Add the new region to `ETF Region Index.md` and
the `Browse by region` links in `ETF Performance Index.md`. Keep the graph
connected with the breadcrumb `[[ETF Region Index]] → [[<Region> ETF]] →
[[ETF Performance Index]]` on each affected ETF page, add the canonical
`geography/<Region-Slug>` tag without removing legacy tags, and verify that every
ETF appears in exactly one primary region and every wikilink resolves.

### valuation

Use `.codex/skills/dcf-valuation/SKILL.md`. Freshly verify market data and use
source-backed FCF, cash, debt, shares, and guidance. Create a valuation memo
only when a calculation succeeds or the user explicitly asks for a gap memo.

### decision-pipeline

Use `.codex/skills/stock-decision-pipeline/SKILL.md`. Read existing vault
context first, use the lightest sufficient flow, update the entity once, and do
not create a valuation-gap memo when P11 cannot calculate a valuation.
For `instrument_type: ETF`, use ETF research -> ETF decision and bypass
P1/P4/P6/P7/P11.

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
raw/imports/ETF_EXCHANGE_TICKER_fund_source_YYYY-MM-DD.md
raw/imports/ETF_performance_sources_YYYY-MM-DD.md
raw/financials/TICKER_fundamentals.md
raw/financials/TICKER_fundamentals.json
raw/funds/ETF_EXCHANGE_TICKER_fund_facts.md
wiki/entities/TICKER.md
wiki/entities/ETF_EXCHANGE_TICKER.md
wiki/analysis/earnings/TICKER Earnings Transcript Digest YYYY-MM-DD.md
wiki/analysis/catalysts/TICKER Catalyst Update YYYY-MM-DD.md
wiki/analysis/catalysts/TICKER Market Move YYYY-MM-DD.md
wiki/analysis/comparisons/Theme Memo Title YYYY-MM-DD.md
wiki/analysis/valuations/TICKER DCF Valuation YYYY-MM-DD.md
wiki/analysis/decisions/TICKER Decision Memo YYYY-MM-DD.md
wiki/analysis/decisions/ETF_EXCHANGE_TICKER Decision Memo YYYY-MM-DD.md
wiki/analysis/sentiment/TICKER X Sentiment YYYY-MM-DD.md
wiki/analysis/sentiment/ETF_EXCHANGE_TICKER X Sentiment YYYY-MM-DD.md
wiki/analysis/performance/ETF_EXCHANGE_TICKER Performance.md
wiki/analysis/audits/Source Integrity Audit YYYY-MM-DD.md
wiki/overview/themes/THEME.md
wiki/overview/macro/TOPIC.md
```

## Entity Page Standard

Use the thin hub in `wiki/reference/entity-template.md`: compact snapshot,
source/report links, business model, thesis/key debate, risks, catalysts,
valuation watch items, follow-up, and unresolved ticker-level gaps. Link to
normalized tables and charts instead of copying them.

For ETFs use `wiki/reference/etf-entity-template.md`. Keep holdings and metrics
in `raw/funds/`; use price/NAV, look-through multiples, yield, expense drag,
tracking, and peers rather than corporate DCF. Without user-provided portfolio
holdings, state fund suitability only and do not claim portfolio fit.

## Missing-Data Ownership

- source note: extraction gaps
- fundamentals: normalization and period-compatibility gaps
- fund facts: ETF normalization, holdings-snapshot, and methodology gaps
- entity: unresolved ticker-level gaps
- valuation: valuation blockers only
- decision: action-relevant gaps only

ETF research v1 (`official-source-etf-research` and its decision/deep-dive
routes) supports passive, index-tracking equity ETFs only. The
`check-etf-performance` workflow additionally supports active long-only equity
ETFs. Return `unsupported ETF type` for bond, commodity, currency, multi-asset,
leveraged, inverse, defined-outcome, covered-call, option-income, single-stock
option, or derivative-heavy funds.

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

## Agent skills

### Issue tracker

Issues and specs live as Markdown files under `.scratch/<feature-slug>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five canonical labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: read root `CONTEXT.md` and relevant ADRs in `docs/adr/`. See `docs/agents/domain.md`.
