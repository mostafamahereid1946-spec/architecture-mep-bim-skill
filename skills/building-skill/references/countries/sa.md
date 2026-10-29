# Saudi Arabia (المملكة العربية السعودية) — Drafting & Code Reference

Legend: **✓** = checked this session against the primary document (tag = source in §8). **⚠ verify** = drafter practice, secondary/news source, or memory only; confirm against the adopted text or the Amanah before issuing drawings. Reader date assumed 2026.
Primary source used for municipal numbers: **MOMAH "Residential Building Construction Requirements" (اشتراطات إنشاء المباني السكنية), Ministerial Decision 4500943139/1 of 1446H (2024), effective for new permits from 8 Muharram 1446H = 14 Jul 2024** [S1][S6]. It applies to ALL Amanahs/municipalities except parking calc and setbacks on commercial streets and special-zone coverage, which each Amanah may set; where the Amanah/Regional Development Authority has its own plan rules, those govern [S1 §1]. Where S1 conflicts with SBC, **SBC governs** [S1 §7-1].

Hierarchy to remember: **SBC (life-safety/technical) > MOMAH national residential requirements (spatial: setbacks, coverage, height, parking) > Amanah/plan-specific rules (Riyadh, Jeddah, NEOM/RCRC/Diriyah etc. special authorities)**.

---
## 1. Units, scales, sheets

| Item | Practice |
|---|---|
| Unit system | Metric. Plans/sections: **metres with 2 decimals** on municipal drawings (e.g. `3.00`, `0.90`) — municipal checkers read the setback table in metres ⚠ practice; many MEP/structural offices use mm. Pick one per set and state it in a note: `ALL DIMENSIONS IN METERS UNLESS NOTED` / `الأبعاد بالمتر ما لم يذكر خلاف ذلك` |
| Levels | `±0.00` = finished ground-floor level (FFL). Municipal sheets also show **pavement level at mid-frontage (منسوب منتصف الرصيف)** because ground-floor height and villa height are measured from it (§5.2) ✓ [S1 §5-5-1] |
| Language | Bilingual Arabic + English is normal; Arabic mandatory for municipal title/owner fields ⚠ practice. Mirror layout is NOT used: drawings read left-to-right, Arabic text blocks right-aligned |
| Numerals | Western digits (0-9) on drawings; do not use Arabic-Indic digits (٠-٩) in dimensions ⚠ practice |
| Dimension format | Chain/continuous dims in metres, 2 decimals; room names + net area in m² to 2 decimals (`15.60 م²`); levels `+0.45` |
| North arrow | On every plan; site plan north up. Plot orientation by street: label street name, **street width (عرض الشارع) in m** on every adjoining street — checkers compute setbacks from it ✓ [S1] |
| Coordinate/grid | Structural grid: letters (A, B, C…) horizontal / numbers (1, 2, 3…) vertical (US/IBC-derived practice) ⚠; some offices use Arabic letters (أ، ب، ج) – keep Latin for coordination ⚠ |
| Date | DD/MM/YYYY Gregorian, often with Hijri (هـ) beside it on municipal forms ⚠ practice |

### 1.1 Typical scales ⚠ practice (no national mandate found; Amanah checklists may fix)
| Drawing | Scale |
|---|---|
| Location/vicinity (موقع عام) | 1:1000 / 1:5000 / NTS |
| Site plan (الموقع العام / مسقط أفقي للموقع) | 1:200 (plots) – 1:500 |
| Floor plans, roof plan | 1:100 (1:50 for small villas on A1) |
| Elevations (الواجهات) & sections (القطاعات) | 1:100 (1:50 villas) |
| Stair/toilet/kitchen enlargements | 1:50 / 1:25 |
| Wall sections, details | 1:20 / 1:10 / 1:5 |
| Structural: foundation/slab plans | 1:100 (1:50) ; beam/column schedules NTS |
| MEP plans | 1:100 (1:50 plant rooms) |

### 1.2 Sheet sizes & title block
| Item | Practice |
|---|---|
| Sheet sizes | ISO A series: A0 (841x1189), A1 (594x841) most common for permit; A2/A3 for details & reduced sets ⚠ practice. Margin 10 mm, binding 20-25 mm left |
| Title block fields (typical) | Project name (اسم المشروع) · Owner (المالك) · Plot no. (رقم القطعة) · Subdivision/plan no. (رقم المخطط) · District (الحي) · City/Amanah · Deed no. & date (رقم وتاريخ الصك) · Plot area from deed (المساحة حسب الصك) · Drawing title/no./rev./date · Scale · Designer office name + **MOMAH office licence no.** + **Saudi Council of Engineers (SCE) membership/licence no.** + stamp & signature (ختم وتوقيع) · Drawn/checked ✓ licence requirement [S1 §5-2][S8] |
| Stamp | Engineering office stamp + responsible engineer's signature on each sheet; design and supervision only by offices approved by MOMAH, execution by MOMAH-approved contractors ✓ [S1 §5-2]. Balady submissions are made by the engineering office through its Balady account, not by the owner ⚠ [S10] |
| Revision | Revision block with date; resubmission after Amanah comments needs cloud/rev letter ⚠ practice |

