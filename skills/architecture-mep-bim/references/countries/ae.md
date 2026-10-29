# United Arab Emirates — Drafting & Code Reference

Legend: **✓** = read this session from an official or near-official text (Dubai Building Code 2021 text as hosted on a SlideShare copy of the u.ae PDF; Dubai Municipality / DMT / DEWA / Al Sa'fat official pages; Abu Dhabi Media Office release) — URL in §8. **⚠ verify** = secondary/news source, drafter practice, or not found. **The UAE has no single national building code** — each emirate (and each free-zone authority) runs its own regime. Always ask: **Dubai (mainland) / Abu Dhabi / Sharjah / other emirate / free zone (DIFC, DMCC, JAFZA, DAFZA, Trakhees-regulated…)?** Default below = Dubai mainland, with Abu Dhabi notes. Source tags [D1]… in §8.

**Villa rule of thumb:** in Dubai, setbacks/height/coverage come mainly from the **plot's Affection Plan / DCR (development control regulations)** or the master-developer guidelines; the DBC supplies fallbacks only [D1 B.4.2.3]. **Do not invent coverage/height for a plot — ask for the Affection Plan / NOC.**

---
## 1. Units, scales, sheets

| Item | UAE practice |
|---|---|
| Unit system | Metric. **DBC A.12.1:** dimensions in **mm without unit**, except values > 1000 mm written in **metres with unit (m)**; dimensions not marked min/max are absolute; counts (parking, fixtures) from fractions **round up** ✓ [D1] |
| Levels | Dubai levelling reference **Port Rashid** datum ✓ [D1 A.11]; show `FFL +0.00 = DMD/Plot level` + road level |
| Horizontal datum — Dubai | **Dubai Local Transverse Mercator (DLTM)**, WGS84-based, EPSG:3997: CM 55.3333°E, k = 1, FE 500 000 m, FN 0 ✓ [D1 A.11][D8] |
| Horizontal datum — Abu Dhabi/others | Often UTM Zone 40N (Nahrwan 1967 EPSG:27040 legacy; WGS84/UTM 40N modern) ⚠ — **confirm ADM/DMT survey spec** [D9] |
| Language | **English + Arabic**; Arabic copy legally prevails but drawings mostly English with Arabic title block/notes ⚠ practice |
| Date | dd/mm/yyyy (Gregorian) ⚠ |
| North arrow | Required on site/plan; project north vs true north noted ⚠ |
| Area units | m²; plot area from title deed/Affection Plan, **GFA excludes villa basements and service attics < 2.15 m high** ✓ [D1 A.5/def.] |
| Dimension style | DBC style: `3000`, `1.2 m`, `15 m` (see above); consultants often draw all in mm on plans, m on site plans ⚠ |

### Typical scales (practice ⚠ — DM/ADM issue drawing checklists via their e-systems)
| Drawing | Scale |
|---|---|
| Location/key map | 1:1000 – 1:5000 |
| Site plan (setbacks, gate, levels, services, parking) | 1:200 (1:100 small plots) |
| Floor plans, roof plan | 1:100 (1:50 for details/typical unit) |
| Elevations, sections | 1:100 (1:50) |
| Wall sections / details | 1:20 – 1:5 |
| Structural GA / foundation | 1:100 / 1:50 |
| MEP layouts | 1:100; riser/SLD NTS |
| Fire / evacuation plans | 1:100 |

**Sheets:** ISO A0 841x1189 / A1 594x841 / A3 297x420; A1 standard for permit prints, A3 for booklets ⚠.

### Title block (bilingual)
Authority + permit/application no. (رقم الطلب / رقم الرخصة) · Project (اسم المشروع) · Owner (المالك) · Plot no. + Community/Sector (رقم القطعة / المنطقة) · Makani no. (Dubai) ⚠ · Consultant (الاستشاري) + **DM/ADM registration no.** · Contractor (المقاول) · Drawing title (عنوان المخطط) · Scale (المقياس) · Date (التاريخ) · Sheet no. (رقم اللوحة) · Revision (المراجعة) · Drawn/Checked/Approved · Consultant stamp & engineer signature (ختم وتوقيع) · Disclaimer "all dimensions in mm unless noted" ⚠.

---
## 2. CAD layer & file naming standard

**No single published mandatory layer standard** was found for Dubai Municipality; Abu Dhabi Municipality publishes CAD/BIM submission specs (naming, coordinate system, file format) and references **ISO 19650** [D9] ⚠ (document not read — fetch latest from ADM/DMT). Consultants typically use **AIA CAD layer guidelines** (`A-WALL`) or **BS 1192/ISO 13567** ⚠; large Dubai/Abu Dhabi developer & government BIM projects use **ISO 19650 CDE naming** `PROJ-ORG-ZONE-LEVEL-TYPE-DISC-NNNN` ⚠.

### Submission requirements to honour ⚠ confirm in current e-service checklist
- **DWG** (AutoCAD 2013–2018 ⚠) + signed PDF (and DWF for some e-services ⚠); XREFs bound/ detached; purge; no proxy objects.
- **Dubai:** site plan in **DLTM**, plot polygon from DM survey / Affection Plan; **Makani** and plot IDs ⚠. Survey Department supports coordinate transformation of legacy Clarke-1880 UTM files [D8].
- **Abu Dhabi:** coordinates per ADM spec [D9]; Estidama/PVRS submittals separate [D11].
- Areas drawn as closed polylines; each floor in own layout.

### Naming
`<PlotNo>-<Disc>-<Type>-<Level>-<Rev>.dwg` e.g. `DXB-123-A-PL-GF-R01.dwg`; sheet nos `A-101…`, `S-101…`, `E-101…`, `M-101…`, `P-101…`, `FF-101…` ⚠ practice.

### Example layers (AIA-style; ACI colour / lineweight mm) ⚠ practice
| Layer | Content | ACI | LW |
|---|---|---|---|
| A-WALL | Blockwork/RC walls (cut) | 7 | 0.50 |
| A-WALL-PRHT | Partitions/parapets | 8 | 0.25 |
| A-DOOR | Doors + swings | 3 | 0.25 |
| A-GLAZ | Windows/curtain wall | 5 | 0.25 |
| A-FLOR-STRS | Stairs | 6 | 0.25 |
| A-FLOR-OTLN | Slab edge, basement outline | 4 | 0.35 |
| A-AREA | Area polylines (closed) | 2 | 0.13 |
| A-ANNO-DIMS | Dimensions | 1 | 0.18 |
| A-ANNO-TEXT / -TEXT-AR | English / Arabic text | 7 | 0.18 |
| A-SITE-BNDY / A-SITE-SETB | Plot line / setback lines | 1 / 4 | 0.70 / 0.35 |
| A-SITE-FENC | Boundary wall, gate | 30 | 0.35 |
| S-COLS / S-BEAM / S-SLAB / S-FNDN | Columns / beams / slabs / footings | 7/2/4/6 | 0.50/0.35/0.25/0.50 |
| M-HVAC-DUCT / M-HVAC-EQPM | Ducts / split units | 5 | 0.25 |
| E-LITE / E-POWR / E-DIST | Lighting / sockets / DB | 2 / 3 / 1 | 0.18 |
| P-SANR-PIPE / P-DOMW-PIPE | Drainage / water | 3 / 5 | 0.25 |
| FP-SPRK / FP-ALRM / FP-EXTG | Sprinklers / detection / extinguishers | 1 / 6 / 1 | 0.25 |
| Defpoints | non-plot | — | — |

---
## 3. Drafting conventions

| Topic | Convention |
|---|---|
| Text heights on paper | 2.5 mm notes; 3.5 mm tags; 5–7 mm titles; Arabic ≈ +10 % taller ⚠ |
| Bilingual | Room names English + Arabic (غرفة نوم، صالة، مجلس، مطبخ، حمام، غرفة خادمة، غرفة سائق، غرفة خدمات، مخزن، مدخل، سطح، بدروم/قبو). Arabic right-aligned beneath/beside English ⚠ |
| Numerals | Western (0-9) on drawings ⚠ |
| Dimension chain | DBC style: mm, no units; > 1000 mm as `1.2 m` ✓ [D1 A.12] |
| Stair note | `Riser 150-165 / tread 300` external & regular-use stairs; `riser ≤180 / tread ≥280` general ✓ (§5.3) |
| Setbacks | Dimension from plot line to each facade at each floor; state source ("Affection Plan", "DBC Table B.1", "Home First 1.5 m") ⚠ |
| Gate | Show gate level **≥ +300 mm above road edge or 2–5 % slope** ✓ [D1 B.4.2.1] |
| Hatch | Blockwork diagonal; RC ANSI31 + dots; insulation zig-zag; earth ANSI37; sand/screed dots; marble/tile grid ⚠ |
| Section/elevation | Circle tags with sheet no.; elevations named by cardinal (شمالية…) ⚠ |
| Symbols | Electrical: BS EN 60617/IEC; fire symbols per UAE FLSC drawings ⚠ |
| Fire plan notes | Show fire-rated walls/doors (rating hr), exit signs, travel distance arrows ⚠ |

### Arabic glossary for bilingual sheets (⚠ practice terms)
| English | Arabic |
|---|---|
| Setback | الارتداد |
| Plot | قطعة الأرض |
| Plot coverage / built-up area | نسبة البناء / مساحة البناء |
| Basement | القبو / البدروم |
| Ground / First / Roof floor | الطابق الأرضي / الأول / السطح |
| Majlis / Service annex | المجلس / ملحق الخدمات |
| Boundary wall / Gate | السور / البوابة |
| Civil Defence / Municipality | الدفاع المدني / البلدية |
| Affection plan (Dubai) | مخطط الأرض (Affection Plan — Arabic term ⚠) |
| Building permit / NOC | رخصة البناء / شهادة عدم ممانعة |
| Stair / Lift / Corridor | الدرج / المصعد / الممر |

---
## 4. Governing codes & authorities

| Discipline | Code / document | Edition | Enforced by |
|---|---|---|---|
| Building (Dubai) | **Dubai Building Code (DBC) 2021** — Decree No. 45 of 2021; approved Oct 2020; implementation 20/30 Dec 2021 (sources differ) ✓ [D1][D2][D3]. Parts: **A General · B Architecture · C Accessibility · D Vertical transportation · E Building envelope · F Structure · G Incoming utilities · H Indoor environment · J Security · K Villas (& townhouses)** ✓ [D1] | 2021 | Dubai Municipality (بلدية دبي), Trakhees (PCFC) in its zones |
| Building (Abu Dhabi) | **ADIBC (Abu Dhabi International Building Code) 2013** ⚠ not read; DMT **Private Housing / villa regulations** (amended Sep 2025) ✓ [D6]; Estidama PBRS/PVRS | ⚠ | Dept. of Municipalities & Transport (DMT), Abu Dhabi Municipality; UPC for planning |
| Fire & life safety | **UAE Fire and Life Safety Code of Practice** (Ministry of Interior/Civil Defence); update of 2011 ed. launched Intersec 2017, 20 chapters; DBC cites **2018** ed. ✓ [D4][D5] — **⚠ confirm if newer edition issued** | 2018 (2017 launch) | Civil Defence (الدفاع المدني) Dubai / Abu Dhabi / federal |
| Electrical (Dubai) | **DEWA Regulations for Electrical Installations 2017 edition** (supersedes 1997; refs IET 17th ed. BS 7671 & IEC) ✓ [D7] | 2017 + circulars | DEWA (هيئة كهرباء ومياه دبي) |
| Electrical (Abu Dhabi) | ADDC / AADC Electricity Wiring Regulations ⚠ not read | ⚠ | ADDC (Abu Dhabi), AADC (Al Ain) |
| Water/drainage | DEWA water regs; DM drainage/sewage (STP/sewer) ⚠ | ⚠ | DEWA / DM |
| Green building (Dubai) | **Al Sa'fat – Dubai Green Building System** (replaced 2010 Dubai Green Building Regs on **19 Oct 2020**); Admin Resolution 154/2020; **2nd ed. Jan 2023**; **Silver Sa'fa mandatory**, Gold/Platinum optional ✓ [D10] | 2023 | Dubai Municipality |
| Green building (Abu Dhabi) | **Estidama Pearl Rating System**; **Pearl Villa Rating System (PVRS)**: ≥ **1 Pearl** for new villas since Sept 2010; 13 required + 32 optional credits (177 pts) ✓ [D11] | PBRS/PVRS | DMT / UPC |
| Structure/wind | DBC Part F; Admin Resolution 37/2021 wind-load table tied to ASCE 7 ✓ [D12] (values not extracted) | 2021 | Dubai Municipality |
| Roads/access | RTA (Dubai), ITC/DMT (Abu Dhabi) NOCs ⚠ | — | RTA / DMT |
| Free zones / Trakhees | **Trakhees (PCFC)**: DBC 2021 adopted for its jurisdiction via CED circular CEDGR-135 (Dec 2021) ✓ [D3]; **DIFC, DMCC, DAFZA, DSO, JAFZA etc. have own authority rules** — check zone regs ⚠ | — | Zone authority |

---
## 5. Key numbers

### 5.1 Villa setbacks / coverage / height

**Dubai mainland**
| Item | Value | Source |
|---|---|---|
| Governing source | **Affection Plan / DCR takes precedence**; DBC Table B.1 applies only where silent ✓ | [D1 B.4.2.3] |
| Default DBC setback from neighbour (G to G+3) | **3 m**; road side 0 m; basement 0 m ✓ | [D1 Table B.1] |
| Default DBC setback by height (G+4…G+10) | 3.75 / 4.5 / 5.25 / 6 / 6.75 / 7.5 / 7.5+ m ✓ | [D1] |
| Setback ≤ 1.5 m | "requires no setback" (DBC wording) ✓; sikka setback measured from centreline (max 3 m width from centre if sikka > 6 m); cemetery plots ≥ 3 m ✓ | [D1] |
| Floor-count height rule | **6 m per floor** for allowed floors (G+10 = 66 m); does not limit individual floor heights ✓ | [D1 B.4.2.2] |
| Plot coverage | DBC B.4.2.6 gives **no numeric limit** ✓; DM FAQ (secondary summary): *no maximum built-up area for private villas, but setbacks on planning map must be met* ⚠ [D13] | — |
| **Home First (Mar 2025)** | Min villa setback **reduced to 1.5 m**; **+1.5 m extra for rooftop floors** on all boundaries; 100 % second-floor extension; service annex **≤ 8 m, two floors**, no setback between annex and villa; townhouses adjacent across two plots; written neighbour consent to remove shared-boundary setback; windows not to overlook neighbours — **reported for Emirati owners; reports differ on wider scope; effective text not read ⚠** | [D14] |
| Boundary wall | Older DM code: ≤ **10 ft (~3.05 m)** incl. hedges, inside plot only ⚠ (idoc.pub copy); master-developer limits tighter (Emaar ≈ 2.0–2.2 m, Nakheel ≈ 1.8–2.0 m ⚠ unofficial) | — |
| Part K Villas (setbacks, annex, majlis, parking) | **⚠ not read — obtain DBC Part K from the PDF** | [D1] |

**Abu Dhabi (DMT amendment, 9–10 Sep 2025)** ✓ [D6]: front setback from street **1.5 m**; full flat roof buildable with **1.5 m setback**; closed lightweight rooftop majlis not counted in land-use %; guest annex may have first floor or basement (not against boundary wall); shading structures exempt from footprint; two villas may share a side without wall by owners' agreement. Coverage %, heights, other setbacks **not stated ⚠** (see plot's DMT/UPC "Plot Specifications"). PVRS ≥ 1 Pearl for villas; villa-size PVRS cap historically 2,000 m² ⚠.

