# MEP + Fire - Method Reference

Tags: **[RoT]** = rule of thumb (sanity check / early-stage only; replace with calculation); **[CODE]** = take from country file or governing standard; **⚠ verify** = unconfirmed. Units SI with imperial in brackets. 1 TR (ton refrigeration) = 3.517 kW = 12,000 Btu/h.

## 0. Common workflow (all MEP trades)

1. Collect: arch plans (RCP, sections, room names/uses), structure (beam depths), client brief (comfort, redundancy, budget), utility info, [CODE].
2. Concept: system choice, plant locations, risers/shafts, main routes -> agree space with architect.
3. Calculate: loads, flows, sizes.
4. Layout: floor plans in the order **plant -> risers -> mains -> branches -> terminals**.
5. Schematics: riser diagrams, single-line, P&ID-style flow diagram.
6. Schedules: equipment, panels, fixtures, valves.
7. Coordinate: Section 6 (clash rules), section lists.
8. Check: Section 8.

## 1. HVAC

### 1.1 Cooling load estimation
Exact method: heat balance / radiant time series (ASHRAE Fundamentals) or CIBSE admittance method, via software (HAP, TRACE, IES, Revit MEP). Components: envelope conduction (walls, roof, glass), solar through glazing (largest in hot climates), people (sensible ~70 W + latent ~45-55 W seated office; ~75+55 for light work ⚠ verify), lighting (W/m²), equipment, ventilation/infiltration load (often 20-35% in hot-humid), safety factor 5-10%.

Rules of thumb for hot climates (Gulf/Egypt), early-stage check only ⚠ verify against calculation:

| Space | Peak cooling W/m² floor | m² per TR [RoT] | Notes |
|---|---|---|---|
| Villa/house (insulated) | 100-160 | 22-35 | West/glazing sensitive |
| Apartment | 90-140 | 25-38 | |
| Office | 100-150 | 23-35 | +fresh air load |
| Retail/mall | 150-250 | 14-23 | High lighting & occupancy |
| Restaurant/dining | 250-400 | 9-14 | High occupancy + kitchen adjacency |
| Hotel room | 90-130 | 27-39 | |
| Hospital ward | 100-150 | 23-35 | OR/ICU higher, 100% OA |
| Data/server room | by equipment kW (+25% for losses) | - | N+1 precision cooling |
| Mosque/prayer hall | 150-250 ⚠ | - | Intermittent, high occupancy |
| Temperate climate (UK/N Europe office) | 60-100 | 35-58 | |

Quick estimate: total cooling kW = area x W/m²; TR = kW/3.517; supply air L/s ≈ sensible kW x ~85 L/s per kW (approx.); exact: V (L/s) = Q_sens (W) / (1.21 x ΔT K). At ΔT 10 K, ≈ 83 L/s per kW sensible [~ 400 cfm per TR]. Imperial: Btu/h = 1.08 x cfm x ΔT °F (sensible); total = 4.5 x cfm x Δh.
Design conditions: Gulf outdoor 46-48 °C DB, 28-29 °C WB (jurisdiction [CODE]); Egypt (Cairo) ~ 38-40 °C DB; indoor 22-24 °C ±1, RH 50-60% (20-24 °C ASHRAE 55 comfort 23-26 °C summer). Supply air temp 12-15 °C (ΔT 8-12 K) for comfort cooling; cold coil leaving air 11-13 °C with chilled water 6/12.

### 1.2 System types

| System | Typical capacity | Use | Pros/cons |
|---|---|---|---|
| Split (wall/cassette/floor/ducted) | 1-5 TR (up to 10+ ducted) | Villas, small shops | Low cost; one outdoor unit per indoor unit/multi; piping limits 15-30 m ⚠ per maker |
| Multi-split | 2-5 indoor per outdoor | Apartments | Fewer outdoor units |
| Packaged DX (rooftop/ducted) | 5-100 TR | Retail, warehouses | Less piping, higher maintenance on roof |
| VRF/VRV | 8-60 HP per outdoor module, >200 HP combined | Offices, hotels, apartments | Energy-efficient part-load, simultaneous heat/cool; refrigerant volume limits (EN 378/ASHRAE 15), max pipe length 150-200 m total, height difference 50-90 m ⚠ per maker |
| Chilled water + FCU | >150-250 TR plant | Hotels, towers, hospitals | Centralised; FCU 2-pipe/4-pipe, ceiling-concealed/cassette; chilled water pipework in ceiling |
| Chilled water + AHU | large zones, lobbies, atria | | Full fresh-air handling, filtration |
| District cooling (Gulf) | Plant by utility | Large developments | Energy transfer station (ETS) with plate heat exchangers; CW supply/return per utility ⚠ |
| Evaporative cooling | Dry climates only | Industrial | Not in humid Gulf coast |
| Heat pump / hydronic heating | Cold climates | Heating loads: 40-100 W/m² ⚠ | Check [CODE] |

Selection RoT: < ~100-150 TR (350-500 kW) -> DX/VRF; > ~200-300 TR -> chilled water central plant ⚠ verify; always weigh lifecycle cost.

Chilled water plant: air-cooled chillers (COP ≈ 2.8-3.5 at peak in Gulf ⚠) vs water-cooled (COP ≈ 5.0-6.5 ⚠) with cooling towers; N+1 redundancy; primary-secondary or variable primary flow; CHW 6/12 °C (ΔT 6 K; ΔT 7-8 for district cooling ⚠), CW 35-37/(30-32) in humid climates ⚠. Flow: L/s = kW / (4.19 x ΔT). For ΔT 6 K: 0.040 L/s per kW (0.14 m³/h per kW). US: gpm = tons x 24 / ΔT°F; e.g., ΔT 10 °F -> 2.4 gpm/ton.
Hot weather: coil sizing for latent loads; dehumidification; high ambient derating of condensers (outdoor units lose 15-25% capacity at 46 °C ⚠ select high-ambient models).

