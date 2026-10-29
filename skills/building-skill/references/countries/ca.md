# Canada (Canada / Canada français) — Drafting & Code Reference

Legend: **[Cn]** = value read this session from the source listed in §8. **⚠ verify** = drafter practice, memory, or a source that is older/secondary than the edition in force. Canada has no single building law: the **National Building Code of Canada 2020 (NBC, Code national du bâtiment — CNB)** is a model code; each province/territory adopts it with amendments, so the **provincial code governs** and a municipality adds zoning, permits and local rules.

Key trap: the numbers below for Part 9 (houses, small buildings) were read from the **BC Building Code 2018** (based on NBC 2015/2018 text). NBC 2020 / BCBC 2024 / OBC 2024 are believed unchanged for these items, but every number carries "⚠ verify vs adopted edition" unless noted.

## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Code is **metric (SI)**; plans in **mm** (structural/commercial) or **m with 2–3 decimals** (site/survey) [C1]. Residential trades still think **imperial**: 2x4/2x6 nominal lumber, 16 in. / 24 in. o.c., 4x8 ft sheets, 24x36 in. sheets, feet-inches on many house plans ⚠ practice. Provincial permit forms accept either but the code check is metric. Dual-dim (mm + ft-in) is common on house plans ⚠ practice |
| Sheet sizes | ISO A1/A0 on public/institutional work; **ARCH D 24x36 in.** or ANSI B 11x17 on houses (Ontario/West) ⚠ practice. Municipalities increasingly take PDF to a fixed paper size via e-permit portal ⚠ verify per city |
| Scales (metric) | Site 1:200–1:500 (survey 1:250/1:500); plans 1:50 or 1:100; elevations 1:50/1:100; sections 1:20–1:50; details 1:1–1:10. Imperial houses: 1/4"=1'-0" (≈1:48) plans, 1/8" site ⚠ practice |
| Title block | Project, civic + legal address (lot/plan/concession), owner, designer name + **registration no.** (Ontario BCIN, architect OAA/AAA/OAQ stamp, engineer P.Eng. seal), sheet no./title, scale, date, revision log, "Do not scale" note ⚠ practice |
| Language | English; **French mandatory in Québec** (Charter of the French language) and common on federal/NB work. Drawings for Québec: titles, notes, legends in French (cuisine, chambre, salle de bain) ⚠ verify OIQ/OAQ practice |
| Levels / datum | Geodetic elevations on site plan (m, 2 decimals); floor levels as +0.000 or geodetic ⚠ practice |
| Date format | ISO YYYY-MM-DD is the federal standard; DD/MM/YYYY or "Oct 28, 2026" seen in practice ⚠ |
| Professional seals | Part 3 / large buildings: architect + engineers (provincial acts). Small houses: Ontario "designer" with **BCIN**, other provinces owner-drawn plans often allowed for Part 9 ⚠ verify per province |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

- No national mandatory layer standard. Commonly used: **AIA CAD Layer Guidelines / US National CAD Standard layer names** (A-WALL, A-DOOR, A-GLAZ, A-ANNO-TEXT…), firm standards, or client standards ⚠ practice. Some federal and provincial owners publish their own CAD standards (PSPC, Alberta Infrastructure, BC Buildings) ⚠ verify.
- File names: `ProjectNo_Discipline_SheetNo_Title_Rev` (e.g. `2026-014_A_A101_FloorPlan_RevB.dwg`) ⚠ practice. Discipline letters: A arch, S struct, M mech, E elec, P plumbing, C civil, L landscape, F fire protection ⚠ practice.
- **E-submission**: most large cities run online permit portals taking PDF sets (e.g. Toronto, Vancouver, Calgary, Ottawa); stamped/signed PDF with digital seal accepted by many engineering/architect bodies. Exact file-size, flattening, naming rules are city-specific ⚠ verify each portal. DWG is generally not accepted as the submission, only as a coordination file.
- BC: designers submit **Letters of Assurance** (Schedules B, C-A/C-B etc.) with the application — a coordinated professional-assurance system for Part 3 buildings ⚠ verify schedule names.

## 3. Drafting conventions

