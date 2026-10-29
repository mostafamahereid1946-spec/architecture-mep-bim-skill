# World index: building code families by country

## How to use
1. Find the country by name or ISO2 code in the regional tables below.
2. If the "Detail file" cell names a file, load that file first; it overrides this row.
3. `us.md`, `uk.md`, `qa.md`, `ae.md`, `sa.md`, `eg.md` are full guides; the other `<iso2>.md` names are planned or available national guides.
4. If a named detail file does not exist yet, fall back to this row (units, code basis, structural family, electrical basis).
5. Eurocode country: load the structure section of `uk.md` as the Eurocode guide, but warn that the National Annex differs (loads, partial factors, snow/wind/seismic maps).
6. IBC- or ACI-based country: load `us.md`, but warn that local amendments and local hazard maps replace the US ones.
7. BS-derived country: use `uk.md` for the BS-style conventions and warn that older BS editions often stay in force locally.
8. French-DTU country: use `fr.md` if present; otherwise use the Eurocode guide and warn about DTU/BAEL legacy practice.
9. Draw in the row's units; if "mixed", ask the user which unit system the drawing set should use.
10. Always ask for the city or municipality: local rules (zoning, setbacks, height, fire, seismic zone, energy) dominate national ones.
11. Always tell the user to confirm with the local authority; output is illustrative and is not stamped engineering.
12. A cell marked ⚠ is unverified: state the uncertainty and never present it as fact.
13. Entries such as Taiwan, Hong Kong, Kosovo and Palestine are listed for practical coverage only, with no political position implied.
14. Code editions change every few years: ask which edition the project is permitted under.
15. If this row, the detail file and the local authority disagree, the local authority wins, then the detail file, then this row.

## Code families

| Family | Meaning |
|---|---|
| ACI / IBC / ASCE | US-style: IBC or a national code referencing ASCE 7 loads and ACI 318 concrete, AISC steel; imperial origins, often metricised. |
| Eurocode+NA | EN 1990-1999 with a country-specific National Annex; building rules (fire, access, energy) stay national. |
| BS-derived | Former British-influence code set (BS 8110, BS 5950, BS 6399, BS 7671); often frozen at old editions. |
| French DTU-based | French technical-unit rules (DTU, BAEL, BPEL, PS92) inherited by Francophone states; shifting to Eurocodes. |
| Own national | A locally authored code that may borrow heavily from the above (e.g. NBC India, GB China, BSL Japan, NCC Australia, SNiP-derived CIS codes). |
| Electrical: IEC 60364 | Most of the world; national wiring rules transpose it (HD 60364 in Europe). |
| Electrical: NEC | NFPA 70 or a NEC-derived national code (Americas, Philippines, parts of the Gulf). |
| Electrical: BS 7671 | UK wiring regulations and the many Commonwealth and Gulf rules built on them. |

Notes: URL cells are authority or standards-body landing pages, not deep links; the Eurocodes portal with National Annex (NDP) data is https://eurocodes.jrc.ec.europa.eu. ⚠ = unverified. "Struct" = structural code family. "Elec" = electrical basis. Research was limited: ICC's own adoption list is region-by-region and partly dated, and no single current Eurocode National Annex status register was found, so many rows rest on general knowledge.

