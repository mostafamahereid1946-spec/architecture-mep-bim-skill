# /// script
# requires-python = ">=3.9"
# dependencies = ["ezdxf"]
# ///
"""Add MEP layers (+ stair / atrium / lift architecture details) to a gen_mall.py level plan DXF.

Usage:
    uv run --with ezdxf scripts/dxf_plan.py GF.json          # plan first
    uv run -q scripts/mep_overlay.py GF.json [--dxf GF.dxf] [-o GF-MEP.dxf]

Reads the level spec written by gen_mall.py (needs its "mall" block: room rectangles, door points,
atrium) and the plan DXF, draws indicative (not hydraulically/aerodynamically designed) services and
writes <level>-MEP.dxf with a legend block in paper space (viewport shortened to make room).

Layers (discipline prefixes M- E- P- FP-, distinct ACI colours; profile key "mep_prefix" may rename them):
  M-HVAC-SCD supply diffusers (grid <= 3.0 m, mep.md 1.5)   M-HVAC-RCG return grilles
  M-HVAC-SAD supply duct main along the service corridor + shop take-offs   M-HVAC-EQPT AHU / risers
  E-LITE mall street luminaire grid (4.2 x 4.0 m RoT, retail 300-750 lx mep.md 3.5)  E-LITE-EMER emergency + exit signs
  E-DB shop DBs + MDB + generator   E-TRAY feeder cable tray   E-FALM detectors (smoke 9.0 m grid; NFPA 72 9.1 m /
  BS 5839 7.5 m radius, mep.md 4.3), manual call points at exits, sounders
  FP-SPRK-HEAD heads (adaptive grid <= 2.8 m; NFPA 13 OH2 12.1 m2 / 4.6 m or EN 12845 OH 12 m2 / 4.0 m, mep.md 4.1)
  FP-SPRK-PIPE indicative branches + mains   FP-HOSE hose reels / FHC at exits and stairs (mep.md 4.2)
  P-FIXT WC fixtures, ablution points, grease traps   P-DCW / P-SANR stack + branch lines (wet wall)
  A-FLOR-STRS stair treads   A-FLOR-OTLN atrium void   A-FLOR-EVTR lifts + escalators   X-ANNO-LGND legend
No sprinklers/detectors in the atrium void (ceiling > 10 m: beam detectors + smoke control, mep.md 4.3).
"""
import argparse
import json
import math
import sys
from pathlib import Path

import ezdxf
from ezdxf.enums import TextEntityAlignment

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dxf_plan  # noqa: E402  (same folder: profile loader)

MC = TextEntityAlignment.MIDDLE_CENTER
LEFT = TextEntityAlignment.MIDDLE_LEFT

# key -> (suffix, aci, lineweight, linetype, description)
LAYERS = {
    "scd": ("M", "HVAC-SCD", 4, 18, None, "Supply air diffuser 600x600"),
    "rcg": ("M", "HVAC-RCG", 3, 18, None, "Return air grille"),
    "sad": ("M", "HVAC-SAD", 5, 35, None, "Supply duct main / take-off"),
    "eqpt": ("M", "HVAC-EQPT", 30, 50, None, "AHU / riser shaft"),
    "mtxt": ("M", "ANNO-TEXT", 150, 18, None, "HVAC tags"),
    "lite": ("E", "LITE", 2, 18, None, "Luminaire (mall street)"),
    "emer": ("E", "LITE-EMER", 40, 18, None, "Emergency light / EXIT sign"),
    "db": ("E", "DB", 6, 50, None, "DB / MDB / generator"),
    "tray": ("E", "TRAY", 210, 35, "DASHED", "Feeder cable tray"),
    "falm": ("E", "FALM", 230, 25, None, "Smoke(S) / heat(H) detector, call point, sounder"),
    "etxt": ("E", "ANNO-TEXT", 52, 18, None, "Electrical tags"),
    "head": ("FP", "SPRK-HEAD", 1, 25, None, "Sprinkler head"),
    "pipe": ("FP", "SPRK-PIPE", 12, 50, None, "Sprinkler branch / main"),
    "hose": ("FP", "HOSE", 20, 35, None, "Hose reel HR / hose cabinet FHC"),
    "ftxt": ("FP", "ANNO-TEXT", 14, 18, None, "Fire tags"),
    "fixt": ("P", "FIXT", 90, 18, None, "WC / basin / urinal / ablution / grease trap"),
    "dcw": ("P", "DCW", 160, 25, None, "Cold water branch"),
    "sanr": ("P", "SANR", 34, 35, None, "Soil / waste stack + branch"),
    "ptxt": ("P", "ANNO-TEXT", 94, 18, None, "Plumbing tags"),
}
ARCH = {
    "strs": ("A-FLOR-STRS", 252, 25, "Stair treads / UP arrow"),
    "otln": ("A-FLOR-OTLN", 253, 25, "Atrium void edge"),
    "evtr": ("A-FLOR-EVTR", 251, 25, "Lift car / escalator"),
}
LGND = "X-ANNO-LGND"


