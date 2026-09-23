# openEO equivalence decisions

Proposed correspondences between the process profiles and the openEO Building Blocks of
[GeoLabs/bblocks-openeo](https://github.com/GeoLabs/bblocks-openeo) (`ogc.openeo.*`, stable
processes of openeo-processes 2.0.0-rc.2). Offered for review, not settled equivalences.
Generated from `scripts/profiles.yaml` by `scripts/generate.py`.

## Criteria

| Level | Used when |
|---|---|
| **exactMatch** | same operation, same parameter semantics, same output type. None found. |
| **closeMatch** | same operation, but a different I/O model (files or URLs vs openEO data cubes), or a parameter subset/superset. |
| **none** | no single openEO process: the step is a composition (process graph), an opaque tool, or a structural helper. |

`relatedMatch` (SKOS) is used for type-level links (e.g. a bounding-box input vs
`ogc.openeo.types.bounding-box`) and for math processes used inside a callback; it never expresses
process equivalence. Composite and opaque processes carry a stage-by-stage `decomposition` in their
process-type entry. openEO `proposals/` (e.g. `load_stac`) are out of scope because
bblocks-openeo only models stable processes.

## Decisions (to be confirmed by Gérald before commit)

| # | Profile | Level | exactMatch / closeMatch | relatedMatch | Rationale (short) |
|---|---|---|---|---|---|
| E01 | `algae-bloom.workflow-earth-search` | none | — | — | Composite: a CWL Workflow scattering a per-product subworkflow over the product list. |
| E02 | `algae-bloom.workflow-earth-search-process` | none | — | — | Composite (11 steps: 4 band downloads, 1 resampling, 3 band calculations, 3 renderings). |
| E03 | `algae-bloom.workflow-copernicus` | none | — | — | Composite; same structure as the Earth-Search variant but over Copernicus Data Space (SAFE products on S3, credentials required). |
| E04 | `algae-bloom.workflow-copernicus-process` | none | — | — | Composite (11 steps). |
| E05 | `algae-bloom.select-products-sentinel2` | closeMatch | `processes.cubes.load_collection` | `types.geojson`, `types.temporal-interval`, `types.collection-id`, `types.metadata-filter` | Same filter semantics as load_collection's `id` (collection), `spatial_extent` (aoi), `temporal_extent` (date±delta or toi) and `properties` (eo:cloud_cover) parameters. |
| E06 | `algae-bloom.download-band-sentinel2-stac-item` | closeMatch | `processes.cubes.load_collection`, `processes.cubes.filter_bands` | `types.band-name`, `types.stac` | Retrieves one band of one product: load_collection with `bands` (or filter_bands) over a single-item extent. |
| E07 | `algae-bloom.download-band-sentinel2-product-safe` | closeMatch | `processes.cubes.load_collection`, `processes.cubes.filter_bands` | `types.band-name` | Same operation as the STAC-Item variant (one band of one product) but reading the SAFE archive on S3 with user credentials and a `resolution` selector (10m/20m/60m). |
| E08 | `algae-bloom.reproject-image` | closeMatch | `processes.cubes.resample_spatial` | — | As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. |
| E09 | `algae-bloom.calculate-band` | closeMatch | `processes.cubes.reduce_dimension` | `processes.math.divide`, `processes.math.power`, `processes.math.multiply`, `processes.math.subtract` | Generic band math (gdal_calc.py with a Python/numpy expression over up to 26 bands A..Z): openEO expresses it as reduce_dimension over the `bands` dimension with a callback built from math processes. |
| E10 | `algae-bloom.plot-image` | closeMatch | `processes.cubes.save_result` | `processes.math.clip`, `processes.math.linear_scale_range` | Partial: the export part (GeoTIFF + PNG) corresponds to save_result with a GTiff or PNG format; `clip_min`/`clip_max` correspond to math.clip. |
| E11 | `kindgrove.mangrove-workflow` | none | — | — | Composite of a BBox-unpacking helper and one opaque tool; the openEO equivalent is a process graph (see the `mangrove` profile for the stage-by-stage decomposition). |
| E12 | `kindgrove.parse-aoi` | none | — | `types.bounding-box` | Structural helper: unpacks an OGC BBox record into west/south/east/north floats and emits a constant `output_dir` ("outputs"). |
| E13 | `kindgrove.mangrove` | none | — | — | Opaque: one ipython2cwl binary running the whole notebook. |
| E14 | `water-bodies.water-bodies` | none | — | — | Composite: a CWL Workflow scattering a per-item sub-workflow over the STAC item list, then aggregating the results into one STAC catalog. |
| E15 | `water-bodies.detect-water-body` | none | — | — | Composite (3 steps: band crop scattered over 2 bands, NDWI, Otsu threshold). |
| E16 | `water-bodies.crop` | closeMatch | `processes.cubes.load_collection`, `processes.cubes.filter_bands` | — | load_collection with a spatial_extent (aoi) and a single band selected (filter_bands); the STAC item is given by URL rather than resolved by collection/date/bbox search, and the windowed COG read (no full download) is an implementation detail openEO back-ends make transparently.. |
| E17 | `water-bodies.norm-diff` | closeMatch | `processes.math.indices.normalized_difference` | — | Exact index formula, generic over which two bands are passed: NDWI (green, nir) in this workflow, same as `ogc.openeo.processes.math.indices.normalized_difference` used for NDVI elsewhere in this register (`kindgrove.mangrove`) -- it is the caller's band choice, not the tool, that names the index.. |
| E18 | `water-bodies.otsu` | none | — | — | openEO has no built-in Otsu (automatic histogram) threshold process; the closest primitive, `ogc.openeo.processes.comparison.gt`, only compares against a caller-supplied constant, not a threshold the process computes itself.. |
| E19 | `water-bodies.stac` | closeMatch | `processes.cubes.save_result` | — | Writes the final rasters to a self-describing output collection; save_result's STAC-catalog output option is the closest openEO equivalent to hand-assembling one.. |

Full rationale and decompositions: each profile's `description.md` and `examples/process-type.json`.
