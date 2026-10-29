# Mexico (México) — Drafting & Code Reference

Legend: **[Mn]** = value read this session from the source in §8. **⚠ verify** = drafter practice, memory, or secondary source. Mexico has **no single national building code**: each state/municipality has its own *reglamento de construcciones*. The best-documented one is **Ciudad de México (CDMX)** — its Reglamento de Construcciones (RCDF/RCCDMX) + **Normas Técnicas Complementarias (NTC)** are the de facto reference and are widely copied. Everything below is CDMX unless noted. For any other state (Jalisco, Nuevo León, Yucatán, Quintana Roo…) read the local reglamento ⚠ verify.

Edition caution: the architectural NTC numbers below come from the **2004 Gaceta text**; a Servicio de Información Jurídica notice points to an update published 12 Dec 2024 that I could not open [M5]. Treat all NTC numbers as ⚠ verify against the current Gaceta before issuing drawings. The Reglamento itself (text of 4 Oct 2024) mostly delegates dimensions to the NTC [M1].

## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | **Metric (SI)**; plans in **metres with 2 decimals** (`3.00`, `0.90`) for architecture; cotas in cm are common on structural/detail sheets; heights as `N.P.T.` (nivel de piso terminado) +0.00 ⚠ practice |
| Scales | Site plan (plano de localización / croquis) 1:200–1:500; plantas, fachadas, cortes 1:50 or 1:100; details 1:20–1:2; area plans 1:75 in house work ⚠ practice |
| Sheet sizes | Sheets 60x90 cm ("lámina 60x90") and 90x120 cm are traditional in Mexico; ISO A1/A0 or "doble carta/tabloide" for reduced sets ⚠ practice. Plataforma Digital accepts PDF uploads ⚠ verify limits |
| Title block (cuadro de datos / "cajetín") | Project name, owner (propietario), address (calle, colonia, alcaldía), **cuenta catastral**, **uso de suelo / Certificado Único de Zonificación (CUZUS)** no., DRO name + **registro DRO** and corresponsables, scale, date, sheet key (A-01, E-01, I-01), north arrow, "acotaciones en metros" note ⚠ practice |
| Language | Spanish; terms: planta baja (PB), planta alta, azotea, corte, fachada, cimentación, losa, trabe, castillo, cadena, firme |
| Dimension notes | State "las cotas rigen sobre el dibujo" and "verificar medidas en obra" ⚠ practice; show built areas (superficie construida) and open area (área libre) per level in a "cuadro de áreas" ⚠ practice |
| Signatures | Owner signature + DRO seal on each sheet, corresponsables on their discipline sheets ⚠ practice [M1: DRO and Corresponsables register the construction manifest] |

## 2. CAD layer/file naming practice + authority CAD/e-submission rules

- No mandatory layer standard. Offices use their own or AIA-style names translated to Spanish (MUROS, PUERTAS, VENTANAS, COTAS, EJES, TEXTO, MOBILIARIO, ESTRUCTURA, ELECTRICO, HIDROSANITARIO) ⚠ practice. Axes (ejes): letters on one direction, numbers on the other, bubbles at 1.20 m beyond outer face ⚠ practice.
- File name: `ClaveProyecto_Disciplina_Hoja_Rev` (e.g. `PRY-021_ARQ_A-02_PLANTA-BAJA_R1.dwg`) ⚠ practice.
- CDMX registers construction manifests and licences through a **Plataforma Digital** (online) — the 2024 Reglamento text says manifestation of construction is registered on it [M1]. Exact file formats, sizes, signatures (e-firma) are set by the platform ⚠ verify.
- Many states and municipalities still take paper plan sets (3–4 copies, bound, folded to carta size) plus PDF ⚠ practice.

## 3. Drafting conventions

- Fachadas show materials (aplanado, tabique, cantera…) and levels; sections show pretiles, losa (thickness), cimentación, firme; roof plan (planta de azotea) with slopes (pendientes), bajadas de agua pluvial (BAP), tinacos ⚠ practice.
- Show **project-controlled data** (shown on CDMX plans): zonificación, área libre %, niveles, altura, cajones de estacionamiento — all come from the local Programa de Desarrollo Urbano / SEDUVI zoning [M1 Art. 76] and appear in the data table.
- Windows: show area of vano vs room area to prove lighting/ventilation (see §5.3) [M2].
- Show accessibility: ramps, parking for people with disabilities, 1.20 m minimum clear path [M2 §2.3].
- Pluvial/water: cisterna, tinaco, bombeo; sanitary and rainwater separated ("red separada") ⚠ practice.
- Electrical: single-line diagram (diagrama unifilar), cuadro de cargas, símbolos per NOM-001-SEDE/CFE practice ⚠ practice.
- Structural: DRO/Corresponsable en Seguridad Estructural stamps; cimentación + estructura per NTC (concreto, mampostería, sismo) ⚠ verify.

