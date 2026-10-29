# United Kingdom — Drafting & Code Reference

Legend: **✓** = checked against a gov.uk/standards-body page or search summary of one this session (URL in §8). **⚠ verify** = drafter knowledge or weak secondary source; confirm against the current Approved Document / standard before issuing. The UK has FOUR separate building-regulation regimes. Default below = **England**. Always ask: England, Wales, Scotland or Northern Ireland?

---
## 1. Units, scales, sheets

### 1.1 Units & dimension format
| Item | UK practice |
|---|---|
| Unit system | Metric (SI). Dimensions in **millimetres, no unit symbol**, whole numbers (e.g., `3800`, `2400`). Levels/site in **metres to 3 decimals** (`12.345`) |
| Dimension format | `3800` (not `3.8 m`, not `3800 mm`). Drawing note states "All dimensions in mm unless stated otherwise" (BS 8888 practice ⚠) |
| Levels | `FFL +100.250` / `FFL 100.250 AOD` (above Ordnance Datum Newlyn); `SSL`, `FFL`, `TOS` (top of steel), `T/O slab`; Ordnance Datum in site plans |
| Gradients | 1:20, 1:60 (ratio) or % ; drainage falls `1:40`, `1:80` |
| Language | British English ("storey", "lift", "WC", "metre", "colour", "tonne") |
| Date format | dd/mm/yyyy or ISO 8601 yyyy-mm-dd |
| Stairs | `rise 170 x going 250`; pitch in degrees |
| Imperial remnants | Door sizes still `1981 x 762/838 mm` (6'6" x 2'6"/2'9"); brick `65 mm` course 75 mm with mortar ⚠ |

### 1.2 Typical scales (BS 8888 / BS EN ISO 5455 preferred scales: 1:1, 1:2, 1:5, 1:10, 1:20, 1:50, 1:100, 1:200, 1:500, 1:1000, 1:2000/1250/2500) ⚠
| Drawing type | Scale | Notes |
|---|---|---|
| Location plan (planning) | **1:1250** or **1:2500** | Site outlined in RED; adjoining land owned in BLUE; ≥ 2 roads named; OS-based, north point, scale bar ✓ (UK national validation requirements) |
| Block / site plan (planning) | **1:500** or **1:200** | Existing & proposed buildings, boundaries, access, parking, trees, levels ✓ |
| Floor plans, elevations, sections (planning) | **1:50** or **1:100** | Householder: 1:50/1:100 ✓ |
| Building control plans/sections | 1:50 / 1:20 for construction sections | |
| Construction details | 1:5, 1:10, 1:20 | Junctions at 1:5 / 1:10 |
| Wall sections | 1:20 | |
| Large-scale joinery/fixtures | 1:2, 1:1 | |
| Structural GA | 1:50 / 1:100 | |
| Services layouts | 1:50 / 1:100 | Plant rooms 1:20 |
| Drainage | 1:100 / 1:200 (site 1:500) | |
Graphic scale bar mandatory when sheet may be reduced (A3 print of A1) ✓.

### 1.3 Sheet sizes (BS EN ISO 5457 — A series)
| Size | mm |
|---|---|
| A0 | 841 x 1189 |
| A1 | 594 x 841 |
| A2 | 420 x 594 |
| A3 | 297 x 420 |
| A4 | 210 x 297 |
✓ ISO 216 values. Planning/BC submissions typically A1/A2/A3 for housing; A0/A1 commercial. Frame margins 20 mm left (binding), 10 mm others for A0–A2; 5–10 mm for A3/A4 ⚠. Orientation marks, trim marks; title block bottom-right (BS EN ISO 7200).

### 1.4 Title block fields (BS EN ISO 7200 / BS 1192 / 19650 practice) ⚠
Project name & address; Client; Originator (practice name/logo/address/RIBA reg no.); **Drawing title**; **Drawing number** (ISO 19650 container ID, see §2); **Revision** (P01, P02… preliminary; C01, C02… contractual) ✓ (BS 1192 revision convention); **Status/suitability code** (S0–S7, A, B, CR); **Scale @ sheet size**; **Date**; Drawn/Checked/Approved; Stage (RIBA stage); Notes/copyright. Status/suitability (UK National Annex to ISO 19650-2): S0 initial/WIP, S1 suitable for coordination, S2 for information, S3 for review & comment, S4 for stage approval, S5 ⚠, S6 for PIM authorisation, S7 for AIM authorisation; published A1… authorised & accepted, B1… partially signed off, CR as-constructed record ⚠ verify code list.

### 1.5 North arrow / grid
- North point on all site/location/floor plans; plans oriented N up where possible.
- Structural grid: **letters** A, B, C… in one direction, **numbers** 1, 2, 3 in the other, bubbles (circles) at both ends on structural drawings ⚠; letters I and O generally omitted ⚠.

---
## 2. CAD layer & file naming standard

