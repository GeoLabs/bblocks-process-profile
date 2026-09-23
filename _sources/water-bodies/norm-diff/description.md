Process profile of **`norm_diff`** (CommandLineTool, W3 Water Bodies).

> Normalized difference between two rasters

## Source

- CWL: [app-water-bodies-cloud-native.cwl#norm_diff](https://github.com/gfenoy/mastering-app-package/blob/40ecc096da56c6810758b87b01a87502f7c4507c/cwl-workflow/app-water-bodies-cloud-native.cwl#norm_diff) (pinned commit `40ecc09`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.water-bodies.detect-water-body`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `rasters` | File[] | `ndwi` | File |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0`.
Reads the two cropped band rasters (positional `rasters: File[]`, order fixed by `node_crop`'s
scatter order over `bands`: green first, nir second in this workflow) and writes
`(A-B)/(A+B)` as one GeoTIFF (`norm_diff.tif`).

**CWL specifics.** `rasters` is `File[]` with **no positional labels**: which raster is the
minuend and which the subtrahend depends entirely on array order, not expressed anywhere in
the processDescription (an unconstrained `array` of File binary schemas).

**Provenance.** Two file inputs, one file output; a plain `wasDerivedFrom` chain (GP-3/GP-4
do not apply, both endpoints are files).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (mastering-app-package 40ecc09 `app-water-bodies-cloud-native.cwl#water-bodies`), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out` against a locally patched copy (U-06), 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_normalized_difference` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Exact index formula, generic over which two bands are passed: NDWI (green, nir) in this workflow, same as `ogc.openeo.processes.math.indices.normalized_difference` used for NDVI elsewhere in this register (`kindgrove.mangrove`) -- it is the caller's band choice, not the tool, that names the index.

- `closeMatch`: `ogc.openeo.processes.math.indices.normalized_difference`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff` (`ospd.process-profiles.process-type`), status `submitted`.