---
## 2. CAD layer & file naming standard

There is **no national CAD layer standard** found in SBC/MOMAH ⚠. Consultants overwhelmingly use **AIA/NCS-style** (`A-WALL`) or in-house layer lists inherited from US/UK parents; Aramco/SEC/giga-project clients impose their own. Default to AIA/NCS and keep a mapping table if the client supplies a template.
**Layer syntax:** `DISCIPLINE-MAJOR-MINOR` (AIA): discipline letter (A/S/M/E/P/F) – major group – minor (e.g. `A-WALL-FULL`). ACI colour (pen) → lineweight assigned in CTB.

| Layer | ACI | Lineweight (mm) | Content |
|---|---|---|---|
| A-WALL | 2 yellow | 0.50 | Cut walls (blockwork/RC outline) |
| A-WALL-PATT | 8 | 0.13 | Poche / hatch of cut walls |
| A-DOOR | 4 cyan | 0.25 | Doors + swings |
| A-GLAZ | 5 blue | 0.25 | Windows, glazing |
| A-FLOR-STRS | 6 magenta | 0.25 | Stairs, treads, UP/DN arrows |
| A-FLOR-OTLN | 7 white | 0.35 | Slab edges, balconies, projections |
| A-FLOR-EVTR | 6 | 0.25 | Lift shaft/car |
| A-AREA | 3 green | 0.13 | Area polylines for coverage calc |
| A-SITE-PROP | 1 red | 0.50 | Plot boundary (حد الملكية) |
| A-SITE-SETB | 1 red | 0.25 dashed | Setback lines (خطوط الارتداد) |
| A-ANNO-DIMS | 3 green | 0.18 | Dimensions |
| A-ANNO-TEXT | 7 | 0.18 | Notes, room tags |
| A-ANNO-TTLB | 7 | 0.35 | Title block/border |
| A-GRID | 1 red | 0.13 center | Axes + bubbles |
| S-COLS | 1 red | 0.50 | Columns |
| S-BEAM | 4 | 0.35 | Beams (dashed below) |
| S-FNDN | 5 | 0.50 | Footings/rafts |
| S-SLAB / S-REBR | 3 / 2 | 0.25 / 0.18 | Slab outlines / reinforcement |
| M-HVAC-DUCT | 4 | 0.35 | Supply/return duct |
| M-HVAC-EQPM | 6 | 0.35 | Split/FCU/AHU |
| M-HVAC-PIPE (chilled water) | 5 | 0.35 | CHW pipes |
| E-LITE | 2 | 0.25 | Lighting fixtures |
| E-POWR | 1 | 0.25 | Sockets/power |
| E-LTNG / E-SPCL | 3 | 0.25 | Low-current (data, CCTV, fire alarm devices if not F-) |
| P-DOMW | 5 | 0.25 | Domestic cold/hot water |
| P-SANR | 30 (brown) | 0.35 | Sanitary drainage (below-slab dashed) |
| P-STRM | 150 | 0.35 | Roof/storm drainage |
| FP-SPRK | 1 | 0.25 | Sprinkler heads/pipes (AIA uses `F-SPRK`) |
| FP-HYDR | 1 | 0.35 | Hydrant/hose reel, risers |
| FP-ALRM | 6 | 0.25 | Detection/alarm (Civil Defense submission) |

**File naming** (common, not mandated ⚠): `[ProjectNo]-[Originator]-[Zone]-[Level]-[Type]-[Disc]-[Number]` e.g. `P123-XYZ-ZZ-00-DR-A-1001_R01.dwg` (ISO 19650 style used on PIF giga-projects). Municipal uploads are normally PDF set + (sometimes) DWG per Amanah; **DWG/dxf submission requirements are Amanah-specific — not verified** ⚠ [S10].

---
## 3. Drafting conventions