**Standards chain:** BS EN ISO 19650-1/-2 (information management using BIM, 2018→UK NA) → **UK National Annex** (naming) ✓; BS 1192:2007+A2:2016 (collaborative production; withdrawn/superseded but its codes persist); **BS EN ISO 13567** (organisation of layers) / **AEC (UK) CAD Standard** layer naming ⚠; Classification **Uniclass 2015** (NBS) ✓; BS 8888 (technical product documentation) and BS EN ISO 128 / ISO 7519 (construction drawings: general principles of presentation) ✓.

### 2.1 Container ID (file/drawing number) — hyphen separated
**BS 1192 form:** `Project-Originator-Volume/System-Level/Location-Type-Role-Number`
Example: `PRJ01-ABC-ZZ-01-DR-A-1001` (project PRJ01, originator ABC, zone ZZ = all, level 01, DR = drawing, A = architect, number 1001).
**UK National Annex to BS EN ISO 19650-2 form** (fewer fields, uses breakdowns): `Project-Originator-Functional breakdown-Spatial breakdown-Form-Discipline-Number` ✓ (field names per CDBB National Annex / pbctoday; full code lists — ⚠ check the Annex).
Example: `PRJ01-ABC-ZZ-01-DR-A-1001`.
| Field | Typical codes |
|---|---|
| Project | ≤ 6 alphanumerics |
| Originator | 3–6 letters (company code) |
| Volume/Functional breakdown | `ZZ` = all/multiple; `V1`,`V2` zones/buildings |
| Level/Spatial breakdown | `00` ground, `01`, `02`; `B1` basement; `RF` roof; `ZZ` multiple; `XX` not applicable |
| Type/Form | `DR` 2D drawing; `M2` 2D model; `M3` 3D model; `SH` schedule; `SP` specification; `RP` report; `CA` calculation; `CO` correspondence; `DB` database; `FN` file note; `MS` method statement; `HS` H&S; `PP` presentation; `VS` visualisation ⚠ |
| Role/Discipline | `A` architect; `B` building surveyor; `C` civil; `D` drainage/highways; `E` electrical; `F` facilities mgmt; `G` geographic/land; `H` heating & ventilating; `K` client; `L` landscape; `M` mechanical; `P` public health; `Q` quantity surveyor; `S` structural; `T` town planner; `W` contractor; `X` subcontractor; `Y` specialist designer; `Z` general (non-disciplinary) ⚠ verify list |
| Number | 4 digits |
- **Suitability/status & revision** are metadata in the CDE (WIP / Shared / Published / Archive states) and in the title block, not part of ID in the Annex ✓ (BSI: status, revision, classification are CDE metadata).
- Classification (Uniclass 2015 table codes): `Co` Complexes, `En` Entities, `Ac` Activities, `SL` Spaces/Locations, `EF` Elements/Functions, `Ss` Systems, `Pr` Products, `TE` Tools & equipment, `FI` Form of information, `PM` Project management, `Zz` CAD ✓. Code syntax `Ss_25_10_30` (table_group_subgroup_section) ✓; `EF_25_10` walls ⚠ exact title.

### 2.2 Layer name syntax
- **AEC (UK) CAD Standard (Basic Layer Naming)** / BS 1192 Part 5 style: `Role-Classification(Uniclass)-Description`, hyphen/underscore, e.g., `A-WALL-EXT` style. Exact AEC(UK) field syntax ⚠ **verify** against the AEC (UK) CAD Standard v3 before claiming compliance — web search for the field spec failed (rate limit).
- **Practical default for UK drawings** (works with NBS/AEC UK users): `RoleLetter-ElementPrefix-Description`, upper case, hyphens, ≤ 31 chars, no spaces, units mm.
- **ISO 13567 form:** Agent responsible (e.g., `A`) + element (6 chars) + presentation (`-` or P, etc.) ⚠ verify field widths.

