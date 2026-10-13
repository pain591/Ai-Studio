"""Build the compact Xuhui dataset that the UI mockup embeds.

Inputs (downloaded separately, not committed):
  sh_full.json   Shanghai district outlines, Aliyun DataV GeoAtlas (GCJ-02)
  ctx.json       OSM land use, parks, water, major roads, metro lines in Xuhui (Overpass)
  bld.json       OSM buildings in Xuhui (Overpass)
  stations.json  OSM railway stations around Xuhui (Overpass)

Output: data.js, defining window.XH. Coordinates are stored as integers in
1e-5 degree units relative to ORIGIN to keep the file small.

Planning attributes attached to plots here (FAR, height caps, zones) are
illustrative placeholders for the mockup, not real regulatory values.
"""
import hashlib
import warnings
import json
import math
import sys
from pathlib import Path

from shapely.geometry import LineString, Point, Polygon, MultiPolygon, shape
from shapely.ops import transform, unary_union
from shapely.strtree import STRtree

warnings.filterwarnings("ignore", category=DeprecationWarning)
SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2])
ORIGIN = (121.30, 31.00)
LAT0 = 31.18
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0


def gcj_to_wgs(lon, lat):
    a, ee = 6378245.0, 0.00669342162296594323

    def tlat(x, y):
        r = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
        r += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
        r += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
        r += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
        return r

    def tlon(x, y):
        r = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
        r += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
        r += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
        r += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
        return r

    dlat = tlat(lon - 105.0, lat - 35.0)
    dlon = tlon(lon - 105.0, lat - 35.0)
    radlat = lat / 180.0 * math.pi
    magic = 1 - ee * math.sin(radlat) ** 2
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * math.pi)
    dlon = (dlon * 180.0) / (a / sqrtmagic * math.cos(radlat) * math.pi)
    return lon - dlon, lat - dlat


def to_m(g):
    return transform(lambda x, y, z=None: ((x - ORIGIN[0]) * KX, (y - ORIGIN[1]) * KY), g)


def to_deg(g):
    return transform(lambda x, y, z=None: (x / KX + ORIGIN[0], y / KY + ORIGIN[1]), g)


def q(coords):
    out = []
    for x, y in coords:
        out += [round((x - ORIGIN[0]) * 1e5), round((y - ORIGIN[1]) * 1e5)]
    return out


def polys(g):
    if g.is_empty:
        return []
    if isinstance(g, Polygon):
        return [g]
    if isinstance(g, MultiPolygon):
        return list(g.geoms)
    return [p for p in getattr(g, "geoms", []) if isinstance(p, Polygon)]


def ring(p):
    return q(list(p.exterior.coords)[:-1])


def way_poly(e):
    pts = [(n["lon"], n["lat"]) for n in e.get("geometry", [])]
    if len(pts) < 4 or pts[0] != pts[-1]:
        return None
    p = Polygon(pts)
    return p if p.is_valid else p.buffer(0)


def h01(s):
    return int(hashlib.md5(str(s).encode()).hexdigest()[:8], 16) / 0xFFFFFFFF


# ---------- districts ----------
dist = json.load(open(SRC / "sh_full.json"))
districts, xuhui = [], None
for f in dist["features"]:
    g = shape(f["geometry"])
    g = transform(lambda x, y, z=None: gcj_to_wgs(x, y), g)
    name = f["properties"]["name"]
    code = f["properties"]["adcode"]
    if code == 310104:
        xuhui = g
    gm = to_m(g).simplify(15 if code == 310104 else 80)
    rings = [ring(to_deg(p)) for p in polys(gm) if p.area > 2e5]
    districts.append({"name": name, "code": code, "rings": rings,
                      "c": q([to_deg(gm).representative_point().coords[0]])})
xuhui = xuhui.buffer(0)
xuhui_m = to_m(xuhui)
xuhui_grow = to_deg(xuhui_m.buffer(60))