## 4. Governing codes & authorities (table)

| Instrument | What it governs | Status |
|---|---|---|
| **Reglamento de Construcciones para la Ciudad de México** (RCDF) | Permits, DRO, classification, general requirements, safety | Compilation last reformed 4 Oct 2024 (earlier reforms 8 May 2024, 2021, 2016) [M1] |
| **NTC Proyecto Arquitectónico** | Min. room sizes, doors, stairs, parking, lighting/ventilation | Text read = GODF 6 Oct 2004 [M2]; update notice dated 12 Dec 2024 ⚠ verify [M5] |
| NTC Diseño por Sismo; Cimentaciones; Concreto; Mampostería; Acero; Madera; Viento; Criterios y Acciones | Structural | A package of 10 NTC was updated in the Gaceta of 6 Nov 2023; a 2024–2029 revision process started [M3, M4] ⚠ verify current |
| NTC Evaluación y Rehabilitación | Existing-building assessment | Referred to in RCDF reform of 4 Oct 2024 [M3] |
| **NOM-001-SEDE-2012** Instalaciones eléctricas (utilización) | Electrical installations | Economy ministry listing shows it in force (DOF 29/11/2012, in force 29/05/2013) [M6]; a draft (anteproyecto) to replace it appeared 2025 ⚠ verify |
| NOM-008-SCFI | SI units | General practice ⚠ verify |
| SEDUVI / alcaldía / Programas de Desarrollo Urbano; Ley de Desarrollo Urbano | Zoning (use, height, área libre, parking) | [M1 Arts. 76, 79] |
| Secretaría de Gestión Integral de Riesgos y Protección Civil (SGIRPC) | Fire/civil protection, programa interno | ⚠ verify |
| SACMEX (agua), CFE (electric utility) | Water/sewer connection; electrical supply approval | ⚠ practice |
| DRO (Director Responsable de Obra) / Corresponsables | Professional of record; required for tipo B/C and many type A items | [M1 Art. 47] |
| Outside CDMX: state reglamento + municipal (Desarrollo Urbano / Obras Públicas) | Local rules | ⚠ verify |

## 5. Key numbers (CDMX)

### 5.1 Permit type thresholds [M1 Art. 51-52]
| Type | Scope |
|---|---|
| **Manifestación tipo A** | One single-family house up to **120 m² built**, lot front ≥ 6 m, two levels, max height **5.5 m**, clear spans ≤ **4 m**; also extension keeping totals within these limits; walls ≤ 2.50 m high; not in risk zone |
| **Tipo B** | Non-residential/mixed up to **5 000 m²**, or up to **10 000 m²** residential (excluding the tipo A case) |
| **Tipo C** | Non-residential/mixed > 5 000 m², residential > 10 000 m², or works needing urban-impact study |

### 5.2 Planning (zoning, parking, setbacks)
Heights, built area, **área libre** (open area) and parking counts come from the **Programa de Desarrollo Urbano** and zoning (CUZUS) [M1 Arts. 76, 79]; no single national value. Separation from neighbours must follow the Normas de Ordenación and RCDF Arts. 87, 88, 166 [M1 Art. 77] ⚠ verify numeric values per plot.
Balconies over public road: only floor, parapet and roof, no enclosure (Art. 75) [M1]. Projection over the alignment: doors/windows below 2.50 m may project 0.10 m, above 2.50 m up to 0.20 m; balconies above 2.50 m up to 1.00 m [M2 §1] ⚠ verify current.

### 5.3 Rooms, ceilings, lighting [M2, 2004 text]
| Item | Value |
|---|---|
| Principal bedroom (recámara principal) | 7.00 m², min side 2.40 m, ceiling 2.30 m (Table 2.1) |
| Additional bedrooms / habitable spaces | 6.00 m², side 2.20 m, ceiling 2.30 m (Table 2.1) |
| Other rooms (sala, comedor, cocina, lavado, baño) | Values are in Table 2.1 but column alignment from the source was unreliable ⚠ verify the table |
| Max floor-to-floor height | 3.60 m (above counts as two levels) |
| Natural lighting | Window area ≥ 17.5 % of floor area (15 % for complementary rooms); ventilation opening ≥ 5 % (3.4.2.1) |
| Skylight lighting in bathrooms/circulations | ≥ 4 % of room area |
| Parking clear height | ≥ 2.20 m inside parking; vehicle ramps ≤ 15 %, width ≥ 2.50 m straight / 3.50 m curve |

