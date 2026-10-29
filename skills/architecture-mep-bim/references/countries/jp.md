# Japan (日本) — Drafting & Code Reference

Legend: **✓** = read this session from the official e-Gov statute text (URL in §8). **⚠ verify** = from memory/secondary source or not confirmed; check before putting on a drawing. Legal text paraphrased; clause numbers are of 建築基準法 (法, Act 201/1950) and 建築基準法施行令 (令, Cabinet Order 338/1950).

**Rule of thumb:** national law sets minimums; **zoning numbers (建蔽率・容積率・高さ) come from the city's 都市計画 for the plot** (用途地域), and the 特定行政庁 (municipality/prefecture) adds 条例. Never invent coverage/FAR — ask for the 用途地域 and 指定建蔽率/容積率, 前面道路幅員.

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Metric. Plans dimensioned in **mm without unit**; site/levels in m ⚠ (JIS A 0150 practice) |
| Area unit | ㎡ (m²). 坪 only informal for clients; never on permit drawings ⚠ |
| Language | Japanese (日本語) only on permit sheets; vertical/horizontal text both seen; English not accepted on 確認申請書 ⚠ |
| Dates | Reiwa (令和) or Gregorian; 確認申請 forms use 令和 ⚠ |
| Sheet sizes | ISO A series (A1 / A2 / A3); A3 landscape common for 確認申請 sets by 指定確認検査機関 ⚠ |
| Scales | Site 1/100–1/200, floor plans 1/50 or 1/100, elevations/sections 1/100 (1/50), details 1/20–1/1 ⚠ — 建築基準法施行規則 sets content, not scale ⚠ |
| Title block | 建築主 (client), 設計者 (designer + 建築士 license no., 一級/二級/木造), 工事名称, 図面名称, 縮尺, 日付, 図面番号 ⚠ |
| Drafting standard | **JIS A 0150 建築製図通則** (building drafting), **JIS Z 8310 製図総則**, JIS Z 8313 (lettering), JIS Z 8312 (lines) ⚠ — cite current edition on request |
| North | 方位 (北) arrow mandatory on 配置図 ✓ practice; show 真北 |
| Level datum | **GL** (地盤面) and **FL** (floor level); 設計GL, 隣地GL; 1FL = ±0 ⚠. Heights per 令2条 averaging method for 地盤面 ⚠ |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

| Topic | Practice |
|---|---|
| Layer naming | No national mandatory scheme for private buildings. Public works follow MLIT **CAD製図基準 / 営繕工事電子納品** (SXF/OCF, JACIC layer names such as 躯体/建具/寸法 in Japanese) ⚠ |
| Suggested layers (skill default) | `A-WALL`, `A-DOOR`, `A-GLAZ`, `A-FLOR`, `A-ANNO-DIMS`, `A-ANNO-TEXT`, `A-AREA` (床面積 boundaries), `S-COLS`, `E-LITE`, `M-DUCT` (AIA/ISO 13567 style) |
| Area drawings | Required separate **面積求積図** layer/sheet (建築面積・床面積 calculation) ✓ practice |
| File format for submission | PDF / A-series paper; **電子申請** via 指定確認検査機関 portals or 建築確認電子申請 systems; DWG/JWW internal only ⚠ |
| BIM | MLIT is rolling out **BIM-based 確認申請 (BIM図面審査)** from 2026 ⚠ verify scope/date |
| Common CAD | JW_CAD (free, dominant for small houses), AutoCAD, Vectorworks, ARCHICAD, GLOOBE, Rebro (MEP) ⚠ |

## 3. Drafting conventions

- **Axes (通り芯):** grid lines labelled X1, X2… (horizontal) and Y1, Y2… (vertical); 壁芯 (wall centreline) base for structure, 内法 (inside face) for room areas ⚠.
- **Floor area basis:** 床面積 measured to **wall centre** (壁芯) per 令2条 ✓ concept (art. 2 not extracted — ⚠ verify numbers); 居室 area for 採光 uses floor area of the room.
- **Symbols:** door `D`/ 建具記号 `AW` (aluminium window), `SD` (steel door), `WD` (wood door), `SS` (steel shutter) ⚠ — tag with 建具表 (door/window schedule).
- **Levels:** 天井高 (CH), 階高 (floor-to-floor), 軒高 (eave height), 最高の高さ, 設計GL.
- **Materials hatching:** RC 鉄筋コンクリート, 断熱材, 木造 per JIS A 0150 ⚠.
- **Required drawings show:** 道路境界線, 隣地境界線, 道路幅員 (m), 道路種別 (法42条 category), 求積表 (area table), 建蔽率・容積率 calc, 斜線制限 diagrams (道路/隣地/北側), 日影図 where applicable ⚠.
- **Text:** Japanese; notes like 「別途」「特記」 for matters in 特記仕様書.

