#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Index page linking several project dashboards as cards.

Usage:
    uv run -q scripts/dashboard_index.py <root> [-o index.html] [--title "Mall in every country"] [--no-build]

Every immediate sub-folder of <root> that holds a project (spec JSON / mall.json) becomes a card:
render or plan thumbnail, country, building type, pipeline dots, audit status. Each card links to
<sub>/dashboard.html, which is (re)built first unless --no-build is given. One static file, relative
links only, works from a double-click.
"""
from __future__ import annotations

import argparse
import importlib.util
import os
import sys
from pathlib import Path
from urllib.parse import quote, unquote

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("dashboard", HERE / "dashboard.py")
dash = importlib.util.module_from_spec(_spec)
sys.modules["dashboard"] = dash
_spec.loader.exec_module(dash)
esc = dash.esc

EXTRA_CSS = r"""
header.top{padding-bottom:0}
.lead{color:var(--ink2);max-width:62ch;margin:6px 0 0}
.bar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:26px 0 0}
.bar .filter{margin:0}
.seg{display:flex;gap:6px;flex-wrap:wrap}
.seg button{font:inherit;font-size:13px;border:1px solid var(--line);background:var(--card);color:var(--ink2);padding:6px 14px;border-radius:999px;cursor:pointer}
.seg button[aria-pressed=true]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink);font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:18px;margin-top:22px}
.pc{display:flex;flex-direction:column;overflow:hidden;color:inherit;transition:transform .15s,box-shadow .15s}
.pc:hover{text-decoration:none;transform:translateY(-2px);box-shadow:0 2px 4px rgba(20,22,30,.06),0 12px 32px rgba(20,22,30,.1)}
.pc[hidden]{display:none}
.th{aspect-ratio:16/10;background:#fff;overflow:hidden;position:relative;border-bottom:1px solid var(--line)}
.th img{width:100%;height:100%;object-fit:cover}
.th.plan img{object-fit:contain}
.th.none{display:grid;place-items:center;background:var(--soft);font-size:44px;color:var(--ink2);font-weight:300;letter-spacing:.04em}
.th .tag{position:absolute;inset-inline-start:10px;top:10px;background:rgba(20,22,30,.72);color:#fff;border-radius:999px;padding:2px 10px;font-size:11.5px}
.pc .in{padding:14px 16px 16px;display:flex;flex-direction:column;gap:8px;flex:1}
.pc h3{margin:0;font-size:17px;display:flex;align-items:center;gap:8px;line-height:1.25}
.pc .sub{color:var(--ink2);font-size:13px;margin:0}
.dots{display:flex;gap:5px;margin-top:2px}
.dots i{width:22px;height:5px;border-radius:3px;background:var(--c)}
.pc .foot{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:auto;padding-top:10px;font-size:12.5px;color:var(--ink2);flex-wrap:wrap}
.summary{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:12px;margin-top:28px}
"""

FILTER_JS = r"""
(function(){var q='',mode='all',cards=[].slice.call(document.querySelectorAll('.pc')),cnt=document.getElementById('cnt');
function run(){var n=0;cards.forEach(function(c){var ok=(!q||c.dataset.s.indexOf(q)>=0)&&(mode==='all'||(mode==='render'&&c.dataset.r==='1')||(mode==='review'&&c.dataset.v==='1'));c.hidden=!ok;if(ok)n++});cnt.textContent=n+' of '+cards.length}
document.getElementById('q').addEventListener('input',function(e){q=e.target.value.toLowerCase();run()});
document.querySelectorAll('.seg button').forEach(function(b){b.addEventListener('click',function(){mode=b.dataset.m;document.querySelectorAll('.seg button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});run()})});run()})();
"""


def rel_url(target: Path, base: Path) -> str:
    return quote(os.path.relpath(target, base).replace("\\", "/"), safe="/")


def overall(D):
    st = [s["state"] for s in D["pipeline"] if s["key"] in ("code", "drawings", "mep", "bim")]
    code = next(s for s in D["pipeline"] if s["key"] == "code")["state"]
    if "fail" in st:
        return "fail", "Fail"
    if code == "warn":
        return "warn", "Verify"
    if code == "ok":
        return "ok", "Pass"
    return "none", "No audit"


def card(D, href, out_dir):
    imgs = D["images"]
    pick = next((i for i in imgs if i["kind"] == "render"), None)
    kind = "render"
    if pick is None:
        pick = next((i for i in imgs if i["kind"] == "plan"), None) or next(
            (i for i in imgs if i["kind"] in ("mep", "sheet")), None)
        kind = "plan"
    if pick:
        src = rel_url(pick["path"], out_dir)
        th = (f'<div class="th {kind}"><img src="{src}" alt="" loading="lazy">'
              f'<span class="tag">{"Render" if kind == "render" else "Plan"}</span></div>')
    else:
        th = f'<div class="th none">{esc((D["cc"] or "?").upper())}</div>'
    state, label = overall(D)
    at = D["audit_total"]
    dots = "".join(f'<i class="s-{s["state"]}" title="{esc(s["en"])}: {esc(s["detail"])}"></i>' for s in D["pipeline"])
    audit = f'{at["PASS"]} pass · {at["WARN"]} warn · {at["FAIL"]} fail' if D["has_audit"] else "no audit file"
    m = D["mall"] or {}
    bits = [f'{len(D["levels"])} level{"s" if len(D["levels"]) != 1 else ""}', f'{D["rooms_total"]} rooms']
    if m.get("gla_m2"):
        bits.append(f'GLA {m["gla_m2"]:,} m²')
    search = f'{D["country"]} {D["cc"]} {D["title"]} {D["type"]}'.lower()
    return (f'<a class="card pc" href="{href}" data-s="{esc(search)}" data-r="{1 if pick and kind == "render" else 0}" '
            f'data-v="{1 if state in ("warn", "fail") else 0}">{th}<div class="in">'
            f'<h3><span class="flag" aria-hidden="true">{D["flag"]}</span>{esc(D["country"])}</h3>'
            f'<p class="sub">{esc(D["title"])} · {esc(D["type"])}</p><div class="dots" aria-hidden="true">{dots}</div>'
            f'<div class="foot"><span>{esc(audit)}</span>{dash.pill(state, label)}</div>'
            f'<div class="foot" style="margin-top:0;padding-top:0">{esc(" · ".join(bits))}</div></div></a>')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("-o", "--out", help="default <root>/index.html")
    ap.add_argument("--title", help="page title (default: folder name)")
    ap.add_argument("--no-build", action="store_true", help="do not rebuild the sub-folder dashboards")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    out = Path(a.out).resolve() if a.out else root / "index.html"
    out_dir = out.parent
    items = []
    for sub in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        if not any(c.is_file() and (c.name.lower() == "mall.json" or dash.is_spec_file(c)) for c in sub.iterdir()):
            continue
        html_path = sub / "dashboard.html"
        if a.no_build and html_path.exists():
            D = dash.collect(sub, html_path)
        else:
            _, D = dash.build(sub, html_path)
        items.append((D, html_path))
    if not items:
        sys.exit(f"no project sub-folders in {root}")
    items.sort(key=lambda t: (t[0]["country"] or "").lower())
    cards = "".join(card(D, rel_url(h, out_dir), out_dir) for D, h in items)
    n = len(items)
    with_r = sum(1 for D, _ in items if any(i["kind"] == "render" for i in D["images"]))
    tot = {k: sum(D["audit_total"][k] for D, _ in items) for k in ("PASS", "WARN", "FAIL")}
    rooms = sum(D["rooms_total"] for D, _ in items)
    stat = lambda v, l: f'<div class="card stat"><b>{v}</b><span>{esc(l)}</span></div>'
    summary = "".join([stat(n, "projects"), stat(with_r, "with 3D render"), stat(f"{rooms:,}", "rooms drawn"),
                       stat(tot["PASS"], "audit checks passed"), stat(tot["WARN"], "audit warnings"),
                       stat(tot["FAIL"], "audit failures")])
    title = a.title or root.name.replace("-", " ").replace("_", " ").title()
    readme = ' <a href="README.md">Method and sources</a>.' if (root / "README.md").exists() else ""
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="color-scheme" content="light dark"><title>{esc(title)} — index</title>'
            f'<style>{dash.CSS}{EXTRA_CSS}</style></head><body>'
            f'<header class="top"><div class="wrap"><div class="eyebrow">ArchMind · project index</div><h1>{esc(title)}</h1>'
            f'<p class="lead">{n} sample projects, one dashboard each: renders, plans, code check, design audit and downloads. '
            f'Sample output, not for construction; every number carries its source.{readme}</p>'
            f'<div class="summary">{summary}</div>'
            f'<div class="bar"><input id="q" class="filter" type="search" placeholder="Search country or project…" aria-label="Search">'
            f'<div class="seg"><button data-m="all" aria-pressed="true">All</button>'
            f'<button data-m="render" aria-pressed="false">With render</button>'
            f'<button data-m="review" aria-pressed="false">Needs verify</button></div>'
            f'<span id="cnt" class="ar"></span></div></div></header>'
            f'<main class="wrap"><div class="grid">{cards}</div></main>'
            f'<footer class="wrap">Generated by ArchMind <code>dashboard_index.py</code>.</footer>'
            f'<script>{FILTER_JS}</script></body></html>')
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out}  ({n} projects)")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    main()
