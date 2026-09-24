Process profile of **`estimate_biomass`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Mangrove detection, allometric biomass and IPCC carbon stock

## Source

- CWL: [mangrove-workflow-steps.cwl#estimate_biomass](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none; candidates: `eoap.cct.stac`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `ndvi_file` | File | `mangrove_mask_file` | File |
| `ndwi_file` | File | `biomass_file` | File |
| `savi_file` | File | `biomass_summary_file` | File |
| `stac_item` | File | `carbon_summary_file` | File |
| `ndvi_min` | float? | `analysis_summary_file` | File |
| `ndvi_max` | float? |  |  |
| `ndwi_min` | float? |  |  |
| `savi_min` | float? |  |  |
| `biomass_slope` | float? |  |  |
| `biomass_intercept` | float? |  |  |
| `carbon_fraction` | float? |  |  |

## Analysis

**Behaviour.** `/app/cwl/bin/steps/05_estimate_biomass`, `ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2`.
Masks pixels within the `ndvi_min`/`ndvi_max`/`ndwi_min`/`savi_min` thresholds as mangrove,
applies `biomass = biomass_slope * ndvi + biomass_intercept` per masked pixel, and
`carbon = biomass * carbon_fraction`; writes the mask, the biomass raster, two CSV summaries
and a JSON analysis summary.

**CWL specifics.** `stac_item` (the scene's own STAC Item) is threaded through purely to
carry scene metadata into the outputs, not read as a raster.

**Provenance.** Three file inputs (ndvi/ndwi/savi) plus the STAC item; five file outputs, a
genuine fan-in/fan-out (GP-10 applies here the same way it does to `kindgrove.mangrove`).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/estimate_biomass` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Opaque: a threshold-based mangrove mask (ndvi_min/max, ndwi_min, savi_min) followed by a fixed linear allometric formula (biomass_slope/intercept) and an IPCC carbon_fraction constant. No openEO process expresses a domain-specific regression model, same as `kindgrove.mangrove`.


## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass` (`ospd.process-profiles.process-type`), status `submitted`.
