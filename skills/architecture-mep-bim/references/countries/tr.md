# Türkiye — Drafting & Code Reference

Legend: **✓** = read this session from the consolidated official text (Planlı Alanlar İmar Yönetmeliği as amended to RG 1/7/2026-33297; Binaların Yangından Korunması Hakkında Yönetmelik [BYKHY] doc dated 01/07/2025; TBDY 2018 annex PDF). **⚠ verify** = not confirmed this session. Source keys [S#] in §8.
Local authority overlays: each belediye (municipality) may have its own İmar Yönetmeliği and Plan Notları (zoning-plan notes) that override defaults below — always read the plan notes of the parcel (İmar Durumu belgesi) first.

---
## 1. Units, scales, sheets, title block, language

| Item | Practice |
|---|---|
| Units | Metric. Plan dims in **cm** on Turkish architectural sheets (e.g. `90`, `120`) or m with 2 decimals for levels/setbacks (`±0.00`, `+3.00`) ⚠ practice varies by office |
| Levels | Kot (kot = level): `±0.00` = ground-floor finished floor; road/pavement kerb level (yol kotu / kaldırım üst kotu) drives entry rules (Art. 30, Art. 43 [S1]) |
| Language | **Turkish only** on submitted drawings (Turkish text, Turkish legend). English optional on non-official sets ⚠ |
| Typical scales | Site/vaziyet planı 1/200 (1/500 large); floor plans/kesit/görünüş **1/50 or 1/100**; details 1/20–1/5 ⚠ practice (the Ministry's architectural-project preparation guidance was not retrievable) |
| Sheets | ISO A-series folded to A4 (210×297) for the dossier; A1/A0 plot ⚠ |
| Title block | Antet/kartuş (right or bottom): proje adı, pafta/ada/parsel no (ada = block, parsel = parcel), yapı sahibi (owner), mimari proje müellifi (architect + oda sicil no), pafta no/ölçek/tarih, revision table. Chamber of Architects (Mimarlar Odası) registration stamp + "Proje Müellifi" signature mandatory ⚠ |
| North / orientation | Required on site plan; adjacent parcel numbers and road widths labelled |
| Area schedule | Alan cetveli: parsel alanı, taban alanı (TAKS), emsal (KAKS) alanı, toplam inşaat alanı, bağımsız bölüm net/brüt — see Art. 21–22 [S1] on what counts as "katlar alanı" |

---
## 2. CAD layer/file naming practice (what local consultants use) + any authority CAD submission rules (DWG version, coordinate system)

- **No single mandatory national layer standard.** An ITU study reports offices each run their own CAD standard [S6]. The Ministry (ÇŞB) published a CADD document covering project/folder/file/layer/block naming, symbols and title block, but the PDF could not be retrieved this session (TLS error) → treat as ⚠ unread [S7].
- Typical Turkish consultant layers (practice, ⚠ no source): `DUVAR`, `KOLON`, `KIRIS`, `PERDE`, `KAPI`, `PENCERE`, `MERDIVEN`, `ASANSOR`, `AKS`, `OLCU`/`DIM`, `YAZI`/`TEXT`, `KOT`, `HATCH`, `MOBILYA`, `ISLAK_HACIM`, `KORKULUK`, `CIKMA`, `TERAS`. English ISO-style (`A-WALL`, `A-DOOR`) common in international-firm files.
- Authority CAD: e-permit flows (belediye e-imar, YAPS/Yapı Denetim) accept PDF + DWG in many municipalities ⚠; no verified DWG version mandate. Deliver **DWG 2010-2018 format (R2013 safe)** plus PDF ⚠ practice.
- Coordinate system: national cadastre/plan CRS is **ITRF96 / TUREF TM 3° zones** (TM27…TM45; Istanbul/Ankara ≈ TM30/TM33) ⚠ EPSG not verified; ED50 UTM legacy plans still circulate. Site plan (vaziyet planı) must tie to the parcel's coordinated cadastral boundary (kadastro/tapu) ⚠.
- File naming practice: `ADAxxx_PARSELyy_MIMARI_PLAN_R01.dwg` ⚠ office convention.

---
## 3. Drafting conventions (dims, text, symbols, bilingual rules)

- **Dimensions:** three chains on plans: overall, axis-to-axis (aks), openings. Columns/beams on structural sheets labelled S1, K1, etc.; architectural plans overlay column grid. Wall thickness conventionally 20 cm exterior / 10 cm interior (brick) ⚠.
- **Text:** Turkish; height ≈ 2.5 mm min plot ⚠. Room tags with function + area (m²) — the İmar Yönetmeliği minimum areas (Art. 29) are checked from these tags.
- **Symbols:** door swing arcs; stairs with up arrow ("ÇIKIŞ"); shafts: "BACA", "ŞAFT", "IŞIKLIK" (lightwell), "HAVA BACASI" (air shaft). Fire stair marked "KAÇIŞ MERDİVENİ"; "YANGIN GÜVENLİK HOLÜ"; "SIĞINAK" (shelter, if required by Sığınak Yönetmeliği [S1 Art. 27]).
- **Hatch/line:** cut walls poché; yıkılacak (demolish) yellow, yapılacak (new) red in tadilat (alteration) projects — classic Turkish convention ⚠.
- Show levels for each floor, "kat yüksekliği" (floor-to-floor, from top-of-slab to top-of-slab — Art. 28 measures this way ✓).
- **Accessibility:** ramps, WC, lift per TS 9111 (Art. 30(9) ✓) — show clearances.


### Local terms for labels
- Plan (kat planı), section (kesit), elevation (görünüş), site plan (vaziyet planı), ada/parsel (block/parcel), kot (level), aks (grid axis).
- TAKS (taban alanı kat sayısı), KAKS/emsal (floor area ratio), çekme mesafesi (setback), cephe (façade), çatı (roof), bodrum (basement).
- İmar durumu (zoning status), yapı ruhsatı (building permit), iskân (occupancy permit), yapı denetim (building inspection), itfaiye (fire brigade).

---
## 4. Governing codes & authorities (table)

| Topic | Instrument | Authority | Notes |
|---|---|---|---|
| Zoning/building form | **Planlı Alanlar İmar Yönetmeliği** (under İmar Kanunu 3194; original RG 3/7/2017 ⚠, amended to RG 1/7/2026-33297 ✓ [S1]) | Çevre, Şehircilik ve İklim Değişikliği Bakanlığı (ÇŞİDB); belediye/büyükşehir | Applies where an uygulama imar planı exists (Art. 2 ✓) |
| Unplanned areas | Plansız Alanlar Yönetmeliği | Belediye / İl Özel İdaresi | Out of scope |
| Seismic | **Türkiye Bina Deprem Yönetmeliği (TBDY 2018)** — RG 30364 mükerrer, 18/3/2018; in force 1/1/2019 ✓ [S3] | AFAD / ÇŞİDB | Replaced DBYBHY 2007 (Art. 4 ✓) |
| Concrete | **TS 500** (RC design) with TBDY ch. 7; **TS EN 206** concrete; TS 498 loads | TSE | Cover/rebar tables not verified → ⚠ |
| Fire | **BYKHY** (RG 19/12/2007-26735; Cabinet decision 2007/12937 ✓ [S2]) | İtfaiye (municipal fire dept) approves project | Updated through 2025 doc |
| Accessibility | TS 9111; Erişilebilirlik mevzuatı | ÇŞİDB / Aile ve Sosyal Hizmetler | Referenced Art. 30 ✓ |
| Energy | Binalarda Enerji Performansı Yönetmeliği; TS 825 insulation; Enerji Kimlik Belgesi | ÇŞİDB | Referenced in Art. 25, 33 ✓; values ⚠ |
| Supervision | Yapı Denetimi Kanunu 4708; yapı denetim kuruluşu | ÇŞİDB | Mandatory for most buildings ⚠ |
| Parking / shelter | Otopark Yönetmeliği; Sığınak Yönetmeliği (RG 25/8/1988-19910) | Belediye | Referenced Art. 27 ✓; ratios ⚠ |
| Electrical | Elektrik İç Tesisleri Yönetmeliği (TS HD 60364) | EMO / distribution co. (e.g. TEİAŞ/BEDAŞ) | 230/400 V 50 Hz ⚠ |

---
## 5. Key numbers (residential setbacks/coverage/height, stairs, egress, doors, ceiling heights, min rooms, parking, fire basics, electrical basics, seismic zone/structural basics)

### 5.1 Setbacks (bahçe mesafeleri) — default when plan silent (Art. 23 ✓)
| Item | Value |
|---|---|
| Front (ön) / road-side / public-space-adjacent | **5.00 m min** |
| Side (yan) | **3.00 m min** |
| Rear (arka) | **3.00 m min** |
| Add for buildings > 4 storeys | **+0.50 m per storey above 4** to side & rear (Art. 23(1)ç) |
| Storey count for side/rear calc | total façade height ÷ 3; remainder > 2.50 m counts as 1 floor (Art. 23(1)d) |
| Fire stair retrofit outside | ≥ 1.50 m from parcel line (side/rear), ≥ 3.00 m (front) (Art. 22 2026 amend.) |
| Multiple buildings on parcel | allowed if each respects yard rules (Art. 24) |

TAKS/KAKS/Hmax: set **by the plan**, not by the regulation — read İmar Durumu ⚠.

### 5.2 Heights (Art. 28 ✓)
| Item | Value |
|---|---|
| Max floor-to-floor, residential zones | **3.60 m** (4.00 m for ≤ 3 storeys excl. basement) |
| Ground floor with shops in housing zone | 4.50 m |
| Commercial zone: ground / mezz. ground / other | 4.50 / 5.50 / 4.00 m |
| Min clear height, inhabited floors | **2.60 m** (2.40 m where air-obstruction limits plan) (Art. 28(4)) |
| Wet rooms, pantry, understair, corridors, uninhabited basement | down to **2.20 m** (Art. 28(5)) |
| Mezzanine (asma kat) clear min | 2.40 m (definition, Art. 4 ✓) |
| Understair enclosed if height < | **1.80 m** (Art. 31(6)) |

### 5.3 Rooms (Art. 29 ✓ — min short side / net area)
Living room 3.00 m / 12.0 m²; bedroom 2.50 m / 9.0 m²; kitchen or cooking niche 1.50 m / 3.30 m²; bathroom 1.50 m / 3.00 m²; WC 1.00 m / 1.20 m². Hall/corridor ≥ **1.20 m** (Art. 29(3)). Combined spaces add the individual minima (29(4)). Kitchen, room and bath/WC may not vent to the same shaft (29(6)). Access/WC must follow TS 9111.

### 5.4 Stairs, ramps, lifts, guards
| Item | Value |
|---|---|
| Common stair & landing width, residential | ≥ **1.20 m** and ≥ fire-escape width (Art. 31(1)a) |
| Other (non-residential) buildings | ≥ 1.50 m |
| Stair inside a dwelling | ≥ **1.00 m** |
| Riser | ≤ **0.16 m** (no lift); ≤ 0.18 m (with lift) (31(2)a) |
| Tread | 2a + b = 60–64 cm, tread ≥ 0.27 m; winders ≥ 0.10 m at narrow end, 0.27 m mid (31(2)b–c) |
| Common stairs must be | daylit; reach roof & basement; not timber (31(1)) |
| Entrance corridor | ≥ 1.50 m (residential) / 2.20 m (public) (Art. 30(1)) |
| Ramp slopes | 1:12 (≤15 cm rise), 1:14 (16–50), 1:16 (51–100), 1:20 (>100) (30(12)) |
| Handrails | 32–45 mm dia, at 0.90 m and 0.70 m (30(13)) |
| Guardrail (korkuluk) | **≥ 1.10 m** above floor; openings ≤ **0.10 m** (Art. 38) |
| Lift required | 3 storeys (incl. basement) = provide shaft; ≥ 4 storeys = install lift (Art. 34(1)); ≥ 2 lifts if > 20 dwellings above ground or ≥ 10 storeys (34(4)) |
| Lift car (single) | ≥ 1.20 m short side, ≥ 1.80 m², door 0.90 m clear; landing 1.20 m (sliding) / 1.50 m (swing) (34(2)) |
| Lightwell (ışıklık) | 1–6 storeys ≥ 1.50 m × 4.50 m²; ≥ 7 storeys ≥ 2.00 m × 9.00 m² (Art. 32(2)) |
| Air shaft | ≥ 0.60 × 0.60 m (32(3)); max 4 rooms per minimum shaft |
| Septic tank to neighbour | ≥ 5.00 m (Art. 37) |

### 5.5 Projections & walls
Closed bay (kapalı çıkma): ≤ **1.50 m** beyond building line on road fronts; rear/side may project 1.50 m but not within 3.00 m of parcel line (Art. 41(a)). Eaves ≤ **1.00 m** unless plan says otherwise; 0.50 m beyond a projection (Art. 42). Garden wall: front ≤ **0.50 m** solid + railing ≤ 1.00 m; behind front line ≤ 1.50 m (Art. 43).

### 5.6 Fire (BYKHY, 2025 doc [S2] ✓)
| Item | Value |
|---|---|
| High-rise (yüksek bina) | building height **> 21.50 m** (or structure > 30.50 m) (Art. 4) |
| Escape capacity unit | **50 cm** width per unit (Art. 32(2)) |
| Escape route min width | 100 cm if 50–500 occupants/floor; corridors serving rooms ≥ 110 cm; absolute min 80 cm; **≥ 120 cm** in high-rise (Art. 33) |
| Exit door single leaf | clear 80–120 cm (Art. 33(5)) |
| Escape stair enclosure | walls ≥ **120 min**, smoke-tight door ≥ **90 min** (Art. 38(3)) |
| Landings | between 4 and 17 steps; no winders if h > 15.50 m or > 100 people/floor (Art. 41(3)) |
| Headroom on stair | ≥ 2.10 m; flight height max 3.00 m (41(6)) |
| Fire-safety lobby | 3–6 m² area, ≥ 1.8 m dimension; 120-min walls / 90-min doors (Art. 34) |
| Exits | ≥ 2 exits generally; > 50 persons ⇒ 2; > 500 ⇒ 3; > 1000 ⇒ 4 (Art. 39) |
| Fire-truck road | ≥ 4 m wide, 8 m dead-end; radii 11/15 m; max 6 % grade; reach ≤ 45 m (Art. 22) |
| Exterior fire stair | not allowed if building height > 21.50 m (Art. 42(3), secondary source ⚠) |

### 5.7 Structure / seismic (TBDY 2018 [S3] ✓)
Design levels: DD-1 2 %/50 yr (2475-yr), DD-2 10 %/50 (475-yr), DD-3 50 %/50 (72-yr), DD-4 68 %/50 (43-yr) (§2.2). Ductile RC columns: min short side **300 mm** (rect.) / **350 mm** dia (circ.) (§7.3.1.1); long. steel 1 %–4 % of Ac, bars ≥ φ14 (§7.3.2.1). Beam web ≥ **250 mm** (§7.4.1.1a). Walls (perde) web thickness ≥ 250 mm and ≥ storey height/16 (§7.6.1.2a). Tunnel-form wall systems: ≥ 1/25 of wall length and ≥ 250 mm, basement perimeter walls ≥ 200 mm (§17.4.1.3; applicability to your system ⚠). Seismic hazard map: AFAD TDTH (Türkiye Deprem Tehlike Haritası) — spectral values by coordinates ⚠.

### 5.8 Electrical basics ⚠
230/400 V, 50 Hz, TT/TN earthing per Elektrik İç Tesisleri Yönetmeliği ⚠; RCD ≤ 30 mA on socket circuits ⚠; lightning rod mandatory for tall/pointed structures (Art. 27(2) ✓).

---
## 6. Permit drawing set
Typical dossier (⚠ practice; municipality checklist governs): İmar durumu + çap (parcel survey), vaziyet planı (site plan with setbacks and kotlar), bodrum/zemin/normal kat/çatı planları, ≥ 2 kesit (one through stair), 4 görünüş, statik proje + zemin etüdü (soil report), elektrik/mekanik/yangın tesisatı projeleri, yangın raporu (itfaiye approval for applicable buildings), sığınak projesi (if required), enerji kimlik belgesi (EKB), MAKS address, mimari proje müellifi taahhüt, yapı denetim sözleşmesi. Dijital: e-belediye/e-imar with PDF + DWG ⚠.

---
## 7. Common rejection reasons
1. Setbacks smaller than plan notes / Art. 23 defaults (5/3/3 m); +0.50 m rule for > 4 storeys forgotten.
2. Floor-to-floor height > 3.60 m (adds floor count → height violation).
3. Room below Art. 29 minima (living 12 m², bedroom 9 m², dimension 3.00/2.50 m).
4. Stair riser > 0.16 m without lift; common stair < 1.20 m; stair not daylit/not reaching roof/basement.
5. Lightwell/air-shaft undersized or shared by kitchen + room + WC.
6. Closed bay beyond 1.50 m or within 3.00 m of boundary.
7. Fire: stair enclosure not 120-min / door not 90-min, no fire-safety lobby for tall/high-rise, dead-end distances.
8. Missing lift shaft for 3-storey, lift at ≥ 4 storeys; lift car/landing undersized.
9. Emsal/TAKS counting errors (balconies, çıkma, basements counted/omitted incorrectly, Art. 21).
10. No accessibility ramp/WC per TS 9111; guard height < 1.10 m.


### Pre-submission checklist (Türkiye — verified numbers)
- [ ] İmar durumu read: TAKS, KAKS/emsal, Hmax or storey count, yard distances, plan notes.
- [ ] Yards: 5 / 3 / 3 m defaults; +0.50 m per storey above 4 on side and rear.
- [ ] Floor-to-floor <= 3.60 m (4.00 m for <= 3 storeys); clear height >= 2.60 m (2.20 m wet areas).
- [ ] Rooms: living 12 m² (3.00 m), bedroom 9 m² (2.50 m), kitchen 3.30 m², bath 3.00 m², WC 1.20 m².
- [ ] Common stair >= 1.20 m, riser <= 0.16 m (0.18 m with lift), tread >= 0.27 m, understair < 1.80 m closed.
- [ ] Lift shaft at 3 floors, lift at >= 4; car 1.20 x 1.80 m², door 0.90 m.
- [ ] Guard rail >= 1.10 m, openings <= 0.10 m; ramps per slope table; TS 9111 compliance.
- [ ] Closed bay <= 1.50 m, eaves <= 1.00 m, garden wall 0.50 m + 1.00 m railing.
- [ ] Fire: stair enclosure 120 min, doors 90 min, escape width by 50 cm units, high-rise > 21.50 m rules.
- [ ] Structure: TBDY 2018 ductile column >= 300 mm, beam web >= 250 mm, wall >= 250 mm.

---
## 8. Sources
- [S1] Planlı Alanlar İmar Yönetmeliği, consolidated to RG 1/7/2026-33297 — https://www.alomaliye.com/wp-content/uploads/2017/07/planli-alanlar-01-07-2026.pdf (read; also check https://www.mevzuat.gov.tr)
- [S2] Binaların Yangından Korunması Hakkında Yönetmelik (RG 19/12/2007-26735), doc 01/07/2025 — https://www.alomaliye.com/wp-content/uploads/2007/12/binalarin-yangindan-01-07-2025.doc ; index page https://www.alomaliye.com/2007/12/19/binalarin-yangindan-korunmasi/
- [S3] Türkiye Bina Deprem Yönetmeliği 2018 — intro https://www.resmigazete.gov.tr/eskiler/2018/03/20180318M1-2.htm ; annex PDF https://www.resmigazete.gov.tr/eskiler/2018/03/20180318M1-2-1.pdf
- [S6] ITU study on CAD standards in Türkiye — https://polen.itu.edu.tr/handle/11527/8335
- [S7] ÇŞİDB CADD standard — https://webdosya.csb.gov.tr/db/yapiisleri/editordosya/file/Cadd/CADD.pdf (TLS error, unread ⚠)