### 1.3 Fresh air and exhaust [RoT; CODE: ASHRAE 62.1, EN 16798/CIBSE Guide B, local]
| Space | Fresh air |
|---|---|
| Office | 2.5 L/s per person + 0.3 L/s/m² (≈ 5 cfm/p + 0.06 cfm/ft²) per ASHRAE 62.1 ⚠ verify edition; typical total 8-12 L/s/person |
| Residential | 0.35 ACH or ~7.5 L/s per person + area rate ⚠ |
| Toilets exhaust | 10-15 ACH [RoT] or 25 L/s per WC / 12.5 L/s urinal ⚠ [CODE]; total exhaust ~80-90% of supply where positive/negative pressure required |
| Kitchen (domestic) | 50 L/s intermittent extraction; commercial hood 0.25-0.5 m³/s per m of hood face + makeup air ~80-90% of exhaust |
| Car park | 6 ACH [RoT]; or 5-6 L/s·m² ⚠ [CODE]; with CO sensors; jet fans |
| Plant/electrical rooms | Heat removal: Q (W) / (1.21 x ΔT) ; typical 5-15 K allowable rise; transformers 1-2% losses |
| Generator room | Combustion + cooling air per maker (often 6-10 m³/s per MVA ⚠) |
| Smoke control | [CODE] (NFPA 92, EN 12101): stair pressurisation 25-50 Pa differential ⚠, pressure relief, 0.5-1 m/s door velocity |
Heat/energy recovery wheel for 100% OA units (hospitals, malls).

### 1.4 Duct sizing
Methods: **equal friction** (0.8-1.2 Pa/m, i.e., 0.1 in.wg/100 ft commonly), **velocity method** (maximum velocities for noise), **static regain** (large mains).

| Duct segment | Max velocity m/s (fpm) [RoT] |
|---|---|
| AHU discharge/main riser | 8-10 (1600-2000) |
| Main trunk (commercial) | 6-9 (1200-1800) |
| Branch | 4-6 (800-1200) |
| Final run to diffuser | 2-4 (400-800) |
| Residential main | 4-5 |
| Return main | 5-7 |
| Fresh-air intake louvre | 2.5 face velocity (500) |
| Exhaust louvre | 3-4 |
| Kitchen exhaust duct | 7.5-10 (1500-2000) min 7.5 for grease [CODE] |
| Toilet exhaust | 4-6 |
| Noise-critical (studio, library) | 2-3 |

- Rectangular equivalent circular diameter: De = 1.30 x (a x b)^0.625 / (a + b)^0.25 (equal friction).
- Aspect ratio ≤ 3:1 (max 4:1); limit duct depth by ceiling void (e.g., 250-400 under beams).
- Flow per diffuser sized by throw; branch balancing dampers (VCD) at each take-off; fire dampers where ducts cross rated walls/floors [CODE]; smoke dampers per smoke zone; flexible duct ≤ 1.5-3 m connecting to diffuser.
- Duct construction: galvanised sheet 0.6 mm (up to ~300 mm), 0.8 (to ~750), 1.0 (to ~1200), 1.2+ above ⚠ SMACNA by pressure class; insulation 25-50 mm foil-faced fibreglass/ PE (thickness for condensation); external ducts: aluminum-clad, weather protection. Pre-insulated PIR panel duct in some regions.
- Leakage class, support spacing [CODE]/SMACNA (typical ≤ 2.4-3.0 m).
- Pressure drop: fittings and equivalent lengths; fan total static = duct + coil (100-250 Pa) + filters (100-250 Pa) + diffusers (20-50 Pa) + safety 10%.

### 1.5 Diffusers and grilles [RoT]
- Ceiling supply diffuser 600x600 neck 250-300 -> ~50-120 L/s ⚠ per maker; neck velocity 2.5-4 m/s; NC 30-35 office, NC 25 bedrooms.
- Throw ≈ 0.7-1.0 x distance to wall (aim: terminal velocity 0.25 m/s at occupied zone).
- Spacing 1.5-3.0 m per diffuser, aligned with ceiling grid and symmetrical.
- Return grille face velocity 2-3 m/s; transfer grille; door undercut 20-25 mm for return air in bedrooms.
- Linear slot, swirl (high induction for VAV), displacement for cold rooms, jet nozzles for atria.
- Sizes in schedule: Mark | Type | Neck size | Airflow L/s | Max NC | Pressure drop | Finish.

