Process profile of **`select_scene`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Select the least cloudy Sentinel-2 L2A scene

## Source

- CWL: [mangrove-workflow-steps.cwl#select_scene](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#select_scene) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Selection / filtering
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `west` | float | `stac_item` | File |
| `south` | float |  |  |
| `east` | float |  |  |
| `north` | float |  |  |
| `cloud_cover_max` | float |  |  |
| `days_back` | int |  |  |
| `stac_api` | string? |  |  |
| `collection` | string? |  |  |

## Analysis

**Behaviour.** `/app/cwl/bin/steps/01_select_scene`, `ghcr.io/geolabs/kindgrove/select-scene:v0.0.2-rc2`.
Searches `stac_api`/`collection` (both defaulted to Earth Search / sentinel-2-l2a) for the
least cloudy scene intersecting the bounding box within `days_back` days of the execution
date, under `cloud_cover_max`, and writes its STAC Item as `scene_item.json`.

**CWL specifics.** `requirements: {NetworkAccess: {networkAccess: true}}` uses the dict-form
requirements syntax, where bare `NetworkAccess` validates without the `cwltool:` namespace
prefix W3's list-form syntax needed (`docs/DEVIATIONS.md` U-06) -- a different encoding of
the same cwltool extension, not a fix to the underlying non-standardness.

**Provenance.** No file input: `west`/`south`/`east`/`north`/`cloud_cover_max`/`days_back`
are literal-valued entities. The network search itself leaves no provenance trace beyond the
output STAC Item file (GP-3, GP-4, the same gap `water-bodies.crop` has).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/select_scene` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Same filter semantics as load_collection's `spatial_extent` (west/south/east/north) and a `properties` cloud-cover filter; `days_back` is a relative time window resolved against the execution date, not an explicit `temporal_extent` -- the same non-reproducibility already documented for `kindgrove.mangrove-workflow` (Q-W2-DAYSBACK).

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/select-scene` (`ospd.process-profiles.process-type`), status `submitted`.
