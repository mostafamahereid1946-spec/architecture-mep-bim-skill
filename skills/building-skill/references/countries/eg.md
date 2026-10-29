# Egypt (جمهورية مصر العربية) — Drafting & Code Reference

Legend: **✓** = read this session in a primary/near-primary text (tag = source in §8). **⚠ verify** = drafter practice, news/secondary source, or memory only. Reader date assumed 2026.
**Coverage warning:** Egypt has no single published national table of setbacks/room minima that could be retrieved this session. Planning numbers are set by (a) Law 119/2008 + Executive Regulation (Decision 144/2009 and amendments), (b) the **approved strategic/detailed plan** and the **site-suitability statement (بيان صلاحية الموقع)** issued by the local planning authority, and (c) **NUCA / developer rules in new cities**. Unverified sections are labelled; do NOT invent setbacks — ask for the plot's planning statement. Egypt's code system (ECP) is HBRC-issued and ACI/Eurocode-influenced.

Hierarchy: **Law 119/2008 > Exec. Regulation 144/2009 (as amended) > Supreme Council for Planning & Urban Development approved heights/strategic plan > governorate/city decisions > NUCA/new-city rules**; all capped by Armed Forces Operations Authority height limits where applicable ✓ [E2].

---
## 1. Units, scales, sheets

| Item | Practice |
|---|---|
| Unit system | Metric. **Architectural & structural plan dimensions are usually in centimetres** (`300`, `120`) with **levels in metres** (`+0.00`, `+3.20`); site plan/ survey in metres; rebar diameters in mm (`Φ12`); stresses N/mm² (MPa) or kN/m² ⚠ practice. State on sheet: `الأبعاد بالسنتيمتر والمناسيب بالمتر / DIMS IN CM, LEVELS IN M` |
| Levels | `±0.00` = finished ground-floor level; site ties to street/pavement level (منسوب الرصيف) and to Survey Authority datum ⚠ |
| Language | Arabic primary on permit drawings; bilingual Arabic/English for consultants, NUCA, foreign-funded and mega-projects |
| Numerals | Western digits (0-9) in drawings and room schedules ⚠ practice |
| Dimension format | Whole numbers in cm; fractions in mm only for details (`2.5`); area in m² to 2 decimals (`مساحة 15.60 م²`) |
| North arrow / grid | North arrow on every plan; site plan north-up. Axes: Arabic or Latin letters one way, numbers other (`أ ب ج` / `1 2 3`) — Latin common in structural ⚠ |
| Date | DD/MM/YYYY Gregorian |

### 1.1 Typical scales ⚠ practice (no mandate found)
| Drawing | Scale |
|---|---|
| Location (موقع عام / كروكي) | NTS / 1:5000 / 1:2500 |
| Site plan (الموقع العام) | 1:200 – 1:500 |
| Plans (المساقط الأفقية), roof | 1:100 (1:50 small buildings) |
| Elevations (الواجهات), sections (القطاعات) | 1:100 / 1:50 |
| Kitchens, baths, stairs | 1:50 / 1:25 |
| Details | 1:20, 1:10, 1:5 |
| Structural plans (foundations, slabs/roof formwork "لوحات الشدات") | 1:100 / 1:50; sections & rebar details 1:20 – 1:10 |
| MEP | 1:100 / 1:50 |

### 1.2 Sheets & title block
| Item | Practice |
|---|---|
| Sizes | ISO A0–A3 (A1 and A0 common for permit); some local units still accept A3-folded sets ⚠ |
| Title block | Project (اسم المشروع) · Owner (المالك) · Location / plot no. (رقم القطعة) / district (الحي) / governorate (المحافظة) · Drawing title / no. / rev. / scale / date · Designing engineer / office name + **Engineers Syndicate (نقابة المهندسين) membership no. & stamp (ختم)** + signature · Drawn / checked / approved · Land-ownership ref ⚠ practice |
| Stamp | Application is filed **only through a licensed engineer or engineering office** and the engineer is legally responsible for the accuracy of the documents and compliance with planning/building conditions ✓ [E1 Art. 40-41]; engineering-syndicate membership of the supervising engineer is required ✓ [E7]; syndicate stamp and stamp-duty on each sheet ⚠ practice |

