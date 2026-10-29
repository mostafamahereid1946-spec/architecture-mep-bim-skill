# Germany — Drafting & Code Reference

Legend: a number WITHOUT a flag was read in the cited source (key in §8; MBO/MBauVorlV read as full text, others via search summaries). **⚠ verify** = from drafter knowledge / weak secondary source — confirm before relying on it. Building law is a *Länder* matter: the MBO is a model; each Landesbauordnung (LBO) adopts and varies it. Always check the LBO of the Bundesland + local Satzungen.

## 1. Units, scales, sheets, title block, language
| Item | Practice |
|---|---|
| Units | Metric. Plan dimensions usually in **metres with 2 decimals** (`4,76`) or cm for small details; levels in m with 3 decimals (`+2,885`) — ⚠ verify office/authority preference |
| Decimal sign | Comma (`3,50 m`); thousands separator dot/space |
| Levels | `±0,00` = Fertigfußboden (OKFF) Erdgeschoss as local reference; absolute height as `NHN` (Normalhöhennull, e.g. `+112,45 m ü. NHN`) on Lageplan ⚠ verify |
| Language | German drawing labels: Grundriss, Schnitt, Ansicht, Lageplan, Wohnen, Schlafen, Küche, Bad, WC, Flur, Abstellraum, HWR, Keller, Dachgeschoss |
| Scale – Lageplan | **≥ 1:500**, larger if assessment needs it (MBauVorlV §7(2)) [D4]. Cadastre extract must show neighbours within **≥ 50 m** (§7(1)) |
| Scale – Bauzeichnungen | **≥ 1:100** for Grundrisse, Schnitte, Ansichten (MBauVorlV §8(1)) [D4]; larger scale (1:50) where detail needed |
| Other scales | 1:20 / 1:10 / 1:5 details; 1:200 Übersicht; 1:1000 Bebauungsplan extract — preferred series per DIN EN ISO 5455 ⚠ verify |
| Sheets | A-series, DIN EN ISO 5457 (A0 841×1189 … A4 210×297); folded to A4 for submission per DIN 824 ⚠ verify; many Ämter now take PDF digitally |
| Title block | Schriftfeld per DIN EN ISO 7200 ⚠ verify: Bauvorhaben, Bauherr, Entwurfsverfasser (Unterschrift), Planinhalt, Maßstab, Datum, Plan-Nr., Index |
| Required signatures | Bauherr + Entwurfsverfasser on Bauvorlagen (MBO §§53, 54, 69 — ⚠ section numbers per LBO) |
| Digital submission | Many Länder run digital Bauantrag portals (XBau data standard) ⚠ verify per Land |

## 2. CAD layer/file naming practice + authority CAD rules
- **DIN EN ISO 13567-1/-2** (CAD layer structure: *Agent* – *Element* – *Presentation* fields) is the formal German layer standard ⚠ verify edition; in practice most offices use software templates (Allplan, Archicad, Revit/Nemetschek) rather than strict ISO 13567.
- **BIM / information management:** DIN EN ISO 19650-1/-2 (national adoption; German national annex status ⚠ verify); naming of containers per project BIM execution plan (BAP/AIA). Revit/IFC delivery needed only for public projects (BIM-Stufenplan, Bund) ⚠ verify.
- Sensible default layer set (own convention, state it in the title block legend): `A-WAND-TRAG`, `A-WAND-NICHT-TRAG`, `A-TUER`, `A-FENSTER`, `A-TREPPE`, `A-MASS`, `A-TEXT`, `A-SCHRAFFUR`, `A-ACHSEN`, `A-RAUM-STEMPEL`, `A-LAGEPLAN-GRENZE`.
- **Authority drawing rules:** MBauVorlV (Bauvorlagenverordnung of each Land) prescribes content *and colour* — **existing = grey, new = red, to be demolished = yellow, Grundstücksgrenze = violet, Baulasten = brown** (Anlage 1, §8(4)) [D4]. Mixed-up colours/hatching are a common reason for Nachforderung.
- Authority may require unchanged **PDF/A or signed PDF** for digital submission ⚠ verify.

