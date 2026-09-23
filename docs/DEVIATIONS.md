# Deviations from `eoap.cct.cwl-to-ogcprocess`

Mapping used: `eoap.cct.cwl-to-ogcprocess` (GeoLabs/bblocks-eoap-cct `c27c60d`, status
*under-development*), jq transform `transforms/cwl-to-ogcprocess.jq` (inline variant), run
**unchanged** by `scripts/generate.py`. Every change applied afterwards is listed here and in the
`description.md` of the profile concerned; when a profile was changed, the raw transform output is
kept as `examples/processDescription.raw.json` and validated against the plain
`ogc.api.processes.v1.schemas.process`.

Legend: **Corrected** = manual change applied in the profile (profile tagged `manually-corrected`);
**Documented** = left as produced, gap recorded.

| ID | Gap in the mapping | Where it bites | Handling |
|---|---|---|---|
| M-01 | CWL `format` of `File` inputs/outputs is ignored: every file becomes `{type: string, contentMediaType: application/octet-stream}` | all 10 W1 profiles (GeoTIFF, JP2, PNG, GeoJSON) | **Corrected**: media type taken from the CWL `format` IRI (`ogc:geotiff` → `image/tiff; application=geotiff`, `iana:image/png` → `image/png`, `iana:image/jp2` → `image/jp2`, `iana:application/geo+json` → `application/geo+json`) and `contentEncoding: binary` added, as in the OGC API - Processes Part 1 binary-input examples |
| M-02 | A list of accepted CWL formats is not expressible in the output | `reproject-image`, `plot-image`, `calculate-band` (26 inputs) | **Corrected**: `oneOf` of one binary schema per format (Part 1 convention). Note: the branches differ only by `contentMediaType`, an annotation, so a strict JSON Schema validator matches all branches (see Q-M02) |
| M-03 | Only the first `Workflow` of a packed `$graph` is converted; a `CommandLineTool` of a packed document cannot be profiled on its own | `kindgrove.parse-aoi`, `kindgrove.mangrove` | **Documented + generator step**: the tool is isolated and inherits the document-level keys (`cwlVersion`, `$namespaces`, `s:*` annotations), which gives it `version: 0.0.1` and the document authorship. Whether that inheritance is correct is Q-M03 |
| M-04 | `cwltool:Secrets` (hints) is ignored: credentials become plain `string` inputs | `download-band-sentinel2-product-safe`, `workflow-copernicus`, `workflow-copernicus-process` | **Corrected**: `writeOnly: true` on the secret inputs (allowed by the OGC schema object). cwltool itself redacts them as `(secret-<uuid>)` in its log and in the CWLProv research object (verified on `w1-copernicus`: job order, PROV entities and engine log carry the placeholders, never the values) |
| M-05 | A `Directory` output is always mapped to a **STAC Collection** | `kindgrove.mangrove`, `kindgrove.mangrove-workflow` | **Corrected** (2026-09-23): the run record (`w2-pinned`, a plain `cwltool --provenance` run with no stage-out) shows `mangrove_cli` itself writes `outputs/catalog.json`, a STAC **Catalog** 1.1.0 with one Item (`mangrove-analysis-<timestamp>.json`, assets `mangrove_mask.tif`, `biomass_summary.csv`, `carbon_summary.csv`). The transform's Collection schema (`enum: [Collection]`, required `extent`, `license`) rejects that output, so the output schema is replaced by a Catalog schema (`generate.py` `STAC_CATALOG_SCHEMA`, `profiles.yaml` `stac_catalog`). The earlier claim that the STAC document comes from the platform stage-out was wrong; what stage-out adds on top of it is still Q-W2-STAC |
| M-06 | Fixed-arity CWL arrays (`int[]` holding `[x, y]`) become unbounded arrays; `maxOccurs: 1` + `type: array` vs `maxOccurs: n` is not decided by the mapping | `reproject-image` (`output_dimensions`, `output_resolution`), `select-products-sentinel2` (`toi`) | **Documented**: CWL cannot declare the arity, so no source for `minItems/maxItems` |
| M-07 | The EOAP `BBox` custom type uses `crs` values `CRS84` / `CRS84h`; OGC API - Processes Part 1 (`ogc.api.processes.v1.schemas.bbox`) expects the CRS URIs (`http://www.opengis.net/def/crs/OGC/1.3/CRS84`, …). An execute value built from the CWL type is rejected by the Part 1 bbox schema | `kindgrove.mangrove-workflow`, `kindgrove.parse-aoi` | **Documented**: upstream question for eoap/schemas (Q-M07). The profile's execute example follows the CWL type |
| M-08 | Missing `label` / `doc` → `title` = id and a placeholder `description: "Process converted from CWL"` | `kindgrove.parse-aoi`, `kindgrove.mangrove` | **Documented** in the processDescription; the process-type entries use a hand-written label/definition (`scripts/profiles.yaml`) |
| M-09 | YAML block scalars keep their trailing newline in `title` | the 4 W1 workflows | **Documented** (cosmetic) |
| M-10 | Inputs/outputs without `doc` get `description: ""` | most profiles | **Documented** (cosmetic) |
| M-11 | `mutable: true` and `jobControlOptions: [async-execute]` are Part 2 (DRU) assumptions; `mutable` is defined only in `ogc.api.processes.v2.schemas.staticIndicator` | all profiles | **Documented**: each profile depends on `ogc.api.processes.v2.schemas.staticIndicator` in addition to the Part 1 `process` schema |
| M-12 | Two parallel mapping artefacts (jq transform vs JSON-LD + SHACL `semantic-uplift`) and two jq variants (inline vs `-refs`); which is normative is not stated | — | **Documented**: the inline jq transform is used because it is the only path that produces processDescription JSON (Q-M12) |

