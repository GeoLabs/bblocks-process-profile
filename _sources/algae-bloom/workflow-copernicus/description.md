Process profile of **`algae-usecase-workflow-copernicus`** (Workflow, W1 Algae Bloom).

> Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.

## Source

- CWL: [algae-usecase-workflow-copernicus.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Filter configuration → Selection / filtering → Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.geojson`, `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.algae-bloom.select-products-sentinel2`, `ospd.process-profiles.algae-bloom.workflow-copernicus-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `date` | string | `chlorophyll_a` | File[] |
| `delta` | int? | `chlorophyll_a_color` | File[] |
| `aoi` | File | `chlorophyll_a_plot` | File[] |
| `collection` | string | `cyanobacteria` | File[] |
| `cloud_cover` | double? | `cyanobacteria_color` | File[] |
| `s3_access_key` | string | `cyanobacteria_plot` | File[] |
| `s3_secret_key` | string | `turbidity` | File[] |
|  |  | `turbidity_color` | File[] |
|  |  | `turbidity_plot` | File[] |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-04 inputs.s3_access_key: declared in cwltool:Secrets -> writeOnly: true
- M-04 inputs.s3_secret_key: declared in cwltool:Secrets -> writeOnly: true

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-copernicus`: Copernicus variant of the pinned W1 package, `cwltool --outdir ./results1 --provenance ./PROV1 algae-usecase-workflow-copernicus.cwl example/algae-usecase-job-copernicus.yml` with Copernicus Data Space S3 credentials, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; one product (S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542). cwltool writes the `cwltool:Secrets` inputs as `(secret-<uuid>)` placeholders in the research object), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite; same structure as the Earth-Search variant but over Copernicus Data Space (SAFE products on S3, credentials required). openEO hides credentials in the back-end.


| Stage | openEO | Level | Note |
|---|---|---|---|
| select_products | `ogc.openeo.processes.cubes.load_collection` | closeMatch |  |
| process (scatter over urls) | — | none |  |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus` (`ospd.process-profiles.process-type`), status `submitted`.
