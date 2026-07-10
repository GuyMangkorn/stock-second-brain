---
name: x-research
description: Use when the user asks what people are saying on X/Twitter, CT, fintwit, or public social media about a stock, sector, company, earnings event, or market narrative.
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
`wiki/analysis/sentiment/TICKER X Sentiment YYYY-MM-DD.md`, update only entity
follow-up, and append one workflow log bullet.

## Workflow

1. Define a one-day, seven-day, or post-event window.
2. Search ticker/company plus bullish, bearish, expert, and source-linked terms.
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

Stop when access is unavailable, results are too noisy, posts are untraceable,
or rumor cannot be separated from evidence.
