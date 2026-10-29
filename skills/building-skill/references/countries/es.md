# Spain — Drafting & Code Reference

Legend: a number WITHOUT a flag was read in the cited source (key in §8; DB-SUA, DB-SI, DB-HE read as official PDF text). **⚠ verify** = drafter knowledge or weak secondary source. Spain has national technical codes (CTE) but **urbanism and habitability are regional/municipal** (Comunidad Autónoma + Plan General/ordenanzas of the ayuntamiento) — always check them.

## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Plans in **metres with 2 decimals** (`3,50`), details in mm/cm; surfaces in m² (superficie útil / construida) |
| Decimal sign | Comma |
| Levels | `±0,00` = cota de referencia (planta baja); `+2,85` cotas; site levels in m relative to street/topographic ⚠ verify |
| Language | Castilian (+ co-official language per region in some documents): planta baja, sección, alzado, planta de cubierta, salón, dormitorio, cocina, baño/aseo, distribuidor, trastero, garaje |
| Scales | Project plans typically 1:50 (viviendas), 1:100 (edificio), 1:200/1:500 (emplazamiento), 1:20–1:5 details ⚠ verify per ayuntamiento; ISO 5455 / UNE 1023 series 1:50, 1:100, 1:200 [E5] |
| Sheets | A-series per UNE-EN ISO 5457 (A4 210×297, A3 297×420, A2 420×594, A1 594×841) with 10 mm margin (as taught/used) [E5]; A0 for large projects |
| Title block | **UNE-EN ISO 7200** (cajetín); old UNE 1035 was annulled 10 Feb 2005 [E5]. Contents: título proyecto, nº plano, escala, autor, fecha, comprobación [E5], promotor, arquitecto + nº colegiado |
| Project doc norm | **UNE 157001:2014** (criterios generales para la elaboración formal de proyectos) [E5] |
| Visado | Colegio visado is mandatory only for certain works (RD 1000/2010 ⚠ verify scope); ayuntamientos often ask for it for obra mayor [E6] |

## 2. CAD layer/file naming practice + authority CAD rules
- No national CAD-layer rule for licencias. References: **UNE-EN ISO 13567** (capas) ⚠ verify; **UNE-EN ISO 19650-1/-2** (BIM) ⚠ verify; buildingSMART Spain / *Comisión es.BIM* guides; Real Decreto/public tender BIM obligations vary ⚠ verify.
- Typical layers (office convention, state it on the plano legend): `A-MUROS`, `A-TABIQUES`, `A-CARPINTERIA`, `A-VENTANAS`, `A-ESCALERA`, `A-COTAS`, `A-TEXTOS`, `A-SOMBREADO`, `A-EJES`, `A-MOBILIARIO`, `A-LIMITE-PARCELA`.
- File naming: `<exp>_<fase>_<disciplina>_<nº>_<descripción>_<rev>.pdf` (fase = BAS/EJE; disciplina = ARQ/EST/INS).
- Electronic submission: sede electrónica del ayuntamiento, PDF **firmado digitalmente** (certificado digital/@firma) and often DWG/DXF or *georreferenciado* ⚠ verify; Colegio visado electrónico (e.g. COAM/COAC) issues a CSV-verified PDF.
- Cadastral base: *Catastro* (Sede Electrónica del Catastro) for referencia catastral and parcel graphics ⚠ verify.

## 3. Drafting conventions
| Topic | Practice |
|---|---|
| Dimensioning | UNE 1039 (acotación, principios generales) [E5]; cotas in m with 2 decimals on plans; chains: exterior total / ejes / huecos ⚠ verify |
| Line types | UNE-EN ISO 128 (grosores 0,18–0,7 mm) ⚠ verify; cut = thick, vista = thin, ejes = dash-dot |
| Hatching/symbols | Hormigón (puntos + diag.), fábrica ladrillo (diag. 45°), aislamiento (zigzag), madera (vetas); ISO 128-50 ⚠ verify. Colors for modificado: **rojo = nuevo, amarillo = demolición** in reform projects (convention) ⚠ verify |
| Rooms | Room name + **superficie útil** in m² per room; "superficie construida" per planta in cuadro de superficies |
| Stairs | Arrow "sube/baja" from first tread; nº contrahuellas × huella e.g. `14 CH × 0,28` |
| Sections | Show forjados, cota de pavimento terminado, altura libre, cubierta pendiente %, cimentación outline |
| Fire plans | DB-SI: separate sheets with sectores de incendio, recorridos de evacuación, salidas, extintores/BIE symbols, ascensores; EI/R ratings in leyenda |
| Accessibility plan | Itinerarios accesibles, círculos Ø 1,50 m, rampas with slope %; per SUA 9 [E1] |
| Project phases | **Proyecto básico** (enough for licencia, not for starting works) and **proyecto de ejecución** (must not lower declared performance) — content per CTE Anejo I [E6] |
| Legend of norms | Cuadro de cumplimiento CTE (DB-SE, SI, SUA, HS, HE, HR) and norma urbanística |