## Europe: EU members

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Austria | AT | metric | Eurocode+NA; OIB-Richtlinien under state building laws | Eurocode | IEC 60364 (ÖVE/ÖNORM E 8001) | OIB; Länder | https://www.oib.or.at | |
| Belgium | BE | metric | Eurocode+NA (NBN EN + ANB); regional building rules | Eurocode | IEC 60364 (AREI/RGIE) | Regions; NBN | https://www.nbn.be | |
| Bulgaria | BG | metric | Eurocode+NA; Spatial Development Act and ordinances | Eurocode | IEC 60364 | MRRB; BDS | ⚠ | |
| Croatia | HR | metric | Eurocode+NA (HRN EN); Building Act | Eurocode | IEC 60364 | Ministry of Spatial Planning; HZN | ⚠ | |
| Cyprus | CY | metric | Eurocode+NA; Streets and Buildings Regulation Law | Eurocode | IEC 60364 (BS 7671 legacy influence) | Interior Ministry; CYS | ⚠ | |
| Czechia | CZ | metric | Eurocode+NA (ČSN EN); Building Act | Eurocode | IEC 60364 (ČSN 33 2000) | MMR; ÚNMZ | https://www.unmz.gov.cz | |
| Denmark | DK | metric | Eurocode+NA (DS/EN); Bygningsreglement BR18 | Eurocode | IEC 60364 (DS/HD) | Trafik-, Bygge- og Boligstyrelsen | https://bygningsreglementet.dk | |
| Estonia | EE | metric | Eurocode+NA (EVS-EN); Building Code Act | Eurocode | IEC 60364 | Ministry of Economic Affairs | ⚠ | |
| Finland | FI | metric | Eurocode+NA (SFS-EN); National Building Code of Finland | Eurocode | IEC 60364 (SFS 6000) | Ministry of the Environment | https://ym.fi | |
| France | FR | metric | Eurocode+NA (NF EN); Code de la construction et de l'habitation; DTU for execution | Eurocode | IEC 60364 (NF C 15-100) | Ministry of Housing; AFNOR; CSTB | https://www.legifrance.gouv.fr | fr.md |
| Germany | DE | metric | Eurocode+NA (DIN EN + NA); MBO and 16 Landesbauordnungen | Eurocode | IEC 60364 (DIN VDE 0100) | DIBt; state ministries; DIN | https://www.dibt.de | de.md |
| Greece | GR | metric | Eurocode+NA (ELOT EN); EAK seismic code legacy; KENAK energy | Eurocode | IEC 60364 (ELOT HD 384) | Ministry of Environment (YPEN); ELOT | ⚠ | |
| Hungary | HU | metric | Eurocode+NA (MSZ EN); OTÉK/TÉKA building rules | Eurocode | IEC 60364 (MSZ HD 60364) | Ministry of Construction; MSZT | ⚠ | |
| Ireland | IE | metric | Eurocode+NA (IS EN); Building Regulations 2010 and Technical Guidance Documents | Eurocode | IEC 60364 (ETCI ET 101) | Dept of Housing; NSAI | https://www.gov.ie | |
| Italy | IT | metric | Own, Eurocode-based: NTC 2018 (Norme Tecniche per le Costruzioni); DPR 380/2001 | Eurocode | IEC 60364 (CEI 64-8) | MIT; Consiglio Superiore LL.PP.; UNI/CEI | https://www.mit.gov.it | it.md |
| Latvia | LV | metric | Eurocode+NA (LVS EN); Cabinet building regulations | Eurocode | IEC 60364 | Ministry of Economics; LVS | ⚠ | |
| Lithuania | LT | metric | Eurocode+NA (LST EN); STR technical regulations | Eurocode | IEC 60364 | Ministry of Environment; LST | ⚠ | |
| Luxembourg | LU | metric | Eurocode+NA (ILNAS); commune building regulations (PAG/PAP) | Eurocode | IEC 60364 | ITM; ILNAS | https://ilnas.public.lu | |
| Malta | MT | metric | Eurocode+NA (MSA); Technical Guidance Documents | Eurocode | IEC 60364 (BS 7671 legacy influence) | Building and Construction Authority; MCCAA | ⚠ | |
| Netherlands | NL | metric | Eurocode+NA (NEN-EN + NB); Bbl (Besluit bouwwerken leefomgeving) | Eurocode | IEC 60364 (NEN 1010) | Ministry of the Interior (BZK); NEN | https://www.nen.nl | |
| Poland | PL | metric | Eurocode+NA (PN-EN); Building Law and Warunki Techniczne | Eurocode | IEC 60364 (PN-HD 60364) | Ministry of Development; PKN | https://www.pkn.pl | |
| Portugal | PT | metric | Eurocode+NA (NP EN); RJUE, RGEU, REH/RECS | Eurocode | IEC 60364 (RTIEBT) | IMPIC; LNEC; IPQ | https://www.lnec.pt | |
| Romania | RO | metric | Eurocode+NA (SR EN); Law 10/1995; P100 seismic code | Eurocode | IEC 60364 (I7) | MDLPA; ASRO | ⚠ | |
| Slovakia | SK | metric | Eurocode+NA (STN EN); Building Act | Eurocode | IEC 60364 | Ministry of Transport and Construction; SUTN | ⚠ | |
| Slovenia | SI | metric | Eurocode+NA (SIST EN); Building Act (GZ) | Eurocode | IEC 60364 | Ministry of Natural Resources and Spatial Planning; SIST | ⚠ | |
| Spain | ES | metric | Own, Eurocode-aligned: Código Técnico de la Edificación (CTE, DB-SE); Código Estructural | Eurocode | IEC 60364 (REBT) | Ministry of Housing; UNE | https://www.codigotecnico.org | es.md |
| Sweden | SE | metric | Eurocode+NA (SS-EN); Boverket BBR and EKS | Eurocode | IEC 60364 (SS 436 40 00) | Boverket | https://www.boverket.se | |

