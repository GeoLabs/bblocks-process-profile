Process profile of **`calculate-band`** (CommandLineTool, W1 Algae Bloom).

> Performs a calculation with bands.

## Source

- CWL: [calculate-band.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/calculate-band.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.algae-bloom.workflow-earth-search-process`, `ospd.process-profiles.algae-bloom.workflow-copernicus-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `name` | string | `result` | File |
| `calc` | string |  |  |
| `band_a` | File? |  |  |
| `band_b` | File? |  |  |
| `band_c` | File? |  |  |
| `band_d` | File? |  |  |
| `band_e` | File? |  |  |
| `band_f` | File? |  |  |
| `band_g` | File? |  |  |
| `band_h` | File? |  |  |
| `band_i` | File? |  |  |
| `band_j` | File? |  |  |
| `band_k` | File? |  |  |
| `band_l` | File? |  |  |
| `band_m` | File? |  |  |
| `band_n` | File? |  |  |
| `band_o` | File? |  |  |
| `band_p` | File? |  |  |
| `band_q` | File? |  |  |
| `band_r` | File? |  |  |
| `band_s` | File? |  |  |
| `band_t` | File? |  |  |
| `band_u` | File? |  |  |
| `band_v` | File? |  |  |
| `band_w` | File? |  |  |
| `band_x` | File? |  |  |
| `band_y` | File? |  |  |
| `band_z` | File? |  |  |

## Analysis

**Behaviour.** Image entrypoint `gdal_calc.py`; fixed arguments
`--co TILED=YES --overwrite --type Float32`; `--calc <expr> --outfile <name>.tiff`. The
formulas come from Se2WaQ (Potes et al. 2018; Toming et al. 2016), per the base image labels.

**CWL specifics.**
- 28 inputs: `name`, `calc` and 26 optional `File?` bands `band_a`..`band_z`, each accepting
  `ogc:geotiff | iana:image/tiff | iana:image/jp2`. The transform resolves each to a `oneOf`
  of one binary schema per format (M-01/M-02, fixed 2026-09-23 in `eoap.cct.cwl-to-ogcprocess`
  itself).
- `calc` is an unconstrained string evaluated as Python: the processDescription cannot say
  which band letters are required, so the process is only meaningful with its callers'
  `valueFrom` expressions. This is the main profiling limit of the tool.
- `doc` says "calculation over JPEG bands" but the Earth-Search variant feeds GeoTIFFs.

**Provenance.** The expression is the scientific content: it must be recorded as a
parameter entity (`calc`) so that turbidity, chlorophyll-a and cyanobacteria runs can be
told apart. With the generic profile this is only possible as a plain `prov:Entity` with
`value` (GP-4); the activity type alone (`calculate-band`) does not identify the indicator.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main/calculate_turbidity_2` (scatter iteration 2, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Generic band math (gdal_calc.py with a Python/numpy expression over up to 26 bands A..Z): openEO expresses it as reduce_dimension over the `bands` dimension with a callback built from math processes. closeMatch at the generic level; each W1 instance is a fixed chain of math processes (see decomposition). The expression is free text in CWL, a process graph in openEO.

- `closeMatch`: `ogc.openeo.processes.cubes.reduce_dimension`
- `relatedMatch`: `ogc.openeo.processes.math.divide`, `ogc.openeo.processes.math.power`, `ogc.openeo.processes.math.multiply`, `ogc.openeo.processes.math.subtract`

| Stage | openEO | Level | Note |
|---|---|---|---|
| chlorophyll_a = 4.26*((C/A)**3.94), A=B01 60m, C=B03 60m | `ogc.openeo.processes.math.divide`, `ogc.openeo.processes.math.power`, `ogc.openeo.processes.math.multiply` | closeMatch |  |
| cyanobacteria = 115530*(((B*C)/A)**2.38), A=B02, B=B03, C=B04 (10m) | `ogc.openeo.processes.math.multiply`, `ogc.openeo.processes.math.divide`, `ogc.openeo.processes.math.power` | closeMatch | coefficient is 115530 in the Earth-Search variant, 115530.31 in the Copernicus variant |
| turbidity = (8.93*(C/A))-6.39, A=B01 60m, C=B03 60m | `ogc.openeo.processes.math.divide`, `ogc.openeo.processes.math.multiply`, `ogc.openeo.processes.math.subtract` | closeMatch |  |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/calculate-band` (`ospd.process-profiles.process-type`), status `submitted`.
