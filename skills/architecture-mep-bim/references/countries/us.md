# United States — Drafting & Code Reference

Legend: **✓** = checked against a primary/near-primary source this session (URL in §8). **⚠ verify** = from drafter knowledge or secondary source only; confirm against the adopted code text before issuing drawings. Edition years assume a 2026 reader. The US has NO single national building code: model codes (ICC, NFPA) are adopted by states and then amended by cities/counties. ALWAYS ask/identify: state, city, adopted code edition, local amendments.

---
## 1. Units, scales, sheets

### 1.1 Units & dimension format
| Item | US practice |
|---|---|
| Unit system | US customary. Architectural: feet-inches. Civil/site: decimal feet (engineering scale). Structural: feet-inches (some firms decimal for elevations). MEP: inches for equipment, feet for ducts/pipe lengths, CFM/GPM/BTU/h/kW |
| Architectural dim format | `12'-6"`, `0'-8"`, `3'-4 1/2"`; fractions to 1/16" (rare below 1/8" on plans); hyphen between feet and inches; ALWAYS show `0'-` (not `-8"`). No units suffix needed once format shown |
| Civil/site format | decimal feet `125.50'`; stationing `STA 12+50.00`; elevations in feet to 0.01 ft (NAVD88 / project datum); bearings `N 45°30'15" E` |
| Metric | Only on federal/DOT jobs that require SI; show soft-metric in `[ ]` brackets or as a secondary dual-dim |
| Elevations | `+0'-0"` = finish floor at level 1 (or actual `EL 100'-0"`); levels ref `LEVEL 2 / EL +12'-0"` |
| Language | US English (e.g., "color", "gray", "elevator", "restroom", "stairs") |
| Date format | MM/DD/YYYY or month spelled out |
| Rounding | Sizes in inches use nominal framing names (2x4, 2x6) — actual 1-1/2"x3-1/2" / 1-1/2"x5-1/2" ⚠ verify nominal vs actual on every detail |

### 1.2 Typical scales (US architectural scale = fractional-inch per foot; civil = 1"=N ft)
| Drawing type | Typical scale | Notes |
|---|---|---|
| Site/civil plan | 1"=20' (also 1"=10', 30', 40', 50') | Civil engineering scale (decimal). Large sites 1"=50' / 1"=100' |
| Vicinity/location map | NTS or 1"=1000' | |
| Floor plans (commercial) | 1/8"=1'-0" (1:96); 1/4"=1'-0" (1:48) for small or enlarged | Large footprints at 1/16" |
| Floor plans (residential) | 1/4"=1'-0" | 1/8" for roof plans |
| Reflected ceiling plans | same as floor plan | |
| Elevations | 1/4"=1'-0" (res); 1/8" (commercial) | |
| Building sections | 1/4" or 1/8" | |
| Wall sections | 3/4" or 1/2"=1'-0" | |
| Enlarged plans (toilets, stairs, elevators) | 1/2"=1'-0" or 3/8" | |
| Details | 1-1/2"=1'-0", 3"=1'-0", 1"=1'-0", 6"=1'-0" (full-size also) | |
| Structural plans | 1/8" or 1/4" | Details 3/4", 1-1/2" |
| MEP plans | 1/8" or 1/4" | Mech/elec rooms 1/4"–1/2" |
| Scale bar | Include graphic scale because sheets get reduced to half size (ARCH D → 11x17) | |

### 1.3 Sheet sizes (ANSI/ASME Y14.1 + Architectural)
| Series | Letter | Inches | mm |
|---|---|---|---|
| ANSI | A | 8.5x11 | 216x279 |
| ANSI | B | 11x17 | 279x432 |
| ANSI | C | 17x22 | 432x559 |
| ANSI | D | 22x34 | 559x864 |
| ANSI | E | 34x44 | 864x1118 |
| ARCH | A | 9x12 | 229x305 |
| ARCH | B | 12x18 | 305x457 |
| ARCH | C | 18x24 | 457x610 |
| ARCH | D | 24x36 | 610x914 |
| ARCH | E1 | 30x42 | 762x1067 |
| ARCH | E | 36x48 | 914x1219 |
Most common permit sheet: ARCH D 24x36 (small res: 18x24). Many jurisdictions cap at 36x48 and require min sheet size (e.g., ≥ 11x17 for small additions) — ⚠ verify per city checklist. Margins: ~1/2" top/bottom/right, 1-1/2" binding edge left ⚠ firm-dependent.

### 1.4 Title block fields (typical)
Firm name/logo/address/license no.; PROJECT name & address; CLIENT; Consultant block(s) with seals; ISSUE/REVISION table (no., date, description); Sheet title; Sheet number (e.g., A-101); Project number; Date; Drawn/Checked initials; Scale; North arrow (on plans); Seal/signature block (see §6 for Texas). NCS: title block on right edge (vertical) or bottom is both accepted; NCS sheets carry "key plan" for partial plans ⚠ verify.

### 1.5 North arrow / grid
- Plans oriented with North up (or up/right); show north arrow on every plan sheet and key plan. True north on site plans, plan north if rotated.
- Column grid: letters (A, B, C…) one direction, numbers (1, 2, 3…) the other; letters skip I and O ⚠ verify firm standard. Bubbles at both ends of grid lines on structural; at least at one end on arch.

---
## 2. CAD layer & file naming standard

**Standard:** US National CAD Standard (NCS) — maintained by the National Institute of Building Sciences (NIBS) buildingSMART alliance. Components: **Uniform Drawing System (UDS, modules 1–8)**, **CAD Layer Guidelines** (derived from AIA CAD Layer Guidelines 2nd ed. 1997), **Plotting Guidelines**. NCS is licensed (full text paywalled) → layer strings below are the widely published pattern; ⚠ verify minor-group codes against the licensed NCS before claiming compliance. Site lists NCS V6; check for V7 ⚠. (nationalcadstandard.org)

