"""Parametric shopping-mall generator: one dxf_plan.py plan spec per level + mall.json.

Usage (stdlib only):
    uv run -q scripts/gen_mall.py --country qa --out examples/malls/qa [--levels 2] [--plot 120x90]
Writes <out>/GF.json, <out>/L1.json (... L2) in mm - the spec format of dxf_plan.py,
plan_audit.py, ifc_from_spec.py (GF also carries "roofs" + "massing" for max_massing.py) -
and <out>/mall.json (summary, every rule with source + warning flag, travel-distance results).
An extra top-level key "mall" (room rectangles, door points, voids) is ignored by those scripts
and read by mep_overlay.py.

Layout (plan, south = plot front/street):
  service corridor | shop row 21.0 m | mall street 12.0 m + atrium | shop row 21.0 m | service corridor
  grid 8.4 m along the street; anchor stores (2 bays x full depth) at both street ends; south entrance
  lobby (full depth, lifts flanking the doors) opening onto the street at the atrium bays; escape-stair
  cores (stair + exit passage + riser rooms) full depth; north row centre = loading bay, MDB/fire pump,
  AHU/generator, WC + prayer blocks; L1 = same footprint, food court over the lobby, atrium void.

Design numbers are rules of thumb [RoT] unless the COUNTRY table cites a references/countries/<cc>.md
section; "warn" True = the source marks the number (verify) or the number is an assumption.
Egress: travel distance is measured to the nearest exit = final exit door or protected-stair door,
along the walking path (shortest path around the atrium void, rooms treated as open plan).
Greedy: starts with 2 stair cores (SW, NE) and adds cores until max travel <= country limit.
"""
import argparse
import datetime
import heapq
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
G = 8400                      # structural bay along the street [RoT: retail 7.5-9 m, disciplines/structural.md 3]
DS, DH, WST = 4200, 21000, 12000   # service corridor, shop depth (18-25 m), mall street (10-12 m) [RoT]
VOID_WALK = 3000              # L1 walkway left each side of the atrium void [RoT]
UP_H = 4500                   # upper floor-to-floor [RoT]
MUSLIM = {"qa", "ae", "sa", "kw", "om", "bh", "jo", "ma", "eg", "tr", "my", "pk"}
EN_SPRINKLER = {"uk", "de", "fr", "es", "it"}   # EN 12845 family; others NFPA 13 (mep.md 4.1)

# ------------------------------------------------------------------ country rules
D_TRAVEL = (45.0, "default 45 m sprinklered - number not in country file (verify with authority)", True)
D_SETB = (5000, 3000, 3000, "ASSUMED 5/3/3 m - no commercial-zone setbacks in country file", True)
D_PARK = (25.0, "rule of thumb 4 bays per 100 m2 GLA", True)
D_STAIR = (1200, "rule of thumb 1200 mm clear", True)
D_GFH = (5000, "rule of thumb 4.5-5.5 m GF floor-to-floor", True)

CITY = {  # name, lat, lon, tz (render sun, 21 March)
    "ae": ("Dubai", 25.20, 55.27, 4), "au": ("Sydney", -33.87, 151.21, 11), "bh": ("Manama", 26.23, 50.59, 3),
    "br": ("Sao Paulo", -23.55, -46.63, -3), "ca": ("Toronto", 43.65, -79.38, -4), "cn": ("Shanghai", 31.23, 121.47, 8),
    "de": ("Frankfurt", 50.11, 8.68, 1), "eg": ("Cairo", 30.04, 31.24, 2), "es": ("Madrid", 40.42, -3.70, 1),
    "fr": ("Paris", 48.86, 2.35, 1), "in": ("Mumbai", 19.08, 72.88, 5.5), "it": ("Milan", 45.46, 9.19, 1),
    "jo": ("Amman", 31.95, 35.93, 3), "jp": ("Tokyo", 35.68, 139.69, 9), "kw": ("Kuwait City", 29.38, 47.99, 3),
    "ma": ("Casablanca", 33.57, -7.59, 1), "mx": ("Mexico City", 19.43, -99.13, -6), "my": ("Kuala Lumpur", 3.14, 101.69, 8),
    "ng": ("Lagos", 6.52, 3.38, 1), "om": ("Muscat", 23.59, 58.41, 4), "pk": ("Karachi", 24.86, 67.01, 5),
    "qa": ("Doha", 25.29, 51.53, 3), "sa": ("Riyadh", 24.71, 46.68, 3), "sg": ("Singapore", 1.35, 103.82, 8),
    "tr": ("Istanbul", 41.01, 28.98, 3), "uk": ("London", 51.51, -0.13, 0), "us": ("Houston", 29.76, -95.37, -5),
    "za": ("Johannesburg", -26.20, 28.05, 2),
}
OVERRIDES = {   # only numbers a country file states; (value, source, warn)
    "qa": dict(travel=(76.0, "qa.md 5.4 'other areas -> exit' 76 m sprinklered (parsed from table layout)", True),
               stair=(1200, "qa.md 5.4 corridor serving >50 persons >= 1200 mm", False)),
    "ae": dict(setb=(0, 3000, 3000, "ae.md 5.1 DBC Table B.1: 3 m from neighbour, 0 m road side", False),
               stair=(1200, "ae.md 5.3 stair clear width 1200 mm (DBC B.6)", False)),
    "sa": dict(travel=(76.0, "sa.md 5.5 SBC 201 R-2 sprinklered 76 m (B 91 m); mercantile not listed, IBC M 250 ft per us.md 5.3", True),
               park=(45.0, "sa.md 5.6 shops 1 bay per 45 m2, min 1 per shop", False),
               stair=(1118, "sa.md 5.5 stairs 1118 mm (>=50 occupants)", True)),
    "om": dict(gfh=(4800, "om.md 5 residential-commercial ground floor internal height 4.0-4.8 m (max used)", False)),
    "bh": dict(park=(50.0, "bh.md 5.4 commercial/services 2 bays per 100 m2 (Art. 13, 20)", False)),
    "tr": dict(setb=(5000, 3000, 3000, "tr.md 5.1 Imar Yonetmeligi Art. 23 defaults 5/3/3 m", False),
               gfh=(4500, "tr.md 5 commercial zone ground storey height 4.50 m", False)),
    "my": dict(travel=(60.0, "my.md 5 UBBL 188 assembly 60 m sprinklered; Seventh Schedule (shops) not read", True)),
    "de": dict(travel=(35.0, "de.md 5 MBO 35(2): any point of a room to stair/outside <= 35 m", False),
               stair=(1000, "de.md 5 stair clear width >= 1.00 m", False)),
    "fr": dict(stair=(1200, "fr.md 5 ERP art. 7-1 stairs >= 1.20 m between handrails", False)),
    "es": dict(travel=(50.0, "es.md 5 DB-SI 3 Tabla 3.1: 50 m with more than one exit", True)),
    "it": dict(stair=(1200, "it.md 5 common stairs >= 1.20 m", False)),
    "uk": dict(travel=(45.0, "uk.md 5.2 AD B Table 2.1 shops, more than one direction 45 m", True),
               stair=(1000, "uk.md 5.2 escape stair >= 1000 mm", True)),
    "us": dict(travel=(76.2, "us.md 5.3 IBC Table 1017.2 M sprinklered 250 ft", True),
               stair=(1118, "us.md 5.3 IBC 1011.2 commercial stair 44 in", False),
               park=(23.2, "us.md 5.5 retail 1 per 250 sq ft", True)),
    "in": dict(travel=(45.0, "in.md 5 IS 16550 summary 45 m sprinklered (NBC Part 4 residential figure 30 m conflicts - verify)", True),
               park=(100.0, "in.md 5 1 ECS per ~100 m2 built-up", True)),
    "mx": dict(travel=(60.0, "mx.md 5 Art. 92: 40 m medium risk +50 % with sprinklers (risk class assumed medium)", True)),
    "au": dict(travel=(40.0, "au.md 5 max 40 m to alternate exits (apartment figure from memory)", True)),
    "jp": dict(travel=(50.0, "jp.md 5 Ord. 120: 50 m (fire-resistive main structure)", False),
               cov=(80.0, "jp.md 5 coverage ratio commercial 8/10 (Law 53(1))"),
               stair=(1400, "jp.md 5 Ord. 23(1): shops > 1500 m2 stair width 140 cm", False)),
    "br": dict(stair=(1200, "br.md 5.2 minimum exit width 1.20 m (PR NPT 011 / SP IT-11)", False)),
}