class Ov:
    def __init__(self, spec, doc, prof):
        self.spec, self.doc, self.prof = spec, doc, prof
        self.m = spec["mall"]
        self.msp = doc.modelspace()
        self.f = prof.get("mm_to_unit", 1)
        self.pm = prof["scale"] * prof.get("paper_mm", 1)       # drawing units per paper mm
        self.style = prof["text"]["style"]
        pre = prof.get("mep_prefix", {})
        self.names = {}
        for k, (d, s, aci, lw, lt, desc) in LAYERS.items():
            name = f"{pre.get(d, d)}-{s}"
            self.names[k] = name
            self.mk(name, aci, lw, lt)
        for k, (name, aci, lw, desc) in ARCH.items():
            self.names[k] = name
            self.mk(name, aci, lw, None)
        self.mk(LGND, 7, 18, None)
        self.rooms = {r["id"]: r for r in self.m["rooms"]}
        self.counts = {}
        g = self.m["geo"]
        self.atrium = tuple(self.m["atrium"]) if self.m.get("atrium") else None
        self.sp_head = 2800
        self.sp_det = 9000
        self.sp_dif = 3000

    # ---- helpers
    def mk(self, name, aci, lw, lt):
        if name not in self.doc.layers:
            lay = self.doc.layers.add(name, color=aci, lineweight=lw)
            if lt:
                lay.dxf.linetype = lt

    def P(self, x, y):
        return (x * self.f, y * self.f)

    def S(self, paper_mm):
        return paper_mm * self.pm

    def n(self, key, k=1):
        self.counts[key] = self.counts.get(key, 0) + k

    def line(self, key, a, b):
        self.msp.add_line(self.P(*a), self.P(*b), dxfattribs={"layer": self.names[key]})

    def poly(self, key, pts, close=True):
        self.msp.add_lwpolyline([self.P(*p) for p in pts], close=close, dxfattribs={"layer": self.names[key]})

    def rect(self, key, x0, y0, x1, y1):
        self.poly(key, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)])

    def text(self, key, s, p, h, align=MC):
        t = self.msp.add_text(s, height=h, dxfattribs={"layer": self.names[key], "style": self.style})
        t.set_placement(self.P(*p), align=align)

    def cross_sq(self, key, c, half):
        """square with diagonals (diffuser / grille symbol), half-size in mm."""
        x, y = c
        self.rect(key, x - half, y - half, x + half, y + half)
        self.line(key, (x - half, y - half), (x + half, y + half))
        self.line(key, (x - half, y + half), (x + half, y - half))

    # ---- grids
    def grid(self, rects, sp, inset=300, excl=()):
        x0, y0 = min(r[0] for r in rects), min(r[1] for r in rects)
        x1, y1 = max(r[2] for r in rects), max(r[3] for r in rects)
        nx = max(1, math.ceil((x1 - x0 - 2 * inset) / sp))
        ny = max(1, math.ceil((y1 - y0 - 2 * inset) / sp))
        cw, ch = (x1 - x0 - 2 * inset) / nx, (y1 - y0 - 2 * inset) / ny
        out = []
        for ix in range(nx):
            for iy in range(ny):
                x, y = x0 + inset + (ix + 0.5) * cw, y0 + inset + (iy + 0.5) * ch
                if not any(r[0] + inset <= x <= r[2] - inset and r[1] + inset <= y <= r[3] - inset for r in rects):
                    continue
                if any(e[0] < x < e[2] and e[1] < y < e[3] for e in excl):
                    continue
                out.append((ix, iy, x, y))
        return out, cw, ch

    def excl(self, kind):
        """areas without ceiling services: atrium void (and GF area under it)."""
        return [self.atrium] if (self.atrium and kind in ("street",)) else []

    # ---- device symbols
    def head(self, x, y):
        r = self.S(0.7)
        self.msp.add_circle(self.P(x, y), r, dxfattribs={"layer": self.names["head"]})
        self.msp.add_line(self.P(x, y), (self.P(x, y)[0] + r * 0.9, self.P(x, y)[1] + r * 0.9), dxfattribs={"layer": self.names["head"]})
        self.n("sprinkler heads")

    def detector(self, x, y, heat=False):
        r = self.S(0.9)
        self.msp.add_circle(self.P(x, y), r, dxfattribs={"layer": self.names["falm"]})
        t = self.msp.add_text("H" if heat else "S", height=r * 1.2, dxfattribs={"layer": self.names["falm"], "style": self.style})
        t.set_placement(self.P(x, y), align=MC)
        self.n("heat detectors" if heat else "smoke detectors")

    def luminaire(self, x, y):
        r = self.S(0.9)
        c = self.P(x, y)
        self.msp.add_circle(c, r, dxfattribs={"layer": self.names["lite"]})
        for dx, dy in ((1, 0), (0, 1)):
            self.msp.add_line((c[0] - dx * r, c[1] - dy * r), (c[0] + dx * r, c[1] + dy * r), dxfattribs={"layer": self.names["lite"]})
        self.n("luminaires")

    def labelled_box(self, key, tkey, x0, y0, x1, y1, label, h=None):
        self.rect(key, x0, y0, x1, y1)
        self.text(tkey, label, ((x0 + x1) / 2, (y0 + y1) / 2), h or self.S(1.6))

    # ---- door helpers
    def doors_of(self, rid):
        return [d for d in self.m["doors"] if rid in (d["a"], d["b"])]

    def door_between(self, a, b):
        for d in self.m["doors"]:
            if {d["a"], d["b"]} == {a, b}:
                return d
        return None

    def inward(self, d, rid):
        """unit vector from the door into room rid."""
        r = self.rooms[rid]
        px, py = d["pt"]
        for ux, uy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x, y = px + ux * 400, py + uy * 400
            if any(q[0] < x < q[2] and q[1] < y < q[3] for q in r["rects"]):
                return ux, uy
        return 0, 0

    # ---------------------------------------------------------------- drawing groups
    def architecture(self):
        m = self.m
        h = self.S(2.0)
        for r in m["rooms"]:
            if r["kind"] == "stair":
                x0, y0, x1, y1 = r["rects"][0]
                cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
                street_side = self.door_between(r["id"], "ST")
                up = 1 if street_side and street_side["pt"][1] > cy else -1   # arrival from the street edge
                for fx in (-1, 1):
                    xa, xb = (cx + fx * 150, cx + fx * 1500) if fx > 0 else (cx - 1500, cx - 150)
                    base = cy - up * 2300
                    for k in range(16):
                        y = base + up * k * 280
                        self.line("strs", (xa, y), (xb, y))
                    self.line("strs", (xa, base), (xa, base + up * 15 * 280))
                    self.line("strs", (xb, base), (xb, base + up * 15 * 280))
                self.rect("strs", cx - 1500, min(cy - 2300, cy - 2300 + up * 15 * 280), cx + 1500, max(cy - 2300, cy - 2300 + up * 15 * 280))
                self.text("strs", "UP", (cx - 825, cy + up * 2400), h)
                self.n("stairs")
            elif r["kind"] == "lift":
                x0, y0, x1, y1 = r["rects"][0]
                for k in range(2):
                    cx = x0 + 750 + k * 1500
                    self.rect("evtr", cx - 650, y0 + 300, cx + 650, y0 + 1900)
                    self.line("evtr", (cx - 650, y0 + 300), (cx + 650, y0 + 1900))
                    self.line("evtr", (cx - 650, y0 + 1900), (cx + 650, y0 + 300))
                self.n("lifts", 2)
        a = self.atrium
        if a:
            if m["index"] >= 1:
                self.rect("otln", *a)
                self.line("otln", (a[0], a[1]), (a[2], a[3]))
                self.line("otln", (a[0], a[3]), (a[2], a[1]))
                self.text("otln", "ATRIUM VOID (OPEN TO BELOW) - glass balustrade", ((a[0] + a[2]) / 2, a[3] - 800), h)
            else:
                self.poly("otln", [(a[0], a[1]), (a[2], a[1]), (a[2], a[3]), (a[0], a[3])])
                self.text("otln", "ATRIUM - OPEN TO L1 / GLASS ROOF", ((a[0] + a[2]) / 2, a[3] - 800), h)
            cx, cy = (a[0] + a[2]) / 2, (a[1] + a[3]) / 2
            for dy in (-900, 900):
                self.rect("evtr", cx - 4800, cy + dy - 650, cx + 4800, cy + dy + 650)
                for k in range(1, 24):
                    xx = cx - 4800 + k * 400
                    self.line("evtr", (xx, cy + dy - 650), (xx, cy + dy + 650))
            self.text("evtr", "ESC UP / DN", (cx, cy), h)

    def sprinklers(self):
        m = self.m
        types = {"shop", "food", "anchor", "street", "corr", "passage", "load", "firepump", "ahu", "gen", "amen", "wc", "prayer", "baby"}
        for r in m["rooms"]:
            if r["kind"] not in types:
                continue
            ex = self.excl(r["kind"])
            pts, cw, ch = self.grid([tuple(q) for q in r["rects"]], self.sp_head, 300, ex)
            if not pts:
                continue
            for ix, iy, x, y in pts:
                self.head(x, y)
            index = {(ix, iy): (x, y) for ix, iy, x, y in pts}
            for (ix, iy), (x, y) in index.items():     # branch lines along x between neighbours
                if (ix + 1, iy) in index:
                    self.line("pipe", (x, y), index[(ix + 1, iy)])
            xs0 = min(ix for ix, _ in index)
            col = sorted((iy, p) for (ix, iy), p in index.items() if ix == xs0)
            for (a, pa), (b, pb) in zip(col, col[1:]):  # cross main joining the rows
                if b == a + 1:
                    self.line("pipe", pa, pb)
            # stub to the room's main door
            ds = self.doors_of(r["id"])
            if ds and col:
                d = ds[0]
                p0 = col[0][1]
                self.line("pipe", p0, (d["pt"][0], p0[1]))
                self.line("pipe", (d["pt"][0], p0[1]), d["pt"])
        # mains: corridors + street centre line
        for r in m["rooms"]:
            q = r["rects"][0]
            if r["kind"] == "corr":
                y = (q[1] + q[3]) / 2 - 900
                self.line("pipe", (q[0] + 600, y), (q[2] - 600, y))
                self.text("ftxt", "SPRINKLER MAIN DN150 (indicative)", ((q[0] + q[2]) / 2, y - self.S(2.5)), self.S(1.6))
        st = self.rooms["ST"]["rects"][0]
        y = (st[1] + st[3]) / 2
        self.line("pipe", (st[0] + 600, y), (st[2] - 600, y))
        self.text("ftxt", "SPRINKLER MAIN DN150 (indicative)", ((st[0] + st[2]) / 2 - 18000, y + self.S(2.2)), self.S(1.6))
        sp = self.m["sprinkler"]
        self.text("ftxt", f"SPRINKLER GRID <= 2.8 m ({sp['std']}: max {sp['max_area']} m2 / {sp['max_spacing']/1000:g} m) RoT - {sp['src']}",
                  ((st[0] + st[2]) / 2 + 12000, y - self.S(2.4)), self.S(1.6))

    def detectors(self):
        for r in self.m["rooms"]:
            k = r["kind"]
            if k in ("wc", "riser", "lift"):
                continue
            heat = k in ("ahu", "gen", "firepump", "load")
            pts, _, _ = self.grid([tuple(q) for q in r["rects"]], self.sp_det, 400, self.excl(k))
            if k == "stair":
                x0, y0, x1, y1 = r["rects"][0]
                pts = [(0, 0, (x0 + x1) / 2, (y0 + y1) / 2)]
            if k == "street" and self.atrium:
                a = self.atrium
                # linear beam detector across the atrium
                self.line("falm", (a[0] + 500, a[1] - 700), (a[2] - 500, a[1] - 700))
                self.text("falm", "BEAM DETECTORS ACROSS ATRIUM", ((a[0] + a[2]) / 2, a[1] - 1500), self.S(1.6))
            for _, _, x, y in pts:
                self.detector(x, y, heat)
        # call points + sounders
        for d in self.m["doors"]:
            kinds = [self.rooms[x]["kind"] for x in (d["a"], d["b"]) if x != "OUT"]
            if d["exit"] or "stair" in kinds:
                inroom = d["a"] if d["a"] != "OUT" else d["b"]
                if "stair" in kinds and d["exit"] is False:
                    inroom = [x for x in (d["a"], d["b"]) if x != "OUT" and self.rooms[x]["kind"] != "stair"][0]
                ux, uy = self.inward(d, inroom)
                p = (d["pt"][0] + ux * 1400 + uy * 900, d["pt"][1] + uy * 1400 + ux * 900)
                self.rect("falm", p[0] - 150, p[1] - 150, p[0] + 150, p[1] + 150)
                self.n("call points")
        st = self.rooms["ST"]["rects"][0]
        for k in range(int((st[2] - st[0]) // 16800) + 1):
            x = st[0] + 4200 + k * 16800
            if x < st[2]:
                self.msp.add_circle(self.P(x, st[1] + 1200), self.S(1.0), dxfattribs={"layer": self.names["falm"]})
                self.text("falm", "B", (x, st[1] + 1200), self.S(1.2))
                self.n("sounders")
        el = [r for r in self.m["rooms"] if r["kind"] == "elec"]
        if el:
            q = el[0]["rects"][0]
            self.labelled_box("falm", "etxt", q[0] + 400, q[3] - 1500, q[0] + 1600, q[3] - 700, "FACP")

    def hose(self):
        for d in self.m["doors"]:
            kinds = [self.rooms[x]["kind"] for x in (d["a"], d["b"]) if x != "OUT"]
            stair = "stair" in kinds
            if not (d["exit"] or stair):
                continue
            side = [x for x in (d["a"], d["b"]) if x != "OUT" and self.rooms[x]["kind"] != "stair"]
            if not side:
                continue
            ux, uy = self.inward(d, side[0])
            p = (d["pt"][0] + ux * 900 - uy * 1700, d["pt"][1] + uy * 900 - ux * 1700)
            self.labelled_box("hose", "ftxt", p[0] - 450, p[1] - 200, p[0] + 450, p[1] + 200, "FHC" if stair else "HR", self.S(1.2))
            self.n("FHC/HR")
        for r in self.m["rooms"]:
            if r["kind"] == "firepump":
                q = r["rects"][0]
                self.labelled_box("hose", "ftxt", q[0] + 400, q[1] + 3000, q[2] - 400, q[1] + 9000, "FIRE WATER TANK", self.S(1.5))
                for k, nm in enumerate(("P1", "P2", "JP")):
                    c = (q[0] + 900 + k * 1000, q[3] - 1500)
                    self.msp.add_circle(self.P(*c), self.S(1.4), dxfattribs={"layer": self.names["hose"]})
                    self.text("ftxt", nm, c, self.S(1.2))
                self.text("ftxt", "FIRE PUMP SET (duty/standby/jockey) - pump room must open to outside route",
                          ((q[0] + q[2]) / 2, q[3] - 3600), self.S(1.2))

    def hvac(self):
        for r in self.m["rooms"]:
            k = r["kind"]
            if k in ("shop", "food", "anchor", "street", "baby", "prayer", "amen"):
                ex = self.excl(k)
                sp = self.sp_dif
                pts, cw, ch = self.grid([tuple(q) for q in r["rects"]], sp, 500, ex)
                for _, _, x, y in pts:
                    self.cross_sq("scd", (x + 350, y + 350), self.S(1.0))
                    self.n("supply diffusers")
        for r in self.m["rooms"]:
            if r["kind"] in ("shop", "anchor"):
                q = r["rects"][0]
                d = [x for x in self.doors_of(r["id"]) if "corr" in [self.rooms[o]["kind"] for o in (x["a"], x["b"]) if o != "OUT"]]
                if d:
                    px, py = d[0]["pt"]
                    ux, uy = self.inward(d[0], r["id"])
                    self.cross_sq("rcg", (px + ux * 1200 + uy * 1800, py + uy * 1200 + ux * 1800), self.S(1.2))
                    self.n("return grilles")
                    # take-off duct from corridor main into the shop, 400 wide
                    for sgn in (1,):
                        x0, y0 = px, py
                        L = 9000
                        if uy:
                            self.rect("sad", x0 - 200, min(y0, y0 + uy * L), x0 + 200, max(y0, y0 + uy * L))
                        else:
                            self.rect("sad", min(x0, x0 + ux * L), y0 - 200, max(x0, x0 + ux * L), y0 + 200)
                        self.n("duct take-offs")
        for r in self.m["rooms"]:
            q = r["rects"][0]
            if r["kind"] == "corr":
                yc = (q[1] + q[3]) / 2 + 700
                self.rect("sad", q[0] + 800, yc - 600, q[2] - 800, yc + 600)
                self.text("mtxt", "SUPPLY AIR MAIN 1200x600 (indicative, from AHU via ceiling void)",
                          ((q[0] + q[2]) / 2, yc + 600 + self.S(1.7)), self.S(1.5))
                self.n("duct mains")
            elif r["kind"] == "ahu":
                self.labelled_box("eqpt", "mtxt", q[0] + 600, q[1] + 600, q[2] - 600, q[1] + 5200, "AHU-1 / CHW PUMPS", self.S(1.5))
                self.text("mtxt", "CHILLERS ON ROOF (air-cooled, Gulf RoT)", ((q[0] + q[2]) / 2, q[1] + 6500), self.S(1.2))
            elif r["kind"] == "riser" and r["sub"] == "riser_m":
                self.cross_sq("eqpt", ((q[0] + q[2]) / 2, (q[1] + q[3]) / 2), 1500)
                self.text("mtxt", "M/P SHAFT", ((q[0] + q[2]) / 2, (q[1] + q[3]) / 2 + 2200), self.S(1.4))
                self.n("risers")
            elif r["kind"] == "riser":
                self.cross_sq("db", ((q[0] + q[2]) / 2, (q[1] + q[3]) / 2), 1500)
                self.text("etxt", "E/ELV SHAFT", ((q[0] + q[2]) / 2, (q[1] + q[3]) / 2 + 2200), self.S(1.4))
                self.n("risers")
            elif r["kind"] == "wc":
                x0, y0, x1, y1 = q
                self.cross_sq("rcg", ((x0 + x1) / 2, (y0 + y1) / 2), self.S(1.0))   # toilet extract grille (return/exhaust)
                self.n("exhaust grilles")

    def electrical(self):
        m = self.m
        for r in m["rooms"]:
            k, q = r["kind"], r["rects"][0]
            if k in ("shop", "food", "anchor"):
                ds = [d for d in self.doors_of(r["id"]) if "corr" in [self.rooms[o]["kind"] for o in (d["a"], d["b"]) if o != "OUT"]]
                if not ds:
                    ds = self.doors_of(r["id"])
                d = ds[0]
                ux, uy = self.inward(d, r["id"])
                dx = d["pt"][0] + ux * 300 + (1500 if uy else 0)
                dy = d["pt"][1] + uy * 300 + (1500 if ux else 0)
                lab = "DB-" + r["name"].split()[-1] if k != "anchor" else "DB-" + r["id"]
                self.labelled_box("db", "etxt", dx - 350, dy - 150, dx + 350, dy + 150, lab, self.S(1.0))
                self.line("tray", d["pt"], (dx, dy))
                self.n("shop DBs")
            elif k == "elec":
                self.labelled_box("db", "etxt", q[0] + 500, q[1] + 600, q[2] - 500, q[1] + 1500, "MDB", self.S(1.6))
                self.labelled_box("db", "etxt", q[0] + 500, q[1] + 2500, q[2] - 500, q[1] + 3300, "ATS", self.S(1.4))
                self.n("MDB")
            elif k == "gen":
                self.labelled_box("db", "etxt", q[0] + 500, q[1] + 1000, q[2] - 500, q[1] + 6500, "GEN SET", self.S(1.6))
            elif k == "corr":
                y = (q[1] + q[3]) / 2 - 1700
                self.line("tray", (q[0] + 600, y), (q[2] - 600, y))
                self.text("etxt", "FEEDER TRAY 300x50 from MDB", ((q[0] + q[2]) / 2, y - self.S(2.0)), self.S(1.3))
                for k2 in range(int((q[2] - q[0]) // 4200)):
                    x = q[0] + 2100 + k2 * 4200
                    self.msp.add_lwpolyline([self.P(x - 600, (q[1] + q[3]) / 2 + 2000), self.P(x + 600, (q[1] + q[3]) / 2 + 2000)],
                                            dxfattribs={"layer": self.names["lite"], "const_width": self.S(0.4)})
                    self.n("corridor luminaires")
        # luminaires in the mall street, outside the atrium void
        st = self.rooms["ST"]
        pts, _, _ = self.grid([tuple(q) for q in st["rects"]], 4200, 600, self.excl("street"))
        for _, _, x, y in pts:
            self.luminaire(x, y)
        # emergency lights + exit signs at exits
        for d in self.m["doors"]:
            kinds = [self.rooms[x]["kind"] for x in (d["a"], d["b"]) if x != "OUT"]
            if d["exit"] or "stair" in kinds:
                side = [x for x in (d["a"], d["b"]) if x != "OUT" and self.rooms[x]["kind"] != "stair"] or [d["a"]]
                ux, uy = self.inward(d, side[0])
                p = (d["pt"][0] + ux * 1000, d["pt"][1] + uy * 1000)
                self.labelled_box("emer", "etxt", p[0] - 450, p[1] - 150, p[0] + 450, p[1] + 150, "EXIT", self.S(0.9))
                self.n("exit signs")
        stq = st["rects"][0]
        for k in range(int((stq[2] - stq[0]) // 8400)):
            x = stq[0] + 4200 + k * 8400
            for y in (stq[1] + 1000, stq[3] - 1000):
                self.rect("emer", x - 200, y - 200, x + 200, y + 200)
                self.text("emer", "E", (x, y), self.S(1.0))
                self.n("emergency lights")

    def plumbing(self):
        for r in self.m["rooms"]:
            k, q = r["kind"], r["rects"][0]
            x0, y0, x1, y1 = q
            if k == "wc":
                w, h = x1 - x0, y1 - y0
                is_acc = r["sub"] == "wca"
                men = r["sub"] == "wcm"
                # wet-wall stack along the wall opposite the door side (long rooms: far end)
                far_y = y1 - 450 if True else y0 + 450
                door = [d for d in self.doors_of(r["id"])][0]
                toward_top = door["pt"][1] < (y0 + y1) / 2
                ys = lambda t: (y0 + t) if not toward_top else (y1 - t)
                sgn = 1 if not toward_top else -1
                n_pans = 1 if is_acc else max(2, min(5, int((h - 3000) // 900)))
                for i in range(n_pans):
                    yy = ys(900 + i * 900) if not is_acc else ys(h / 2)
                    xx = x0 + 450 if not is_acc else x0 + 600
                    self.msp.add_ellipse(self.P(xx, yy), major_axis=(0, 420 * self.f, 0), ratio=0.65, dxfattribs={"layer": self.names["fixt"]})
                    self.line("fixt", (xx - 400, yy - 450), (xx + 400, yy - 450)) if i == n_pans - 1 else None
                    self.n("WC pans")
                if men:
                    for i in range(3):
                        yy = ys(1200 + i * 700)
                        self.rect("fixt", x1 - 450, yy - 150, x1 - 100, yy + 150)
                        self.n("urinals")
                nb = 1 if is_acc else 3
                for i in range(nb):
                    yy = ys(h - 1500 - i * 800) if not is_acc else ys(h / 2 + 900)
                    xx = x1 - 400 if not is_acc else x1 - 400
                    self.rect("fixt", xx - 250, yy - 200, xx + 250, yy + 200)
                    self.n("basins")
                # stack + branches
                self.msp.add_circle(self.P(x0 + 150, ys(150)), self.S(0.9), dxfattribs={"layer": self.names["sanr"]})
                self.text("ptxt", "SS", (x0 + 150, ys(150)), self.S(1.0))
                self.line("sanr", (x0 + 150, ys(150)), (x0 + 150, ys(900 + (n_pans - 1) * 900)))
                self.line("dcw", (x1 - 150, ys(150)), (x1 - 150, ys(h - 800)))
                self.text("ptxt", "CW", (x1 - 150, ys(150)), self.S(1.0))
                self.msp.add_circle(self.P((x0 + x1) / 2, (y0 + y1) / 2), self.S(0.6), dxfattribs={"layer": self.names["fixt"]})   # FD
                self.n("floor drains")
            elif r["kind"] == "prayer" and r["sub"] in ("prm", "prw"):
                for i in range(4):
                    self.msp.add_circle(self.P(x0 + 600 + i * 700, y1 - 500), self.S(0.8), dxfattribs={"layer": self.names["fixt"]})
                self.text("ptxt", "ABLUTION TAPS", ((x0 + x1) / 2, y1 - 1200), self.S(1.1))
                self.n("ablution taps", 4)
            elif r["kind"] == "food":
                self.labelled_box("fixt", "ptxt", x0 + 300, y0 + 300, x0 + 1100, y0 + 800, "GT", self.S(1.0))
                self.n("grease traps")

    def run(self):
        self.architecture()
        self.hvac()
        self.sprinklers()
        self.detectors()
        self.hose()
        self.electrical()
        self.plumbing()


def legend(ov, doc, prof, spec):
    sh = prof["sheet"]
    inch = sh["units"].startswith("in")
    k = 1 / 25.4 if inch else 1.0
    w, h, m = sh["w"], sh["h"], sh["margin"]
    psp = doc.layouts.get(sh["name"])
    L = 70 * k
    vps = [v for v in psp.query("VIEWPORT") if v.dxf.id != 1]
    for v in vps:
        old_h = v.dxf.height
        v.dxf.height = old_h - L
        cx, cy = v.dxf.center[0], v.dxf.center[1]
        v.dxf.center = (cx, cy + L / 2)
        v.dxf.view_height = v.dxf.view_height * (old_h - L) / old_h
        vw = v.dxf.width
    x0, y0 = 2 * m, m * 1.6
    vw_ = vw if vps else w - 3 * m
    psp.add_lwpolyline([(x0, y0), (x0 + vw_, y0), (x0 + vw_, y0 + L - m), (x0, y0 + L - m)], close=True,
                       dxfattribs={"layer": LGND})
    th = 2.2 * k
    style = prof["text"]["style"]
    psp.add_text("MEP / ARCH OVERLAY LEGEND - indicative layouts, not hydraulic/aerodynamic designs; spacing per references/disciplines/mep.md",
                 height=th * 1.1, dxfattribs={"layer": LGND, "style": style}).set_placement((x0 + 2 * k, y0 + L - m - 4 * k), align=LEFT)
    items = []
    for key in ("head", "pipe", "falm", "hose", "scd", "rcg", "sad", "eqpt", "lite", "emer", "db", "tray", "fixt", "dcw", "sanr"):
        items.append((key, ov.names[key], LAYERS[key][5]))
    for key in ("strs", "otln", "evtr"):
        items.append((key, ov.names[key], ARCH[key][3]))
    cols = 4
    rows = math.ceil(len(items) / cols)
    cw = vw_ / cols
    rh = (L - m - 12 * k) / rows
    for i, (key, name, desc) in enumerate(items):
        c, r = divmod(i, rows)
        x = x0 + 3 * k + c * cw
        y = y0 + L - m - 9 * k - r * rh
        aci = doc.layers.get(name).dxf.color
        psp.add_line((x, y), (x + 8 * k, y), dxfattribs={"layer": LGND, "color": aci})
        psp.add_circle((x + 4 * k, y), 1.2 * k, dxfattribs={"layer": LGND, "color": aci})
        psp.add_text(f"{name}  {desc}", height=th * 0.9, dxfattribs={"layer": LGND, "style": style}).set_placement((x + 10 * k, y), align=LEFT)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("--dxf")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    sp = Path(a.spec)
    spec = json.loads(sp.read_text(encoding="utf-8"))
    if "mall" not in spec:
        raise SystemExit("spec has no 'mall' block - mep_overlay.py needs a spec written by gen_mall.py")
    prof = dxf_plan.load_profile(spec["country"])
    for kk, v in spec.get("profile", {}).items():
        prof[kk] = {**prof[kk], **v} if isinstance(v, dict) and isinstance(prof.get(kk), dict) else v
    dxf = Path(a.dxf or sp.with_suffix(".dxf"))
    doc = ezdxf.readfile(dxf)
    ov = Ov(spec, doc, prof)
    ov.run()
    legend(ov, doc, prof, spec)
    out = Path(a.out or dxf.with_name(dxf.stem + "-MEP.dxf"))
    doc.saveas(out)
    print(f"wrote {out}  " + ", ".join(f"{k}={v}" for k, v in sorted(ov.counts.items())))


if __name__ == "__main__":
    main()