- Doors: swing arcs shown on plans; door/window tags keyed to schedules; window schedules show **rough opening**, glazing type, egress yes/no, safety-glass note ⚠ practice.
- Walls: poché or hatch by assembly; tag wall types to a wall-type legend with **fire-resistance rating (FRR, h/min)** and STC where relevant ⚠ practice. Show fire separations as heavy dashed lines with rating callout [C1: Part 9.10].
- Section/elevation markers use circle-with-sheet-ref (US/NCS style) ⚠ practice. Notes in sentence case, 2.5–3.5 mm plot height.
- Show **radon rough-in** (sub-slab pipe & sump location) in BC 2024 and other provinces adopting NBC 2020 Part 9 radon rough-in rule — BC requires radon subfloor depressurization rough-in [C2]; other provinces ⚠ verify.
- Energy: show envelope assembly R-values/RSI and ventilation notes per code compliance path (NBC Section 9.36 / National Energy Code for Buildings 2020 for Part 3; or provincial path such as Ontario SB-12 / BC Step Code) ⚠ verify. RSI vs R conversion: R ÷ 5.678 = RSI.
- Structural design: snow, wind and seismic loads from NBC Part 4 climatic tables by municipality; state design snow/wind/seismic values on structural drawings ⚠ practice.
- Accessibility: barrier-free path, washroom, ramp slopes per NBC 3.8 for Part 3 buildings; Ontario also has an OBC barrier-free section ⚠ verify.

## 4. Governing codes & authorities (table)

| Instrument | What it governs | Edition / status |
|---|---|---|
| **NBC 2020** (Code national du bâtiment – Canada 2020) | Model building code; Div A/B/C; Part 9 = housing & small buildings; Part 3 = large/complex | Published by NRC 28 Mar 2022; not law until adopted [C7] |
| National Fire Code 2020 (NFC) | Fire safety in operation/maintenance, hazardous materials, existing buildings | 2020 model code, adopted provincially [C7] ⚠ verify provincial editions |
| National Plumbing Code 2020; National Energy Code of Canada for Buildings 2020 (NECB) | Plumbing; Part 3 energy | 2020 model codes [C7] |
| **BC Building Code 2024** (Book I General, Book II Plumbing) | BC except City of Vancouver (own Vancouver Building By-law) | In force 8 Mar 2024, for permit applications on/after; earthquake and adaptable-dwelling parts apply from 10 Mar 2025 (in-stream extension to 8 Mar 2027 by Ministerial Order) [C2] |
| **Ontario Building Code 2024 (O. Reg. 163/24)** | Ontario; adopts NBC 2020 + Ontario amendments | In force 1 Jan 2025; old 2012 code (O. Reg. 332/12) continues only for permits/applications under the transition rule [C3] |
| **Alberta**: National Building Code – 2023 Alberta Edition (NBC(AE)) | Alberta | Based on NBC 2020; in force 1 May 2024 [C4] |
| **Québec**: Code de construction du Québec, Chapitre I – Bâtiment (CNB 2020 modifié); RBQ | Québec | Update based on CNB 2020 in rulemaking from 2023 [C9]; ⚠ verify the date in force |
| Other provinces/territories (MB, SK, NS, NB, NL, PEI, YT, NT, NU) | Adopt NBC with amendments | ⚠ verify edition per province |
| **CSA C22.1 — Canadian Electrical Code Part I (CEC)**, 26th ed. **C22.1:24** | Electrical installations; enforced by provincial electrical authority (ESA Ontario, Technical Safety BC, SAFE/Alberta, etc.) | 26th edition (2024) [C6, C10]; adoption date varies by province ⚠ verify |
| **CSA A23.3** Design of concrete structures; **CSA A23.1** concrete materials; CSA O86 wood; CSA S16 steel | Referenced by NBC Part 4 | A23.3:24 and S16:24 exist; **NBC 2020 references the earlier editions (A23.3:19, S16:19)** ⚠ verify which the adopting province references [C11] |
| Municipal zoning by-law + permit office | Setbacks, lot coverage, height, parking, trees | Municipal; always check ⚠ |
| Local fire dept / Fire Marshal | Fire access, fire alarm review (Part 3), operating permits | Provincial |