---
## 2. CAD layer & file naming standard

No national layer standard found ⚠. Offices use **AIA/NCS-style English layers** (`A-WALL`) or **in-house Arabic/English or numbered layers** (e.g. `01-WALLS`, `ELEC-LIGHT`); contractors and Gulf-funded work often request AIA/ISO 19650. Recommended default: AIA/NCS with ACI→CTB lineweights.

| Layer | ACI | LW (mm) | Content |
|---|---|---|---|
| A-WALL | 2 | 0.50 | Cut masonry/RC walls (brick 12/25 cm, block) |
| A-WALL-PATT | 8 | 0.13 | Wall hatches |
| A-DOOR | 4 | 0.25 | Doors/swings |
| A-GLAZ | 5 | 0.25 | Windows |
| A-FLOR-STRS | 6 | 0.25 | Stairs, steps, arrow, UP/DN |
| A-FLOR-OTLN | 7 | 0.35 | Slab edge, balconies (البلكونات) |
| A-FLOR-EVTR | 6 | 0.25 | Lift shaft |
| A-SITE-PROP | 1 | 0.50 | Plot boundary (حد الملكية) |
| A-SITE-SETB | 1 | 0.25 dashed | Setback / building line (خط التنظيم) |
| A-AREA | 3 | 0.13 | Area polylines |
| A-ANNO-DIMS | 3 | 0.18 | Dims |
| A-ANNO-TEXT | 7 | 0.18 | Notes, tags |
| A-ANNO-TTLB | 7 | 0.35 | Title block |
| A-GRID | 1 | 0.13 center | Axes |
| S-COLS | 1 | 0.50 | Columns (أعمدة) |
| S-BEAM | 4 | 0.35 | Beams (كمرات) |
| S-FNDN | 5 | 0.50 | Footings/raft (القواعد/اللبشة) |
| S-SLAB | 3 | 0.25 | Slab outline, solid/flat/ribbed |
| S-REBR | 2 | 0.18 | Reinforcement |
| M-HVAC-DUCT | 4 | 0.35 | Ducts |
| M-HVAC-EQPM | 6 | 0.35 | Split units, FCU, AHU |
| E-LITE | 2 | 0.25 | Lighting |
| E-POWR | 1 | 0.25 | Sockets/power |
| E-LTNG / E-SPCL | 3 | 0.25 | Low-current |
| P-DOMW | 5 | 0.25 | Water supply |
| P-SANR | 30 | 0.35 | Drainage |
| P-STRM | 150 | 0.35 | Roof/storm |
| FP-SPRK | 1 | 0.25 | Sprinklers |
| FP-HYDR | 1 | 0.35 | Fire hose cabinets/hydrants |
| FP-ALRM | 6 | 0.25 | Detection & alarm (Civil Defense) |

File naming ⚠ practice: `ProjectCode_Disc_Level_SheetNo_Rev.dwg`, e.g. `NC-045_A_GF_A101_R0.dwg`. **Submission format:** since permits are now processed through the technological centers and an electronic system (upload of drawings/documents, online fee payment, e-signature being rolled out) ✓ [E7][E10], send PDF (and DWG when the centre asks) per centre instructions — exact CAD rules not found ⚠.

---
## 3. Drafting conventions