## 3. Drafting conventions
| Topic | Rule / practice |
|---|---|
| Governing standards | **DIN 1356-1** (Bauzeichnungen) — 2018 edition listed as withdrawn; **E DIN 1356-1:2026-09** draft exists [D9]; dimensioning of building drawings now by **DIN EN ISO 7519** [D9]. Which one an authority cites varies ⚠ verify |
| Dimension basis | **Rohbaumaße** (structural/rough sizes, measured to unplastered wall faces) are the default on Bauantrag/Rohbau drawings [D9]; Ausbaumaß (finished size) only if stated |
| Openings | Rect. openings noted as **width/height** fraction (e.g. `1,01/2,135`) at axis or reference line [D9]. Brüstungshöhe given as `BRH` ⚠ verify |
| Dimension chains | Typically 3 chains on elevations of plans: Gesamtmaß / Raummaße (axis or wall to wall) / Öffnungsmaße ⚠ verify |
| Height marks | Triangle symbol with `OKFF`, `OKRD` (Rohdecke), `UK`, `OK Attika`, `First`, `Traufe`; Geländelinie bold with `±0,00` |
| Room data | Room name + **Fläche in m²** + (optional) Bodenbelag per room; Wohnfläche per WoFlV, DIN 277 for Brutto-/Netto-Raumfläche ⚠ verify |
| Break-throughs | Wand-Durchbrüche: two narrow diagonal solid lines in section/elevation [D9] |
| Suspended ceilings | Narrow dash-double-dot line on plan, level or room height noted [D9] |
| Cut line | Schnittlinie with arrows + letters `A–A`, arrow shows view direction [D9 cross-reference required] |
| Stairs | Laufrichtung arrow starts at first riser, "auf" (up) at start; Steigungsverhältnis noted `18 / 27` ⚠ verify |
| North arrow | Required on Lageplan and floor plans (MBauVorlV §7(3)) [D4] |
| Hatching | Per DIN 1356-1/ISO 128 ⚠ verify: Beton = dense diag. + dots; Mauerwerk = diag. 45°; Dämmung = wavy/zigzag; Holz = grain; Stahl = bold. Authority legend overrides |
| Line weights | 0,18 / 0,25 / 0,35 / 0,5 / 0,7 mm (ISO 128 ladder √2) ⚠ verify. Cut elements heaviest |
| Symbols | Anlage 1 MBauVorlV defines Zeichen & Farben [D4] — other symbols must be explained in legend |

## 4. Governing codes & authorities
| Domain | Instrument | Notes |
|---|---|---|
| Building law | **MBO** (Musterbauordnung, Fassung Nov 2002, last amended per BMK decision **25.09.2020**) [D1] → 16 **LBOs** | Check Land; 2023 MBO amendment exists ⚠ verify |
| Planning law | BauGB, BauNVO (GRZ/GFZ/Vollgeschosse), Bebauungsplan, §34/§35 BauGB | Municipality (Bauamt/Stadtplanungsamt) |
| Permit forms | Baugenehmigung (normal), vereinfachtes Verfahren, Genehmigungsfreistellung, Kenntnisgabe (BW) — varies by Land | Untere Bauaufsichtsbehörde |
| Drawing content | **MBauVorlV** (Musterbauvorlagenverordnung, Feb 2007, last amended 25.09.2020) [D4] + Land BauVorlV | |
| Fees/phases | **HOAI** §34 (Gebäude) | [D2] |
| Energy | **GEG** (Gebäudeenergiegesetz): Neubau Wohngebäude §§15–17; Energieausweise §§79–88; Anlage 1 Referenzgebäude [D3] | Current wording being reformed ⚠ verify (some §§ now "weggefallen") |
| Accessibility | **DIN 18040-1** (öffentlich), **-2** (Wohnungen); LBO §50-type rules | Technische Baubestimmung per Land |
| Stairs | **DIN 18065** Gebäudetreppen (ed. 2022-09 ⚠ verify) | |
| Structures | **Eurocodes** DIN EN 1990–1999 + German NA (e.g. DIN EN 1990/NA, 1991-1-1/NA, 1992-1-1/NA, 1998-1/NA seismic) | Standsicherheitsnachweis by Prüfingenieur (GK 4-5) |
| Fire | MBO §§26ff + **MVV TB**, Brandschutznachweis; Muster-Industriebau-/Versammlungsstätten-/Beherbergungsstättenverordnung | |
| Electrical | **VDE 0100** series (VDE 0100-410 RCD ≤ 30 mA), **DIN 18015-1/-2/-3**, TAB of Netzbetreiber | Elektrofachkraft |
| Acoustics / thermal | DIN 4109 (Schallschutz), DIN 4108 (Wärmeschutz) | |
| Authorities | Bauaufsichtsamt (Bauantrag); Brandschutzdienststelle; Denkmalbehörde; Umwelt-/Naturschutz; Vermessung (amtlicher Lageplan by ÖbVI, §7 plan sources) | |

