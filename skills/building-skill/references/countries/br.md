# Brazil (Brasil) — Drafting & Code Reference

Legend: **[Bn]** = value read this session from the source in §8. **⚠ verify** = drafter practice, memory, or a secondary/teaching source. Important: **ABNT NBR standards are paywalled** — I could not read their text. Numbers attributed to NBRs below come from secondary sources (university notes, public-agency checklists, a state fire-brigade norm that restates them) and are flagged. Brazil has **no national building code**: the controlling document is the **municipal Código de Obras** (+ zoning law) and the **state Corpo de Bombeiros** fire norms; NBRs are binding through reference by those and by consumer/professional law.

## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | **Metric**. Plans: dimensions in **metres with 2 decimals** (`3,00`), small details in cm; decimal **comma** (`2,50 m`) in Portuguese text; levels `±0,00` / `+0,15` ⚠ practice |
| Standard for architectural drawings | **ABNT NBR 6492** (2021 edition) — documentation for architecture/urbanism projects; text not readable here, requirements below are practice ⚠ [B1] |
| Related drafting norms | NBR 16752 (drawing sheets/format, 2020), NBR 8196 (scales), NBR 8403 (line types), NBR 10067 (orthographic projection), NBR 10126 (dimensioning), NBR 10582 (title-block area) ⚠ verify numbers and years |
| Sheet sizes | ISO A series A0–A4 (A1 = 594x841 mm common for approvals) ⚠ practice |
| Scales | Site plan (implantação) 1:200–1:500; plantas 1:50 (1:75 / 1:100 for large buildings); fachadas, cortes 1:50 / 1:100; details 1:20, 1:10, 1:5, 1:2, 1:1 ⚠ practice. NBR 6492 lists preferred scales; one teaching source quotes 1:20, 1:25, 1:50, 1:75 and 1:150 but with an obvious typo, so ⚠ verify [B1] |
| Title block (legenda / carimbo) | Project name (empreendimento), address + **inscrição imobiliária/cadastro**, owner, **autor do projeto and responsável técnico with CREA/CAU number and ART/RRT number**, sheet content, scale, date, revision, drawing no. "2/8" ⚠ practice |
| Responsibility documents | **ART** (CREA, engineers/architects) or **RRT** (CAU, architects) attached to every project/works — standard in all municipalities ⚠ verify per municipality |
| Language | Portuguese. Vocabulary: planta baixa, corte, fachada, cobertura, implantação, área construída, taxa de ocupação (TO), coeficiente de aproveitamento (CA), taxa de permeabilidade (TP), recuo, afastamento, pé-direito, vão, esquadria, laje, viga, pilar, sapata, baldrame |
| Date | DD/MM/AAAA ⚠ |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