| Item | Convention ⚠ practice |
|---|---|
| Text height on paper | Dim text 2.5 mm, notes/room names 3.0–3.5 mm, titles 5 mm, sheet title 7 mm |
| Dim style | Architectural tick, 3 strings: overall / axes / openings; cm integer |
| Symbols | Section arrows with sheet ref; level triangles with `±0.00`; door/window tags `D1/W1` or `ب1/ش1`; room tag name + area |
| Grid bubbles | Ø 8–10 mm paper; structural axes on all plans |
| Hatch | RC = ANSI31 + dots; red brick = ANSI31 sparse or AR-BRSTD; cement block = ANSI37; stone cladding = AR-B88; earth = EARTH; sand = AR-SAND; screed/mortar = dots; insulation = wavy line. Provide a legend |
| Wall types | Exterior brick/block 25 cm; interior 12 cm; RC columns typically shown solid black in structure sheets ⚠ practice |
| Arabic in AutoCAD | Use TrueType Unicode fonts (Arial, Tahoma, Simplified Arabic, Sakkal Majalla). Use **MTEXT** so letters connect and RTL order is correct; avoid SHX/DTEXT for Arabic; keep digits as Western; don't explode text; if PDF shows disconnected letters, re-plot with TrueType text "as text" and check the font is embedded. Legacy offices use "Arabic CAD" fonts that break on other PCs — convert to Unicode before issue ⚠ |
| Bilingual labelling | Arabic right / English left; `غرفة معيشة LIVING` |

---
## 4. Governing codes & authorities

| Discipline | Code | Current edition | Enforced by |
|---|---|---|---|
| Building & planning law | **Unified Building Law No. 119 of 2008** (Official Gazette no. 19 bis (a), 11 May 2008 ✓ [E1]) | Amended 2015/2021/2024 (cabinet-approved amendment bill sent to Parliament Oct 2024 — final status ⚠) ✓ [E7] | Local administrative unit (الوحدة المحلية / الحي / مجلس المدينة); technological centres |
| Executive Regulation | Min. Decision **144/2009** (6 Apr 2009; Waqa'i 82, 8 Apr 2009) ✓ [E5b] — amended by **200/2010** (Arts 19, 26, 27, 57, 58, 103(5), 108, 115, 116, 135 bis; Waqa'i 98, 29 Apr 2010) ✓ [E5]; **410/2021** added Arts 110 bis, 112 bis, 117 bis; **943/2024** (3 Sep 2024) replaced those ✓ [E3][E6]; Art. 26 village-heights amendment Jan 2025 ✓ [E2] | Current consolidated text — obtain from Waqa'i/ministry ⚠ | Ministry of Housing (وزارة الإسكان) with Ministry of Local Development (وزارة التنمية المحلية) |
| Enabling law for codes | Law 6/1964 ✓ [E4] | | HBRC |
| Loads | **ECP 201** (Design Loads) — edition 2012 cited by designers ⚠ | verify | HBRC (المركز القومي لبحوث الإسكان والبناء); local unit requires compliance |
| Soil / foundations | **ECP 202** | ⚠ edition | HBRC |
| Reinforced concrete | **ECP 203** — 2020 edition; English version adopted by Housing Ministry Decision **550/2024**, published Waqa'i 31 Jul 2024 ✓ [E4] | 2020 | HBRC |
| Steel structures, masonry, seismic | Egyptian steel code (limit-state & ASD), masonry code; seismic provisions inside ECP 201 ⚠ numbers/editions | verify | HBRC |
| Electrical installations | Egyptian Code for Electrical Installations in Buildings (HBRC) ⚠ number/edition | verify | HBRC; Egyptian Electricity Holding Co. distribution companies for connection |
| Fire protection | Egyptian Code for Fire Protection in Buildings (HBRC; ECP 126 per memory ⚠) — law Art. 49 makes fire-insurance conditions per this code a permit condition ✓ [E4b] | verify | **Civil Protection / Civil Defense (الحماية المدنية)** |
| Plumbing / sanitary | Egyptian Code for Plumbing/Sanitary Works (ECP 101 per memory ⚠) | verify | HBRC; water & sewage holding co. |
| HVAC | Egyptian Code for Heating, Ventilation & Air Conditioning (ECP 10x ⚠) | verify | HBRC |
| Energy efficiency | Egyptian Energy Efficiency Code(s) for buildings (residential / commercial; ECP 305/306 per memory ⚠) | verify | HBRC; Housing Ministry |
| Accessibility | Egyptian code for accessibility of persons with disabilities in buildings & outdoor spaces ⚠ number | verify | HBRC; local unit |
| Lifts | Law Art. 50: lift count suited to height/floors/units/use; installed by firms registered with the Egyptian Federation for Construction & Building Contractors ✓ [E4b] | — | Local unit |
| Professional body | **Engineers Syndicate (نقابة المهندسين)** — licensed engineer/office signs & stamps ✓ [E1][E7] | — | Syndicate |
| New cities | **New Urban Communities Authority (NUCA, هيئة المجتمعات العمرانية الجديدة)** — own plot-specific "اشتراطات البناء" per city/district and developer booklets (كراسة الشروط) ⚠ not retrieved | per city | NUCA city authority (جهاز مدينة) |
| Planning | GOPP (الهيئة العامة للتخطيط العمراني); Supreme Council for Planning & Urban Development approves heights in strategic plans ✓ [E5] | — | |
| Height ceiling | Armed Forces Operations Authority (هيئة عمليات القوات المسلحة) airspace/height limits ✓ [E2] | — | |

