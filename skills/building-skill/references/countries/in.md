# India (भारत) — Drafting & Code Reference

Legend: **✓** = read this session from a page (all secondary — BIS NBC/IS text is paid and was not accessible; MoHUA PDFs not fetched). **⚠ verify** = secondary/memory. **Important:** India has **no single national building permit rule.** The **National Building Code of India 2016 (NBC 2016, BIS SP 7)** is a model code; **each state/UT/municipal body adopts its own bye-laws** (the MoHUA *Model Building Bye-Laws 2016* is also a template, not binding by itself ✓). Values below are *typical* — **override with the city's current bye-laws/Master Plan/Zonal Plan.**

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Permit drawings in **metric (m / mm)** under NBC; but residential office/contractor drawings often **feet-inches** (e.g. 10'-6") ⚠ — state "all dimensions in mm unless noted" |
| Plot units | sq m, sq ft, sq yd (**gaj**), **cent / ground / bigha / biswa** regionally ⚠ |
| Language | English (permit); Hindi / regional language on vernacular forms and some municipalities ⚠ |
| Sheets | ISO A0–A4; A1 (594×841) common; some municipalities accept A3 booklet ⚠ |
| Scales | Site/ key plan 1:500–1:1000 (location 1:2000+), plans/elevations/sections **1:100**, details 1:20–1:5 ⚠ |
| Title block | Project, plot/survey/khasra no., ward, owner name, **Architect (COA registration no.) / Licensed Technical Personnel (LTP) / Engineer** ✓ practice, drawing no., scale, date ⚠ |
| Levels | Datum: road crown / plinth level (PL) +0.00; plinth ≥ 450 mm above road level typical ⚠ |
| Drafting standard | **IS 962:1989** Code of practice for architectural and building drawings; **SP 46:2003**; IS 10811 sheet sizes ⚠ |
| Area terms | **FAR** or **FSI (Floor Space Index)** = built-up area / plot area (synonyms ✓); **ground coverage**, **carpet / built-up / super built-up** ⚠ |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

| Topic | Practice |
|---|---|
| National e-portal | **OBPS (Online Building Permission System)** — MoHUA-driven; many states use own systems (Maharashtra **AutoDCR**, Delhi **DUAC/MCD e-portal**, Karnataka **BBMP/ BDA** online) ⚠ |
| CAD rules | AutoDCR and others require **DWG with prescribed layer names** (plot boundary, building outline, setbacks, rooms) and closed polylines for area calculation ⚠ — **ask the target ULB for the layer list** |
| Layers (skill default) | `A-WALL`, `A-DOOR`, `A-GLAZ`, `A-ANNO-DIMS`, `A-AREA` (closed polylines), `PLOT-BOUNDARY`, `SETBACK`, `ROAD` ⚠ |
| File naming | `[PlotNo]-[Floor]-[Rev].dwg` ⚠ |
| Digital signature | DSC (Class 3) of architect/ owner on e-portals ⚠ |
| Hard copy | Many ULBs still require 3–6 printed sets + stamped site plan ⚠ |

## 3. Drafting conventions

- **Required notes**: "Plot area (sq m)", "Road width (m)", "Permissible FAR / provided FAR", "Ground coverage %", "Parking provided", "Water harvesting (RWH) tank details", "Solar water heater", "STP" (large) ⚠.
- **Standard sheets**: Key plan, Site plan (with setbacks and road widths on all sides), Floor plans with area statement, Elevation(s), Section through staircase, Terrace plan, Drainage/ sewerage layout, Structural ⚠.
- **Setback display**: front/rear/left/right distances from boundary to built-up (excl. permissible projections) ✓.
- **Ventilation**: windows tagged "W1" with sizes; ventilation shafts dimensioned ✓ practice.
- **Rooms**: "Drawing room", "Puja", "Store", "Lobby", "Servant quarter", "Toilet (Indian + Western)", "Verandah" ⚠.
- **Accessibility**: ramp 1:12, rails, toilet for differently abled (NBC Part 3 Annex) ⚠.
- **Structural**: separate RCC drawings referencing **IS 456:2000**, **IS 1893 (Part 1):2016**, **IS 13920:2016**, **IS 875 (Parts 1–5)** ✓ names (editions per BIS catalogue) ⚠.

## 4. Governing codes & authorities

| Item | Code / authority | Status |
|---|---|---|
| NBC 2016 | **BIS SP 7**: Part 3 Development Control Rules & General Building Requirements; Part 4 Fire & Life Safety; Part 6 Structural Design (Sec 1–6); Part 8 Building Services (Sec 2 Electrical) | ✓ search summaries |
| Model Building Bye-Laws 2016 | MoHUA, Govt. of India (template for states) | ✓ |
| State/municipal bye-laws | e.g. **Delhi UBBL 2016 (Unified Building Bye-Laws)**, MCGM/DCPR 2034 (Mumbai), BBMP Zoning Regulations 2015 (Bengaluru), Hyderabad GO 168/ HMDA, Chennai CMDA DR, UP/Haryana/Punjab state rules | ✓ partial |
| Concrete | **IS 456:2000** Plain and Reinforced Concrete | ⚠ |
| Seismic | **IS 1893 (Part 1):2016** (zones II–V), IS 13920:2016, IS 4326 | ⚠ |
| Loads | **IS 875** Parts 1–5 (dead, imposed, wind, snow, special) | ⚠ |
| Fire | NBC Part 4; state **Fire Department NOC**; IS 16009/ IS 15683? | ⚠ |
| Electrical | **CEA (Measures relating to Safety and Electric Supply) Regulations 2023** (supersede 2010 version) ⚠; IS 732; NBC Part 8 Sec 2; DISCOM norms (voltage 230/415 V, 50 Hz) | ⚠ |
| Heritage/Environment | ASI/State heritage limits near monuments (100 m/ 200 m zones ⚠); EIA for ≥ 20,000 m² built-up (MoEFCC) ⚠ | ⚠ |
| Professionals | **Council of Architecture (COA)**, state LTP/ empanelled structural engineers | ✓ practice |

## 5. Key numbers (typical; secondary; **override with local bye-laws**)

| Item | Value | Source |
|---|---|---|
| Stair riser (residential) | **≤ 190 mm** (some sources 150–190 mm; one source 175 mm) | NBC 2016 Part 4 / Part 3 via infralens (secondary) ⚠ |
| Stair tread (going) | **≥ 250 mm** residential (one source 230 mm) | ⚠ |
| Stair clear width — individual house | ≥ 0.9–1.0 m | ⚠ conflicting |
| Stair clear width — apartments | **1.0 m (≤ G+3), 1.25 m (high-rise)** per infralens citing NBC Part 4 cl. 4.4.1; another source 1.5 m for common stairs | ⚠ conflicting |
| Travel distance (residential) | **22.5 m**, **30 m** if sprinklered (NBC Part 4 Table, cl. 4.4.2); IS 16550 summary 45 m for sprinklered | ⚠ conflicting |
| High-rise definition | height ≥ 15 m (NBC) → Fire NOC mandatory | ⚠ well-known |
| Habitable room min. | ≥ 9.5 m² one room, ≥ 7.5 m² others; min width 2.4 m / 2.1 m; kitchen ≥ 5.0 m² (min width 1.8 m) | NBC 2016 Part 3 ⚠ memory |
| Ceiling height | habitable ≥ 2.75 m (2.4 m in hilly/ Delhi ⚠), kitchen ≥ 2.75 m, bath/WC ≥ 2.2 m | ⚠ memory |
| Window area | ≥ 1/6 floor area (wall area 1/10 ⚠) | ⚠ memory |
| Door widths | main ≥ 1.0 m; internal ≥ 0.9 m; toilets ≥ 0.75 m | ⚠ memory |
| Delhi front setback (UBBL 2016-based table) | 0 m (≤ 50 m² plots), 3.0 m (100–250 m²), 4.5 m (250–500 m²) | studiomatrx (secondary) ⚠ |
| FAR range | 1.0–2.5 typical residential; UP: 2.0 for ≤ 150 m² plots dropping to 1.25 for > 1,200 m² | blogs ⚠ — set by Master Plan |
| Ground coverage | % by plot size and zone — **ask local authority** | ⚠ |
| Parking | 1 ECS (equivalent car space) per ~100 m² built-up (varies) ⚠; ECS = 23 m² incl. aisle ⚠ | ⚠ |
| Seismic zones | II (Z=0.10), III (0.16), IV (0.24), V (0.36) — IS 1893 (Part 1):2016 | ⚠ memory |
| RC cover | slab 20 mm, beam 25 mm, column 40 mm, footing 50 mm (moderate exposure) | IS 456:2000 Table 16 / cl.26.4 ⚠ memory |
| Electrical | 230 V single / 415 V three-phase, 50 Hz; ELCB/RCCB 30 mA | CEA/ IS 732 ⚠ |

## 6. Permit drawing set

1. Ownership/title docs, NOC from adjoining authorities (airport AAI height ⚠, fire, railway, environmental where relevant)
2. Architect's drawings (key plan, site plan, plans, sections, elevations, terrace, parking, RWH, area statement) signed by COA architect/ LTP
3. Structural design basis + drawings by structural engineer; soil report for > G+2 ⚠
4. Fire NOC drawings (hydrants, exits, firefighting) for ≥ 15 m or group housing/ commercial
5. Electrical/ plumbing/ HVAC layouts for large projects; sewage/ STP; RERA registration (if real-estate project)
6. Commencement certificate → Plinth check → Occupancy/ completion certificate (OC/CC) ✓ practice

## 7. Common rejection reasons

- FAR/ground coverage/height beyond zone limits; **setbacks not as per road width and plot size**.
- Mismatch between road width on drawing and Master Plan/revenue map.
- Missing structural engineer details, RWH, solar, STP or parking calculation.
- Stair width or travel distance below NBC Part 4 for the building height; no refuge/ fire lift where required.
- Area statement not matching closed polylines (AutoDCR-style checks).
- Non-conforming land-use (agricultural vs residential) or title/NOC gaps.

## 8. Sources

- Staircase design / NBC summaries (secondary): https://infralens.in/handbook/staircase-design , https://infralens.in/code/NBC-2016-Part-4-2016 ⚠
- NBC 2016 Part 4 fire summary: https://infralens.in/knowledge/nbc-2016-part-4-fire-safety ⚠
- MoHUA Model Building Bye-Laws summaries / setbacks: https://www.studiomatrx.org/students/build-your-own-house-india/byelaws-far-setbacks-india ⚠ , https://www.studiomatrx.org/india/delhi/setbacks ⚠
- Mumbai/Bengaluru/Delhi comparison: https://infralens.in/knowledge/setback-rules-india-hmda-bbmp-mcgm-dda-comparison ⚠
- Official: BIS (NBC 2016 purchase) https://www.bis.gov.in ; MoHUA https://mohua.gov.in ; CEA https://cea.nic.in — not opened ⚠