## 4. Governing codes & authorities
| Domain | Instrument | Notes |
|---|---|---|
| Building quality | **LOE – Ley 38/1999** de Ordenación de la Edificación; **CTE** (RD 314/2006) | Agents: promotor, proyectista, director de obra, DEO, constructor |
| Structures | **DB-SE** (bases), SE-AE (acciones), SE-C (cimientos), SE-A (acero), SE-F (fábrica), SE-M (madera); **Código Estructural** (RD 470/2021) replaces EHE-08 ⚠ verify; seismic **NCSE-02** ⚠ verify | |
| Fire | **DB-SI** (edition incl. RD 164/2025, BOE 10/04/2025) [E2]; RIPCI (RD 513/2017) ⚠ verify | |
| Safety & accessibility | **DB-SUA** (consolidated 14 Jun 2022, RD 450/2022) [E1] | |
| Health | **DB-HS** (HS1 humedad, HS2 residuos, HS3 calidad aire, HS4 suministro agua, HS5 evacuación aguas, HS6 radón) [E3b] ⚠ verify edition | |
| Energy | **DB-HE** (HE0 consumo, HE1 envolvente, HE2 instalaciones térmicas/RITE, HE3 iluminación, HE4 ACS renovable, HE5 FV, HE6 recarga EV) [E3]; RD 390/2021 certificación ⚠ verify | |
| Acoustics | **DB-HR** (RD 1371/2007 and amendments) ⚠ verify | |
| Electrical | **REBT** RD 842/2002 + ITC-BT-25 (circuitos interiores viviendas) [E4] | Boletín (CIE) by instalador autorizado |
| Telecom | ICT (RD 346/2011) ⚠ verify | |
| Urbanism | Ley del suelo (TRLSRU, RDL 7/2015) ⚠ verify, PGOU/Normas Subsidiarias, ordenanzas municipales, Plan Parcial | Ayuntamiento (Urbanismo/Licencias) |
| Safety on site | Estudio/Estudio básico de seguridad y salud (RD 1627/1997) ⚠ verify; Estudio de gestión de residuos (RD 105/2008) ⚠ verify | |
| Authorities | Ayuntamiento, Colegio de Arquitectos (visado), Comunidad Autónoma (habitabilidad, patrimonio), bomberos (SI for special uses) | |

