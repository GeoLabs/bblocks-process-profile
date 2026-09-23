
# Process type register entry (Schema)

`ospd.process-profiles.process-type` *v0.1*

Candidate entry for the OSPD process-type register (Activity 4), linking a process profile, its six-phase position, its provenance class and its proposed openEO equivalences.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Schema of a **candidate process-type register entry** (OSPD Activity 4).

A process type classifies the activities recorded in provenance. The link is one-way and uses
plain W3C PROV: a provenance `Activity` (or a `wfprov:ProcessRun` / `wfprov:WorkflowRun`) of this
type carries the entry `id` in `activityType`. The entry itself is a SKOS concept:

- `phase` (→ `skos:broader`) positions the process in the six-phase framework
  (filter configuration → selection/filtering → data retrieval → pre-processing →
  scientific computation → export/aggregation);
- `exactMatch` / `closeMatch` / `relatedMatch` (→ SKOS mapping properties) point to openEO
  Building Blocks (`https://www.opengis.net/def/bblocks/ogc.openeo.*`);
- `openeoEquivalence.level` states the equivalence level explicitly, including `none`, which
  SKOS cannot express, with the rationale and, for composite or opaque processes, a
  stage-by-stage decomposition.

Status values follow ISO 19135. Entries in this register are candidates: at most `submitted`.

The `pp:` vocabulary (`https://geolabs.github.io/bblocks-process-profiles/def/`) and the phase IRIs
are provisional, pending a decision on the process-type register namespace.

## Examples