### 2.3 Example layers (colours = conventional ACI, not mandated; lineweights = ISO 128 set: 0.13, 0.18, 0.25, 0.35, 0.5, 0.7, 1.0, 1.4, 2.0 mm ✓)
| Layer (practical default) | Content | ACI colour | Lineweight (mm) |
|---|---|---|---|
| A-WALL-EXT | External wall (cut) | 7 | 0.50 |
| A-WALL-INT | Internal wall (cut) | 7 | 0.35 |
| A-WALL-PART | Partitions | 8 | 0.25 |
| A-DOOR | Doors + swings | 2 | 0.25 |
| A-GLAZ | Windows/glazing | 4 | 0.25 |
| A-COLS | Columns (arch) | 7 | 0.50 |
| A-FLOR-STRS | Stairs | 3 | 0.25 |
| A-FLOR-LEVL | Floor levels FFL | 7 | 0.18 |
| A-CLNG | Ceiling grid | 5 | 0.13 |
| A-ROOF | Roof | 7 | 0.35 |
| A-FURN | Furniture/fittings | 8 | 0.13 |
| A-ANNO-DIMS | Dimensions | 1 | 0.18 |
| A-ANNO-TEXT | Text/notes | 7 | 0.18 |
| A-ANNO-SYMB | Section/elev. markers | 7 | 0.25 |
| A-ANNO-TTLB | Title block | 7 | 0.35–0.70 |
| A-ANNO-NPLT | Non-plot | 9 | no plot |
| A-GRID | Setting-out grid | 1 | 0.13 |
| A-SECT-CUT | Section cut | 7 | 0.70 |
| S-COLS | Columns | 1 | 0.50 |
| S-BEAM | Beams | 4 | 0.35 |
| S-FNDN | Foundations | 6 | 0.50 |
| S-SLAB | Slab edge | 3 | 0.35 |
| S-GRID | Structural grid | 1 | 0.13 |
| M-HVAC-DUCT | Ductwork | 5 | 0.35 |
| M-PIPE-HTG | Heating pipework | 1 | 0.35 |
| M-PIPE-CHW | Chilled water | 4 | 0.35 |
| E-LITE | Lighting | 2 | 0.25 |
| E-POWR | Power/sockets | 3 | 0.25 |
| E-FIRE-ALRM | Fire alarm devices | 1 | 0.25 |
| E-COMM | Data/comms | 5 | 0.25 |
| P-DOMW | Domestic water | 5 | 0.35 |
| P-SANR | Soil & waste | 3 | 0.35 |
| P-DRAN | Below-ground drainage | 2 | 0.35 |
| F-SPRN | Sprinklers ⚠ | 1 | 0.25 |
(Layer strings are practical, based on the shared AIA/ISO pattern; ⚠ verify to AEC(UK) before contract use.)

### 2.4 Drawing numbering / suffix conventions
- 4-digit number: first digit(s) denote type group, e.g. `0001–0099` location/site; `1000–1999` plans; `2000s` elevations; `3000s` sections; `4000s` details; `5000s` schedules ⚠ (practice varies; define in BIM Execution Plan).
- Revision: `P01…` while stage design (preliminary), `C01…` once contractual (BS 1192) ✓.
- Models and drawings share one container ID; PDFs inherit it plus revision suffix.
- Information Delivery Plan / BEP (BIM Execution Plan) must record naming convention (ISO 19650-2 clause 5.x ⚠).

---
## 3. Drafting conventions

### 3.1 Text, dimension, line (BS EN ISO 3098 / ISO 128 / BS 8888)
| Item | Value |
|---|---|
| Lettering heights (ISO 3098) | 2.5, 3.5, 5, 7, 10 mm ✓ (series √2) |
| Notes/dimension text | 2.5 mm (minimum) – 3.5 mm plotted ✓ |
| Titles | 5 mm; sheet title 7 mm |
| Line widths (ISO 128-20) | 0.13, 0.18, 0.25, 0.35, 0.50, 0.70, 1.0, 1.4, 2.0 mm ✓; ratio √2; typical 3-weight (0.25 / 0.50 / 0.70) |
| Dimension line | thin continuous; **oblique stroke (tick) 45°** at ends or closed arrowhead; text above the line, read from bottom/right ✓ (ISO 129-1) |
| Extension line | gap ~1 mm, overshoot 2 mm ⚠ |
| Dimension strings | Overall; opening positions; room-internal on request ⚠ |
| Leaders | thin, arrow/dot, text at horizontal landing |

### 3.2 Symbols & tags (ISO 7519 / BS 8888 ⚠ details)
| Item | Convention |
|---|---|
| Door tag | `D01`, `D1.02` etc., numbered circle/diamond; schedule keyed; fire-rated doors `FD30`, `FD60`, `FD30S` (smoke seals) ✓ |
| Window tag | `W01` / `W1.02` ; glazing type schedule |
| Room tag | Room name + number ; area (m²) on planning plans |
| Grid bubble | circle, letters/numbers |
| Section marker | thick line at ends, arrow showing look direction, letter `A–A`, `B–B`; sheet ref beside |
| Elevation marker | arrow with north/east or number ; or named elevations (Front, Rear, Side) |
| Detail callout | circle with detail no./sheet |
| Level marker | `FFL +00.000` triangle |
| Revision cloud | cloud + triangle with `P01`, `C02` |
| North point | arrow with N |
| Fire compartment line | hatched thick line + `60` , `FD60` ✓ |
| Fire escape routes | green arrows (green circles) on fire strategy drawings ⚠ BS 9999 / BS ISO 3864 |
| Abbreviations | `FFL` finished floor level, `SSL` structural slab level, `DPC` damp-proof course, `DPM`, `RWP` rainwater pipe, `SVP` soil & vent pipe, `UBO`, `EWI`, `TBC`, `NTS`, `FD30`, `WC`, `OG` |