## 5. Key numbers
| Item | Value | Source |
|---|---|---|
| Protection from falls | barrier required where drop > **55 cm**; barrier height **0,90 m** (drop ≤ 6 m), **1,10 m** (beyond); stair openings < 40 cm wide: 0,90 m | DB-SUA SUA 1 §3.1, §3.2.1 [E1] |
| Stair – restricted use | width ≥ **0,80 m**; riser ≤ **20 cm**; tread ≥ **22 cm** | SUA 1 §4.1 [E1] |
| Stair – general (vivienda) | tread ≥ **28 cm**; riser **13–18,5 cm** (≤ 17,5 cm in public use or when no lift alternative); **54 ≤ 2C + H ≤ 70 cm** | SUA 1 §4.2.1 [E1] |
| Stair width (Residencial Vivienda) | clear width ≥ **1,00 m** (Tabla 4.1); other uses 0,80 / 0,90 / 1,00 | SUA 1 §4.2.2 [E1] |
| Landing (meseta) | length ≥ **1,00 m**, width ≥ stair width | SUA 1 §4.2.3 [E1] |
| Handrail | height **0,90–1,10 m**; required when rise > 55 cm; both sides if width > 1,20 m or no lift; extends 30 cm; ≥ 4 cm from wall | SUA 1 §4.2.4 [E1] |
| Ramps | slope ≤ **12 %**; accessible: ≤ **10 %** (< 3 m), **8 %** (< 6 m), **6 %** otherwise; cross slope ≤ 2 %; run ≤ 15 m (accessible 9 m); landing ≥ 1,50 m | SUA 1 §4.3 [E1] |
| Headroom | ≥ **2,10 m** (restricted-use), **2,20 m** elsewhere; **2,00 m** at door thresholds | SUA 2 §1.1 [E1] |
| Doors accessible | clear width ≥ **0,80 m** (≥ 0,78 m at 90° opening) | SUA 9 Anejo A [E1] |
| Turning space | Ø **1,50 m** free (vestíbulo, bath, rooms of accessible dwelling) | SUA 9 [E1] |
| Lift obligation (vivienda) | when > **2 floors** between accessible entrance and dwelling or common zone, or > **12 viviendas** on floors without accessible entrance | SUA 9 §1.1.2 [E1] |
| Evacuation distance | **25 m** single exit; **50 m** with > 1 exit; **35 m** where occupants sleep; 50 m if direct exit & ≤ 25 persons; limits not applied inside dwelling units (origin = dwelling door) ⚠ verify | DB-SI SI 3 Tabla 3.1 [E2] |
| Evacuation height | descending **≤ 28 m** (uso general); ascending ≤ 10 m | SI 3 [E2] |
| Single exit occupancy | ≤ 100 persons (500 for building of viviendas) | SI 3 [E2] |
| Sector de incendio | Residencial Vivienda: ≤ **2 500 m²**; separation between viviendas **EI 60** | SI 1 Tabla 1.1 [E2] |
| Structure fire resistance | vivienda unifamiliar R 30; Residencial Vivienda: sótano **R 120**, ≤ 15 m **R 60**, ≤ 28 m **R 90**, > 28 m **R 120** | SI 6 Tabla 3.1 [E2] |
| Thermal limits (DB-HE1, Tabla 3.1.1.a, zones α/A/B/C/D/E) | Muros/suelos exterior U_lim 0,80/0,70/0,56/**0,49**/**0,41**/0,37 W/m²K; cubiertas 0,55/0,50/0,44/**0,40**/**0,35**/0,33; huecos U_H 3,2/2,7/2,3/2,1/1,8/1,80 (row alignment inferred ⚠ verify) | [E3] |
| REBT circuits (electrificación básica) | C1 iluminación 10 A, 1,5 mm², ≤ 30 puntos · C2 tomas 16 A, 2,5 mm², ≤ 20 · C3 cocina/horno 25 A, 6 mm², 2 · C4 lavadora/lavavajillas/termo 20 A, 4 (6) mm², 3 · C5 baño/cocina 16 A, 2,5 mm², 6 | ITC-BT-25 [E4] |
| REBT room minima | salón/dormitorio: 3 tomas, or 1 per 6 m²; light point 2 if > 10 m²; kitchen 2 C2 + horno C3 + 3 C4 + 3 C5; corridors 1 light per 5 m | ITC-BT-25 Tabla 2 [E4] |
| REBT protection | general switch ≥ 25 A omnipolar; diferencial ≤ 30 mA; max voltage drop 3 % | ITC-BT-25 [E4] |
| Min. ceiling height (habitability) | typically 2,50 m habitable rooms — **regional/municipal** (not CTE) ⚠ verify | |
| Parking | per PGOU/ordenanza (e.g. 1 plaza/vivienda) ⚠ verify; accessible plaza dimensions per SUA 9 ⚠ verify | |
| Setbacks/height | set by PGOU/plan parcial (retranqueos, altura, ocupación, edificabilidad) | local |