### 2.1 Layer name syntax (NCS/AIA)
`DISCIPLINE - MAJOR - MINOR1 - MINOR2 - STATUS`, hyphen-separated, uppercase, 4-character fields:
| Field | Chars | Meaning | Example |
|---|---|---|---|
| Discipline designator | 1 (optional 2nd = sub-discipline) | Level 1 letter | A |
| Major group | 4 | Principal building system | WALL |
| Minor group 1 | 4 (optional) | Qualifier | FULL |
| Minor group 2 | 4 (optional) | Further qualifier | DIMS |
| Status | 1 (optional) | N new, E existing to remain, D existing to demolish, F future, T temporary, M items to be moved, X not in contract, 1–9 phase | N |
Result: `A-WALL-FULL-N`.
Discipline designators (Level 1): G General, H Hazardous materials, V Survey/Mapping, B Geotechnical, C Civil, L Landscape, S Structural, A Architectural, I Interiors, Q Equipment, F Fire Protection, P Plumbing, D Process, M Mechanical, E Electrical, W Distributed Energy, T Telecommunications, R Resource, X Other, Z Contractor/Shop Drawings, O Operations. ⚠ verify list vs NCS V6/V7.

### 2.2 Example layers (colors = common AutoCAD ACI convention, NOT mandated by NCS; lineweights = typical plotted mm, NCS plotting guidelines leave to firm)
| Layer | Content | ACI color | Lineweight (mm) |
|---|---|---|---|
| A-WALL | Walls (general; cut) | 7 white/black | 0.50 |
| A-WALL-FULL | Full-height walls | 7 | 0.50 |
| A-WALL-PRHT | Partial-height walls | 8 gray | 0.35 |
| A-DOOR | Doors, swings | 2 yellow | 0.25 |
| A-GLAZ | Windows/glazing | 4 cyan | 0.25 |
| A-COLS | Columns (arch) | 7 | 0.50 |
| A-FLOR-STRS | Stairs | 3 green | 0.25 |
| A-FLOR-HRAL | Handrails | 3 | 0.18 |
| A-FLOR-OVHD | Overhead items (dashed) | 8 | 0.18 |
| A-CLNG | Ceiling | 5 blue | 0.18 |
| A-FURN | Furniture | 8 | 0.13 |
| A-AREA-IDEN | Room names/areas | 7 | 0.18 |
| A-ANNO-DIMS | Dimensions | 1 red | 0.18 |
| A-ANNO-TEXT | General text | 7 | 0.18 |
| A-ANNO-NOTE | Notes/keynotes | 7 | 0.18 |
| A-ANNO-SYMB | Symbols (north arrow, tags) | 7 | 0.25 |
| A-ANNO-TTLB | Title block | 7 | 0.35–0.70 |
| A-ANNO-NPLT | Non-plotting | 9 | n/a (no plot) |
| A-SECT-MCUT | Section cut (major) | 7 | 0.70 |
| A-ELEV-OTLN | Elevation outline | 7 | 0.50 |
| A-GRID | Column grid | 1 | 0.13 |
| S-COLS | Structural columns | 1 | 0.50 |
| S-BEAM | Beams | 4 | 0.35 |
| S-FNDN | Foundation | 6 magenta | 0.50 |
| S-GRID | Structural grid | 1 | 0.13 |
| S-SLAB | Slab edges/depressions | 3 | 0.35 |
| M-HVAC-DUCT | Ductwork ⚠ verify minor | 5 | 0.35 |
| M-HVAC-SDFF | Supply diffusers ⚠ | 4 | 0.25 |
| M-HVAC-RDFF | Return/exhaust grilles ⚠ | 4 | 0.25 |
| M-PIPE | Mech piping ⚠ | 6 | 0.35 |
| E-LITE | Light fixtures | 2 | 0.25 |
| E-POWR | Power/receptacles | 3 | 0.25 |
| E-POWR-PANL | Panels | 1 | 0.35 |
| E-COMM | Communications ⚠ | 5 | 0.25 |
| P-DOMW | Domestic water ⚠ | 5 | 0.35 |
| P-SANR | Sanitary/waste/vent ⚠ | 3 | 0.35 |
| P-STRM | Storm drainage ⚠ | 2 | 0.35 |
| P-FIXT | Plumbing fixtures | 4 | 0.25 |
| F-SPRN | Sprinkler heads/piping ⚠ | 1 | 0.25–0.35 |
| F-ALRM | Fire alarm devices ⚠ | 1 | 0.25 |
| C-ROAD, C-STRM, C-SSWR, C-TOPO | Civil road/storm/sewer/topo | varies | varies |
| L-PLNT | Landscape planting | 3 | 0.25 |

### 2.3 File & sheet numbering
- **Sheet identifier (NCS UDS Module 2):** `D-TNN` or `D-TNNN` : D = discipline designator; T = sheet type digit; NN(N) = sequence. Examples: `G-001` general, `A-101` first floor plan, `A-201` exterior elevations, `A-301` building sections, `A-501` details, `A-601` schedules, `S-201` foundation plan, `M-101` mechanical plan, `E-101` power plan, `P-101` plumbing plan.
- **Sheet type digits:** 0 General (cover, notes, legends), 1 Plans, 2 Elevations, 3 Sections, 4 Large-scale views (enlarged plans, stairs), 5 Details, 6 Schedules & diagrams, 7–8 user-defined, 9 3D/photo.
- **Discipline order in a set:** G, H, V, B, C, L, S, A, I, Q, F, P, D, M, E, W, T, R, X, Z, O.
- **Detail/section/elevation reference** shows `detail number / sheet number`, e.g. `3 / A-501`.
- **Project file naming (not standardized by NCS):** `ProjNo_Discipline_SheetNo_Description_Rev.dwg`, e.g. `24017_A_A-101_FloorPlan_R2.dwg`; Xrefs prefixed `X-`. Keep filenames free of spaces/special chars.
- **Plotting:** NCS Plotting Guidelines define pen/lineweight tables; plot with CTB/STB mapping color→pen. Use paper-space viewports, model space 1:1 in feet or inches (never mixed). Set INSUNITS = inches (arch) or feet (civil).

