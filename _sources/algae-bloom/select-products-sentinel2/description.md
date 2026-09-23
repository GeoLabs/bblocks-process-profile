Process profile of **`select-products-sentinel2`** (CommandLineTool, W1 Algae Bloom).

> Searches the specified catalog for Sentinel-2 products matching filtering criteria.

## Source

- CWL: [select-products-sentinel2.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/select-products-sentinel2.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Selection / filtering
- EOAP CWL custom types used: none; candidates: `eoap.cct.geojson`, `eoap.cct.string-format`
- Used by: `ospd.process-profiles.algae-bloom.workflow-earth-search`, `ospd.process-profiles.algae-bloom.workflow-copernicus`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `date` | string? | `urls` | string[] |
| `delta` | int? |  |  |
| `toi` | string[]? |  |  |
| `aoi` | File |  |  |
| `collection` | string |  |  |
| `product_level` | ["null", {"type": "enum", "symbols": ["L1C", "L2A"]}] |  |  |
| `catalog` | {"type": "enum", "symbols": ["copernicus", "earth-search"]} |  |  |
| `cloud_cover` | double? |  |  |

## Analysis

**Behaviour.** Queries either the Copernicus Data Space OData catalogue
(`catalog: copernicus`, returns `s3:///eodata/...SAFE` URLs) or the Element84 Earth-Search
STAC API (`catalog: earth-search`, returns STAC Item URLs). The JSON list is written to
stdout, captured as `collection-urls.json` and parsed with `outputEval` into `string[]`.

**CWL specifics that matter for the profile.**
- `aoi` is a `File` with `format: iana:application/geo+json` (a GeoJSON *Polygon* geometry
  in the example, not a Feature): candidate for `eoap.cct.geojson`.
- `date` / `toi` are plain `string` / `string[]` holding ISO dates: candidates for
  `eoap.cct.string-format` (`Date` / `DateTime`); the either/or constraint between them is
  only stated in `doc` and cannot be expressed in the processDescription.
- `product_level` and `catalog` are enums; the parent workflows fix them with `valueFrom`
  (`L2A`, and `earth-search` or `copernicus`), so they are not exposed at workflow level.
- Requires `NetworkAccess`.

**Provenance.** The output is a list of literal URLs, not files: under the generic profile
it can only be a plain `prov:Entity` with `value` (GP-4). Its value is what links the
selection to each scattered download (`product_url`).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main/select_products` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Same filter semantics as load_collection's `id` (collection), `spatial_extent` (aoi), `temporal_extent` (date±delta or toi) and `properties` (eo:cloud_cover) parameters. Not an exactMatch: the tool only selects (returns product URLs) and does not load data; the `catalog` switch (copernicus / earth-search) is a back-end choice with no openEO parameter; `date`+`delta` must be turned into an interval; the Earth-Search branch filters `0 < eo:cloud_cover < cloud_cover` (strict, excludes 0) where an openEO `lte` filter would be expected.

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`
- `relatedMatch`: `ogc.openeo.types.geojson`, `ogc.openeo.types.temporal-interval`, `ogc.openeo.types.collection-id`, `ogc.openeo.types.metadata-filter`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/select-products-sentinel2` (`ospd.process-profiles.process-type`), status `submitted`.
