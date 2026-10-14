# Shanghai Plot Atlas prototype

A clickable prototype of the plot map for Xuhui district. Open `index.html` through a local
web server; it loads `data.js` (map data built by `build_data.py`).

## Run it on your computer

```sh
cd mockup
python3 -m http.server 8000
```

Then open <http://localhost:8000> in Chrome, Edge or Safari.

## Use the Amap (高德) base map

The built-in map draws buildings from OpenStreetMap, and most of their heights are estimates.
The Amap base map adds Amap's real 3D buildings, street and place labels, and satellite
imagery, with the plots, zones and buildable envelope drawn on top.

Amap only works when the page is opened from your computer or your own website. It does not
work inside the claude.ai preview link, which blocks scripts from webapi.amap.com.

1. Sign in at [lbs.amap.com](https://lbs.amap.com) (高德开放平台) with a mainland China mobile
   number and complete developer verification (个人认证 is enough for development).
2. In the console, go to 应用管理 › 我的应用, create an app, and add a key with the service
   platform **Web端 (JS API)**. Amap shows a **Key** and a **安全密钥** (security code).
3. Optional: in the key settings, limit it to your domain or `localhost`.
4. Open the prototype, go to **地图 Map › 底图 Base map**, choose **高德 Amap** or **卫星 Satellite**,
   paste the key and security code, then press **保存并加载 Save and load**.

The key and code are saved only in your browser (localStorage), not in this repository.
After changing a key, reload the page.

Free personal keys cover development and demos. A public commercial product needs Amap's
commercial licence (商用授权). For production, Amap recommends serving the security code
through your own proxy rather than shipping it in the page.

## What changes with Amap

| Item | Built-in map | Amap base map |
| --- | --- | --- |
| Buildings | OpenStreetMap footprints, most heights estimated | Amap's 3D buildings |
| Labels | Our metro and landmark labels | Amap's full street, place and station labels |
| Imagery | None | Satellite option |
| Plots, zones, metro | Drawn by the app | Drawn by the app on top of Amap |
| Selected plot | Existing buildings hidden, test design shown | Amap buildings on the plot hidden, test design shown |
| Coordinates | WGS-84 | Converted to GCJ-02 (Amap's system) |

Map data © OpenStreetMap contributors (ODbL). Base map © AutoNavi (高德).