## Europe: other states

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| United Kingdom | GB | metric (mixed in daily life) | BS-derived / Eurocode+NA: Building Regulations 2010 Approved Documents (England); Scotland, Wales, N. Ireland separate | Eurocode (BS EN + UK NA); BS legacy | BS 7671 | MHCLG; devolved governments; BSI | https://www.gov.uk/government/collections/approved-documents | uk.md |
| Norway | NO | metric | Eurocode+NA (NS-EN); TEK17 | Eurocode | IEC 60364 (NEK 400) | DiBK; Standards Norway | https://www.dibk.no | |
| Iceland | IS | metric | Eurocode+NA (IST EN); Building Regulation 112/2012 | Eurocode | IEC 60364 | HMS; Staðlaráð | ⚠ | |
| Switzerland | CH | metric | Eurocode-aligned SIA standards (SIA 260-267) with cantonal building laws | Eurocode (SIA) | IEC 60364 (NIN SN 411000) | SIA; cantons | https://www.sia.ch | |
| Liechtenstein | LI | metric | Swiss/EU mix; Baugesetz ⚠ | Eurocode ⚠ | IEC 60364 ⚠ | Amt für Bau und Infrastruktur | ⚠ | |
| Andorra | AD | metric | Spanish/French/Eurocode mix ⚠ | Eurocode ⚠ | IEC 60364 ⚠ | Govern d'Andorra; comú | ⚠ | |
| Monaco | MC | metric | French-influenced; Eurocodes ⚠ | Eurocode ⚠ | IEC 60364 (NF C 15-100) ⚠ | Département de l'Équipement | ⚠ | |
| San Marino | SM | metric | Italian NTC-influenced ⚠ | Eurocode ⚠ | IEC 60364 (CEI 64-8) ⚠ | Ufficio Urbanistica | ⚠ | |
| Albania | AL | metric | Eurocode+NA (SSH EN); old seismic code legacy ⚠ | Eurocode | IEC 60364 | Ministry of Infrastructure; DPS | ⚠ | |
| Bosnia and Herzegovina | BA | metric | Eurocode adoption in progress; entity-level building laws | Eurocode ⚠ | IEC 60364 | Entity ministries; BAS | ⚠ | |
| Montenegro | ME | metric | Eurocode+NA (MEST EN) | Eurocode | IEC 60364 | Ministry of Spatial Planning | ⚠ | |
| North Macedonia | MK | metric | Eurocode+NA (MKS EN); Law on Construction | Eurocode | IEC 60364 | Ministry of Transport and Communications; ISRSM | ⚠ | |
| Serbia | RS | metric | Eurocode+NA (SRPS EN); Law on Planning and Construction | Eurocode | IEC 60364 | Ministry of Construction; ISS | ⚠ | |
| Kosovo | XK | metric | Eurocode adoption ⚠ | Eurocode ⚠ | IEC 60364 ⚠ | Ministry of Environment and Spatial Planning | ⚠ | |
| Moldova | MD | metric | Eurocode adoption with NCM national norms | Eurocode ⚠ | IEC 60364 | MDED; Institutul de Standardizare | ⚠ | |
| Ukraine | UA | metric | Own: DBN with Eurocode adoption (DSTU-N B EN + NA) | Eurocode / own (SNiP legacy) | IEC 60364 (PUE legacy) | Ministry of Development; UkrNDNC | ⚠ | |
| Belarus | BY | metric | Own: TKP EN Eurocode adoption plus SNB norms | Eurocode (TKP EN) | IEC 60364 / TKP 339 ⚠ | Ministry of Architecture and Construction | ⚠ | |
| Russia | RU | metric | Own: SP/SNiP (Set of Rules) and GOST; Urban Planning Code | own (SNiP lineage) | own PUE (GOST R 50571 ≈ IEC 60364) | Ministry of Construction (Minstroy); Gosstandart | https://www.minstroyrf.gov.ru | |

## Caucasus and Central Asia

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Georgia | GE | metric | Own: Technical Regulations, SNiP legacy, Eurocode alignment ⚠ | own / Eurocode ⚠ | IEC 60364 ⚠ | Ministry of Regional Development | ⚠ | |
| Armenia | AM | metric | Own: RA Building Codes (SNiP-derived), Eurocode transition ⚠ | own (SNiP) | IEC / PUE ⚠ | Ministry of Territorial Administration | ⚠ | |
| Azerbaijan | AZ | metric | Own: AzDTN (SNiP-derived) | own (SNiP) | PUE / IEC ⚠ | State Committee for Urban Planning | ⚠ | |
| Kazakhstan | KZ | metric | Own: SP RK / SN RK, Eurocode-aligned with NA | Eurocode (SP RK EN) | IEC 60364 / PUE ⚠ | Ministry of Industry and Construction | ⚠ | |
| Uzbekistan | UZ | metric | Own: KMK/ShNK (SNiP-derived) | own (SNiP) | PUE / IEC ⚠ | Ministry of Construction | ⚠ | |
| Kyrgyzstan | KG | metric | Own: SNiP KR | own (SNiP) | PUE ⚠ | Gosstroy | ⚠ | |
| Tajikistan | TJ | metric | Own: MKS (SNiP-derived) | own (SNiP) | PUE ⚠ | Agency for Construction and Architecture | ⚠ | |
| Turkmenistan | TM | metric | Own: SNiP-derived ⚠ | own (SNiP) ⚠ | PUE ⚠ | Ministry of Construction | ⚠ | |