---
## 5. Key numbers

### 5.1 Law 119/2008 — permit, height, structure of control
| Rule | Value | Source |
|---|---|---|
| Permit required for any building / alteration; issued under conditions in force on issue date | Art. 39 | ✓ E1 |
| Application filed via licensed engineer/office with required documents; engineer responsible for conformity | Art. 40-41 | ✓ E1 |
| Authority must issue the permit within **30 days** of the engineer's readiness certificate; silence past deadline = **deemed approval** | Art. 41-42 | ✓ E1 (⚠ confirm numbering vs Gazette) |
| Permit validity: start within **1 year**, else obtain a one-year extension certificate | Art. 52 | ✓ E1 (⚠ numbering) |
| Insurance policy required: works **≥ EGP 1,000,000**, buildings **≥4 floors**, and extensions | Art. 46 | ✓ E1 |
| Interim height rule where no approved detailed plan: height ≤ **1.5 x street width**, max **36 m** | Law Art. 15 (interim provisions) | ✓ E1 |
| Penalties: building without permit — prison up to 5 years and fine of 2–3x value of works; daily fine 1% of works for non-compliance with removal order | Arts. 102, 107 | ✓ E1 |
| Engineer violating permit articles: fine 5–10% of works value (min EGP 50,000), possible removal from register | Art. 103 | ✓ E1 |

### 5.2 Executive Regulation (as amended) — streets, heights, projections
| Rule | Value | Source |
|---|---|---|
| Min street width to build on — cities, inside built-up area | **6 m** (roads without approved alignment) | ✓ E5 Art. 26 (2010) |
| — cities, urban extension | **10 m** | ✓ E5 |
| — villages, inside built-up: internal / main road / regional ring road | **4 m / 6 m / 8 m** | ✓ E5 |
| — villages, extension | **6 m** | ✓ E5 |
| If existing street narrower than minimum when building/rebuilding | set back by **half the shortfall on each side** until width achieved | ✓ E5 Art. 26 |
| Building heights (cities) | per Supreme Council–approved conditions in the strategic plan; may differ within a zone | ✓ E5 Art. 26 |
| Village heights (amended Jan 2025): street ≥4 m | ground + 2 repeated, **10 m** | ✓ E2 |
| street ≥6 m | ground + 3 repeated, **13 m** | ✓ E2, E4b |
| street ≥8 m | up to **2 x street width** | ✓ E2 (all subject to Armed Forces height limits) |
| Temporary density (no general plan): villages / cities | built-up total ≤ **4x / 6x** plot area ⚠ interpretation of "كثافة" | ✓ E5 Art. 19 (2010) |
| Projections: open balconies / towers (أبراج) | ≤ **10% / 5%** of street width and never > **1.25 m** | ✓ E5 Art. 103(5) |
| Balcony distance from neighbour boundary | no open balcony within **1.50 m** | ✓ E5 |
| Internal facade angle <180° | no projections within **1.50 m** of angle midpoint | ✓ E5 |
| Tower length | ≤ half the facade length (non-residential exempt) | ✓ E5 |
| Use on residential building ground & first floor on roads >10 m wide | commercial/administrative allowed | ✓ E3 |
| Tolerances the governor may waive for **existing** violations (Art. 135 bis): rooms/baths/kitchens 5% (area ≥95% of required); courts (أفنية) dims/areas 10%; max heights 10% (no extra floors); projections 10%; stair length 5% | do NOT design to the tolerance | ✓ E5 |
| Setbacks (ردود أمامية/جانبية/خلفية), courts, light-well minima, plot frontage | Fixed by the approved detailed plan / site-suitability statement for the plot; no national table retrieved | ⚠ ask the local planning authority |
| Plot minimum | 200 m² under the 2008 law regime; March-2021 conditions (≤175 m² built 100%, larger plots 70% cover, 8.5 m min frontage) were **cancelled** and 119/2008 restored in old cities; **new cities unchanged** | ✓/⚠ news [E3][E6b]; confirm |
| Garage | Each new building must provide garage/parking per 119/2008 regime | ⚠ news [E3]; ratio not retrieved |