---
## 3. Drafting conventions

### 3.1 Dimension & text (paper heights, plotted)
| Item | Value |
|---|---|
| General notes / dimension text | 1/8" (3 mm) plotted, all-caps sans-serif or architectural font; min legibility ~3/32" (2.4 mm) ⚠ firm/NCS |
| Room names, sub-titles | 3/16" (4.8 mm) |
| View titles | 1/4" (6 mm), underlined |
| Sheet title in title block | 3/8"–1/2" |
| Dimension line | 0.18–0.25 mm; arch ticks (45° slash, 1/8" long) or closed dot at structure; extension line gap 1/16", overshoot 1/8" ⚠ firm practice |
| Dimension strings | Typically 3 strings on exterior: overall; wall/opening centers; detail. Dim to face of stud/CMU, centerline of column grid ⚠ firm convention; state "face of stud / face of masonry / centerline" in plan notes |
| Leader | Arrowed/dotted, 30–60°, horizontal landing at note |
Text scale in model space = plotted height × scale factor (e.g., 1/8" text at 1/4"=1' → 6" model height; at 1/8"=1' → 12").

### 3.2 Symbols & tags (UDS Module 6; shape conventions ⚠ firm variants exist)
| Item | Convention |
|---|---|
| Door tag | Numbered tag at door, often a hexagon or circle; number keys to door schedule (e.g., `101`, `101A`). Doors numbered by room number + suffix |
| Window tag | Letter in hexagon/diamond/oval or number; keys to window schedule |
| Room tag | Room name + number (box) |
| Wall type tag | Hexagon/oval w/ letter-number; wall type legend references UL/GA assembly (e.g., UL U305, GA WP 1200) |
| Grid bubble | Circle 3/8"–1/2" dia., letters/numbers inside |
| Section marker | Circle on cut line with arrow showing view direction; top = section number, bottom = sheet number |
| Building elevation marker | Circle with triangle arrow, number/sheet |
| Detail callout | Circle; number top / sheet bottom, bubble on boundary of enlarged area |
| Revision | Triangle with rev. no. + cloud around change |
| Keynote | Number/letter in hex; keynote legend per sheet (CSI MasterFormat/UniFormat-coded) |
| North arrow | Arrow w/ N; on each plan |
| Spot elevation | Triangle or cross `±0'-0"` / `EL 101.50` |
| Level marker | Triangle datum line w/ name and elev |
| Interior elevation | Square/diamond on floor plan with arrow(s) and number/sheet |
| Match line | Heavy line with `MATCH LINE – SEE A-102` |
| Dimensions: finishes | `CLR` clear; `NOM` nominal; `V.I.F.` verify in field; `TYP` typical; `U.N.O.` unless noted otherwise; `A.F.F.` above finish floor |

### 3.3 Hatch patterns (AutoCAD standard .pat names; US practice)
| Material | Pattern (typical) |
|---|---|
| Concrete (section) | AR-CONC (dots/triangles) or ANSI-"CONC" (dot + gravel) |
| CMU / block | Light diagonal hatch (ANSI31 sparse) w/ block joints outlined, or crosshatch 'ANSI37' |
| Brick (section) | ANSI31 at 45° 1/8" (or ANSI37 cross) |
| Earth | EARTH (45° long lines w/ ticks) |
| Gravel / aggregate fill | GRAVEL (AR-SAND denser) |
| Sand | AR-SAND |
| Wood (section, framing) | Diagonal "X" in rectangle for blocking; continuous wood = ANSI? — typical: 'X' for rough; lines along grain for finish wood ⚠ firm |
| Plywood/sheathing | Thin parallel stripes (3 thin lines) |
| Gypsum board | Thin double line (or solid grey) — rarely hatched at small scale |
| Batt insulation | Wavy "squiggle" — INSUL (custom) |
| Rigid insulation | Parallel lines with X or open rectangle |
| Steel (section) | ANSI32 or solid (black) for rolled shapes at ≥1" scales |
| Aluminum | ANSI33 |
| Glass | Single thin line with 45° tick marks (or three lines) |
| Stone | Random irregular outline |
| Tile | Orthogonal grid |
Notes: hatch scale in paper space; no hatch patterns on cut line at small scale (<1/4") — use solid poché. These are firm conventions, not code; ⚠ verify.

### 3.4 Line types (ANSI/AIA ⚠)
| Line | Use | Weight (mm) |
|---|---|---|
| Continuous heavy | Cut walls/sections | 0.50–0.70 |
| Continuous medium | Edges beyond, doors/windows | 0.25–0.35 |
| Continuous light | Dimensions, hatch, annotation | 0.13–0.18 |
| Dashed (HIDDEN) | Hidden/overhead/above | 0.18–0.25 |
| Center (long-short dash) | Center lines, grid | 0.13 |
| Phantom (long-short-short) | Alternate position, future | 0.18 |
| Dash-dot | Property line (long dash with dots "PROPERTY"), setbacks | 0.35 |
| Break line | Zigzag for break | 0.18 |

---
## 4. Governing codes & authorities

| Discipline | Model code / standard | Edition (current as of Oct 2026; local adoption lags) | Who enforces |
|---|---|---|---|
| Building (non-residential, multi-family >3 stories) | **International Building Code (IBC)** — ICC | 2024 published (ICC); most jurisdictions on 2018/2021; ⚠ verify local | City/county building dept (AHJ) |
| 1&2-family & townhouses ≤3 stories | **International Residential Code (IRC)** | 2024 published; many on 2018/2021 | AHJ |
| Existing buildings | International Existing Building Code (IEBC) | 2021/2024 | AHJ |
| Fire / life safety | International Fire Code (IFC) and/or **NFPA 1**, **NFPA 101 Life Safety Code** | IFC 2021/2024; NFPA 101 2024 ⚠ | Fire marshal / AHJ; (NFPA 101 mainly adopted for health care by CMS, and some states) |
| Sprinklers | **NFPA 13** (also 13R, 13D) | 2022 / 2025 ed ⚠ verify | AHJ/fire marshal |
| Fire alarm | **NFPA 72** | 2022 / 2025 ed ⚠ | Fire marshal |
| Electrical | **NFPA 70 National Electrical Code (NEC)** | 2023 (most states); **2026 edition published**, adoption pending ⚠ | State/local electrical inspector; state licensing (e.g., TDLR in Texas) |
| Plumbing | **International Plumbing Code (IPC)** or **Uniform Plumbing Code (UPC, IAPMO)** | 2021/2024; UPC used in CA, WA (UPC), OR, parts of West ⚠ | AHJ |
| Mechanical | **International Mechanical Code (IMC)** or UMC (IAPMO) | 2021/2024 | AHJ |
| Fuel gas | International Fuel Gas Code (IFGC) / NFPA 54 | 2021/2024 | AHJ |
| Energy | **IECC** (ICC) + **ASHRAE 90.1** (commercial alternative) | IECC 2021 / 2024; ASHRAE 90.1-2019/2022 ⚠ verify | State energy office / AHJ |
| Ventilation/IAQ | ASHRAE 62.1 (commercial), 62.2 (residential) | 62.1-2019/2022 ⚠ | AHJ via IMC |
| Accessibility (federal) | **2010 ADA Standards for Accessible Design** (DOJ) + ABA (Architectural Barriers Act) | 2010 (in effect since 2012) ✓ | DOJ (private suits & enforcement); no plan review by DOJ; AHJ enforces via ICC A117.1 |
| Accessibility (building code) | IBC Ch.11 + **ICC A117.1** | A117.1-2017 (IBC 2021/2024) | AHJ |
| Housing | Fair Housing Act Accessibility Guidelines (FHAA) — multi-family ≥4 units | 1991 | HUD (complaint-driven) |
| Structural loads | **ASCE 7** | ASCE 7-16 (IBC 2021), ASCE 7-22 (IBC 2024) | AHJ plan reviewer |
| Concrete / steel / wood / masonry | ACI 318, AISC 360 (+341 seismic), AWC NDS (+SDPWS), TMS 402/602 | per IBC ch.35 | AHJ |
| Wildland-urban interface | IWUIC | where adopted | Fire/building |
| Zoning (land use) | Municipal zoning ordinance / UDC | Not a model code | City planning dept; variances through BOA/BZA |
| Subdivision/platting | Local + state | | City/county |
| Stormwater | Local/state (EPA NPDES) | | City public works / state agency |
| Historic | NPS standards + local landmark commission | | SHPO / commission |

### 4.1 State adoption & Texas note
- Adoption is **state-by-state, and local municipalities/counties amend further**; model-code editions are NOT uniform. Some states (CA Title 24/CBC, FL FBC, NY, MA, WA, OR, NJ) have their own state-written code based on ICC. California uses CBC/CRC/CPC/CMC/CEC/Title 24 energy. Florida FBC (Wind-borne debris regions). ⚠ verify
- **Texas:** Historically no statewide building code. Municipalities adopt codes; state law sets a baseline: ICC page states Texas adopted 2012 IBC/IRC as mandatory municipal standards from June 7, 2021; local building code adoption occurs at the local level (iccsafe.org/advocacy/adoption-map/texas) ✓ (secondary summary). Major cities typically adopt newer editions (e.g., 2021 IBC/IRC). ⚠ verify per city (Houston, Dallas, Austin, San Antonio, Fort Worth each have local amendments).
- Texas: **TDLR** (Texas Dept. of Licensing & Regulation) administers Texas Accessibility Standards (TAS); TAS 2012 is the adopted accessibility standard (aligned to 2010 ADA with Texas differences) and requires project registration and review/inspection (RAS) for projects over a cost threshold ($50,000 ⚠ verify). TDLR also licenses electricians and adopts the NEC (2020 for industrialized housing/ buildings per TDLR; 2023 statewide ⚠ verify).
- ICC release (Aug 2026): Texas TDLR adopted 2024 IMC, IFGC, IRC, effective **Sept 1, 2026** (scope likely industrialized housing/state rule, not clearly statewide) ✓ source; ⚠ verify scope. TDLR rule: industrialized housing/buildings use 2021 IBC/IRC/IMC/IPC/IFGC, 2015 IECC, 2020 NEC (effective July 1, 2024) ✓ (TDLR).
- Texas coastal (TDI/TWIA windstorm designated catastrophe area; engineer-certified WPI-8 forms) ⚠ verify. Texas Energy: SECO adopts IECC for state; residential IECC 2015 baseline in many local jurisdictions; 2021 IECC adoption timeline ⚠ verify.
- Professional seal: In Texas, plans must be sealed by a Registered Architect (Texas Board of Architectural Examiners) and/or PE (TBPELS) as required by Occupations Code ch.1051/1001; many single-family houses are exempt ⚠ verify.
- Local zoning (setbacks, FAR, height, lot coverage, parking minimums, landscaping, impervious cover) is **municipal** — Houston has no zoning but deed restrictions & ordinance (setbacks, parking); Dallas/Austin/SA use zoning districts. Counties may regulate in ETJ limited ways.

---
## 5. Key numbers

Citation key: IRC = 2021 International Residential Code; IBC = 2021 International Building Code. Editions 2024 mostly unchanged for these values; ⚠ confirm numbers if jurisdiction uses a different edition.

### 5.1 Residential stairs (IRC R311.7)
| Item | Value (US) | Metric | Source/status |
|---|---|---|---|
| Min stair clear width | 36" (above handrail height); handrail may project 4-1/2" each side | 914 mm; 114 mm | IRC R311.7.1 — secondary (city handouts) ⚠ verify |
| Max riser | 7-3/4" | 197 mm | IRC R311.7.5.1 — secondary ⚠ |
| Riser variation | max 3/8" between largest & smallest in flight | 9.5 mm | R311.7.5.1 ⚠ |
| Min tread (run) | 10" | 254 mm | R311.7.5.2 — secondary ⚠ |
| Nosing | 3/4" to 1-1/4" required if tread < 11"; solid risers | 19–32 mm | R311.7.5.3 ⚠ |
| Headroom | 6'-8" (measured vertically from nosing line) | 2032 mm | R311.7.2 ⚠ |
| Winder tread | min 10" at walkline; 6" min at narrow end | 254 / 152 mm | R311.7.5.2.1 ⚠ |
| Spiral stair | 26" clear width; riser 9-1/2" max; 6'-6" headroom; tread 6-3/4" at 12" from narrow edge | 660 / 241 / 1981 / 171 mm | R311.7.10.1 ⚠ (verify numbers) |
| Landing | width ≥ stair width; depth ≥ 36" in direction of travel | 914 mm | R311.7.6 ⚠ |
| Max vertical rise between landings | 12'-7" | 3835 mm | R311.7.3 ⚠ |
| Handrail required | on at least one side where ≥4 risers | | R311.7.8 ⚠ |

### 5.2 Guards & handrails
| Item | Value | Source/status |
|---|---|---|
| Residential guard height | 36" min (914 mm); on open side of stair 34" (864 mm) measured from tread nosing line | IRC R312.1.2 ⚠ |
| Guard required when floor/grade drop | > 30" (762 mm) | R312.1.1 ⚠ |
| Max opening in guard | 4" sphere (102 mm); stair triangle opening 6" sphere | R312.1.3 ⚠ |
| Residential handrail height | 34"–38" (864–965 mm) above nosing | R311.7.8.1 ⚠ |
| Handrail grip (circular) | 1-1/4" – 2" dia. (32–51 mm) | R311.7.8.5 ⚠ (also ADA 505.7.1 ✓) |
| Handrail clearance to wall | 1-1/2" min (38 mm) | ADA 505.5 ✓ |
| Commercial (IBC) guard | 42" (1067 mm) min; 4" sphere; <21" high intermediate rail no ladder effect | IBC 1015.3–1015.4 ⚠ |
| Commercial handrail | 34–38" ; extensions 12" at top, tread depth + 12" at bottom | IBC 1014.2, 1014.6 ⚠; ADA 505.10 ✓ |
| Guard load | 50 plf, 200 lb concentrated; infill 50 lb on 1 sq ft | IBC 1607.9 ⚠ |

### 5.3 Egress (IBC Chapter 10)
| Item | Value | Source/status |
|---|---|---|
| Egress width stairs | 0.3 in. per occupant (7.6 mm) | IBC 1005.3.1 ✓ (secondary source) |
| Egress width other components | 0.2 in. per occupant (5.1 mm); sprinklered+alarm reduces stairs to 0.2 in. | IBC 1005.3.1–.2 ✓/⚠ |
| Stair min width (commercial) | 44" (1118 mm); 36" if occupant load served < 50 | IBC 1011.2 ✓ (secondary) |
| Riser/tread (commercial) | riser 7" max, 4" min; tread 11" min | IBC 1011.5.2 ⚠ |
| Door clear width | 32" min (815 mm) clear opening; 80" high | IBC 1010.1.1 ✓ (clear width; height ⚠) |
| Door swing | in direction of egress for occupant load ≥ 50 (A, E) or H | IBC 1010.2.1 ⚠ |
| Corridor min width | 44" general; 36" for < 50 occ.; 72" educational (corridors w/ occupant load ≥ 100); 96" I-2 | IBC 1020.2 ⚠ |
| Dead-end corridor | 20 ft (6.1 m); 50 ft (15.2 m) in sprinklered B, E, F, I-1, M, R-1, R-2, R-4, S, U | IBC 1020.5 ⚠ |
| Common path of travel | 75 ft; 100 ft sprinklered B, F, S ⚠ | IBC 1006.2.1 / Table 1006.2.1 ⚠ |
| Exit access travel distance (Table 1017.2) | B: 200 ft unsprinklered / 300 ft sprinklered ✓ (secondary); A, E, F-1, M, S-1: 200/250 ft ⚠; R-2 (sprinklered) 250 ft ⚠ | IBC Table 1017.2 |
| Number of exits per story | 1–500 occ.: 2; 501–1000: 3; >1000: 4 | IBC 1006.3.1 ⚠ |
| Exit separation | ≥ 1/2 diagonal (1/3 if sprinklered) | IBC 1007.1.1 ⚠ |
| Occupant load factors (gross unless noted) | Business 150; Assembly unconcentrated 15 net; concentrated 7 net; standing 5 net; Classroom 20 net; Mercantile 60; Residential 200; Storage 300; Warehouse 500; Kitchen commercial 200; parking garage 200 | IBC Table 1004.5 ⚠ |
| Exit enclosures | 1-hr (< 4 stories), 2-hr (≥ 4 stories) | IBC 1023.2 ⚠ |
| Min ceiling height | 7'-6" (2286 mm) occupiable; 7'-0" bathrooms/corridors/storage | IBC 1208.2 ⚠ |
| Residential ceiling height | 7'-0" (2134 mm) habitable; basement 6'-8"; beams 6'-4" | IRC R305.1 ⚠ |
| Hallway width (dwelling) | 36" (914 mm) | IRC R311.6 ⚠ |
| Egress door (dwelling) | 1 door ≥ 32" clear x 78" clear height, side-hinged | IRC R311.2 ⚠ |
| Emergency escape & rescue opening | ≥ 5.7 sq ft net clear (5.0 at grade); min height 24", min width 20"; sill ≤ 44" AFF; window well 9 sq ft, 36" min dimension | IRC R310.2 ⚠ |
| Room area | 70 sq ft min habitable room (kitchens excepted), 7' min dimension; (some editions 120 sq ft one room) | IRC R304 ⚠ (2021 revision status) |
| Natural light/vent | glazing 8% of floor area; openable 4%; | IRC R303.1 ⚠ |
| Smoke/CO alarms | each sleeping room, outside each sleeping area, each level; CO outside bedrooms if fuel-burning/attached garage | IRC R314/R315 ⚠ |

### 5.4 Accessibility (2010 ADA Standards — access-board.gov, ✓ verified)
| Item | Value | ADA § |
|---|---|---|
| Door clear width | 32" (815 mm) min; 36" if opening deeper than 24" | 404.2.3 ✓ |
| Maneuvering clearance, pull side, front approach | 60" perpendicular x latch side 18" beyond | 404.2.4.1 ✓ |
| Maneuvering, push side, front approach | 48" perpendicular (+12" if latch & closer) | 404.2.4.1 ✓ |
| Hardware height | 34"–48" AFF; opening force 5 lbf interior | 404.2.7 / 404.2.9 ✓ |
| Clear floor space | 30"x48" (760x1220 mm) | 305.3 ✓ |
| Turning space | 60" dia. circle or T-shape (60" sq., arms 36" wide) | 304.3 ✓ |
| Walking surface width | 36" min (32" for ≤ 24" length) | 403.5.1 ✓ |
| Passing space | at ≤ 200 ft intervals where width < 60" | 403.5.3 ✓ |
| Running slope walk | ≤ 1:20; cross slope ≤ 1:48 | 403.3 ✓ |
| Ramp slope | ≤ 1:12; rise ≤ 30" per run; width 36" min; landings 60" long; handrails if rise > 6" | 405.2, .5, .6, .7, .8 ✓ |
| Curb ramp | slope ≤ 1:12; flares ≤ 1:10; top landing 36" | 406 ✓ |
| Reach range | 15" min – 48" max (unobstructed forward/side) | 308 ✓ |
| Protruding objects | 27"–80" AFF may project ≤ 4"; headroom 80" | 307 ✓ |
| Stairs (accessible) | riser 4"–7"; tread 11" min; nosing radius ≤ 1/2" | 504 ✓ |
| Handrail | 34"–38"; 1-1/2" from wall; extension 12" | 505 ✓ |
| WC centerline | 16"–18" from side wall; clearance 60" x 56" | 604.2, 604.3 ✓ |
| Grab bars | rear 36", side 42", 33"–36" high | 604.5, 609.4 ✓ |
| Accessible car stall | 96" (2440 mm) wide; van 132" with 60" aisle or 96" with 96" aisle; aisle 60" | 502 ✓ |
| Van clearance | 98" (2490 mm) | 502.5 ✓ |
| Number of accessible spaces | 1 per 25 spaces up to ... (Table 208.2); 1 van per 6 | 208 ✓ (partial) |
| Passenger loading | 96" wide x 20 ft long pull-up | 503.2 ✓ |
| Elevator exemption | < 3 stories or < 3000 sq ft/story (not for shopping center, health care) | 36.404 ✓ |
| Path of travel alterations | 20% disproportionality cap | 36.403 ✓ |

### 5.5 Parking (zoning — municipal) ⚠ verify per city
| Item | Typical | Note |
|---|---|---|
| Standard stall | 9' x 18' (2.7 x 5.5 m); 8.5'x18' compact in some cities | Zoning code |
| Drive aisle | 24' two-way (7.3 m); 90° parking aisle 24'; 60° 18'; 45° 13' ⚠ | |
| Ratios | Office 1/300 sq ft; retail 1/250; restaurant 1/100; res 1–2/unit ⚠ | Vary; many cities removing minimums |
| Bicycle | per local | |
| Accessible | per ADA §5.4 ✓ | |

### 5.6 Fire separation basics (IBC)
| Item | Value | Source/status |
|---|---|---|
| Shaft enclosure | 1-hr (< 4 stories), 2-hr (≥ 4) | IBC 713.4 ⚠ |
| Door ratings in rated walls | 3-hr wall → 3-hr door; 2-hr → 1-1/2 hr; 1-hr shaft/exit → 1-hr; 1-hr corridor → 20-min | IBC Table 716.1(2) ⚠ |
| Dwelling–garage | 1/2" gyp on garage side; 5/8" Type X under habitable; 20-min or solid-wood 1-3/8" door | IRC R302.6 ⚠ |
| Townhouse separation | 1-hr (common wall, each unit) or 2-hr common | IRC R302.2 ⚠ |
| Exterior walls < 5 ft from lot line | 1-hr rated, no openings < 3 ft | IRC R302.1 ⚠ |
| Occupancy separation | Table 508.4 | IBC ⚠ |
| Construction types | I–V (A/B); Table 601 for ratings; Tables 504.3/504.4/506.2 height/area | IBC ⚠ |
| Sprinkler spacing (NFPA 13) | Light hazard: ≤ 225 sq ft (20.9 m²)/head, ≤ 15 ft (4.6 m); Ordinary: 130 sq ft (12.1 m²), 15 ft; Extra: 100 sq ft (9.3 m²), 12 ft | NFPA 13 ⚠ |
| Sprinkler distance | ≥ 6 ft between heads; deflector 1"–12" below ceiling | NFPA 13 ⚠ |
| Fire alarm | pull stations within 5 ft of exit, ≤ 200 ft travel; height 42"–48"; strobes 80"–96" AFF; smoke det spacing 30 ft | NFPA 72 ⚠ |

### 5.7 Electrical (NEC 2023)
| Item | Value | Source/status |
|---|---|---|
| Dwelling wall receptacle spacing | no point along wall > 6 ft from receptacle (12 ft max spacing); wall ≥ 2 ft needs one | NEC 210.52(A) ⚠ |
| Kitchen countertop | no point > 24" (610 mm) from receptacle; ≥ 12" wide counters | NEC 210.52(C) ⚠ |
| Bathroom | ≥ 1 GFCI receptacle within 36" of basin edge | 210.52(D) ⚠ |
| Outdoor | front & back (≤ 6'-6" AFG) | 210.52(E) ⚠ |
| GFCI | bathrooms, garages, outdoors, kitchen counters, laundry, basements, within 6 ft of sink | 210.8 ⚠ |
| AFCI | bedrooms, living areas etc. in dwellings | 210.12 ⚠ |
| Working clearance | 36" depth (cond. 1, 0–150V), 30" width min, 6'-6" (2.0 m) headroom | 110.26 ⚠ |
| Branch circuits dwelling | 2 x 20A small-appliance; 1 laundry 20A; 1 bathroom 20A | 210.11(C) ⚠ |
| Max OCPD height | 6'-7" (2.0 m) | 240.24(A) ⚠ |
| Min dwelling service | 100 A | 230.79(C) ⚠ |
| Switch/receptacle heights (ADA) | 15" min, 48" max | ADA 308 ✓ |
| Typical wire | 14 AWG/15A, 12 AWG/20A, 10 AWG/30A | NEC 240.4(D) ⚠ |

### 5.8 Plumbing (IPC 2021) ⚠ all
| Item | Value |
|---|---|
| WC clearance | 15" min centerline to wall; 21" in front (IPC 405.3.1) |
| Lavatory | 15" centerline to wall; 30" c-c; 21" in front |
| Shower | 30x30 min (900 sq in) |
| Drain slope | 1/4" per ft (≤ 2-1/2" pipe), 1/8" per ft (≥ 3") — IPC 704.1 |
| Fixtures — business (Table 403.1) | WC 1/25 first 50, 1/50 after; lav 1/40 first 80, 1/80 after; drinking fountain 1/100; service sink 1 |
| Fixtures — dwelling | 1 kitchen sink, 1 lav, 1 tub/shower, 1 WC, laundry hookup |
| Water use | WC 1.6 gpf max (federal); 1.28 gpf WaterSense |
| Separate facilities | by sex when occupant load > 15 (IPC 403.2 exceptions allow single-user) ⚠ |

### 5.9 Mechanical / ventilation ⚠ all
| Item | Value |
|---|---|
| Outdoor air (ASHRAE 62.1 / IMC 403) | Office: 5 cfm/person + 0.06 cfm/ft²; Retail: 7.5 + 0.12; Classroom (9+): 10 + 0.12; Restaurant dining: 7.5 + 0.18 |
| Bath exhaust (res) | 50 cfm intermittent / 20 cfm continuous (IRC R303.3) |
| Dryer duct | 4" dia.; 35 ft max length minus fitting equiv. (IMC 504.8) |
| Kitchen hood | Type I for grease; per IMC 507 |
| Return air | Not permitted from bathrooms/kitchens |

### 5.10 Structural live loads (ASCE 7-16 Table 4.3-1 / IBC Table 1607.1) ⚠ all
| Occupancy | psf | kPa |
|---|---|---|
| Residential (one/two-family) living | 40 | 1.92 |
| Sleeping rooms | 30 | 1.44 |
| Office | 50 (+ 15 partition) | 2.40 |
| Lobbies & first-floor corridors | 100 | 4.79 |
| Corridors above first floor (office) | 80 | 3.83 |
| Assembly movable seating | 100 | 4.79 |
| Assembly fixed seating | 60 | 2.87 |
| Classrooms | 40 | 1.92 |
| Retail 1st floor / upper | 100 / 75 | 4.79 / 3.59 |
| Stairs & exits | 100 (40 for 1-/2-family) | 4.79 |
| Balconies / decks | 1.5 × area served (max 100) | |
| Garages (passenger cars) | 40 | 1.92 |
| Storage light / heavy | 125 / 250 | 5.99 / 11.97 |
| Roof (ordinary flat) | 20 | 0.96 |
Wind (ASCE 7 ch.26–30), snow (ch.7), seismic (ch.11–12) from ASCE Hazard Tool by site — never guess; show design criteria on S-001. Materials: ACI 318-19, AISC 360-16/-22, NDS 2018/2024, TMS 402-16 ⚠.

---
## 6. Permit / approval drawing set

**Typical commercial set order (NCS discipline order):**
1. **G-000 Cover** — project name/address, sheet index, vicinity map, team contacts, applicable code list (edition!), project data (zoning, lot area, FAR, building area, stories, height).
2. **G-001 Code analysis** — occupancy classification (IBC ch.3), construction type (ch.6), height/area (ch.5), sprinklers (903), fire-resistance schedule (Table 601/602), occupant load by space, egress width/count, travel distance, plumbing count, accessibility notes.
3. **G-002 Life safety plan** — egress paths, exits, distances, rated walls, occupant loads, exit signs.
4. **C-xxx Civil** — grading, utilities, drainage, erosion control; **L-xxx Landscape**.
5. **A-001 Site plan** — setbacks, property lines, easements, building footprint, parking count/ADA stalls, fire lanes, hydrant, accessible route to public way, utilities.
6. **A-1xx Floor plans** (demolition, new), RCPs, roof plan, enlarged plans (toilets, stairs).
7. **A-2xx Elevations**, **A-3xx Sections**, **A-4xx Enlarged**, **A-5xx Details**, **A-6xx Schedules** (door/window/room finish, hardware).
8. **S-xxx Structural** — general notes & design criteria (loads, wind/seismic, soil), foundation plan, framing plans, typical details, special inspection schedule.
9. **M-xxx** — plans, schedules (equipment, diffusers), energy compliance (IECC/COMcheck).
10. **P-xxx** — plans, risers, fixture & equipment schedules, isometric, gas.
11. **E-xxx** — site, lighting, power, panel schedules, one-line, grounding, energy forms.
12. **F-xxx** Fire protection — typically *deferred submittal* with its own shop drawings (NFPA 13/72), list on cover.
**Residential (IRC) set:** plot/site plan; foundation plan; floor plans with dimensions; roof plan/framing; elevations; sections; typical details (wall, stair, guard); structural/ wind bracing (R602.10); window/door schedule with egress & safety glazing; energy compliance (REScheck/prescriptive); MEP layout (often by trade).
**Required on every sheet:** sheet number/title, date, revision, scale, seal block (for jurisdictions requiring), north arrow on plans. Include **Texas:** RA/PE seal, TDLR TAS registration number (EBPL) and TAS notes where applicable ⚠ verify.

---
## 7. Common rejection reasons / mistakes

1. Wrong or unlisted **code edition** (must state IBC/IRC/NEC edition adopted by that city).
2. No **code analysis** or wrong occupancy/construction type; height & area exceeded; mixed-use separation not shown.
3. **Egress**: travel distance over Table 1017.2; dead end > limit; exits not separated; door swing wrong; panic hardware missing; width not calculated by 0.3"/0.2" factors.
4. **Stair**: riser > 7" (7-3/4" res), tread < 11"/10", missing handrail extensions, headroom < 6'-8"/80", guard < 42"/36", openings > 4".
5. **Accessibility**: no 18" latch-side clearance, 60" turning circles missing, ramp > 1:12, missing accessible route to public way, grab bars/toilet clearances, reach heights, parking signage, TAS items in Texas.
6. **Rated assemblies not identified** (UL/GA number), penetrations/draftstopping, door ratings, smoke damper locations.
7. Missing **structural design criteria** (loads, soils report, deflection), special inspection schedule (IBC ch.17), anchorage/connection details, drawings not matching calculations.
8. **Energy compliance** forms missing (COMcheck/REScheck), window U/SHGC not stated, insulation R-values missing.
9. **Unsealed or unsigned** drawings; wrong seal type; no license number.
10. **Zoning**: setbacks not dimensioned, lot coverage/impervious cover/FAR omitted, parking count short, landscaping.
11. **Inconsistencies**: plan vs. section vs. schedule (door numbers, wall types), missing sheets from index, scale errors.
12. **MEP**: no load calcs, panel schedule mismatch, ventilation rates, plumbing fixture count short, GFCI/AFCI omissions, equipment clearances (NEC 110.26).
13. Sprinkler/fire alarm designed by architect but required as deferred submittal not listed; knox box, fire lane, FDC location.
14. Revision clouds/delta not provided on resubmittals; comment-response letter missing.
15. Mixing **metric dimensions** or inches/feet incorrectly (e.g., `6'` vs `6"`, missing `0'-`).