def country_rules(cc):
    o = OVERRIDES.get(cc, {})
    return dict(travel=o.get("travel", D_TRAVEL), setb=o.get("setb", D_SETB), park=o.get("park", D_PARK),
                stair=o.get("stair", D_STAIR), gfh=o.get("gfh", D_GFH), cov=o.get("cov"))


# ------------------------------------------------------------------ names (en, ar). Arabic avoids words that
# plan_audit treats as habitable (غرفة, صالة, مجلس, ...) and keeps digits out of Arabic text.
NM = {
    "shop": ("SHOP", "محل تجاري"), "anchor": ("ANCHOR STORE", "المتجر الرئيسي"),
    "street0": ("MALL STREET & ATRIUM", "الممشى الرئيسي والأتريوم"),
    "street1": ("MALL STREET & FOOD COURT", "الممشى الرئيسي وساحة المطاعم"),
    "streetn": ("MALL STREET", "الممشى الرئيسي"),
    "corr": ("SERVICE CORRIDOR", "ممر الخدمة"), "stair": ("ESCAPE STAIR", "درج الهروب"),
    "passage": ("PASSAGE", "ممر الهروب"), "riser_e": ("ELEC RISER", "مجرى كهرباء"),
    "riser_m": ("MECH RISER", "مجرى ميكانيكا"), "elec": ("MDB", "لوحة التوزيع"),
    "firepump": ("FIRE PUMP", "مضخات الحريق"), "ahu": ("AHU PLANT", "محطة التكييف"),
    "gen": ("GEN SET", "المولد"), "load": ("LOADING BAY", "ساحة التحميل والنفايات"),
    "amen": ("LINK", "ممر"), "wcm": ("MEN WC", "دورة مياه الرجال"),
    "wcw": ("WOMEN WC", "دورة مياه النساء"), "wca": ("ACCESS WC", "دورة مياه"),
    "prm": ("PRAYER M", "مصلى الرجال"), "prw": ("PRAYER W", "مصلى النساء"),
    "baby": ("BABY CARE", "رعاية الأطفال"), "aid": ("FIRST AID", "إسعافات أولية"),
    "lift": ("LIFTS", "مصاعد"), "food": ("FOOD UNIT", "محل مأكولات"),
}
THROUGH = {"street", "corr", "passage", "amen"}
NOOCC = {"stair", "riser", "lift"}        # not sampled for travel distance
FIRE_RATED = {"stair", "passage", "riser", "lift", "load", "elec", "firepump", "ahu", "gen", "anchor"}
AMEN = {"amen", "wc", "prayer", "baby"}


# ------------------------------------------------------------------ geometry helpers
def seg_hits(p, q, r, eps=1.0):
    """True if segment p-q passes through the open interior of rect r (shrunk by eps)."""
    x0, y0, x1, y1 = r[0] + eps, r[1] + eps, r[2] - eps, r[3] - eps
    if x0 >= x1 or y0 >= y1:
        return False
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pp == 0:
            if qq <= 0:
                return False
        else:
            t = qq / pp
            if pp < 0:
                if t > t1:
                    return False
                t0 = max(t0, t)
            else:
                if t < t0:
                    return False
                t1 = min(t1, t)
    return t0 < t1 - 1e-9


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