### 3.3 Hatching (BS EN ISO 128-50 + UK construction practice ⚠ verify per BS 8888/BS 1192 Annex)
| Material | Convention |
|---|---|
| Brickwork (section) | 45° lines, close spacing, or cross-hatched |
| Blockwork | Diagonal lines wide spacing, "block" outline ; or small crosses |
| Concrete (in situ) | Dot + small triangle stipple (random aggregate) |
| Concrete (precast) | Same dots with a line border ⚠ |
| Timber (sawn/structural) | Diagonal cross within rectangle (X) |
| Timber (planed/finish) | Parallel grain lines |
| Hardcore | Solid dark / irregular stones |
| Earth | Short 45° stroke lines / earth hatch |
| Insulation (rigid) | Diagonal lines within outline or crossed rectangle |
| Insulation (quilt) | Wavy/zigzag loops |
| Steel | Solid fill or thin 45° lines at small scale |
| Plasterboard | Thin double line / dotted band |
| Glass | Single thin line (or three) with diagonals |
| Membranes (DPC/DPM) | Thick line (DPC) ; line with ticks (DPM) |

### 3.4 Linetypes (ISO 128-20; ISO types) ✓
| Type | ISO ref | Use |
|---|---|---|
| Continuous thick | 01.2 | Outlines, cut |
| Continuous thin | 01.1 | Dimensions, hatch, leaders |
| Dashed | 02 | Hidden edges/outlines ; above-cut elements |
| Long dash short dash | 04 | Centre lines, axes |
| Long dash double short dash | 05 | Hidden structure / alternative position |
| Dash-dot thick ends | 04.2 | Section planes |
| Thin freehand/zigzag | 01 + sym | Break lines |
| Dot/phantom | 05 | Boundaries (red line on site plan) |
Red line boundary (planning) = continuous red; blue line = adjoining land owned/controlled ✓.

---
## 4. Governing codes & authorities

