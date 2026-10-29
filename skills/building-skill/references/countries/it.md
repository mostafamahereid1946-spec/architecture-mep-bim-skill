# Italy — Drafting & Code Reference

Legend: a number WITHOUT a flag was read in the cited source (key in §8; DM 5/7/1975 and DM 236/1989 read via full-text pages). **⚠ verify** = drafter knowledge or weak secondary source. Italy has **state law (DPR 380/2001 etc.) + regional laws + municipal Regolamento Edilizio / PRG-PGT-PUC / NTA**: always check the Comune and Region. The *Salva Casa* reform (DL 69/2024, Law 105/2024) changed many rules — check current text.

## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Plans in **metres with 2 decimals** (`3,50`) or cm; areas in m² (superficie utile, SLP, SU/Snr), volumes in m³ (still used in many PRG) |
| Decimal sign | Comma |
| Levels | `±0,00` = quota di riferimento (pavimento piano terra); site quotes in m s.l.m. or vs strada ⚠ verify |
| Language | Italian: pianta, sezione, prospetto, planimetria generale, stato di fatto / di progetto / sovrapposizione (giallo-rosso), soggiorno, camera, cucina, bagno, disimpegno, ripostiglio, cantina |
| Scales | Planimetria generale/inquadramento 1:1000–1:2000 (stralcio PRG/mappa catastale 1:2000); lotto 1:200/1:500; piante, sezioni, prospetti **1:100** (1:50 for detail); dettagli 1:20–1:1 ⚠ verify with Comune |
| Catasto | Planimetria unità immobiliare commonly **1:200** (also 1:100, 1:50, 1:500 by size); elaborato planimetrico commonly 1:500 or 1:200 [I7] |
| Sheets | A-series UNI EN ISO 5457 ⚠ verify; digital PDF |
| Title block | Cartiglio: committente, oggetto, ubicazione (foglio/mappale/sub), tavola n., scala, data, revisione, progettista (albo/ordine + n.), firme |
| Signatures | Digital signature (firma digitale CAdES/PAdES) on PDF for SUE/SUAP portals ⚠ verify |

## 2. CAD layer/file naming practice + authority CAD rules
- **UNI 11337** series (BIM: modeling, information levels LOD/LOI, digital document management) and **UNI EN ISO 19650-1/-2**; public procurement BIM duties in D.Lgs. 36/2023 (Allegato I.9) ⚠ verify. Layer standard: UNI EN ISO 13567 ⚠ verify; most studios use own layers.
- Typical layers: `A-MURI-PORTANTI`, `A-TRAMEZZI`, `A-SERRAMENTI`, `A-SCALE`, `A-QUOTE`, `A-TESTI`, `A-CAMPITURE`, `A-ASSI`, `A-DEMOLIZIONI` (giallo), `A-COSTRUZIONI` (rosso), `A-CATASTO`.
- **Colour convention for sovrapposizione:** *giallo = demolizioni, rosso = nuove costruzioni* (universal practice, in most Regolamenti edilizi) ⚠ verify per Comune.
- File naming: `<pratica>_<TAV-nn>_<contenuto>_<rev>.pdf(.p7m)`.
- Submission: SUE (Sportello Unico Edilizia) or **SUAP** (impresainungiorno.gov.it) via MUDE/regional portals; PDF/A signed; DWG generally not required ⚠ verify.
- Catasto: DOCFA (planimetrie, elaborato planimetrico) and PREGEO (frazionamenti) software formats from Agenzia delle Entrate [I7] ⚠ verify.

