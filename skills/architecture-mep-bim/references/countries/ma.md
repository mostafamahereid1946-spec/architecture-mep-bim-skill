# Morocco — Drafting & Code Reference

Legend: **✓** = read this session (secondary where noted). **⚠ verify** = not confirmed. The **procedural** layer (RGC permit decree) was read from the Bulletin officiel PDF; the **technical** layer (setbacks, coverage, heights, stairs) in Morocco is set by each commune's **plan d'aménagement (PA)**/zoning regulation and the lotissement cahier des charges, which I could not access — so numbers there are mostly ⚠. Source keys [S#] in §8.

**Regime in one line:** Law 12-90 (urbanisme) + Law 25-90 (lotissements/groupes d'habitations/morcellements) + Law 78-00 communal charter; **RGC = Règlement Général de Construction**, approved by **Décret 2-13-424 of 24 May 2013** (BO 6174, 1 Aug 2013; effective the first day of the 6th month after publication, Art. 2) ✓ [S1] — a catalogue and FAOLEX listing suggest it was later replaced by **Décret 2-18-577** (12 June 2019; BO 6874, 16 Apr 2020) ⚠ [S2]; seismic = **RPS 2000** (Décret 2-02-177, 22 Feb 2002) with a 2011 version ✓ [S3]; permits by communal president via **commune/guichet unique** with the **Agence urbaine (وكالة حضرية)** ✓ [S1].

---
## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Plans in **cm** (e.g. `300`, `120`) or m; levels `±0.00` (« niveau 0.00 = RDC ») ; areas m² ⚠ practice |
| Language | **French** on drawings (most offices), Arabic on administrative forms; bilingual title block common ⚠ |
| Scales | Plan de situation 1/2000 (1/5000 rural); plan de masse 1/200–1/500; plans, coupes, façades 1/50 or 1/100 ⚠ (a private source gives 1/2000, 1/5000 rural for situation; others practice) |
| Sheets | A4 folded dossier; A1/A0 plot ⚠ |
| Title block (cartouche) | Maître d'ouvrage, projet, référence foncière (TF n° / réquisition n° / Melkia), commune, architecte (OMA — Ordre National des Architectes — n°), BET (bureau d'études), échelle, date, indice ⚠ |
| Area schedule | Surface terrain, emprise au sol, SHON/surface plancher, COS/CUF (taux), hauteur (R+n), parkings, logements |
| Abbreviations | RDC (rez-de-chaussée), R+2 = 3 levels, R+3 = 4 levels ✓ ([S1] annex: R+2 = 11.50 m, R+3 = 15.50 m) |

---
## 2. CAD layer/file naming practice (what local consultants use) + any authority CAD submission rules (DWG version, coordinate system)
- No national layer standard found. Moroccan offices use French or English layers: `MUR`, `PORTE`, `FENETRE`, `POTEAU`, `ESCALIER`, `COTATION`, `TEXTE`, `HACHURE`, `AXES`, `MOBILIER`, `LIMITE_PARCELLE`, `RETRAIT`, `ALIGNEMENT` ⚠ practice, no source.
- Online filing through **Rokhas.ma** (national platform; >1,000 communes per a private guide) lets applicant file and track ✓ secondary [S4]. Accepted formats (PDF/DWG) and DWG version ⚠ not verified → export DWG 2013 + signed PDF.
- Coordinates: cadastral plans use **Merchich Lambert zones** (Nord Maroc, Sud Maroc, Sahara) ⚠ EPSG codes not verified; ANCFCC (cadastre) supplies the plan cadastral for titled land ✓ secondary [S4]. Respect the **alignement** (property line vs road right-of-way) from the Note de renseignements urbanistiques ✓ [S1].
- File naming ⚠: `TF12345_RDC_R00.dwg`.

---
## 3. Drafting conventions (dims, text, symbols, bilingual rules)
- **Alignment/retrait (setback) drawn and dimensioned** relative to the alignment line given by the Agence urbaine note (Art. 8 and Annex 1 ✓ [S1]).
- Show in the dossier: plan de situation (1/2000), plan de masse, plans of all levels, façades, coupes, plus **photomontage of the existing site** (private-guide list ⚠ [S4]).
- Dimension chains in cm; ceiling heights in coupe; name rooms in French (séjour, chambre, cuisine, SDB, WC, cour/courette, patio, terrasse accessible).
- Symbols: stair arrow « monte », shafts « gaine », courette ventilation; hatch demolition/new in extensions ⚠.
- Sheet text: French (and Arabic in cartouche). Dimensions Western numerals.
- Mark "ne varietur" copies — the permit refers to plans bearing the mention « ne varietur » (permit template) ✓ [S1 annex 6].
- Rooms to label with net area; keep courette (light well) dimensions visible on every plan because communes check them against the PA rules ⚠.
- Draw the road alignment, road width (emprise) and neighbour parcels (TF numbers) on the plan de masse ⚠ practice.


### Local terms for labels
- Plot/land title (titre foncier, TF), alignement (التصفيف), retrait (الارتداد), emprise au sol (البصمة), COS (coefficient d'occupation du sol), CUF.
- Rez-de-chaussée (RDC / الطابق الأرضي), R+1…R+n, courette (فناء داخلي صغير), terrasse (سطح), sous-sol (قبو).
- Permis de construire (رخصة البناء), permis d'habiter (رخصة السكن), certificat de conformité (شهادة المطابقة), Agence urbaine (الوكالة الحضرية).

---
## 4. Governing codes & authorities (table)
| Topic | Instrument | Authority |
|---|---|---|
| Urban planning | Law 12-90 (dahir 1-92-31, 17 June 1992) ✓ cited [S1]; decree 2-92-832 | Ministry of Interior / Habitat |
| Subdivisions | Law 25-90 (dahir 1-92-7); decree 2-92-833 ✓ cited | |
| Permit procedure & documents | **RGC 2-13-424 (2013)** ✓ [S1]; **2-18-577 (2019)** ⚠ replacing | Commune, guichet unique, Agence urbaine |
| Zoning (setbacks, COS, height) | Plan d'aménagement / zonage of each commune + cahier des charges ⚠ | Agence urbaine |
| Seismic | **RPS 2000** (Décret 2-02-177, 22 Feb 2002) ✓ [S3]; RPS 2000 version 2011 (5 seismic zones instead of 3; also ground velocity) ⚠ secondary; draft decree **2.24.766** amending it after the Al Haouz earthquake ✓ news | Ministry of Habitat; applies nationwide, excludes traditional earth/straw/wood buildings and **monolithic residential/professional buildings ≤ 50 m²** ✓ [S3] |
| Concrete | **BAEL 91 / Eurocode transition**, Moroccan standards **NM** (IMANOR) e.g. NM 10.1.xxx ⚠ numbers unverified | IMANOR |
| Fire | Règlement de sécurité contre les risques d'incendie et de panique (Décret 2-14-499 listed as avant-projet on SGG) ⚠ status | Protection civile |
| Electrical | ONEE / distributors (Lydec, Redal, Amendis, régies); NM EN 60364 ⚠ ; **230/400 V 50 Hz** ⚠ | |
| Architect/engineer | Law 016-89 (architects) ⚠; architect mandatory above **240 m²** footprint or non-individual housing (private source ⚠) | OMA |
| Legacy technical rules | Décret 2-64-445 (26 Dec 1964) building rules ⚠ may be superseded | |

---
## 5. Key numbers (residential setbacks/coverage/height, stairs, egress, doors, ceiling heights, min rooms, parking, fire basics, electrical basics, seismic zone/structural basics)

### 5.1 Permit classification (RGC annexes ✓ [S1])
| Class | Definition |
|---|---|
| **Petits projets** | Individual housing (villa/pavillon) **≤ 11.50 m (R+2)** incl. superstructure in a *received* lotissement; buildings **≤ 15.50 m (R+3)** in a received lotissement; shops/trade premises of 3rd-category < **500 m²** floor area & **5.50 m** height; modifications without change of envelope |
| **Grands projets** | Public-body projects; commercial > **500 m²** or > **5.50 m** high; industrial (except 3rd category ≤ 500 m²/5.50 m); buildings **> 15.50 m (R+3)**, or = 15.50 m outside a lotissement; housing groups **> 20 dwellings** |
Procedure ✓ [S1]: Note de renseignements urbanistiques from Agence urbaine within **2 working days** (Art. 7); guichet unique in communes **> 50,000 inhabitants** (Art. 10); for the permis d'habiter dossier the president notifies the inspection date within 3 working days and decides within 15 working days (Art. 41–42 area; construction-permit timelines in Titre III ⚠ not itemised here); a permit lapses if foundation works do not start within **1 year** (permit template Art. 12 ✓ [S1]); commune fences site with **2 m** hoarding (template Art. 14 ✓ [S1]). Private guide: regulatory max 30 days, validity 1 year ⚠ [S4].

### 5.2 Setbacks / coverage / height (⚠ zone-specific)
No national residential setback or coverage figures. Read: PA zone sheet (e.g., zone « villa », « immeuble R+3 », « habitat économique »), COS/CUF, retrait avant/arrière/latéral, hauteur max, parcellaire minimum — all ⚠. Typical Moroccan zones are expressed as **R+n with hauteur max in m** and **taux d'occupation** — do not assume.

### 5.3 Technical minima — legacy decree 1964 (secondary, ⚠ may be superseded)
| Item | Value |
|---|---|
| Min ceiling height (pièces d'habitation) | **2.80 m** away from coast; **2.60 m** in the coastal band (25 km); sloped ceilings min 2.45 m / 2.25 m at lowest point ⚠ [S5] |
| Stair width | **0.80 m** (one upper dwelling) up to **1.20 m** for > 10 dwellings served ⚠ [S5 summary] |
| Lift | mandatory above **5 levels** (legacy) ⚠ |
Current RGC/PA technical thresholds (stairs, lifts, courettes, room sizes, accessibility, parking) are not retrieved — ⚠ all.

### 5.4 Seismic, structural, fire, electrical
- RPS 2000: two safety levels (functional continuity for critical structures; life protection by preventing collapse) ✓ [S3]; zones by acceleration/velocity maps per commune (RPS 2000 v.2011) ⚠ no Za/Zv values verified; Haouz revision pending ✓ news.
- Fire: Protection civile approval ⚠, no figures.
- Electrical: 230/400 V ⚠.

---
## 6. Permit drawing set
Per RGC Annex 4 application + « pièces constitutives » ✓ [S1]: application to commune president; (from private guide ⚠ [S4]) form ×2, CIN ×2 (signature legalised), engagement letter ×3, architect contract ×2, plan de situation ×8 (1/2000), construction drawings ×8 (plans/coupes/façades), titre foncier/ certificat de propriété, plan cadastral, photomontage of site, utility information. Large projects go to the commission d'instruction; permit then « ne varietur » plans; later **permis d'habiter + certificat de conformité** (Art. 41 ✓ [S1]) with completion declaration and telecom conformity attestation.

---
## 7. Common rejection reasons
1. Alignment (retrait) not respected vs Agence urbaine note.
2. Height R+n exceeds PA/lotissement limit (e.g. > 11.50 m R+2 in villa zone).
3. COS/CUF or footprint above zone limit; plot smaller than minimum parcel.
4. Project filed as petit projet but is grand projet (> 15.50 m, > 20 dwellings, > 500 m² commercial).
5. Missing architect/BET stamps, wrong référence foncière, plan not matching titre foncier.
6. Seismic design (RPS 2000) calc / bureau de contrôle report missing.
7. Courette/ventilation or stair/lift not meeting the commune's technical rules ⚠.
8. Incomplete dossier (copies count, plan scales).
9. Site photomontage or utility attestations absent.
10. Works started before permit or not started within 1 year (lapse).


### Pre-submission checklist (Morocco — procedural items verified, technical ⚠)
- [ ] Note de renseignements urbanistiques obtained from the Agence urbaine (issued within 2 working days).
- [ ] Zone, alignment, COS/CUF, hauteur max, retraits read from the PA / cahier des charges.
- [ ] Project class decided: petit projet (<= R+2 11.50 m, or <= R+3 15.50 m in received lotissement) vs grand projet.
- [ ] Guichet unique / Rokhas.ma channel selected; number of copies set per commune.
- [ ] Plan de situation (1/2000 or 1/5000 rural) and plan de masse tied to titre foncier.
- [ ] Architect contract and BET stamps included when architect is mandatory.
- [ ] Seismic zone (RPS 2000) and bureau de contrôle noted in structural file.
- [ ] Fire/civil protection requirements checked for the building class.
- [ ] Permit validity (1 year to start foundations) scheduled; site hoarding 2 m.
- [ ] Completion path planned: permis d'habiter + certificat de conformité.

---
## 8. Sources
- [S1] BO 6174 (1 Aug 2013), Décret 2-13-424 RGC — https://rabat.eregulations.org/media/R%C3%A8glement%20g%C3%A9n%C3%A9ral%20de%20construction%20(RGC).pdf (read)
- [S2] RGC status — https://leap.unep.org/en/countries/ma/national-legislation/decret-ndeg-2-13-424-du-13-rejeb-1434-24-mai-2013-approuvant-le ; catalogue https://citurbarea.com/normes/texte/ma-rgc-2-13-424 ; Adala 2-18-577 PDF https://adala.justice.gov.ma/api/uploads/2025/10/21/ (unreachable ⚠)
- [S3] RPS 2000 — https://fr.hespress.com/354734-rps-2000-la-garantie-de-la-solidite-de-nos-batisses.html ; revision news https://medias24.com/2024/09/03/le-reglement-parasismique-marocain-sera-actualise-dans-80-communes/ (403 ⚠), https://en.yabiladi.com/articles/details/154270/morocco-enacts-earthquake-resistant-building-regulations.html
- [S4] Demarches Maroc permit guide (private) — https://www.demarchesmaroc.com/permis-construire/
- [S5] Décret 2-64-445 (1964) — https://www.aumk.ma/sites/default/files/2020-07/decret_1[1].pdf ; https://auessaouira.ma/wp-content/uploads/2015/06/decret_10.pdf