- No mandatory national layer standard. Offices use their own names in Portuguese (PAREDE, PORTA, JANELA, COTA, EIXO, TEXTO, MOBILIÁRIO, HACHURA, ESTRUTURA) or AIA/ISO-style names ⚠ practice. Some public clients (federal agencies, state works) issue their own CAD standards ⚠ verify.
- File naming: `PROJ-NNN_ARQ_PLT-01_PlantaBaixa_R01.dwg` ⚠ practice. Discipline codes: ARQ, EST, HID (hidrossanitário), ELE, PCI (prevenção contra incêndio), TER (terraplenagem) ⚠ practice.
- E-submission: large cities use electronic licensing (São Paulo's COE decree regulates digital licensing ⚠ [B2]); PDF plus DWG upload and electronic signature (ICP-Brasil certificate) are frequent ⚠ verify per city. Smaller municipalities still require paper plus PDF ⚠.
- The fire brigade has its own system (e.g. **SP: Via Fácil Bombeiros**; RS: PPCI via CBMRS portal) ⚠ verify.

## 3. Drafting conventions

- Plans show room name + net area (m²) and floor level; walls with thickness (14 cm 1/2 vez, 19–20 cm 1 vez are typical masonry) ⚠ practice; doors/windows tagged P1/J1 with a schedule (quadro de esquadrias) giving width x height x peitoril ⚠ practice.
- **Quadro de áreas** (area table): terreno, área construída por pavimento, área computável, TO, CA, TP — read by plan checkers against zoning ⚠ practice [B2: building area, recuo, TO, CA are checked].
- Site plan shows terrain dimensions, setbacks (recuos), road width, trees, calçada, sidewalk accessible path ⚠ practice.
- Accessibility per **NBR 9050** (current edition 2020, with 2021 amendment) — show clear manoeuvring circles, accessible toilet, ramps ⚠ verify.
- Fire: show saídas de emergência, escadas, hydrants, extintores symbols per state IT/NPT [B3].
- Structural: concrete per **NBR 6118** (2023 edition ⚠ verify), loads NBR 6120, wind NBR 6123, seismic NBR 15421 (very low hazard in most of Brazil) ⚠ verify editions.
- Energy/performance: NBR 15575 (residential performance) — designer demonstrates thermal/acoustic/durability for housing ⚠ verify [B4].

## 4. Governing codes & authorities (table)

| Instrument | Governs | Status |
|---|---|---|
| **Código de Obras e Edificações** of each município (São Paulo: Lei 16.642/2017 + Decreto 57.776/2017) | Permits, edification rules, procedures | Municipal; SP read this session [B2] |
| Lei de Zoneamento / Plano Diretor (SP: PDE and LPUOS) | Setbacks, TO, CA, height, parking | Municipal [B2] |
| **NBR 6492** | Architectural drawing documents | 2021 edition ⚠ verify |
| **NBR 9050** | Accessibility | 2020 edition ⚠ verify |
| **NBR 6118** | Reinforced concrete design | 2023 edition ⚠ verify |
| **NBR 5410** | Low-voltage electrical installations | 2004 text (corrected 2008) ⚠ verify any newer revision |
| **NBR 15575** | Residential building performance | 2021 edition (parts 1–6) ⚠ verify |
| **NBR 14039, 5419, 13570** | MV installations; lightning protection; assembly places | ⚠ verify |
| State **Corpo de Bombeiros** IT (SP) / NPT (PR) / NT (GO, etc.) | Fire safety, AVCB/CLCB | State-by-state; SP IT-11 and Paraná NPT 011 v7 (Jan 2024, in force 6 Mar 2024) [B3] |
| CREA / CAU | Professional registration, ART / RRT | Federal conselhos ⚠ |
| Concessionária de energia (e.g. Enel, CPFL), water utility | Service connection, standards | Utility-specific ⚠ |

## 5. Key numbers

### 5.1 Planning (municipal)
| Item | Value |
|---|---|
| Setbacks / TO / CA / TP / height | Set by the zoning law of each city; no national value ⚠ verify at the municipality |
| São Paulo internal light-court (área livre descoberta interna) for building height H ≤ 10 m | Area ≥ **5.00 m²** and width ≥ **1.50 m**; for H > 10 m a rectangle of sides 2A x 3A (A = formula in code) (COE SP, Anexo item 5.3.1) [B2] |
| Vehicle ramp setback in SP | Ramp starts at least **4.00 m** back from the street alignment (COE SP Anexo item 8.3) [B2] |
| SP code removal of prescriptive room sizes | Teaching source says the 2017 code removed many fixed room dimensions that existed in the 1992 code; prior 1992 values (e.g. 2.50 m ceilings) are historic ⚠ verify against Decreto 57.776 |

### 5.2 Stairs & guards — state fire-norm values (Paraná NPT 011 v7, Jan 2024), consistent with SP IT-11 practice [B3]
| Item | Value |
|---|---|
| Riser (altura h) | **16–18 cm** (tolerance 0.5 cm); same height inside a flight; flights may differ ≤ 5 mm |
| Tread (largura b) | Blondel: **63 ≤ 2h + b ≤ 64 cm** |
| Nosing | Overhang ≤ 1.5 cm |
| Minimum exit width | **1.20 m** (stairs, ramps, accesses in general); passage unit (unidade de passagem) = **0.55 m** |
| Exit door clear width | ≥ **0.80 m** (counts as 1 UP) |
| Guard height | **1.05 m** min; may be 0.92 m on internal stairs with well ≤ 0.15 m |
| Handrails | Double handrail at **0.92 m and 0.70 m** (also used for NBR 9050 accessible routes) |
| Landing | Flight min 3 steps; ramp landings ≥ 1.20 m long |
Residential Brazilian practice (not code): riser 17–18 cm, tread 27–30 cm, width 0.90–1.00 m ⚠ practice.

### 5.3 Accessibility (NBR 9050 values as reported by AGU/exam sources; ⚠ verify against the norm) [B5]
| Item | Value |
|---|---|
| Ramp slope | max **8.33 % (1:12)** for rise up to 0.80 m per segment |
| Ramp width | recommended 1.50 m; minimum 1.20 m (0.90 m with ≤ 4.00 m segments only in existing buildings, reported) |
| Handrail on ramps | Double, continuous, 0.70 m and 0.92 m; intermediate rail if ramp ≥ 2.40 m wide |

### 5.4 Electrical (NBR 5410, 2004 text — university teaching sources) [B6]
| Item | Value |
|---|---|
| TUG (general sockets) in living room/bedroom | At least 1 per **5 m** (or fraction) of perimeter, evenly spread |
| Kitchen, pantry | At least 1 per **3.5 m** of perimeter, and at least one above each worktop ≥ 0.30 m wide |
| Other rooms | 1 point if ≤ 2.25 m²; 1 if 2.25–6 m²; above 6 m² 1 per 5 m perimeter |
| Lighting minimum load | 100 VA for rooms ≤ 6 m², +60 VA per whole 4 m² above 6 m² |
| Power per TUG | 600 VA per point in bathrooms, kitchens, services; 100 VA otherwise ⚠ verify (secondary source) |

### 5.5 Fire basics
- Required exit widths from unidade de passagem 0.55 m; width = number of UP x 0.55 [B3]. Pressurized/protected stair requirements by height and occupancy are in the state IT/NPT tables ⚠ verify per state. Max travel distances are in IT-11/NPT 011 Tables 2 and 2A (not transcribed) ⚠ verify. **AVCB** (Auto de Vistoria do Corpo de Bombeiros) or CLCB (small buildings) is needed before habite-se ⚠ verify.

### 5.6 Structure / performance
- Design working life (VUP): primary structure ≥ **50 years** (NBR 15575; 63 intermediate, 75 superior levels in the 2013 edition), per secondary sources ⚠ verify against 2021 edition [B4]. Seismicity is low; wind governs most designs ⚠ verify.

## 6. Permit drawing set

Typical municipal approval (alvará de aprovação e execução) ⚠ practice: requerimento + título de propriedade/matrícula + IPTU · ART/RRT of project and execution · implantação (site plan, with levels and recuos) · plantas baixas de todos os pavimentos + cobertura · cortes (min. 2, including stair) · fachadas · quadro de áreas · memorial descritivo / quadro de esquadrias ⚠ · structural projects are not usually filed for houses but ART is ⚠ · fire plan (PPCI/PSCIP) submitted to the state bombeiros · habite-se on completion ("as-built") ⚠. Large city example: SP COE allows digital licensing and requires reports above 750 m² / 1,500 m² thresholds (see COE Anexo items 3.7–3.8) [B2] ⚠ verify what they require.

## 7. Common rejection reasons

- Area table inconsistent with zoning (TO/CA/TP exceeded, recuos missing) ⚠ practice [B2].
- Missing ART/RRT or professional registry no. in title block ⚠ practice.
- Stair geometry outside 16–18 cm riser or 63–64 cm Blondel in fire-regulated buildings [B3].
- Exit widths below 1.20 m / door clear < 0.80 m [B3].
- Accessibility not drawn (ramp slopes, accessible WC, rampa de acesso) ⚠ [B5].
- Fire plan (PPCI) not approved; AVCB missing before habite-se ⚠ practice.
- Light court / ventilation openings not dimensioned [B2 item 5.3.1].
- Drawings not at standard scale or not legible when printed ⚠ practice.

## 8. Sources

- [B1] NBR 6492 mentioned in teaching material: `https://www.arquitetura-urbanismo.timoteo.cefetmg.br/wp-content/uploads/sites/332/2023/09/DTA_Plano-de-Ensino_V2023.pdf` (norm text itself not read).
- [B2] São Paulo Lei 16.642/2017 (Código de Obras e Edificações) full text: `https://www.saopaulo.sp.leg.br/iah/fulltext/leis/L16642.pdf`; Decreto 57.776/2017 listed at `https://prefeitura.sp.gov.br/web/licenciamento/w/legislacao/3258`
- [B3] Paraná CBMPR NPT 011 Saídas de Emergência v7 (Jan 2024): `https://www.bombeiros.pr.gov.br/sites/bombeiros/arquivos_restritos/files/documento/2024-03/npt-011-saidas_de_emergencia_versao_jan_2024.pdf` (state norm modelled on SP IT-11; São Paulo IT-11 text not read).
- [B4] NBR 15575 VUP summary: `https://institutodeengenharia.org.br/site/wp-content/uploads/2019/05/Apresentação-Carlos-Del-Mar.pdf` (2013 edition basis).
- [B5] AGU accessibility audit checklist citing NBR 9050: `https://www.gov.br/agu/pt-br/acesso-a-informacao/acoeseprogramas/acessbilidade-nas-edificacoes-da-agu/rj-laudo-petropolis-psf-pdf.pdf`
- [B6] NBR 5410 residential socket rules (USP course material): `https://edisciplinas.usp.br/mod/resource/view.php?id=3048637`