## 5. Key numbers
Gebäudeklassen (MBO §2(3)) [D1]: **GK1** freistehend ≤ 7 m, ≤ 2 Nutzungseinheiten, ≤ 400 m² · **GK2** same without "freistehend" · **GK3** other ≤ 7 m · **GK4** ≤ 13 m, each NE ≤ 400 m² · **GK5** all others. Height = OKFF of highest storey with possible Aufenthaltsraum above mean ground. **Hochhaus** > 22 m (§2(4)).

| Item | Value | Source |
|---|---|---|
| Abstandsfläche depth | **0,4 H, min 3 m**; Gewerbe/Industrie 0,2 H, min 3 m; Wohngebäude GK1–2 ≤ 3 oberirdische Geschosse: **3 m** | MBO §6(5) [D1] |
| H (Wandhöhe) | wall height + 1/3 roof height if pitch < 70°; full roof height if ≥ 70° | MBO §6(4) [D1] |
| Garage / Nebengebäude on boundary | mittlere Wandhöhe ≤ 3 m, length ≤ 9 m per boundary, ≤ 15 m total on plot | MBO §6(8) [D1] |
| Vorbauten ignored | ≤ ⅓ of wall width, projection ≤ 1,50 m, ≥ 2 m from opposite boundary | MBO §6(6) [D1] |
| Lichte Raumhöhe | Aufenthaltsräume **≥ 2,40 m** (not required in Wohngebäude GK1–2 or in Dachraum) | MBO §47(1) [D1] |
| Daylight | Rohbau window opening ≥ **1/8** of room Netto-Grundfläche | MBO §47(2) [D1] |
| Dwelling | each Wohnung: Küche/Kochnische, Bad (Wanne/Dusche) + WC; storage for pram/bikes in GK3–5 | MBO §48 [D1] |
| Zwei Rettungswege | per NE per Geschoss; 2nd may be Feuerwehr ladder point; Anleiterhöhe Brüstung **≤ 8 m** | MBO §33(1)(3) [D1] |
| Escape distance | from any point of Aufenthaltsraum to Treppenraum/outside **≤ 35 m** (Luftlinie) | MBO §35(2) [D1][D11] |
| Rauchabschnitt corridor | **≤ 30 m** (soll); single-direction corridor to Sicherheitstreppenraum ≤ 15 m | MBO §36(3) [D1] |
| Rescue window | clear **≥ 0,90 × 1,20 m**, sill ≤ 1,20 m above floor | MBO §37(5) [D1] |
| Wohnungstür (lift-served) | clear width ≥ **0,90 m** | MBO §37(3) [D1] |
| Brüstung/Umwehrung | window parapet ≥ 0,80 m (drop ≤ 12 m), ≥ 0,90 m (> 12 m); Umwehrung 0,90 m (drop 1–12 m), 1,10 m (> 12 m) | MBO §38(3)(4) [D1] |
| Lift | required if building height **> 13 m**; Rollstuhl car ≥ 1,10 × 1,40 m, Trage 1,10 × 2,10, door ≥ 0,90 m | MBO §39(4)(5) [D1] |
| Barrierefrei | buildings > 2 Wohnungen: one Geschoss' dwellings barrierefrei erreichbar | MBO §50(1) [D1] |
| Stair (DIN 18065) | Steigung 14–20 cm, Auftritt 23–37 cm (Wohnen, ≤ 2 Wohnungen); notw. Treppen > 2 Wohnungen 14–19 / 26–37 ⚠; 2s+a ≈ 59–65 cm ⚠ | [D5][D7] |
| Stair width | clear Laufbreite ≥ **0,80 m** (≤ 2 Wohnungen), ≥ **1,00 m** (others); stair width measured between handrails | [D5] |
| Headroom | Treppendurchgangshöhe **≥ 2,00 m** (DIN 18065 §6.4); side strip may drop 25 cm in houses ≤ 2 Wohnungen | [D6] |
| Handrail | height **0,80–1,15 m**; clearance to wall ≥ 5 cm (DIN 18040: 0,85–0,90 m) | [D6] |
| Accessible (DIN 18040-2, NRW checklists) | Wohnungstür clear ≥ 0,90 × 2,05; Innentür ≥ 0,80 × 2,05; Bewegungsfläche 1,50 × 1,50; Rampe ≤ 6 %, width ≥ 1,20, landing every 6 m; Lift > 1,10 × 1,40 | [D8] (secondary; ⚠ verify norm) |
| Parking | set by Land/municipal **Stellplatzsatzung**; MBO §49 only states duty and Ablöse | [D1]; numbers ⚠ local |
| Fire resistance | GK1–2 feuerhemmend tragende Bauteile; GK4 hochfeuerhemmend; GK5 feuerbeständig (MBO §27) ⚠ verify | |
| Structural factors | γG = 1,35, γQ = 1,50 (DIN EN 1990/NA) ⚠ verify; seismic zones 0–3 per DIN EN 1998-1/NA ⚠ verify |
| Electrical | RCD ≤ 30 mA on socket circuits ≤ 20 A (DIN VDE 0100-410) ⚠ verify; min. equipment per DIN 18015-2 (Ausstattungswert 1–3) ⚠ verify counts |

