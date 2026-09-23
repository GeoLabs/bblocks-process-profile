Process profile of **`algae-usecase-workflow-copernicus-process`** (Workflow, W1 Algae Bloom).

> Processing on Sentinel-2 bands to evaluate algae bloom.

## Source

- CWL: [algae-usecase-workflow-copernicus-process.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.algae-bloom.download-band-sentinel2-product-safe`, `ospd.process-profiles.algae-bloom.calculate-band`, `ospd.process-profiles.algae-bloom.plot-image`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `product_url` | string | `chlorophyll_a` | File |
| `s3_access_key` | string | `chlorophyll_a_color` | File |
| `s3_secret_key` | string | `chlorophyll_a_plot` | File |
|  |  | `cyanobacteria` | File |
|  |  | `cyanobacteria_color` | File |
|  |  | `cyanobacteria_plot` | File |
|  |  | `turbidity` | File |
|  |  | `turbidity_color` | File |
|  |  | `turbidity_plot` | File |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-04 inputs.s3_access_key: declared in cwltool:Secrets -> writeOnly: true
- M-04 inputs.s3_secret_key: declared in cwltool:Secrets -> writeOnly: true

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-copernicus`: Copernicus variant of the pinned W1 package, `cwltool --outdir ./results1 --provenance ./PROV1 algae-usecase-workflow-copernicus.cwl example/algae-usecase-job-copernicus.yml` with Copernicus Data Space S3 credentials, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; one product (S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542). cwltool writes the `cwltool:Secrets` inputs as `(secret-<uuid>)` placeholders in the research object), activity `main` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite (11 steps). No resampling step: the SAFE product already provides 60 m bands, so B03 60 m is downloaded directly instead of being resampled.


| Stage | openEO | Level | Note |
|---|---|---|---|
| download_b0x (x5) | `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands` | closeMatch |  |
| calculate_* (x3) | `ogc.openeo.processes.cubes.reduce_dimension` | closeMatch |  |
| plot_* (x3) | `ogc.openeo.processes.cubes.save_result` | closeMatch | partial |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process` (`ospd.process-profiles.process-type`), status `submitted`.
