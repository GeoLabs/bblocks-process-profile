Process profile of **`mangrove-workflow`** (Workflow, W2 KindGrove).

> Mangrove Biomass Workflow

## Source

- CWL: [mangrove-workflow.cwl#mangrove-workflow](https://github.com/GeoLabs/bblocks-eoap-cct/blob/c27c60d2755c01f69bd7f1bd0903b6388d375e58/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow) (pinned commit `c27c60d`, license <https://spdx.org/licenses/Apache-2.0>). Referenced, not copied.
- Six-phase position: Filter configuration → Selection / filtering → Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: `eoap.cct.bbox`
- Steps (profiles): `ospd.process-profiles.kindgrove.parse-aoi`, `ospd.process-profiles.kindgrove.mangrove`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `cloud_cover_max` | float | `stac` | Directory |
| `days_back` | int |  |  |
| `aoi` | https://raw.githubusercontent.com/eoap/schemas/main/ogc.yaml#BBox |  |  |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `c27c60d`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-05 outputs.stac: the Directory output is a STAC Catalog written by the tool itself (run record: `catalog.json` with one Item), not the Collection assumed by the transform

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w2-pinned`: the register's pinned W2 source itself (bblocks-eoap-cct c27c60d `mangrove-workflow.cwl#mangrove-workflow`) run with the profile's execute inputs, `cwltool --no-match-user --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, 126 s; scene selected by `days_back` on that day: S2C_46PGC_20260913_0_L2A), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite of a BBox-unpacking helper and one opaque tool; the openEO equivalent is a process graph (see the `mangrove` profile for the stage-by-stage decomposition). `stac.yaml` is imported in `SchemaDefRequirement` but unused.


| Stage | openEO | Level | Note |
|---|---|---|---|
| parse_aoi | — | none | structural; bounding box is a native openEO parameter type |
| step_1 (mangrove_cli) | — | none | see ospd.process-profiles.kindgrove.mangrove |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow` (`ospd.process-profiles.process-type`), status `submitted`.
