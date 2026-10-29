# China (中国) — Drafting & Code Reference

Legend: **✓** = read this session in a government/standards-body text (URL in §8). **⚠ verify** = memory/secondary/not opened; confirm against the current edition and the **local 规划/住建 bureau (市规划局/住建局)** rules. Most national "GB" standards are paywalled; only GB 55038-2025 (Beijing excerpt) was read in full for dimensions.

**Key status facts:** Since 2022 China is replacing older "GB 5xxxx" recommended codes with **mandatory full-text engineering codes (GB 55xxx 通用规范)**; where an old code (e.g. GB 50096) and a new one (GB 55038) conflict, the **mandatory GB 55xxx wins** ✓ (announcement abolishes GB 50368-2005, per bendibao copy of MOHURD notice).

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Millimetres on plans (no unit written); elevations/site in metres to 3 decimals ⚠ (GB/T 50001) |
| Language | Simplified Chinese (简体中文); bilingual only for foreign-funded projects ⚠ |
| Sheet sizes | A0 841×1189, A1 594×841, A2, A3, A4 (ISO-like, 图幅 0–4) ⚠ GB/T 50001-2017 ch.3 |
| Scales | Site 1:500–1:2000; plans/elevations/sections 1:100 (1:50, 1:200); details 1:20–1:1 ⚠ — GB/T 50001-2017 ch.6, 建筑工程设计文件编制深度规定 (2016) ⚠ |
| Title block | 图签/会签栏: 设计单位 (+ 资质证书 grade/no.), 项目名称, 图名, 图号, 比例, 日期, 设计/校对/审核/审定 signatures, 注册建筑师 stamp (出图章) ⚠ |
| Levels | Absolute elevation (绝对标高, from 黄海 or 1985国家高程基准) and ±0.000 relative; both noted on site plan ⚠ |
| Coordinates | CGCS2000 (国家2000大地坐标系); older 北京54/西安80 on legacy sites ⚠ |
| North | 指北针 + 风玫瑰 (wind rose) on site plan ⚠ |
| Area terms | 建筑面积 (GFA), 使用面积, 套内建筑面积, 公摊 (shared); 容积率 = total above-ground GFA / site area ⚠ |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

| Topic | Practice |
|---|---|
| National CAD standard | **GB/T 18112-2000 (CAD layer for building drawings)** — older, rarely strictly used; actual layers follow Chinese-language names or in-house ⚠ (verify current code) |
| Typical layers (practice) | `0-轴线 (axis)`, `0-墙体 (walls)`, `0-门窗`, `0-标注 (dims)`, `0-文字`, `0-家具`, `A-WALL`, `A-DOOR`… English forms appear in joint-venture jobs ⚠ |
| Files | `.dwg` (AutoCAD / 天正建筑 TArch, 浩辰 GstarCAD), plus PDF; 天正 objects often require TArch to open — **export "t3" / explode before sharing** ⚠ |
| 审图 (drawing review) | Mandatory **施工图审查 by licensed 审图机构** (independent review firm) before 施工许可证 ✓ (fire reviewed by 住建 for special cases) ⚠ |
| e-submission | National platforms; Shenzhen/Shanghai/Beijing have online 工程建设项目审批 systems; many accept PDF + signed DWG plus **BIM模型** pilots ⚠ |
| Digital seal | 电子签章 with 注册建筑师/结构工程师 certificates ⚠ |

## 3. Drafting conventions

- **Grid:** 定位轴线 labelled with numbers (1,2,3 horizontal) and capital letters (A,B,C vertical, omitting I, O, Z); circles 8–10 mm dia at 1:100 ⚠ GB/T 50001 ch.8.
- **Dimensions:** three tiers outside the plan (总尺寸 overall, 轴线尺寸 grid, 细部尺寸 details); dimension strings in mm; ±0.000 for ground floor FFL ⚠.
- **Line weights:** b = 0.5–1.4 mm series; wall cut lines heavy (b), door swing arcs thin (0.25b) ⚠.
- **Material fill:** 钢筋混凝土 RC with diagonal hatch and black dots; 砖 masonry 45° ⚠ GB/T 50001 Appendix.
- **Doors/windows:** codes `M-1`, `C-1` (门/窗) with 门窗表 schedule; fire doors `FM甲/乙/丙` (A/B/C grade) ✓ practice.
- **Sections:** 剖切符号 numbered 1-1, 2-2; 详图索引 circle with sheet no.
- **Notes:** 设计总说明 sheet (design standards list, 耐火等级, 抗震设防烈度, 使用年限, 材料做法 with 标准图集 refs like 15J…, 12J…) ⚠.
- **Refs:** 国标图集 (national atlases, e.g. 11J…) cited by number ⚠.