## 5. Key numbers

### 5.1 Planning (municipal — no national value)
| Item | Value |
|---|---|
| Setbacks, lot coverage, FAR, height, parking | **Set only by municipal zoning by-law**, vary by zone (R1, RS-1, etc.); read the zoning table and survey. No country-wide value exists ⚠ verify per municipality |
| Secondary suite size/ceiling | Ontario 2024: reduced ceiling 1.95 m, 1.85 m under beams/ducts, for secondary suites only (Sent. 9.5.3.1.(2),(3)) [C5] |

### 5.2 Stairs, guards (private stairs serving one dwelling) — BCBC 2018 Section 9.8 [C1]
| Item | Value |
|---|---|
| Rise | max 200 mm / min 125 mm (Table 9.8.4.1) |
| Run (rectangular tread) | max 355 mm / min 255 mm (Table 9.8.4.2) |
| Stair width, exit stair serving one dwelling | ≥ 860 mm (9.8.2.1.(2)) |
| Headroom | ≥ 1 950 mm over stairs and landings in a single dwelling (9.8.2.2.(3)) |
| Handrail height | 865 to 1 070 mm above nosing line (9.8.7.4.(2)); NBC 2020 value ⚠ verify |
| Guard height in dwelling unit; exterior guard ≤1 800 mm above grade serving one unit; guards on steps | 900 mm min (9.8.8.3.(2)–(4)); all other guards 1 070 mm min |
| Note | Public (non-dwelling) stairs: rise max 180 / min 125 mm (Table 9.8.4.1) |

### 5.3 Rooms, doors, hallways [C1 Section 9.5]
| Item | Value |
|---|---|
| Ceiling height (Table 9.5.3.1) | **2.1 m** min over the lesser of the room area or: living 10.0 m², dining 5.2 m², kitchen 3.2 m², primary bedroom 4.9 m², other bedroom 3.5 m²; unfinished basement 2.0 m clear (below beams and on passage routes) |
| Minimum room floor areas | 2018 BCBC Part 9 gives none in 9.5.1; Ontario/other provincial amendments may differ ⚠ verify |
| Door sizes, Table 9.5.5.1 | Dwelling entrance, entrance hall/vestibule, stairs to a finished floor, doors on a line from outside to basement: **810 x 1 980 mm**; bath/WC, walk-in closet, utility: **610 x 1 980 mm**; other rooms/exterior balcony: 760 mm wide (min) x 1 980 mm |
| Hallway width in dwelling | ≥ 860 mm; 710 mm permitted if only bedrooms and baths lie beyond and a second exit is provided (9.5.4.1) |
| Combination rooms | Opening between areas ≥ 3 m² or 40 % of the dependent area wall, whichever larger (9.5.1.2) |

### 5.4 Fire / egress / alarms [C1]
| Item | Value |
|---|---|
| Egress window from sleeping room | Unobstructed opening ≥ **0.35 m²** with no dimension < **380 mm**; clearance ≥ 760 mm in front of a window well (9.9.10.1.(2),(3)) |
| Smoke alarms | At least one on every storey including basements; in each sleeping room and in the hallway/between bedrooms and rest of storey (9.10.19.4.(1)) |
| CO alarms | Required by Section 9.32 where fuel-burning appliance or attached garage; location rules in 9.32.4 ⚠ verify |
| Door in means of egress | Single active leaf ≥ 810 mm wide, two-leaf ≥ 610 mm each (Part 9.9 exit-door text; applies to non-dwelling egress, confirm) ⚠ verify |

### 5.5 Electrical (CEC Rule 26-722) [C6]
| Item | Value |
|---|---|
| Habitable-room receptacles | Duplex receptacle so no point along the floor line of usable wall space is > 1.8 m horizontally from one; wall space counts only if ≥ 900 mm wide; excludes bathrooms, hallways, laundry etc. Source is NB regulation restating CEC; ⚠ verify against C22.1:24 and the provincial amendments |
| Edition | 26th edition = C22.1:24 [C10] |

