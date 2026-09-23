Process profile of **`algae-usecase-workflow-earth-search-process`** (Workflow, W1 Algae Bloom).

> Processing on Sentinel-2 L2A bands to evaluate algae bloom.

## Source

- CWL: [algae-usecase-workflow-earth-search-process.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search-process.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.algae-bloom.download-band-sentinel2-stac-item`, `ospd.process-profiles.algae-bloom.reproject-image`, `ospd.process-profiles.algae-bloom.calculate-band`, `ospd.process-profiles.algae-bloom.plot-image`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `product_url` | string | `chlorophyll_a` | File |
|  |  | `chlorophyll_a_color` | File |
|  |  | `chlorophyll_a_plot` | File |
|  |  | `cyanobacteria` | File |
|  |  | `cyanobacteria_color` | File |
|  |  | `cyanobacteria_plot` | File |
|  |  | `turbidity` | File |
|  |  | `turbidity_color` | File |
|  |  | `turbidity_plot` | File |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `c27c60d`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-01 outputs.chlorophyll_a: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.chlorophyll_a_color: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.chlorophyll_a_plot: contentMediaType from CWL format `iana:image/png` -> `image/png`; contentEncoding binary
- M-01 outputs.cyanobacteria: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.cyanobacteria_color: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.cyanobacteria_plot: contentMediaType from CWL format `iana:image/png` -> `image/png`; contentEncoding binary
- M-01 outputs.turbidity: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.turbidity_color: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.turbidity_plot: contentMediaType from CWL format `iana:image/png` -> `image/png`; contentEncoding binary

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main` (scatter iteration 2, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite (11 steps: 4 band downloads, 1 resampling, 3 band calculations, 3 renderings). In openEO this is one load_collection with band selection followed by a process graph.


| Stage | openEO | Level | Note |
|---|---|---|---|
| download_b0x (x4) | `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands` | closeMatch |  |
| reproject_b03_60m | `ogc.openeo.processes.cubes.resample_spatial` | closeMatch |  |
| calculate_* (x3) | `ogc.openeo.processes.cubes.reduce_dimension` | closeMatch |  |
| plot_* (x3) | `ogc.openeo.processes.cubes.save_result` | closeMatch | partial, no colour-ramp rendering |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search-process` (`ospd.process-profiles.process-type`), status `submitted`.
