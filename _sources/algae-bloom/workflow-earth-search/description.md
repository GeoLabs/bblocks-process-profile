Process profile of **`algae-usecase-workflow-earth-search`** (Workflow, W1 Algae Bloom).

> Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.

## Source

- CWL: [algae-usecase-workflow-earth-search.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Filter configuration → Selection / filtering → Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.geojson`, `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.algae-bloom.select-products-sentinel2`, `ospd.process-profiles.algae-bloom.workflow-earth-search-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `date` | string? | `chlorophyll_a` | File[] |
| `delta` | int? | `chlorophyll_a_color` | File[] |
| `toi` | string[]? | `chlorophyll_a_plot` | File[] |
| `aoi` | File | `cyanobacteria` | File[] |
| `collection` | string | `cyanobacteria_color` | File[] |
| `cloud_cover` | double? | `cyanobacteria_plot` | File[] |
|  |  | `turbidity` | File[] |
|  |  | `turbidity_color` | File[] |
|  |  | `turbidity_plot` | File[] |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite: a CWL Workflow scattering a per-product subworkflow over the product list. The openEO equivalent would be a user-defined process graph, which has no Building Block of its own; the correspondence is carried by the steps.


| Stage | openEO | Level | Note |
|---|---|---|---|
| select_products | `ogc.openeo.processes.cubes.load_collection` | closeMatch |  |
| process (scatter over urls) | — | none | openEO has no scatter over products; a collection is loaded as one data cube. |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search` (`ospd.process-profiles.process-type`), status `submitted`.