### 5.6 Structure / seismic
- Loads from NBC Part 4 plus provincial tables; climatic design data (snow, wind, rain) are **by municipality** in Appendix C ⚠ verify. Seismic design values changed in NBC 2020 (updated hazard model), so use the 2020 tables, not 2015 ones ⚠ verify. Part 9 prescriptive framing (joist, rafter spans, bracing) is in Section 9.23 ⚠ verify.

## 6. Permit drawing set

Typical for a house (Ontario/BC/Alberta) ⚠ practice: application form + professional/designer declaration (Ontario Schedule 1 w/ BCIN; BC Letters of Assurance) · site plan from survey with setbacks and grades · foundation + floor plans · roof plan · all elevations · two building sections · wall-section detail with assembly and RSI values · structural framing plans (stamped for engineered items) · energy compliance (Ontario SB-12 / BC Step Code / NBC 9.36) · HVAC/ventilation design · plumbing fixture layout · electrical layout where required · grading/drainage plan (Ontario Lot Grading) · truss/I-joist layouts · geotechnical report where required. Large buildings add fire protection/life safety report, accessibility report, mechanical/electrical engineered sets ⚠ verify per jurisdiction.

## 7. Common rejection reasons

- Zoning non-compliance (setbacks, coverage, height, parking) shown only on code table, not on survey-based site plan ⚠ practice.
- Missing professional seals/registration number, or wrong-edition code cited (for example citing OBC 2012 after the transition date) [C3].
- Egress window size missing, or window well clearance (760 mm) not shown [C1].
- Stair geometry: run < 255 mm or rise > 200 mm, headroom < 1 950 mm [C1].
- Ceiling height in basement/secondary suite not shown with beam/duct dimensions [C1, C5].
- No smoke/CO alarm locations; no radon rough-in (BC 2024) [C1, C2].
- Missing energy-compliance forms or insulation values ⚠ practice.
- Structural drawings without engineer stamp for beams/lintels/trusses ⚠ practice.
- Drawing set not matching the e-submission portal rules (naming, file size) ⚠ practice.

## 8. Sources

- [C1] BC Building Code 2018 Div B (free): Section 9.5 `https://free.bcpublications.ca/civix/document/id/public/bcbc2018/bcbc_2018dbp9s95`, 9.8 `…/bcbc_2018dbp9s98`, 9.9 `…/bcbc_2018dbp9s99`, 9.10 `…/bcbc_2018dbp9s910`, 9.32 `…/bcbc_2018dbp9s932`. Read as PDFs this session.
- [C2] BC Codes 2024 page: `https://www2.gov.bc.ca/gov/content/industry/construction-industry/building-codes-standards/bc-codes/2024-bc-codes`
- [C3] Ontario O. Reg. 163/24: `https://www.ontario.ca/laws/regulation/r24163` (search snippet confirms effective 1 Jan 2025 and transition).
- [C4] NRC page for NBC 2023 Alberta Edition: `https://nrc.canada.ca/en/certifications-evaluations-standards/codes-canada/codes-canada-publications/national-building-code-2023-alberta-edition`; Alberta `https://www.alberta.ca/building-codes-and-standards`
- [C5] OBOA bulletin on 2024 OBC ceiling heights: `https://bcas.oboa.on.ca/support/solutions/articles/70000679990-2024-obc-update-ceiling-height-allowances`
- [C6] New Brunswick Reg. 2026-5 (Rule 26-722 receptacles, C22.1-24): `https://laws.gnb.ca/en/document/ar/2026-5`
- [C7] NRC, new national model codes (28 Mar 2022): `https://nrc.canada.ca/en/certifications-evaluations-standards/codes-canada/new-latest-editions-national-model-codes-now-available`
- [C9] RBQ regulatory impact analysis (Chapitre I update): `https://www.rbq.gouv.qc.ca/fileadmin/medias/pdf/Publications/francais/analyse-impact-reglementaire-projet-reglement-mod-chapitre-I-code-construction.pdf`
- [C10] CSA Group, C22.1:24: `https://www.csagroup.org/store/product/CSA_C22.1%3A24_PACKAGE/`
- [C11] CSA A23.3 listing: `https://www.csagroup.org/store/product/CSA%20A23.3:19/`; Nimonik `https://www.standards.nimonik.com/products/csa/a23pt3/`