### 5.2 Rooms, ceilings (DBC Part B, Dubai) ✓ [D1]
| Item | Value |
|---|---|
| Residential living/bedroom | **10.5 m²**, min dimension **3 m** (Table B.3) |
| Studio | 21 m², 3 m |
| **Housekeeper/guard room** (single occupancy) | **4.5 m²**, min dim **2.1 m** |
| Enclosed kitchen | **5.4 m²**, min dim **1.8 m**; manoeuvring space 1.2 m |
| Clear heights (Table B.4) | Living/bedroom **2.7 m**; offices/retail 2.5 m; corridors, lobbies, washrooms, storage, egress, other occupiable **2.3 m**; light-vehicle parking 2.3 m; ramps 2.4 m |
| Stairway headroom | **2.03 m** above treads, **2.3 m** above landings; protruding objects ≤ 50 % ceiling with 2.03 m min |
| Glazing for habitable spaces | ≥ **10 %** of room area; **150 lux** daylight in bedrooms/living; room depth ≤ 3 × window-wall width |
| Operable window controls | 900–1200 mm above floor |
| Courtyard min | 6 m × 6 m; height ≤ 23 m; > 15 m full sprinklers |

### 5.3 Stairs, guards, doors ✓ [D1 B.6]
| Item | Value |
|---|---|
| Stair clear width | **1200 mm** (handrails may project 100 mm each side) |
| Riser / tread (general) | riser **100–180 mm**, tread ≥ **280 mm**; variation ≤ 10 mm in flight |
| Regular-use & external stairs (Table B.6) | tread ≥ **300 mm**, riser **150–165 mm**, 2–14 steps per flight |
| Landings | ≤ 3660 mm vertical between; length ≥ 1200 mm on straight run |
| Handrail | **865–965 mm** high; extra child rail 650–750 mm; Ø 32–51 mm |
| **Guard** | trigger **760 mm** drop; height **≥ 1200 mm** (1065 mm where handrail forms the guard); **100 mm sphere** rule; no climbable rails within 865 mm of base |
| Spiral stairs | clear width ≥ 660 mm, headroom 2030, riser ≤ 240, tread ≥ 190 at 305 mm |
| Corridor (internal in unit) | **1.0 m**; common residential corridor 1.5 m single / 1.8 m double-loaded; service corridor 1.2 m |
| Doors (Table B.7) | entry **915 mm** clear; bathroom/toilet **815 mm** clear; exit doors ≥ 915 mm; clear between two door openings ≥ 1.2 m |
| Level changes | 13 mm–535 mm need ramp or stair |