# ---------- land use ----------
CAT = {
    "residential": "R", "commercial": "C8", "retail": "C2", "industrial": "M1",
    "construction": "X", "brownfield": "X", "greenfield": "X",
    "grass": "G", "meadow": "G", "forest": "G", "flowerbed": "G", "recreation_ground": "G",
    "railway": "S", "military": "D", "religious": "CR",
}
ctx = json.load(open(SRC / "ctx.json"))["elements"]
raw_plots, water, roads, metro = [], [], [], []
for e in ctx:
    t = e.get("tags", {})
    if e["type"] != "way":
        continue
    if "landuse" in t or t.get("leisure") == "park":
        cat = "G" if t.get("leisure") == "park" else CAT.get(t["landuse"])
        p = way_poly(e)
        if cat and p is not None:
            raw_plots.append((p, cat, t.get("name"), e["id"]))
    elif t.get("natural") == "water":
        p = way_poly(e)
        if p is not None:
            for pp in polys(p.intersection(xuhui_grow)):
                if to_m(pp).area > 200:
                    water.append(ring(pp))
    elif "highway" in t:
        pts = [(n["lon"], n["lat"]) for n in e["geometry"]]
        ls = LineString(pts).intersection(xuhui_grow)
        for part in getattr(ls, "geoms", [ls]):
            if isinstance(part, LineString) and len(part.coords) > 1:
                roads.append({"k": t["highway"][0], "n": t.get("name", ""), "p": q(part.coords)})
    elif t.get("railway") == "subway":
        pts = [(n["lon"], n["lat"]) for n in e["geometry"]]
        if len(pts) > 1:
            name = t.get("name", "")
            line = "".join(ch for ch in name if ch.isdigit())
            metro.append({"l": line, "p": q(pts)})

plots = []
for p, cat, name, oid in raw_plots:
    for pp in polys(p.intersection(xuhui)):
        pm = to_m(pp)
        if pm.area < 400:
            continue
        plots.append({"g": pp, "gm": pm, "cat": cat, "name": name, "osm": oid})
plots.sort(key=lambda d: -d["gm"].area)

# ---------- stations ----------
st = json.load(open(SRC / "stations.json"))["elements"]
tags = {e["id"]: e["tags"] for e in st if "tags" in e}
pos = {e["id"]: (e["lon"], e["lat"]) for e in st if "lat" in e}
by_name = {}
for i, t in tags.items():
    if i in pos and t.get("name") and t.get("station") == "subway":
        nm = t["name"].replace("（在建）", "")
        by_name.setdefault(nm, {"pts": [], "built": "在建" not in t["name"]})["pts"].append(pos[i])
stations = []
for nm, d in by_name.items():
    x = sum(p[0] for p in d["pts"]) / len(d["pts"])
    y = sum(p[1] for p in d["pts"]) / len(d["pts"])
    if xuhui_grow.buffer(0.004).contains(Point(x, y)):
        stations.append({"n": nm, "p": q([(x, y)]), "b": d["built"], "pt": Point(x, y)})

# ---------- buildings ----------
bl = json.load(open(SRC / "bld.json"))["elements"]
buildings, named = [], {}


def est_height(t, area, oid):
    if "height" in t:
        try:
            return float(t["height"].replace("m", "").strip()), 0
        except ValueError:
            pass
    if "building:levels" in t:
        try:
            return float(t["building:levels"]) * 3.2 + 1, 0
        except ValueError:
            pass
    b, r = t.get("building", "yes"), h01(oid)
    if b in ("house", "detached", "terrace") or area < 150:
        return 6 + r * 5, 1
    if b in ("industrial", "warehouse", "factory", "shed"):
        return 9 + r * 6, 1
    if b in ("commercial", "office", "retail", "hotel"):
        return 18 + r * 50, 1
    if area < 450:
        return 9 + r * 6, 1
    if area < 1300:
        return 17 + r * 4, 1
    return 24 + r * 60, 1


for e in bl:
    t = e.get("tags", {})
    if e["type"] != "way":
        continue
    p = way_poly(e)
    if p is None or p.is_empty or not isinstance(p, Polygon):
        continue
    area = to_m(p).area
    h, est = est_height(t, area, e["id"])
    buildings.append({"g": p, "h": round(h, 1), "e": est, "n": t.get("name", "")})
    if t.get("name"):
        named[t["name"]] = p

# ---------- overlay zones (approximate outlines for the mockup) ----------
def zone_poly(pts):
    return Polygon(pts)


pagoda = named.get("龙华塔")
pagoda_pt = pagoda.centroid if pagoda is not None else Point(121.4508, 31.1756)
pagoda_m = to_m(pagoda_pt)
xjh_pt = Point(121.4375, 31.1945)
zones = [
    {"id": "heritage", "label": "衡山路–复兴路历史文化风貌区", "en": "Hengshan–Fuxing Rd heritage area",
     "g": zone_poly([(121.4290, 31.2150), (121.4400, 31.2195), (121.4530, 31.2160), (121.4585, 31.2085),
                     (121.4535, 31.2005), (121.4440, 31.1968), (121.4365, 31.1990), (121.4305, 31.2060)])},
    {"id": "core", "label": "徐家汇城市副中心", "en": "Xujiahui sub-centre (high-intensity core)",
     "g": to_deg(to_m(xjh_pt).buffer(650, 24))},
    {"id": "westbund", "label": "徐汇滨江 · 西岸", "en": "West Bund riverfront redevelopment",
     "g": zone_poly([(121.4520, 31.1960), (121.4640, 31.1950), (121.4700, 31.1850), (121.4660, 31.1700),
                     (121.4560, 31.1580), (121.4480, 31.1600), (121.4560, 31.1730), (121.4590, 31.1850)])},
    {"id": "caohejing", "label": "漕河泾开发区", "en": "Caohejing Hi-Tech Park",
     "g": zone_poly([(121.3880, 31.1790), (121.4110, 31.1815), (121.4140, 31.1655), (121.3920, 31.1610)])},
    {"id": "relic", "label": "龙华塔 文物保护范围 / 建设控制地带", "en": "Longhua Pagoda protection + construction-control zone",
     "g": to_deg(pagoda_m.buffer(250, 24))},
]
for z in zones:
    z["g"] = z["g"].intersection(xuhui_grow)