---
## 8. Sources (URLs)

- ADA 2010 Standards — https://www.access-board.gov/ada/ ✓ (Chapters 3–6 verified)
- US National CAD Standard — https://www.nationalcadstandard.org/ncs6/ (landing page ✓; contents licensed)
- ICC code viewer — https://codes.iccsafe.org/ (IBC/IRC; page returned 403 to fetch; numbers cited from secondary sources)
- IRC stair values (secondary) — City handouts e.g. https://www.cityofboise.org/media/14405/437-treads-risers_march-2022.pdf ; https://www.whitebearlakemn.gov/media/35136
- IBC stair/egress discussion (secondary) — https://www.thebuildingcodeforum.com/ ; https://idighardware.com/wp-content/uploads/2021/08/2021-IBC-Opening-Force-and-Operable-Force.pdf
- ICC Texas adoption — https://www.iccsafe.org/advocacy/adoption-map/texas/ ; https://www.iccsafe.org/about/periodicals-and-newsroom/texas-strengthens-building-safety-and-resilience-by-adopting-2024-international-codes/
- TDLR — https://www.tdlr.texas.gov/ihb/codes.htm ; TAS: https://www.tdlr.texas.gov/ab/abtas.htm ⚠ (URL not fetched)
- NFPA 70 / 13 / 72 / 101 — https://www.nfpa.org/codes-and-standards
- ASCE 7 Hazard Tool — https://ascehazardtool.org/
- IAPMO UPC — https://www.iapmo.org/
- DOE energy codes — https://www.energycodes.gov/