### 5.4 Parking & access ✓ [D1 B.7]
| Item | Value |
|---|---|
| Bay (90°) | **2.5 × 5.5 m**; driveway 6 m two-way / 5.5 m one-way; parallel 2.5 × 6 m; +300 mm if bounded by structure; 5 × 2.5 m bays allowed in small plots (< 30 m) |
| Internal road | 3 m one-way / 6 m two-way |
| Ramps | straight ≤ 12 %, lane ≥ 3 m, clear height 2.4 m; curved lane 3.5 m inner R 4 m; helical ≤ 8 % |
| Parking floor slope | ≤ 4 % (accessible 2 %); wheel stop ≤ 120 mm |
| Tandem | max 2 bays residential; dead-end driveway ≤ 8 spaces |
| Residential ratios (apartments) | studio/1-2 BR: **1**; 3-4 BR: **2**; 5 BR/duplex/penthouse: **3** per unit; **villa ratio ⚠ per Part K** |
| EV / preferred | 5 % preferred bays if > 20 bays |
| Gate level | ≥ +300 mm above road edge or 2–5 % slope |

### 5.5 Fire / egress
| Item | Value |
|---|---|
| Code | UAE FLSC (MOI) — **exit stairs/corridors 1200 mm** (vs NFPA 1120 mm) for < 2000 occupants ⚠ trade-press summary [D5] |
| Sprinklers | Required per FLSC occupancy/height thresholds (not extracted) ⚠; sprinklers permit relaxed egress as in NFPA |
| LPG | New buildings: centralised gas piping, no cylinders (Dubai statement, 2017) ⚠ |
| Exterior stairs | none above 15 m; screens ≥ 1200 mm above 11 m ✓ [D1 B.6.4.1.10] |
| Travel distance / compartmentation | **⚠ verify in UAE FLSC Ch. 3 / Dubai Civil Defence checklist** — not extracted |
| Villa fire | Villas generally smoke alarms + extinguishers; Civil Defence NOC for villas w/ pools/lifts/basements ⚠ |