## 6. Permit drawing set
Typical Bauantrag (Land form + MBauVorlV) [D4][D10]:
1. Bauantragsformular (Land form), signed Bauherr + Entwurfsverfasser; Betriebsbeschreibung where relevant.
2. **Amtlicher Lageplan** ≥ 1:500 with neighbour parcels ≥ 50 m, Baulasten, distances to boundaries/Abstandsflächen, access, parking, Höhenpunkte, North arrow (§7). Sometimes also "Abstandsflächenplan" (separate sheet).
3. **Bauzeichnungen** ≥ 1:100: Grundrisse all floors incl. usable Dachraum (room uses, stairs, doors on escape routes, shafts, flues), Schnitte (foundations, ground levels existing/new, lichte Raumhöhen, stair geometry, roof pitch), Ansichten (adjoining buildings, materials, terrain) (§8) [D4].
4. **Baubeschreibung** with Gebäudeklasse & Höhe (§9).
5. Berechnung **BRI / GRZ / GFZ**, Wohn-/Nutzfläche, Stellplatznachweis, Entwässerungsantrag.
6. **Standsicherheitsnachweis** (§10) or Erklärung des Tragwerksplaners; **Brandschutznachweis** (§11) [D4].
7. Nachweis Wärmeschutz/GEG (Energieausweis-relevant data) [D3]; Schallschutznachweis if required.
8. Statistik-Bogen, Bauleiter/Fachplaner-Benennung, Freiflächenplan / Entwässerungspläne where needed.

