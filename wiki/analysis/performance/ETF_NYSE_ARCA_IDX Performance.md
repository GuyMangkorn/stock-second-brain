---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IDX
ticker: IDX
exchange: NYSE Arca
fund: VanEck Indonesia Index ETF
tracked_index: MVIS Indonesia Index (MVIDXTR)
benchmark: S&P 500 Total Return
updated: 2026-07-19
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-16
price_nav_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-19.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IDX
  - geography/Indonesia
  - style/emerging-market
---

# IDX Performance

## Bottom line

`IDX` ในที่นี้คือ `VanEck Indonesia Index ETF` ที่จดทะเบียนบน `NYSE Arca` ไม่ใช่
ดัชนี IDX Composite ของตลาดหุ้นอินโดนีเซีย. Official NAV YTD อยู่ที่ `-36.18%`
ณ 16 ก.ค. 2026; rolling 1Y/3Y/5Y/10Y NAV annualized อยู่ที่ `-30.93%` /
`-15.82%` / `-8.96%` / `-5.49%` ณ 30 มิ.ย. 2026. จึงมีโอกาสเกิด tactical
rebound จากภาวะ oversold แต่ยังไม่มีหลักฐานยืนยันการกลับตัวเป็นขาขึ้นแบบยั่งยืน.

## Performance check

- `entity_key: NYSE Arca:IDX`
- Fund: VanEck Indonesia Index ETF; inception `15 ม.ค. 2009`; passive,
  index-tracking equity ETF; gross/net expense ratio `0.86%` / `0.57%`
  (net cap ถึงอย่างน้อย 1 พ.ค. 2027)