class Region:
    """Walkable region = union of rects minus obstacle rects; geodesic distance by visibility graph."""

    def __init__(self, rects, obstacles=()):
        self.rects = [tuple(r) for r in rects]
        self.obs = [tuple(o) for o in obstacles]
        xs = sorted({v for r in self.rects for v in (r[0], r[2])} | {v for o in self.obs for v in (o[0], o[2])})
        ys = sorted({v for r in self.rects for v in (r[1], r[3])} | {v for o in self.obs for v in (o[1], o[3])})
        self.xs, self.ys = xs, ys

        def inside(x, y):
            if any(o[0] < x < o[2] and o[1] < y < o[3] for o in self.obs):
                return False
            return any(r[0] < x < r[2] and r[1] < y < r[3] for r in self.rects)

        self.cells = {}
        self.out = []
        for i in range(len(xs) - 1):
            for j in range(len(ys) - 1):
                cx, cy = (xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2
                ok = inside(cx, cy)
                self.cells[(i, j)] = ok
                if not ok:
                    self.out.append((xs[i], ys[j], xs[i + 1], ys[j + 1]))
        self.corners = []
        for i in range(1, len(xs) - 1):
            for j in range(1, len(ys) - 1):
                n = sum(self.cells.get(k, False) for k in ((i - 1, j - 1), (i, j - 1), (i - 1, j), (i, j)))
                if n == 3:
                    self.corners.append((xs[i], ys[j]))
        n = len(self.corners)
        self.apsp = [[math.inf] * n for _ in range(n)]
        for a in range(n):
            self.apsp[a][a] = 0.0
            for b in range(a + 1, n):
                if self.visible(self.corners[a], self.corners[b]):
                    self.apsp[a][b] = self.apsp[b][a] = dist(self.corners[a], self.corners[b])
        for k in range(n):
            for a in range(n):
                for b in range(n):
                    if self.apsp[a][k] + self.apsp[k][b] < self.apsp[a][b]:
                        self.apsp[a][b] = self.apsp[a][k] + self.apsp[k][b]

    def visible(self, p, q):
        return not any(seg_hits(p, q, o) for o in self.out)

    def geo(self, p, q):
        if not self.out or self.visible(p, q):
            return dist(p, q)
        vp = [(dist(p, c), a) for a, c in enumerate(self.corners) if self.visible(p, c)]
        vq = [(dist(q, c), b) for b, c in enumerate(self.corners) if self.visible(q, c)]
        best = math.inf
        for dp, a in vp:
            for dq, b in vq:
                best = min(best, dp + self.apsp[a][b] + dq)
        return best

    def samples(self, step=3000, inset=200):
        pts = set()
        for (i, j), ok in self.cells.items():
            if not ok:
                continue
            x0, x1, y0, y1 = self.xs[i] + inset, self.xs[i + 1] - inset, self.ys[j] + inset, self.ys[j + 1] - inset
            if x0 > x1 or y0 > y1:
                continue
            nx, ny = max(1, math.ceil((x1 - x0) / step)), max(1, math.ceil((y1 - y0) / step))
            for a in range(nx + 1):
                for b in range(ny + 1):
                    pts.add((x0 + (x1 - x0) * a / nx, y0 + (y1 - y0) * b / ny))
        return sorted(pts)


# ------------------------------------------------------------------ level layout
class Plan:
    """Rooms (id, name, kind, rects) and door requests for one level; coordinates absolute mm."""

    def __init__(self, cfg, lv):
        self.cfg, self.lv = cfg, lv
        self.rooms, self.doors, self.wins = {}, [], []
        self.n = 0

    def room(self, rid, kind, rects, name=None, name_ar=None, sub=None):
        en, ar = NM[sub or kind]
        self.rooms[rid] = dict(id=rid, kind=kind, sub=sub or kind, rects=[tuple(r) for r in rects],
                               name=name or en, name_ar=name_ar or ar)
        return rid

    def door(self, a, b, o, coord, c, w, swing, double=False, exit=False, tag=True):
        self.doors.append(dict(a=a, b=b, o=o, coord=coord, c=c, w=w, swing=swing, double=double, exit=exit, tag=tag))

    def win(self, o, coord, a, b, room=None):
        if b - a >= 600:
            self.wins.append(dict(o=o, coord=coord, a=a, b=b))


def assign_bays(n, extra):
    lw = 3 if n % 2 else 2
    c0 = (n - lw) // 2
    s, nn = ["shop"] * n, ["shop"] * n
    for i in range(c0, c0 + lw):
        s[i] = "lobby"
    s[0] = "core"
    nn[n - 1] = "core"
    mid = (n - 1) / 2
    order = [i for i in sorted(range(n), key=lambda i: (abs(i - mid), i)) if nn[i] == "shop"]
    kinds = ["load", "plantA", "plantB", "amen"] + (["amen"] if n >= 9 else [])
    for k, i in zip(kinds, order):
        nn[i] = k
    for side, i in extra:
        (s if side == "s" else nn)[i] = "core"
    return s, nn, lw, c0


def build_plan(cfg, lv, bays):
    """Rooms + door requests for level index lv (0 = GF)."""
    P = Plan(cfg, lv)
    n, A = cfg["n"], cfg["A"]
    bx0, by0 = cfg["bx0"], cfg["by0"]
    xW = bx0 + A * G
    xE = xW + n * G
    bx1 = xE + A * G
    Y0 = by0
    ys0, ys1, ys2 = Y0 + DS, Y0 + DS + DH, Y0 + DS + DH + WST
    yn1, Y1 = ys2 + DH, ys2 + DH + DS
    X = lambda i: xW + i * G
    s_types, n_types, lw, c0 = bays
    lx0, lx1 = X(c0), X(c0 + lw)
    P.geo = dict(xW=xW, xE=xE, bx1=bx1, Y0=Y0, ys0=ys0, ys1=ys1, ys2=ys2, yn1=yn1, Y1=Y1, lx0=lx0, lx1=lx1)
    rowinfo = {"s": dict(ext=Y0, cb=ys0, st=ys1, sg=-1, types=s_types),
               "n": dict(ext=Y1, cb=yn1, st=ys2, sg=+1, types=n_types)}

    def zy(side, a, b):   # y-range between distances a..b measured from the street edge into the row
        r = rowinfo[side]
        y1, y2 = r["st"] + r["sg"] * a, r["st"] + r["sg"] * b
        return (min(y1, y2), max(y1, y2))

    def rect_y(x0, x1, side, a, b):
        lo, hi = zy(side, a, b)
        return (x0, lo, x1, hi)

    # ---- street (+ lobby)
    st_rects = [(xW, ys1, xE, ys2)]
    lobby = []
    lw3 = 3000
    R1 = (lx0, Y0 + 6000, lx1, ys1)
    R3w, R3e = (lx0, Y0 + 4200, lx0 + lw3, Y0 + 6000), (lx1 - lw3, Y0 + 4200, lx1, Y0 + 6000)
    R2 = (lx0 + lw3, Y0, lx1 - lw3, Y0 + 6000)
    st_rects += [R1, R3w, R3e]
    food = lv == 1
    if not food:
        st_rects.append(R2)
    sub = "street0" if lv == 0 else "street1" if lv == 1 else "streetn"
    P.room("ST", "street", st_rects, sub=sub)
    P.room("LFW", "lift", [(lx0, Y0, lx0 + lw3, Y0 + 4200)])
    P.room("LFE", "lift", [(lx1 - lw3, Y0, lx1, Y0 + 4200)])
    P.door("LFW", "ST", "h", Y0 + 4200, lx0 + lw3 / 2, 1200, "ST")
    P.door("LFE", "ST", "h", Y0 + 4200, lx1 - lw3 / 2, 1200, "ST")
    cxl = (lx0 + lx1) / 2
    if not food:
        for dx in (-3600, 3600):
            P.door("ST", "OUT", "h", Y0, cxl + dx, 2200, "OUT", double=True, exit=True)
        P.win("h", Y0, lx0 + lw3 + 600, cxl - 4700 - 300)
        P.win("h", Y0, cxl - 2500 + 300, cxl + 2500 - 300)
        P.win("h", Y0, cxl + 4700 + 300, lx1 - lw3 - 600)
    else:
        P.food_units = []
        for k in range(4):
            fx0 = lx0 + lw3 + k * 4800
            rid = f"FU{k + 1}"
            P.room(rid, "food", [(fx0, Y0, fx0 + 4800, Y0 + 6000)], name=f"FOOD {k + 1:02d}")
            P.door(rid, "ST", "h", Y0 + 6000, fx0 + 2400, 1200, rid)
            P.win("h", Y0, fx0 + 900, fx0 + 3900)
    void = None
    if cfg["levels"] > 1 and lv >= 1:
        void = (lx0, ys1 + VOID_WALK, lx1, ys2 - VOID_WALK)
    P.void = void

    # ---- anchors
    for key, (ax0, ax1), nm in (("AW", (bx0, xW), "W"), ("AE", (xE, bx1), "E")):
        P.room(key, "anchor", [(ax0, Y0, ax1, Y1)], name=f"ANCHOR STORE {nm}")
        edge = xW if key == "AW" else xE
        for dy in (-3000, 3000):
            P.door(key, "ST", "v", edge, (ys1 + ys2) / 2 + dy, 2200, "ST", double=True)
        outx = bx0 if key == "AW" else bx1
        na = cfg["anc_doors"]
        for k in range(na + 1):
            P.door(key, "OUT", "v", outx, Y0 + (k + 0.5) * (Y1 - Y0) / (na + 1), 2200, "OUT", double=True, exit=True)
        for yy in (Y0, Y1):
            for k in range(na):
                P.door(key, "OUT", "h", yy, ax0 + (k + 0.5) * (ax1 - ax0) / na, 2200, "OUT", double=True, exit=True)

    # ---- rows: corridor runs
    corr_of = {}
    for side, r in rowinfo.items():
        types, i, k = r["types"], 0, 0
        while i < n:
            if types[i] in ("shop", "plantA", "plantB", "amen"):
                j = i
                while j + 1 < n and types[j + 1] in ("shop", "plantA", "plantB", "amen"):
                    j += 1
                k += 1
                cid = f"C{side.upper()}{k}"
                ya, yb = sorted((r["ext"], r["cb"]))
                tag = ("S" if side == "s" else "N") + ("W" if X(i) < (xW + xE) / 2 else "E")
                P.room(cid, "corr", [(X(i), ya, X(j + 1), yb)], name=f"SERVICE CORRIDOR {tag}{k}")
                for b in range(i, j + 1):
                    corr_of[(side, b)] = cid
                len_ = (j + 1 - i) * G
                m = max(2, math.ceil(len_ / 21000))
                for q in range(m):
                    P.door(cid, "OUT", "h", r["ext"], X(i) + (q + 0.5) * len_ / m, 1200, "OUT", exit=True)
                i = j + 1
            else:
                i += 1

    # ---- bays
    shop_no = 0
    core_no = 0
    cores = []
    for side in ("s", "n"):
        r = rowinfo[side]
        for i, t in enumerate(r["types"]):
            x0, x1 = X(i), X(i) + G
            xc = (x0 + x1) / 2
            tag = f"{side.upper()}{i}"
            cid = corr_of.get((side, i))
            if t == "shop":
                shop_no += 1
                rid = f"S{shop_no:02d}"
                P.room(rid, "shop", [rect_y(x0, x1, side, 0, DH)], name=f"SHOP {shop_no:02d}")
                P.door(rid, "ST", "h", r["st"], xc, 2000, rid, double=True)
                P.door(rid, cid, "h", r["cb"], xc, 1000, rid, tag=False)
                P.win("h", r["st"], x0 + 600, xc - 1000 - 400)
                P.win("h", r["st"], xc + 1000 + 400, x1 - 600)
            elif t == "plantA":
                for k, (sub, key) in enumerate((("elec", "EL"), ("firepump", "FP"))):
                    rid = f"{key}{tag}"
                    P.room(rid, sub, [rect_y(x0 + k * 4200, x0 + (k + 1) * 4200, side, 0, DH)], sub=sub)
                    P.door(rid, cid, "h", r["cb"], x0 + k * 4200 + 2100, 1200, rid, tag=False)
            elif t == "plantB":
                for k, (sub, key) in enumerate((("ahu", "AH"), ("gen", "GN"))):
                    rid = f"{key}{tag}"
                    P.room(rid, sub, [rect_y(x0 + k * 4200, x0 + (k + 1) * 4200, side, 0, DH)], sub=sub)
                    P.door(rid, cid, "h", r["cb"], x0 + k * 4200 + 2100, 1200, rid, tag=False)
            elif t == "load":
                ya, yb = sorted((r["ext"], r["st"]))
                P.room("LD", "load", [(x0, ya, x1, yb)])
                for dx in (2100, 6300):
                    P.door("LD", "OUT", "h", r["ext"], x0 + dx, 3000, "OUT", double=True, exit=True)
                for nb, xe in ((i - 1, x0), (i + 1, x1)):
                    c2 = corr_of.get((side, nb)) if 0 <= nb < n else None
                    if c2:
                        ymid = r["cb"] + (r["ext"] - r["cb"]) / 2
                        P.door(c2, "LD", "v", xe, ymid, 1200, "LD", tag=False)
            elif t == "amen":
                muslim = cfg["muslim"]
                sp0, sp1 = x0 + 3300, x0 + 5100
                an = len([1 for rr in P.rooms if rr.startswith("AM")]) // 6 + 1
                p = f"AM{an}"
                P.room(f"{p}L", "amen", [rect_y(sp0, sp1, side, 0, 17400)], sub="amen")
                P.room(f"{p}A", "wc", [rect_y(sp0, sp1, side, 17400, DH)], sub="wca")
                P.room(f"{p}M", "wc", [rect_y(x0, sp0, side, 0, 9800)], sub="wcm")
                P.room(f"{p}W", "wc", [rect_y(sp1, x1, side, 0, 9800)], sub="wcw")
                P.room(f"{p}P", "prayer" if muslim else "baby", [rect_y(x0, sp0, side, 9800, DH)],
                       sub="prm" if muslim else "baby")
                P.room(f"{p}Q", "prayer" if muslim else "baby", [rect_y(sp1, x1, side, 9800, DH)],
                       sub="prw" if muslim else "aid")
                ys = lambda a, b: (zy(side, a, b)[0] + zy(side, a, b)[1]) / 2
                P.door("ST", f"{p}L", "h", r["st"], xc, 1200, f"{p}L")
                P.door(f"{p}L", f"{p}M", "v", sp0, ys(0, 9800), 1000, f"{p}M", tag=False)
                P.door(f"{p}L", f"{p}W", "v", sp1, ys(0, 9800), 1000, f"{p}W", tag=False)
                P.door(f"{p}L", f"{p}P", "v", sp0, ys(9800, 17400), 1000, f"{p}P", tag=False)
                P.door(f"{p}L", f"{p}Q", "v", sp1, ys(9800, 17400), 1000, f"{p}Q", tag=False)
                P.door(f"{p}L", f"{p}A", "h", r["st"] + r["sg"] * 17400, xc, 1000, f"{p}A", tag=False)
            elif t == "core":
                core_no += 1
                cores.append((x0, side, i))
                inner = +1 if i < (n - 1) / 2 else -1
                k = core_no
                ya, yb = sorted((r["ext"], r["st"]))
                px0, px1 = (x1 - 3000, x1) if inner > 0 else (x0, x0 + 3000)
                rx0, rx1 = (x0, x0 + 5400) if inner > 0 else (x1 - 5400, x1)
                tg = f"{side.upper()}{i}"
                P.room(f"ST{tg}", "stair", [rect_y(x0, x1, side, 0, 8400)], name=f"ESCAPE STAIR {k}")
                P.room(f"PS{tg}", "passage", [rect_y(px0, px1, side, 8400, DH + DS)], name=f"PASSAGE {k}")
                P.room(f"RE{tg}", "riser", [rect_y(rx0, rx1, side, 16800, DH + DS)], name=f"ELEC RISER {k}", sub="riser_e")
                P.room(f"RM{tg}", "riser", [rect_y(rx0, rx1, side, 8400, 16800)], name=f"MECH RISER {k}", sub="riser_m")
                pc = (px0 + px1) / 2
                P.door("ST", f"ST{tg}", "h", r["st"], xc, 2000, f"ST{tg}", double=True)
                P.door(f"ST{tg}", f"PS{tg}", "h", r["st"] + r["sg"] * 8400, pc, 2000, f"PS{tg}", double=True)
                P.door(f"PS{tg}", "OUT", "h", r["ext"], pc, 2000, "OUT", double=True, exit=True)
                bx = px0 if inner < 0 else px1
                ymid = lambda a, b: (zy(side, a, b)[0] + zy(side, a, b)[1]) / 2
                P.door(f"PS{tg}", f"RM{tg}", "v", px0 if inner > 0 else px1, ymid(8400, 16800), 900, f"RM{tg}", tag=False)
                P.door(f"PS{tg}", f"RE{tg}", "v", px0 if inner > 0 else px1, ymid(16800, DH + DS), 900, f"RE{tg}", tag=False)
                nb = i + inner
                c2 = corr_of.get((side, nb)) if 0 <= nb < n else None
                if c2:
                    xb = x1 if inner > 0 else x0
                    P.door(c2, f"PS{tg}", "v", xb, ymid(DH, DH + DS), 1200, f"PS{tg}", tag=False)
    P.cores, P.shops = cores, shop_no
    P.corr_of = corr_of
    # rename stairs by x order
    order = sorted(cores)
    for k, (x0, side, i) in enumerate(order, 1):
        tg = f"{side.upper()}{i}"
        P.rooms[f"ST{tg}"]["name"] = f"ESCAPE STAIR {k}"
        P.rooms[f"PS{tg}"]["name"] = f"PASSAGE {k}"
        P.rooms[f"RE{tg}"]["name"] = f"ELEC RISER {k}"
        P.rooms[f"RM{tg}"]["name"] = f"MECH RISER {k}"
    return P


# ------------------------------------------------------------------ travel distance
def door_pt(d):
    return (d["c"], d["coord"]) if d["o"] == "h" else (d["coord"], d["c"])


def travel(P):
    """Max walking distance to the nearest exit over all occupied rooms of the plan."""
    regs = {}
    obst = [P.void] if P.void else []
    for rid, r in P.rooms.items():
        regs[rid] = Region(r["rects"], obst if r["kind"] == "street" else ())
    ds = [d for d in P.doors]
    node = [door_pt(d) for d in ds]
    INF = math.inf
    dd = [INF] * len(ds)
    for i, d in enumerate(ds):
        kinds = {P.rooms[x]["kind"] for x in (d["a"], d["b"]) if x != "OUT"}
        if "OUT" in (d["a"], d["b"]) or "stair" in kinds:
            dd[i] = 0.0
    by_room = {}
    for i, d in enumerate(ds):
        for x in (d["a"], d["b"]):
            if x != "OUT":
                by_room.setdefault(x, []).append(i)
    edges = []
    for rid, lst in by_room.items():
        if P.rooms[rid]["kind"] not in THROUGH:
            continue
        for a in range(len(lst)):
            for b in range(a + 1, len(lst)):
                w = regs[rid].geo(node[lst[a]], node[lst[b]])
                edges.append((lst[a], lst[b], w))
    heap = [(0.0, i) for i in range(len(ds)) if dd[i] == 0.0]
    adj = {}
    for a, b, w in edges:
        adj.setdefault(a, []).append((b, w))
        adj.setdefault(b, []).append((a, w))
    while heap:
        cd, u = heapq.heappop(heap)
        if cd > dd[u]:
            continue
        for v, w in adj.get(u, ()):
            if cd + w < dd[v]:
                dd[v] = cd + w
                heapq.heappush(heap, (dd[v], v))
    worst = (0.0, None, None)
    for rid, r in P.rooms.items():
        if r["kind"] in NOOCC:
            continue
        lst = by_room.get(rid, [])
        if not lst:
            continue
        for p in regs[rid].samples():
            best = min(regs[rid].geo(p, node[i]) + dd[i] for i in lst)
            if best > worst[0]:
                worst = (best, rid, p)
    return worst, dd


# ------------------------------------------------------------------ layout search
def layout_ok(cfg, bays):
    res = []
    for lv in range(cfg["levels"] if cfg["levels"] < 3 else 3):
        P = build_plan(cfg, lv, bays)
        (d, rid, p), dd = travel(P)
        res.append((P, d, rid, p))
    return res


def search(cfg, limit_mm):
    n = cfg["n"]
    extra = []
    for it in range(14):
        bays = assign_bays(n, extra)
        res = layout_ok(cfg, bays)
        bad = [(d, rid, p, P) for P, d, rid, p in res if d > limit_mm]
        if not bad:
            return bays, res, extra
        d, rid, p, P = max(bad, key=lambda t: t[0])
        # candidate shop bays (not already core); nearest to the worst point
        cands = []
        for side, types in (("s", bays[0]), ("n", bays[1])):
            for i, t in enumerate(types):
                if t == "shop":
                    x = P.geo["xW"] + (i + 0.5) * G
                    y = P.geo["ys1"] - 10500 if side == "s" else P.geo["ys2"] + 10500
                    cands.append((math.hypot(x - p[0], y - p[1]), side, i))
        if not cands:
            break
        cands.sort()
        extra.append((cands[0][1], cands[0][2]))
        if it % 3 == 2:
            cfg["anc_doors"] = min(cfg["anc_doors"] + 1, 6)
    bays = assign_bays(n, extra)
    return bays, layout_ok(cfg, bays), extra


# ------------------------------------------------------------------ walls from rooms
def thickness(ka, kb):
    if ka is None or kb is None:
        return 300
    if ka in FIRE_RATED or kb in FIRE_RATED:
        return 250
    if ka in AMEN and kb in AMEN or (ka == "wc" and kb in AMEN | {"wc"}) or (kb == "wc" and ka in AMEN):
        return 150
    return 200


def build_walls(P):
    kind = lambda rid: P.rooms[rid]["kind"]
    # edges per line
    H, V = {}, {}
    for rid, r in P.rooms.items():
        for (x0, y0, x1, y1) in r["rects"]:
            H.setdefault(y0, []).append((x0, x1, rid, "above"))   # room lies above the line y0
            H.setdefault(y1, []).append((x0, x1, rid, "below"))
            V.setdefault(x0, []).append((y0, y1, rid, "right"))
            V.setdefault(x1, []).append((y0, y1, rid, "left"))
    walls = []
    index = {}
    for orient, lines in (("h", H), ("v", V)):
        for coord in sorted(lines):
            ed = lines[coord]
            pts = sorted({e[0] for e in ed} | {e[1] for e in ed})
            segs = []
            for a, b in zip(pts, pts[1:]):
                sides = {}
                for (e0, e1, rid, side) in ed:
                    if e0 <= a and e1 >= b:
                        sides[side] = rid
                s1, s2 = (sides.get("above"), sides.get("below")) if orient == "h" else (sides.get("right"), sides.get("left"))
                if s1 is None and s2 is None:
                    continue
                if s1 == s2:
                    continue
                segs.append((a, b, thickness(kind(s1) if s1 else None, kind(s2) if s2 else None)))
            merged = []
            for a, b, t in segs:
                if merged and merged[-1][1] == a and merged[-1][2] == t:
                    merged[-1][1] = b
                else:
                    merged.append([a, b, t])
            for a, b, t in merged:
                idx = len(walls)
                if orient == "h":
                    walls.append({"from": [a, coord], "to": [b, coord], "thk": t})
                else:
                    walls.append({"from": [coord, a], "to": [coord, b], "thk": t})
                index.setdefault((orient, coord), []).append((a, b, idx))
    return walls, index


def room_has(P, rid, pt):
    return any(r[0] < pt[0] < r[2] and r[1] < pt[1] < r[3] for r in P.rooms[rid]["rects"])


def swing_point(P, d):
    c, coord = d["c"], d["coord"]
    for off in (1500, 700, 300):
        for sg in (1, -1):
            pt = (c, coord + sg * off) if d["o"] == "h" else (coord + sg * off, c)
            if d["swing"] == "OUT":
                if not any(room_has(P, rid, pt) for rid in P.rooms):
                    return list(pt)
            elif room_has(P, d["swing"], pt):
                return list(pt)
    raise SystemExit(f"cannot find swing point for door {d}")


def place_openings(P, walls, index):
    ops, counter = [], [0]

    def find(o, coord, a, b):
        for (s, e, idx) in index.get((o, coord), ()):
            if s - 1 <= a and b <= e + 1:
                return idx, a - s
        raise SystemExit(f"{P.cfg['cc']}: no wall for opening {o}@{coord} {a}..{b}")

    for d in P.doors:
        w = d["w"]
        a = d["c"] - w / 2
        idx, at = find(d["o"], d["coord"], a, a + w)
        into = swing_point(P, d)
        counter[0] += 1
        tag = f"D{counter[0]:02d}" if d["tag"] else None
        if d["double"]:
            for k in range(2):
                f, t_ = find(d["o"], d["coord"], a + k * w / 2, a + (k + 1) * w / 2)
                o = {"wall": f, "at": round(t_), "width": round(w / 2), "kind": "door", "into": [round(into[0]), round(into[1])],
                     "hinge": "start" if k == 0 else "end"}
                if tag and k == 0:
                    o["tag"] = tag
                ops.append(o)
        else:
            o = {"wall": idx, "at": round(at), "width": round(w), "kind": "door", "into": [round(into[0]), round(into[1])],
                 "hinge": "start"}
            if tag:
                o["tag"] = tag
            ops.append(o)
    for wn in P.wins:
        try:
            idx, at = find(wn["o"], wn["coord"], wn["a"], wn["b"])
        except SystemExit:
            continue
        ops.append({"wall": idx, "at": round(at), "width": round(wn["b"] - wn["a"]), "kind": "window"})
    return ops


def add_anchor_windows(P):
    """Glazing bands on the anchor stores' exterior walls between the exit doors."""
    g = P.geo
    for key, (ax0, ax1) in (("AW", (g["xW"] - P.cfg["A"] * G, g["xW"])), ("AE", (g["xE"], g["bx1"]))):
        for o, coord, lo, hi in (("h", g["Y0"], ax0, ax1), ("h", g["Y1"], ax0, ax1),
                                 ("v", ax0 if key == "AW" else ax1, g["Y0"], g["Y1"])):
            used = [(d["c"] - d["w"] / 2 - 700, d["c"] + d["w"] / 2 + 700) for d in P.doors
                    if d["o"] == o and d["coord"] == coord and d["a"] == key]
            x = lo + 1500
            while x + 3000 <= hi - 1500:
                if not any(x < u1 and x + 3000 > u0 for u0, u1 in used):
                    P.win(o, coord, x, x + 3000)
                x += 6000


# ------------------------------------------------------------------ areas
def net_area(room, bodies):
    xs, ys = set(), set()
    bb = (min(r[0] for r in room["rects"]), min(r[1] for r in room["rects"]),
          max(r[2] for r in room["rects"]), max(r[3] for r in room["rects"]))
    near = [b for b in bodies if b[0] < bb[2] and b[2] > bb[0] and b[1] < bb[3] and b[3] > bb[1]]
    for r in room["rects"]:
        xs.update((r[0], r[2]))
        ys.update((r[1], r[3]))
    for b in near:
        xs.update(min(max(v, bb[0]), bb[2]) for v in (b[0], b[2]))
        ys.update(min(max(v, bb[1]), bb[3]) for v in (b[1], b[3]))
    xs, ys = sorted(xs), sorted(ys)
    tot = 0.0
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            cx, cy = (xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2
            if not any(r[0] < cx < r[2] and r[1] < cy < r[3] for r in room["rects"]):
                continue
            if any(b[0] < cx < b[2] and b[1] < cy < b[3] for b in near):
                continue
            tot += (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])
    return tot / 1e6


def wall_bodies(walls):
    out = []
    for w in walls:
        (x0, y0), (x1, y1) = w["from"], w["to"]
        h = w["thk"] / 2
        if y0 == y1:
            out.append((min(x0, x1) - h, y0 - h, max(x0, x1) + h, y0 + h))
        else:
            out.append((x0 - h, min(y0, y1) - h, x0 + h, max(y0, y1) + h))
    return out


# ------------------------------------------------------------------ profile / sheet scale
def load_profile(cc):
    path = HERE / "profiles" / f"{cc}.json"
    if not path.exists():
        raise SystemExit(f"No profile {path.name}")
    prof = json.loads(path.read_text(encoding="utf-8"))
    if "extends" in prof:
        base = load_profile(prof.pop("extends"))
        for k, v in prof.items():
            base[k] = {**base[k], **v} if isinstance(v, dict) and isinstance(base.get(k), dict) else v
        prof = base
    return prof


def pick_scale(prof, bw, bd, pw, pd, legend_mm=70):
    """Smallest standard scale whose viewport holds plot + grid bubbles; returns (scale, label)."""
    sh = prof["sheet"]
    w, h, m = sh["w"], sh["h"], sh["margin"]
    inch = sh["units"].startswith("in")
    k = 25.4 if inch else 1.0
    vw = (w - m - sh["tb_w"] - 3 * m) * k
    vh = (h - 4 * m) * k - legend_mm
    cands = [48, 96, 192, 384] if inch else [100, 125, 150, 200, 250, 300, 400, 500, 1000]
    for s in cands:
        if max(pw, bw + 90 * s) <= vw * s and max(pd, bd + 90 * s) <= vh * s:
            break
    if inch:
        lab = {48: '1/4" = 1\'-0"', 96: '1/8" = 1\'-0"', 192: '1/16" = 1\'-0"', 384: '1/32" = 1\'-0"'}[s]
    else:
        lab = prof["scale_label"].replace("100", str(s), 1)
    return s, lab


def dump_spec(spec):
    """One top-level key per line, compact values (keeps examples/malls small, still diff-able)."""
    parts = [json.dumps(k, ensure_ascii=False) + ":" + json.dumps(v, ensure_ascii=False, separators=(",", ":"))
             for k, v in spec.items()]
    return "{\n" + ",\n".join(parts) + "\n}\n"


# ------------------------------------------------------------------ main generator
def generate(cc, out, levels, plot):
    prof = load_profile(cc)
    R = country_rules(cc)
    PX, PY = plot
    front, side, rear, setb_src, setb_warn = R["setb"]
    avail = PX - 2 * side
    nt = int(avail // G)
    A = 3 if nt >= 17 else 2
    n = nt - 2 * A
    if n < 7:
        raise SystemExit(f"{cc}: plot {PX/1000:g} m wide holds only {nt} bays; need >= 11")
    bw = nt * G
    bd = DS * 2 + DH * 2 + WST
    bx0 = round((PX - bw) / 2 / 100) * 100
    rear_gap = max(rear, 12000)
    by0 = PY - bd - rear_gap
    if by0 < front:
        by0 = front
        rear_gap = PY - bd - by0
    if rear_gap < rear:
        raise SystemExit(f"{cc}: plot depth {PY/1000:g} m too small (need {(bd + front + rear)/1000:g} m)")
    cfg = dict(cc=cc, n=n, A=A, bx0=bx0, by0=by0, levels=levels, anc_doors=2, muslim=cc in MUSLIM)
    limit = R["travel"][0] * 1000
    bays, res, extra = search(cfg, limit)
    names = ["GF"] + [f"L{i}" for i in range(1, levels)]
    if levels > 3:   # levels >= L2 repeat L2 layout
        P2 = build_plan(cfg, 2, bays)
    plans = []
    for lv in range(levels):
        plans.append(res[lv][0] if lv < len(res) else build_plan(cfg, 2, bays))
    bilingual = bool(prof.get("bilingual"))
    cityname, lat, lon, tz = CITY[cc]
    gf_h = R["gfh"][0]
    g = plans[0].geo
    foot = (g["xW"] - A * G, g["Y0"], g["bx1"], g["Y1"])
    plot_poly = [[0, 0], [PX, 0], [PX, PY], [0, PY]]
    ratio, label = pick_scale(prof, bw, bd, PX, PY)
    grids = {"x": [bx0 + k * G for k in range(nt + 1)], "y": [g["Y0"], g["ys0"], g["ys1"], g["ys2"], g["yn1"], g["Y1"]]}
    totals = dict(gla=0.0, gfa=0.0)
    mall_levels, specs = [], []
    today = datetime.date.today().isoformat()
    travel_rows = []
    for lv, P in enumerate(plans):
        add_anchor_windows(P)
        walls, index = build_walls(P)
        ops = place_openings(P, walls, index)
        bodies = wall_bodies(walls)
        rooms_spec, meta_rooms = [], []
        for rid, r in P.rooms.items():
            a = net_area(r, bodies)
            main = max(r["rects"], key=lambda q: (q[2] - q[0]) * (q[3] - q[1]))
            pt = [round((main[0] + main[2]) / 2), round((main[1] + main[3]) / 2)]
            ar = r["name_ar"] if bilingual else ""
            rooms_spec.append({"name": r["name"], "name_ar": ar, "pt": pt, "area": round(a, 1)})
            meta_rooms.append({"id": rid, "kind": r["kind"], "sub": r["sub"], "name": r["name"], "rects": [list(q) for q in r["rects"]],
                               "pt": pt, "area": round(a, 1)})
            totals["gfa"] += a if lv == 0 else 0
            if r["kind"] in ("shop", "anchor", "food"):
                totals["gla"] += a
        floors = names[lv]
        title = "Sample Shopping Mall - " + ("Ground Floor" if lv == 0 else f"Level {lv}")
        rules = {"source": f"{setb_src}" + (" [verify]" if setb_warn else ""), "front": front, "side": side, "rear": rear}
        if R["cov"]:
            rules["coverage_max"] = R["cov"][0]
            rules["source"] += f"; coverage {R['cov'][1]}"
        (wd, wrid, wp) = (res[lv][1] / 1000, res[lv][2], res[lv][3]) if lv < len(res) else (None, None, None)
        notes = [
            "SAMPLE PROJECT generated by ArchMind gen_mall.py - not for submission.",
            f"GRID {G/1000:g} m [RoT retail 7.5-9 m]; street {WST/1000:g} m, shops {G/1000:g} x {DH/1000:g} m, service corridor {DS/1000:g} m [RoT].",
            f"TRAVEL LIMIT {R['travel'][0]:g} m: {R['travel'][1]}" + (" (verify)" if R['travel'][2] else "")
            + (f". Computed max this level {wd:.1f} m." if wd is not None else ""),
            "Exit = final exit door or protected-stair door; path around atrium void; open-plan rooms; sprinklered building (assumed).",
            f"SETBACKS F/S/R {front/1000:g}/{side/1000:g}/{rear/1000:g} m: {setb_src}" + (" (verify)" if setb_warn else ""),
            "ASSUMPTIONS: plot "
            f"{PX/1000:g} x {PY/1000:g} m, frontage south, loading yard north; service corridors fire-rated, 2+ exits each.",
            "WC + prayer rooms separated men/women (design-concepts.md 6.6 RoT)." if cc in MUSLIM else
            "WC separated men/women, accessible WC every level (RoT).",
            "Stairs, escalators, atrium void: see MEP/ARCH overlay.",
        ]
        spec = {
            "country": cc,
            "project": {"title": "Sample Shopping Mall", "title_ar": "مركز تسوق نموذجي", "client": "Showcase",
                        "plot": "PIN 00000000 (sample)", "drawing": "Ground Floor Plan" if lv == 0 else f"Level {lv} Plan",
                        "drawing_ar": "مسقط الدور الأرضي" if lv == 0 else "مسقط الدور الأول" if lv == 1 else "مسقط الدور المتكرر",
                        "number": f"A-10{lv + 1}", "rev": "0", "date": today, "drawn": "ArchMind gen_mall"},
            "profile": {"scale": ratio, "scale_label": label, "dim": {"text_h": round(prof["dim"]["text_h"] * 0.8, 5)}},
            "walls": walls, "openings": ops, "rooms": rooms_spec, "grids": grids,
            "plot": {"polygon": plot_poly, "front": "south"},
            "rules": rules, "notes": notes,
        }
        spec["mall"] = dict(
            level=floors, index=lv, bay=G, cc=cc, bounds=list(foot), geo=g, ratio=ratio,
            void=list(P.void) if P.void else None, levels_total=levels,
            atrium=[g["lx0"], g["ys1"] + VOID_WALK, g["lx1"], g["ys2"] - VOID_WALK] if levels > 1 else None, rooms=meta_rooms,
            doors=[dict(pt=list(door_pt(d)), w=d["w"], o=d["o"], a=d["a"], b=d["b"], exit=d["exit"], double=d["double"])
                   for d in P.doors],
            wall_thk={"exterior": 300, "fire_rated": 250, "other": 200},
            sprinkler=dict(std="EN 12845 OH" if cc in EN_SPRINKLER else "NFPA 13 OH2",
                           max_area=12.0 if cc in EN_SPRINKLER else 12.1, max_spacing=4000 if cc in EN_SPRINKLER else 4600,
                           src="references/disciplines/mep.md 4.1"),
            gf_h=gf_h, up_h=UP_H, muslim=cc in MUSLIM)
        travel_rows.append(dict(level=floors, max_m=round(wd, 1) if wd is not None else None, room=wrid,
                                pt=[round(wp[0]), round(wp[1])] if wp else None))
        specs.append(spec)
    # ---- GF render data
    gf = specs[0]
    H = gf_h + (levels - 1) * UP_H
    foot_ov = 900
    lx0, lx1, ys1, ys2 = g["lx0"], g["lx1"], g["ys1"], g["ys2"]
    void = plans[1].void if levels > 1 else None
    fx0, fy0, fx1, fy1 = foot
    if void:
        vx0, vy0, vx1, vy1 = void
        gf["roofs"] = [[fx0, fy0, vx0, fy1], [vx1, fy0, fx1, fy1], [vx0, fy0, vx1, vy0], [vx0, vy1, vx1, fy1]]
    else:
        gf["roofs"] = [[fx0 - foot_ov, fy0 - foot_ov, fx1 + foot_ov, fy1 + foot_ov]]
    mass = []
    for k in range(1, levels):
        z0 = gf_h + (k - 1) * UP_H + 300
        z1 = gf_h + k * UP_H
        t = 300
        mass += [
            {"box": [fx0, fy0, fx1, fy0 + t], "z": [z0, z1], "mat": "plaster"},
            {"box": [fx0, fy1 - t, fx1, fy1], "z": [z0, z1], "mat": "plaster"},
            {"box": [fx0, fy0, fx0 + t, fy1], "z": [z0, z1], "mat": "plaster"},
            {"box": [fx1 - t, fy0, fx1, fy1], "z": [z0, z1], "mat": "plaster"},
            {"box": [fx0 + t, fy0 - 40, fx1 - t, fy0], "z": [z0 + 900, z1 - 1000], "mat": "glass"},
            {"box": [fx0 + t, fy1, fx1 - t, fy1 + 40], "z": [z0 + 900, z1 - 1000], "mat": "glass"},
            {"box": [fx0 - 120, fy0 - 160, fx1 + 120, fy0 - 60], "z": [z0 + 900, z1 - 1000], "mat": "frame", "kind": "fins", "spacing": G},
            {"box": [fx0 - 120, fy1 + 60, fx1 + 120, fy1 + 160], "z": [z0 + 900, z1 - 1000], "mat": "frame", "kind": "fins", "spacing": G},
        ]
        if void:
            vx0, vy0, vx1, vy1 = void
            zb = gf_h + (k - 1) * UP_H + 300
            for bx in ([vx0, vy0, vx1, vy0 + 60], [vx0, vy1 - 60, vx1, vy1], [vx0, vy0, vx0 + 60, vy1], [vx1 - 60, vy0, vx1, vy1]):
                mass.append({"box": bx, "z": [zb, zb + 1100], "mat": "glass"})
    # roof slab pieces + skylight
    if void:
        vx0, vy0, vx1, vy1 = void
        for rr in ([fx0, fy0, vx0, fy1], [vx1, fy0, fx1, fy1], [vx0, fy0, vx1, vy0], [vx0, vy1, vx1, fy1]):
            mass.append({"box": rr, "z": [H, H + 300], "mat": "plaster"})
        mass.append({"box": [vx0, vy0, vx1, vy1], "z": [H, H + 1800], "mat": "glass"})
        mass.append({"box": [vx0, vy0, vx1, vy1], "z": [H + 1800, H + 1900], "mat": "frame", "kind": "fins", "spacing": 1400})
        # rooftop plant over the north plant bays
        for k in range(3):
            cx = lx0 + 3000 + k * 6000
            mass.append({"box": [cx, yn1_ := g["yn1"] - 9000, cx + 4200, yn1_ + 6000], "z": [H + 300, H + 2400], "mat": "frame"})
    else:
        mass.append({"box": [fx0 - foot_ov, fy0 - foot_ov, fx1 + foot_ov, fy1 + foot_ov], "z": [H, H + 300], "mat": "plaster"})
    # signage band + canopy
    mass.append({"box": [lx0, fy0 - 450, lx1, fy0], "z": [H - 1700, H - 500], "mat": "frame"})
    for a0, a1 in ((fx0, g["xW"]), (g["xE"], fx1)):
        mass.append({"box": [a0 + 1500, fy0 - 350, a1 - 1500, fy0], "z": [H - 1700, H - 700], "mat": "wood"})
    cxl = (lx0 + lx1) / 2
    cw = 19200
    mass.append({"box": [cxl - cw / 2, fy0 - 4500, cxl + cw / 2, fy0], "z": [gf_h - 900, gf_h - 600], "mat": "frame"})
    for dx in (-cw / 2 + 300, cw / 2 - 300):
        mass.append({"box": [cxl + dx - 150, fy0 - 4350, cxl + dx + 150, fy0 - 4050], "z": [0, gf_h - 900], "mat": "frame"})
    # parking
    park_info = dict(rows=0, bays=0)
    py0, py1 = 1500, fy0 - 2500
    depth = py1 - py0
    rows = 2 if depth >= 17000 else 1 if depth >= 11500 else 0
    px0, px1 = side, PX - side
    if rows:
        mass.append({"box": [px0, py0 - 500, px1, py1], "z": [-150, -90], "mat": "frame"})
        nb = int((px1 - px0) // 2500)
        for r_ in range(rows):
            ry0 = py0 if r_ == 0 else py0 + 5500 + 6000
            for k in range(nb + 1):
                mass.append({"box": [px0 + k * 2500 - 40, ry0, px0 + k * 2500 + 40, ry0 + 5500], "z": [-90, -70], "mat": "plaster"})
        park_info = dict(rows=rows, bays=nb * rows)
    gf["massing"] = mass
    gf["mall"]["parking"] = park_info
    # ---- write
    out.mkdir(parents=True, exist_ok=True)
    files = {}
    for nm, spec in zip(names, specs):
        p = out / f"{nm}.json"
        p.write_text(dump_spec(spec), encoding="utf-8")
        files[nm] = p.name
    cov = (fx1 - fx0) * (fy1 - fy0) / (PX * PY) * 100
    req_bays = math.ceil(totals["gla"] / R["park"][0]) if totals["gla"] else 0
    stairs = [len([r for r in P.rooms.values() if r["kind"] == "stair"]) for P in plans]
    ext_exits = [len([d for d in P.doors if d["exit"]]) for P in plans]
    summary = dict(
        country=cc, profile_country=prof.get("country"), levels=names, files=files, bilingual=bilingual,
        plot_m=[PX / 1000, PY / 1000], footprint_m=[round(bw / 1000, 1), round(bd / 1000, 1)], bays=dict(total=nt, anchor_each=A, street=n),
        shops_per_level=[len([r for r in P.rooms.values() if r["kind"] in ("shop", "food")]) for P in plans],
        coverage_pct=round(cov, 1), gla_m2=round(totals["gla"]), parking=dict(required=req_bays, shown=park_info["bays"],
            ratio_m2_per_bay=R["park"][0], source=R["park"][1], warn=R["park"][2],
            note="surface bays shown as ground massing; balance assumed basement/off-plot, not modelled"),
        travel=dict(ok=all(r["max_m"] is not None and r["max_m"] <= R["travel"][0] for r in travel_rows), limit_m=R["travel"][0], source=R["travel"][1], warn=R["travel"][2], computed=travel_rows,
                    stairs_per_level=stairs, exterior_exit_doors_per_level=ext_exits,
                    extra_cores=[f"{s}{i}" for s, i in extra]),
        setbacks=dict(front=front, side=side, rear=rear, source=setb_src, warn=setb_warn),
        coverage_rule=dict(max=R["cov"][0], source=R["cov"][1]) if R["cov"] else None,
        stair_clear_width_mm=dict(value=R["stair"][0], source=R["stair"][1], warn=R["stair"][2]),
        gf_height_mm=dict(value=gf_h, source=R["gfh"][1], warn=R["gfh"][2]), upper_height_mm=UP_H,
        sprinkler=specs[0]["mall"]["sprinkler"],
        scale=dict(ratio=ratio, label=label),
        render=dict(city=cityname, BS_LAT=lat, BS_LON=lon, BS_TZ=tz, BS_HEIGHT=gf_h),
        design_rules=[
            "Structural grid 8.4 m [RoT: references/disciplines/structural.md 3 retail 7.5-9 m]",
            "Mall street 12.0 m double-loaded, central atrium = lobby bays [RoT]",
            "Shops 8.4 m x 21.0 m (brief 18-25 m) [RoT]; service corridor 4.2 m [RoT]",
            "Two anchors at street ends, 2 bays wide (3 on large plots) [RoT]",
            "Muslim-majority: prayer room + ablution men/women [references/disciplines/design-concepts.md 6.6]" if cc in MUSLIM else "No prayer rooms (country not in Muslim-majority list)",
            "Travel distance to exit: " + R["travel"][1] + (" (verify)" if R["travel"][2] else ""),
            "Escape stair width: " + R["stair"][1] + (" (verify)" if R["stair"][2] else ""),
            "Sprinkler/detector/diffuser spacing: references/disciplines/mep.md 4.1, 4.3, 1.5",
        ],
    )
    (out / "mall.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    return summary


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--country", required=True, help="iso2 code with a scripts/profiles/<cc>.json")
    ap.add_argument("--out", required=True)
    ap.add_argument("--levels", type=int, default=2)
    ap.add_argument("--plot", default="120x90", help="plot WxD in metres, front = south side")
    a = ap.parse_args()
    w, d = (float(v) for v in a.plot.lower().split("x"))
    s = generate(a.country.lower(), Path(a.out), max(1, a.levels), (round(w * 1000), round(d * 1000)))
    t = s["travel"]
    print(f"{a.country}: {s['levels']} footprint {s['footprint_m']} m, shops/level {s['shops_per_level']}, "
          f"travel max {[r['max_m'] for r in t['computed']]} m (limit {t['limit_m']}), stairs {t['stairs_per_level']} -> {a.out}")


if __name__ == "__main__":
    main()
