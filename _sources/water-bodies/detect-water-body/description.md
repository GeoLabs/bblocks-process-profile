Process profile of **`detect_water_body`** (Workflow, W3 Water Bodies).

> Water body detection based on NDWI and otsu threshold

## Source

- CWL: [app-water-bodies-cloud-native.cwl#detect_water_body](https://github.com/gfenoy/mastering-app-package/blob/40ecc096da56c6810758b87b01a87502f7c4507c/cwl-workflow/app-water-bodies-cloud-native.cwl#detect_water_body) (pinned commit `40ecc09`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval → Scientific computation
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`, `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.water-bodies.crop`, `ospd.process-profiles.water-bodies.norm-diff`, `ospd.process-profiles.water-bodies.otsu`
- Used by: `ospd.process-profiles.water-bodies.water-bodies`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `aoi` | string | `detected_water_body` | File |
| `epsg` | string |  |  |
| `bands` | string[] |  |  |
| `item` | string |  |  |

## Analysis

**Behaviour.** Crops the requested `bands` (scatter) of one STAC `item` to `aoi`/`epsg`,
computes their normalized difference, then an Otsu binary threshold on the result.

**CWL specifics.** `bands` fixes the crop order and therefore which raster `node_normalized_difference`
treats as the minuend: with the workflow default (`green`, `nir`) the index computed is NDWI,
but nothing in the processDescription says so -- `norm-diff` itself is generic (see that profile).

**Provenance.** Composite of `crop` x2, `norm-diff`, `otsu`; see each for its own gaps.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (mastering-app-package 40ecc09 `app-water-bodies-cloud-native.cwl#water-bodies`), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out` against a locally patched copy (U-06), 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite (3 steps: band crop scattered over 2 bands, NDWI, Otsu threshold). In openEO this is one load_collection with band selection followed by a short process graph.


| Stage | openEO | Level | Note |
|---|---|---|---|
| node_crop (x2, scatter over bands) | `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands` | closeMatch |  |
| node_normalized_difference | `ogc.openeo.processes.math.indices.normalized_difference` | closeMatch |  |
| node_otsu | — | none | no stable Otsu-threshold process in openEO |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/detect-water-body` (`ospd.process-profiles.process-type`), status `submitted`.