## 4. Governing codes & authorities

| Item | Code/Authority | Note |
|---|---|---|
| Building Standards Act 建築基準法 | MLIT 国土交通省; **特定行政庁** (local gov / 建築主事) enforces | ✓ |
| Enforcement Order 建築基準法施行令 | Cabinet Order 338/1950, many amendments | ✓ |
| Enforcement Regulation 施行規則 | Forms and drawing content for 確認申請 | ⚠ |
| 確認申請 (building confirmation) | 建築主事 or **指定確認検査機関** (private designated inspection body); issues **確認済証** before work starts | ✓ 法6 |
| 中間検査 / 完了検査 | Interim & completion inspections → **検査済証** | ⚠ 法7, 7-3 |
| Urban Planning Act 都市計画法 | Sets 用途地域, 指定建蔽率/容積率 | ⚠ |
| Fire Service Act 消防法 | Fire fighting equipment (法17), residential alarms (法9-2); local **消防署** reviews | ✓ |
| Electrical | 電気事業法 / 電気設備技術基準; **内線規程 JEAC 8001** (wiring practice, JESC) | ⚠ |
| Structure | 令3章 (88 seismic), 木造 壁量計算 (令46), 耐震基準 | ✓ 令88 |
| Accessibility | バリアフリー法 (Barrier-Free Act) for specified buildings | ⚠ |
| Energy | 建築物省エネ法 — all new buildings must comply from Apr 2025 | ⚠ verify |
| Local rules | Municipal 建築基準条例, 景観条例, 開発指導要綱 | ⚠ |

## 5. Key numbers

**Zoning (法) ✓ from e-Gov:**

| Item | Value | Source |
|---|---|---|
| Site must touch a road (接道義務) | **≥ 2 m** frontage on a 法42 road | 法43(1) ✓ |
| Road width definition | **≥ 4 m** (6 m in designated areas) | 法42(1) ✓ |
| 建蔽率 (coverage) | low-rise exclusive residential: **3/10, 4/10, 5/10 or 6/10** as set by city plan; 準住居 etc. 5/10, 6/10, 8/10; commercial 8/10 | 法53(1) ✓ |
| 容積率 (FAR) | 第一種低層住居専用: **5/10, 6/10, 8/10, 10/10, 15/10 or 20/10**; mid-high-rise residential/commercial: 10/10 upward (list continues) | 法52(1) ✓ |
| Wall setback in low-rise zones | **1 m or 1.5 m** where city plan sets one | 法54 ✓ |
| Height cap low-rise zones | **10 m or 12 m** per city plan | 法55 ✓ |
| Road-slope (道路斜線) | factor **1.25** for residential zones (1.5 beyond 1.25×road width); other zones per 別表第三 | 法56(1)1, 56(3) ✓ |
| Adjacent-slope (隣地斜線) | rises from **20 m @1.25** (residential) or **31 m @2.5** | 法56(1)2 ✓ |
| North-slope (北側斜線) | applies in low-rise (4 m off) and mid-high-rise (8 m off) residential zones; offsets cited in 法56(7)3 | ✓ (slope values 5 m+1.25 / 10 m+1.25 ⚠ verify in 法56(1)3) |
| 日影規制 (shadow) | per 条例 and 法56-2 | ⚠ |

**Rooms & stairs (令):**

| Item | Value | Source |
|---|---|---|
| Habitable-room ceiling height | **≥ 2.1 m** (average where ceiling varies) | 令21 ✓ |
| Daylight window / floor area, dwelling living rooms | **≥ 1/7** (schools 1/5; other schools 1/10) | 令19(3), 法28(1) ✓ |
| Natural ventilation opening | **≥ 1/20** of room floor area (unless mechanical vent) | 法28(2) ✓ |
| Ground floor height, timber floors | floor ≥ **45 cm** above ground; vent holes ≥ 300 cm² each 5 m of wall | 令22 ✓ |
| Stairs — dwelling (single-family, non-communal) | width ≥ **75 cm**; riser ≤ **23 cm**; tread ≥ **15 cm** (relaxation permitted) / standard table row 4: 75 / 22 / 21 | 令23(1) ✓ |
| Stairs — communal/other with upper-floor rooms > 200 m² | width ≥ **120 cm**; riser ≤ **20**; tread ≥ **24** | 令23(1) table row 3 ✓ |
| Stairs — primary school pupils | width 140; riser ≤ 16; tread ≥ 26 | 令23(1) row 1 ✓ |
| Stairs — shops > 1,500 m², theatres, junior-high | width 140; riser ≤ 18; tread ≥ 26 | 令23(1) row 2 ✓ |
| Winder tread measured | 30 cm from narrow end | 令23(2) ✓ |
| Handrail on stairs | required; mid-rail if width > 3 m (unless riser ≤ 15 & tread ≥ 30) | 令25 ✓ |
| Landing required | height > 4 m (> 3 m for school/theatre types); landing depth ≥ 1.2 m on straight stair | 令24 ✓ |
| Rooftop/upper-floor balcony guard | **≥ 1.1 m** | 令126 ✓ |
| Common corridor (apartment floor with units totalling > 100 m²) | **≥ 1.6 m** both-sided; **≥ 1.2 m** one-sided | 令119 ✓ |
| Site access path (outdoor escape stair) | ≥ **1.5 m**; ≥ 0.9 m for ≤ 3 storeys and < 200 m² | 令128 ✓ |
| Door / opening width (no national value for dwelling doors) | designer's choice ≥ 0.75 typical; accessibility 80 cm clear ⚠ | ⚠ |