| Item | Convention ⚠ practice unless marked |
|---|---|
| Text height (on paper) | Dims/notes 2.5 mm; room names 3.0–3.5 mm; drawing titles 5 mm; sheet titles 7 mm. AutoCAD text height = paper height x scale factor |
| Dim style | Architectural tick or closed-filled arrow, 1.5–2 mm offset, extension 1 mm beyond; 3 dim strings on plans: overall, grid/openings, details |
| Symbols | ISO/US mix: section marker with sheet ref, elevation marker, level triangle, door tag `D1`, window tag `W1`, room tag name+no.+area. Include legend sheet |
| Grid bubbles | Ø 8–10 mm circle on paper, letters horizontal / numbers vertical |
| Hatch (poche) | RC = diagonal ANSI31 + dots (AR-CONC); blockwork = ANSI37 light cross or solid-grey; masonry hollow block 200 mm = two parallel lines + hatch; insulation = wavy line (INSUL); earth = EARTH; sand/screed = AR-SAND; glazing = 3 parallel lines; waterproofing = bold dashed. Always include a material legend ⚠ |
| Wall thickness conventions | Ext. block 200 mm (+ insulation) / int. 100–150 mm (non-RC) – check SBC 602 U-values for the final build-up ⚠ |
| Arabic in AutoCAD | Use **Unicode TrueType fonts** (Arial, Tahoma, Simplified Arabic, Traditional Arabic) in text styles; SHX fonts cannot shape Arabic. Use **MTEXT** (not DTEXT) so letters join and RTL order works; set MTEXT reading direction "Right to left" or type from keyboard in Arabic mode; mixed Arabic+number strings: keep numbers as separate MTEXT or add RLM marks. Never explode text (breaks shaping). Plot with TrueType-as-geometry off so glyphs shape correctly in PDF ⚠ |
| Bilingual labelling | Arabic on top/right, English below: `غرفة نوم / BEDROOM` |
| Keynotes | Prefer numbered keynotes; Arabic notes need separate text block |

---
## 4. Governing codes & authorities

| Discipline | Code | Current edition | Enforced by |
|---|---|---|---|
| General building (use/occupancy, egress, fire resistance, accessibility, interior) | **SBC 201** Saudi General Building Code (IBC-based) | **SBC 2024 edition** — mandatory **30 Jun 2025** after a 180-day transition that started early Jan 2025; 2018 edition applied to all projects until then ✓ [S2]. (MOMAH 2024 doc still cites the 2018 edition [S1 §8]) | Amanah/municipality (permit); Civil Defense (fire-life-safety approval); SBC authority for violations |
| Structural loads & forces | **SBC 301** | 2024 (2018 prior) | Amanah via licensed design office |
| Structural – construction/testing, foundations/soils, concrete, masonry, steel | **SBC 302–306** (MOMAH cites the series as **SBC 301-309**) ✓ [S1 §5-2]. Individual titles: 303 soils/foundations, 304 concrete, 305 masonry, 306 steel ⚠ verify numbering | 2024; 2024 update added 3 codes: seismic design of steel, repair/rehabilitation of existing concrete, GFRP-reinforced concrete ✓ [S2] | Amanah |
| Electrical | **SBC 401** | 2024 | SEC (supply/metering), Civil Defense (alarm), Amanah |
| Mechanical (HVAC) | **SBC 501** | 2024 | Amanah |
| Energy conservation | **SBC 601** (non-residential) / **SBC 602** (residential) ✓ [S1 §5-4] | 2024 | Amanah / Saudi Energy Efficiency Center (SEEC) ⚠ |
| Plumbing | **SBC 701** | 2024 | Amanah; National Water Company (NWC) for connection |
| Sanitary drainage / septic | **SBC 702** (Table 802.8 sets septic tank clearances) ✓ [S1 §5-5] | 2024 | Amanah |
| Fire protection | **SBC 801** | 2024 | **General Directorate of Civil Defense (الدفاع المدني)** ✓ [S1 §5-6] |
| Residential (R3, 1–2 family, ≤3 storeys) | **SBC 1101** (also **SBC 1102**; MOMAH cites 1101 for structural/entrance width and 1102 for electrical in villas) ✓ [S1 §5-2,5-3][S3] | 2024 | Amanah |
| Municipal spatial rules | MOMAH Residential Requirements 2024 (+ Amanah plan rules) | 1446H/2024 ✓ [S1] | Amanah/municipality via **Balady** |
| Building-code governance | National Committee for SBC (SBCNC); institutional change to a "Saudi Building Code Center" under MOMAH reported (CoM decision 656, 4 Mar 2025) ⚠ verify [S9] | — | — |
| Engineering professionals | **Saudi Council of Engineers (SCE)** – Practising Engineering Professions Law, Royal Decree M/36 (1438H); office licensing/classification ✓ [S8] | — | SCE |
| Elevators | SASO elevator technical regulation ✓ [S1 §5-3-8] | — | SASO / MOMAH |
| Accessibility | SBC 201 + King Salman Center for Disability Research guide + MOMAH simplified guide (1443H); applies to residential buildings with **≥4 units** and commercial/office, **not** villas ✓ [S1 §5-1-3] | — | Amanah |
| Noise | Executive Regulation on Noise (Min. of Environment) ✓ [S1 §5-1-17] | 1441H | Amanah |