### 5.3 Rooms, stairs, egress, parking — NOT retrieved from primary text
The Executive Regulation has detailed minimum room areas/widths, ceiling heights, stair widths, courts and parking ratios, but the consolidated text could not be downloaded this session. Practice-level values below are **⚠ verify against the Executive Regulation / local unit**:
| Item | Commonly applied ⚠ |
|---|---|
| Habitable room ceiling | ~2.70 m clear; kitchens/baths ~2.40–2.70 m ⚠ |
| Stairs (residential) | riser ~15–17.5 cm, tread ≥25–30 cm, clear width ~1.00–1.20 m ⚠ |
| Guard/balustrade | ~1.00–1.10 m ⚠ (ECP fire/accessibility codes) |
| Door | main 1.00 m; rooms 0.90 m; baths 0.70–0.80 m ⚠ |
| Fire escape distance, exit width | per Egyptian Fire Protection Code tables by occupancy ⚠ |
| Lifts | number by Art. 50 / exec reg table ✓ rule, ⚠ numbers |
| Parking | per exec reg / local decisions (garage mandatory in new buildings ✓ [E3]) ⚠ ratio |

### 5.4 Structural basics (ECP 201 / 203)
| Item | Value | Source |
|---|---|---|
| Live load, residential rooms | **2 kN/m²** | ⚠ lecture [E8], ECP 201 Ch.4 table |
| Stairs, kitchens, bathrooms | **3 kN/m²** | ⚠ lecture [E8] |
| Offices | 2.5 kN/m² (record/filing rooms more) | ⚠ lecture [E8] |
| Retail shops (ordinary) | 5 kN/m² | ⚠ lecture [E8] |
| Balconies | 3–4 kN/m² (residential/public) | ⚠ verify |
| Demountable partitions allowance | ≥1.0 kN/m² minimum (secondary) | ⚠ [E9] |
| Load factors / design method | ECP 203 limit-state: 1.4 DL + 1.6 LL (ECP 203-2007 baseline; 2018/2020 editions ECP 201 combos may differ) | ⚠ |
| Concrete / steel grades | fcu 25–40 N/mm² (cube); rebar 240/350, 360/520, 400/600 (yield/ultimate N/mm²) | ⚠ practice |
| Concrete cover | slabs ~25 mm, beams/columns ~25–30 mm, footings ~50–70 mm against soil, ECP 203 durability table governs | ⚠ verify |
| Soil investigation | boreholes report required per ECP 202 and local unit | ⚠ |
| Seismic | ECP 201 seismic map (zones 1–5) per site ⚠ | ⚠ |

### 5.5 MEP basics
| Item | Value | Source |
|---|---|---|
| Supply | 220/380 V, 3-phase 4-wire, 50 Hz; single-phase 220 V 50 Hz; sockets Type C/F (Schuko) 16 A | ⚠ general knowledge — confirm with distribution company |
| Fire | Fire insurance + Egyptian fire code compliance is a permit condition (Art. 49; fine EGP 20,000–50,000 for violating Arts 49/50, heavier if deaths) | ✓ E4b |
| Water | Tanks/pumps and sanitary design per plumbing code ⚠; sewage connection per water company |
| AC | Split/central design per HVAC code ⚠; outdoor units on dedicated balcony niches shown on elevations (local units object to street-facing units ⚠) |

