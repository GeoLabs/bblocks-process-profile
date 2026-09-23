# OSPD Process Profiles

OGC API - Processes profiles for the deployable CWL processes of the OSPD 2026 reference
workflows (W1 Algae Bloom, W2 KindGrove mangrove biomass), each linked to its CWL source,
the generic provenance profile, the EOAP CWL custom types and the openEO Building Blocks.


This register is produced by GeoLabs under OSPD 2026 (D100 Workflow Profiler, D120 OGC API
Processes Profiler). It holds one Building Block per deployable CWL process (`CommandLineTool`
or `Workflow`) identified in the workflow observability investigation.

Each process profile combines:

- a reference to the source CWL (linked by URL at a pinned commit, never copied);
- an OGC API - Processes Part 1 `processDescription` derived with the
  `eoap.cct.cwl-to-ogcprocess` mapping (deviations are documented, not hidden);
- a provenance view expressed as an instance of the generic provenance profile
  (`ogc.bbr.provenance.*`);
- a candidate process-type entry (`ospd.process-profiles.process-type`) for the OSPD
  process-type register (Activity 4);
- proposed openEO equivalences (`ogc.openeo.*`) with an explicit level
  (exactMatch / closeMatch / none) and rationale;
- a representative execution example.

All mappings are proposed correspondences offered for review, not settled equivalences.


## Building Blocks

### `ospd.process-profiles.process-type` — Process type register entry

**Type:** schema

Candidate entry for the OSPD process-type register (Activity 4), linking a process profile, its six-phase position, its provenance class and its proposed openEO equivalences.

### `ospd.process-profiles.algae-bloom.calculate-band` — Process profile: calculate-band

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `calculate-band` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.download-band-sentinel2-product-safe` — Process profile: download-band-sentinel2-product-safe

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `download-band-sentinel2-product-safe` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.download-band-sentinel2-stac-item` — Process profile: download-band-sentinel2-stac-item

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `download-band-sentinel2-stac-item` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.plot-image` — Process profile: plot-image

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `plot-image` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.reproject-image` — Process profile: reproject-image

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `reproject-image` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.select-products-sentinel2` — Process profile: select-products-sentinel2

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `select-products-sentinel2` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-copernicus` — Process profile: algae-usecase-workflow-copernicus

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-copernicus` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-copernicus-process` — Process profile: algae-usecase-workflow-copernicus-process

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-copernicus-process` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-earth-search` — Process profile: algae-usecase-workflow-earth-search

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-earth-search` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.algae-bloom.workflow-earth-search-process` — Process profile: algae-usecase-workflow-earth-search-process

**Type:** schema

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-earth-search-process` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove.mangrove` — Process profile: mangrove_cli

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `mangrove_cli` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove.mangrove-workflow` — Process profile: mangrove-workflow

**Type:** schema

OGC API - Processes profile of the CWL Workflow `mangrove-workflow` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

### `ospd.process-profiles.kindgrove.parse-aoi` — Process profile: parse_aoi

**Type:** schema

OGC API - Processes profile of the CWL CommandLineTool `parse_aoi` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

