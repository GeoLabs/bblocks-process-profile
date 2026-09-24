Process profile of **`download_band`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Download one Sentinel-2 band over a bounding box

## Source

- CWL: [mangrove-workflow-steps.cwl#download_band](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#download_band) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`, `eoap.cct.stac`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `stac_item` | File | `band_file` | File |
| `band` | string |  |  |
| `west` | float |  |  |
| `south` | float |  |  |
| `east` | float |  |  |
| `north` | float |  |  |

## Analysis

**Behaviour.** `/app/cwl/bin/steps/02_download_band`, `ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2`.
Reads the given `band` asset of `stac_item`, windowed to the bounding box, writes one COG.

**Provenance.** One file input (`stac_item`), literal `band`/bbox inputs, one file output; a
plain `wasDerivedFrom` on `stac_item`.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/download_band` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** load_collection with a spatial_extent and a single band selected (filter_bands); the STAC item is a resolved File (the output of `select-scene`) rather than resolved in-process, same pattern as `algae-bloom.download-band-sentinel2-stac-item`.

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/download-band` (`ospd.process-profiles.process-type`), status `submitted`.