## Middle East

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Saudi Arabia | SA | metric | IBC-adopted: Saudi Building Code (SBC 201-1101) | ACI (ASCE 7 / ACI 318 via SBC 301) | NEC-derived (SBC 401) with SEC rules | SBC National Committee; MOMRAH | https://sbc.gov.sa | sa.md |
| United Arab Emirates | AE | metric | Mixed: Abu Dhabi ADIBC (IBC-based), Dubai Building Code (BS/IBC/ACI mix), Sharjah local | ACI / BS mixed | BS 7671-derived (DEWA/ADDC regulations) | Dubai Municipality; Abu Dhabi DMT | https://www.dm.gov.ae | ae.md |
| Qatar | QA | metric | Mixed: Qatar Construction Specifications and Qatar Building Code, BS/ACI/IBC mix | ACI / BS mixed | BS 7671-derived (Kahramaa) | Ministry of Municipality; Kahramaa | ⚠ | qa.md |
| Kuwait | KW | metric | Own: Kuwait Building Code (MPW), ACI/BS influence | ACI / BS mixed | BS 7671-derived (MEW) | Ministry of Public Works; MEW | ⚠ | kw.md |
| Oman | OM | metric | Own / mixed: building regulations with BS/ACI references ⚠ | BS / ACI mixed ⚠ | BS 7671-derived (Omani wiring regulations) | Ministry of Housing; MEDC | ⚠ | om.md |
| Bahrain | BH | metric | Own: Bahrain Building Regulations, BS/ACI/IBC mix ⚠ | BS / ACI mixed ⚠ | BS 7671-derived (EWA) | Ministry of Works / Municipalities | ⚠ | bh.md |
| Jordan | JO | metric | Own: Jordan National Building Code (JNBC) series | ACI / BS mixed | IEC 60364 / BS 7671 mix ⚠ | Housing and Urban Development Corp; Jordan Engineers Assoc. | ⚠ | jo.md |
| Iraq | IQ | metric | Own: Iraqi building code series, BS/ACI influence ⚠ | ACI / BS mixed ⚠ | BS 7671-derived ⚠ | Ministry of Construction, Housing, Municipalities | ⚠ | |
| Iran | IR | metric | Own: Iranian National Building Regulations (Mabhas) and Standard 2800 | own (ACI-derived) | own (Mabhas 13; IEC-aligned) | Ministry of Roads and Urban Development | ⚠ | |
| Israel | IL | metric | Own: Planning and Building Law; Israel Standards (SI 413 seismic, SI 466 concrete) | own (Eurocode-aligned) | own (SI 61, IEC-based) | Ministry of Housing; SII | https://www.sii.org.il | |
| Lebanon | LB | metric | Own: Building Law 646/2004; French/ACI/BS mix ⚠ | ACI / BS mixed ⚠ | French / IEC ⚠ | Order of Engineers; DGUP | ⚠ | |
| Syria | SY | metric | Own: Arab Syrian Code (ACI-derived) ⚠ | ACI ⚠ | IEC / French ⚠ | Ministry of Public Works and Housing | ⚠ | |
| Yemen | YE | metric | Own / ⚠: limited national code, BS/ACI practice | ⚠ | ⚠ | Ministry of Public Works | ⚠ | |
| Palestine | PS | metric | Own: Palestinian building code (Jordanian/ACI/Israeli influence) ⚠ | ACI / BS mixed ⚠ | IEC ⚠ | Ministry of Local Government; Palestine Standards Institution | ⚠ | |
| Turkey | TR | metric | Own: TBDY 2018 seismic, TS 500 / TS EN 1992 transition, Imar Law | own / Eurocode transition | IEC 60364 (TS HD 60364) | Ministry of Environment, Urbanisation (ÇŞİDB); AFAD; TSE | https://www.csb.gov.tr | tr.md |

## North Africa

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Egypt | EG | metric | Own: Egyptian Code of Practice ECP 201/203 (ACI-based), HBRC | ACI (ECP 203) | own (Egyptian Electrical Code; IEC-based) | HBRC; Ministry of Housing | https://hbrc.edu.eg | eg.md |
| Morocco | MA | metric | French DTU-based: RPS 2000 (seismic), BAEL legacy, Eurocode transition | French BAEL / Eurocode transition | IEC 60364 (NM; NF C 15-100 influence) | Ministry of Housing; IMANOR | ⚠ | ma.md |
| Algeria | DZ | metric | French DTU-based: DTR, RPA 99/2003, BAEL legacy | French BAEL / own | IEC 60364 (NF C 15-100 influence) | CGS; Ministry of Housing | ⚠ | |
| Tunisia | TN | metric | French DTU-based with Eurocode transition ⚠ | French / Eurocode ⚠ | IEC 60364 (NF C 15-100 influence) | Ministry of Equipment; INNORPI | ⚠ | |
| Libya | LY | metric | Own / ⚠: Libyan codes with Italian/BS/ACI influence | ⚠ | IEC ⚠ | Ministry of Housing | ⚠ | |
| Sudan | SD | metric | Own / ⚠: Sudanese Building Code, BS/Egyptian influence | BS ⚠ | BS 7671-derived ⚠ | Ministry of Infrastructure | ⚠ | |

## Sub-Saharan Africa: West and Central

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Nigeria | NG | metric | BS-derived: National Building Code 2006 | BS (Eurocode transition) | BS 7671-derived ⚠ | Ministry of Housing; SON; COREN | https://son.gov.ng | ng.md |
| Ghana | GH | metric | Mixed: Ghana Building Code (GS 1215:2018), partly IBC-based, BS legacy | BS / ACI mixed | BS 7671-derived | Ministry of Works and Housing; GSA | https://www.gsa.gov.gh | |
| Senegal | SN | metric | French DTU-based | French BAEL / Eurocode transition | IEC 60364 (NF C 15-100 influence) | Ministry of Urbanism, Housing | ⚠ | |
| Côte d'Ivoire | CI | metric | French DTU-based | French BAEL / Eurocode transition | IEC 60364 (NF C 15-100) | Ministry of Construction | ⚠ | |
| Mali | ML | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Housing | ⚠ | |
| Burkina Faso | BF | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Urban Planning | ⚠ | |
| Niger | NE | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Urban Planning | ⚠ | |
| Chad | TD | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Infrastructure | ⚠ | |
| Benin | BJ | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Housing | ⚠ | |
| Togo | TG | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Urban Planning | ⚠ | |
| Guinea | GN | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Urbanism | ⚠ | |
| Guinea-Bissau | GW | metric | Portuguese/French influence ⚠ | ⚠ | IEC ⚠ | ⚠ | ⚠ | |
| Sierra Leone | SL | mixed | BS-derived ⚠ | BS ⚠ | BS 7671-derived ⚠ | Ministry of Works | ⚠ | |
| Liberia | LR | mixed | IBC / US-influenced ⚠ | ACI ⚠ | NEC ⚠ | Ministry of Public Works | ⚠ | |
| Gambia | GM | metric | BS-derived ⚠ | BS ⚠ | BS 7671-derived ⚠ | Dept of Physical Planning | ⚠ | |
| Cabo Verde | CV | metric | Portuguese / Eurocode-based ⚠ | Eurocode ⚠ | IEC 60364 ⚠ | Ministry of Infrastructure | ⚠ | |
| Mauritania | MR | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Housing | ⚠ | |
| Cameroon | CM | metric | French DTU-based | French / Eurocode transition ⚠ | IEC / NF | Ministry of Housing and Urban Development | ⚠ | |
| Central African Republic | CF | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | ⚠ | ⚠ | |
| Gabon | GA | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Housing | ⚠ | |
| Republic of the Congo | CG | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | ⚠ | ⚠ | |
| DR Congo | CD | metric | Belgian/French influence ⚠ | French / Belgian ⚠ | IEC ⚠ | Ministry of Urbanism and Housing | ⚠ | |
| Equatorial Guinea | GQ | metric | Spanish/French influence ⚠ | ⚠ | IEC ⚠ | ⚠ | ⚠ | |
| Sao Tome and Principe | ST | metric | Portuguese-influenced ⚠ | ⚠ | IEC ⚠ | ⚠ | ⚠ | |
| Angola | AO | metric | Portuguese-influenced; Eurocode adoption ⚠ | Eurocode ⚠ | IEC 60364 ⚠ | Ministry of Construction | ⚠ | |

