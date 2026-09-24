Process profile of **`export_stac`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Plot the biomass map and export a STAC catalog

## Source

- CWL: [mangrove-workflow-steps.cwl#export_stac](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#export_stac) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.stac`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `mangrove_mask_file` | File | `stac_catalog` | Directory |
| `biomass_file` | File |  |  |
| `biomass_summary_file` | File |  |  |
| `carbon_summary_file` | File |  |  |
| `analysis_summary_file` | File |  |  |
| `stac_item` | File |  |  |
| `west` | float |  |  |
| `south` | float |  |  |
| `east` | float |  |  |
| `north` | float |  |  |

## Analysis

**Behaviour.** `/app/cwl/bin/steps/06_export_stac`, `ghcr.io/geolabs/kindgrove/export-stac:v0.0.2-rc2`.
Renders a `biomass_quicklook.png` from the biomass raster, then writes a STAC Catalog with
one Item (`mangrove-analysis-<timestamp>`, timestamped at run time like `kindgrove.mangrove`'s
own output) carrying the mask, biomass raster, two summary CSVs, the analysis JSON and the
quicklook PNG as assets.

**CWL specifics.** Output `stac_catalog` is a `Directory` (`glob: outputs`), mapped by the
transform to a STAC **Collection**; the run record shows the tool itself writes a STAC
**Catalog** (`"type": "Catalog"`) with one Item: corrected (M-05), the same gap as
`kindgrove.mangrove` / `kindgrove.mangrove-workflow` and `water-bodies.stac` /
`water-bodies.water-bodies` -- a third, independent tool hitting the identical gap.

**Provenance.** Five file inputs coupled to one Item (GP-10 applies to the whole per-item
asset set); `west`/`south`/`east`/`north` are literal-valued entities describing the Item's
geometry, not files.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-05 outputs.stac_catalog: the Directory output is a STAC Catalog written by the tool itself (run record: `catalog.json` with one Item), not the Collection assumed by the transform

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/export_stac` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Writes the final rasters and summaries to a self-describing STAC output, plus a quicklook PNG rendering; save_result's STAC output option is the closest openEO equivalent, same partial match as `algae-bloom.plot-image` and `water-bodies.stac`.

- `closeMatch`: `ogc.openeo.processes.cubes.save_result`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/export-stac` (`ospd.process-profiles.process-type`), status `submitted`.