Permit platform: **Balady (بلدي)** — MOMAH's municipal licensing portal; licensed engineering office submits and the e-deed/e-lease must be valid ⚠ [S10]. Utilities: **SEC** (Saudi Electricity Co.) load approval + meter room; **NWC** water/sewer; STC for telecom ⚠ practice.

---
## 5. Key numbers

### 5.1 Plot coverage (نسبة البناء) — MOMAH 2024
| Building type | Ground floor | First floor | Repeated floors | Upper annex (ملحق علوي) | Source |
|---|---|---|---|---|---|
| Villa (فيلا, R3) | **≤75%** of plot (includes ground annexes) | **≤75%** | – | **≤70%** of floor below (incl. stair/lift cores) | ✓ S1 §4-1(1-3) |
| Apartment bldg (عمارة سكنية, R2) / res-commercial (R2+M+A2) / res-office (R2+B) | **≤65%** | **≤75%** | **≤75%** | **≤70%** of floor below | ✓ S1 §4-2(1-3), §4-3 |
| Coverage excludes | open light shafts/courts, permitted projections, electrical rooms ✓ S1 §2 (نسبة البناء) | | | | |
| Setback-area ground building (villa) | Allowed on all sides up to **70% of plot perimeter length**, within permitted ground coverage, parking & light/vent provided; height ≤ ground-floor height and **≤4.5 m** | | | | ✓ S1 §4-1(8) |
| Attached ground annex | May be attached/merged to ground floor; if separated, gap **≥1.20 m**; height one floor, **≤4.5 m** | | | | ✓ S1 §4-1(12), §5-13 |
| Basement (قبو) | Allowed under full plot, multiple levels; uses: parking, dwelling (with natural light/vent per SBC), services, recreation ✓ S1 §5-8. Level-adjustment floors (أدوار التسوية) allowed when street/ground level difference **≥3.00 m**; ≤**70%** of ground-floor area; first one not counted in allowed area/height ✓ S1 §5-9 | | | | |
| Older Riyadh form (undated): ground 60% / first 65% / height 12 m | superseded by 2024 national rules; do not use ⚠ [S7b] | | | | |

### 5.2 Setbacks (الارتدادات) — measured from property line (حد الملكية) to the ground-floor building edge ✓ [S1 §4(11), §2]
| Boundary | Villa (§4-1) | Apt / res-com / res-office (§4-2,4-3) |
|---|---|---|
| Front, street **<30 m** wide | **1/5 street width, min 3.00 m** | **1/5 street width, min 3.00 m** |
| Front, street **≥30 m** wide | **min 6.00 m** | ⚠ not stated in S1 for apartments — check Amanah |
| Side/rear **streets** | **1/5 street width, min 2.00 m** | **1/5 street width, min 2.00 m** |
| Toward **neighbour** & pedestrian paths | **min 1.50 m** (was 2.00 m before 2024) | **min 2.00 m** (building ≤5 floors); **min 3.00 m** (>5 floors) |
| Toward plazas/squares (ساحات وميادين) | **min 3.00 m** | – |
| Upper annex setback from edge of floor below | **≥1.50 m** toward surrounding streets/squares; none required toward neighbours/pedestrian paths ✓ §4-1(6) | – |
| First floor & annex over neighbour minimum setback | Building not allowed in the min. neighbour setback ✓ §4-1(7) | – |
| Corner plot chamfer (شطفة) | **≥1/5 street width, not less than 3 x 3 m**; no vehicle entries in chamfer; chamfer area NOT deducted from plot area for coverage ✓ §5-16 | same |
| Group villas "on the party line" (على الصامت) | allowed with Amanah approval on 1 side (other side ≥3.00 m) or 2 sides (others normal); double structural-separation wall required; neighbour-facing part height ≤4.5 m ✓ §4-1(9,10,13) | – |
| Setback use | Roofs of setback buildings may not be terraces/balconies; no AC condensers or dishes on them ✓ §4(12) | |