### 1.6 Piping (chilled water/condenser/hot water)
- Velocity 1.0-2.0 m/s small pipes (≤ DN50) 1.2-2.4 m/s larger; friction 100-400 Pa/m ⚠ (≈ 1-4 ft w.g./100 ft). Use pipe-maker friction tables for final sizes.
- Insulation: closed-cell elastomeric 19-50 mm or PUF/phenolic with vapour barrier + cladding (aluminium/PVC) on roof/external.
- Drain: condensate slope ≥ 1:100 (1%), min 20 mm (3/4") per indoor unit, trap, run to floor drain/ riser; AC condensate must not drain onto walkways.
- Air vents at high points, drains at low points, isolation + balancing valves at risers, strainers, expansion tank, flexible connectors, thermometers/pressure gauges, BTU meters in apartments.
- Refrigerant piping: size per maker; oil traps in vertical risers > 4-6 m ⚠; brazed copper; leak testing.

### 1.7 Controls
Thermostats (wired/wireless), BMS/BAS points (BACnet/Modbus), VAV boxes, 2-way/3-way valves, VFD on fans/pumps, CO2 sensors for demand ventilation, fire alarm interface (AHU shutdown). Mount thermostat 1500 AFFL ⚠ typical, away from sun/diffusers.

### 1.8 HVAC drawing contents
Legend/abbreviations; equipment schedule (cooling capacity, airflow, ESP, power, electrical, weights); duct layout with sizes `W x H` (width first), flow L/s per run, diffuser tags; piping layout with sizes; plant room plan + sections; riser diagram; schematic (chilled water flow diagram with pumps, valves, chillers); toilet & kitchen extraction; car-park ventilation; stair pressurisation; control diagram; details (AHU/FCU connection, duct hanger, roof curb, louvre, fire damper, condensate drain); notes (insulation, testing, balancing, commissioning).

## 2. Plumbing and drainage

### 2.1 Water supply method
1. Demand estimate: fixture units (WSFU) or loading units (EN 806-3 LU) -> peak flow via Hunter curve / EN 806-3 formula.
2. Daily demand for storage: [RoT] residential 150-250 L/person/day (Gulf villas up to 300-500 ⚠), apartments 150-200, office 40-70 L/person/day (inc. toilets), hotels 250-500/room, hospitals 400-1000/bed, schools 30-60/pupil, restaurants 15-25/cover, mosques 20-40/person ⚠ verify [CODE/utility].
3. Storage: ground (underground/GL) tank sized ~ 1 day total (Gulf/Egypt practice [RoT: 24 h domestic + separate fire storage]) ⚠ verify; roof tank ~ 1/3-1/2 day if gravity distribution; booster set from GL tank when no roof tank (duty/standby VFD).
4. Pump head = static lift + friction + residual pressure at highest fixture (min 100 kPa, flush valve 100-170, shower mixer 100-150 ⚠) + safety.
5. Pipe size by velocity (supply 1.0-2.0 m/s, max ~2.4 m/s [CODE]) and friction (Hazen-Williams C = 140 for plastic/copper, 100-120 for old steel).
6. Zone: pressure reducing valves (PRV) when static pressure > 400-500 kPa (4-5 bar); high-rise zones ~ 30-40 m per zone ⚠.
7. Hot water: central or local storage heater (50-80 L per bathroom typical, 6-10 kW); solar heaters in ME; storage at ≥ 60 °C, distribute ≥ 50-55, return loop; demand 40-60 L/person/day (hot) [RoT]; thermal expansion vessel; pressure relief; scald protection at taps.
8. Cold supply: from public main -> meter -> backflow preventer -> GL tank (air gap) -> booster pump -> risers -> branch -> fixtures. Water supply materials: PPR, copper, CPVC, HDPE, stainless; ME common PPR (PN16-20).
9. Isolation valves per bathroom/riser; water hammer arrestors; water treatment (chlorination/UV) where required [CODE]; disinfection of tanks.

Typical WSFU/DFU values (IPC/UPC tables; ⚠ verify against current edition): lavatory 1 DFU, shower 2, bathtub 2, kitchen sink 2, WC (1.6 gpf) 3-4 DFU, floor drain 2-3; WSFU private: lav 0.5-1, shower 1.5-2, WC (tank) 2.5-3, sink 1.5. Public use is higher. 1 DFU ≈ 28 L/min (7.5 gpm) discharge ⚠.

### 2.2 Drainage method
- Separate: foul (soil+waste), storm/rainwater, subsoil; kitchen waste -> grease trap; car park/garage -> petrol interceptor.
- Each fixture trap seal 50-75 mm; trap size ≥ fixture outlet (lav 32-40 mm, bath/shower 40-50, sink 40-50, WC 100 (4"), floor drain 75-100).
- Branch slopes [RoT, CODE]: 1:40 (2.5%, 1/4"/ft) for ≤ 75 mm; 1:60-1:100 (1/8"-1/4"/ft) for ≥ 100 mm (US 1/8" per ft ok for ≥ 4"? ⚠); buried drains 100 mm ≥ 1:80 ⚠ (UK AD H), 150 mm ≥ 1:150 ⚠. Self-cleansing velocity 0.7-0.8 m/s min.
- Stack: 100 mm (4") for WC stack up to ~ 10-20 storeys depending on DFU; size from DFU table: 100 mm stack typical ≤ 160-256 DFU ⚠ verify; branch connection ≥ stack size; offsets avoided; no reduction downstream.
- Vent: one vent per fixture group; vent stack 50-75 mm (min 1/2 drain size; ≥ 32 mm), connects ≥ 150 mm above overflow level of highest fixture; terminate 0.3-0.6 m above roof (1+ m from openings, 3 m from air intakes ⚠ [CODE]); air admittance valves (AAV) where allowed; stack vent, relief vent for high rise; wet venting for bathroom groups.
- Max developed length for trap-to-vent (UPC/IPC Table: 40 mm (1.5") trap max trap-to-vent distance varies with size and slope ⚠ verify in table).
- Cleanouts at base of stacks, changes of direction > 45°, every 15-30 m on horizontal runs; rodding access; inspection chambers at junctions.
- Pumped drainage: sump + duplex submersible pumps for basement fixtures (sump ≥ 15-30 min retention ⚠), alarm, non-return valve, vent.
- External drainage: manholes at direction/gradient/diameter change, junctions, max spacing 30-45 m ⚠ [CODE]; invert levels; pipe uPVC/HDPE/ GRP / concrete; cover ≥ 0.9 m under traffic; benching in manholes; see civil-site.md for invert method.
- No public sewer: septic tank + soakaway/leaching field or holding tank (tanker pickup) common in ME/Egypt: septic volume ≈ 2-3 x daily flow, retention ≥ 24 h ⚠; soakaway sized from percolation test; tank access manhole 600x600 min; ventilation; 5-15 m separation from buildings/boundary and ≥ 30 m from wells ⚠ [CODE].
- Rainwater: Q (L/s) = C x i (mm/h) x A (m²) / 3600; typical design intensity 50-120 mm/h ⚠ by local data; roof drains 75-100 mm, secondary/emergency overflow; gutters sized by catchment; about 1 downpipe per 80-100 m² roof [RoT] ⚠; flat roof falls ≥ 1:80-1:100; scuppers for overflow.
- AC condensate, tank overflow, tank washout: indirect connection to drains (air break), drain visible.
- Fire-stopping and acoustic collars on plastic pipes through rated floors.

### 2.3 Tanks and pumps (common Gulf/Egypt arrangement)
Public main -> meter -> GL tank (cast RC, split in 2 cells, access manhole, vent, overflow 100 mm + level sensors, bund) -> booster pumps (duty/standby, VFD, hydropneumatic vessel) OR transfer pumps to roof tank -> gravity risers -> PRVs -> bathrooms. Roof tank with float valve, level control, overflow/warning pipe, vent screened, insulated/shaded lid to limit temperature rise (Gulf summer tank water 40-50 °C ⚠). Separate fire tank [CODE]. Pump room drain, 1-2 m clear access around pumps.
Pump power: P (kW) = ρ g Q H / η = 9.81 x Q (L/s) x H (m) / (1000 x η) with η = 0.5-0.7 [RoT].

### 2.4 Plumbing drawing contents
Legend; fixtures schedule; cold & hot water layouts (pipe size tags, valves), drainage layouts (pipe size, slope arrows, cleanouts, floor drains), vent layout, riser/isometric diagrams (single-line vertical, with sizes, valves, PRVs, tanks), roof drainage, plant room (tank, pump, calcs), external drainage layout (MH schedule with invert, cover, depth), details (WC/basin connection, floor drain, shower drain, cleanout, MH, septic, grease trap, thrust blocks, pipe hanger, sleeve through slab).

## 3. Electrical

### 3.1 Load estimate method
1. List connected loads by space (lighting W/m², small power W/m² or per socket, HVAC kW, motors, lifts, pumps, kitchens, special).
2. Apply demand/diversity factors per category and per board [CODE: BS 7671 App 1 / NEC 220 / IEC 60364].
3. Sum = maximum demand (kVA) = kW / pf (pf 0.85-0.9 before correction).
4. Add spare capacity 15-25% (future).
5. Choose transformer(s): kVA ≥ MD / (0.7-0.8 loading) -> standard sizes 500, 630, 800, 1000, 1250, 1600, 2000, 2500 kVA; generator (standby) sized on essential + starting loads (largest motor start 3-6x ⚠).

Typical design loads [RoT] ⚠ verify:
| Space | Lighting W/m² | Small power W/m² | Total incl. AC VA/m² (hot climate) |
|---|---|---|---|
| Villa | 8-12 | 10-20 | 120-200 |
| Apartment | 8-12 | 15-25 | 100-160 |
| Office | 8-12 | 20-30 | 150-250 |
| Retail | 15-30 | 20-40 | 200-300 |
| Hospital | 10-20 | 25-50 | 200-350 |
Rule: AC load typically 40-60% of building demand in hot climates.
Power: 1-ph kW = V x I x pf / 1000; 3-ph kW = √3 x V_L x I x pf / 1000, I = kW x 1000 / (√3 x V_L x pf x η).

### 3.2 Distribution architecture
Utility MV -> RMU/ring main -> MV/LV transformer(s) -> LV main switchboard (MDB/LVSB) -> sub-main switchboards -> distribution boards (DBs) per floor/zone/apartment -> final circuits. Metering at utility connection point and per tenant. Essential/emergency board with ATS from standby generator; UPS for critical (IT, life safety). Power factor correction (cap bank 0.95+ target; detuned reactors where harmonics). Riser: busbar trunking or cables in vertical shaft; segregated from plumbing risers.
Voltage: 230/400 V 50 Hz (UK/EU/most ME and Egypt 220/380 V ⚠ verify), 120/208 or 277/480 V 60 Hz (US).

### 3.3 Circuits and protection (BS 7671 / IEC style; US NEC equivalents in brackets)
| Circuit | Typical MCB | Cable (Cu, 70 °C PVC) | Notes |
|---|---|---|---|
| Lighting | 6-10 A (B/C curve) | 1.5 mm² | ≤ ~10-12 points / circuit [RoT]; (US: 15 A 14 AWG) |
| Sockets radial | 16-20 A | 2.5 mm² | ≤ 6-10 sockets/ circuit RoT (UK ring 32 A 2.5 mm²) |
| AC split unit (1-2 TR) | 16-32 A | 2.5-4 mm² | Dedicated circuit with isolator near outdoor unit |
| Water heater | 16-20 A | 2.5-4 mm² | with DP switch |
| Cooker/oven | 32-40 A | 6-10 mm² | |
| Motors | per start type | per FLC x 1.25 | DOL/star-delta/VFD |
| Feeders to DB | MCCB | per calc | |
- Protective device ratings: In ≥ Ib; Iz ≥ In; I2 ≤ 1.45 Iz (BS 7671). Curves: B (3-5 x In, resistive), C (5-10 x In, general/motor), D (10-20 x In, high inrush).
- RCD/RCBO 30 mA on sockets and wet areas; 100/300 mA at distribution; type A/AC/B per load [CODE].
- Phase balance across L1/L2/L3 within ~10% ⚠; limit single-phase to per utility rules ⚠.

### 3.4 Cable sizing method (stepwise)
1. **Design current** Ib (1-ph) = P / (V x pf); (3-ph) = P / (√3 x V_L x pf x η).
2. Select protective device In ≥ Ib (MCB/MCCB).
3. Required tabulated current I_t = In / (Ca x Cg x Ci x Cd...) where Ca ambient temp factor, Cg grouping, Ci thermal insulation, Cd depth for buried. Hot climate reference: for PVC at ambient 40 °C Ca ≈ 0.87, 45 °C ≈ 0.79, 50 °C ≈ 0.71 (ref 30 °C) ⚠ verify BS 7671 Table 4B1; US NEC 310.15(B)(1) 75/90 °C columns.
4. Choose cable size from current rating tables (installation method: conduit, tray, trunking, buried) with I_z ≥ I_t.
5. **Voltage drop**: ΔV = (mV/A/m x Ib x L)/1000; limit [CODE] e.g. BS 7671: 3% lighting, 5% other (from origin), 5-6% total at utilisation in many ME utilities ⚠ ; US NEC recommends 3% branch, 5% total.
6. **Short-circuit thermal withstand**: S ≥ √(I²t)/k (k = 115 for PVC Cu, 143 XLPE Cu); check fault level at the cable origin, disconnection time.
7. **Earth fault loop impedance** Zs ≤ limit so protective device trips within 0.4 s (final circuits ≤ 32 A) / 5 s (distribution); depends on EF loop and cable CPC.
8. Specify cable type: XLPE/SWA/PVC (armoured) for mains, FP200/MICC for fire life-safety, LSZH in escape routes.
Fault level estimate at transformer secondary: I_sc ≈ S_kVA / (√3 x V_L(kV) x Z%) e.g., 1000 kVA, 400 V, Z = 5%: 1000 / (1.732 x 0.4 x 0.05) ≈ 28.9 kA (infinite source). Typical LV board ratings 50 kA/1s.

### 3.5 Lighting design
Lumen method: N = (E x A) / (Φ x UF x MF) where E lux, A m², Φ lamp/luminaire lumens, UF 0.4-0.7 (room index, reflectances), MF 0.7-0.85. Verify with DIALux/Relux. Typical LED luminaire efficacy 90-130 lm/W; LPD target 5-9 W/m² in offices [CODE energy: ASHRAE 90.1/Part L/Estidama etc.].

Illuminance [RoT, from EN 12464-1 / CIBSE SLL / IES; verify local]:
| Space | Maintained lux |
|---|---|
| Corridors, lift lobbies | 100 |
| Stairs | 150 |
| WC | 200 |
| Living/bedroom | 100-200 (general) |
| Kitchen (domestic) | 300 (500 worktop) |
| Office/desk | 500 |
| Reception | 300 |
| Meeting room | 500 |
| Retail | 300-750 |
| Plant room | 200 |
| Parking | 75 (ramp 75-150) |
| Classroom | 300-500 |
| Hospital ward/exam | 100-200 / 500 |
| Server room | 500 |
| Emergency escape route | ≥ 1 lux centre line (open area ≥ 0.5 lux) for 1-3 hr per [CODE] (US 90 min / 1 fc avg; EN 1838 1 lux, BS 5266 3 hr ⚠ verify) |
Provide emergency/exit signs at doors, stairs, and changes of direction; maintained vs non-maintained; central battery or self-contained; test switch.
Controls: switches 1100-1400 AFFL (1200 common ⚠), occupancy sensors, dimming, daylight sensors, scene control in hotels/villas.
Mounting heights: sockets 300-450 (general) /1100-1200 above counters/ 150-300 for floor sockets; TV 1000-1700 ⚠; AC isolator ~1800-2000; DB top ≤ 1800-2000; fire-alarm MCP 1200-1400 ⚠.

### 3.6 Earthing and lightning protection
- System earthing types: TN-S, TN-C-S (PME), TT, IT, TN-C; utility determines. Main earth terminal (MET), main equipotential bonding of water, gas, steel, HVAC; supplementary bonding in bathrooms [CODE].
- Earth electrode: copper rod/plate/ring, resistance targets ≤ 1-5 Ω for LV/substations; ≤ 10 Ω lightning ⚠ verify [CODE]; test pits with inspection chamber; earth bar sizes.
- Lightning protection: risk assessment per IEC 62305 / NFPA 780 / BS EN 62305; air terminals, down conductors (spacing 10-20 m ⚠ by protection level), earth rings, SPD Type 1/2/3 at MDB and sub-boards.
- Surge protection and EMC for ELV/IT.

### 3.7 Single-line diagram content
Utility incoming (voltage, fault level) -> transformer (kVA, vector group Dyn11, impedance %, tap) -> LV main breaker (type, rating A, breaking kA) -> busbar rating (A, kA) -> outgoing feeders (MCCB rating, cable size/length/type) -> ATS/generator (kVA) -> sub-boards -> DBs; metering (CTs, kWh), PFC bank (kVAr), UPS (kVA, autonomy), SPD, earthing symbol, protection relays/trip settings, loads (kW), tags (MSB, SMDB, DB-GF-01). Each DB: name, location, ratings (A, kA), outgoing circuits.

### 3.8 Panel / DB schedule columns
Circuit no. | Phase (L1/L2/L3) | MCB/RCBO rating, curve, poles | Cable size/type | Load description (e.g., "Lighting - Bed 1") | Connected load W | Diversity | Remarks; totals per phase W/A, imbalance %. Include main breaker, RCD, SPD, spare ways (15-25%).

### 3.9 Low current / ELV systems
- Structured cabling: Cat6/Cat6A permanent link ≤ 90 m (channel 100 m); rack in comms room (cooling, power, floor loading, ≥ 1.2 front clearance); backbone fibre OM3/OM4/OS2; data outlet count 2/workstation + 20% spare.
- Telephone/PBX, TV/MATV/IPTV, CCTV (camera coverage + NVR storage), access control, intercom/video door phone (villas, apartments), PA/VA & emergency voice, BMS, nurse call, parking guidance, AV in meeting rooms.
- Segregation: power vs data parallel ≥ 50 mm-300 mm depending on shielding ⚠ [CODE EN 50174-2].
- Containment: cable trays (perforated/ladder), trunking, conduit (PVC 20/25/32 mm); fill ≤ 40% ⚠; separate trays for power, ELV, fire alarm; fire-rated conduits for life safety.
- Fire alarm cable: fire-resistant (FP200, MICC). See section 5.
- Show on drawings: outlet symbols with tag (D=data, T=tel, TV), rack elevation, riser diagram, device schedule, containment routes.

### 3.10 Electrical drawing set
Legend/notes; lighting layout (fitting tags, circuit numbers, switches, emergency lighting); small power layout; AC power layout; DB schedules; single-line (MV/LV); riser diagram; load schedule/calculation; earthing & lightning protection layout; ELV layouts (data/tel, CCTV, access, TV); substation/room layouts & sections; lighting fixture schedule; details (mounting heights, bonding, trench, pole bases); external lighting.

## 4. Fire protection (design only - [CODE] governs: NFPA 13/14/20/72, BS EN 12845, BS 5839, EN 54, local civil defence)

### 4.1 Sprinklers
Hazard class (NFPA 13): Light (offices, hospitals, residential, churches), Ordinary Group 1 (parking, laundries, restaurants service), Ordinary Group 2 (retail, light manufacturing), Extra Group 1/2 (flammable liquids, plastics), special storage. BS EN 12845: LH, OH1-OH4, HHP, HHS.

Typical design criteria (NFPA 13 density/area curve points ⚠ verify):
| Hazard | Density mm/min (gpm/ft²) | Design area m² (ft²) | Max coverage per sprinkler m² (ft²) | Max spacing m (ft) | Hose allowance L/min (gpm) | Duration min |
|---|---|---|---|---|---|---|
| Light | 4.1 (0.10) | 139 (1500) | 20.9 (225) [up to 18.6/200 std] | 4.6 (15) | 380 (100) | 30 |
| Ordinary 1 | 6.1 (0.15) | 139 (1500) | 12.1 (130) | 4.6 (15) | 380-950 (100-250) | 60-90 |
| Ordinary 2 | 8.1 (0.20) | 139 (1500) | 12.1 (130) | 4.6 (15) | 950 (250) | 60-90 |
| Extra 1 | 12.2 (0.30) | 232 (2500) | 9.3 (100) | 3.7 (12) | 1900 (500) | 90-120 |
| Extra 2 | 16.3 (0.40) | 232 (2500) | 9.3 (100) | 3.7 (12) | 1900 (500) | 90-120 |
BS EN 12845: LH 2.25 mm/min over 84 m² (max 21 m²/sprinkler, 4.6 m); OH1 5 mm/min/72 m²; OH2 5/144; OH3 5/216; OH4 5/360 (max 12 m², 4.0 m) ⚠ verify.

Layout rules [RoT/typical]: standard spray K = 5.6 (80 L/min/bar^0.5); min operating pressure 0.5 bar (7 psi); temperature ratings 57 °C (orange), 68 °C (red, ordinary), 79 °C (yellow), 93 °C (green, near heat sources/roof spaces in hot climates ⚠); deflector 25-300 mm below ceiling (standard pendent); keep ≥ 450 mm clear below sprinkler (storage), obstructions: ducts/ trays > 1.2 m wide get sprinklers beneath; min spacing between sprinklers 1.8-2.4 m (avoid cold soldering); max distance from wall ½ spacing (≤ 2.3 m), min from wall 100 mm; sidewall heads in corridors/small rooms; concealed heads in finished ceilings; protect void spaces if combustible; no sprinklers needed in some small bathrooms/ elec rooms depending on [CODE]. Dry/pre-action systems in unheated/ data rooms; wet in general.
Hydraulics: pipe schedule (small/low hazard) or hydraulic calc: Hazen-Williams p = 6.05 x 10^5 x Q^1.85 / (C^1.85 x d^4.87) (p bar/m, Q L/min, d mm); C = 120 black steel wet, 140-150 plastic/copper/stainless ⚠ verify; typical riser sizing velocity ≤ 6 m/s (20 fps); typical sizes DN25 ending, DN32-DN50 branches, DN80-DN150 mains.
Water supply: tank volume = demand flow x duration (e.g., OH1 ~ 1000 L/min x 60 min = 60 m³ incl. hose) ⚠; pumps: electric main + diesel standby (or two electrics) + jockey; NFPA 20 pump curves: 150% flow at ≥ 65% pressure, shutoff ≤ 140% rated; siamese FDC; alarm valve + flow switch + tamper switch per floor/zone; test and drain at each riser.

### 4.2 Standpipes, hose reels, hydrants, extinguishers
- Standpipe Class I (65 mm / 2.5" fire dept valves), Class II (40 mm / 1.5" hose station), Class III (both) [NFPA 14]. Flow typically 500 gpm (1900 L/min) first riser + 250 gpm (950 L/min) each additional up to 1000-1250 gpm; residual 100 psi (6.9 bar) at hydraulically most remote 65 mm outlet (65 psi at 40 mm Class II) ⚠ verify; hose valves in stair enclosures/landings; standpipe riser ≥ DN100 (DN150 for tall) ⚠.
- Hose reels (EN 671, NFPA 14 Class II ): 19-25 mm hose, 30 m long, flow ≥ 0.33-0.4 L/s ⚠ at 2-6 bar; spacing so all points ≤ 6 m beyond hose reach (reach ~30 m hose + ~6 m jet) [RoT]; cabinet height 1.0-1.3 m above floor; located at exits/stairs.
- Hydrants: spacing ≤ 90-150 m along roads, within 100-150 m of building entrance ⚠ [CODE]; flow 1000-1500 L/min; 2.5" outlets; fire department connection near road.
- Extinguishers: ABC dry powder (6-9 kg) general, CO2 (2-5 kg) electrical/server, foam/water (9 L) class A/B, wet chemical class K kitchens; max travel distance to extinguisher 15-23 m ⚠ (NFPA 10: 75 ft class A); at least one per ~200-250 m² per floor (BS 5306-8: 1 per 200 m²) ⚠; mount top at ≤ 1.2-1.5 m, heavy > 18 kg lower ⚠; clearly signed; one per floor min, near exits.
- Clean agent / inert gas (FM-200, Novec 1230, IG-541) for server/ control rooms: room volume + leakage + discharge pressure relief; abort/hold buttons.
- Kitchen hood: wet chemical system.

### 4.3 Fire alarm and detection
System: addressable panel (FACP) -> loop (2 wires, ~125-250 devices per loop typical ⚠) -> detectors, manual call points (MCP), sounders/strobes, interface modules (door holders, AHU shutdown, lift recall, damper release, sprinkler flow/tamper, fire pump status, access release, smoke control, PA/VA); battery 24 h standby + 30 min alarm (BS 5839: 24-72 h ⚠) [CODE]; remote monitoring/civil defence connection.
Detector selection: optical smoke (general), ionisation (largely phased out), heat (fixed 57-78 °C/ rate of rise: kitchens, car parks, garages, plant rooms), multi-sensor, beam (atria, warehouses), aspirating VESDA (data/ clean rooms), flame detectors (hangars), CO detectors; duct detectors in AHU; linear heat cable.
Spacing method (spot, flat ceiling ≤ ~10 m ⚠):
| Standard | Smoke | Heat |
|---|---|---|
| BS 5839-1 / EN 54-14 | radius 7.5 m (~110 m² per detector) ⚠ | radius 5.3 m (A1 grade, ~50 m²) |
| NFPA 72 | listed spacing nominal 9.1 m (30 ft); all points within 0.7 x S (6.4 m) | listed spacing 15 m (50 ft) for 3 m ceilings ⚠ |
| Wall distance | ≥ 0.5 m (0.1 m min in corridors ≤ 3 m wide) ⚠ | |
Adjust for ceiling height (derate spacing above ~10 m for heat), beams (>10% of ceiling height compartments), HVAC diffusers (≥ 1 m ⚠), sloped ceiling. Provide detectors in ceiling void and floor void if deeper than a code threshold (~800 mm typical) ⚠ [CODE], lift lobbies, stairs, corridors, plant rooms, electrical rooms; no smoke detectors in kitchens/bathrooms (use heat).
MCPs: at each exit/stair, travel to nearest ≤ 45 m (BS 5839) / 61 m (200 ft NFPA 72) ⚠, 1.2-1.4 m above floor ⚠ [CODE]; no more than 1.5 m horizontally from exit door (NFPA 72 uses ~5 ft) ⚠.
Sounders: ≥ 65 dB(A) or 5 dB above ambient; ≥ 75 dB(A) at bed heads; NFPA 72: 15 dB above ambient / 10 dB above max; visual strobes in public areas/ accessible [CODE]. Voice alarm (EVAC) for high-rise/ assembly.
Zones: BS 5839 zone ≤ 2000 m² per floor, search distance ≤ 60 m; every stair separate zone; addressable shows each device.
Cabling: fire-rated, FP200/MICC; shielded twisted pair; segregate from power; labelled red conduit.

### 4.4 Passive/ other coordination
Fire-rated walls/doors from architect; fire dampers where ducts cross rated barriers; fire-stopping of pipe/cable penetrations; smoke control & stair pressurisation fans on emergency power; refuge areas; firefighting lift power; emergency lighting & exit signs; fire pump room accessible from outside, 2-hr rated, drainage, ventilation.

### 4.5 Fire drawings
Legend; sprinkler layout with head type/temp/K, pipe sizes, zone/riser, flow switches; hydraulic calc sheet; riser diagram; fire pump room layout + schematic; tank room; hose reel/standpipe riser & layout; extinguisher & hydrant locations; fire alarm layout with device tags (SD, HD, MCP, S/B), loop/zone schematic; riser; panel location/schedule; gas suppression/ kitchen; smoke control; cause & effect matrix.

## 5. Symbols and abbreviations legend (minimum list)

**Line types:** CHWS/CHWR chilled water supply/return; CWS/CWR condenser water; HWS/HWR heating hot water; REF refrigerant (liquid/suction); COND condensate drain; DCW/DHW domestic cold/hot water; PW potable; SW soil/waste (SOL/WST); VP vent; RWP rainwater pipe; ST storm; SP sprinkler; FH fire hydrant; FW fire water; HR hose reel; GAS; (H)VAC ducts: supply/return/exhaust/fresh air (arrows + SA/RA/EA/OA).

**HVAC:** supply diffuser (square with X), return grille (square with diagonal), linear slot, VCD volume control damper, FD fire damper, SD smoke damper, FSD combined, MD motorised damper, flex duct (zig-zag), AHU, FCU, VAV, split indoor/outdoor, thermostat T, sensor, silencer, louvre, fan (circle with blades), inline fan, access door AD, turning vanes.

**Plumbing:** gate valve, ball valve, check valve, globe valve, butterfly, PRV, strainer, balancing valve (BV), flow meter, water meter, pressure gauge PG, thermometer, air vent AV, drain cock, hose bib HB, floor drain FD, floor trap FT, cleanout CO, roof drain RD, manhole MH, inspection chamber IC, pump (circle with triangle), tank, water heater, backflow preventer BFP, expansion vessel.

**Electrical:** lighting types (circle with cross; downlight; linear; wall; emergency "E"; exit sign running man), switch S/S2/S3 (1/2/3-gang), dimmer, socket (single/double 13 A), TV/data/tel outlets, isolator/FCU (switch fused), DB/MDB (rectangle), transformer, generator G, motor M, ATS, UPS, CT, kWh meter, earth bar, earth pit, lightning air terminal, junction box JB, cable tray, conduit.

**Fire:** smoke detector SD (circle with S), heat detector HD, MCP (square with red), sounder/strobe, FACP, sprinkler pendent/upright/sidewall (circle with cross/ triangle), alarm valve, flow switch FS, tamper switch TS, riser, FDC, extinguisher FE (triangle/ circle), hose reel HR, hydrant FH, exit/emergency light, fire damper FD.

Symbol standards: IEC 60617, IEEE 315 / ANSI Y32.9, ASHRAE 134, ISO 14617, NFPA 170 (fire), ISO 7010 (safety signs). Pick one standard and include a legend; do not mix.
Colours (typical CAD conventions, not mandatory): HVAC ducts blue, CHW green/cyan, drainage brown, water supply cyan, fire red, electrical yellow, ELV magenta/orange.

## 6. MEP coordination rules

**Priority ("who moves"):** (1) structure, (2) gravity pipes (drainage, condensate with slope, storm), (3) large ducts (hardest to move), (4) fire sprinkler mains (fixed hydraulics), (5) pressure pipes (chilled water, domestic), (6) cable trays/ busbar, (7) conduits, ELV, (8) small items (flex ducts, drops). Pipe/duct that can bend or offset yields to one that cannot.

**Space budget:** services zone above ceiling [RoT] = largest duct depth + insulation 50 + hanger/slab clearance 100 + ceiling depth 50-100 + light fittings 100 (+ sprinkler drop 100). Typically 400-800 mm in offices. Drainage falls: 1:100 over 20 m = 200 mm; sprinkler branch slope ≥ 1:250-1:500 ⚠ (dry/pre-action 1:250-1:500).

**Layering convention (top to bottom):** structure -> large ducts -> chilled water pipes/ sprinkler mains -> cable trays -> light fittings/ diffusers -> ceiling; avoid crossing layers; lights at ceiling plane.

**Clearances:** 50-100 mm between services (excluding insulation), 150-300 to structure for hangers/access; electrical switchgear front clearance 1000 mm (NEC 110.26: 0.9-1.2 m depending on voltage ⚠), rear/side 600-800; plant maintenance access 600-1000 mm each side; coil withdrawal space = coil length; AHU filter withdrawal; tank clear space 600-1000; pump room clear 1 m; lift machine room.

**Do/Don't:** no wet services (pipes, ducts with condensation, sprinklers) over electrical/ELV rooms or switchboards; no pipes in lift shafts; keep power/ELV segregated; keep chilled water pipes below ducts to avoid dripping; don't run pipes through beams/columns without sleeve approval; provide access panels at valves, dampers, FCUs, JBs, cleanouts; all penetrations through rated walls sleeved/sealed; risers have fire-stopped slab openings and drain points; insulation thickness included in clash model.

**Penetrations:** MEP supplies sleeve/opening schedule (location, size, level, element); structural approval for beams/slabs; slab openings > 300 mm require trimmer; no openings within 150-300 of columns/supports ⚠; beam holes per structural.md.

**Shafts/risers:** HVAC/plumbing/electrical/ELV/fire each get dedicated shafts or segregated compartments (power separated from water); shaft sizes: plumbing 600x600-800x1000; electrical riser 600x1200 per ~4-6 floors loads; ELV 600x600; HVAC duct riser per airflow (4-6 m/s, plus insulation). Align vertically; access doors every floor, fire-rated.

**Equipment rooms:** locations near load centre; transformer/switchgear on ground/basement with ventilation, access path for removal (1.5-2.4 m doors), cable trenches; generator exhaust and fuel; chillers on roof or plant level with weight/slab; cooling towers with air flow clearance (clearances per maker) ⚠; tanks and pumps at basement/ground.

**Clash classes:** hard (physical intersection) -> must be resolved; soft (clearance/maintenance zone violated) -> check; workflow/4D (sequence). Process: model coordination by BIM (Revit + Navisworks), weekly clash meetings, resolution log with owner and date, issue coordinated "composite" drawings; signing off ceiling height at critical areas (corridors, plant, ramp entrance).

## 7. Drawing set lists (sheet prefixes: M = mechanical/HVAC, P = plumbing, E = electrical, FP = fire protection, FA = fire alarm; UK often uses numeric 5xx/6xx)

| Set | Sheets |
|---|---|
| **M** HVAC | M-000 notes, legend, abbreviations, design conditions, load summary; M-001 equipment schedule(s); M-1xx floor plans HVAC (duct + piping + equipment per floor); M-2xx roof/plant plan; M-3xx sections; M-4xx riser/schematics (chilled water flow diagram, duct riser, control); M-5xx details; M-6xx schedules (diffusers, FCU, AHU, fans, pumps, valves) |
| **P** Plumbing | P-000 notes, legend, fixture schedule; P-1xx water supply (cold/hot); P-2xx drainage + vent; P-3xx roof drainage; P-4xx riser diagrams/isometrics; P-5xx plant rooms (tanks/pumps), details; P-6xx schedules; external drainage/water network sheets (cross-ref civil C-xxx) |
| **E** Electrical | E-000 notes, legend, abbreviations; E-001 single line diagram; E-002 DB schedules; E-1xx lighting plans; E-2xx power plans; E-3xx AC/equipment power; E-4xx ELV (data, TV, CCTV, access, intercom, PA); E-5xx earthing + lightning protection; E-6xx room layouts (substation, genset), sections; E-7xx details; E-8xx schedules (luminaires, load calcs, cable) |
| **FP** Fire | FP-000 notes, legend; FP-1xx sprinkler layouts; FP-2xx standpipe/hose reel/extinguisher layouts; FP-3xx pump room + tanks; FP-4xx riser diagrams; FP-5xx details; FP-6xx hydraulic calcs; FA-1xx alarm layouts; FA-2xx riser/loop schematic; FA-3xx panel schedule, cause-effect |

## 8. Checklist (pre-issue)
- Design basis page present (codes, conditions, loads, standards) and equipment schedules complete with electrical data.
- Loads reconciled: HVAC electrical load -> electrical load schedule; pumps, lifts, fans included; transformer/gen sizing agrees.
- Riser positions match arch shafts on every floor; riser diagrams match plan counts.
- All sleeves and openings submitted to structure; ceiling heights verified at corridors/clash spots.
- Drainage has slopes, cleanouts, vents, trap seals; pump sumps have alarms; invert levels continuous.
- Cable/busbar sizes pass current/VD/fault; DB phase balance; spare capacity; labelling.
- Fire: sprinkler coverage per hazard, hydraulic calc present, alarm coverage + cause and effect + interfaces; fire dampers shown at rated walls.
- Symbols/legend consistent; scales and sheet numbers; revision cloud.
- Maintenance access shown for equipment; no wet over electrical; plant room clearances.
- Testing/commissioning notes (air balance, pressure test, insulation resistance, flush & disinfect, hydro test 1.5x operating or 14 bar for 2 h for sprinklers ⚠ verify).