## Sub-Saharan Africa: East and Southern

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Ethiopia | ET | metric | Own: Ethiopian Building Code Standards (EBCS), Eurocode-derived | Eurocode-derived own | IEC ⚠ | Ministry of Urban Development | ⚠ | |
| Eritrea | ER | metric | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | |
| Djibouti | DJ | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | ⚠ | ⚠ | |
| Somalia | SO | metric | ⚠ no unified code; BS/Italian practice | ⚠ | ⚠ | ⚠ | ⚠ | |
| Kenya | KE | metric | BS-derived: Building Code 1968 (Adoptive By-laws), revision pending | BS (Eurocode transition) | BS 7671-derived ⚠ | Ministry of Lands and Housing; KEBS | https://www.kebs.org | |
| Uganda | UG | metric | BS-derived: Building Control Act 2013 | BS ⚠ | BS 7671-derived ⚠ | Ministry of Lands; UNBS | ⚠ | |
| Tanzania | TZ | metric | BS-derived ⚠ | BS ⚠ | BS 7671-derived ⚠ | Ministry of Works; TBS | ⚠ | |
| Rwanda | RW | metric | Own: Rwanda Building Code (Eurocode-based) | Eurocode | IEC 60364 ⚠ | Rwanda Housing Authority | ⚠ | |
| Burundi | BI | metric | French/Belgian influence ⚠ | French ⚠ | IEC ⚠ | ⚠ | ⚠ | |
| South Sudan | SS | metric | ⚠ no unified code | ⚠ | ⚠ | ⚠ | ⚠ | |
| South Africa | ZA | metric | Own: National Building Regulations (SANS 10400) | own (SANS 10100, SANS 10162; Eurocode partially) | own SANS 10142-1 (IEC-aligned) | NRCS; SABS | https://www.nrcs.org.za | za.md |
| Namibia | NA | metric | SANS-based with national regulations ⚠ | own (SANS) ⚠ | SANS 10142-1 ⚠ | Ministry of Urban and Rural Development | ⚠ | |
| Botswana | BW | metric | SANS / BS-derived ⚠ | SANS / BS ⚠ | SANS / BS ⚠ | Dept of Building Control | ⚠ | |
| Zimbabwe | ZW | metric | BS / SANS-derived ⚠ | BS / SANS ⚠ | SAZ / BS ⚠ | Local authorities; SAZ | ⚠ | |
| Zambia | ZM | metric | BS-derived ⚠ | BS ⚠ | BS 7671-derived ⚠ | Ministry of Housing; ZABS | ⚠ | |
| Malawi | MW | metric | BS-derived ⚠ | BS ⚠ | BS 7671-derived ⚠ | Ministry of Lands; MBS | ⚠ | |
| Mozambique | MZ | metric | Portuguese / SANS-influenced ⚠ | ⚠ | IEC ⚠ | ⚠ | ⚠ | |
| Lesotho | LS | metric | SANS / BS-derived ⚠ | SANS ⚠ | SANS ⚠ | ⚠ | ⚠ | |
| Eswatini | SZ | metric | SANS-derived ⚠ | SANS ⚠ | SANS ⚠ | ⚠ | ⚠ | |
| Madagascar | MG | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | Ministry of Land and Housing | ⚠ | |
| Mauritius | MU | metric | BS-derived with Eurocode adoption ⚠ | Eurocode / BS ⚠ | BS 7671-derived ⚠ | Ministry of National Infrastructure; MSB | ⚠ | |
| Seychelles | SC | metric | BS-derived ⚠ | BS ⚠ | BS 7671-derived ⚠ | Planning Authority | ⚠ | |
| Comoros | KM | metric | French DTU-based ⚠ | French ⚠ | IEC / NF ⚠ | ⚠ | ⚠ | |