# ---------- per-plot analysis ----------
plot_tree = STRtree([d["g"] for d in plots])
res_m = [d["gm"] for d in plots if d["cat"] == "R"]
res_tree = STRtree(res_m)
st_m = [to_m(s["pt"]) for s in stations if s["b"]]
st_names = [s["n"] for s in stations if s["b"]]
SETBACK = {"R": 8, "C8": 6, "C2": 5, "M1": 6, "X": 6, "CR": 5, "D": 0, "G": 0, "S": 0}
out_plots = []
for i, d in enumerate(plots):
    gm = d["gm"]
    c = gm.representative_point()
    dists = [c.distance(s) for s in st_m]
    k = min(range(len(dists)), key=dists.__getitem__) if dists else None
    zs = [z["id"] for z in zones if to_m(z["g"]).intersects(gm) and to_m(z["g"]).intersection(gm).area > 0.15 * gm.area]
    near_res = any(r is not gm and r.distance(gm) < 35 for r in res_tree.geometries.take(res_tree.query(gm.buffer(35))))
    inset = gm.buffer(-SETBACK.get(d["cat"], 5), join_style=2)
    inset_ring = ring(to_deg(max(polys(inset), key=lambda p: p.area))) if not inset.is_empty and polys(inset) else []
    out_plots.append({
        "i": i, "c": d["cat"], "n": d["name"] or "", "a": round(gm.area),
        "r": [ring(p) for p in polys(d["g"])][:1][0], "in": inset_ring,
        "z": zs, "st": st_names[k] if k is not None else "", "sd": round(dists[k]) if k is not None else 99999,
        "nr": bool(near_res), "pc": q([to_deg(c).coords[0]]),
        "pd": round(c.distance(pagoda_m)),
    })

# building -> plot (centroid containment, smallest containing plot wins)
out_b = []
for b in buildings:
    cen = b["g"].representative_point()
    hits = [j for j in plot_tree.query(cen) if plots[j]["g"].contains(cen)]
    pid = min(hits, key=lambda j: plots[j]["gm"].area) if hits else -1
    out_b.append([b["h"], b["e"], int(pid), ring(b["g"])])

landmarks = []
for nm in ["龙华塔", "徐家汇圣依纳爵主教座堂", "上海体育馆", "上海游泳馆", "上海南站", "东方商厦"]:
    if nm in named:
        landmarks.append({"n": nm, "p": q([named[nm].centroid.coords[0]])})

data = {
    "origin": ORIGIN,
    "districts": districts,
    "plots": out_plots,
    "buildings": out_b,
    "water": water,
    "roads": roads,
    "metro": metro,
    "stations": [{"n": s["n"], "p": s["p"], "b": s["b"]} for s in stations],
    "zones": [{"id": z["id"], "label": z["label"], "en": z["en"], "r": [ring(p) for p in polys(z["g"])]} for z in zones],
    "landmarks": landmarks,
    "stats": {"buildings": len(out_b), "tagged_heights": sum(1 for b in out_b if b[1] == 0),
              "plots": len(out_plots), "stations": sum(1 for s in stations if s["b"]),
              "roads": len(roads), "osm_timestamp": "2026-05-31"},
}
OUT.write_text("window.XH=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("plots", len(out_plots), "buildings", len(out_b), "water", len(water), "roads", len(roads),
      "metro", len(metro), "stations", len(stations), "bytes", OUT.stat().st_size)
from collections import Counter
print(Counter(p["c"] for p in out_plots))
cands = [p for p in out_plots if "westbund" in p["z"] and p["c"] in ("X", "C8", "C2") and 8000 < p["a"] < 80000]
print("westbund candidates", [(p["i"], p["c"], p["n"], p["a"], p["st"], p["sd"]) for p in cands][:20])