### 4.1 England — Building Regulations 2010 (SI 2010/2214) + Approved Documents (AD)
Dates as listed on the gov.uk collection page (https://www.gov.uk/government/collections/approved-documents) ✓ — the page shows one date per document without saying "edition" vs "effective"; ⚠ treat as latest published; check each AD page.
| Part | AD title | Latest date shown ✓/⚠ | Notes |
|---|---|---|---|
| A | Structure | 2004 ed. incl. 2013 amend. (date 1 Sep 2013) | Loading ref BS EN 1991; Part A also: DfE guidance |
| B | Fire safety (Vol 1 dwellings, Vol 2 other) | 2019 ed. with amendments; latest 16 Sep 2026 (second stairs, evacuation lifts in tall residential) ✓ page; transition to 2029 ⚠ | Second stair >18 m residential; sprinklers ≥11 m; care homes ✓ (sprinklers) |
| C | Site prep, contaminants & moisture | 2004 + 2013 amend. | |
| D | Toxic substances | 2013 (listed 2 Dec 2010) ⚠ | |
| E | Resistance to sound | 2003 + amendments to 2015 (4 Mar 2015) | |
| F | Ventilation | 2021 ed. (15 Jun 2022) | Vol 1 dwellings, Vol 2 non-dwellings |
| G | Sanitation, hot water safety, water efficiency | 2015 ed. + 2016 amend.; page lists 1 Oct 2024 ⚠ | 125 L/p/day (110 optional) ⚠ |
| H | Drainage & waste disposal | 2015 ed. ; page lists 2010 ⚠ verify | |
| J | Combustion appliances & fuel storage | 2010 + 2022 amend. (30 Sep 2022) | |
| K | Protection from falling, collision, impact | 2013 (3 Jan 2013) ✓ | Stairs/guarding/glazing |
| L | Conservation of fuel & power (L1 dwellings, L2 other) | 2021 ed. + amendments (page lists 2 Feb 2023) ✓ | Future Homes/Buildings Standard pending ⚠ |
| M | Access to & use of buildings | Vol 1 dwellings, Vol 2 other; 2015 ed. with 2024 amendments (1 Oct 2024) ✓ | M4(1) visitable, M4(2) accessible & adaptable, M4(3) wheelchair user ✓ |
| O | Overheating | 2021 (15 Jun 2022) ✓ | |
| P | Electrical safety — dwellings | 2006 + amendments; page lists 1 Jan 2013 | Competent person scheme |
| Q | Security — dwellings | 22 Nov 2024 ✓ | |
| R | Infrastructure for electronic communications | 2022 (4 Oct 2022) | |
| S | Infrastructure for EV charging | 2021; page lists 17 Apr 2023 | |
| T | Toilet accommodation | 3 Nov 2025 ✓ | |
| 7 | Materials & workmanship (Reg 7) | 29 Nov 2018 ✓ | |
(No ADs I or N now; N merged into K.) ✓

### 4.2 Authorities by discipline
| Discipline | Code / standard | Edition (Oct 2026) | Who enforces |
|---|---|---|---|
| Planning permission | Town & Country Planning Act 1990; GPDO 2015 (permitted development) ; NPPF ; local plan | current | Local planning authority (LPA) ; Secretary of State on appeal |
| Building control | Building Act 1984; Building Regs 2010 | current ADs | Local authority building control or Registered Building Control Approver (RBCA; approved inspectors abolished Apr 2024) ⚠ |
| Higher-risk buildings (≥18 m or 7 storeys, 2+ residential units/care/hospital) | Building Safety Act 2022 | in force | **Building Safety Regulator** (HSE), Gateways 1 (planning), 2 (pre-construction), 3 (completion) ⚠ |
| Electrical | **BS 7671:2018+A2:2022** (18th ed.); **A3:2024 published 31 Jul 2024** ✓; A4 reported published Apr 2026 with transition ending Oct 2026 ⚠ low-confidence | verify current | Competent person scheme (NICEIC, NAPIT, etc.) / building control; Part P in England |
| Structure | **Eurocodes BS EN 1990–1999 + UK National Annexes**; PD 6693 | 1st gen; 2nd gen BS EN coming ⚠ | BC / approved inspector; Building Safety Regulator for HRB |
| Fire | AD B ; BS 9999:2017 (non-domestic), BS 9991:2015 (dwellings) ⚠ ; Fire Safety (England) Regs 2022 ; Regulatory Reform (Fire Safety) Order 2005 | | Fire & rescue authority (consultee); BC |
| Accessibility | AD M ; BS 8300-1/2:2018 ⚠ ; Equality Act 2010 | | BC; Equality Act via courts |
| Energy | AD L ; SAP 10.2 (dwellings), SBEM (non-domestic) ; EPC | | BC |
| Drainage / water | AD H ; BS EN 12056, 752 ; Water Supply (Water Fittings) Regs 1999 ; WRAS | | Water company / BC |
| Heating/ventilation design | **CIBSE** Guide A, B, C, F, G; TM59, TM52, TM54 ; BSRIA ; BS EN 12831, 16798 ⚠ | | design reference |
| Lighting | SLL Code for Lighting ; BS EN 12464-1 | | |
| CDM | Construction (Design & Management) Regs 2015 | | HSE |
| Heritage | Listed buildings/conservation areas ; Planning (LBCA) Act 1990 | | LPA / Historic England |

### 4.3 Wales, Scotland, Northern Ireland
- **Wales:** Building Regulations 2010 (same SI, Wales-specific ADs; Part L 2022, Part F 2021 differ; Welsh ADs separate from England) ⚠ verify. Welsh Government; local authority building control. Sprinklers required in new residential since 2016 ✓ (Building (Amendment) Regs, Wales) ⚠.
- **Scotland:** **Building (Scotland) Act 2003 + Building (Scotland) Regulations 2004**; Mandatory standards via **Technical Handbooks (Domestic / Non-domestic)** — Sections 0 General, 1 Structure, 2 Fire, 3 Environment, 4 Safety, 5 Noise, 6 Energy, 7 Sustainability ✓; requires **building warrant** (not "building regs approval") and completion certificate; verifier = local authority; planning separate under Town & Country Planning (Scotland) Act 1997; metric; Scottish version of Part M = Section 4 ; stair rise 170 max (domestic 180?) ⚠ verify. Scottish Building Standards Division.
- **Northern Ireland:** Building Regulations (NI) 2012; Technical Booklets A–V ; Part P equiv; District Councils; planning via local councils since 2015 ⚠.
- NI/Scot/Wales: confirm separate parts for energy (L/F/J/E) and AD letters differ.

---
## 5. Key numbers

### 5.1 Stairs (AD K 2013, private stairs; Table 1.1 values) — search-confirmed ✓ (secondary)
| Item | Value | Notes |
|---|---|---|
| Rise (private stair) | 150–**220** mm | ✓ ADK table via designingbuildings / sitemate (secondary) |
| Going (private stair) | **220**–300 mm | ✓ |
| Max pitch (private stair) | **42°** | ✓ |
| Twice rise + going | 550–700 mm | ✓ |
| Institutional/assembly stair | rise ≤ 180, going ≥ 280 | ⚠ |
| Other (utility) | rise ≤ 190, going ≥ 250 | ⚠ |
| Headroom | **2.0 m** over pitch line (loft stair 1.9 m centre / 1.8 m edge ⚠) | ✓ (2.0) |
| Stair width | min 900 mm for M4(2) ⚠ ; AD B escape stairs per fire strategy | |
| Handrail height | 900–1000 mm above pitch line / landing | ⚠ |
| Guarding (dwelling) | **900 mm** stairs, ramps, landings, internal floor edges; **1100 mm** external balconies, roof edges ✓ (one secondary source; another says 1100 on landings — ⚠ verify) | |
| Guarding required when | drop ≥ **600 mm** | ✓ |
| Guarding gap | **100 mm** sphere must not pass | ✓ |
| Tapered treads | min going 50 mm at narrow end ; 220 mm at 270 mm from narrow side ⚠ | |
| Single-flight rise to landing | landings ≥ stair width ; ≤ 36 risers ⚠ | |
| Ladders (loft) | only for single room in loft ⚠ | |

### 5.2 Egress & fire (AD B 2019, Vol 2) ⚠
| Item | Value |
|---|---|
| Max travel distance — offices, shops, assembly: one direction / more than one direction | 18 m / 45 m ⚠ ; industrial 25 m / 45 m ⚠ (Table 2.1) |
| Min exit width | 1050 mm door/ 1000 mm escape route; 850 mm clear for up to 100 persons (Table 4.1: ≤ 50: 800 mm, ≤ 110: 850 mm, ≤ 220: 1050 mm) ⚠ |
| Escape stair width | ≥ 1000 mm for 2 stairs (≤ 220 persons: 1000 mm Table 3.? ) ⚠ |
| Dwelling: bedrooms above 4.5 m | Protected stair / protected landing ⚠ |
| Dwelling: escape window | clear opening ≥ 450 mm x 750 mm (0.33 m² ; bottom ≤ 1100 mm AFFL) ✓ (AD B vol 1 §2.? ⚠) |
| Compartment walls | typically 60 min (30 in small); up to 120 min ⚠ ; AD B Table B3 |
| Doors | FD30 / FD60 ; smoke seals S |
| Sprinklers | new residential ≥ 11 m height ✓ (page notes care homes sprinklers) ⚠ ; Scotland: all new flats ; Wales: all residential ✓ ⚠ |
| Second stair | residential ≥ 18 m (England) ⚠ ; evacuation lift ≥ 18 m ⚠ ; transition ends 2029 ⚠ |
| Fire separation — boundary | 1 m from boundary for unprotected area (Table B? ) ⚠ |

### 5.3 Doors, corridors, accessibility (AD M)
| Item | Value | Status |
|---|---|---|
| M4(1) visitable dwelling | Level approach ; entrance clear opening 775–800 ; ground-floor WC | ⚠ |
| M4(2) accessible & adaptable | Door clear opening ≥ 800–850 mm ; hallways 1050 mm min, 1200 if not head-on ✓ (Camden, secondary) | ⚠ verify |
| M4(3) wheelchair user | **850 mm** every door clear opening, 300 mm nib leading edge / 200 mm following ; 1500 mm turning circle in entrance & Cat 3 bathrooms ; living 1400x1700 ellipse or 1500 circle ✓ (gov FAQ & Camden) | ✓ secondary |
| Switch/socket height | **450–1200 mm** above FFL (AD M Vol 1) | ⚠ |
| Ramps (Vol 2) | 1:20 max normal, 1:15 ≤ 5 m, 1:12 ≤ 2 m going ; landings 1500 mm long ; width ≥ 1500 mm for external; handrails both sides, 900–1000 mm | ⚠ |
| Door clear opening (non-domestic) | 800 mm min on accessible routes ; 1000 mm external main entrance (≥ 1000 effective clear opening) | ⚠ |
| Corridor width | 1200 mm min ; passing places at 1800 (1500) ⚠ | |
| Lifts | min 1100 x 1400 mm car ; 1500 x 2000 for wheelchair stretcher ⚠ BS EN 81-70 |
| Accessible WC (non-dom.) | 2200 x 1500 mm compartment ⚠ ; now AD T 2025 changes (Changing Places, mixed-sex) ⚠ |
| Parking: accessible bay | 2.4 m x 4.8 m + 1.2 m safety zone each side/rear (or 3.6 m wide) ⚠ (Inclusive Mobility / BS 8300) |
| Ceiling height | **No minimum in Building Regs**; planning NDSS 2.3 m for ≥ 75 % GIA ✓ (policy) ; AD F/O fresh-air |

### 5.4 Space standards (Nationally Described Space Standard, DLUHC 2015; used where adopted by local plan; London Plan) ⚠ verify all
| Unit | GIA m² |
|---|---|
| 1b1p | 39 (37 w/ shower) |
| 1b2p | 50 |
| 2b3p | 61 |
| 2b4p | 70 |
| 3b4p | 74 |
| 3b5p | 86 |
| 4b6p | 99 |
Double bedroom ≥ 11.5 m², ≥ 2.75 m wide; single ≥ 7.5 m² ≥ 2.15 m; built-in storage ≥ 2.0 m² (1b2p); floor-to-ceiling 2.3 m ≥ 75 % ✓.

### 5.5 Parking
| Item | Value |
|---|---|
| Standard bay | 2.4 x 4.8 m (2.5 x 5.0 in some LPAs) ⚠ |
| Aisle | 6.0 m for 90° ⚠ |
| EV charging | AD S: new homes with parking → 1 charge point per dwelling ✓ topic ; 7 kW typical ⚠ |
| Cycle storage | LPA standards (London Plan: 1.5 per 1b2p ) ⚠ |

### 5.6 Ventilation (AD F 2021, Vol 1) ⚠
| Item | Value |
|---|---|
| Continuous extract (min high rate) | Kitchen 13 l/s ; bathroom 8 l/s ; utility 8 l/s ; WC 6 l/s ✓ (secondary) |
| Intermittent extract | Kitchen 30 l/s adjacent hob / 60 l/s otherwise ; utility 30 ; bathroom 15 ; WC 6 ✓ (secondary) |
| Whole-dwelling rate | ≥ 0.3 l/s per m² internal floor area ; per bedrooms 1b: 13, 2b: 17, 3b: 21, 4b: 25, 5b: 29 l/s ⚠ |
| Purge | openable area ≥ 1/20 floor area ⚠ |
| Background vents | 5000 mm² equivalent area in habitable rooms (trickle vents) ⚠ |
| Heating design temps | Living 21 °C, bedroom 18 °C, bathroom 22 °C, hall 18 °C ; outside −3 °C (CIBSE Guide A) ⚠ |
| Overheating (AD O) | glazing limits / TM59 ⚠ |

### 5.7 Electrical (BS 7671 18th ed.)
| Item | Value | Status |
|---|---|---|
| Socket-outlet | BS 1363 13 A (3-pin square) ; RCD 30 mA for sockets ≤ 32 A (411.3.3) | ⚠ |
| Ring final circuit | 32 A, 2.5 mm² T&E ; radial 20 A, 2.5 mm² ; lighting 6 A, 1.0/1.5 mm² ; cooker 32 A, 6 mm² ; shower 45 A, 10 mm² | ⚠ |
| Consumer unit | non-combustible (metal) enclosure (421.1.201) | ⚠ |
| AFDD | A2:2022 introduced AFDD requirement for some higher-risk residential ✓ | ✓ search |
| Bathrooms | Zones 0, 1, 2 ; IPX ratings ; supplementary bonding | ⚠ Section 701 |
| Part M heights | 450–1200 mm for switches/sockets ✓ ⚠ | |
| Working clearance | no fixed number in BS 7671 ; follow manufacturer / EAWR 1989 ⚠ | |

### 5.8 Plumbing & drainage ⚠
| Item | Value |
|---|---|
| Drain gradient 100 mm | min 1:80 (1:40 for ≤ 1 WC sections) ⚠ |
| Soil stack | 100 mm min ; vent to above eaves ⚠ |
| Hot water | stored ≥ 60 °C, outlet ≤ 48 °C at bath (TMV) AD G ✓ ⚠ |
| Fixtures | BS 6465-1 tables ⚠ (per occupancy) |
| Water efficiency | AD G 125 L/p/d (110 optional) ⚠ |

### 5.9 Structural actions (BS EN 1991-1-1 + UK NA Table NA.2) ⚠
| Category | qk (kN/m²) | Qk (kN) |
|---|---|---|
| A domestic floors | 1.5 | 2.0 |
| A stairs | 2.0 | 2.0 |
| A balconies | 2.5 | 2.0 |
| B offices | 2.5 | 2.7 |
| C1–C3 assembly | 3.0 | 4.0 |
| C5 crowds | 5.0 | 3.6 |
| D shops | 4.0 | 3.6 |
| E storage | 2.4 per m height | 7.0 |
| H roof (not accessible) | 0.6 | 0.9 |
Partial factors γG 1.35, γQ 1.5 (STR) ✓ standard EN 1990. Snow/wind: BS EN 1991-1-3/-4 + NA maps. Materials: BS EN 1992 (concrete), 1993 (steel), 1995 (timber), 1996 (masonry), 1997 (geotech), 1998 (seismic, usually not governing). Each with UK NA ✓.

---
## 6. Permit / approval drawing set

### 6.1 Planning application (householder, England) — national validation list ✓ / ⚠
1. Application form (via Planning Portal).
2. **Location plan** 1:1250 or 1:2500 — red line, blue line, north point, scale bar, 2 named roads.
3. **Block/site plan** 1:500 or 1:200 — site boundary, existing/proposed footprints, access, parking, trees, levels.
4. **Existing & proposed floor plans** 1:50/1:100 (every floor, roof plan).
5. **Existing & proposed elevations** (all sides) 1:50/1:100 with materials annotated.
6. **Sections** (site/building) with levels.
7. Certificates (A–D ownership), fee, Design & Access Statement (major/CA/listed), Heritage Statement, Flood Risk Assessment, Biodiversity Net Gain (BNG) statement (major since Feb 2024; small sites since Apr 2024) ⚠, tree survey, transport, noise per local list.
8. Local validation list (each LPA adds) ⚠.

### 6.2 Building control (Full Plans or Building Notice)
- Full plans: floor plans 1:50 showing structure, openings, fire doors, stair details (rise/going/headroom/guard), sections 1:20 (foundations, wall, floor, roof), roof/ceiling plans, drainage layout 1:100 (falls, manholes, inspection chambers, SVP), structural calculations & engineer's drawings, specification, fire strategy, SAP/SBEM & overheating calcs, ventilation (AD F) design, electrical competent-person certificate (Part P), soundproofing details (Part E pre-completion testing), accessibility schedule (M4(1)/(2)/(3)).
- Building Safety Regulator (HRB): Gateway 2 submission includes fire & emergency file, construction control plan, change control plan.
- Inspection stages: commencement, foundations, DPC, drains, oversite, roof, completion.

### 6.3 RIBA Plan of Work 2020 stages ✓
0 Strategic Definition · 1 Preparation & Briefing · 2 Concept Design · 3 Spatial Coordination · 4 Technical Design · 5 Manufacturing & Construction · 6 Handover · 7 Use. Planning submission typically end of Stage 3; Building regs full plans in Stage 4. ISO 19650 information exchanges align with stages; "Level of information need" per BS EN 17412-1 replaces LOD ⚠.

### 6.4 Planning vs building control (don't conflate)
| Aspect | Planning permission | Building control |
|---|---|---|
| Question | Is the use/appearance acceptable? | Does construction comply with Building Regs? |
| Decision | Permission/refusal, conditions, S106/CIL | Approval/completion certificate |
| Time | 8 weeks (householder), 13 (major) ✓ ⚠ | 5 weeks (full plans, 2 months w/ extension) ⚠ |
| Permitted development | GPDO 2015 Sch. 2: rear single-storey extension 3 m attached / 4 m detached (6 / 8 m via prior approval) ⚠ | PD ≠ exempt from building regs |
Approval of one never implies the other.

---
## 7. Common rejection reasons / mistakes

**Planning invalidation:**
1. Location plan wrong scale (1:1250/2500) or no red line/blue line; no north point; not based on OS.
2. Block plan missing site levels/boundary dimensions; scale not shown.
3. Elevations missing materials, not all sides, or not 1:50/1:100.
4. Mixed units/format (`3.8m` vs `3800`), scale bars absent, plans not to scale when printed (PDF at A3 vs A1).
5. Existing vs proposed not clearly distinguished; proposed floor areas inconsistent.
6. Wrong ownership certificate; no DAS or heritage statement where required; BNG omitted.
**Building control:**
7. Stair rise/going outside AD K (rise >220, going <220, pitch >42°), headroom <2.0 m, guards <900/1100, gaps ≥100 mm.
8. No structural calcs / lintel sizes / steel beam spec / foundation depth vs trees.
9. Fire: no escape window (450 x 750 mm), no protected route, FD30 doors absent, fire-stopping details missing, compartment lines unlabelled.
10. Drainage: no falls (1:40/1:80), manhole depths, access, building over drains (build-over agreement with water company).
11. Insulation U-values/Part L not demonstrated (SAP/SBEM missing), thermal bridging, air-tightness.
12. Ventilation: extract rates not specified for each wet room (AD F), no background ventilators, overheating (AD O) assessment missing.
13. Part M: step-free access, level thresholds, accessible WC, door widths, switch heights 450–1200 mm.
14. Electrical: no EIC / Part P cert; consumer unit combustible enclosure; RCD protection.
15. Drawings out of date (revision not tracked), inconsistent naming per ISO 19650, wrong status code (S-codes), missing P/C revision.
16. Higher-risk buildings: Gateway 2 submitted without sufficient fire strategy/coordination.

---
## 8. Sources (URLs)

- Approved Documents collection — https://www.gov.uk/government/collections/approved-documents ✓ (dates)
- AD B — https://www.gov.uk/government/publications/fire-safety-approved-document-b ✓
- AD K — https://www.gov.uk/government/publications/protection-from-falling-collision-and-impact-approved-document-k ✓ (page only; stair numbers from secondary: https://www.designingbuildings.co.uk/wiki/Firefighting_stair , https://sitemate.com/?p=47389)
- AD M — https://www.gov.uk/government/publications/access-to-and-use-of-buildings-approved-document-m ✓ ; FAQ PDF https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/648232/FAQ_ADM_Vol1_and_Vol2.pdf
- AD F — https://www.gov.uk/government/publications/ventilation-approved-document-f ; secondary https://products.zehnder.co.uk/en/indoor-ventilation/insights/building-regulations
- UK BIM Framework / National Annex — https://www.cdbb.cam.ac.uk/files/national_annex_guidance.pdf ; https://www.ukbimframework.org/
- ISO 19650 naming discussion — https://www.pbctoday.co.uk/news/bim-news/bim-in-the-uk-changes-uk-naming-convention-uk-annex/112109/
- BS 7671 A3:2024 — https://www.bsigroup.com/en-GB/insights-and-media/insights/brochures/bs-76712018a32024-iet-wiring-regulations-amendment ✓
- Uniclass 2015 — https://www.thenbs.com/our-tools/uniclass
- RIBA Plan of Work 2020 — https://www.architecture.com/knowledge-and-resources/resources-landing-page/riba-plan-of-work
- Planning validation (national requirements) — https://www.gov.uk/guidance/make-a-planning-application ⚠ not fetched
- Scotland Technical Handbooks — https://www.gov.scot/policies/building-standards/ ⚠ not fetched
- NDSS — https://www.gov.uk/government/publications/technical-housing-standards-nationally-described-space-standard ⚠ not fetched
- Eurocode UK NAs — https://shop.bsigroup.com/ (BS EN 1990–1999 + NA)
- CIBSE Guides — https://www.cibse.org/knowledge-research/knowledge-portal