## South Asia

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| India | IN | metric | Own: National Building Code of India 2016 plus IS codes (IS 456, IS 800, IS 1893) | own (IS; ACI/BS lineage) | own (IS 732 / National Electrical Code; IEC-influenced) | BIS; CPWD; state/municipal bodies | https://www.bis.gov.in | in.md |
| Pakistan | PK | metric | Own: Building Code of Pakistan (seismic provisions 2007, UBC-97-derived) | ACI / UBC | BS 7671 / IEC ⚠ | Pakistan Engineering Council; NHA | https://www.pec.org.pk | pk.md |
| Bangladesh | BD | metric | Own: BNBC 2020 (UBC/ACI-based) | ACI | IEC / BS ⚠ | HBRI; Ministry of Housing and Public Works | ⚠ | |
| Sri Lanka | LK | metric | BS-derived: UDA regulations, SLS standards | BS (Eurocode transition ⚠) | BS 7671-derived (SLS) | UDA; SLSI | https://www.slsi.lk | |
| Nepal | NP | metric | Own: Nepal National Building Code (NBC series, IS-derived) | own (IS-derived) | IEC / IS ⚠ | Dept of Urban Development and Building Construction | ⚠ | |
| Bhutan | BT | metric | Own: Bhutan Building Rules with IS influence ⚠ | own (IS) ⚠ | IEC / IS ⚠ | Dept of Human Settlement | ⚠ | |
| Maldives | MV | metric | Own: Maldives Building Code ⚠ | BS / IS ⚠ | BS 7671-derived ⚠ | Ministry of National Planning, Housing and Infrastructure | ⚠ | |
| Afghanistan | AF | metric | ICC/IBC-based working document with local practice ⚠ | ACI ⚠ | IEC / BS ⚠ | Ministry of Urban Development and Housing | ⚠ | |

## East Asia

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| China | CN | metric | Own: GB national standards (GB 50010 concrete, GB 50011 seismic, GB 50016 fire) | own (GB) | own (GB 50054; IEC-aligned) | MOHURD | https://www.mohurd.gov.cn | cn.md |
| Japan | JP | metric | Own: Building Standard Law (BSL) plus AIJ standards | own (BSL / AIJ) | own (Electrical Facilities Technical Standards; JIS C 60364 in part) | MLIT; AIJ | https://www.mlit.go.jp | jp.md |
| South Korea | KR | metric | Own: Korean Building Code (KBC) / KDS design standards, ACI/ASCE-derived | own (ACI/ASCE-derived) | own (KEC; IEC-aligned) | MOLIT; KCSC | https://www.kcsc.re.kr | |
| North Korea | KP | metric | ⚠ no public national code | ⚠ | ⚠ | ⚠ | ⚠ | |
| Mongolia | MN | metric | Own: BNbD (SNiP-derived) | own (SNiP) | PUE / IEC ⚠ | Ministry of Construction and Urban Development | ⚠ | |
| Taiwan | TW | metric | Own: Building Technical Regulations; seismic design code (ACI/UBC-derived) | own (ACI-derived) | own (Taiwan electrical installation rules; IEC/NEC influence) ⚠ | Ministry of the Interior (Construction and Planning Agency) | https://www.cpami.gov.tw | |
| Hong Kong | HK | metric | BS-derived: Buildings Ordinance (Cap. 123) and Building (Construction) Regulations; Code of Practice for Structural Use of Concrete 2013 | BS-derived own | IEC / BS 7671-derived (Code of Practice for the Electricity (Wiring) Regulations) | Buildings Department; EMSD | https://www.bd.gov.hk | |

## Southeast Asia

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Singapore | SG | metric | Eurocode+NA: Building Control Act, SS EN 1990-1999 with Singapore NAs | Eurocode | own SS 638 (IEC 60364-based) | BCA; Enterprise Singapore | https://www1.bca.gov.sg | sg.md |
| Malaysia | MY | metric | Own: UBBL 1984 with MS EN Eurocodes+NA | Eurocode (MS EN + NA) | own MS IEC 60364 / MS 1936 | JKR; CIDB; JPBD | https://www.cidb.gov.my | my.md |
| Indonesia | ID | metric | Own: Building Law and SNI (SNI 1726 seismic, SNI 2847 concrete ACI-based) | ACI / own (SNI) | own PUIL 2011 (IEC-based) | Ministry of Public Works (PUPR); BSN | https://pu.go.id | |
| Thailand | TH | metric | Own: Building Control Act and Ministerial Regulations; EIT/ACI practice | ACI | own (EIT; IEC-based) | Dept of Public Works and Town and Country Planning; EIT | ⚠ | |
| Vietnam | VN | metric | Own: QCVN 06 (fire), QCVN 03; TCVN design standards, Eurocode-influenced | own (TCVN; Eurocode/ACI mix) | own TCVN (IEC-based) | Ministry of Construction | ⚠ | |
| Philippines | PH | metric | Own: National Building Code PD 1096 and NSCP 2015 (ASCE/ACI-based) | ACI (NSCP) | NEC-derived (Philippine Electrical Code) | DPWH; PICE; PRC | https://www.dpwh.gov.ph | |
| Myanmar | MM | mixed | Own: Myanmar National Building Code 2016 (IBC/UBC-based) | ACI | BS / IEC mix ⚠ | Ministry of Construction; MES | ⚠ | |
| Cambodia | KH | metric | Own: Law on Construction; BS/ACI/Eurocode mix ⚠ | mixed ⚠ | IEC / BS ⚠ | Ministry of Land Management, Urban Planning and Construction | ⚠ | |
| Laos | LA | metric | Own / ⚠: Lao building code, Thai/Vietnamese influence | ⚠ | IEC ⚠ | Ministry of Public Works and Transport | ⚠ | |
| Brunei | BN | metric | BS-derived: Brunei building order ⚠ | BS ⚠ | BS 7671-derived ⚠ | Ministry of Development, Dept of Technical Services | ⚠ | |
| Timor-Leste | TL | metric | ⚠ limited code, Portuguese/Indonesian influence | ⚠ | IEC ⚠ | ⚠ | ⚠ | |

