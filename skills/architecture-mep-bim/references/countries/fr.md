# France — Drafting & Code Reference

Legend: a number WITHOUT a flag was read in the cited source (key in §8). **⚠ verify** = drafter knowledge or weak secondary source — confirm on Légifrance / local PLU before relying on it. Local urban-planning rules (PLU) override most dimensional rules for the plot; national codes govern safety, accessibility, energy.

## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Plans in **metres with 2 decimals** (`3,50`) or cm for details; mm for construction details ⚠ verify office practice |
| Decimal sign | Comma (`2,50 m`) |
| Levels | `NGF` (Nivellement Général de la France) altitudes on plan de masse/coupe; finished floor `±0,00` = RDC reference; `+3,12 NGF` style ⚠ verify |
| Language | French: plan de situation, plan de masse, plan de coupe, façades, toiture, RDC, R+1, combles, séjour, chambre, cuisine, SDB, WC, cellier, garage |
| Scales (no legal scale for PC) | The official guidance lists the documents but states **no scale**; the form refers to the dossier checklist [F1]. Usual practice: situation 1/5000–1/25000, masse 1/200–1/500, plans/coupes/façades 1/100 or 1/50 ⚠ verify with mairie |
| Sheets | A4/A3 ISO 5457; plans may be A3 folded to A4 in the dossier; PDF in electronic submission (SVE) ⚠ verify |
| Title block | Cartouche: maître d'ouvrage, adresse, parcelle (section cadastrale + n°), nom de la pièce (PC2…), échelle, date, architecte (+ n° d'ordre, Ordre des architectes) |
| Compulsory architect | Needed if surface de plancher of the project **> 150 m²**, and for any legal entity except farm co-ops [F1] |
| Copies (paper) | General: **4** complete dossiers + **5 extra** each of situation, masse, coupe; protected area: 5 dossiers (6 in natural park) + 5 extra of the three plans [F1] |

## 2. CAD layer/file naming practice + authority CAD rules
- No mandatory national layer scheme for permit drawings. Formal references: **NF EN ISO 13567** (layers) ⚠ verify French adoption; **NF EN ISO 19650-1/-2** (BIM information management); French BIM guidance (*Convention BIM*, *Charte BIM*, MINnD/PTNB) ⚠ verify.
- Common office layers: `A-MUR-PORT`, `A-CLOISON`, `A-MENUISERIE`, `A-ESCALIER`, `A-COTATION`, `A-TEXTE`, `A-HACHURE`, `A-AXE`, `A-LIMITE-PARCELLE`, `A-RESEAUX`, `A-VEGETATION`. File naming: `<opération>_<PCn>_<intitulé>_<ind>.pdf` (e.g. `DUPONT_PC2_Plan_de_masse_A.pdf`).
- **Electronic submission:** communes must accept applications online (saisine par voie électronique; mandatory for communes > 3 500 inhab. since 1 Jan 2022 ⚠ verify). Files are PDF; size limits per platform (e.g. GNAU); name each file with its piece code.
- Authority symbology: none prescribed nationally; keep existing / new / to-demolish distinguishable (hatching or colour) — ABF and instructeurs expect clear *état existant / état projeté* ⚠ verify.

## 3. Drafting conventions
| Topic | Practice |
|---|---|
| Plan de masse (PC2/PCMI2) | Must be **coté dans les trois dimensions** (R.431-9 ⚠ verify article; a search summary attributed it to R*431-8): implantation with distances to boundaries and neighbouring buildings, access, parking, networks (eaux usées/EP/eau/électricité), existing + planned trees, levels of natural ground and finished floor [F8] |
| Dimensions | Chains on plans: overall, then wall/openings; dimensions in metres (wall thickness in cm on details) ⚠ verify |
| Façades & toitures (PC5) | All elevations, materials + colours referenced (teinte RAL/nuancier), openings, roof slopes in %/° and ridge/egout heights vs natural ground [F8] |
| Coupe (PC3) | Cuts the terrain and the building: natural ground profile (TN) vs finished (TF), floor levels, height sous plafond, faîtage and égout, slopes; terrain modelling shown |
| Hatching | NF EN ISO 128-50 ⚠ verify: béton (pointillé + diag.), maçonnerie (diag. 45°), isolant (zigzag), bois (veines). Show demolished (jaune) / new (rouge) in rénovation dossiers (convention, not law) ⚠ verify |
| Symbols | North arrow + graphic scale; door swing arcs; stair arrow "montée"; coupe line with letters; cotes d'altitude `+x,xx NGF`; surfaces per room in m² |
| Surfaces | Distinguish **surface de plancher** (urbanisme; excludes parts < 1,80 m headroom — R.111-22 C.urb ⚠ verify) from **surface habitable** (CCH R.111-2; excludes areas < 1,80 m) [F9] |
| Photos | PC7 near + PC8 far views; viewpoint arrows marked on plan de situation + plan de masse [F8] |
| Notice (PC4) | Describes terrain, access, parking, materials, colours, plantings, networks [F1] |