### 5.3 Height, levels, parapets
| Item | Value | Source |
|---|---|---|
| Max villa height | **14.0 m** from mid-pavement level at entrance to top of annex roof slab (was 12 m) | ✓ S1 §5-5-1(3) |
| Ground-floor level above mid-pavement | **max 1.20 m**, min **0.30 m** | ✓ S1 §5-5-1(2) |
| Services excluded from height (lift/tank rooms) | up to **6.0 m** above roof slab; no other use | ✓ S1 §5-5-1(4) |
| Roof screen/parapet (سترة السطح) | **min 1.70 m – max 2.00 m** from roof floor (as extracted — presumably privacy screen; ⚠ confirm wording) | ✓/⚠ S1 §5-5-1(5) |
| Annex roof parapet | **0.40 – 0.80 m** | ✓ S1 §5-5-1(6), §5-14(3) |
| Light-shaft parapet | **≥0.90 m** on usable roofs; **≥0.40 m** on non-usable | ✓ S1 §5-6(6) |
| Stilt ground floor (parking) in apartment bldgs | clear height **≥2.50 m**; not counted as a regulated floor; façade must be screened with approved local trees | ✓ S1 §4(5) |
| Multi-storey bldg / high-rise | >4 floors above ground and **>15 m** / **>23 m** | ✓ S1 §2 |
| Fence toward neighbours | **max 4.5 m**; no screens added above the allowed fence height | ✓ S1 §4(8,9) |
| Fence on commercial street | none allowed for res-commercial/res-office on commercial streets; side fence must not pass building end ✓ S1 §4(7) |
| Projections (بروزات) | Allowed only on streets/paths **≥10 m**; **≤1.25 m**; upper floors; none in side/rear setbacks except decorative cornice **≤0.25 m**; stair landing may project **≤1.00 m** into setback (soffit ≥2.10 m, width ≤2.80 m, no openings facing neighbour); nothing beyond property line | ✓ S1 §5-11 |
| Balcony guard | **≥0.90 m**; balcony facing neighbour inside the legal building line: screen wall **≥1.80 m** | ✓ S1 §5-11(5,6) |

### 5.4 Rooms, light & vent
| Space | Min area (m²) | Min width (m) | Source |
|---|---|---|---|
| Majlis / dining / living (المجلس/الطعام/الصالة) | 11.2 | 2.8 | ✓ S1 §5-4-2 (columns reconstructed from PDF extraction; ⚠ confirm row mapping) |
| Bedroom (غرفة نوم) | 6.5 | 2.1 | ✓ idem |
| Kitchen (مطبخ) | 5.0 | 1.8 | ✓ idem |
| Bathroom (حمام) | 2.8 | 1.4 | ✓ idem |
| WC only (دورة مياه) | 1.5 | 1.0 | ✓ idem |
| Guard/driver/maid room (excl. bathroom) | 6.5 | 2.1 | ✓ idem (older secondary source says 10 m² [S3] – superseded) |
| Internal corridor (ممر) | – | 0.90 | ✓ idem |
| Minimum dwelling unit | living/majlis + bedroom + WC + kitchen | | ✓ S1 §5-4-1 |

| Item | Value | Source |
|---|---|---|
| Glazing for light | **≥8%** of room floor area; openable part **≥4%** | ✓ S1 §5-15(2) |
| WC/bath window | **≥0.30 m²**, half openable; mechanical vent + artificial light permitted | ✓ S1 §5-15(3) |
| Vent opening must connect fully to outside air; one tied to A/C unit does not count | | ✓ S1 §5-15(4) |
| Kitchen open to living area | allowed if vent/smoke extraction adequate | ✓ S1 §5-15(6) |
| Habitable min ceiling height | 2.10 m (secondary [S3]); structural calc if floor-to-floor >3.6 m (older) ⚠ verify against SBC 201 / SBC 1101 | ⚠ |
| Escape window sill (upper bedroom) | **≤1.10 m** above floor | ✓ S1 §5-1-1(2) |

**Light shafts (مناور)** — min clear size, width x length [S1 §5-6]:
| Height of shaft | Windows on 1 side or 2 non-opposite sides | Windows on opposite sides or all sides |
|---|---|---|
| 1 floor | 0.90 x 1.80 | 1.50 x 1.80 |
| 2 floors | 1.50 x 1.80 | 1.80 x 1.80 |
| 3 floors | 1.80 x 2.40 | 2.10 x 2.40 |
| 4 floors | 2.10 x 3.00 | 2.40 x 3.00 |
| >4 floors | add **0.30 m width + 0.60 m length per extra floor** (up to 14 floors) | same |
Rules: access door at ground level; shaft open to sky, not roofed; drained; light-coloured walls; mechanical vent allowed for baths without shaft ✓ S1 §5-6(2-7).