**Fire & egress:**

| Item | Value | Source |
|---|---|---|
| Walking distance to stair — normal rooms | **50 m** (準耐火/不燃 main structure) / **40 m** (other); 30 m for windowless rooms | 令120 ✓ (+10 m allowance for upper storeys ⚠ verify in 令120(2)) |
| Two stairs required — apartment floor | when habitable-room area on that floor **> 100 m²** (200 m² if 準耐火/不燃 per 令121(2)) | 令121(1)5 ✓ |
| Two stairs — floor ≥ 6 with habitable rooms | required unless ≤ 100 m² with balcony/escape | 令121(1)6 ✓ |
| Protected stair (避難階段) | required to ≥ 5th floor or B2; special stair from 15th floor / B3 | 令122 ✓ |
| Smoke extraction (排煙) | special buildings > 500 m²; 3+ storeys > 500 m²; rooms > 200 m² when GFA > 1,000 m² — **dwelling units of apartments exempt if ≤ 200 m²** | 令126-2 ✓ |
| Emergency lighting | not required in houses/dwelling units; **1 lux** minimum | 令126-4, 126-5 ✓ |
| Residential alarms (住宅用火災警報器) | mandatory in all dwellings | 消防法9-2 ✓ (device placement: 市町村条例 ⚠) |

**Structure:** earthquake shear coefficient **Ci = Z·Rt·Ai·Co**, Z 1.0–0.7 by region (Z map) — 令88 ✓; Co = 0.2 for 一次設計 (0.2 allowable-stress) ⚠ verify; 新耐震 post-1981; timber houses use 壁量計算 (令46) ⚠.

**Parking:** no national rule; municipal 駐車場条例 for large buildings ⚠.

## 6. Permit drawing set (確認申請)

1. 確認申請書 (forms 第1面–第5面) ✓ 法6
2. 付近見取図 (location map), 配置図 (site plan with setbacks, 道路幅員, 隣地境界)
3. 各階平面図, 立面図 (2 or more), 断面図 (2 or more) ⚠ per 施行規則
4. 求積図・面積表, 建蔽率/容積率 calc
5. 構造図 (伏図, 軸組図, 構造計算書 or 壁量計算) and 設備図 (給排水・換気・電気 as needed)
6. 斜線制限 and 日影図 where applicable; 採光・換気 calc sheet; 防火区画図 for fire compartments
7. Parallel: 消防同意 (fire dept agreement) ⚠ for non-single-family; Mandatory 省エネ計算 documents ⚠

## 7. Common rejection reasons

- 建蔽率/容積率 over by calculation (balcony, eave, parking inclusion errors).
- 前面道路 width or 接道 2 m not proven (法42 category unclear, 2項道路 setback not drawn).
- 斜線制限 not checked at all three directions (道路・隣地・北側).
- Window area below 1/7 (採光) after subtracting 隣地 distance factor; missing 換気 1/20.
- Stairs outside 令23 limits; no handrail (令25); landing missing (令24).
- Walking distance (令120) or 2-stair requirement (令121) missed on shared corridor.
- Drawing inconsistencies between plan/elevation/section/area table; 求積図 not matching.

## 8. Sources

- 建築基準法施行令 (e-Gov): https://laws.e-gov.go.jp/law/325CO0000000338 ✓
- 建築基準法 (e-Gov): https://laws.e-gov.go.jp/law/325AC0000000201 ✓
- 消防法 (e-Gov): https://laws.e-gov.go.jp/law/323AC1000000186 ✓
- MLIT 建築確認 portal: https://www.mlit.go.jp/jutakukentiku/ ⚠ (not read this session)
- Secondary only (stair summaries): https://www.mec-h.com/words/detail?n=2864 ⚠
