Process profile of **`download-band-sentinel2-product-safe`** (CommandLineTool, W1 Algae Bloom).

> Downloads Copernicus products.

## Source

- CWL: [download-band-sentinel2-product-safe.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/download-band-sentinel2-product-safe.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval
- EOAP CWL custom types used: none; candidates: `eoap.cct.string-format`
- Used by: `ospd.process-profiles.algae-bloom.workflow-copernicus-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `product_url` | string | `product` | File |
| `s3_access_key` | string |  |  |
| `s3_secret_key` | string |  |  |
| `resolution` | ["null", {"type": "enum", "symbols": ["10m", "20m", "60m"]}] |  |  |
| `band` | {"type": "enum", "symbols": ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B11", "B12", "AOT", "SCL", "TCI", "WVP"]} |  |  |
| `debug` | boolean? |  |  |

## Analysis

**Behaviour.** Opens the SAFE manifest from `s3:///eodata/...` (Copernicus Data Space S3,
authenticated) and extracts `T<tile>_<datetime>_<band>_<res>.jp2`.

**CWL specifics.**
- `s3_access_key` / `s3_secret_key` are declared in the `cwltool:Secrets` hint. The engine
  redacts them in the log (`(secret-<uuid>)`), but the transform exposes them as plain
  `string` inputs (M-04).
- `resolution` is `null | enum` (optional enum), `debug` an optional boolean with default.
- Output `product` is `File` with `format: iana:image/jp2`, dropped by the transform (M-01).

**Provenance.** Secret inputs must be recorded as entities without value (GP-5): the generic
profile has no redaction convention, the example records the input entity with no `value`.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-04 inputs.s3_access_key: declared in cwltool:Secrets -> writeOnly: true
- M-04 inputs.s3_secret_key: declared in cwltool:Secrets -> writeOnly: true

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-copernicus`: Copernicus variant of the pinned W1 package, `cwltool --outdir ./results1 --provenance ./PROV1 algae-usecase-workflow-copernicus.cwl example/algae-usecase-job-copernicus.yml` with Copernicus Data Space S3 credentials, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; one product (S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542). cwltool writes the `cwltool:Secrets` inputs as `(secret-<uuid>)` placeholders in the research object), activity `main/download_b03_60m` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Same operation as the STAC-Item variant (one band of one product) but reading the SAFE archive on S3 with user credentials and a `resolution` selector (10m/20m/60m). openEO has no credential parameters (handled by the back-end) and chooses native resolution per band; choosing another resolution is resample_spatial territory.

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands`
- `relatedMatch`: `ogc.openeo.types.band-name`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/download-band-sentinel2-product-safe` (`ospd.process-profiles.process-type`), status `submitted`.