## Oceania

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Australia | AU | metric | Own: National Construction Code (NCC) with AS/NZS standards | own (AS 3600, AS 4100, AS 1170) | own (AS/NZS 3000, IEC-aligned) | ABCB; state regulators | https://ncc.abcb.gov.au | au.md |
| New Zealand | NZ | metric | Own: New Zealand Building Code (Building Act 2004) with NZS standards | own (NZS 3101, NZS 1170) | own (AS/NZS 3000) | MBIE | https://www.building.govt.nz | |
| Papua New Guinea | PG | metric | AS/NZS-derived National Building Act ⚠ | own (AS/NZS) ⚠ | AS/NZS 3000 ⚠ | Dept of Works | ⚠ | |
| Fiji | FJ | metric | Own: Fiji National Building Code (AS/NZS-based) ⚠ | own (AS/NZS) ⚠ | AS/NZS 3000 ⚠ | Dept of Town and Country Planning | ⚠ | |
| Solomon Islands | SB | metric | Pacific / AS-NZS-influenced ⚠ | ⚠ | AS/NZS ⚠ | ⚠ | ⚠ | |
| Vanuatu | VU | metric | Vanuatu National Building Code (AS/NZS-based) ⚠ | ⚠ | AS/NZS ⚠ | Dept of Public Works | ⚠ | |
| Samoa | WS | metric | Pacific / NZS-influenced ⚠ | ⚠ | AS/NZS ⚠ | MWTI | ⚠ | |
| Tonga | TO | metric | Pacific / NZS-influenced ⚠ | ⚠ | AS/NZS ⚠ | ⚠ | ⚠ | |
| Kiribati | KI | metric | Pacific / NZS-influenced ⚠ | ⚠ | AS/NZS ⚠ | ⚠ | ⚠ | |
| Tuvalu | TV | metric | Pacific / NZS-influenced ⚠ | ⚠ | AS/NZS ⚠ | ⚠ | ⚠ | |
| Nauru | NR | metric | ⚠ | ⚠ | AS/NZS ⚠ | ⚠ | ⚠ | |
| Micronesia | FM | mixed | IBC-influenced (US compact) ⚠ | ACI ⚠ | NEC ⚠ | ⚠ | ⚠ | |
| Marshall Islands | MH | mixed | IBC-influenced (US compact) ⚠ | ACI ⚠ | NEC ⚠ | ⚠ | ⚠ | |
| Palau | PW | mixed | IBC-influenced (US compact) ⚠ | ACI ⚠ | NEC ⚠ | ⚠ | ⚠ | |

## North and Central America

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| United States | US | imperial | IBC-adopted state/local codes (IBC, IRC) | ACI (ACI 318, ASCE 7, AISC) | NEC (NFPA 70) | ICC; state and local AHJs | https://codes.iccsafe.org | us.md |
| Canada | CA | metric | Own: National Building Code of Canada plus provincial codes | own (CSA A23.3, CSA S16) | own (CSA C22.1 Canadian Electrical Code) | NRC; provinces | https://nrc.canada.ca/en/certifications-evaluations-standards/codes-canada | ca.md |
| Mexico | MX | metric | Own: state/municipal reglamentos, Mexico City RCDF and NTC; CFE seismic manual | ACI-derived own | NEC-derived (NOM-001-SEDE) | CDMX SOBSE; CFE; state authorities | ⚠ | mx.md |
| Guatemala | GT | metric | Own: AGIES NSE norms (ACI/ASCE-based) | ACI | NEC / IEC mix ⚠ | AGIES; CONRED; municipalities | ⚠ | |
| Belize | BZ | mixed | Own / ⚠: Belize Building Act, IBC/BS influence | ACI / BS ⚠ | NEC / BS mix ⚠ | Dept of Housing and Urban Development | ⚠ | |
| Honduras | HN | metric | IBC-adopted basis: Código Hondureño de Construcción (CHOC-08) | ACI | NEC ⚠ | Colegio de Ingenieros Civiles | ⚠ | |
| El Salvador | SV | metric | Own: Reglamento para la Seguridad Estructural (ACI/UBC) | ACI | NEC ⚠ | MOP; VMVDU | ⚠ | |
| Nicaragua | NI | metric | Own: RNC-07 (ACI/UBC-based) | ACI | NEC ⚠ | MTI | ⚠ | |
| Costa Rica | CR | metric | Own: Código Sísmico de Costa Rica (CSCR) plus Ley de Construcciones | ACI / ASCE-based | NEC-derived (Código Eléctrico) | CFIA; municipalities | https://www.cfia.or.cr | |
| Panama | PA | mixed | Own: REP-2014 (ACI/IBC-based) | ACI | NEC | MIVIOT; JTIA | ⚠ | |

