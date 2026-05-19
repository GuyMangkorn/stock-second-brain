---
name: x-research
description: Research public X/Twitter sentiment for a stock, sector, company, or market event, saving it as lower-priority market context rather than durable company fact.
---

# X Research

Use this skill when the user asks what people are saying on X/Twitter, public
sentiment, CT, fintwit, market chatter, expert posts, or community reaction to a
stock, sector, earnings result, or market event.

This is adapted from Dexter's `x-research` skill, but in this vault sentiment is
treated as context, not a primary fact source.

## Language Standard

Follow `wiki/reference/output-contract.md`: summarize sentiment themes,
caveats, and follow-up in Thai, while keeping source labels, account handles,
tickers, links, and market/finance terms in English.

## Source Position

X/Twitter is below the normal source stack:

1. SEC filings and official company filings
2. Earnings transcripts and call materials
3. Financial statements and metrics
4. News and web research
5. X/Twitter sentiment and public market chatter

Do not use X posts as the source for revenue, EPS, valuation, guidance, segment
data, insider activity, or filing facts unless the post links to a primary
source that is independently checked.

## Research Loop

1. Define the time window, usually last 1 day, 7 days, or post-event window.
2. Build 3-5 targeted queries:
   - core ticker: `$TICKER` or company name
   - bullish signal: `bullish OR upside OR catalyst OR beat`
   - bearish signal: `risk OR miss OR overvalued OR concern`
   - expert signal: known analyst/investor accounts if relevant
   - source-backed signal: posts with links or screenshots
3. Prefer posts with links, primary-source references, or clear reasoning.
4. Group findings by theme, not by chronology.
5. Separate retail chatter, expert commentary, news reaction, and source-backed
   posts.
6. Save a sentiment memo only when the result is durable.

## Output File

Save durable sentiment work as:

```text
wiki/analysis/sentiment/TICKER X Sentiment YYYY-MM-DD.md
```

For sector or theme sentiment:

```text
wiki/analysis/sentiment/THEME X Sentiment YYYY-MM-DD.md
```

Append `log.md`.

## Memo Sections

- `# TICKER X Sentiment - YYYY-MM-DD`
- `## Query Summary`
- `## Bullish Themes`
- `## Bearish Themes`
- `## Neutral / Mixed Themes`
- `## Source-Backed Posts`
- `## Overall Sentiment`
- `## Caveats`
- `## Follow-Up`

## Output Rules

- Quote sparingly and link to posts when possible.
- Do not over-weight viral posts without evidence.
- Mark sentiment as `bullish`, `bearish`, `mixed`, or `neutral`.
- Include confidence: `low`, `medium`, or `high`.
- State why confidence is limited, such as sample bias, low volume, bot/spam
  risk, or event-driven noise.
- If sentiment changes thesis or follow-up items, update the entity page with a
  short note under `Follow-Up`, not as a financial fact.

## Stop Conditions

Stop and report gaps when:

- X/search access is unavailable
- query results are too noisy to summarize honestly
- posts cannot be linked or traced
- the topic is being driven by rumors with no source-backed confirmation
