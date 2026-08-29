---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KWEB
input_ticker: KWEB
ticker: KWEB
exchange: NYSE Arca
fund: KraneShares CSI China Internet ETF
tracked_index: CSI Overseas China Internet Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
annual_performance_as_of: 2025-12-31
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
nav_as_of: 2026-08-28
market_price_as_of: 2026-08-28
distribution_as_of: 2025-12-23
fund_facts_as_of: 2026-08-28
risk_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/KWEB
  - geography/China
  - theme/china-internet
---

# KWEB Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

`KWEB` คือ KraneShares CSI China Internet ETF, canonical listing
`NYSE Arca:KWEB`. Latest official KraneShares July month-end capture reports
NAV TR YTD `-17.66%`, 1Y `-15.45%`, 3Y `-0.04%`, 5Y `-7.75%` และ rolling 10Y
`+0.22%` ณ 31 ก.ค. 2026. Current official NAV `US$26.30`, market price
`US$26.32` และ net assets `US$5.19B` ณ 28 ส.ค. 2026. Complete calendar-year
rows 2016-2025 ยังเป็น secondary dividend-reinvested market-price proxy `*`;
proxy cumulative `12.19%` และ 2021-2025 CAGR `-11.89%*` จึงไม่ใช้แทน official
NAV rolling return.

## Performance check

- `entity_key: NYSE Arca:KWEB`; KraneShares ระบุว่า KWEB trades on the NYSE under ticker `KWEB`; canonical vault key ใช้ `NYSE Arca` ตาม established exchange-qualified page convention. CUSIP `500767306`, ISIN `US5007673065`, inception `2013-07-31`, distribution frequency `Annual`.
- Classification: `passive-index-tracking`; กองทุนมุ่งติดตาม `CSI Overseas China Internet Index` และให้ exposure แก่ Chinese internet/e-commerce/technology companies.
- Metric: official `NAV Total Return` รวม dividends/capital-gains distributions ที่ reinvested และหัก fund expenses; market-price return ถูกเก็บแยก. Annual rows ในตารางเป็น secondary dividend-reinvested market-price proxy `*`.
- Common reference benchmark: `S&P 500 Total Return` (USD, dividends reinvested); เป็น reference เท่านั้น ไม่ใช่ tracked index ของ KWEB.
- Official rolling 10-year field as of `2026-07-31`: NAV `0.22%`, closing price `0.29%`, underlying index `0.20%` annualized. Raw NAV endpoints ไม่เปิดเผย.
- Latest official daily capture as of `2026-08-28`: NAV `US$26.30`, market price `US$26.32`, premium/discount `US$0.02`, 30-day median bid/ask spread `0.04%` as of 2026-08-27.
- Fund details as of `2026-08-28`: net assets `US$5,193,762,658`, shares outstanding `197,500,000`, total annual fund operating expense `0.69%`, underlying index `CSI Overseas China Internet Index`.

### Official July 2026 standardized returns

| Return basis | 1M | 3M | 6M | YTD | Since inception |
|---|---:|---:|---:|---:|---:|
| NAV | 15.90% | -0.14% | -21.20% | -17.66% | 44.81% |
| Closing price | 16.43% | -0.97% | -19.47% | -16.33% | 46.20% |
| CSI Overseas China Internet Index | 15.91% | -0.27% | -21.67% | -18.18% | 45.05% |

### Official rolling annualized returns

| Period | NAV | Closing price | Underlying index |
|---|---:|---:|---:|
| 1 Year | -15.45% | -14.76% | -15.89% |
| 3 Years | -0.04% | -0.20% | -0.65% |
| 5 Years | -7.75% | -7.50% | -7.97% |
| 10 Years | 0.22% | 0.29% | 0.20% |
| Since inception | 2.89% | 2.96% | 2.90% |

All official tables above are as of `2026-07-31`; returns include reinvested
distributions where applicable and are not predictions.

### Secondary annual total-return context