## 3. Drafting conventions
| Topic | Practice |
|---|---|
| Standards | UNI EN ISO 7519 (disegni tecnici edilizia, general principles) ⚠ verify; UNI EN ISO 128 (lines), UNI EN ISO 5455 (scales) ⚠ verify |
| Stato di fatto / progetto / comparativo | Three plan sets or one sovrapposizione: existing (as legitimate stato legittimo), project, comparative with yellow/red |
| Dimensions | Quote chains in m (2 decimals) for external overall, internal rooms, openings; clear openings (luce netta) for accessibility checks [I2] |
| Room data | Each room: destinazione d'uso, superficie utile (m²), altezza interna (H = 2,70) , rapporto aeroilluminante (RAI ≥ 1/8) table [I1] |
| Hatching | Calcestruzzo (punteggiato + diag.), muratura (diag. 45°), isolante (zigzag), legno; UNI EN ISO 128-50 ⚠ verify |
| Sections | Show H min/medie in sottotetti (altezza media, minima), quota terreno originario / sistemato, quota ±0,00 |
| Prospetti | All elevations with materials and colours (PRG/Regolamento Colore); quote of colmo/gronda |
| Distance drawings | Distances between pareti finestrate and from confini (DM 1444/68 art. 9) [I3]; Codice Civile art. 873–907 (confini, vedute) ⚠ verify |
| Fire plans | Planimetrie antincendio: compartimentazione, vie d'esodo, lunghezze d'esodo, aree a rischio, mezzi estinzione, percorsi VVF (Codice prevenzione incendi) [I8] |
| Impianti | Schemi unifilari/planimetria impianto elettrico CEI 64-8 with level (1/2/3) declared; scarichi/impianto idrico per UNI 9182 ⚠ verify |
| Accessibility | Layout showing rotation space, rampe %, ascensore, parcheggi riservati [I2] |

## 4. Governing codes & authorities
| Domain | Instrument | Notes |
|---|---|---|
| Building law | **DPR 380/2001** (Testo Unico Edilizia): art. 6 edilizia libera, 6-bis CILA, 10 permesso di costruire, 22 SCIA, 24 agibilità (SCA), 34-bis tolleranze, 36-bis sanatoria; **Salva Casa** DL 69/2024 → L. 105/2024 [I5] | Comune (SUE/SUAP) |
| Planning | DM 1444/1968 (distances, heights, standard urbanistici), PRG/PGT/PUC, NTA, Regolamento Edilizio comunale | |
| Hygiene/habitability | **DM 5 luglio 1975** (altezza, superfici) [I1]; Regolamento d'igiene ASL/regionale | ASL |
| Accessibility | **L. 13/1989**, **DM 236/1989**, DPR 503/1996 (spazi pubblici) [I2] | |
| Structural | **NTC 2018** (DM 17 gennaio 2018) + Circolare 21 gennaio 2019 n. 7 [I4]; seismic classification zones 1–4 (OPCM 3274/2003) ⚠ verify; authorization/deposit with Genio Civile/Regione (art. 93–94 DPR 380) ⚠ verify | Collaudo statico |
| Fire | **DM 3 agosto 2015** Codice di prevenzione incendi (RTO + RTV); RTV V.14 (DM 19 maggio 2022) residential > 24 m [I8]; DM 16/5/1987 n. 246 ⚠ verify; DPR 151/2011 attività soggette ⚠ verify | VVF – SCIA antincendio / parere |
| Energy | L. 10/1991, **D.Lgs 192/2005**, **DM 26/6/2015** (requisiti minimi), APE (attestato di prestazione energetica), D.Lgs 199/2021 (rinnovabili) ⚠ verify | Relazione tecnica ex L.10 |
| Electrical | **CEI 64-8** (3 performance levels; current chapter 37 edition ⚠ verify) ; **DM 37/2008** dichiarazione di conformità [I6] | |
| Acoustics | DPCM 5/12/1997 (requisiti acustici passivi) ⚠ verify | |
| Authorities | Comune (SUE/SUAP), Soprintendenza (vincoli D.Lgs 42/2004), Regione/Genio Civile, VVF, ASL, Agenzia Entrate-Territorio (Catasto) | |

