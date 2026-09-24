Process profile of **`mangrove-workflow-steps`** (Workflow, W2b KindGrove (step notebooks)).

> Mangrove Biomass Workflow (step notebooks)

## Source

- CWL: [mangrove-workflow-steps.cwl#mangrove-workflow-steps](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#mangrove-workflow-steps) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Filter configuration → Selection / filtering → Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: `eoap.cct.bbox`
- Steps (profiles): `ospd.process-profiles.kindgrove-steps.parse-aoi-steps`, `ospd.process-profiles.kindgrove-steps.select-scene`, `ospd.process-profiles.kindgrove-steps.download-band`, `ospd.process-profiles.kindgrove-steps.reproject-band`, `ospd.process-profiles.kindgrove-steps.calculate-indices`, `ospd.process-profiles.kindgrove-steps.estimate-biomass`, `ospd.process-profiles.kindgrove-steps.export-stac`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `aoi` | https://raw.githubusercontent.com/eoap/schemas/main/ogc.yaml#BBox | `stac` | Directory |
| `cloud_cover_max` | float |  |  |
| `days_back` | int |  |  |
| `stac_api` | string? |  |  |
| `collection` | string? |  |  |
| `epsg` | int? |  |  |
| `resolution` | float? |  |  |
| `ndvi_min` | float? |  |  |
| `ndvi_max` | float? |  |  |
| `ndwi_min` | float? |  |  |
| `savi_min` | float? |  |  |
| `biomass_slope` | float? |  |  |
| `biomass_intercept` | float? |  |  |
| `carbon_fraction` | float? |  |  |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-05 outputs.stac: the Directory output is a STAC Catalog written by the tool itself (run record: `catalog.json` with one Item), not the Collection assumed by the transform

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite: a CWL Workflow decomposed into one CommandLineTool per notebook, aligned on the same granularity as W1 Algae Bloom (parse AOI, select scene, download/reproject bands, compute indices, estimate biomass, export STAC) -- the workflow's own `doc:` says so explicitly. A ground-up reimplementation of `kindgrove.mangrove-workflow`'s computation, not a repackaging of it; the openEO equivalent would be a user-defined process graph.


| Stage | openEO | Level | Note |
|---|---|---|---|
| select_scene | `ogc.openeo.processes.cubes.load_collection` | closeMatch |  |
| download_band (x3, scatter over bands) | `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands` | closeMatch |  |
| reproject_band (x3) | `ogc.openeo.processes.cubes.resample_spatial` | closeMatch |  |
| calculate_indices | `ogc.openeo.processes.cubes.ndvi`, `ogc.openeo.processes.math.indices.normalized_difference` | closeMatch | NDVI and NDWI; SAVI has no openEO process in this register |
| estimate_biomass | — | none | opaque allometric regression + IPCC carbon fraction |
| export_stac | `ogc.openeo.processes.cubes.save_result` | closeMatch |  |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/mangrove-workflow-steps` (`ospd.process-profiles.process-type`), status `submitted`.
