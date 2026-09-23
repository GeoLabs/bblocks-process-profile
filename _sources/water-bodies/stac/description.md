Process profile of **`stac`** (CommandLineTool, W3 Water Bodies).

> Assemble a STAC catalog of detected water bodies

## Source

- CWL: [app-water-bodies-cloud-native.cwl#stac](https://github.com/gfenoy/mastering-app-package/blob/40ecc096da56c6810758b87b01a87502f7c4507c/cwl-workflow/app-water-bodies-cloud-native.cwl#stac) (pinned commit `40ecc09`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.stac`
- Used by: `ospd.process-profiles.water-bodies.water-bodies`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `item` | {"type": "array", "items": "string", "inputBinding": {"prefix": "--input-item"}} | `stac_catalog` | Directory |
| `rasters` | {"type": "array", "items": "File", "inputBinding": {"prefix": "--water-body"}} |  |  |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0`.
Pairs each `item` (a STAC item URL, in order) with the matching `rasters` entry (in order,
the same positional-array coupling as `norm-diff`) and writes a root `catalog.json` plus one
per-item sub-folder holding that item's own STAC JSON and its water-body raster asset.

**CWL specifics.** Output `stac_catalog` is a `Directory`, mapped by the transform to a STAC
**Collection**; the run record shows the tool itself writes a STAC **Catalog**
(`catalog.json`, `"type": "Catalog"`) with one Item per input identifier: corrected (M-05),
the same gap as `kindgrove.mangrove` / `kindgrove.mangrove-workflow`.

**Provenance.** Two array inputs coupled positionally (GP-3: neither is itself a file-typed
entity that could carry `wasDerivedFrom` to the water-body rasters it packages); the output
directory's members are the register's own `execution` bundle's per-file artefacts (GP-10).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-05 outputs.stac_catalog: the Directory output is a STAC Catalog written by the tool itself (run record: `catalog.json` with one Item), not the Collection assumed by the transform

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (mastering-app-package 40ecc09 `app-water-bodies-cloud-native.cwl#water-bodies`), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out` against a locally patched copy (U-06), 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_stac` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Writes the final rasters to a self-describing output collection; save_result's STAC-catalog output option is the closest openEO equivalent to hand-assembling one.

- `closeMatch`: `ogc.openeo.processes.cubes.save_result`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac` (`ospd.process-profiles.process-type`), status `submitted`.