## 5. Key numbers
| Item | Value | Source |
|---|---|---|
| Min internal height (abitabili) | **2,70 m**; corridors, bathrooms, WC, ripostigli **2,40 m**; mountain communes > 1000 m: 2,55 m. *Salva Casa* added derogations (esp. existing buildings) — ⚠ verify current text | DM 5/7/1975 art. 1 [I1] |
| Min areas | 14 m² per first 4 occupants + 10 m² each further; bedroom **9 m²** (1 person) / **14 m²** (2); living room **≥ 14 m²** | DM 5/7/1975 art. 2 [I1] |
| One-room dwelling | ≥ **28 m²** (1 person) / **38 m²** (2 persons) incl. services | art. 3 [I1] |
| Daylight | openable window area ≥ **1/8** of floor area; average daylight factor ≥ **2 %** | art. 5 [I1] |
| Bathroom | each dwelling ≥ 1 bathroom with WC, bidet, bath/shower, washbasin; window or mechanical extraction | art. 7 [I1] |
| Distance between buildings | min **10 m** between pareti finestrate of facing buildings (zones other than A) | DM 1444/1968 art. 9 [I3] |
| Doors | entrance door clear opening ≥ **80 cm**; other doors ≥ **75 cm**; handles 85–95 cm | DM 236/89 p. 8.1.1 [I2] |
| Corridors | width ≥ **100 cm** with widened turning points about every 10 m | p. 8.1.9 [I2] |
| Stairs (common) | width ≥ **1,20 m**; tread ≥ **30 cm**; 2r + a = 62–64 cm; parapet ≥ **1,00 m**; handrail 0,90–1,00 m | p. 8.1.10 [I2] |
| Ramps | slope ≤ **8 %**; width ≥ 0,90 m (1 wheelchair) / 1,50 m (2 people); landing about every 10 m | p. 8.1.11 [I2] |
| Lift (new residential) | car ~**1,30 deep × 0,95 wide**; non-residential 1,40 × 1,10; lobby 1,50 × 1,50 | p. 8.1.12 [I2] |
| Bathroom accessibility | WC/bidet lateral access ≥ 100 cm from axis; bath lateral ≥ 140 cm; basin frontal ≥ 80 cm | p. 8.1.6 [I2] |
| Parapets | balcony/terrace parapet ≥ **100 cm**, sphere Ø 10 cm must not pass | p. 8.1.3 / 8.1.8 [I2] |
| Accessible parking | width ≥ **3,20 m**; ≥ 1 per 50 spaces | p. 8.2.3 [I2] |
| External path | width ≥ 90 cm; slope generally ≤ 5 % | p. 8.2.1 [I2] |
| Structural – service life | VN ≥ **50 years** ordinary works; ≥ 100 strategic; classes of use I–IV with **CU = 0,7 / 1,0 / 1,5 / 2,0**; reference period **VR = VN × CU, minimum 35 years** | NTC 2018 Tab. 2.4.I–II [I4] |
| Structural – partial factors | γG1 = 1,3, γQ = 1,5 ⚠ verify (Tab. 2.6.I) | NTC 2018 |
| Seismic | zones 1–4; site hazard via NTC grid (ag, F0, Tc*) ⚠ verify | NTC 2018 / OPCM 3274 |
| Fire – residential | RTV V.14 for civil habitation with fire height > **24 m**; fire-height classes & resistance levels per Codice S.2 ⚠ verify numbers | DM 3/8/2015 [I8] |
| Electrical | CEI 64-8 level 1/2/3; sizing ≥ **3 kW** up to 75 m², **6 kW** above; ≥ 2 differential switches (level 1); 30 mA ⚠ verify | CEI 64-8 [I6] |
| Tolerances | art. 34-bis tolerances 2 %–6 % depending on useful surface ⚠ verify (Salva Casa); works completed by 24 May 2024 | [I5] |
| Parking | L. 122/1989: 1 m² per 10 m³ of volume ⚠ verify; PRG may require more | |
| Setbacks/height | per PRG/NTA (distanza dai confini, indice fondiario, altezza max) — DM 1444 art. 8 limits ⚠ verify | local |

Quick drafting checklist for numbers (Italy):
- Room schedule on every floor plan: use, m², H, window area, RAI vs 1/8 [I1].
- Doors drawn ≥ 80 cm (entrance) / 75 cm (internal) clear; corridors ≥ 100 cm [I2].
- Common stairs 1,20 m wide, tread ≥ 30 cm, parapet 1,00 m [I2].
- Ramps ≤ 8 % with landing about every 10 m; lift car at least 1,30 × 0,95 m (residential) [I2].
- Dimension distances between pareti finestrate (10 m) and to boundaries on the lot plan [I3].
- State VN, class of use, CU and VR on the structural cover sheet [I4].
- Declare CEI 64-8 level (1/2/3) on the electrical sheet and in the DM 37/08 declaration [I6].
- Update catasto drawing (1:200) after final works [I7].