### 5.6 Electrical — DEWA (Dubai)
| Item | Value |
|---|---|
| Supply | **230/400 V, 50 Hz, 3-phase 4-wire**, tolerance ±10 % ⚠ study-guide summary of DEWA 2017 regs [D7] |
| Standard | DEWA 2017 + IET 17th ed. (BS 7671:2008) + IEC ✓ [D7] |
| Process | **Prior design approval** before starting; consultant checklist covers earth leakage, overcurrent, under-voltage protection and including future loads in connected load ✓ [D7] |
| Villa meter/DB | DEWA circulars give villa water-meter drawings, villa complex conduit layout, location of main switch room ✓ [D7 circulars] |
| Typical final circuits | 1.5 mm² lighting / 2.5 mm² sockets, RCD 30 mA ⚠ (international practice, **not** DEWA-verified) |
| Max demand/diversity | **⚠ verify in DEWA 2017 Part (loads)** |
| Abu Dhabi | ADDC regs ⚠ |

### 5.7 Plumbing, HVAC, structure
| Item | Value |
|---|---|
| Water | DEWA Water Regulations ⚠ not extracted; DBC Part G Incoming utilities |
| HVAC/envelope | DBC Part E (envelope), H (indoor environment); Al Sa'fat Silver mandatory (≈ 19 % energy saving vs baseline; Gold 32 %, Platinum 35 %) ✓ [D10]; DBC folds Silver prerequisites into mandatory requirements ✓ |
| Structure | DBC Part F; wind loads per ASCE 7 via Admin Res. 37/2021 (tem. structures 32 m/s ✓ snippet); **Dubai design basic wind speed & seismic zone ⚠ verify** |
| Design temp | ⚠ verify |

