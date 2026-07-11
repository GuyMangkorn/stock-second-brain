---
name: x-research
description: Use when the user asks what people are saying on X/Twitter, CT, fintwit, or public social media about a stock, ETF, sector, company, earnings event, or market narrative.
---

# X Research

## Source Position

Treat X as market context below filings, earnings materials, financial facts,
and reputable news. Independently verify any post that claims revenue, EPS,
guidance, valuation, insider activity, or filing facts.

## Default Mode

Use `chat`: define the time window, summarize themes in at most 400 words, and
write no files.

Use `lean` when the user asks to save or when source-backed sentiment materially
changes a durable follow-up. Save
`wiki/analysis/sentiment/TICKER X Sentiment YYYY-MM-DD.md`, or
`wiki/analysis/sentiment/ETF_EXCHANGE_TICKER X Sentiment YYYY-MM-DD.md` for an
ETF; update only entity follow-up, and append one workflow log bullet.

Chat sentiment may cover any ETF. Durable ETF output is limited to passive,
index-tracking equity ETFs. For bond, commodity, multi-asset, active,
leveraged, inverse, or derivative-heavy ETFs, stay in chat and do not create or
update ETF artifacts under the v1 contract.

## Workflow

1. Define a one-day, seven-day, or post-event window.
2. Search ticker/company/fund plus bullish, bearish, expert, and source-linked
   terms. For an ETF, resolve `EXCHANGE:TICKER` and separate fund commentary
   from claims about the index or underlying holdings.
3. Prefer traceable posts with reasoning or primary-source links.
4. Group by theme and separate retail chatter, expert commentary, news reaction,
   and independently verified posts.
5. Label overall sentiment `bullish`, `bearish`, `mixed`, or `neutral` with
   `low`, `medium`, or `high` confidence.
6. State sample bias, low volume, bot/spam, rumor, or event-noise limitations.

## Chat Recipe

- query/window summary
- up to three bullish and three bearish themes
- source-backed signals
- overall sentiment + confidence
- caveat and next confirmation

Quote sparingly and link posts. Do not treat virality as evidence.

## Durable Memo

Use query summary, theme groups, source-backed posts, overall sentiment,
caveats, and follow-up. Keep company facts in their owning files.
For ETFs, keep official fund facts in `raw/funds/` and use exchange-qualified
identity in durable filenames and links.

Stop when access is unavailable, results are too noisy, posts are untraceable,
or rumor cannot be separated from evidence.