## Upstream issues met while validating (not the mapping)

| ID | Issue | Handling |
|---|---|---|
| U-01 | `ogc.api.processes.v1.schemas.execute` / `results` / `inputValueNoObject` use `oneOf` over `string`, `number`, `integer` and `binaryInputValue` (`string` + `format: byte`): an integer matches both `number` and `integer`, a string matches both `string` and `binaryInputValue` (formats are not asserted), so plain literal inputs are rejected | Each profile defines its own `$defs/execute` and `$defs/results`, built on the processDescription names and on `ogc.api.processes.v1.schemas.link` / `qualifiedInputValue`. Proposed upstream fix: `anyOf` |
| U-02 | `ogc.api.processes.` is used by three registers (v1 schemas, Part 2 schemas, standard-as-BBs); no collision today (`v1.*`, `v2.*`, `part1.*`/`part2.*`) | none; watch when importing further forks |

## Deviations needed to execute the pinned W1 package (run record `w1-earth-search`)

None of these touches a CWL file; they are what it took to obtain the two W1 run records of
2026-09-23 (`w1-earth-search`, `w1-copernicus`). The Copernicus run needs Copernicus Data Space S3
credentials; cwltool writes them into the research object as `(secret-<uuid>)` placeholders only
(M-04), verified on `primary-job.json`, the PROV entities and the engine log.

| ID | Issue | Handling |
|---|---|---|
| U-03 | `reproject-image.cwl` declares `dockerPull: ogc-ospd/algae-usecase/reproject-image` **without a tag**, while `docker-compose.yml` builds `ogc-ospd/algae-usecase/reproject-image:1.0.0`; cwltool pulls `:latest`, which does not exist. **The pinned package cannot run as published**, even with every image built (consequence of GP-6). Also, `docker compose build` does not order builds by `depends_on`: `base` must be built first or BuildKit tries to pull it from Docker Hub | `docker tag ogc-ospd/algae-usecase/reproject-image:1.0.0 ogc-ospd/algae-usecase/reproject-image:latest`. Upstream fix: pin the tag in the CWL |
| U-04 | On **linux/arm64** the conda-forge `gdal=3.6.2` package (`env-algae-usecase.yml`) ships `gdal_calc.py` with a cross-compilation shebang (`#!/home/conda/feedstock_root/.../cross-python`) that does not exist at runtime: `calculate-band` (`ENTRYPOINT ["gdal_calc.py"]`) fails with `exec: no such file or directory`. amd64 hosts are not affected | Local only: an extra layer on `calculate-band:1.1.0` rewriting the shebang to the environment's `python`. Same tag, same CWL. A platform artefact, not a package defect; recorded because the run record was produced on such a host |
| U-05 | `plot_cyanobacteria` renders the 10 m cyanobacteria raster (485 MB GeoTIFF, B02/B03/B04) with matplotlib; two runs in parallel in a 16 GB Docker VM got one of them OOM-killed (exit 137). `calculate-band`/`plot-image` declare no `ResourceRequirement` | Run one workflow at a time. Upstream: a `ramMin` on the plot tool, or plotting at 60 m |