| Year | KWEB total-return proxy* (USD; not official NAV) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016 | -8.54% | 11.96% |
| 2017 | 69.73% | 21.83% |
| 2018 | -33.80% | -4.38% |
| 2019 | 29.92% | 31.49% |
| 2020 | 58.23% | 18.40% |
| 2021 | -49.01% | 28.71% |
| 2022 | -17.24% | -18.11% |
| 2023 | -9.06% | 26.29% |
| 2024 | 12.01% | 25.02% |
| 2025 | 23.55% | 17.88% |

The annual KWEB series is a secondary dividend-reinvested total-return proxy;
it is not issuer-published NAV TR and is not used for strict cross-ETF ranking.
The S&P 500 rows use the cached USD total-return convention as of 2025-12-31.

## Window calculations and tracking context

- Proxy 2016-2025 compounds to `12.19%*` / rounded-input CAGR `1.16%*`; up/down years are `5 / 5`; best is 2017 `+69.73%*`; worst is 2021 `-49.01%*`.
- Proxy 2021-2025 compounds to `-46.89%*` / rounded-input CAGR `-11.89%*`; up/down years are `2 / 3`. Cached S&P 500 TR compounds to `96.17%` / CAGR `14.43%` over the same window; this is a common reference, not manager-skill evidence.
- Official NAV minus linked index tracking observations are YTD `+0.52 pp`, 1Y `+0.44 pp`, 3Y `+0.61 pp`, 5Y `+0.22 pp`, 10Y `+0.02 pp`, and since inception `-0.01 pp`. These are implementation/expense observations, not alpha.
- Official rolling 10Y NAV TR `0.22%` annualized is kept separate from the secondary 2021-2025 proxy CAGR `-11.89%*`; the periods and return bases differ.
- Reconciliation: the prior page used official June quarter-end NAV TR `-28.96%` and rolling 10Y `-0.85%`; the newer official July month-end capture is `-17.66%` YTD and `0.22%` rolling 10Y. The current page uses the newer July performance window and separately records the Aug-28 NAV/price snapshot.

## Risk read-through

The official Aug-28 holdings snapshot shows the largest positions as Tencent
`10.23%`, Alibaba `8.58%`, PDD `8.38%`, Meituan `7.11%`, and NetEase `6.20%`;
the top five sum to `40.50%`. Listed-location exposure is Hong Kong `76.9%`,
US ADRs with no secondary HK listing `12.2%`, and US ADRs with a secondary HK
listing `10.8%`. This creates high sensitivity to China policy, consumer and
internet demand, valuation, geopolitical/US-China relations, HKD/USD and
underlying-market liquidity.

Secondary Total Real Returns data ending 28 ส.ค. 2026 reports current drawdown
`-69.56%` from the 17 ก.พ. 2021 peak and worst drawdown `-80.92%` to 24 ต.ค.
2022. These are secondary adjusted/market-price proxy statistics; official
daily NAV drawdown and recovery series `ไม่พบข้อมูลที่ยืนยันได้`. The official
current market-price/NAV gap is only `US$0.02` (premium/discount shown by the
issuer), so no current evidence indicates a material ETF-specific dislocation.

The card ticker `KWEB` is resolved to the US-listed fund above. The distinct
UCITS share class `LSE:KWEB` / alias `KRANF` has ISIN `IE00BFXR7892` and remains
on [[ETF_LSE_KWEB Performance]]; its rows are not mixed into this page.

## Sources

- [KraneShares KWEB product page](https://kraneshares.com/etf/kweb/) — official US identity, NYSE ticker, index, fee, NAV/market price/premium-discount, standardized performance, fund facts and holdings; current captures as of 2026-07-31 and 2026-08-28 where stated.
- [KraneShares KWEB factsheet](https://kraneshares.com/resources/factsheet/kweb_factsheet.pdf) — official return-basis and fund-document cross-reference.
- [Total Real Returns KWEB](https://totalrealreturns.com/n/KWEB) — secondary dividend-reinvested annual history, current YTD and drawdown proxy; data ending 2026-08-28.
- [Stock Analysis KWEB history](https://stockanalysis.com/etf/kweb/history/) — secondary market-price history cross-check.
- [KraneShares KWEB UCITS page](https://kraneshares.eu/etf/kwebln/) — distinct LSE USD UCITS identity/ISIN used for ticker disambiguation.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