### 5.5 Stairs, doors, egress, lifts
| Item | Value | Source |
|---|---|---|
| Main stair & landing clear width — villa (R3) | **≥0.90 m** (SBC 1101) | ✓ S1 §5-12(2) |
| Main stair & landing clear width — apt bldg (R2) | **≥1.20 m** (SBC 201); landing ≥ stair width | ✓ S1 §5-12(2) |
| Riser/tread | per SBC 201 & SBC 1101 – values not in S1. IBC baseline 178 mm max riser / 279 mm min tread ⚠ verify SBC value | ⚠ |
| Stair lighting | natural light or artificial **≥11 lux** | ✓ S1 §5-12(4) |
| Guard (درابزين) villa balcony/open stair | stated "85–95 cm min" range in text (⚠ read as ≥0.85–0.95 m); **≥0.90 m** apt bldgs; balusters must stop a **10 cm** sphere | ✓ S1 §5-1-1(1) |
| Guard height (SBC 201, non-residential) | 1.07 m (IBC 42 in) ⚠ verify | ⚠ |
| Villa entrance door width | **≥0.80 m** | ✓ S1 §5-7(2) |
| Driver's-room gate on fence | ≥0.80 m | ✓ S1 §4-1(15) |
| Car entrance (villa) | **≥3.00 m** | ✓ S1 §5-7(4) |
| Basement ramp | one ramp ≥4.00 m wide for ≤25 cars; >25 cars: separate entry & exit each ≥3.50 m | ✓ S1 §5-8(4) |
| Egress width/travel distance/exit count (non-villa) | SBC 201 Ch.10 (IBC 2015-derived): e.g. door clear 813 mm, corridor 1118 mm, stairs 1118 mm (≥50 occ.), travel distance R-2 sprinklered 76 m / B sprinklered 91 m ⚠ verify every figure in the SBC 201 table | ⚠ [S7] |
| Waste chute | required in buildings **>4 floors** (SBC 201 §713) | ✓ S1 §5-1-1(3) |
| Lifts | multi-storey buildings need passenger + accessible lift per SBC & SASO | ✓ S1 §5-3(8) |
| Ground slope for external paving | **1% – 2%** to drains | ✓ S1 §5-1-1(5) |

### 5.6 Parking
| Use | Requirement | Source |
|---|---|---|
| Villa on plot **≤400 m²** | **1** space inside plot | ✓ S1 §4-1(14) |
| Villa on plot **>400 m²** | **2** spaces | ✓ same |
| Upper annex used as separate dwelling | +1 space | ✓ S1 §4-1(3) |
| Floors split into separate flats in a villa | 1 space per unit; plot width ≥12 m (detached) / ≥10 m (attached/semi) | ✓ S1 §4-1(11) |
| Apartment | **1.5 spaces per flat**, round up | ✓ S1 §4-2(6) |
| Shops / commercial area | **1 per 45 m²**, min 1 per shop | ✓ S1 §4-2(5) |
| Offices | **1 per 45 m²**, min 1 per office | ✓ S1 §4-3(5) |
| Tandem (back-to-back) | allowed for same unit; apartments: count of tandem+single ≥ no. of flats; tandem bay ≥2.8 m wide x 11 m long | ✓ S1 §4(6) |
| Design guide | MOMAH parking design guide (دليل تصميم مواقف السيارات) – stall/aisle dims not in S1 | ✓ S1 §4(2) |

