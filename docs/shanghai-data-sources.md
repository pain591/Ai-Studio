# Shanghai Plot Atlas: research notes on sources, laws and data

> Status: research notes for the UI prototype, October 2026. They are not legal advice.
> Every regulation listed here must be confirmed as the current version with the Shanghai
> Planning and Natural Resources Bureau (上海市规划和自然资源局, ghzyj.sh.gov.cn) before the
> product relies on it.

## 1. What the product does

The product turns scattered Shanghai planning documents (PDF plan drawings, public notices,
technical regulations, land sale notices) into a 3D map. A user clicks any plot and sees:

- what may be built there
- how big and how tall it may be
- which rules apply, each with the document it comes from

The first district is **Xuhui (徐汇区)**. It was chosen because it contains most kinds of
planning constraint in one place:

| Area | Why it matters for the rules engine |
|---|---|
| Hengshan–Fuxing Road heritage area (衡山路–复兴路历史文化风貌区) | Height and style limits, listed buildings that cannot be demolished |
| Xujiahui sub-centre (徐家汇城市副中心) | High-intensity zone with higher floor-area ratios and tall towers |
| West Bund (徐汇滨江 / 西岸) | Riverfront redevelopment, public waterfront, Shanghai's AI start-up cluster |
| Caohejing Hi-Tech Park (漕河泾开发区) | Industrial and R&D land, multi-storey industry (工业上楼) |
| Longhua Temple and Pagoda (龙华寺 / 龙华塔) | Cultural relic protection and construction-control zones |

## 2. Regulations and standards to ingest

