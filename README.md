# bblocks-process-profiles

OGC Building Blocks register holding **process profiles** for the deployable CWL processes of the
OSPD 2026 reference workflows. Identifier prefix: `ospd.process-profiles.`

| Workflow | Source (linked, not copied) |
|---|---|
| W1 Algae Bloom | [`crim-ca/ogc-ospd-phase1@5edd4ec`](https://github.com/crim-ca/ogc-ospd-phase1/tree/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg) (CC-BY-NC-SA-4.0) |
| W2 KindGrove | [`GeoLabs/bblocks-eoap-cct@291a741`](https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl) |
| W3 Water Bodies | [`gfenoy/mastering-app-package@40ecc09`](https://github.com/gfenoy/mastering-app-package/blob/40ecc096da56c6810758b87b01a87502f7c4507c/cwl-workflow/app-water-bodies-cloud-native.cwl) (CC-BY-SA-4.0; tool images from `Terradue/ogc-eo-application-package-hands-on`) |

## Building blocks

| Identifier | CWL class | Phase(s) | openEO |
|---|---|---|---|
| `ospd.process-profiles.algae-bloom.workflow-earth-search` | Workflow | Filter configuration, Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none |
| `ospd.process-profiles.algae-bloom.workflow-earth-search-process` | Workflow | Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none |
| `ospd.process-profiles.algae-bloom.workflow-copernicus` | Workflow | Filter configuration, Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none |
| `ospd.process-profiles.algae-bloom.workflow-copernicus-process` | Workflow | Data retrieval, Scientific computation, Export / aggregation | none |
| `ospd.process-profiles.algae-bloom.select-products-sentinel2` | CommandLineTool | Selection / filtering | closeMatch: processes.cubes.load_collection |
| `ospd.process-profiles.algae-bloom.download-band-sentinel2-stac-item` | CommandLineTool | Data retrieval | closeMatch: processes.cubes.load_collection, processes.cubes.filter_bands |
| `ospd.process-profiles.algae-bloom.download-band-sentinel2-product-safe` | CommandLineTool | Data retrieval | closeMatch: processes.cubes.load_collection, processes.cubes.filter_bands |
| `ospd.process-profiles.algae-bloom.reproject-image` | CommandLineTool | Pre-processing | closeMatch: processes.cubes.resample_spatial |
| `ospd.process-profiles.algae-bloom.calculate-band` | CommandLineTool | Scientific computation | closeMatch: processes.cubes.reduce_dimension |
| `ospd.process-profiles.algae-bloom.plot-image` | CommandLineTool | Export / aggregation | closeMatch: processes.cubes.save_result |
| `ospd.process-profiles.kindgrove.mangrove-workflow` | Workflow | Filter configuration, Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none |
| `ospd.process-profiles.kindgrove.parse-aoi` | CommandLineTool | Filter configuration | none |
| `ospd.process-profiles.kindgrove.mangrove` | CommandLineTool | Selection / filtering, Data retrieval, Pre-processing, Scientific computation, Export / aggregation | none |
| `ospd.process-profiles.water-bodies.water-bodies` | Workflow | Data retrieval, Scientific computation, Export / aggregation | none |
| `ospd.process-profiles.water-bodies.detect-water-body` | Workflow | Data retrieval, Scientific computation | none |
| `ospd.process-profiles.water-bodies.crop` | CommandLineTool | Data retrieval | closeMatch: processes.cubes.load_collection, processes.cubes.filter_bands |
| `ospd.process-profiles.water-bodies.norm-diff` | CommandLineTool | Scientific computation | closeMatch: processes.math.indices.normalized_difference |
| `ospd.process-profiles.water-bodies.otsu` | CommandLineTool | Scientific computation | none |
| `ospd.process-profiles.water-bodies.stac` | CommandLineTool | Export / aggregation | closeMatch: processes.cubes.save_result |

Shared: `ospd.process-profiles.process-type` — schema of a candidate process-type register entry (Activity 4).

## What each process profile contains

| Artefact | Validated against |
|---|---|
| `processDescription` (default schema) | this profile = `ogc.api.processes.v1.schemas.process` + `ogc.api.processes.v2.schemas.staticIndicator` + id/input/output constraints |
| raw `cwl-to-ogcprocess` output (when a manual correction was needed) | `ogc.api.processes.v1.schemas.process` |
| OGC Application Package (Part 2 deploy body, `executionUnit` = link to the CWL) | `ogc.api.processes.v2.schemas.ogcapppkg` |
| execute request / results | `ogc.api.processes.v1.schemas.execute` / `results` |
| provenance chain | `ogc.bbr.provenance.provenance` |
| process run (CommandLineTool) | `ogc.bbr.wf4ever.wfprov.ProcessRun` (gap GP-1 in the generic profile) |
| execution bundle (Workflow) | `ogc.bbr.provenance.execution` |
| process-type entry | `ospd.process-profiles.process-type` |

## Documentation

- [docs/DEVIATIONS.md](docs/DEVIATIONS.md) — deviations from / gaps in `eoap.cct.cwl-to-ogcprocess`
- [docs/PROVENANCE-GAPS.md](docs/PROVENANCE-GAPS.md) — gaps in `bblocks-generic-provenance-profile`
- [docs/OPENEO-EQUIVALENCES.md](docs/OPENEO-EQUIVALENCES.md) — equivalence decisions and criteria
- [docs/OPEN-QUESTIONS.md](docs/OPEN-QUESTIONS.md)
- [docs/VALIDATION.md](docs/VALIDATION.md) — validation status (Docker build passing, 20/20)

## Regenerating

```bash
# needs jq, python3 (pyyaml, prov>=2 for the W3C PROV-JSONLD examples), git, cwltool + Docker
python3 scripts/run_workflows.py --sources-root DIR --runs-root DIR --build-images --generate
#   clones the pinned sources (scripts/sources.yaml `repo:`/`commit:`) under --sources-root when
#   missing, runs each entry under `runs:` with `cwltool --provenance` (asks for the Copernicus S3
#   credentials, or reads CDSE_S3_ACCESS_KEY / CDSE_S3_SECRET_KEY), stores the research objects
#   under --runs-root as named in `runs:`, then regenerates; --only NAME picks runs, --force
#   replaces an existing bag, --no-fetch leaves the clones alone
python3 scripts/generate.py --sources-root DIR --runs-root DIR   # regenerate only, never downloads
python3 scripts/validate_offline.py --deps-root ../   # pre-check only
./build.sh                                             # authoritative validation (Docker)
./view.sh                                              # http://localhost:9090
```

Generated files are overwritten; hand-written content lives in `scripts/profiles.yaml` and `docs/`.
The run-derived examples (times, engine, container images, output names and checksums) are read
from real `cwltool --provenance` research objects declared under `runs:` in `scripts/sources.yaml`;
those are local directories (the W1 one carries a 3.1 GB payload) and are not part of this
repository. Without them the generator stops.

## License

Apache-2.0 for this register. The W1 CWL files are CC-BY-NC-SA-4.0 and are **referenced by URL only**.