### 5.4 Doors, corridors, stairs [M2 §4.1]
| Item | Value |
|---|---|
| Door heights | ≥ 2.10 m; main access door in homes 0.90 m wide, habitable rooms 0.75 m (Table 4.1; cocinas/baños value ⚠ verify) |
| Corridors in homes | ≥ 0.75 m wide, 2.30 m high (common to 2+ dwellings ≥ 0.90 m) (Table 4.2) ⚠ verify cell alignment |
| Stair width | Private stair with wall on one side 0.75 m; between two walls 0.90 m; common to 2+ dwellings 0.90 m (Table 4.3) ⚠ verify |
| Tread / riser | Tread ≥ **0.25 m**; riser ≤ **0.18 m** (≥ 0.10 m; ≤ 0.20 m for limited-use service stairs); 2 risers + 1 tread = **0.61–0.65 m** |
| Max risers between landings | 15 |
| Handrails/guards | Guard at least one side at 0.90 m; spiral stair inside dwelling min diameter 1.80 m |
| Ramps for pedestrians | Walk-ways min 1.20 m wide; sidewalk ramps ≥ 1.00 m, ≤ 10 % ⚠ verify |

### 5.5 Egress / fire
- Maximum travel distance to an exit/circulation leading outside: **50 m** high-risk buildings, **40 m** medium/low risk (+50 % with sprinkler/extinguishing devices, per Art. 92) [M1]. Egress doors/vestibules per Art. 91; emergency exit system per Art. 99 [M1] ⚠ verify exact text.
- Building groups: A (essential/high consequence), B1/B2 (others) — Art. 139 for structural purposes [M1].

### 5.6 Electrical / structure
- Electrical design per **NOM-001-SEDE** (2012 edition in force per economy ministry listing [M6]); CFE service point and meter location approved separately ⚠ verify. No numeric receptacle spacing recorded ⚠ verify.
- Seismic: CDMX is in strongly zoned soil (Zonas I, II, IIIa–IIId in the NTC-Sismo); do not design from the architectural NTC — use the updated structural NTC [M3, M4] ⚠ verify numeric zone data.

## 6. Permit drawing set

Typical CDMX package ⚠ practice: Formato de manifestación/licencia (online) · CUZUS or certificado de zonificación · escritura/prueba de propiedad · boleta predial · site plan with colindancias · arquitectónicos: plantas por nivel, fachadas, cortes (min. 2), azotea, cuadro de áreas · estructurales (memoria de cálculo + planos) for B/C and stamped by DRO/Corresponsable · instalaciones hidrosanitarias, eléctricas, gas, contra incendio ⚠ · estudio de mecánica de suelos for larger works ⚠ · DRO responsiva letter. Tipo A is a registration, with lighter documents [M1].

## 7. Common rejection reasons

- Tipo A claimed beyond 120 m² / 5.5 m / 4 m spans / risk-zone plot (needs tipo B) [M1].
- Missing or inconsistent **área libre** or number of parking spaces versus zoning ⚠ practice.
- Lighting/ventilation percentages not demonstrated; window schedule absent [M2].
- Stair geometry (tread < 0.25, riser > 0.18, 2R+T outside 0.61–0.65) [M2].
- Room smaller than Table 2.1 minimum; ceiling < 2.30 m [M2].
- DRO/Corresponsable registration expired or missing seal [M1] ⚠.
- Citing superseded NTC edition ⚠.

## 8. Sources

- [M1] Reglamento de Construcciones para la Ciudad de México, PAOT compilation to 4 Oct 2024: `https://paot.org.mx/centro/reglamentos/df/pdf/2024/RGTO_CONSTRUCCIONES_04_10_2024.pdf` (Arts. 47, 51–52, 75–79, 91–92, 139 read).
- [M2] NTC Proyecto Arquitectónico, GODF 6 Oct 2004 (Tomo II): `https://data.consejeria.cdmx.gob.mx/portal_old/uploads/gacetas/Octubre04_06_103BISTII.pdf`
- [M3] Gaceta agreement 6 Nov 2023 updating NTC (as reported): see PAOT compilation list `https://paot.org.mx/centro/reglamentos/df/pdf/2024/RGTO_CONSTRUCCIONES_04_10_2024.pdf` and news `https://www.elfinanciero.com.mx/nacional/publicaran-actualizacion-de-normas-para-construcciones-de-cdmx/`
- [M4] NTC Diseño por Sismo (text copy): `https://paot.mx/centro/normas_a/2022/2 NORMAS TECNICAS COMPLEMENTARIAS PARA DISENO POR SISMO CON COMENTARIOS.pdf` (older edition).
- [M5] Servicio de Información Jurídica notice on 12/12/24 update (via search snippet; not opened) ⚠.
- [M6] Secretaría de Economía, NOM-001-SEDE-2012: `https://platiica.economia.gob.mx/normalizacion/NOM-001-SEDE-2012/`