**HOAI §34 Leistungsphasen (Gebäude)** [D2]: LPH 1 Grundlagenermittlung 2 % · 2 Vorplanung 7 % · 3 Entwurfsplanung 15 % · **4 Genehmigungsplanung 3 %** (the Bauantrag phase) · 5 Ausführungsplanung 25 % · 6 Vorbereitung der Vergabe 10 % · 7 Mitwirkung bei der Vergabe 4 % · 8 Objektüberwachung 32 % · 9 Objektbetreuung 2 %. Drawing scales by phase: LPH 3 1:100, LPH 5 1:50/1:20/1:1–10 ⚠ verify (Anlage 10 HOAI).

## 7. Common rejection reasons
- Abstandsflächen not shown or computed with wrong H (missing roof ⅓ share) or overlapping neighbour's area [D1 §6].
- Lageplan not by Vermessungsstelle / out of date (sources cite ½–1 year validity, Land-specific) — ⚠ verify.
- Plans below 1:100 or missing colour code (grey/red/yellow) and legend [D4].
- Missing Rettungsweg proof: 2nd escape route, 35 m distance, rescue-window size 0,90 × 1,20 [D1].
- Fensterfläche < 1/8 of room area or ceiling height < 2,40 m where required [D1].
- Stellplatznachweis / Fahrradabstellplätze per Satzung missing.
- Inconsistent areas/heights between Grundriss, Schnitt, Ansicht, Baubeschreibung and Berechnungsbögen.
- Missing Standsicherheits-/Brandschutznachweis or unsigned forms.
- Non-compliance with Bebauungsplan (GRZ, Baugrenze, Dachform, Traufhöhe).
- Treppe directly behind door opening into it without Podest [D1 §34(7)].

## 8. Sources
- [D1] MBO Nov 2002, amended 25.09.2020 — https://bauministerkonferenz.de/Dokumente/42323530.pdf
- [D2] HOAI §34 — https://www.gesetze-im-internet.de/hoai_2013/__34.html
- [D3] GEG contents — https://www.gesetze-im-internet.de/geg/
- [D4] MBauVorlV text (§§7–11, Anlage 1) — https://umwelt-online.de/recht/bau/argebau/bvorl.htm ; edition listing — https://www.bauministerkonferenz.de/verzeichnis.aspx?id=991&o=759O986O991
- [D5] Stufen/Treppen rules — https://www.baunetzwissen.de/drucken/stufen-definition-begriffe-und-regeln-3352555
- [D6] Treppendurchgangshöhe — https://www.baunetzwissen.de/treppen/fachwissen/planungsgrundlagen/treppendurchgangshoehe-3448835 ; Handlauf — https://www.baunetzwissen.de/treppen/fachwissen/treppenelemente/handlauf-167534
- [D7] DIN 18065 secondary (14–19 / 26–37, 59–65) — https://www.deutschland-rechner.de/treppe-rechner
- [D8] DIN 18040-2 city checklists — https://www.stadt-muenster.de/fileadmin//user_upload/stadt-muenster/63_bauordnungsamt/pdf/checkliste-fuer-die_pruefung-der-barrierefreiheit.pdf ; https://www.wipperfuerth.de/fileadmin/redaktion/Hansestadt_Wipperfuerth/Bauaufsicht/Barrierefreiheit_fuer_Wohnungen.pdf
- [D9] Dimensioning DIN EN ISO 7519 / DIN 1356-1 status — https://www.bauprofessor.de/bemassung-bauzeichnungen/ ; https://www.din.de/en/wdc-beuth:din21:403956420
- [D10] Bauvorlagen overview (Stuttgart, 11.2024) — https://stuttgart.de/medien/ibs/63-uebersicht-bauvorlagen-wohnungsbau-stand-11.2024.pdf
- [D11] Rettungswege — https://www.baunetzwissen.de/treppen/fachwissen/brand--schallschutz/rettungswege-167600