### 5.7 Fire / electrical / plumbing / HVAC / structure basics
| Topic | Value | Source |
|---|---|---|
| Fire | SBC 801 + Civil Defense safety regulation for residential & admin buildings; fire systems designed/installed by Civil-Defense-approved specialist office; emergency evacuation guide for persons with disabilities applies | ✓ S1 §5-6 |
| Fire resistance of elements | SBC 201 Ch.6/7 table for group R (R-2 typically Type I–V, 1–2 h) ⚠ verify | ⚠ |
| Electrical supply | 60 Hz; 127/220 V & 220/380 V (some areas 230/400 V) from SEC ⚠ verify with SEC for the plot; sockets British BS 1363 type G dominant ⚠ | ⚠ [S11] |
| Electrical docs | single-line diagram, load schedules, specs prepared by licensed office; generators in locked/acoustic rooms; external substations/panels inside plot, locked, screened | ✓ S1 §5-3 |
| Water tanks | combined ground+roof storage ≥ **5 days** demand; tank to septic pit **≥1.0 m**; pit to neighbour **≥2.0 m**, to street **≥1.0 m**; tank waterproofed | ✓ S1 §5-5(4-6) |
| Septic (no sewer) | clearances per SBC 702 Table 802.8, inside plot only | ✓ S1 §5-5(7) |
| Drainage | ground-floor drain connected separately to main, not on upper stack | ✓ S1 §5-5(8) |
| HVAC | SBC 501 ventilation/heating-cooling load calc; SBC 602 for residential envelope; recover A/C condensate where cooling load **>350 kW**; no A/C units/ducts on façades facing main streets | ✓ S1 §5-4(7), §5-10(4) |
| Energy | roof and external wall insulation per SBC 602 / SBC 601 U-values; green-roof type insulation for annex | ✓ S1 §5-2, §5-14(6) |
| Design temp (Riyadh summer) | ~46 °C DB (ASHRAE-type) – use SBC 501 Appendix table ⚠ verify | ⚠ |
| Structure | loads per SBC 301 (ASCE 7-derived), concrete per SBC 304 (ACI 318-derived); soil investigation (تقرير فحص التربة) required for apartment buildings (SBC 301-309) | ✓ S1 §5-2(2) |
| Concrete cover | per SBC 304 (ACI 318 baseline: slab/wall 20 mm, beam/column 40 mm, cast against soil 75 mm) ⚠ verify; hot, saline soils (sabkha) need extra cover & sulfate-resistant cement | ⚠ |
| Seismic/wind | Seismic zones from SBC 301 map (Red Sea/Gulf of Aqaba higher); wind basic speed per SBC 301 ⚠ verify per city | ⚠ |

---
## 6. Permit / approval drawing set
Process: Balady application by licensed office → Amanah technical review → NOCs (Civil Defense, SEC, NWC where applicable) → licence ⚠ [S10]. MOMAH requires design + supervision by MOMAH-approved offices, execution by approved contractors, and soil/materials testing by qualified labs ✓ [S1 §5-2, §6-2].

Typical order (⚠ per Amanah checklist; confirm in Balady):
| # | Sheet(s) | Must show |
|---|---|---|
| 0 | Documents | Deed/e-deed (صك), survey decision (قرار مساحي), plot & plan no., soil report, office/engineer licences |
| 1 | Site plan | Plot boundary + dims, deed area, **street names & widths**, setback lines with dimensions, building footprint, ground annexes, fence, gates, parking bays, driveway width, chamfers, pavement level, north arrow, coverage table (plot area / allowed % / proposed per floor) |
| 2 | Floor plans (basement, ground, first, annex, roof) | Room names + areas, door/window schedule tags, stairs, lifts, light shafts with dimensions, setbacks, levels, parapet heights, area table per floor |
| 3 | Elevations (4) & sections (≥2, through stairs and shafts) | Levels from mid-pavement, total height, ground-floor level (0.30–1.20 m), parapets, fence heights, projections |
| 4 | Door/window schedules & details | Opening sizes, glazing %, openable % |
| 5 | Structural | Foundation plan, column layout, slab/beam plans, schedules, sections, general notes (SBC 301/304, concrete grade, cover, soil bearing) |
| 6 | Electrical | Single-line diagram, load schedule, lighting/power plans, panel locations (inside plot), earthing |
| 7 | Mechanical / HVAC | Load calc summary, equipment schedule, plans, vent for baths/kitchens/parking |
| 8 | Plumbing & drainage | Water supply isometric, drainage layout, tank capacities (≥5 days), septic/connection, storm |
| 9 | Fire & life safety | Civil Defense approved layout for buildings (exits, extinguishers, alarm, sprinklers); signed by Civil-Defense-approved office |
| 10 | Energy / insulation | SBC 602/601 compliance forms/U-value table |