### 5.6 New cities (NUCA) & other zones
| Item | Rule |
|---|---|
| Authority | NUCA city authority (جهاز المدينة) approves drawings for plots it allocated; planning rules (coverage, setbacks, floors, use) come from the plot's allocation contract and the city/district building booklet — **not** the generic governorate rules ⚠ not retrieved |
| March-2021 city conditions | The cancellation applies to old cities/neighbourhoods only; new-city conditions unchanged ✓ [E6] |
| What to request before drawing | Allocation contract/plot plan, district building conditions (اشتراطات البناء للحي), max floors & height, coverage %, setbacks, parking ratio, façade/colour rules, utility-connection NOCs |
| Heritage / Nile / coastal zones | Separate height & use controls (NOPH, Ministry of Antiquities, Nile Law) ⚠ not retrieved |

### 5.7 Arabic title-block text (copy-ready)
`المشروع` Project · `المالك` Owner · `رقم القطعة` Plot no. · `الحي / المدينة / المحافظة` District/City/Governorate · `اللوحة` Sheet · `المقياس` Scale · `التاريخ` Date · `المهندس المصمم` Design engineer · `رقم القيد بالنقابة` Syndicate reg. no. · `ختم النقابة` Syndicate stamp · `المراجعة` Rev. · `شمال` North · `الردود` setbacks · `خط التنظيم` building/alignment line · `بيان صلاحية الموقع` site-suitability statement · `قطاع` section · `واجهة` elevation · `مسقط أفقي` plan · `دور أرضي / متكرر / سطح` ground / typical / roof.

---
## 6. Permit / approval drawing set
Process (post-2024 simplification): file through the **technological centre for planning & building (المركز التكنولوجي)**; Housing Ministry circular reduced steps from **15 to 8**, all completed inside the centre without separate university/agency visits ✓ secondary [E7]; first fully electronic permits issued (New Cairo, Abu Redis) ✓ [E10]. Typical required documents: national ID, **survey map approved by Survey Authority**, ownership deed or POA, **site-suitability certificate (بيان صلاحية الموقع)**, engineering drawings, permit-fee receipt, and insurance policy where required ✓ [E4b]; engineer's contract/POA and syndicate card ✓ [E4b][E7]; soil test for larger buildings ⚠ [E7].

| # | Sheet(s) | Must show ⚠ practice |
|---|---|---|
| 1 | Site plan / location | Plot boundary with dims & area from deed vs survey, street names & widths, alignment/building lines, setbacks, adjacent plots, north, building footprint, entrances, garage |
| 2 | Architectural plans (basement, ground, typical, roof, machine room) | Room names/areas, dims (cm), door/window tags, stairs, lift, light wells/courts with dimensions, levels, areas table per floor |
| 3 | Elevations (all sides) | Total height vs street width allowance, floors count, projections (≤10% street width / 1.25 m ✓), parapet |
| 4 | Sections (≥2 incl. stair & court) | Floor-to-floor, slab thickness, levels |
| 5 | Structural | Foundation plan, columns schedule, slab/beam layout, rebar details, notes citing ECP 201/203 and soil bearing; signed by structural engineer |
| 6 | Electrical, plumbing/drainage, HVAC (when required) | Single-line, risers, tank/septic, equipment |
| 7 | Fire protection | Per Egyptian fire code; Civil Protection approval for qualifying buildings |
| 8 | Insurance/engineer undertakings | Insurance policy for ≥4 floors ✓; syndicate stamps |
| 9 | NUCA submissions | Via city authority portal with plot allocation contract & developer rules ⚠ |

Vertical extension (التعلية) needs engineer's safety report — Art. 43 ✓ [E1].

