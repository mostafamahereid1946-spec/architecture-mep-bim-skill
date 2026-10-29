#!/usr/bin/env bash
# Rebuild every mall example: bash examples/malls/build_all.sh [cc ...]   (run from the repo root)
# per country: gen_mall -> dxf_plan -> mep_overlay -> plan_audit -> ifc_from_spec (GF)
set -u
S=skills/architecture-mep-bim/scripts
OUT=examples/malls
build() {
  cc=$1
  uv run -q $S/gen_mall.py --country "$cc" --out "$OUT/$cc" || return 1
  for f in $(ls $OUT/$cc | grep -E '^(GF|L[0-9])\.json$'); do
    lv=${f%.json}
    uv run -q --with ezdxf $S/dxf_plan.py "$OUT/$cc/$lv.json" >/dev/null
    uv run -q $S/mep_overlay.py "$OUT/$cc/$lv.json" >/dev/null
    uv run -q --with shapely --with networkx $S/plan_audit.py "$OUT/$cc/$lv.json" > "$OUT/$cc/$lv-audit.txt"
  done
  h=$(grep -A1 '"gf_height_mm"' $OUT/$cc/mall.json | grep -o '[0-9]\+' | head -1)
  uv run -q --with ifcopenshell $S/ifc_from_spec.py "$OUT/$cc/GF.json" --height "${h:-5000}" > "$OUT/$cc/ifc.txt"
  echo "$cc done"
}
export -f build; export S OUT
if [ $# -gt 0 ]; then ccs="$@"; else ccs=$(ls $S/profiles | sed 's/\.json//'); fi
printf '%s\n' $ccs | xargs -P${JOBS:-2} -I{} bash -c 'build {}'