## 4. Governing codes & authorities
| Domain | Instrument | Notes |
|---|---|---|
| Urbanism | **Code de l'urbanisme** (permis de construire R.421-1ff, pièces R.431-4ff / R*431-7 to R*431-10 ⚠ verify) [F8] | Mairie (service urbanisme); ABF if protected perimeter |
| Zoning | **PLU/PLUi** (zones U, AU, A, N; règlement écrit + graphique); RNU where none; Carte communale | Heights, recul, emprise au sol, CES, stationnement set locally |
| Construction | **Code de la construction et de l'habitation (CCH)**, R.111-1ff (exigences générales), R.111-18ff (accessibilité) | |
| Fire – housing | **Arrêté du 31 janvier 1986** (bâtiments d'habitation, familles 1–4) [F4] | |
| Fire – ERP | **Arrêté du 25 juin 1980** (règlement ERP) + arrêtés types (CO, CH, AM, GE, PE…) ; commission de sécurité | Dossier ERP via PC (AT); notice de sécurité [F5] |
| Accessibility | Housing: **arrêté du 24 décembre 2015** (+ 23 mars 2016); ERP/IOP: **arrêté du 20 avril 2017** (in force 1 July 2017) [F2][F3] | |
| Energy/environment | **RE2020** (arrêté du 4 août 2021; indicateurs Bbio, Cep, Cep,nr, DH, Ic énergie, Ic construction) [F6] | Attestation RE2020 required with PC [F1] |
| Structure | **Eurocodes** NF EN 1990–1999 + Annexes nationales (NF EN 1990/NA…); seismic: décret 2010-1255 zones 1–5 + arrêté du 22 oct 2010 ⚠ verify | |
| DTU | Documents Techniques Unifiés (e.g. DTU 20.1 maçonnerie, 31.2 MOB, 40.xx couverture, 60.11 plomberie, 68.3 VMC ⚠ verify numbers) | CSTB / AFNOR |
| Electrical | **NF C 15-100** (installations BT), NF C 14-100 (branchement) ⚠ verify | Consuel attestation |
| Risks/others | PPRI/PPRN (flood, etc.), Code du patrimoine (ABF radius 500 m ⚠ verify), Loi littoral/montagne, assainissement (SPANC) | |

## 5. Key numbers
| Item | Value | Source |
|---|---|---|
| Instruction délais | maison individuelle **2 mois**, other **3 mois** (general); protected sector 3 mois / 4 mois; incomplete dossier: mairie asks within 1 mois, applicant has 3 mois | [F1] |
| Architect threshold | **150 m²** surface de plancher | [F1] |
| Surface under low ceilings | areas < **1,80 m** headroom excluded from surface habitable | CCH R.111-2 [F9] |
| Décence min. height | 2,20 m; min. room 9 m² / 20 m³ ⚠ verify (décret 2002-120) | [F9] weak |
| Housing – corridor/doors (common parts) | door nominal **0,90 m** = passage utile **0,83 m**; cellar/cellier doors nominal **0,80 m** = **0,77 m** | arr. 24/12/2015 art. 8 [F3] |
| Housing – rooms | rotation circle **Ø 1,50 m** in main rooms/salle d'eau; kitchen passage > **1,50 m**; bedroom bed 1,40 × 1,90 with passages 0,90 / 1,20; WC lateral space **0,80 × 1,30 m** | [F3] |
| Lift obligation (housing) | when building has more than **3 floors above RDC** (R.111-5 CCH) ⚠ verify; ELAN 2018 relaxed "logements accessibles" to ~20 % ⚠ verify | [F3] weak |
| ERP – circulation | cheminement width **≥ 1,40 m** (local narrowing 1,20–1,40 m); slope **≤ 5 %** (8 % over ≤ 2 m; 10 % over ≤ 0,50 m) | arr. 20/04/2017 art. 2 [F2] |
| ERP – parking | adapted bay **3,30 m wide × 5,00 m long**; +1,20 m overlength for angled bays | art. 3 [F2] |
| ERP – doors | main doors < 100 persons: nominal **0,90 m** = **0,83 m** passage; ≥ 100 persons: **1,40 m** passage; non-adapted WC doors 0,80 / 0,77 | art. 10 [F2] |
| ERP – stairs | width between handrails **≥ 1,20 m**; handrail height **0,80–1,00 m** | art. 7-1 [F2] |
| ERP – platform lift | 0,90 × 1,40 m (simple service) / 1,10 × 1,40 m (corner); door nominal 0,90 m; allowed up to 1,20 m height without shaft | art. 7-2 [F2] |
| ERP – unit of passage | 1 UP = **0,60 m**; 1 UP counted as **0,90 m**, 2 UP as **1,40 m**; ≤ 19 persons: 1 dégagement 0,90 m; 20–50: 1,40 m exit | arr. 25/06/1980 [F5] |
| Housing fire families | 3rd family: lowest floor of top dwelling **≤ 28 m** above fire-engine ground; 3A max 7 étages sur RDC; 2nd family: stair must be enclosed if top dwelling floor > **8 m**; "à l'abri des fumées" stair door ≥ **0,80 m** | arr. 31/01/1986 [F4] |
| IGH threshold | habitation > 50 m ⚠ verify (CCH R.122-2) | |
| RE2020 – maison individuelle | Bbio max (mean) **63**; DH max **1 250** °C·h; Ic construction max 640 → **530** kgCO₂/m² from 2025 ⚠ verify (décret 2024-1258); Ic énergie max ~160 kgCO₂/m² ⚠ verify; Cep,nr max value ⚠ verify (sources conflict) | [F6] |
| NF C 15-100 – sockets | chambre ≥ **3**; cuisine ≥ **6** if ≥ 4 m² (3 if < 4 m²), with **4** above worktop; séjour 5 (≤ 28 m²) / 7+ (> 28 m²) ⚠ verify (sources conflict 7 vs 9); sockets axis 5 cm–1,30 m above floor | [F7] |
| NF C 15-100 – circuits | 16 A circuit max 8 sockets (1,5 mm²), 20 A max 12 (2,5 mm²) ⚠ verify; 30 mA RCD ⚠ verify; applies to permits filed ≥ 27 Nov 2015 | [F7] |
| Setbacks / height | **set by the PLU** (recul, prospect "L ≥ H/2" type rules, emprise, hauteur) — no national number | PLU |
| Parking | per PLU; PMR share per CCH ⚠ verify | |
| DP vs PC | extensions: déclaration préalable up to 20 m² (40 m² in PLU urban zone), above that PC; PC if total > 150 m² → architect ⚠ verify (R.421-9, R.421-14, R.431-2) | |

Quick drafting checklist for numbers (France):
- Draw ERP circulation at 1,40 m clear and mark any 1,20 m pinch point with its length [F2].
- Show Ø 1,50 m rotation circles in each main room and salle d'eau of accessible dwellings [F3].
- Show 0,90 m nominal doors (0,83 m passage) on common parts; 0,80 m (0,77 m) for cellars [F3].
- Parking: adapted bay 3,30 × 5,00 m with connecting path horizontal [F2].
- Housing stair "à l'abri des fumées": door ≥ 0,80 m [F4].
- State family (1st–4th) of the building on the fire sheet [F4].
- Label every dimension chain in metres; keep one decimal convention (comma).
- Put RE2020 indicator table (Bbio, Cep,nr, DH, Ic) on the notice or separate attestation sheet [F1].

## 6. Permit drawing set
Maison individuelle (CERFA 13406 ⚠ verify, pieces PCMI) / other buildings (CERFA 13409 ⚠ verify, pieces PC) — same pieces [F1][F8]:
| Code | Piece |
|---|---|
| PC1 / PCMI1 | Plan de situation du terrain (e.g. Géoportail extract) |
| PC2 / PCMI2 | Plan de masse des constructions à édifier ou modifier, coté en 3 dimensions |
| PC3 / PCMI3 | Plan en coupe du terrain et de la construction |
| PC4 / PCMI4 | Notice décrivant le terrain et le projet |
| PC5 / PCMI5 | Plan des façades et des toitures |
| PC6 / PCMI6 | Document graphique d'insertion (photomontage) |
| PC7 / PCMI7 | Photographie : environnement proche |
| PC8 / PCMI8 | Photographie : environnement lointain |
Additional: attestation RE2020 [F1]; PC-ERP notice de sécurité + notice d'accessibilité (ERP) [F5]; PC10 / étude de sol (RGA) ⚠ verify; PC-architecte signature if > 150 m² [F1]; assainissement (SPANC) attestation; PC-ABF extras. Floor plans (plans des niveaux) are not a separate coded piece but are normally added with the coupe/notice for clarity ⚠ verify.

## 7. Common rejection reasons
- Dossier incomplete → mairie's *demande de pièces manquantes* within **1 mois** (délai restarts) [F1].
- Plan de masse **not coté in 3 dimensions** (no NGF levels, no distances to boundaries/neighbours) [F8].
- Missing PC6/PC7/PC8 or viewpoints not marked on plans [F8].
- Distances/hauteur/emprise/stationnement violate **PLU** (recul, hauteur maximale, coefficient d'emprise, espaces verts).
- Missing architect where > 150 m² [F1] or missing **attestation RE2020** [F1].
- Aspect extérieur conflicts (ABF opinion in protected sector; teinte/matériaux not specified in PC5/PC4).
- Façades inconsistent with coupe/plan de masse heights; no scale/north arrow.
- ERP: missing notice de sécurité/accessibilité, door/cheminement widths below art. 2/10 values [F2].
- Surface de plancher miscalculated (areas < 1,80 m included, or voids) → wrong procedure (DP vs PC).
- Risk zones (PPRI/PPRN, sols argileux) ignored.

## 8. Sources
- [F1] service-public.gouv.fr (pièces, délais, copies, architecte) — https://www.service-public.gouv.fr/particuliers/vosdroits/F1986
- [F2] Arrêté 20 avril 2017 (ERP/IOP accessibility), JO 26/04/2017 — https://www.maine-et-loire.gouv.fr/contenu/telechargement/16410/111979/file/arrete_du_20_avril_2017_relatif_a_l_accessibilite_desph_dans_les_erp.pdf
- [F3] DDT Ain analysis of décret + arrêtés 24/12/2015 & 23/03/2016 (housing accessibility) — https://www.ain.gouv.fr/contenu/telechargement/8751/79161/file/2016NoteAnalyseDecretArreteLogementV3.pdf
- [F4] Arrêté 31 janvier 1986 (Légifrance, version 2015-06-24) — https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000474032/2015-06-24
- [F5] ERP effectifs/dégagements — https://www.culture.gouv.fr/fr/Media/Thematiques/Securite-Surete/Fichiers/securite-incendie/fiche-n-11-effectifs-et-issus-de-secours-2022 ; https://www.ffbatiment.fr/techniques-batiment/reglementation-construction/reglementation-securite-incendie/dossier-bam/cheminements-d-evacuation-en-erp-dispositions-constructives-liees-aux-degagements
- [F6] RE2020 thresholds — https://www.ffbatiment.fr/actualites-batiment/actualite/nouveaux-seuils-1er-janvier-2025-pour-batiments-soumis-re-2020 ; https://www.construires.fr/re2020-seuils-2025/
- [F7] NF C 15-100 sockets (Legrand) — https://www.legrand.fr/questions-frequentes/combien-de-prises-de-courant-doit-on-installer-dans-chaque-piece
- [F8] Code de l'urbanisme (pieces R*431-7ff) — https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006188190/ ; PC pieces summary — https://www.culture.gouv.fr/Media/Regions/Drac-Auvergne-Rhone-Alpes/Files/services-patrimoniaux/UDAP-69/Procedure-Recevabilite-du-permis-de-construire
- [F9] Surface habitable 1,80 m — https://questions.assemblee-nationale.fr/dyn/12/questions/QANR5L12QE10778.pdf