---
## 7. Common rejection reasons / mistakes
| Mistake | Why/fix |
|---|---|
| No site-suitability statement (بيان صلاحية الموقع) or expired (the 2008 regime valid only ~2 weeks per news ⚠) | Obtain fresh statement ✓ [E3] |
| Building height not matching street width / plan heights, or above Armed Forces limit | ✓ E2, E5 |
| Street narrower than minimum and no half-shortfall setback | ✓ E5 Art. 26 |
| Projections > 1.25 m or > 10% of street width; balcony within 1.5 m of neighbour | ✓ E5 Art. 103(5) |
| Changing residential unit to commercial without road >10 m | ✓ E3 |
| Missing garage / fewer parking than local requirement | ⚠ E3 |
| Courts and light wells under size, built over | Violations; tolerance 10% is only for legalising existing violations ✓ E5 |
| Using the cancelled March-2021 rules (175 m², 100%, 8.5 m frontage) in old cities | ✓ E3, E6b |
| Applying village heights (10 / 13 m / 2x street) to a city | Village-only ✓ E2 |
| Missing insurance policy for ≥4-floor or ≥EGP 1M works | ✓ E1 Art. 46 |
| Drawings not stamped by syndicate engineer / office | ✓ E1, E7 |
| Fire and lift provisions ignored (Arts 49-50) | ✓ E4b |
| Arabic text as SHX / exploded text, unreadable in PDF | MTEXT + TrueType |
| Dimension units mixed (cm vs m) | Declare and apply one unit per sheet |
| Designing to ECP 203 old edition (2007/2018) after 2020 adoption | Check which edition the local authority requires ⚠ |

---
## 8. Sources
- [E1] Law 119/2008 text (Arabic Wikisource, reproduces Gazette 19 bis (a), 11 May 2008): https://ar.wikisource.org/wiki/قانون_البناء_الموحد_119_لسنة_2008_(مصر)
- [E2] Art. 26 village heights, Jan 2025 (Masrawy): https://www.masrawy.com/news/news_egypt/details/2025/1/24/2715006
- [E3] Cancellation of 2021 conditions / return to 119/2008 (Egypt Telegraph, 27 Sep 2024): https://www.egypttelegraph.com/77002
- [E4] Housing Min. Decision 550/2024 adopting ECP 203-2020 English: https://alberonsy.com/?p=4909 ; [E4b] Law 119 summary incl. Arts 49-50, documents (Banker.news, 16 Jan 2026): https://banker.news/123330
- [E5] Min. Decision 200/2010 amending Exec. Reg. (Arts 19, 26, 27, 103(5), 135 bis): https://www.laweg.net/framePlain.aspx?action=ViewActivePages&ItemID=41095&Type=6&NID=52893 ; [E5b] Decision 144/2009: https://www.laweg.net/framePlain.aspx?action=ViewActivePages&ItemID=78690&Type=6&NID=96843 ; catalogue: https://manshurat.org/node/12555
- [E6] Decision 943/2024 (AqarMap): https://aqarmap.com.eg/ar/advice/?p=25512 ; [E6b] same
- [E7] Ministry of Housing real-estate blog (permits, amendments Oct 2024): https://blogs.realestate.gov.eg/?p=85847 ; https://blogs.realestate.gov.eg/news/egypts-unified-building-law-amendments-aim-to-streamline-urban-development/
- [E8] ECP 201 live-load lecture (YouTube, secondary): https://www.youtube.com/watch?v=L82ROZX8BoM
- [E9] ECP 201 lecture notes (Benha Univ., secondary): https://feng.stafpu.bu.edu.eg/Civil Engineering/2478/crs-18926/Lecture 1.pdf
- [E10] First electronic permits: https://blogs.realestate.gov.eg/news/first-digitized-building-permit-issued-in-abu-redis-amidst-streamlined-procedures/ ; https://blogs.realestate.gov.eg/news/minister-of-housing-announces-the-issuance-of-the-first-fully-electronic-building-permit-from-the-new-cairo-city-authority/
- HBRC (code publisher; not fetched): https://hbrc.edu.eg
