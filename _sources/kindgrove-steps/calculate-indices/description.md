Process profile of **`calculate_indices`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Compute NDVI, NDWI and SAVI

## Source

- CWL: [mangrove-workflow-steps.cwl#calculate_indices](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#calculate_indices) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `band_files` | File[] | `ndvi_file` | File |
|  |  | `ndwi_file` | File |
|  |  | `savi_file` | File |

## Analysis

**Behaviour.** `/app/cwl/bin/steps/04_calculate_indices`, `ghcr.io/geolabs/kindgrove/calculate-indices:v0.0.2-rc2`.
Reads the three reprojected bands (positional-order `File[]`: red, green, nir) and writes
NDVI, NDWI and SAVI as three separate GeoTIFFs.

**CWL specifics.** `band_files` is `File[]` with **no positional labels**, the same gap as
`water-bodies.norm-diff`'s `rasters`: which file is red/green/nir depends entirely on the
caller's array order, not expressed in the processDescription.

**Provenance.** Three file inputs, three file outputs; a plain `wasDerivedFrom` fan-out.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/calculate_indices` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite, one tool computing three indices from the same three-band input at once. NDVI alone would be closeMatch `ogc.openeo.processes.cubes.ndvi`; NDWI alone closeMatch `ogc.openeo.processes.math.indices.normalized_difference` (as in `water-bodies.norm-diff` and `kindgrove.mangrove`); SAVI (soil-adjusted, not a plain normalized difference) has no openEO process in this register. Kept `none` for the tool as a whole since no single openEO process covers the composite.


| Stage | openEO | Level | Note |
|---|---|---|---|
| ndvi | `ogc.openeo.processes.cubes.ndvi` | closeMatch |  |
| ndwi | `ogc.openeo.processes.math.indices.normalized_difference` | closeMatch |  |
| savi | — | none | soil-adjusted vegetation index, no openEO process in this register |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/calculate-indices` (`ospd.process-profiles.process-type`), status `submitted`.