## 4. Governing codes & authorities

| Item | Code / authority | Status |
|---|---|---|
| Civil building design (all types) | **GB 50352-2019 民用建筑设计统一标准**; MOHURD; eff 2019-10-01, replaced 2005 version; mandatory clauses 4.3.1, 6.7.4, 6.8.6, 6.8.9 | ✓ gongbiaoku |
| Housing | **GB 55038-2025 住宅项目规范** (mandatory), eff 2025-05-01; GB 50096-2011 住宅设计规范 partly superseded | ✓ Beijing excerpt |
| Fire (design) | **GB 50016-2014 (2018 ed.) 建筑设计防火规范**; **GB 55037-2022 建筑防火通用规范** (mandatory, eff 2023-06-01 ⚠) | ✓ edition; ⚠ dates |
| Drawing standard | **GB/T 50001-2017 房屋建筑制图统一标准**, eff 2018-05-01, replaced 2010 | ✓ gongbiaoku-search |
| Concrete | **GB 50010-2010 (2015 ed.) 混凝土结构设计规范**; new GB 55008-2021 | ⚠ |
| Seismic | **GB 50011-2010 (2016 ed.) 建筑抗震设计规范**; GB 55002-2021 mandatory | ⚠ |
| Electrical | GB 50054 低压配电设计规范; GB 50034 照明; 民用建筑电气设计标准 GB 51348-2019 | ⚠ |
| Planning | 城乡规划法; **建设工程规划许可证**, **建设用地规划许可证**; 地方规划技术管理规定 (e.g. 北京/上海/深圳) | ⚠ |
| Accessibility | GB 50763-2012 无障碍设计规范; GB 55019-2021 | ⚠ |
| Authorities | 住建局 (building permit 施工许可), 规划自然资源局 (planning), 消防救援支队 (fire), 人防办 (civil air defence), 审图机构 | ✓ practice |

## 5. Key numbers

**Residential — GB 55038-2025 (mandatory) ✓ Beijing excerpt:**

| Item | Value | Clause |
|---|---|---|
| Bedroom area | **≥ 5 m²** usable; bedroom serving as living ≥ 9 m²; short side ≥ 1.80 m | 4.1.1 |
| Storey height | **≥ 3.00 m** (new houses) | 4.1.2(1) |
| Clear height bedroom/living | **≥ 2.60 m**; local ≥ 2.20 m provided < 2.60 area ≤ 1/3 of room | 4.1.2(2) |
| Attic rooms | ≥ 1/2 of area with clear height ≥ 2.20 m | 4.1.2(3) |
| Kitchen / bath clear height | ≥ 2.20 m | 4.1.2(4) |
| Kitchen area | ≥ 3.5 m² usable | 4.1.4 |
| Bathroom (3 fixtures) | ≥ 2.5 m² | 4.1.6 |
| No bedrooms/kitchens in basements | semi-basement only with ventilation, damp-proofing measures | 4.1.3 |
| Thresholds / level changes | ≤ 0.015 m (kitchen, bath, closed balcony, entrance door) | 4.1.12 |
| Corridor inside flat | entry hall ≥ 1.10 m; to bedrooms/living ≥ 1.00 m; to kitchen/bath/store ≥ 0.90 m | 4.1.13 |
| Door clear width | entrance **≥ 0.90 m** (existing retrofits 0.80); bedroom ≥ 0.80; kitchen/bath ≥ 0.70 | 4.1.14 |
| Balcony guard | clear height **≥ 1.20 m**; baluster gap ≤ 0.11 m; anti-climb | 4.1.15, 4.2.8 |
| Window sill guard | protection if sill < 0.90 m; bay window sill ≤ 0.45 m → guard 0.90 from sill, > 0.45 → 0.60 | 4.1.16 |
| Public corridor | width ≥ 1.20 m; height ≥ 2.20 m | 4.2.1 |
| Public stair width | ≤ 15 m top residential floor: ≥ 1.00 m one-side rail, ≥ 1.10 m between walls; > 15 m: ≥ 1.10 m | 4.2.2(1) |
| Public stair step | tread **≥ 0.26 m**, riser **≤ 0.175 m**, uniform | 4.2.2(2) |
| Handrail height | ≥ 0.90 m; ≥ 1.20 m for horizontal run > 0.50 m; baluster gap ≤ 0.11 m; stairwell gap > 0.11 m needs anti-fall | 4.2.2(3)(4) |
| Lifts | highest dwelling floor ≥ 4th storey **or > 9 m** → ≥ 1 lift per unit; ≥ 12th storey or > 33 m → ≥ 2 lifts | 4.2.4 |
| Lift car (accessible) | door ≥ 0.90 m; wide car 1.60×1.50, deep 1.10×2.10 | 4.2.4(3) |
| Public entrance | door clear ≥ 1.10 m; one leaf ≥ 0.80 m; platform depth ≥ 1.50 m | 4.2.7 |
| Slab thickness (RC) | solid slab ≥ 100 mm | 5.0.4 |
| Structural class | safety level ≥ 2 (二级); seismic category ≥ standard (标准设防类) | 5.0.1, 5.0.2 |
| Sound insulation | bedroom separating wall/floor DnT,w+C ≥ 50 dB; impact ≤ 65 dB | 6.1.2 |
| Site slope | > 8% → terraced; retaining wall > 2 m: 3.0 m / 2.0 m clearances | 3.2.4 |
| Green space | new areas ≥ 0.50 m²/person; width ≥ 8 m | 3.2.2 |
| Sunshine | per Table 3.1.2 (大寒日 hours); old-area projects ≥ 1 h | 3.1.2 |

