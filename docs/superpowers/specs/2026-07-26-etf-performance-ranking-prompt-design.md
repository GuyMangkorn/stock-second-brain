# ETF Performance Ranking Prompt Design

## Goal

Add a reusable prompt to `wiki/entities/ETF Index.md` that ranks passive,
index-tracking equity ETFs by sustained historical performance while reducing
the influence of the latest two annual returns when those values are
AI-derived. The output must select 10 U.S. ETFs and 5 non-U.S. ETFs diversified
across distinct primary regions.

## Data Contract

- Use the common complete-calendar window `2016-2025`.
- Compare `NAV Total Return` only, including reinvested distributions and fund
  expenses. Do not mix NAV TR, market-price return, price return, YTD, partial
  years, or incompatible currencies/return bases in one ranking.
- Require all 10 annual observations. At least eight years must be official
  values or transparent calculations from official inputs.
- Permit no more than the latest two annual observations to be AI-derived.
- Preserve a source-confidence label for every annual observation:
  `official`, `official-derived`, `secondary`, or `AI-derived`.
- Use the ETF's verified underlying exposure and `primary region`; do not infer
  region from its listing exchange.

## Eligibility

Include only passive, index-tracking equity ETFs with a verified canonical
`entity_key: EXCHANGE:TICKER`. Exclude active, bond, commodity, multi-asset,
leveraged, inverse, and derivative-heavy funds. Exclude funds with incomplete
10-year coverage, more than two AI-derived annual rows, an unresolved return
basis, or a material strategy/index break that prevents a continuous
like-for-like record.

## Scoring

Calculate a `Total Score` from 0 to 100:

1. `Weighted annual TR percentile` — 60 points. Convert each eligible ETF's
   annual NAV TR into a percentile rank against the eligible universe for the
   same year. Apply source-confidence weights of `1.00` for official, `0.80`
   for official-derived, `0.50` for secondary, and `0.25` for AI-derived
   observations. Normalize by the sum of applicable confidence weights before
   scaling this component to 60 points.
2. `Consistency` — 25 points. Award 15 points from the ratio of positive years
   across 2016-2025 and 10 points from the longest consecutive positive-year
   streak relative to the 10-year window.
3. `Downside stability` — 15 points. Award 10 points from the cross-sectional
   percentile rank of each ETF's worst annual NAV TR, where a less-negative
   result scores higher, and 5 points from inverse annual-return volatility,
   where lower standard deviation scores higher.

Display component scores, the final score, the source-confidence mix, the
positive-year count, longest positive streak, worst year, and annual
volatility. Break ties by higher official-data coverage, then higher
Consistency score, then higher Downside stability score, then ticker
alphabetically.

## Selection

- `USA Top 10`: rank ETFs whose verified `primary region` is `USA` and select
  the 10 highest scores.
- `Non-U.S. Regional Top 5`: rank all ETFs whose `primary region` is not `USA`
  in one common pool. Keep only the highest-scoring ETF from each distinct
  primary region, then select the five highest-scoring regional winners.
- Do not use the exchange location to classify a U.S.-listed ETF as U.S. when
  its underlying exposure belongs to another region.

## Prompt Output

The prompt must request:

- a methodology and eligibility summary;
- one `USA Top 10` ranking table;
- one `Non-U.S. Regional Top 5` ranking table with one ETF per region;
- excluded candidates and the exact exclusion reason;
- a data-quality note identifying AI-derived annual rows and showing their
  reduced `0.25` confidence weight;
- formulas and enough intermediate values to reproduce every score;
- Thai-first narrative with English metric names and source links near the
  supported figures.

The ranking is a performance screen, not a recommendation or a claim of
personal portfolio fit.

## Validation

Confirm that every selected ETF has 10 complete annual NAV TR observations,
that the source-confidence weights and component totals reproduce the final
score, that exactly 10 USA ETFs and 5 distinct non-U.S. regions are selected,
and that every referenced ETF page and region wikilink resolves.
