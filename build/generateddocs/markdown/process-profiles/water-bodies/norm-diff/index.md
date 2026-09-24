
# Process profile: norm_diff (Schema)

`ospd.process-profiles.water-bodies.norm-diff` *v0.1*

OGC API - Processes profile of the CWL CommandLineTool `norm_diff` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`norm_diff`** (CommandLineTool, W3 Water Bodies).

> Normalized difference between two rasters

## Source

- CWL: [norm_diff.cwl](https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl) (pinned commit `f472585`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.water-bodies.detect-water-body`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `rasters` | File[] | `ndwi` | File |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0`.
Reads the two cropped band rasters (positional `rasters: File[]`, order fixed by `node_crop`'s
scatter order over `bands`: green first, nir second in this workflow) and writes
`(A-B)/(A+B)` as one GeoTIFF (`norm_diff.tif`).

**CWL specifics.** `rasters` is `File[]` with **no positional labels**: which raster is the
minuend and which the subtrahend depends entirely on array order, not expressed anywhere in
the processDescription (an unconstrained `array` of File binary schemas).

**Provenance.** Two file inputs, one file output; a plain `wasDerivedFrom` chain (GP-3/GP-4
do not apply, both endpoints are files).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (ogc-eo-application-package-hands-on f472585 `water-bodies/app-pkg-multiple/water-bodies.cwl`, one CWL file per step), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_normalized_difference` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Exact index formula, generic over which two bands are passed: NDWI (green, nir) in this workflow, same as `ogc.openeo.processes.math.indices.normalized_difference` used for NDVI elsewhere in this register (`kindgrove.mangrove`) -- it is the caller's band choice, not the tool, that names the index.

- `closeMatch`: `ogc.openeo.processes.math.indices.normalized_difference`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL CommandLineTool is referenced, not copied: <https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl>.

### processDescription
OGC API - Processes processDescription derived from the CWL.
#### json
```json
{
  "id": "norm_diff",
  "version": "1.4.1",
  "title": "norm_diff",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "norm_diff"
    },
    {
      "role": "https://schema.org/description",
      "value": "Process converted from CWL"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.4.1"
    }
  ],
  "inputs": {
    "rasters": {
      "title": "rasters",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "application/octet-stream"
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "ndwi": {
      "title": "ndwi",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    }
  },
  "jobControlOptions": [
    "async-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld",
  "id": "norm_diff",
  "version": "1.4.1",
  "title": "norm_diff",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "norm_diff"
    },
    {
      "role": "https://schema.org/description",
      "value": "Process converted from CWL"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.4.1"
    }
  ],
  "inputs": {
    "rasters": {
      "title": "rasters",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "application/octet-stream"
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "ndwi": {
      "title": "ndwi",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    }
  },
  "jobControlOptions": [
    "async-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/norm_diff> dcterms:description "Process converted from CWL" ;
    dcterms:title "norm_diff" ;
    pp:version "1.4.1" ;
    proc:inputs [ ns1:rasters [ dcterms:description "" ;
                    dcterms:title "rasters" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentMediaType "application/octet-stream" ] ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "1.4.1" ;
            proc:role schema:softwareVersion ],
        [ rdf:value "norm_diff" ;
            proc:role schema:name ],
        [ rdf:value "Process converted from CWL" ;
            proc:role schema:description ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:ndwi [ dcterms:description "" ;
                    dcterms:title "ndwi" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ] .


```


### OGC Application Package (deploy)
Part 2 deploy body: the execution unit is a link to the pinned CWL.
#### json
```json
{
  "processDescription": {
    "process": {
      "id": "norm_diff",
      "version": "1.4.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld",
  "processDescription": {
    "process": {
      "id": "norm_diff",
      "version": "1.4.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/norm_diff> pp:version "1.4.1" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/norm_diff> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl" ;
            pp:rel "http://www.opengis.net/def/rel/ogc/1.0/executionUnit" ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "rasters": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_green.tif",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_nir.tif",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld",
  "inputs": {
    "rasters": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_green.tif",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_nir.tif",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  "response": "document"
}
```

#### ttl
```ttl
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

[] proc:inputs [ ns1:rasters [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_green.tif" ;
                    proc:type "image/tiff; application=geotiff" ],
                [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_nir.tif" ;
                    proc:type "image/tiff; application=geotiff" ] ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "ndwi": {
    "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-norm-diff-0001/results/norm_diff.tif",
    "type": "image/tiff; application=geotiff"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld",
  "ndwi": {
    "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-norm-diff-0001/results/norm_diff.tif",
    "type": "image/tiff; application=geotiff"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:ndwi [ pp:href "https://ospd.example.org/ogc-api/jobs/water-bodies-norm-diff-0001/results/norm_diff.tif" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:water-bodies:norm-diff",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff",
    "startedAtTime": "2026-09-23T20:14:14Z",
    "used": [
      "urn:example:entity:norm-diff:in:rasters"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145",
      "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/norm_diff"
      }
    ],
    "endedAtTime": "2026-09-23T20:14:35Z"
  },
  {
    "id": "urn:example:entity:norm-diff:in:rasters",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/norm_diff#inputs/rasters",
    "value": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_green.tif",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_nir.tif",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  {
    "id": "urn:example:entity:norm-diff:out:ndwi",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/norm_diff#outputs/ndwi",
    "wasGeneratedBy": "urn:example:run:water-bodies:norm-diff",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-norm-diff-0001/results/norm_diff.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:engine:cwltool-3.1.20260108082145",
    "provType": "prov:SoftwareAgent",
    "name": "cwltool 3.1.20260108082145"
  },
  {
    "id": "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0",
    "provType": "prov:SoftwareAgent",
    "name": "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
  }
]

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:water-bodies:norm-diff",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff",
      "startedAtTime": "2026-09-23T20:14:14Z",
      "used": [
        "urn:example:entity:norm-diff:in:rasters"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145",
        "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/norm_diff"
        }
      ],
      "endedAtTime": "2026-09-23T20:14:35Z"
    },
    {
      "id": "urn:example:entity:norm-diff:in:rasters",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/norm_diff#inputs/rasters",
      "value": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_green.tif",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_nir.tif",
          "type": "image/tiff; application=geotiff"
        }
      ]
    },
    {
      "id": "urn:example:entity:norm-diff:out:ndwi",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/norm_diff#outputs/ndwi",
      "wasGeneratedBy": "urn:example:run:water-bodies:norm-diff",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-norm-diff-0001/results/norm_diff.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:engine:cwltool-3.1.20260108082145",
      "provType": "prov:SoftwareAgent",
      "name": "cwltool 3.1.20260108082145"
    },
    {
      "id": "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0",
      "provType": "prov:SoftwareAgent",
      "name": "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <http://www.iana.org/assignments/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:entity:norm-diff:out:ndwi> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/norm_diff#outputs/ndwi> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/water-bodies-norm-diff-0001/results/norm_diff.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:water-bodies:norm-diff> .

<urn:example:entity:norm-diff:in:rasters> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/norm_diff#inputs/rasters> ;
    rdf:value [ pp:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_green.tif" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/crop_nir.tif" ] .

<urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0> a prov:SoftwareAgent ;
    pp:name "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0" .

<urn:example:run:water-bodies:norm-diff> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff> ;
    prov:endedAtTime "2026-09-23T20:14:35+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/norm_diff> ] ;
    prov:startedAtTime "2026-09-23T20:14:14+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:norm-diff:in:rasters> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145>,
        <urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0> .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Process run (wfprov:ProcessRun, gap GP-1)
#### json
```json
{
  "id": "urn:example:run:water-bodies:norm-diff",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/norm_diff",
  "usedInput": [
    {
      "id": "urn:example:entity:norm-diff:in:rasters"
    }
  ],
  "startedAtTime": "2026-09-23T20:14:14Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:water-bodies:detect-water-body"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld",
  "id": "urn:example:run:water-bodies:norm-diff",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/norm_diff",
  "usedInput": [
    {
      "id": "urn:example:entity:norm-diff:in:rasters"
    }
  ],
  "startedAtTime": "2026-09-23T20:14:14Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:water-bodies:detect-water-body"
}
```

#### ttl
```ttl
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:run:water-bodies:norm-diff> a wfprov:ProcessRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff> ;
    wfprov:describedByProcess <https://ospd.example.org/ogc-api/processes/norm_diff> ;
    wfprov:usedInput <urn:example:entity:norm-diff:in:rasters> ;
    wfprov:wasPartOfWorkflowRun <urn:example:run:water-bodies:detect-water-body> ;
    prov:startedAtTime "2026-09-23T20:14:14+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff",
  "type": "ProcessType",
  "prefLabel": "Normalized difference between two rasters",
  "definition": "Computes the normalized difference index ((A-B)/(A+B)) of two co-registered rasters.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.water-bodies.norm-diff",
  "processDescription": {
    "id": "norm_diff",
    "version": "1.4.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "norm_diff",
    "license": "https://spdx.org/licenses/CC-BY-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.indices.normalized_difference"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Exact index formula, generic over which two bands are passed: NDWI (green, nir) in this workflow, same as `ogc.openeo.processes.math.indices.normalized_difference` used for NDVI elsewhere in this register (`kindgrove.mangrove`) -- it is the caller's band choice, not the tool, that names the index."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff",
  "type": "ProcessType",
  "prefLabel": "Normalized difference between two rasters",
  "definition": "Computes the normalized difference index ((A-B)/(A+B)) of two co-registered rasters.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.water-bodies.norm-diff",
  "processDescription": {
    "id": "norm_diff",
    "version": "1.4.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "norm_diff",
    "license": "https://spdx.org/licenses/CC-BY-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.indices.normalized_difference"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Exact index formula, generic over which two bands are passed: NDWI (green, nir) in this workflow, same as `ogc.openeo.processes.math.indices.normalized_difference` used for NDVI elsewhere in this register (`kindgrove.mangrove`) -- it is the caller's band choice, not the tool, that names the index."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/norm-diff> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.indices.normalized_difference> ;
    skos:definition "Computes the normalized difference index ((A-B)/(A+B)) of two co-registered rasters." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Normalized difference between two rasters" ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "Exact index formula, generic over which two bands are passed: NDWI (green, nir) in this workflow, same as `ogc.openeo.processes.math.indices.normalized_difference` used for NDVI elsewhere in this register (`kindgrove.mangrove`) -- it is the caller's band choice, not the tool, that names the index." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/norm_diff> ;
    pp:profile "ospd.process-profiles.water-bodies.norm-diff" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:source [ pp:cwl <https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/norm_diff.cwl> ;
            pp:cwlClass "CommandLineTool" ;
            pp:cwlId "norm_diff" ;
            pp:license "https://spdx.org/licenses/CC-BY-SA-4.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/norm_diff> pp:version "1.4.1" .


```


### Run record, W3C PROV-JSONLD (cwltool CWLProv bundle)
The CWLProv bundle of the run record that holds this profile's activity, re-serialised as PROV-JSONLD by the `prov` library (mentions of nested bundles rewritten as `specializationOf` + `prov:asInBundle`, see that block's notes), validated against `ogc.ogc-utils.prov.w3c-prov-jsonld` and read as RDF through its own context: the PROV-O graph here is the engine's, not this register's provenance view.
#### jsonld
```jsonld
{
  "@context": [
    {
      "wfprov": "http://purl.org/wf4ever/wfprov#",
      "wfdesc": "http://purl.org/wf4ever/wfdesc#",
      "cwlprov": "https://w3id.org/cwl/prov#",
      "foaf": "http://xmlns.com/foaf/0.1/",
      "schema": "http://schema.org/",
      "orcid": "https://orcid.org/",
      "id": "urn:uuid:",
      "data": "urn:hash::sha1:",
      "sha256": "nih:sha-256;",
      "researchobject": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/",
      "metadata": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/",
      "provenance": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/provenance/",
      "wf": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#",
      "input": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/primary-job.json#",
      "wf4ever": "http://purl.org/wf4ever/wf4ever#"
    },
    "https://openprovenance.org/prov-jsonld/context.jsonld"
  ],
  "@graph": [
    {
      "@type": "Agent",
      "@id": "id:1851e03b-b5dd-458e-b892-800c846451b6"
    },
    {
      "@type": "Agent",
      "@id": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "type": [
        "prov:SoftwareAgent",
        "wfprov:WorkflowEngine"
      ],
      "label": [
        {
          "@value": "cwltool 3.1.20260108082145"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:8bbef2fa-3721-4f50-b27c-1d641100a89f",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:887634a3-fcfa-4422-aaa1-8949fd8db10b",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0"
        }
      ]
    },
    {
      "@type": "Start",
      "activity": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "starter": "id:1851e03b-b5dd-458e-b892-800c846451b6",
      "time": "2026-09-23T22:09:36.483674"
    },
    {
      "@type": "Start",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "starter": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "time": "2026-09-23T22:09:36.483742"
    },
    {
      "@type": "Start",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:09:38.001367"
    },
    {
      "@type": "Start",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:11:25.771051"
    },
    {
      "@type": "Start",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:14.484903"
    },
    {
      "@type": "Start",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "starter": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:35.950035"
    },
    {
      "@type": "Activity",
      "@id": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "startTime": "2026-09-23T22:09:36.483701",
      "type": [
        "wfprov:WorkflowRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_crop"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_crop_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_normalized_difference"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_otsu"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_crop"
    },
    {
      "@type": "Association",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "agent": "id:8bbef2fa-3721-4f50-b27c-1d641100a89f"
    },
    {
      "@type": "Association",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_crop_2"
    },
    {
      "@type": "Association",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "agent": "id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6"
    },
    {
      "@type": "Association",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_normalized_difference"
    },
    {
      "@type": "Association",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "agent": "id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea"
    },
    {
      "@type": "Association",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_otsu"
    },
    {
      "@type": "Association",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "agent": "id:887634a3-fcfa-4422-aaa1-8949fd8db10b"
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "type": [
        "wfdesc:Workflow",
        "prov:Plan"
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "wfdesc:hasSubProcess": [
        {
          "@value": "wf:main/node_crop",
          "@type": "xsd:QName"
        }
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "wfdesc:hasSubProcess": [
        {
          "@value": "wf:main/node_normalized_difference",
          "@type": "xsd:QName"
        }
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "wfdesc:hasSubProcess": [
        {
          "@value": "wf:main/node_otsu",
          "@type": "xsd:QName"
        }
      ],
      "label": [
        {
          "@value": "Prospective provenance"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/node_crop",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/node_normalized_difference",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/node_otsu",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "-121.399,39.834,-120.74,40.472"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "-121.399,39.834,-120.74,40.472"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "-121.399,39.834,-120.74,40.472"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "green"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "green"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "nir"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "nir"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "EPSG:4326"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "EPSG:4326"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "EPSG:4326"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:69255dfb77442b710fb7caf4fe2c555a8a8ca404",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "crop_green.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "crop_green"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "crop_nir.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "crop_nir"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ea91fcdd6f24b5105718011ca77810e4b6763c09",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "norm_diff.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "norm_diff"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:8cb131413518c30be6ba485ea61764491444cde5",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "otsu.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "otsu"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tif"
        }
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "entity": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "time": "2026-09-23T22:09:37.997833",
      "role": [
        "wf:main/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "entity": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "time": "2026-09-23T22:09:37.998964",
      "role": [
        "wf:main/bands"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "entity": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "time": "2026-09-23T22:09:37.999442",
      "role": [
        "wf:main/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "time": "2026-09-23T22:09:38.074291",
      "role": [
        "wf:main/node_crop/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c",
      "time": "2026-09-23T22:09:38.074835",
      "role": [
        "wf:main/node_crop/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "time": "2026-09-23T22:09:38.075291",
      "role": [
        "wf:main/node_crop/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "entity": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "time": "2026-09-23T22:09:38.075873",
      "role": [
        "wf:main/node_crop/item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "time": "2026-09-23T22:11:25.786582",
      "role": [
        "wf:main/node_crop_2/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd",
      "time": "2026-09-23T22:11:25.787372",
      "role": [
        "wf:main/node_crop_2/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "time": "2026-09-23T22:11:25.787927",
      "role": [
        "wf:main/node_crop_2/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "entity": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2",
      "time": "2026-09-23T22:11:25.788461",
      "role": [
        "wf:main/node_crop_2/item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "entity": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "time": "2026-09-23T22:14:14.589864",
      "role": [
        "wf:main/node_normalized_difference/rasters"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "entity": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "time": "2026-09-23T22:14:36.026698",
      "role": [
        "wf:main/node_otsu/raster"
      ]
    },
    {
      "@type": "Membership",
      "collection": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "entity": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c"
    },
    {
      "@type": "Membership",
      "collection": "id:1f7549f8-4403-44f2-a435-f95a32edb9de",
      "entity": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd"
    },
    {
      "@type": "Membership",
      "collection": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "entity": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e"
    },
    {
      "@type": "Membership",
      "collection": "id:eb53f504-eecb-4585-8e33-f7afdbbf816a",
      "entity": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e",
      "generalEntity": "data:69255dfb77442b710fb7caf4fe2c555a8a8ca404"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f",
      "generalEntity": "data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "generalEntity": "data:ea91fcdd6f24b5105718011ca77810e4b6763c09"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "generalEntity": "data:8cb131413518c30be6ba485ea61764491444cde5"
    },
    {
      "@type": "Generation",
      "entity": "id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "time": "2026-09-23T22:11:25.695199",
      "role": [
        "wf:main/node_crop/cropped"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:42580139-e758-4dbe-8ca8-7a114f7abf7f",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "time": "2026-09-23T22:14:14.382819",
      "role": [
        "wf:main/node_crop_2/cropped"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:740c294a-a5f9-49be-b685-970f3eec0666",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "time": "2026-09-23T22:14:35.757198",
      "role": [
        "wf:main/node_normalized_difference/ndwi"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "time": "2026-09-23T22:14:43.705762",
      "role": [
        "wf:main/node_otsu/binary_mask_item"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:43.709003",
      "role": [
        "wf:main/workflow%20node_water_bodies/detected_water_body"
      ]
    },
    {
      "@type": "End",
      "activity": "id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:11:25.695175"
    },
    {
      "@type": "End",
      "activity": "id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:14.382774"
    },
    {
      "@type": "End",
      "activity": "id:f960d24b-dcbf-4c16-88ce-ad7029487e59",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:35.757176"
    },
    {
      "@type": "End",
      "activity": "id:6d7920a6-ee35-4701-88be-68838b9ba10b",
      "ender": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "time": "2026-09-23T22:14:43.705752"
    },
    {
      "@type": "End",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "ender": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "time": "2026-09-23T22:14:43.709126"
    }
  ]
}
```

#### ttl
```ttl
@prefix cwlprov: <https://w3id.org/cwl/prov#> .
@prefix data: <urn:hash::sha1:> .
@prefix id: <urn:uuid:> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix provext: <https://openprovenance.org/ns/provext#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix wf: <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#> .
@prefix wf4ever: <http://purl.org/wf4ever/wf4ever#> .
@prefix wfdesc: <http://purl.org/wf4ever/wfdesc#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

id:5fa19808-d14c-4c01-8bd1-05a7a8845019 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:6d7920a6-ee35-4701-88be-68838b9ba10b ;
            prov:atTime "2026-09-23T22:14:43.705762"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu/binary_mask_item> ],
        [ a prov:Generation ;
            prov:activity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ;
            prov:atTime "2026-09-23T22:14:43.709003"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/workflow%20node_water_bodies/detected_water_body> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8cb131413518c30be6ba485ea61764491444cde5 ] ;
    cwlprov:basename "otsu.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "otsu" .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/node_crop"^^xsd:QName,
        "wf:main/node_normalized_difference"^^xsd:QName,
        "wf:main/node_otsu"^^xsd:QName .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f a wfprov:Artifact,
        prov:Entity .

data:69255dfb77442b710fb7caf4fe2c555a8a8ca404 a wfprov:Artifact,
        prov:Entity .

data:8cb131413518c30be6ba485ea61764491444cde5 a wfprov:Artifact,
        prov:Entity .

data:ea91fcdd6f24b5105718011ca77810e4b6763c09 a wfprov:Artifact,
        prov:Entity .

id:1851e03b-b5dd-458e-b892-800c846451b6 a prov:Agent .

id:1f7549f8-4403-44f2-a435-f95a32edb9de a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:ba936cb0e062bea4078e8b56371ca8fe054093dd ],
        [ a provext:Membership ;
            provext:member data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c ] .

id:42580139-e758-4dbe-8ca8-7a114f7abf7f a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5 ;
            prov:atTime "2026-09-23T22:14:14.382819"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/cropped> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:2d6eb0dc351bd77d3f5b06672ed012ef5dec508f ] ;
    cwlprov:basename "crop_nir.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "crop_nir" .

id:6d7920a6-ee35-4701-88be-68838b9ba10b a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_otsu" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu> ],
        [ a prov:Association ;
            prov:agent id:887634a3-fcfa-4422-aaa1-8949fd8db10b ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:43.705752"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:14:35.950035"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:14:36.026698"^^xsd:dateTime ;
            prov:entity id:740c294a-a5f9-49be-b685-970f3eec0666 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_otsu/raster> ] .

id:740c294a-a5f9-49be-b685-970f3eec0666 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f960d24b-dcbf-4c16-88ce-ad7029487e59 ;
            prov:atTime "2026-09-23T22:14:35.757198"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference/ndwi> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:ea91fcdd6f24b5105718011ca77810e4b6763c09 ] ;
    cwlprov:basename "norm_diff.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "norm_diff" .

id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/norm_diff:1.5.0" .

id:887634a3-fcfa-4422-aaa1-8949fd8db10b a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0" .

id:8bbef2fa-3721-4f50-b27c-1d641100a89f a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" .

id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_crop" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:8bbef2fa-3721-4f50-b27c-1d641100a89f ],
        [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:11:25.695175"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:38.001367"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.075873"^^xsd:dateTime ;
            prov:entity data:5f0002427ab880579cf6a5a5c704bd399f3310f2 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.075291"^^xsd:dateTime ;
            prov:entity data:9d1fba832b03655b5b73ff964bc74d4543bf904a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.074291"^^xsd:dateTime ;
            prov:entity data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:38.074835"^^xsd:dateTime ;
            prov:entity data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/band> ] .

id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:8d6db404-8e9b-4740-bc17-6a2fab7c0c32 ;
            prov:atTime "2026-09-23T22:11:25.695199"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop/cropped> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:69255dfb77442b710fb7caf4fe2c555a8a8ca404 ] ;
    cwlprov:basename "crop_green.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "crop_green" .

id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0" .

id:eb53f504-eecb-4585-8e33-f7afdbbf816a a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:42580139-e758-4dbe-8ca8-7a114f7abf7f ],
        [ a provext:Membership ;
            provext:member id:b3b5dbf6-efbd-48f2-ba85-a9937bb49c7e ] .

id:f47bdfb0-199b-4f9a-93c9-1bc6e9427cc5 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_crop_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:c2b78598-db7e-4ab3-89eb-621c7b5c9bd6 ],
        [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:14.382774"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:11:25.771051"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.787927"^^xsd:dateTime ;
            prov:entity data:9d1fba832b03655b5b73ff964bc74d4543bf904a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.786582"^^xsd:dateTime ;
            prov:entity data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.787372"^^xsd:dateTime ;
            prov:entity data:ba936cb0e062bea4078e8b56371ca8fe054093dd ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:11:25.788461"^^xsd:dateTime ;
            prov:entity data:5f0002427ab880579cf6a5a5c704bd399f3310f2 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_crop_2/item> ] .

id:f960d24b-dcbf-4c16-88ce-ad7029487e59 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_normalized_difference" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference> ],
        [ a prov:Association ;
            prov:agent id:87ca5fb7-8991-4f4e-b107-8b30f9be5eea ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:35.757176"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:14:14.484903"^^xsd:dateTime ;
            prov:hadActivity id:006f10ba-bce7-4602-bc25-46f0ca2c5724 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:14:14.589864"^^xsd:dateTime ;
            prov:entity id:eb53f504-eecb-4585-8e33-f7afdbbf816a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_normalized_difference/rasters> ] .

data:5f0002427ab880579cf6a5a5c704bd399f3310f2 a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A" .

data:ba936cb0e062bea4078e8b56371ca8fe054093dd a wfprov:Artifact,
        prov:Entity ;
    prov:value "nir" .

data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c a wfprov:Artifact,
        prov:Entity ;
    prov:value "green" .

data:9d1fba832b03655b5b73ff964bc74d4543bf904a a wfprov:Artifact,
        prov:Entity ;
    prov:value "EPSG:4326" .

data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad a wfprov:Artifact,
        prov:Entity ;
    prov:value "-121.399,39.834,-120.74,40.472" .

id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:36.483674"^^xsd:dateTime ;
            prov:hadActivity id:1851e03b-b5dd-458e-b892-800c846451b6 ] .

id:006f10ba-bce7-4602-bc25-46f0ca2c5724 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:14:43.709126"^^xsd:dateTime ;
            prov:hadActivity id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:36.483742"^^xsd:dateTime ;
            prov:hadActivity id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.998964"^^xsd:dateTime ;
            prov:entity id:1f7549f8-4403-44f2-a435-f95a32edb9de ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/bands> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.999442"^^xsd:dateTime ;
            prov:entity data:9d1fba832b03655b5b73ff964bc74d4543bf904a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.997833"^^xsd:dateTime ;
            prov:entity data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/aoi> ] ;
    prov:startedAtTime "2026-09-23T22:09:36.483701"^^xsd:dateTime .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `norm_diff`
  (CWL CommandLineTool). Pins the process id and the input/output names; the input/output
  schemas are those derived from the CWL.
allOf:
- $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/process/schema.yaml
- $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/v2/schemas/staticIndicator/schema.yaml
- type: object
  required:
  - id
  - version
  - inputs
  - outputs
  properties:
    id:
      const: norm_diff
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - rasters
      propertyNames:
        enum:
        - rasters
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - ndwi
      propertyNames:
        enum:
        - ndwi
      x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
$defs:
  rawProcessDescription:
    $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/process/schema.yaml
  applicationPackage:
    $ref: https://geolabs.github.io/bblock-ogcapi-processes-part2/build/annotated/api/processes/v2/schemas/ogcapppkg/schema.yaml
  provenance:
    $ref: https://geolabs.github.io/bblocks-generic-provenance-profile/build/annotated/bbr/provenance/provenance/schema.yaml
  processTypeEntry:
    $ref: https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/process-type/schema.yaml
  w3cProvJsonLd:
    $ref: https://ogcincubator.github.io/bblocks-prov-jsonld-alt/build/annotated/ogc-utils/prov/w3c-prov-jsonld/schema.yaml
  execute:
    description: Execute request for this process. Built on the processDescription
      input schemas and on ogc.api.processes.v1.schemas.link / qualifiedInputValue,
      because ogc.api.processes.v1.schemas.execute rejects plain strings and numbers
      (upstream issue U-01).
    type: object
    required:
    - inputs
    properties:
      inputs:
        type: object
        required:
        - rasters
        propertyNames:
          enum:
          - rasters
        additionalProperties:
          anyOf:
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/link/schema.yaml
          - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/qualifiedInputValue/schema.yaml
          - type:
            - string
            - number
            - integer
            - boolean
            - array
            - object
        x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
        x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
      outputs:
        type: object
        propertyNames:
          enum:
          - ndwi
        x-jsonld-id: https://w3id.org/ogc/api/processes/outputs
        x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/output/
      response:
        enum:
        - raw
        - document
        x-jsonld-id: https://w3id.org/ogc/api/processes/response
  results:
    description: Results document (response=document) for this process (see U-01).
    type: object
    propertyNames:
      enum:
      - ndwi
    additionalProperties:
      anyOf:
      - $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/link/schema.yaml
      - type: array
        items:
          $ref: https://ogcincubator.github.io/bblocks-ogcapi-processes/build/annotated/api/processes/v1/schemas/link/schema.yaml
      - type:
        - string
        - number
        - integer
        - boolean
        - array
        - object
  processRun:
    $ref: https://ogcincubator.github.io/bblocks-wf4ever/build/annotated/bbr/wf4ever/wfprov/ProcessRun/schema.yaml
x-jsonld-extra-terms:
  type: '@type'
  ProcessRun: http://purl.org/wf4ever/wfprov#ProcessRun
  WorkflowRun: http://purl.org/wf4ever/wfprov#WorkflowRun
  WorkflowEngine: http://purl.org/wf4ever/wfprov#WorkflowEngine
  Artifact: http://purl.org/wf4ever/wfprov#Artifact
  ProcessType: http://www.w3.org/2004/02/skos/core#Concept
  title: http://purl.org/dc/terms/title
  description: http://purl.org/dc/terms/description
  keywords: http://purl.org/dc/terms/subject
  version: https://geolabs.github.io/bblocks-process-profiles/def/version
  mutable: https://w3id.org/ogc/api/processes/mutable
  jobControlOptions: https://w3id.org/ogc/api/processes/jobControlOptions
  outputTransmission: https://w3id.org/ogc/api/processes/outputTransmission
  metadata: https://w3id.org/ogc/api/processes/metadata
  role:
    x-jsonld-id: https://w3id.org/ogc/api/processes/role
    x-jsonld-type: '@id'
  links:
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    x-jsonld-context:
      href:
        '@id': http://www.w3.org/ns/oa#hasTarget
        '@type': '@id'
      rel:
        '@id': http://www.iana.org/assignments/relation
        '@type': '@id'
        '@context':
          '@base': http://www.iana.org/assignments/relation/
      type: http://purl.org/dc/terms/type
      title: http://www.w3.org/2000/01/rdf-schema#label
  response: https://w3id.org/ogc/api/processes/response
  executionUnit: https://w3id.org/ogc/api/processes/executionUnit
  processDescription: https://geolabs.github.io/bblocks-process-profiles/def/processDescription
  result: https://geolabs.github.io/bblocks-process-profiles/def/result
  engine: https://geolabs.github.io/bblocks-process-profiles/def/engine
  run: https://geolabs.github.io/bblocks-process-profiles/def/run
  provType:
    x-jsonld-id: '@type'
    x-jsonld-type: '@vocab'
  provName: http://www.w3.org/2000/01/rdf-schema#label
  activityType:
    x-jsonld-id: '@type'
    x-jsonld-type: '@id'
  entityType:
    x-jsonld-id: '@type'
    x-jsonld-type: '@id'
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  wasAssociatedWith:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  qualifiedAssociation: http://www.w3.org/ns/prov#qualifiedAssociation
  agent:
    x-jsonld-id: http://www.w3.org/ns/prov#agent
    x-jsonld-type: '@id'
  hadPlan:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPlan
    x-jsonld-type: '@id'
  startedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#startedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  endedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#endedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  value: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
  describedByProcess:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#describedByProcess
    x-jsonld-type: '@id'
  describedByWorkflow:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#describedByWorkflow
    x-jsonld-type: '@id'
  usedInput:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#usedInput
    x-jsonld-type: '@id'
  wasEnactedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAssociatedWith
    x-jsonld-type: '@id'
  wasPartOfWorkflowRun:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#wasPartOfWorkflowRun
    x-jsonld-type: '@id'
  hadSubProcessRun:
    x-jsonld-id: http://purl.org/wf4ever/wfprov#hadSubProcessRun
    x-jsonld-type: '@id'
  wasOutputFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#generated
    x-jsonld-type: '@id'
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  definition: http://www.w3.org/2004/02/skos/core#definition
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  status: https://geolabs.github.io/bblocks-process-profiles/def/status
  phase:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
  profile: https://geolabs.github.io/bblocks-process-profiles/def/profile
  source: https://geolabs.github.io/bblocks-process-profiles/def/source
  cwl:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/cwl
    x-jsonld-type: '@id'
  cwlClass: https://geolabs.github.io/bblocks-process-profiles/def/cwlClass
  cwlId: https://geolabs.github.io/bblocks-process-profiles/def/cwlId
  provenanceClass:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/provenanceClass
    x-jsonld-type: '@id'
  cctDependencies: https://geolabs.github.io/bblocks-process-profiles/def/cctDependency
  candidateCctDependencies: https://geolabs.github.io/bblocks-process-profiles/def/candidateCctDependency
  hasStep:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/hasStep
    x-jsonld-type: '@id'
  exactMatch:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#exactMatch
    x-jsonld-type: '@id'
  closeMatch:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#closeMatch
    x-jsonld-type: '@id'
  relatedMatch:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#relatedMatch
    x-jsonld-type: '@id'
  openeoEquivalence: https://geolabs.github.io/bblocks-process-profiles/def/openeoEquivalence
  level: https://geolabs.github.io/bblocks-process-profiles/def/equivalenceLevel
  rationale: https://geolabs.github.io/bblocks-process-profiles/def/rationale
  decomposition:
    x-jsonld-id: https://geolabs.github.io/bblocks-process-profiles/def/decomposition
    x-jsonld-container: '@list'
  stage: https://geolabs.github.io/bblocks-process-profiles/def/stage
  openeo: https://geolabs.github.io/bblocks-process-profiles/def/openeo
  note: http://www.w3.org/2004/02/skos/core#note
x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/
x-jsonld-prefixes:
  wfprov: http://purl.org/wf4ever/wfprov#
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
  pp: https://geolabs.github.io/bblocks-process-profiles/def/
  proc: https://w3id.org/ogc/api/processes/
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  oa: http://www.w3.org/ns/oa#
  prov: http://www.w3.org/ns/prov#
  xsd: http://www.w3.org/2001/XMLSchema#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#

```

Links to the schema:

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "inputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-process-profiles/def/input/",
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "keywords": "proc:keywords",
        "type": "proc:type"
      },
      "@id": "proc:inputs"
    },
    "outputs": {
      "@context": {
        "@vocab": "https://geolabs.github.io/bblocks-process-profiles/def/output/",
        "schema": {
          "@context": {
            "@vocab": "https://w3id.org/ogc/api/schema/"
          },
          "@id": "proc:schema"
        },
        "keywords": "proc:keywords",
        "type": "proc:type"
      },
      "@id": "proc:outputs"
    },
    "id": "@id",
    "type": "@type",
    "ProcessRun": "wfprov:ProcessRun",
    "WorkflowRun": "wfprov:WorkflowRun",
    "WorkflowEngine": "wfprov:WorkflowEngine",
    "Artifact": "wfprov:Artifact",
    "ProcessType": "skos:Concept",
    "title": "dct:title",
    "description": "dct:description",
    "keywords": "dct:subject",
    "version": "pp:version",
    "mutable": "proc:mutable",
    "jobControlOptions": "proc:jobControlOptions",
    "outputTransmission": "proc:outputTransmission",
    "metadata": "proc:metadata",
    "role": {
      "@id": "proc:role",
      "@type": "@id"
    },
    "links": {
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": {
          "@id": "oa:hasTarget",
          "@type": "@id"
        },
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "title": "rdfs:label"
      }
    },
    "response": "proc:response",
    "executionUnit": "proc:executionUnit",
    "processDescription": "pp:processDescription",
    "result": "pp:result",
    "engine": "pp:engine",
    "run": "pp:run",
    "provType": {
      "@id": "@type",
      "@type": "@vocab"
    },
    "provName": "rdfs:label",
    "activityType": {
      "@id": "@type",
      "@type": "@id"
    },
    "entityType": {
      "@id": "@type",
      "@type": "@id"
    },
    "used": {
      "@id": "prov:used",
      "@type": "@id"
    },
    "wasAssociatedWith": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasGeneratedBy": {
      "@id": "prov:wasGeneratedBy",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "prov:wasDerivedFrom",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@id": "prov:wasAttributedTo",
      "@type": "@id"
    },
    "qualifiedAssociation": "prov:qualifiedAssociation",
    "agent": {
      "@id": "prov:agent",
      "@type": "@id"
    },
    "hadPlan": {
      "@id": "prov:hadPlan",
      "@type": "@id"
    },
    "startedAtTime": {
      "@id": "prov:startedAtTime",
      "@type": "xsd:dateTime"
    },
    "endedAtTime": {
      "@id": "prov:endedAtTime",
      "@type": "xsd:dateTime"
    },
    "value": "rdf:value",
    "describedByProcess": {
      "@id": "wfprov:describedByProcess",
      "@type": "@id"
    },
    "describedByWorkflow": {
      "@id": "wfprov:describedByWorkflow",
      "@type": "@id"
    },
    "usedInput": {
      "@id": "wfprov:usedInput",
      "@type": "@id"
    },
    "wasEnactedBy": {
      "@id": "prov:wasAssociatedWith",
      "@type": "@id"
    },
    "wasPartOfWorkflowRun": {
      "@id": "wfprov:wasPartOfWorkflowRun",
      "@type": "@id"
    },
    "hadSubProcessRun": {
      "@id": "wfprov:hadSubProcessRun",
      "@type": "@id"
    },
    "wasOutputFrom": {
      "@id": "prov:generated",
      "@type": "@id"
    },
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
    "source": "pp:source",
    "cwl": {
      "@id": "pp:cwl",
      "@type": "@id"
    },
    "cwlClass": "pp:cwlClass",
    "cwlId": "pp:cwlId",
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
    "openeoEquivalence": "pp:openeoEquivalence",
    "level": "pp:equivalenceLevel",
    "rationale": "pp:rationale",
    "decomposition": {
      "@id": "pp:decomposition",
      "@container": "@list"
    },
    "stage": "pp:stage",
    "openeo": "pp:openeo",
    "note": "skos:note",
    "nullable": "proc:nullable",
    "$ref": {
      "@id": "proc:ref",
      "@type": "@id"
    },
    "default": {
      "@id": "proc:default",
      "@type": "@json"
    },
    "enum": {
      "@id": "proc:enum",
      "@container": "@set"
    },
    "minOccurs": "proc:minOccurs",
    "maxOccurs": "proc:maxOccurs",
    "dct": "http://purl.org/dc/terms/",
    "proc": "https://w3id.org/ogc/api/processes/",
    "wfprov": "http://purl.org/wf4ever/wfprov#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "pp": "https://geolabs.github.io/bblocks-process-profiles/def/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/norm-diff/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/water-bodies/norm-diff`