## Caribbean

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Cuba | CU | metric | Own: NC standards (NC 450 etc.) | own (ACI/Spanish lineage) | own (NC, IEC-based) | MICONS; ONN | ⚠ | |
| Dominican Republic | DO | metric | Own: Reglamentos R-001 etc. (ACI/ASCE-based) | ACI | NEC-derived | MOPC | ⚠ | |
| Haiti | HT | metric | Own: Code National du Bâtiment d'Haïti 2012 (IBC-based) | ACI | NEC / French mix ⚠ | MTPTC | ⚠ | |
| Jamaica | JM | mixed | IBC-adopted / CUBiC: Jamaica National Building Code (Caribbean Uniform Building Code basis) | ACI | NEC | Jamaica Bureau of Standards; local authorities | ⚠ | |
| Bahamas | BS | mixed | Own: Bahamas Building Code (IBC/Florida-influenced) ⚠ | ACI ⚠ | NEC ⚠ | Ministry of Works | ⚠ | |
| Barbados | BB | mixed | Own: CUBiC-based Barbados National Building Code ⚠ | ACI / BS ⚠ | BS 7671-derived ⚠ | Town and Country Development Planning Office | ⚠ | |
| Trinidad and Tobago | TT | mixed | Own: TTS 2016 National Building Code (CUBiC/IBC-based) ⚠ | ACI / BS ⚠ | BS 7671 / NEC ⚠ | Ministry of Planning; TTBS | ⚠ | |
| Antigua and Barbuda | AG | mixed | OECS Building Code (CUBiC lineage) | ACI / BS ⚠ | BS 7671-derived ⚠ | Development Control Authority | ⚠ | |
| Dominica | DM | mixed | OECS Building Code | ACI / BS ⚠ | BS 7671-derived ⚠ | Physical Planning Division | ⚠ | |
| Grenada | GD | mixed | OECS Building Code | ACI / BS ⚠ | BS 7671-derived ⚠ | Physical Planning Unit | ⚠ | |
| Saint Lucia | LC | mixed | OECS Building Code | ACI / BS ⚠ | BS 7671-derived ⚠ | Development Control Authority | ⚠ | |
| Saint Vincent and the Grenadines | VC | mixed | OECS Building Code | ACI / BS ⚠ | BS 7671-derived ⚠ | Physical Planning Unit | ⚠ | |
| Saint Kitts and Nevis | KN | mixed | OECS Building Code | ACI / BS ⚠ | BS 7671-derived ⚠ | Dept of Physical Planning | ⚠ | |

## South America

| Country | ISO2 | Units | Building code basis | Struct | Elec | Main authority | Official code source URL | Detail file |
|---|---|---|---|---|---|---|---|---|
| Brazil | BR | metric | Own: ABNT NBR standards (NBR 6118, 6120, 15575) plus municipal building codes | own (ABNT; Eurocode/ACI influence) | own NBR 5410 (IEC 60364-based) | ABNT; municipalities | https://www.abnt.org.br | br.md |
| Argentina | AR | metric | Own: CIRSOC / INPRES-CIRSOC (ACI-based) plus municipal codes | ACI-derived own | own AEA 90364 (IEC 60364-based) | INTI-CIRSOC; INPRES; AEA | https://www.inti.gob.ar | |
| Chile | CL | metric | Own: Ordenanza General de Urbanismo y Construcciones; NCh 430, NCh 433 | ACI-derived own | own NCh Elec 4 (IEC-based) | MINVU; INN; SEC | https://www.minvu.gob.cl | |
| Colombia | CO | metric | Own: NSR-10 (ACI/ASCE-based) | ACI | NEC-derived (RETIE, NTC 2050) | CIDAR; Ministerio de Vivienda; ICONTEC | ⚠ | |
| Peru | PE | metric | Own: Reglamento Nacional de Edificaciones (E.030, E.060) | ACI-derived own | NEC / IEC mix (CNE Utilización) | MVCS; SENCICO | https://www.gob.pe/sencico | |
| Ecuador | EC | metric | Own: NEC-15 Norma Ecuatoriana de la Construcción | ACI / ASCE-based | NEC-derived ⚠ | MIDUVI | ⚠ | |
| Venezuela | VE | metric | Own: COVENIN norms (COVENIN 1753 concrete, 1756 seismic) | ACI-derived own | NEC-derived (Código Eléctrico Nacional) | COVENIN-FONDONORMA; MPPHV | ⚠ | |
| Bolivia | BO | metric | Own: Norma Boliviana NB 1225001 (ACI) ⚠ | ACI ⚠ | IEC / NEC mix ⚠ | IBNORCA; ministry ⚠ | ⚠ | |
| Paraguay | PY | metric | Own / ⚠: municipal codes; ACI/INTN norms | ACI ⚠ | IEC ⚠ | INTN; municipalities | ⚠ | |
| Uruguay | UY | metric | Own: departmental building ordinances; UNIT standards | mixed ACI / Eurocode ⚠ | own UTE rules (IEC-based) ⚠ | UNIT; intendencias | ⚠ | |
| Guyana | GY | mixed | BS-derived: Guyana National Building Code ⚠ | BS ⚠ | BS 7671 / NEC ⚠ | Central Housing and Planning Authority | ⚠ | |
| Suriname | SR | metric | Dutch-influenced; ⚠ no unified code | ⚠ | IEC (Dutch NEN influence) ⚠ | ⚠ | ⚠ | |