- Metric: `NAV Total Return` รวม distributions ที่ reinvested และหัก fund expenses
- Tracked index (issuer benchmark): `MVIS Indonesia Index (MVIDXTR)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ IDX)
- 10-year window: `2016-06-30` ถึง `2026-06-30` (rolling; issuer ไม่เปิด raw
  start/end TR values)
- 10-year NAV TR CAGR: `-5.49%` ณ 30 มิ.ย. 2026; `Start/End TR value:
  not disclosed`; ไม่อนุมาน endpoint ซ้ำ
- Current NAV: `$10.65` ณ 16 ก.ค. 2026; current YTD NAV TR `-36.18%`
- Market price: `$10.90`, closing NAV `$10.86`, premium `0.37%` ณ 17 ก.ค. 2026;
  price drawdown จาก 52-week high `$17.55` เท่ากับ `-37.89%` (secondary proxy,
  ไม่ใช่ official maximum drawdown)
- Annual coverage: `secondary total-return proxy*` ปี 2016-2025; official SEC
  prospectus แสดง annual chart เป็นภาพ แต่ไม่เปิดค่าตัวเลขในข้อความ

| ปี | IDX TR proxy* | S&P 500 TR |
|---|---:|---:|
| 2016 | 16.67% | 11.96% |
| 2017 | 19.25% | 21.83% |
| 2018 | -10.46% | -4.38% |
| 2019 | 6.13% | 31.49% |
| 2020 | -7.45% | 18.40% |
| 2021 | -2.60% | 28.71% |
| 2022 | -9.39% | -18.11% |
| 2023 | 1.97% | 26.29% |
| 2024 | -9.75% | 25.02% |
| 2025 | 13.83% | 17.88% |

`*` ตาราง IDX เป็น secondary total-return proxy จาก FinanceCharts ไม่ใช่ annual
NAV TR ที่ issuer เปิดเผย จึงไม่ใช้แทน rolling NAV CAGR หรือจัดอันดับร่วมกับ
กองที่มี official annual NAV TR. Proxy 2016-2025 cumulative/CAGR คือ `13.13%`
และ `1.24%`; 2021-2025 cumulative/CAGR คือ `-7.55%` และ `-1.56%`. S&P 500
common benchmark ใช้ cached USD TR convention ณ 31 ธ.ค. 2025.

## Up years / Down years

- Up years / Down years: `5 / 5` ใน proxy window 2016-2025
- Best: 2017, `+19.25%*`
- Least positive: 2023, `+1.97%*`
- Worst: 2018, `-10.46%*`
- Least bad down year: 2022, `-9.39%*`
- Current YTD: `-36.18%` official NAV ณ 16 ก.ค. 2026; market price วันที่
  17 ก.ค. เพิ่ม `1.77%` เป็นเพียงสัญญาณรีบาวด์ระยะสั้น

## Risk read-through

Rolling 10-year NAV CAGR ติดลบและ 3Y/5Y ก็ยังติดลบ สะท้อนว่า cheap valuation
ยังไม่เพียงพอให้เกิด rerating. ณ 30 มิ.ย. 2026 กองมี P/E `9.45x`, P/B `1.21x`,
top 10 holdings `49.91%`, โดย sector หลักคือ Financials `26.48%`, Materials
`21.91%`, Industrials `12.47%` และ Energy `12.33%`; country exposure คือ
Indonesia `77.58%` และ China `14.36%`. โครงสร้างนี้ทำให้ IDX ไวต่อดอกเบี้ย,
Rupiah, commodity cycle, bank earnings และ China risk มากกว่าตลาดโลกแบบกระจาย.
Official daily NAV TR series สำหรับคำนวณ maximum drawdown/recovery date:
`ไม่พบข้อมูลที่ยืนยันได้`. กองยังมี AUM เพียง `$31.41M` ณ 16 ก.ค. 2026 จึงควร
เผื่อ liquidity/bid-ask risk.

## Indonesia macro overlay and reversal scenarios

กรอบเวลา: 6-12 เดือน. Causal chain คือ growth และ employment ช่วยพยุง earnings
แต่ policy/FX/governance risk ยังขวาง multiple expansion. GDP Q1 2026 โต `5.61%`
และ unemployment `4.68%`; TFR `2.13` เป็น long-run demand tailwind. อย่างไรก็ดี
BI-Rate `5.75%` เทียบ headline inflation `3.34%` ให้ ex-post real policy-rate
ประมาณ `+2.41 percentage points` (คำนวณแบบหยาบ) ขณะที่ CPI corruption score
ของ Indonesia อยู่ที่ `34/100`; จึงยังไม่ใช่สภาพแวดล้อมที่เอื้อต่อการลด discount rate
อย่างชัดเจน. ค่าใช้จ่ายอาหารเฉลี่ยระดับประเทศราว `Rp804,430/คน/เดือน` และค่าใช้จ่าย
คนโสดใน Jakarta ราว `Rp8.44M/เดือน ไม่รวมค่าเช่า` เป็นข้อมูลประกอบที่ชี้ว่า
ฐานต้นทุนต่ำ แต่ purchasing power ในเมืองกับระดับประเทศแตกต่างกันมาก.

| Scenario | เงื่อนไข | ผลต่อ IDX |
|---|---|---|
| Base | GDP ยังใกล้ 5%, BI คงดอกเบี้ยสูง, Rupiah/foreign flow ผันผวน | รีบาวด์เป็นช่วง ๆ ได้ แต่ยัง choppy; ยังไม่ยืนยัน trend reversal |
| Bull / Upside | เงินเฟ้อและ FX ผ่อนคลายจน BI pause/cut, bank credit/earnings ฟื้น, FDI และ governance/logistics reform เดินหน้า | financials และ domestic-demand shares นำการ rerating; โอกาสกลับตัวชัดขึ้น |
| Bear / Downside | FX อ่อนต่อ, inflation สูงกว่าขอบบน target, BI ต้องตึงตัว, commodity/China shock หรือ foreign outflow ต่อเนื่อง | ทำ low ใหม่ได้ แม้ valuation ดูถูก |

**Signposts:** BI-Rate จาก `5.75%` ต้องหยุดขึ้นหรือเริ่มลด, inflation ต้องไม่ทะลุ
ขอบบน target, Rupiah และ foreign flows ต้องหยุดทำจุดต่ำใหม่, bank credit/earnings
ต้องฟื้น และหุ้นใน Materials/Energy ต้องไม่ลากดัชนีลงต่อ.

**Falsifier:** หากเงินเฟ้อ/FX บังคับให้ BI ขึ้นดอกเบี้ยอีก พร้อม foreign outflow และ
earnings revisions ลงต่อ มุมมอง tactical rebound จะถูกยกเลิก. สรุปเชิงวิเคราะห์:
`มีโอกาสรีบาวด์ แต่ยังรอ confirmation`; ระยะยาวควรถือเป็น high-beta country/sector
bet ไม่ใช่ pure Indonesia macro proxy.

## Sources

- [VanEck IDX product page](https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx?audience=retail&country=us) — current NAV/YTD, fees, holdings, sector/country weights, distributions
- [VanEck IDX fact sheet](https://www.vaneck.com/us/en/investments/indonesia-index-etf-idx-fact-sheet.pdf) — official rolling returns, valuation, top-10 concentration, risk and benchmark
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1137360/000113736026000469/vaneckindonesiaindexetfidx.htm) — fund objective, calendar-year chart, and risk disclosures
- [FinanceCharts IDX performance](https://www.financecharts.com/etfs/IDX/performance) — secondary annual total-return proxy, clearly separated from official NAV TR
- [Charles Schwab IDX summary](https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=IDX) — secondary 17 Jul 2026 market price/NAV and 52-week range
- [BPS Q1 2026 GDP, labor and demographics](https://www.bps.go.id/en/news/2026/05/06/910/ekonomi-indonesia-resilien-dan-tumbuh-solid--pada-triwulan-1-2026.html)
- [Bank Indonesia BI-Rate indicator](https://www.bi.go.id/en/statistik/indikator/bi-rate.aspx)
- [BPS June 2026 inflation](https://www.bps.go.id/en/pressrelease/2026/07/01/2590/inflasi-year-on-year--y-on-y--pada-juni-2026-sebesar-3-34-persen-.html)
- [Transparency International CPI 2025 Asia-Pacific](https://www.transparency.org/en/press/corruption-perceptions-index-2025-stalling-anti-corruption-progress-asia-pacific-public-anger-surges)
- [KPK SPI 2025 dashboard](https://spi.kpk.go.id/dashboard/hasil/)
- [BPS September 2025 consumption expenditure](https://www.bps.go.id/en/publication/2026/05/29/057b21b35bc236c5ede9d160/expenditure-for-consumption-of-indonesia-september-2025.html) and [Katadata BPS-based food-spending summary](https://databoks.katadata.co.id/produk-konsumen/statistik/6a18ecc8f1404/pengeluaran-warga-ri-untuk-rokok-melampaui-belanja-beras-pada-september-2025)
- [Numbeo Jakarta cost-of-living estimate](https://www.numbeo.com/cost-of-living/in/Jakarta) — crowd-sourced urban indicator, not a national official average
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — benchmark identity; annual rows reuse the cached 2016-2025 USD TR convention