---
## 6. Permit / approval drawing set

### Dubai (Dubai Municipality building permit, consultant-submitted e-service) ⚠ practice list — confirm in DM checklist
| # | Sheet | Must show |
|---|---|---|
| 1 | Affection Plan / plot data + NOCs (DEWA, Civil Defence where applicable, RTA, Dubai Roads, telecom) | Plot, setbacks, max floors, community guidelines (Emaar/Nakheel/Meraas) |
| 2 | Site plan | DLTM coordinates, setbacks per floor, gate level, parking bays 2.5×5.5, wall heights, service connections |
| 3 | Floor plans (basement, G, 1, roof, annex, majlis) | Room names EN/AR, min areas/dims, stairs 1.2 m, doors 915/815 clear, windows ≥ 10 % |
| 4 | Elevations / sections | Heights, ceiling 2.7 m, guard 1.2 m |
| 5 | Structural drawings + calculations + soil report | Foundations, columns, slabs, wind (ASCE 7) |
| 6 | MEP (E, HVAC, P&D) + DEWA approval | Load schedule; DEWA design review |
| 7 | Fire (if required) | Civil Defence approved |
| 8 | **Al Sa'fat Silver compliance** checklist | Mandatory |
| 9 | Boundary wall / gate detail | Heights per community guideline |

