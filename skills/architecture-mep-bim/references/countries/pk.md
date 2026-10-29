# Pakistan (پاکستان) — Drafting & Code Reference

Legend: **✓** = read this session on a web page (URL in §8). **⚠ verify** = memory/secondary/not opened. **Honest status:** official PDFs (LDA regulations, CDA, KB&TPR, Building Code of Pakistan documents) returned 404/500/garbled to the fetch tool, so this file has **few confirmed numbers**. Treat it as a map of *who decides what*; **pull the plot's own regulations** before drawing.

**Rule of thumb:** local development authorities set planning numbers per plot size — **LDA** (Lahore), **CDA** (Islamabad), **SBCA/KB&TPR** (Sindh/Karachi), **RDA, FDA, MDA, PDA** (Punjab cities), **KP/ BDA** (Peshawar/ Balochistan) — and *which* edition applies changes often. The national **Building Code of Pakistan (BCP)** is issued by PEC but its legal force after the 18th Amendment is **ambiguous and not uniformly adopted** ✓ (2016 academic paper).

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | **Mixed.** Metric allowed; practice is **feet-inches** on residential plans (e.g. 10'-6") and **sq ft / marla / kanal** for plots; Karachi uses **sq yards** (plot 120/240/400 sq yd) ⚠ |
| Marla / kanal | 1 marla = 272.25 sq ft (25.29 m²) in Punjab/Islamabad conventions; 1 kanal = 20 marla = 5,445 sq ft (≈ 506 m²) ⚠ — **Sindh/KP marla values differ** ⚠ |
| Language | English (permit drawings); Urdu only for client sketches |
| Sheets | A1 / A2 / A3 and **24×36 in** or 18×24 in on blueprint paper ⚠ |
| Scales | Site/plot plan 1/16" = 1' to 1/8" = 1' (≈ 1:192–1:96) or 1:100/1:200 metric; plans 1/8" = 1'; sections 1/4" = 1' ⚠ |
| Title block | Owner name & plot no./sector/phase/block, design consultant with **PEC (Pakistan Engineering Council) registration** and/or PCATP (architect) number, drawing title, scale, date ⚠ |
| Levels | Plinth/GL reference; road crown level used for height (LDA measures from road crown) ✓ see §5 |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

| Topic | Practice |
|---|---|
| Layer naming | None mandated; offices use English names (`WALL`, `DOOR`, `WINDOW`, `DIM`, `TEXT`, `COL`, `BEAM`). Skill default: AIA-style `A-WALL`, `A-DOOR` ⚠ |
| File naming | `Plot#-Block-Sector-Floor-Rev` ⚠ practice |
| Authority submission | Mostly **hard-copy printed sets** with stamps; **LDA e-Khidmat / e-Services**, **CDA e-Sahulat**, **SBCA online** portals exist with PDF uploads ⚠ verify current portal; DWG rarely required ⚠ |
| Verification | Physical site verification + sign-offs from sub-engineer/ architect of authority ⚠ |
| Drawing medium | PDF + signed physical copies; some authorities require **colour-coded** drawings (red = proposed, black = existing) ⚠ |

## 3. Drafting conventions

- **Dimensions** in feet-inches on residential plans (e.g. `12'-0" x 14'-0"`); metric on commercial/engineering.
- **Wall thickness**: 9" brick external, 4.5" partition (practice) ⚠ — masonry with RCC frame is the norm.
- **Plot plan** must show: plot dimensions and area (marla/kanal/sq yd), road width (ROW), setbacks (front/rear/side) with arrows, boundary wall & gate, covered-area calculation.
- **Section** shows plinth (1'-0" to 2'-0" above road crown ⚠), floor-to-floor, parapet height.
- **Rooms** labelled: Drawing Room (ڈرائنگ روم), Lounge / TV Lounge, Bedroom, Kitchen, Bath/Toilet, Store, Garage / Porch, Courtyard (صحن), Servant Quarter ⚠.
- **Notes** quoting the authority's regulation number, "all dimensions in feet unless noted" ⚠.
- **Structural**: separate RCC sheet with zone/seismic note and BCP-SP 2007 compliance ⚠.
- **Height datum**: LDA-type rules measure building height from the **road crown** to the parapet — show road crown RL on the section ✓ (LDA text via search).

## 4. Governing codes & authorities

| Item | Code / authority | Status |
|---|---|---|
| Seismic | **Building Code of Pakistan — Seismic Provisions 2007 (SP-2007)**, Ministry of Housing & Works; includes Zone 4 extra minimum base shear; zones 1–4 incl. 2A/2B | ✓ iisee index + study |
| Fire & life safety | **Building Code of Pakistan — Fire Safety Provisions 2016**, issued by Pakistan Engineering Council with NDMA; based on NFPA 1; notified 31 Oct 2016 as PEC construction bye-law (PEC Act 1975 s.25) | ✓ search summary |
| BCP-SP 2021 | revised seismic provisions rumoured / drafted ⚠ **not confirmed** — verify with PEC | ⚠ |
| Structural loads | UBC 97 / ASCE 7 equivalents referenced inside BCP-SP; ACI 318 for RC ⚠ | ⚠ |
| Lahore | **LDA Building & Zoning Regulations** (2019, amended; drafts 2021) | ⚠ |
| Islamabad | **CDA Building Control Regulations / Zoning Regulations 2020** | ⚠ |
| Karachi / Sindh | **Karachi Building & Town Planning Regulations 2002 (KB&TPR)**; **Sindh Building Control Ordinance 1979**; SBCA (Sindh Building Control Authority) | ✓ search summaries |
| KP / Punjab / Balochistan | PDA/ KPBCA; Punjab Land Use Rules; local development authorities ⚠ | ⚠ |
| Electrical | **IESCO/LESCO/K-Electric** service rules; Pakistan Electrical Code PEC ⚠; typical 220 V single-phase / 380–415 V three-phase, 50 Hz ⚠ | ⚠ |
| Energy | **Building Energy Code of Pakistan 2013** (PEC/NEECA) ⚠ | ⚠ |
| Planning law | Provincial Local Government Acts; **Master Plans** | ⚠ |

## 5. Key numbers

| Item | Value | Source |
|---|---|---|
| Seismic zones | Zones **1, 2A, 2B, 3, 4**; Peshawar is **Zone 2B = 0.16–0.24 g PGA (475-yr)** | ✓ study (BCP 2007) — other zone ranges **not confirmed ⚠** (typical: 2A 0.08–0.16, 3 0.24–0.32, 4 > 0.32 ⚠) |
| Base shear | equation set (a–d); (d) minimum applies **only in Zone 4** | ✓ iisee BCP-SP 2007 |
| Zone factor Z, importance I, R, Ca, Cv, Nv | in Tables 1–7 of BCP-SP 2007 | ✓ iisee index — values ⚠ |
| LDA height (non-apartment, road ROW ≤ 25 ft) | **≤ 38 ft (11.58 m)** from road crown to parapet | LDA doc via search ✓ ⚠ (older rule) |
| LDA amended height | plots < 1 kanal: **36 → 48 ft**; 1–2 kanal: **60 → 90 ft** (G+6) | Graana news ⚠ secondary |
| LDA 2021 draft | 20 ft building line for houses; side/rear 7 ft (2–4 kanal) or 10 ft (≥ 4 kanal); apartment plots 13 ft | draft ⚠ not final |
| Ground coverage / FAR | e.g. < 5 marla: coverage up to 80%, FAR up to 1:2.4, up to 3 storeys | Zameen blog ⚠ secondary |
| Karachi high-rise | 2017 Supreme Court-ordered ban beyond G+2, later relaxed; check current SBCA rule | Gulf Times ⚠ |
| Stairs | typical practice: tread 10"–11", riser 6"–7", width ≥ 3'-0" private, 4'-0" public ⚠ (verify in authority regs) | ⚠ |
| Min room sizes / heights | local (e.g. habitable room clear height 9'-0"–10'-0" ⚠) | ⚠ |
| Parking | per authority (e.g. 1 car per house; apartments by unit size) ⚠ | ⚠ |
| Egress/fire | occupancy-based per BCP Fire Safety 2016 (NFPA 1/101 principles): ≥ 2 exits for buildings above G+2/ > 15 m ⚠ | ⚠ |

## 6. Permit drawing set (typical, authority-specific)

1. Allotment / title documents, **NOC** (if required), fard/ registry, previous map ⚠
2. Site plan + floor plans + elevations + sections + roof plan, covered-area statement
3. Structural drawings & design report certified by **PEC-registered engineer**; soil report for > 3 storeys ⚠
4. Fire safety plan for high-rise/ commercial (per BCP Fire 2016) ⚠
5. Fees receipt; undertaking; electrical/ MEP for larger projects
6. Approval stamp → commencement; completion certificate / occupancy ⚠

## 7. Common rejection reasons

- Covered area / FAR / height over the plot-size table; setbacks not as per approved scheme or society bylaws (DHA, Bahria, etc.).
- Encroachment on road/ service lane; boundary wall/ gate swing outside plot.
- Missing structural certification, wrong seismic zone factor, or no soil report where required.
- Society/ scheme NOC missing (DHA, Bahria Town, Gulberg, Askari) or non-compliant with society architectural control.
- Approved dimensions in feet but area calculation in metric (unit mismatch).
- Basement/ mezzanine counted as non-covered incorrectly.

## 8. Sources

- Building Code of Pakistan (Seismic Provisions 2007) — IISEE index: https://iisee.kenken.go.jp/net/seismic_design_code/pakistan/pakistan.htm ✓ (tables not shown)
- BCP Fire Safety Provisions 2016 (PEC/NDMA): https://www.shehri.org/Building Code of Pakistan-Fire Safety Provisions-2016.pdf ⚠ (500 error; summary via search)
- Peshawar Zone 2B (BCP 2007) — study: https://jau.vgtu.lt/index.php/JCEM/article/view/15854 ⚠
- LDA building regulations (404s): https://lda.gop.pk/website/images/LDA_BR.pdf , https://lda.gop.pk/website/images/DRAFT_FINAL_BUILDING_REGULATIONS_22_06_2021.pdf ⚠
- Graana on LDA height amendments: https://www.graana.com/blog/lda-approves-bylaws-to-promote-high-rises-in-residential-areas/ ⚠
- Sindh Building Control Ordinance 1979: https://www.sindhlaws.gov.pk/Setup/Publications_SindhCode/PUB-15-000377.pdf ⚠
- Pakistan Accord standard (adopts both codes): https://internationalaccord.org/wp-content/uploads/2023/09/Pakistan-Accord-Building-Standard-Version-1-1.pdf ⚠