### reproject-image (closeMatch)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "type": "ProcessType",
  "prefLabel": "Performs image reprojection.",
  "definition": "Performs a reprojection over image bands and returns the resulting GeoTiff.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
  ],
  "profile": "ospd.process-profiles.algae-bloom.reproject-image",
  "processDescription": {
    "id": "reproject-image",
    "version": "1.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image",
  "type": "ProcessType",
  "prefLabel": "Performs image reprojection.",
  "definition": "Performs a reprojection over image bands and returns the resulting GeoTiff.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing"
  ],
  "profile": "ospd.process-profiles.algae-bloom.reproject-image",
  "processDescription": {
    "id": "reproject-image",
    "version": "1.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "reproject-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place."
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/reproject-image> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.resample_spatial> ;
    skos:definition "Performs a reprojection over image bands and returns the resulting GeoTiff." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Performs image reprojection." ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "As used in W1 the tool only changes the pixel size (gdalwarp `-tr 60 60`, nearest neighbour by default, no `-t_srs`): resample_spatial with `resolution: 60`, `projection: null`, `method: near`. Not an exactMatch: `output_dimensions` (`-ts`) has no openEO parameter, the output type is forced to Float32 (`-ot Float32`), and the tool works on a file rather than a data cube. Despite its name, no CRS transformation takes place." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/reproject-image> ;
    pp:profile "ospd.process-profiles.algae-bloom.reproject-image" ;
    pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ;
    pp:source [ dcterms:license <https://spdx.org/licenses/CC-BY-NC-SA-4.0> ;
            pp:cwl <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/reproject-image.cwl> ;
            pp:cwlClass "CommandLineTool" ;
            pp:cwlId "reproject-image" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/reproject-image> pp:version "1.0.0" .


```


### KindGrove mangrove (none, with decomposition)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "type": "ProcessType",
  "prefLabel": "Mangrove biomass and carbon estimation",
  "definition": "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook).",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.kindgrove.mangrove",
  "processDescription": {
    "id": "mangrove_cli",
    "version": "0.0.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli",
    "cwlClass": "CommandLineTool",
    "cwlId": "mangrove_cli",
    "license": "https://spdx.org/licenses/Apache-2.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.bbox"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data).",
    "decomposition": [
      {
        "stage": "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "NDVI (nir-red)/(nir+red+1e-8)",
        "openeo": [
          "ogc.openeo.processes.cubes.ndvi",
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch",
        "note": "epsilon 1e-8 in the denominator"
      },
      {
        "stage": "NDWI (green-nir)/(green+nir+1e-8)",
        "openeo": [
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "SAVI ((nir-red)/(nir+red+0.5))*1.5",
        "openeo": [],
        "level": "none",
        "note": "no stable process; composition of add/subtract/divide/multiply"
      },
      {
        "stage": "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2",
        "openeo": [
          "ogc.openeo.processes.comparison.gt",
          "ogc.openeo.processes.comparison.lt",
          "ogc.openeo.processes.logic.and",
          "ogc.openeo.processes.cubes.mask"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "biomass = 250.5*NDVI - 75.2",
        "openeo": [
          "ogc.openeo.processes.cubes.apply",
          "ogc.openeo.processes.math.multiply",
          "ogc.openeo.processes.math.subtract"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "carbon stock and totals (IPCC carbon fraction 0.47)",
        "openeo": [
          "ogc.openeo.processes.cubes.aggregate_spatial",
          "ogc.openeo.processes.math.sum",
          "ogc.openeo.processes.math.multiply"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "export CSV + GeoTIFF",
        "openeo": [
          "ogc.openeo.processes.cubes.save_result"
        ],
        "level": "closeMatch",
        "note": "CSV summaries are not a raster format"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove",
  "type": "ProcessType",
  "prefLabel": "Mangrove biomass and carbon estimation",
  "definition": "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook).",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.kindgrove.mangrove",
  "processDescription": {
    "id": "mangrove_cli",
    "version": "0.0.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli",
    "cwlClass": "CommandLineTool",
    "cwlId": "mangrove_cli",
    "license": "https://spdx.org/licenses/Apache-2.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.bbox"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data).",
    "decomposition": [
      {
        "stage": "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "NDVI (nir-red)/(nir+red+1e-8)",
        "openeo": [
          "ogc.openeo.processes.cubes.ndvi",
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch",
        "note": "epsilon 1e-8 in the denominator"
      },
      {
        "stage": "NDWI (green-nir)/(green+nir+1e-8)",
        "openeo": [
          "ogc.openeo.processes.math.indices.normalized_difference"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "SAVI ((nir-red)/(nir+red+0.5))*1.5",
        "openeo": [],
        "level": "none",
        "note": "no stable process; composition of add/subtract/divide/multiply"
      },
      {
        "stage": "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2",
        "openeo": [
          "ogc.openeo.processes.comparison.gt",
          "ogc.openeo.processes.comparison.lt",
          "ogc.openeo.processes.logic.and",
          "ogc.openeo.processes.cubes.mask"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "biomass = 250.5*NDVI - 75.2",
        "openeo": [
          "ogc.openeo.processes.cubes.apply",
          "ogc.openeo.processes.math.multiply",
          "ogc.openeo.processes.math.subtract"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "carbon stock and totals (IPCC carbon fraction 0.47)",
        "openeo": [
          "ogc.openeo.processes.cubes.aggregate_spatial",
          "ogc.openeo.processes.math.sum",
          "ogc.openeo.processes.math.multiply"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "export CSV + GeoTIFF",
        "openeo": [
          "ogc.openeo.processes.cubes.save_result"
        ],
        "level": "closeMatch",
        "note": "CSV summaries are not a raster format"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> ;
    skos:definition "Detects mangroves from Sentinel-2 L2A vegetation indices within a bounding box and estimates above-ground biomass and carbon stock (ipython2cwl binary of the KindGrove notebook)." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Mangrove biomass and carbon estimation" ;
    pp:candidateCctDependency "eoap.cct.bbox" ;
    pp:openeoEquivalence [ pp:decomposition ( [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.load_collection" ;
                        pp:stage "STAC search, Earth-Search sentinel-2-l2a, bbox, cloud cover, last N days" ] [ skos:note "epsilon 1e-8 in the denominator" ;
                        pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.ndvi",
                            "ogc.openeo.processes.math.indices.normalized_difference" ;
                        pp:stage "NDVI (nir-red)/(nir+red+1e-8)" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.math.indices.normalized_difference" ;
                        pp:stage "NDWI (green-nir)/(green+nir+1e-8)" ] [ skos:note "no stable process; composition of add/subtract/divide/multiply" ;
                        pp:equivalenceLevel "none" ;
                        pp:stage "SAVI ((nir-red)/(nir+red+0.5))*1.5" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.comparison.gt",
                            "ogc.openeo.processes.comparison.lt",
                            "ogc.openeo.processes.cubes.mask",
                            "ogc.openeo.processes.logic.and" ;
                        pp:stage "mangrove mask: 0.3<NDVI<0.9 and NDWI>-0.3 and SAVI>0.2" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.apply",
                            "ogc.openeo.processes.math.multiply",
                            "ogc.openeo.processes.math.subtract" ;
                        pp:stage "biomass = 250.5*NDVI - 75.2" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.aggregate_spatial",
                            "ogc.openeo.processes.math.multiply",
                            "ogc.openeo.processes.math.sum" ;
                        pp:stage "carbon stock and totals (IPCC carbon fraction 0.47)" ] [ skos:note "CSV summaries are not a raster format" ;
                        pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.save_result" ;
                        pp:stage "export CSV + GeoTIFF" ] ) ;
            pp:equivalenceLevel "none" ;
            pp:rationale "Opaque: one ipython2cwl binary running the whole notebook. No single openEO process; each notebook stage has a closeMatch (decomposition). run_udf could wrap the binary but expects a data cube in and out, which this tool does not follow (it searches and downloads its own data)." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove_cli> ;
    pp:profile "ospd.process-profiles.kindgrove.mangrove" ;
    pp:provenanceClass <http://purl.org/wf4ever/wfprov#ProcessRun> ;
    pp:source [ dcterms:license <https://spdx.org/licenses/Apache-2.0> ;
            pp:cwl <https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove_cli> ;
            pp:cwlClass "CommandLineTool" ;
            pp:cwlId "mangrove_cli" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove_cli> pp:version "0.0.1" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Candidate entry for the OSPD process-type register (Activity 4). A process
  type classifies the

  activities recorded in provenance: a provenance Activity of this type carries the
  entry `id` as

  its `activityType`. The entry is modelled as a SKOS concept; openEO equivalences
  use the SKOS

  mapping properties.

  '
type: object
required:
- id
- type
- prefLabel
- definition
- inScheme
- status
- phase
- profile
- source
- provenanceClass
- openeoEquivalence
properties:
  id:
    description: IRI of the process type (also used as `activityType` in provenance
      records).
    type: string
    format: uri
    x-jsonld-id: '@id'
  type:
    const: ProcessType
    x-jsonld-id: '@type'
  prefLabel:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
  definition:
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    description: IRI of the process-type register (concept scheme) this entry is proposed
      to.
    type: string
    format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status:
    description: ISO 19135 item status. Entries produced here are candidates, hence
      `submitted` at most.
    type: string
    enum:
    - submitted
    - valid
    - invalid
    - superseded
    - retired
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/status
  phase:
    description: Position(s) in the six-phase workflow framework.
    type: array
    minItems: 1
    items:
      type: string
      enum:
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation
      - https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
  profile:
    description: Identifier of the process-profile Building Block.
    type: string
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/profile
  processDescription:
    type: object
    required:
    - id
    - version
    properties:
      id:
        type: string
        x-jsonld-id: '@id'
      version:
        type: string
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/version
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/processDescription
  source:
    type: object
    required:
    - cwl
    - cwlClass
    - cwlId
    properties:
      cwl:
        description: Pinned URL of the CWL document.
        type: string
        format: uri
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwl
        x-jsonld-type: '@id'
      cwlClass:
        enum:
        - CommandLineTool
        - Workflow
        - ExpressionTool
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwlClass
      cwlId:
        type: string
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwlId
      license:
        type: string
        format: uri
        x-jsonld-id: http://purl.org/dc/terms/license
        x-jsonld-type: '@id'
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/source
  provenanceClass:
    description: Class of the run records produced by executing this process.
    type: string
    enum:
    - http://purl.org/wf4ever/wfprov#ProcessRun
    - http://purl.org/wf4ever/wfprov#WorkflowRun
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/provenanceClass
    x-jsonld-type: '@id'
  cctDependencies:
    description: EOAP CWL custom types used by the CWL source.
    type: array
    items:
      type: string
      pattern: ^eoap\.cct\.
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cctDependency
  candidateCctDependencies:
    description: EOAP CWL custom types that could replace plain CWL types (not used
      by the source).
    type: array
    items:
      type: string
      pattern: ^eoap\.cct\.
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/candidateCctDependency
  hasStep:
    description: Process types of the steps of a Workflow.
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/hasStep
    x-jsonld-type: '@id'
  exactMatch:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
    x-jsonld-type: '@id'
  closeMatch:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#closeMatch
    x-jsonld-type: '@id'
  relatedMatch:
    type: array
    items:
      type: string
      format: uri
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#relatedMatch
    x-jsonld-type: '@id'
  openeoEquivalence:
    type: object
    required:
    - level
    - rationale
    properties:
      level:
        enum:
        - exactMatch
        - closeMatch
        - none
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
      rationale:
        type: string
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/rationale
      decomposition:
        description: Ordered correspondence of the stages of a composite or opaque
          process.
        type: array
        items:
          type: object
          required:
          - stage
          - level
          properties:
            stage:
              type: string
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/stage
            openeo:
              type: array
              items:
                type: string
                pattern: ^ogc\.openeo\.
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/openeo
            level:
              enum:
              - exactMatch
              - closeMatch
              - none
              x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
            note:
              type: string
              x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
        x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/decomposition
        x-jsonld-container: '@list'
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/openeoEquivalence
x-jsonld-extra-terms:
  ProcessType: http://www.w3.org/2004/02/skos/core#Concept
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  pp: https://geolabs.github.io/bblocks-process-profiles/def/

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ProcessType": "skos:Concept",
    "id": "@id",
    "type": "@type",
    "prefLabel": "skos:prefLabel",
    "definition": "skos:definition",
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "status": "pp:status",
    "phase": {
      "@id": "skos:broader",
      "@type": "@id"
    },
    "profile": "pp:profile",
    "processDescription": {
      "@context": {
        "version": "pp:version"
      },
      "@id": "pp:processDescription"
    },
    "source": {
      "@context": {
        "cwl": {
          "@id": "pp:cwl",
          "@type": "@id"
        },
        "cwlClass": "pp:cwlClass",
        "cwlId": "pp:cwlId",
        "license": {
          "@id": "http://purl.org/dc/terms/license",
          "@type": "@id"
        }
      },
      "@id": "pp:source"
    },
    "provenanceClass": {
      "@id": "pp:provenanceClass",
      "@type": "@id"
    },
    "cctDependencies": "pp:cctDependency",
    "candidateCctDependencies": "pp:candidateCctDependency",
    "hasStep": {
      "@id": "pp:hasStep",
      "@type": "@id"
    },
    "exactMatch": {
      "@id": "skos:exactMatch",
      "@type": "@id"
    },
    "closeMatch": {
      "@id": "skos:closeMatch",
      "@type": "@id"
    },
    "relatedMatch": {
      "@id": "skos:relatedMatch",
      "@type": "@id"
    },
    "openeoEquivalence": {
      "@context": {
        "level": "pp:equivalenceLevel",
        "rationale": "pp:rationale",
        "decomposition": {
          "@context": {
            "stage": "pp:stage",
            "openeo": "pp:openeo",
            "note": "skos:note"
          },
          "@id": "pp:decomposition",
          "@container": "@list"
        }
      },
      "@id": "pp:openeoEquivalence"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "pp": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/context.jsonld)

## Sources

* [ISO 19135-1 Geographic information - Procedures for item registration](https://www.iso.org/standard/54721.html)
* [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/process-type`