### Abu Dhabi (TAMM / DMT) ⚠
Architectural + structural + MEP + fire drawings, **Estidama PVRS ≥ 1 Pearl documentation**, UPC/DMT plot specification compliance, Civil Defence approval; follow DMT Sep 2025 villa amendment (1.5 m front, roof setback) [D6][D11].

---
## 7. Common rejection reasons / mistakes
1. Using DBC Table B.1 default (3 m) when Affection Plan/DCR or master-developer guidelines differ — or vice versa using Home First 1.5 m for non-eligible owners ⚠.
2. Setbacks not dimensioned per floor; rooftop floor missing extra 1.5 m (Home First).
3. Room below 10.5 m² / 3 m; kitchen < 5.4 m²; maid/guard room < 4.5 m² / 2.1 m.
4. Ceiling < 2.7 m habitable; corridors < 2.3 m; stair headroom < 2.03 m.
5. Stair width < 1200 mm; riser > 180 mm; guard < 1200 mm or gaps > 100 mm; handrail outside 865–965.
6. Doors < 915 mm entry / 815 mm bathroom clear.
7. Gate level < +300 mm above road or wrong slope; bays smaller than 2.5×5.5; reverse-out only.
8. Missing Al Sa'fat Silver or Estidama 1 Pearl documentation (permit blocked).
9. Coordinates not in DLTM / wrong datum; plot polygon altered.
10. No DEWA approval before MEP; spare capacity/future loads omitted.
11. Neighbour consent missing where shared-boundary setback removed; windows overlooking neighbour.
12. Free-zone plot submitted to municipality rather than zone authority (or vice versa).

