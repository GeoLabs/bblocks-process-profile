Process profile of **`parse_aoi`** (CommandLineTool, W2 KindGrove).

> Parse area of interest

## Source

- CWL: [mangrove-workflow.cwl#parse_aoi](https://github.com/GeoLabs/bblocks-eoap-cct/blob/c27c60d2755c01f69bd7f1bd0903b6388d375e58/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#parse_aoi) (pinned commit `c27c60d`, license <https://spdx.org/licenses/Apache-2.0>). Referenced, not copied.
- Six-phase position: Filter configuration
- EOAP CWL custom types used: `eoap.cct.bbox`
- Used by: `ospd.process-profiles.kindgrove.mangrove-workflow`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `aoi` | https://raw.githubusercontent.com/eoap/schemas/main/ogc.yaml#BBox | `west` | float |
|  |  | `south` | float |
|  |  | `east` | float |
|  |  | `north` | float |
|  |  | `output_dir` | string |

## Analysis

**Behaviour.** `echo --` in `alpine:3.22.2`; all outputs come from `outputEval`
JavaScript expressions over `inputs.aoi.bbox[0..3]`. Nothing is computed by the container.

**CWL specifics.** The only W2 tool that uses a custom type (`ogc.yaml#BBox`). Its
processDescription therefore exposes the eoap BBox schema, whose `crs` enum
(`CRS84`, `CRS84h`) differs from the OGC API - Processes Part 1 bbox CRS URIs (M-07).
The `crs` value is ignored by the expressions: a bbox in another CRS would be silently
misread.

**Provenance.** An activity with parameter-only inputs and outputs: nothing in it is a file,
so neither `eoap-artifact` nor `execution` apply (GP-3, GP-4). Deployed standalone it is of
little use; it is profiled because it is a separately deployable CWL process.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `c27c60d`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w2-pinned`: the register's pinned W2 source itself (bblocks-eoap-cct c27c60d `mangrove-workflow.cwl#mangrove-workflow`) run with the profile's execute inputs, `cwltool --no-match-user --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, 126 s; scene selected by `days_back` on that day: S2C_46PGC_20260913_0_L2A), activity `main/parse_aoi` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Structural helper: unpacks an OGC BBox record into west/south/east/north floats and emits a constant `output_dir` ("outputs"). No openEO process does this, because openEO passes a bounding box object directly (`ogc.openeo.types.bounding-box`, relatedMatch at type level).

- `relatedMatch`: `ogc.openeo.types.bounding-box`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/parse-aoi` (`ospd.process-profiles.process-type`), status `submitted`.