Quick drafting checklist for numbers (Spain):
- Stairs in viviendas: draw 1,00 m clear width, tread ≥ 28 cm, riser 13–18,5 cm, check 54 ≤ 2C+H ≤ 70 [E1].
- Landings ≥ 1,00 m long, full stair width; no door swing over the landing zone [E1].
- Barriers 0,90 m (drop ≤ 6 m) / 1,10 m; no footholds 30–50 cm above floor in dwellings [E1].
- Accessible doors ≥ 0,80 m clear; Ø 1,50 m circles in vestíbulo, baño, dormitorios, estancia [E1].
- Mark sector limit 2 500 m² and EI 60 walls between viviendas on the SI sheet [E2].
- Show structural R rating by evacuation height (15 / 28 / >28 m) on the SI sheet [E2].
- Climate zone (α–E) must be stated before filling the HE1 envelope table [E3].
- List C1–C5 circuits and room outlet counts on the electrical schematic [E4].

## 6. Permit drawing set
**Licencia de obras** (obra mayor; obra menor via *declaración responsable* in many municipalities ⚠ verify) — *Proyecto básico* visado/firmado [E6]:
1. Solicitud / instancia, referencia catastral, justificante de tasas e ICIO.
2. **Memoria** (descriptiva, constructiva, justificación del cumplimiento del CTE: DB-SE, SI, SUA, HS, HE, HR; cuadro de superficies y normativa urbanística) [E6].
3. **Planos**: situación/emplazamiento (1:500–1:2000 ⚠ verify), plano de parcela y cotas de rasante; plantas 1:100 (or 1:50), alzados, secciones (con cotas, alturas libres), planta de cubiertas; plano de cumplimiento urbanístico (retranqueos, ocupación, edificabilidad); plano de accesibilidad; plano de evacuación/sectores (DB-SI).
4. **Pliego/Presupuesto** (mediciones por capítulos or presupuesto de ejecución material).
5. Estudio básico/estudio de seguridad y salud; gestión de residuos; ficha de justificación energética (HE) [E6].
6. Hoja de encargo / dirección facultativa; nombramiento; visado colegial if required [E6].
7. After licence: **proyecto de ejecución** (conforming to básico; changes need prior authorisation) [E6]; end of works → Libro del Edificio, certificado final de obra, licencia de primera ocupación ⚠ verify.

## 7. Common rejection reasons
- Cumplimiento urbanístico: retranqueos, altura, ocupación, edificabilidad vs PGOU not justified/drawn.
- Missing or unsigned *visado*/colegiado signature where required [E6].
- No CTE justification (SUA stairs 28 cm tread / 13–18,5 riser / 54–70 rule; SI evacuation; HE U-values) [E1][E2][E3].
- Accessibility: no accessible itinerary, lift required (> 2 plantas / > 12 viviendas) not provided [E1].
- Habitability regs (autonómica): minimum room areas/ceiling height not met ⚠ verify.
- Execution project deviates from básico without prior authorisation [E6].
- Wrong or missing referencia catastral; inconsistent surfaces between memoria, planos and cuadro de superficies.
- Missing fire plan (sectors, evacuation distances, EI/R ratings) [E2].
- Heritage/protection constraints (Catálogo de bienes protegidos, entorno BIC) ignored.
- REBT: insufficient circuits/points or electrification grade not stated [E4].

## 8. Sources
- [E1] DB-SUA (14 Jun 2022 consolidated) — https://www.codigotecnico.org/pdf/Documentos/SUA/DBSUA.pdf
- [E2] DB-SI (incl. RD 164/2025) — https://www.codigotecnico.org/pdf/Documentos/SI/DBSI.pdf
- [E3] DB-HE (incl. RD 450/2022) — https://www.codigotecnico.org/pdf/Documentos/HE/DBHE.pdf ; [E3b] DB-HS — https://www.codigotecnico.org/pdf/Documentos/HS/DBHS.pdf
- [E4] ITC-BT-25 table — https://normatia.com/es/normativa/rebt/2025/itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas/ ; https://ocw.unican.es/pluginfile.php/2391/course/section/2392/3_13.pdf
- [E5] Drawing standards (ISO 5457, UNE 1039, cajetín ISO 7200, UNE 157001) — https://eia.unex.es/wp-content/uploads/sites/5/2024/07/Documento-planos-1.pdf ; https://shop.standards.ie/en-ie/standards/une-157001-2014-16107_saig_une_une_35771
- [E6] Proyecto básico vs ejecución, licencia — https://arquitectes.cat/en/printpdf/28222 ; https://sax.es/wp-content/uploads/2024/08/TRAMITE-SOLICITUD-LICENCIA-DE-OBRA-MAYOR.pdf