| Document | What it controls | Version found | Link |
|---|---|---|---|
| 上海市控制性详细规划技术准则 | Land-use codes, density zones, plot indicators (floor-area ratio, height, coverage, green ratio) | 2016 revision. No newer edition was found; check. | [PDF](https://hd.ghzyj.sh.gov.cn/zcfg/ghbz/201701/P020170111543883631659.pdf) |
| 上海市控制性详细规划制定办法 (沪府令34号) | How detailed control plans (控规) are made, changed and publicly notified | In force since 1 Nov 2015 | ghzyj.sh.gov.cn |
| 上海市详细规划实施深化管理规定 (沪规划资源详〔2020〕503号) | Refining an approved detailed plan at project stage | Nov 2020 | ghzyj.sh.gov.cn |
| 上海市城市规划管理技术规定（土地使用 建筑管理） | Setbacks, building spacing, sunlight, height and boundary rules | 2003, amended 2010. Its interpretation notes (沪规法〔2007〕524号) were confirmed as still applicable in Apr 2025. | [PDF](https://www.shanghai.gov.cn/cmsres/86/86b1c89fade347b3b2349e077bfe8a99/0e5e011bfdea700a47c78f3c9c55d3af.pdf) |
| 上海市日照分析技术规范 | How sunlight on neighbouring homes is calculated | 2023 | ghzyj.sh.gov.cn |
| 上海市历史文化风貌区和优秀历史建筑保护条例 | Heritage areas, protected roads, listed buildings | Revised 2019. The protection system then covered 44 heritage areas, 144 protected roads and 632 listed historic buildings (the list has since grown). | [Study](https://www.shplanning.com.cn/archive/download/id/1342.html) |
| 上海市城市更新条例 | Urban renewal procedures | 2021 | [PDF](https://www.shanghai.gov.cn/cmsres/8d/8df5e015491046f496dae5d29829049c/790a2c7dacb13573183d55b5abfd7b27.pdf) |
| Heritage-area renewal guidance (沪规划资源风〔2025〕9号) | Urban renewal inside heritage areas (trial) | Jan 2025 | [PDF](https://ghzyj.sh.gov.cn/cmsres/b5/b5842750c3b947ab90c96badc780ddb9/7e0a2ff68587c3be66ff9954025c14c7.pdf) |
| 上海市城市总体规划 (2017–2035) (国函〔2017〕147号) | Citywide structure. Caps construction land at 3,200 km² by 2035. | 2017 | ghzyj.sh.gov.cn |
| Cultural relics law (文物保护法): protection and construction-control zones | Building limits around protected relics such as Longhua Pagoda | National law plus municipal designations | — |

## 3. Plot-level data: where the numbers live

The binding numbers for a plot (land use, floor-area ratio, height, green ratio) live in
**detailed control plan (控规) drawings**. They are not in one open database.

1. **District plan notices (规划公示).** District planning bureaus publish draft plans and
   revisions as PDFs, usually with a 30-day public comment period. Examples were found for
   Putuo, Pudong and Minhang. For Xuhui, scrape the district government's "规划公示" section
   and the bureau's announcements.
2. **Land sale plans (土地使用权出让方案).** District governments approve each sale before it
   goes to the Shanghai land exchange (上海市土地交易市场). These notices state exact
   conditions. For example, Putuo 普府〔2026〕54号 (Jul 2026) lists plot W06-1401 105-03:
   research and design use, 8,839.42 m² site, floor-area ratio 2.2, 19,446.72 m² of
   floor area. The usual terms are 70 years for residential, 40 for commercial, and 50 for
   office and other uses.
3. **Shanghai public data portal (data.sh.gov.cn).** It's run by the Shanghai Data Bureau.
   No planning or land datasets were confirmed there; check by hand.
4. **Industrial land and investment maps.** The citywide industry map (上海产业地图) and the
   15th Five-Year plan for new industrialisation (Aug 2026) define industrial zones and parks.

Expected engineering work: PDF and scanned-drawing parsing (OCR plus layout models), map
alignment of plan drawings (georeferencing), and a human review queue for every extracted
number before it appears in the product.

## 4. Base map data used in the prototype

| Data | Source | Notes |
|---|---|---|
| 12,768 building footprints in Xuhui | OpenStreetMap (Overpass, snapshot 31 May 2026) | Only 549 have tagged heights. The rest are estimated from building type and footprint size. |
| 1,072 land-use plots | OpenStreetMap land-use and park polygons | Mapped to Shanghai planning categories for the mockup. These are not official plan boundaries. |
| Roads, metro lines, 19 metro stations | OpenStreetMap | — |
| 16 district outlines | Aliyun DataV GeoAtlas | Converted from GCJ-02 to WGS-84 |

OpenStreetMap data is under the ODbL licence. The product must show attribution, and any
database built on it inherits share-alike terms.

## 5. Legal constraints on map data in China

- **Surveying and mapping law (测绘法).** Publishing maps in China requires an approved map
  review number (审图号). Precise coordinates are controlled, and maps must use the official
  GCJ-02 offset system.
- **Foreign investment.** Surveying and mapping, including compiling navigation and
  electronic maps, is on the foreign-investment **prohibited** list. If any founder or
  investor is foreign, the China-facing product should run in a Chinese-owned company and use
  licensed base maps (Tianditu 天地图, AutoNavi/Amap, Baidu) rather than its own survey data.
- **Important data.** Detailed 3D models of critical infrastructure can count as "important
  data" under the Data Security Law. Keep sensitive sites out, and get legal review before
  publishing building-level 3D data.
- **The OpenStreetMap prototype is for design review only.** A public launch in mainland
  China would need approved base maps.

## 6. What the prototype shows (and what it fakes)

| Element | Real or placeholder |
|---|---|
| Shanghai district map, Xuhui buildings, plots, roads, metro | Real (OpenStreetMap / DataV) |
| Plot outlines | Real OpenStreetMap land-use shapes, not official plan plots |
| Land-use category per plot | Mapped from OpenStreetMap tags (placeholder) |
| Floor-area ratio, height limits, coverage, green ratio | **Illustrative placeholders** |
| Heritage area, West Bund, Caohejing, Xujiahui core, Longhua zones | **Approximate hand-drawn outlines** |
| Rule logic (metro density bonus, heritage caps, sunlight checks, setbacks) | Realistic structure, illustrative numbers |
| Citations | Real document titles and links, from the search results above |
| "Ask about this plot" | Small local rules engine. The real product would answer from the documents with citations. |

## 7. Next steps if the UI direction is approved

1. Collect every Xuhui detailed-plan notice and land sale notice from 2015 onwards. Build a
   parser and a review queue for them.
2. Replace the OpenStreetMap plots with official plan plots, starting with the West Bund and
   Caohejing.
3. Encode the technical regulations (setbacks, spacing, sunlight) as testable rules with
   citations down to the article.
4. Add official heritage boundaries and the listed-building list.
5. Decide the legal structure for map data (see §5) before any public launch.