---
## 8. Sources
- [D1] Dubai Building Code 2021 (u.ae PDF; read via SlideShare text copy — A.11, A.12, B.4–B.8): https://u.ae/-/media/Documents-2023/Dubai-Building-Code_English_2021-Edition_compressed-(1).pdf ; https://www.slideshare.net/slideshow/dubai-building-codeenglish2021-editionakpdf/264939916
- [D2] Decree No. 45 of 2021: https://dlp.dubai.gov.ae/Legislation%20Reference/2021/Decree%20No.%20(45)%20of%202021%20Concerning%20the%20Dubai%20Building%20Code.html
- [D3] Trakhees circular CEDGR-135: https://pcfc.ae/en/Rules%20and%20Regulations/Trakhees/Civil%20Engineering%20Department/Permits%20(Facilities)/Circulars/CEDGR-135%20Dubai%20Building%20Code%20Circular%202021.pdf ; ICC note: https://www.iccsafe.org/building-safety-journal/bsj-technical/dubai-executive-council-issues-dubais-new-building-code ; DM page: https://www.dm.gov.ae/municipality-business/planning-and-construction/dubai-building-code-2/
- [D4] Fire code update (Khaleej Times): https://khaleejtimes.com/article/fire-safety-code-for-the-uae-updated
- [D5] ME Construction News (1200 mm stairs): https://meconstructionnews.com/?p=2050
- [D6] Abu Dhabi Media Office, DMT villa amendments (9 Sep 2025): https://www.mediaoffice.abudhabi/en/infrastructure/strengthening-family-and-community-bonds-department-of-municipalities-and-transport-introduces-amendments-to-private-villa-building-regulations/ ; https://www.dmt.gov.ae/en/Media-Centre/News/Department-of-Municipalities-and-Transport-Announces-Amendments-to-Private-Villas-Regulations
- [D7] DEWA Regulations for Electrical Installations 2017: https://dewa.gov.ae/-/media/DEWA_Regulations_for_Electrical_Installations_2017_Edition.ashx ; circulars: https://dewa.gov.ae/en/builder/useful-tools/dewa-circulars
- [D8] DLTM EPSG:3997 / DM Survey: https://epsg.io/3997 ; https://www.dm.gov.ae/survey-department/geodesy/
- [D9] ADM CAD/BIM guidance: https://globalbim.org/info-collection/abu-dhabi-municipality-adm-guidelines/ ; Nahrwan UTM 40N https://epsg.io/27040
- [D10] Al Sa'fat: https://www.dm.gov.ae/municipality-business/al-safat-dubai-green-building-system/ ; https://mediaoffice.ae/en/news/2023/December/07-12/Green-Buildings-in-Dubai ; Admin Res 154/2020 https://dlp.dubai.gov.ae/Legislation%20Reference/2020/Administrative%20Resolution%20No.%20(154)%20of%202020%20Concerning%20the%20Bylaw%20on%20the%20Dubai%20Green.html
- [D11] Estidama/PVRS: https://pages.dmt.gov.ae/en/Urban-Planning/The-Pearl-Rating-System-for-Estidama
- [D12] Admin Resolution 37/2021 (wind): https://dlp.dubai.gov.ae/Legislation%20Reference/2021/Administrative%20Resolution%20No.%20(37)%20of%202021%20Amending%20the%20Bylaw%20Concerning.html
- [D13] DM permit FAQ: https://www.dm.gov.ae/wp-content/uploads/2023/09/FAQ-for-Buildings-Permit-Procedures-and-Regulations-eng-1.pdf (page fetch returned homepage; statement from search summary ⚠)
- [D14] Home First (Mar 2025): https://www.khaleejtimes.com/uae/dubai-building-code-update ; https://gulfnews.com/uae/dubai-eases-villa-construction-rules-for-emiratis-allows-second-family-homes-1.500713942 ; https://www.thenationalnews.com/news/uae/2025/03/17/dubai-emirati-housing-plan/

### Open items summary
⚠ DBC Part K (villa setbacks/coverage/parking); UAE FLSC edition & travel-distance tables; DEWA max demand, final-circuit rules, voltage tolerance; ADIBC 2013 numbers; ADM CAD spec & coordinate system; Dubai wind speed/seismic; DM CAD/layer requirements; Home First eligibility; boundary-wall height; Abu Dhabi coverage/height; Trakhees/free-zone regs.