## 6. Permit drawing set
Choose title (DPR 380/2001) [I5]: **CILA** (art. 6-bis, light works), **SCIA** (art. 22, e.g. manutenzione straordinaria strutturale / alternative), **Permesso di costruire** (art. 10, new build, heavy ristrutturazione), **SCIA in alternativa al PdC**, edilizia libera (art. 6). Typical PdC/SCIA package:
1. Modello unico (MUDE/regional) + procura/delega, diritti di segreteria, marca da bollo.
2. **Relazione tecnica illustrativa** + asseverazione del progettista (conformità urbanistica/edilizia, igienico-sanitaria, art. 20 DPR 380).
3. **Inquadramento**: estratto di mappa catastale, estratto PRG/NTA, estratto CTR/ortofoto (1:1000–1:5000 ⚠ verify).
4. **Planimetria generale/lotto** (1:200–1:500) with confini, distanze, quote, accessi, parcheggi (L.122), superfici permeabili.
5. **Piante** (tutti i livelli, coperture), **sezioni** (≥ 2, incl. stair/ sottotetto), **prospetti** 1:100 (1:50 ⚠), tabelle di calcolo (SLP, volume, SC, H, RAI) and sovrapposizione giallo/rosso for interventions on existing.
6. **Stato legittimo** documents (title edilizio storico) for existing buildings (art. 9-bis).
7. Elaborati **barriere architettoniche** (L.13/89, DM 236/89) + relazione [I2].
8. **Strutturale**: deposito/autorizzazione sismica + relazione NTC 2018 [I4].
9. **Impianti** (DM 37/08 progetto if required), **L.10** energy report/APE, acoustic report, fire (VVF SCIA/valutazione progetto) [I8][I6].
10. Paesaggistica (autorizzazione) if vincolo; ASL parere where needed; **fine lavori / SCA (agibilità)** and **aggiornamento catasto (DOCFA)** after works [I7].

## 7. Common rejection reasons
- Non-compliance with **DM 1444/68 art. 9** 10 m rule or boundary distances (measured at every point; also non-parallel walls) [I3].
- Missing/ambiguous **stato legittimo** — no title for existing parts; plans do not match catasto [I5][I7].
- Heights/areas below DM 5/7/1975 (2,70 m, 9/14 m², 1/8 window) with no derogation basis (check Salva Casa limits) [I1].
- Accessibility layout missing or doors < 80 cm, stairs < 1,20 m, ramps > 8 % [I2].
- Wrong procedure (CILA used where SCIA/PdC needed — structural or prospetti changes).
- Missing sismica deposit or structural report; NTC class of use/VR not stated [I4].
- Fire safety documents missing for activities under DPR 151/2011 [I8].
- No sovrapposizione yellow/red, or colours not legible; missing signatures/digital signature.
- Catasto planimetria not updated or not at the declared scale [I7].
- Landscape/heritage authorisation (Soprintendenza) not obtained.

## 8. Sources
- [I1] DM 5 luglio 1975 — https://www.bosettiegatti.eu/info/norme/statali/1975_dm_05_07.htm
- [I2] DM 14 giugno 1989 n. 236 — https://www.bosettiegatti.eu/info/norme/statali/1989_0236.htm
- [I3] DM 1444/1968 art. 9 — https://ediltecnico.it/distanze-in-edilizia-pareti-finestrate-inderogabili-i-10-metri/
- [I4] NTC 2018 parameters — https://ediltecnico.it/quali-parametri-scegliere-per-definire-azione-sismica/ ; https://online.scuola.zanichelli.it/strutturecalcoloprogetto/files/2017/06/Zanichelli_Zavanella_VolumeC_ModuloO.pdf
- [I5] DPR 380/2001 / Salva Casa — https://www.lavoripubblici.it/news/gestione-difformita-edilizie-salva-casa-34245/1
- [I6] CEI 64-8 V3 levels — https://informaimpresa.it/item/variante-v3-alla-norma-cei-64-8
- [I7] Catasto planimetrie — https://www.edilizia.com/catasto/planimetria-catastale-costo-dove-richiederla-e-a-chi-richiederla/ ; https://www.visura.it/downl/SUPP/GuideV/Guida_Planimetrie.pdf
- [I8] Codice prevenzione incendi / RTV — https://www.ingenio-web.it/articoli/rtv-14-per-edifici-di-civile-abitazione-uno-sguardo-d-insieme/