**Not verified (⚠):** GB 50352 universal dims (standard door ≥ 0.9 m, public stair 1.2–1.8 m by use), setbacks (退线), 容积率/建筑密度 (set per plot in 规划条件 / 控规 — **ask**), parking (地方 ratio e.g. 1 space/unit ⚠), GB 50016 fire details: residential evacuation stair width (1.10 m, 1.00 m for ≤ 18 m with railing one side) ⚠, apartment compartment 1,500 m² ⚠, floor-to-door distance tables ⚠, fire separation 6 m between multi-storey buildings ⚠, 防火间距 for high-rise 9 m ⚠. Electrical: 220/380 V, 50 Hz; RCD (30 mA) in wet rooms ⚠ (GB 51348). Seismic: 抗震设防烈度 6–9°, design basic acceleration 0.05g–0.40g by city ⚠ (GB 50011 App. A). Concrete cover for slab 15 mm indoor ⚠.

## 6. Permit drawing set (typical, ⚠ varies by city)

1. 建设用地规划许可证 + 规划条件 (planning conditions) — obtained first
2. 方案设计 (scheme: site plan, plans, elevations, sections, 日照分析, 经济技术指标表)
3. 初步设计 / 施工图: 总平面, 各层平面, 立面, 剖面, 大样, 门窗表, 防火分区图, 无障碍
4. 结构施工图 + 计算书; 设备 (给排水, 暖通, 电气); 节能计算 / 绿建; 人防 if applicable
5. 施工图审查合格书 → 建设工程规划许可证 → 施工许可证

## 7. Common rejection reasons

- 日照分析 failing 大寒日/冬至日 hours for neighbours (GB 55038 3.1.2).
- 容积率/建筑密度/限高 over 规划条件; setback lines (退线、退红线) ignored.
- Fire: wrong 防火分区 area, evacuation distance, 疏散楼梯 width, fire lift/fire engine access (登高操作场地) missing.
- Stairs/clear heights below new mandatory GB 55038 values (older drawings at 2.80 m storey height, 0.25 m treads).
- Missing accessibility paths; missing 门窗表/节能 sheet; 图签 without 注册师 stamps.
- Using withdrawn code references in 设计总说明 (e.g. GB 50368-2005, GB 50016 without GB 55037).

## 8. Sources

- GB 55038-2025 excerpt (Beijing Planning & Natural Resources Standards Centre): https://ghzrzyw.beijing.gov.cn/biaozhunguanli/bzzl/202506/P020250609570099619169.pdf ✓
- GB 50352-2019 status/mandatory clause list: https://www.gongbiaoku.com/book/ue116739ngg ✓
- MOHURD notice copy (GB 55038 eff 2025-05-01, abolishes GB 50368): https://m.bendibao.com/show986460.html ⚠ secondary
- Xinhua (storey height ≥ 3 m, lift at ≥ 4 storeys): https://www.news.cn/house/20250401/5701ed566ec14e68af711d504c930882/c.html
- GB/T 50001-2017 status: https://www.gongbiaoku.com/mobile/book/6id19977k7u (index only)
- GB 50016 text (not readable this session): https://sbc.shu.edu.cn/JZSJFHGF.pdf ⚠
