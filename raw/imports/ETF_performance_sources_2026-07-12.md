---
type: source-note
source_profile: etf-performance-batch
accessed: 2026-07-12
canonical_output: wiki/analysis/performance/ETF_EXCHANGE_TICKER Performance.md
tags:
  - source/etf
  - source/performance
---

# ETF Performance Sources - 2026-07-12

## Source Map

| ETF | Official source | Secondary context |
|---|---|---|
| `AMEX:DGRO` | [iShares product page](https://www.ishares.com/us/products/264623/ishares-core-dividend-growth-etf), [factsheet](https://www.ishares.com/us/literature/fact-sheet/dgro-ishares-core-dividend-growth-etf-fund-fact-sheet-en-us.pdf) | [PortfoliosLab](https://portfolioslab.com/symbol/DGRO), [Total Real Returns](https://totalrealreturns.com/n/DGRO%2CSPY) |
| `AMEX:VIG` | [Vanguard product page](https://investor.vanguard.com/investment-products/etfs/profile/vig) | [PortfoliosLab](https://portfolioslab.com/symbol/VIG), [Total Real Returns](https://totalrealreturns.com/n/VIG) |
| `NASDAQ:VIGI` | [Vanguard product page](https://investor.vanguard.com/investment-products/etfs/profile/vigi) | [PortfoliosLab](https://portfolioslab.com/symbol/VIGI), [Total Real Returns](https://totalrealreturns.com/n/VIGI) |
| `AMEX:DIVI` | [Franklin factsheet](https://www.franklintempleton.com/forms-literature/download/DIVI-FF), [fund source note](ETF_AMEX_DIVI_fund_source_2026-07-12.md) | [PortfoliosLab](https://portfolioslab.com/symbol/DIVI) |
| `NYSE Arca:DTD` (`AMEX:DTD` input alias) | [WisdomTree product page](https://www.wisdomtree.com/us/products/equity/dtd), [factsheet](https://www.wisdomtree.com/us/media/wisdomtree-factsheet-dtd-1005), [Q1-2026 presentation](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/presentations/equity/dtd_presentation.pdf), [WTDI index page](https://www.wisdomtree.com/us/indexes/wtdi) | [PortfoliosLab](https://portfolioslab.com/symbol/DTD) |

## DTD source details

| Source | Role | As-of | Durable use |
|---|---|---|---|
| WisdomTree product page | Identity, NYSE Arca listing, fee, NAV/market price, current performance and distributions | 2026-07-10 for product/NAV/price; 2026-06-30 for performance | Canonical current fund facts and NAV Total Return |
| WisdomTree DTD Q1-2026 presentation | Calendar-year NAV returns, MSCI USA IMI comparison, standard deviation | 2026-03-31 | Official annual table for 2016-2025 |
| WisdomTree DTD factsheet | Inception, expense ratio, NAV/market-price return disclosure, benchmark transition note | 2026-03-31 | Return-definition and fund metadata cross-check |
| WisdomTree U.S. Dividend Index | WTDI methodology and index facts | 2026-07-06 | Tracked-index identity and methodology |
| PortfoliosLab | Maximum drawdown and recovery | secondary; page accessed 2026-07-12 | Risk context only; not a replacement for official NAV history |

## Scope

- Canonical metric is `NAV Total Return` in USD, with distributions reinvested
  and fund expenses included when the issuer reports it.
- For DTD, the latest completed-year base is official 2025 NAV Total Return
  `+14.22%`; this is after fund operating expenses reflected in NAV. The `0.28%`
  expense ratio is not subtracted again from that return. Current 2026 YTD NAV
  Total Return is `+10.80%` as of 2026-06-30.
- Official annual tables are used for complete-year ranking. `*` marks a
  secondary dividend-reinvested proxy; `†` marks an official inception-year
  partial period.
- Current YTD, monthly behavior and drawdowns are partial or secondary context;
  each page keeps its own as-of date.
- DGRO official annual coverage in this pass begins at 2021; VIG begins at 2011;
  VIGI complete-year official coverage begins at 2017; DIVI begins at 2017.
- DTD official complete-year coverage is 2016-2025; the current WTDI underlying
  index is shown for rolling/current periods, while the saved annual comparison
  uses MSCI USA IMI, the issuer's broad-based benchmark in the 2026 presentation.

## VIGI Capture Detail

- Official Vanguard annual NAV total returns and benchmark comparison: product
  page, annual table as of 2025-12-31; 2016 is an inception-year partial.
- Official current performance: advisor product page reports VIGI NAV YTD
  `+4.64%` as of 2026-07-08 and 1-year NAV return `+6.06%` as of 2026-06-30.
- Official fund factsheet: `F4415.pdf`, as of 2026-03-31; benchmark is the S&P
  Global Ex-U.S. Dividend Growers Index (USD) NTR, expense ratio `0.07%`,
  quarterly distributions, and 3-year monthly standard deviation `12.01%`.
- Official benchmark methodology and return definitions: S&P Dividend Growers
  Index Series methodology; the benchmark NTR reinvests regular dividends after
  applicable withholding taxes.
- Secondary risk context: PortfoliosLab last updated 2026-07-09; maximum
  drawdown `-31.01%` on 2020-03-23 and recovery `114` trading sessions. This is
  adjusted-price total-return context, not an official NAV series.

## Gaps

- A durable issuer monthly NAV observation series is not captured for this pass.
- Secondary monthly and drawdown figures must not replace official NAV returns.
- Holdings-level attribution for 2022 and 2025 remains a follow-up, not a fact.
- DTD's annual WTDI total-return series was not captured; do not treat MSCI USA IMI
  as the fund's tracked index. The page labels both roles explicitly.
- Vanguard current benchmark YTD is not disclosed in the same current capture;
  no benchmark YTD is presented on the VIGI performance page.
- Current official price/NAV quote and distribution records were not needed for
  this performance save and remain separate from the NAV return ranking.