---
## 7. Common rejection reasons / mistakes
| Mistake | Why it is wrong / fix |
|---|---|
| Using old 12 m villa height, 2.0 m neighbour setback, 70% coverage | 2024 rules: 14 m, 1.5 m, 75% ✓ S1 — but check the Amanah has applied the 2024 rules to that plan |
| Measuring setbacks from the wall to the fence instead of from the **property line** | S1 §4(11): from property line to ground-floor building edge |
| Counting ground annexes outside the 75% | Ground coverage includes ground annexes ✓ S1 §4-1(1) |
| Annex >70% of floor below or counting stair/lift core out | Core is included in the 70% ✓ |
| Annex stair continuing to roof of annex; annex window directly onto neighbour | Both prohibited ✓ S1 §5-14(3,4) |
| Missing street widths on the site plan | Setback = 1/5 street width cannot be checked |
| Using the 1/5 rule for streets ≥30 m (front must be ≥6 m) | ✓ S1 §4-1(5) |
| Light shaft undersized or roofed | See §5.4 table ✓ |
| Wall of setback building >4.5 m | ✓ S1 §4-1(8) |
| AC units/ducts on façade toward main street; dishes on balconies | Prohibited ✓ S1 §5-10(4), §5-11(5) |
| Projections in side/rear setback; projection onto street <10 m wide | ✓ S1 §5-11 |
| No parking (1 / 2 per villa; 1.5 per flat) or ramp too narrow | ✓ §5.6 |
| Car entrance placed in corner chamfer | ✓ S1 §5-16(2) |
| Septic/tank clearances ignored | ✓ §5.7 |
| Fire plan not from Civil-Defense-approved office; fire plan missing exits | ✓ S1 §5-6(3) |
| Applying S1 numbers to hotels, rest houses (استراحات), high-rise, staff housing | Excluded from scope ✓ S1 §1-1 |
| Villa plan ignoring 12 m / 10 m plot-width limit when splitting floors into flats | ✓ S1 §4-1(11) |
| Arabic text exploded / SHX font → question marks in PDF | Use TrueType + MTEXT |
| Citing 2018 SBC editions after 30 Jun 2025 | 2024 edition mandatory ✓ S2 |

Riyadh/Jeddah notes: Riyadh Amanah posts building-code PDFs at `eservices.alriyadh.gov.sa/Documents/BuildingCodes/` (e.g. "T3.1": corner-plot secondary-façade setback rules; server unreachable this session ⚠). Riyadh approved (Jul 2025) stricter conditions for approving urban plans requiring infrastructure/public realm completed before construction ✓ [S5]. Riyadh also applies the "Riyadh urban code / height-by-corridor" overlays; Jeddah Amanah and Madinah/Makkah apply heritage-area and Haram-corridor height limits ⚠ — always request the plot's **zoning certificate (شهادة اشتراطات)** from the Amanah.

---
## 8. Sources
- [S1] MOMAH, اشتراطات إنشاء المباني السكنية (Residential Construction Requirements), Ministerial Decision 4500943139/1 – 1446H/2024: https://momah.gov.sa/sites/default/files/2024-07/ashtratat%20a%27nsha%20almbany%20alsknyt%20almnshwrt%20%60ly%20mwq%60%20alwzart%20.pdf (read in full; numbers above from it)
- [S2] SBC 2024 edition mandatory 30 Jun 2025: https://amlak.net.sa/en/73090/
- [S3] Secondary summary of residential code (maid room 10 m², ceiling 2.1 m): https://amlak.net.sa/en/59167/
- [S4] Press summary of 2024 changes (Al Watan): https://www.alwatan.com.sa/article/1150133
- [S5] Riyadh plan-approval conditions Jul 2025 (Okaz): https://www.okaz.com.sa/ampArticle/2206265
- [S6] Effective date 14 Jul 2024 / villa parking (search summary of Okaz 2165939): https://www.okaz.com.sa/ampArticle/2165939
- [S7] ICC SBC 201 egress course (confirms SBC 201 egress chapter; no numbers): https://shop.iccsafe.org/saudi-building-code-201-egress-and-design-of-exit-systems.html ; [S7b] Riyadh old audit form: https://mobapps.alriyadh.gov.sa/_layouts/RM_Pages/FormsDownload/BlS_Project_audit_Form1.pdf
- [S8] SCE circular on office licensing (Royal Decree M/36): https://www.saudieng.sa/Admin/DepartmentsDocuments/Circular No 3-40.pdf
- [S9] SBC Center restructuring (secondary): https://practiceguides.chambers.com/practice-guides/construction-law-2026/saudi-arabia/trends-and-developments
- [S10] Balady steps (commercial summary): https://www.capsulaa.sa/saudi-arabia-services/%D8%A5%D8%B5%D8%AF%D8%A7%D8%B1-%D8%B1%D8%AE%D8%B5%D8%A9-%D8%A7%D9%84%D8%A8%D9%84%D8%AF%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%B4%D8%B1%D9%88%D8%B7-%D9%88%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D9%86%D8%AF%D8%A7/
- [S11] Official SBC portal (not fetched; code texts are access-controlled): https://sbc.gov.sa
