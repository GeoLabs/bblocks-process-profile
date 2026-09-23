Process profile of **`download-band-sentinel2-stac-item`** (CommandLineTool, W1 Algae Bloom).

> Downloads Sentinel-2 GeoTiff from STAC Item.

## Source

- CWL: [download-band-sentinel2-stac-item.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/download-band-sentinel2-stac-item.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval
- EOAP CWL custom types used: none; candidates: `eoap.cct.string-format`, `eoap.cct.stac`
- Used by: `ospd.process-profiles.algae-bloom.workflow-earth-search-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `product_url` | string | `product` | File |
| `band` | {"type": "enum", "symbols": ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B11", "B12", "AOT", "SCL", "TCI", "WVP"]} |  |  |

## Analysis

**Behaviour.** Resolves the STAC Item, picks the GeoTIFF asset of the requested band and
downloads it as `<band>.tif` (COG from the Earth-Search Sentinel-2 L2A collection).

**CWL specifics.** `product_url` is a plain `string` holding an HTTPS STAC Item URL
(candidate `eoap.cct.string-format` URI, or `eoap.cct.stac` Item if the Item itself were
passed). `band` is an enum of 16 values. Output `product` is `File` with
`format: ogc:geotiff`, resolved by the transform to
`contentMediaType: image/tiff; application=geotiff` (M-01, fixed 2026-09-23 in
`eoap.cct.cwl-to-ogcprocess` itself).

**Provenance.** The downloaded band is the first file entity of the chain; its
`wasDerivedFrom` is the STAC Item (remote, not an output of the run), which
`eoap-artifact` cannot express because it requires `wasOutputFrom` (GP-3).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main/download_b03_10m_2` (scatter iteration 2, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Retrieves one band of one product: load_collection with `bands` (or filter_bands) over a single-item extent. The closest openEO process, `load_stac`, is only an openEO proposal and out of the register's scope. The band is chosen by Sentinel-2 band id (B01..B12), matched to STAC `eo:common_name` assets inside the tool, where openEO uses collection band names directly.

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands`
- `relatedMatch`: `ogc.openeo.types.band-name`, `ogc.openeo.types.stac`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/download-band-sentinel2-stac-item` (`ospd.process-profiles.process-type`), status `submitted`.
