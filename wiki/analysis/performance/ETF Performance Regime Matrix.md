---
type: etf-performance-regime-matrix
scope: pilot
updated: 2026-07-12
common_window: 2021-2025
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - analysis/regime
  - analysis/classification
---

# ETF Performance Regime Matrix

## Purpose

Matrix นี้แยก `Structural classification` ออกจาก `Behavioral classification`
เพื่อไม่ให้ชื่อกองหรือ dividend label ถูกใช้แทนพฤติกรรมจริง. ตัวเลข annual
return เป็น official NAV total return ใน common window 2021-2025; COVID drawdown
และ monthly behavior เป็น secondary dividend-adjusted context.

## Common Window Comparison

| ETF | Structural classification | 2021 | 2022 | 2023 | 2024 | 2025 | Cumulative | CAGR | Positive years | Negative years |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [[ETF_AMEX_DGRO]] | U.S. dividend growth / broad quality | 26.56% | -7.85% | 10.43% | 16.61% | 15.74% | 73.82% | 11.69% | 4 | 1 |
| [[ETF_AMEX_VIG]] | U.S. dividend growth / quality | 23.64% | -9.79% | 14.46% | 17.02% | 14.18% | 70.58% | 11.27% | 4 | 1 |
| [[ETF_NASDAQ_VIGI]] | international dividend growth | 12.42% | -16.71% | 16.16% | 2.62% | 16.89% | 30.47% | 5.46% | 4 | 1 |
| [[ETF_AMEX_DIVI]] | developed ex-North America dividend tilt | 17.22% | -1.74% | 19.23% | 2.36% | 34.51% | 89.08% | 13.59% | 4 | 1 |

## Behavioral Matrix

| ETF | COVID max drawdown | Max drawdown / recovery | Avg monthly return | Positive months | 2022 read | 2025 read |
|---|---:|---:|---:|---:|---|---|
| [[ETF_AMEX_DGRO]] | -35.10% | -35.10% / 161 sessions | 1.05% | 67% | downside contained versus international dividend growth, but still equity risk | strong U.S. quality participation |
| [[ETF_AMEX_VIG]] | -31.72% | -46.81% / 491 sessions over full history | 0.88% | 67% | defensive relative to broad equity, but rate-sensitive | steady quality participation |
| [[ETF_NASDAQ_VIGI]] | -31.01% | -31.01% / 114 sessions | 0.77% | 66% | weakest common-window year; FX/country/rate mix amplified losses | recovered with international risk-on/value support |
| [[ETF_AMEX_DIVI]] | -27.76% | -27.76% / 207 sessions | 0.92% | 64% | near-flat year; value/financials/ex-North-America exposure likely offset part of U.S. duration shock | largest rebound, consistent with international/value/FX tailwinds; attribution still needs holdings-level check |

## Regime Notes

### 2022 Inflation / Rate-Hike Shock

**Confirmed event:** the Federal Reserve's December 2022 statement said inflation
remained elevated, cited pandemic supply-demand imbalances, food and energy
prices and the Russia-Ukraine war, and raised the federal-funds target range to
4.25%-4.50% after 4.25 percentage points of increases during 2022. See the
[FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm).

**Observed performance:** VIGI fell 16.71%, while DGRO, VIG and DIVI fell 7.85%,
9.79% and 1.74%, respectively. **Probable driver:** U.S. dividend-growth funds
had a quality/large-cap cushion, while international dividend growth carried
more FX, country and regional cyclicality. DIVI's financials/value tilt may have
offset some duration pressure, but this remains a composition hypothesis until
holdings-level attribution is added.

### 2020 COVID Crash

**Confirmed event:** the Federal Reserve described the COVID outbreak as harming
communities, disrupting economic activity and significantly affecting global
financial conditions; it cut rates and introduced emergency support. See the
[March 2020 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm)
and the [Federal Reserve financial-stability overview](https://www.federalreserve.gov/publications/2020-may-financial-stability-report-overview.htm).

**Observed secondary drawdowns:** DIVI -27.76%, VIGI -31.01%, VIG -31.72% and
DGRO -35.10%. The cross-sectional result suggests DIVI had the shallowest pilot
drawdown, but the series is dividend-adjusted market data rather than one
issuer-standardized NAV history.

### 2025 Risk-On / International Rebound

**Observed performance:** DIVI +34.51%, VIGI +16.89%, DGRO +15.74% and VIG
+14.18%. **Probable driver:** international value, financials, currency and
regional leadership helped DIVI, while U.S. quality continued to compound at a
steadier pace. This is a hypothesis for the next attribution pass, not a claim
that DIVI will lead every risk-on market.

## Portfolio-Construction Use

This matrix can support an instrument-level shortlist:

- `U.S. quality / dividend growth`: DGRO, VIG
- `International dividend growth`: VIGI
- `International value / dividend tilt`: DIVI

It does not yet prove that holding all four creates diversification. A portfolio
fit conclusion requires the user's actual holdings, compatible dates and overlap
analysis.

## Sources

- [[ETF_AMEX_DGRO_performance_source_2026-07-12]]
- [[ETF_AMEX_VIG_performance_source_2026-07-12]]
- [[ETF_NASDAQ_VIGI_performance_source_2026-07-12]]
- [[ETF_AMEX_DIVI_performance_source_2026-07-12]]
- [Federal Reserve 2022 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm)
- [Federal Reserve 2020 FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm)
