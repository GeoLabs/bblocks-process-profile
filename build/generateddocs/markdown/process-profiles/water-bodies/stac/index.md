
# Process profile: stac (Schema)

`ospd.process-profiles.water-bodies.stac` *v0.1*

OGC API - Processes profile of the CWL CommandLineTool `stac` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`stac`** (CommandLineTool, W3 Water Bodies).

> Assemble a STAC catalog of detected water bodies

## Source

- CWL: [stac.cwl](https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl) (pinned commit `f472585`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.stac`
- Used by: `ospd.process-profiles.water-bodies.water-bodies`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `item` | {"type": "array", "items": "string", "inputBinding": {"prefix": "--input-item"}} | `stac_catalog` | Directory |
| `rasters` | {"type": "array", "items": "File", "inputBinding": {"prefix": "--water-body"}} |  |  |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0`.
Pairs each `item` (a STAC item URL, in order) with the matching `rasters` entry (in order,
the same positional-array coupling as `norm-diff`) and writes a root `catalog.json` plus one
per-item sub-folder holding that item's own STAC JSON and its water-body raster asset.

**CWL specifics.** Output `stac_catalog` is a `Directory`, mapped by the transform to a STAC
**Collection**; the run record shows the tool itself writes a STAC **Catalog**
(`catalog.json`, `"type": "Catalog"`) with one Item per input identifier: corrected (M-05),
the same gap as `kindgrove.mangrove` / `kindgrove.mangrove-workflow`.

**Provenance.** Two array inputs coupled positionally (GP-3: neither is itself a file-typed
entity that could carry `wasDerivedFrom` to the water-body rasters it packages); the output
directory's members are the register's own `execution` bundle's per-file artefacts (GP-10).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-05 outputs.stac_catalog: the Directory output is a STAC Catalog written by the tool itself (run record: `catalog.json` with one Item), not the Collection assumed by the transform

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (ogc-eo-application-package-hands-on f472585 `water-bodies/app-pkg-multiple/water-bodies.cwl`, one CWL file per step), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_stac` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Writes the final rasters to a self-describing output collection; save_result's STAC-catalog output option is the closest openEO equivalent to hand-assembling one.

- `closeMatch`: `ogc.openeo.processes.cubes.save_result`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL CommandLineTool is referenced, not copied: <https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl>.

### processDescription
OGC API - Processes processDescription derived from the CWL (manually corrected, see description).
#### json
```json
{
  "id": "stac",
  "version": "1.4.1",
  "title": "stac",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "stac"
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
    "item": {
      "title": "item",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
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
    "stac_catalog": {
      "title": "stac_catalog",
      "description": "",
      "schema": {
        "type": "object",
        "required": [
          "type",
          "stac_version",
          "id",
          "description",
          "links"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "Catalog"
            ]
          },
          "stac_version": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "links": {
            "type": "array"
          }
        },
        "format": "stac-catalog"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "id": "stac",
  "version": "1.4.1",
  "title": "stac",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "stac"
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
    "item": {
      "title": "item",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
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
    "stac_catalog": {
      "title": "stac_catalog",
      "description": "",
      "schema": {
        "type": "object",
        "required": [
          "type",
          "stac_version",
          "id",
          "description",
          "links"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "Catalog"
            ]
          },
          "stac_version": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "links": {
            "type": "array"
          }
        },
        "format": "stac-catalog"
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
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/stac> dcterms:description "Process converted from CWL" ;
    dcterms:title "stac" ;
    pp:version "1.4.1" ;
    proc:inputs [ ns2:item [ dcterms:description "" ;
                    dcterms:title "item" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ] ] ] ;
            ns2:rasters [ dcterms:description "" ;
                    dcterms:title "rasters" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentMediaType "application/octet-stream" ] ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "Process converted from CWL" ;
            proc:role schema:description ],
        [ rdf:value "1.4.1" ;
            proc:role schema:softwareVersion ],
        [ rdf:value "stac" ;
            proc:role schema:name ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:stac_catalog [ dcterms:description "" ;
                    dcterms:title "stac_catalog" ;
                    proc:schema [ proc:type "object" ;
                            ns1:format "stac-catalog" ;
                            ns1:properties [ dcterms:description [ proc:type "string" ] ;
                                    dcterms:title [ proc:type "string" ] ;
                                    rdfs:seeAlso [ dcterms:type "array" ] ;
                                    proc:type [ proc:enum "Catalog" ;
                                            proc:type "string" ] ;
                                    ns1:stac_version [ proc:type "string" ] ] ;
                            ns1:required "description",
                                "id",
                                "links",
                                "stac_version",
                                "type" ] ] ] .


```


### Raw cwl-to-ogcprocess output
Unmodified output of the `eoap.cct.cwl-to-ogcprocess` jq transform.
#### json
```json
{
  "id": "stac",
  "version": "1.4.1",
  "title": "stac",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "stac"
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
    "item": {
      "title": "item",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
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
    "stac_catalog": {
      "title": "stac_catalog",
      "description": "",
      "schema": {
        "type": "object",
        "required": [
          "type",
          "stac_version",
          "id",
          "description",
          "license",
          "extent",
          "links"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "Collection"
            ]
          },
          "stac_version": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "license": {
            "type": "string"
          },
          "extent": {
            "type": "object"
          },
          "links": {
            "type": "array"
          },
          "assets": {
            "type": "object"
          }
        },
        "format": "stac-collection"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "id": "stac",
  "version": "1.4.1",
  "title": "stac",
  "description": "Process converted from CWL",
  "mutable": true,
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "stac"
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
    "item": {
      "title": "item",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
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
    "stac_catalog": {
      "title": "stac_catalog",
      "description": "",
      "schema": {
        "type": "object",
        "required": [
          "type",
          "stac_version",
          "id",
          "description",
          "license",
          "extent",
          "links"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "Collection"
            ]
          },
          "stac_version": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "license": {
            "type": "string"
          },
          "extent": {
            "type": "object"
          },
          "links": {
            "type": "array"
          },
          "assets": {
            "type": "object"
          }
        },
        "format": "stac-collection"
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
@prefix ns1: <https://w3id.org/ogc/api/schema/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/stac> dcterms:description "Process converted from CWL" ;
    dcterms:title "stac" ;
    pp:version "1.4.1" ;
    proc:inputs [ ns3:item [ dcterms:description "" ;
                    dcterms:title "item" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ] ] ] ;
            ns3:rasters [ dcterms:description "" ;
                    dcterms:title "rasters" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentMediaType "application/octet-stream" ] ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "stac" ;
            proc:role schema:name ],
        [ rdf:value "1.4.1" ;
            proc:role schema:softwareVersion ],
        [ rdf:value "Process converted from CWL" ;
            proc:role schema:description ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns2:stac_catalog [ dcterms:description "" ;
                    dcterms:title "stac_catalog" ;
                    proc:schema [ proc:type "object" ;
                            ns1:format "stac-collection" ;
                            ns1:properties [ dcterms:description [ proc:type "string" ] ;
                                    dcterms:title [ proc:type "string" ] ;
                                    rdfs:seeAlso [ dcterms:type "array" ] ;
                                    proc:type [ proc:enum "Collection" ;
                                            proc:type "string" ] ;
                                    ns1:assets [ proc:type "object" ] ;
                                    ns1:extent [ proc:type "object" ] ;
                                    ns1:license [ proc:type "string" ] ;
                                    ns1:stac_version [ proc:type "string" ] ] ;
                            ns1:required "description",
                                "extent",
                                "id",
                                "license",
                                "links",
                                "stac_version",
                                "type" ] ] ] .


```


### OGC Application Package (deploy)
Part 2 deploy body: the execution unit is a link to the pinned CWL.
#### json
```json
{
  "processDescription": {
    "process": {
      "id": "stac",
      "version": "1.4.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "processDescription": {
    "process": {
      "id": "stac",
      "version": "1.4.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/stac> pp:version "1.4.1" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/stac> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/raw/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl" ;
            pp:rel "http://www.opengis.net/def/rel/ogc/1.0/executionUnit" ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "item": [
      "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A",
      "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A"
    ],
    "rasters": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2B_10TFK_20210713_0_L2A/otsu.tif",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_10TFK_20220524_0_L2A/otsu.tif",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "inputs": {
    "item": [
      "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A",
      "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A"
    ],
    "rasters": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2B_10TFK_20210713_0_L2A/otsu.tif",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_10TFK_20220524_0_L2A/otsu.tif",
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

[] proc:inputs [ ns1:item "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A",
                "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A" ;
            ns1:rasters [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_10TFK_20220524_0_L2A/otsu.tif" ;
                    proc:type "image/tiff; application=geotiff" ],
                [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2B_10TFK_20210713_0_L2A/otsu.tif" ;
                    proc:type "image/tiff; application=geotiff" ] ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "stac_catalog": {
    "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-stac-0001/results/catalog.json",
    "type": "application/json"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "stac_catalog": {
    "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-stac-0001/results/catalog.json",
    "type": "application/json"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:stac_catalog [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/json> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/water-bodies-stac-0001/results/catalog.json" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:water-bodies:stac",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac",
    "startedAtTime": "2026-09-23T20:17:40Z",
    "used": [
      "urn:example:entity:stac:in:item",
      "urn:example:entity:stac:in:rasters"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145",
      "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/stac"
      }
    ],
    "endedAtTime": "2026-09-23T20:17:45Z"
  },
  {
    "id": "urn:example:entity:stac:in:item",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/stac#inputs/item",
    "value": [
      "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A",
      "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A"
    ]
  },
  {
    "id": "urn:example:entity:stac:in:rasters",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/stac#inputs/rasters",
    "value": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2B_10TFK_20210713_0_L2A/otsu.tif",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_10TFK_20220524_0_L2A/otsu.tif",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  {
    "id": "urn:example:entity:stac:out:stac_catalog",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/stac#outputs/stac_catalog",
    "wasGeneratedBy": "urn:example:run:water-bodies:stac",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-stac-0001/results/catalog.json",
        "rel": "item",
        "type": "application/json"
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
    "id": "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0",
    "provType": "prov:SoftwareAgent",
    "name": "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0"
  }
]

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:water-bodies:stac",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac",
      "startedAtTime": "2026-09-23T20:17:40Z",
      "used": [
        "urn:example:entity:stac:in:item",
        "urn:example:entity:stac:in:rasters"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145",
        "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/stac"
        }
      ],
      "endedAtTime": "2026-09-23T20:17:45Z"
    },
    {
      "id": "urn:example:entity:stac:in:item",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/stac#inputs/item",
      "value": [
        "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A",
        "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A"
      ]
    },
    {
      "id": "urn:example:entity:stac:in:rasters",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/stac#inputs/rasters",
      "value": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2B_10TFK_20210713_0_L2A/otsu.tif",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_10TFK_20220524_0_L2A/otsu.tif",
          "type": "image/tiff; application=geotiff"
        }
      ]
    },
    {
      "id": "urn:example:entity:stac:out:stac_catalog",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/stac#outputs/stac_catalog",
      "wasGeneratedBy": "urn:example:run:water-bodies:stac",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/water-bodies-stac-0001/results/catalog.json",
          "rel": "item",
          "type": "application/json"
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
      "id": "urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0",
      "provType": "prov:SoftwareAgent",
      "name": "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0"
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

<urn:example:entity:stac:out:stac_catalog> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/stac#outputs/stac_catalog> ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/water-bodies-stac-0001/results/catalog.json> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:water-bodies:stac> .

<urn:example:entity:stac:in:item> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/stac#inputs/item> ;
    rdf:value "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A",
        "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A" .

<urn:example:entity:stac:in:rasters> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/stac#inputs/rasters> ;
    rdf:value [ pp:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_10TFK_20220524_0_L2A/otsu.tif" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2B_10TFK_20210713_0_L2A/otsu.tif" ] .

<urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0> a prov:SoftwareAgent ;
    pp:name "container image ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0" .

<urn:example:run:water-bodies:stac> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac> ;
    prov:endedAtTime "2026-09-23T20:17:45+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/stac> ] ;
    prov:startedAtTime "2026-09-23T20:17:40+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:stac:in:item>,
        <urn:example:entity:stac:in:rasters> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145>,
        <urn:example:image:ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0> .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Process run (wfprov:ProcessRun, gap GP-1)
#### json
```json
{
  "id": "urn:example:run:water-bodies:stac",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/stac",
  "usedInput": [
    {
      "id": "urn:example:entity:stac:in:item"
    },
    {
      "id": "urn:example:entity:stac:in:rasters"
    }
  ],
  "startedAtTime": "2026-09-23T20:17:40Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:water-bodies:water-bodies"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "id": "urn:example:run:water-bodies:stac",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/stac",
  "usedInput": [
    {
      "id": "urn:example:entity:stac:in:item"
    },
    {
      "id": "urn:example:entity:stac:in:rasters"
    }
  ],
  "startedAtTime": "2026-09-23T20:17:40Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:water-bodies:water-bodies"
}
```

#### ttl
```ttl
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:run:water-bodies:stac> a wfprov:ProcessRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac> ;
    wfprov:describedByProcess <https://ospd.example.org/ogc-api/processes/stac> ;
    wfprov:usedInput <urn:example:entity:stac:in:item>,
        <urn:example:entity:stac:in:rasters> ;
    wfprov:wasPartOfWorkflowRun <urn:example:run:water-bodies:water-bodies> ;
    prov:startedAtTime "2026-09-23T20:17:40+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac",
  "type": "ProcessType",
  "prefLabel": "Assemble a STAC catalog of detected water bodies",
  "definition": "Writes a STAC Catalog with one Item per input identifier, each carrying the corresponding water-body raster as an asset.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.water-bodies.stac",
  "processDescription": {
    "id": "stac",
    "version": "1.4.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "stac",
    "license": "https://spdx.org/licenses/CC-BY-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.stac"
  ],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Writes the final rasters to a self-describing output collection; save_result's STAC-catalog output option is the closest openEO equivalent to hand-assembling one."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac",
  "type": "ProcessType",
  "prefLabel": "Assemble a STAC catalog of detected water bodies",
  "definition": "Writes a STAC Catalog with one Item per input identifier, each carrying the corresponding water-body raster as an asset.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.water-bodies.stac",
  "processDescription": {
    "id": "stac",
    "version": "1.4.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "stac",
    "license": "https://spdx.org/licenses/CC-BY-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.stac"
  ],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Writes the final rasters to a self-describing output collection; save_result's STAC-catalog output option is the closest openEO equivalent to hand-assembling one."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/stac> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result> ;
    skos:definition "Writes a STAC Catalog with one Item per input identifier, each carrying the corresponding water-body raster as an asset." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Assemble a STAC catalog of detected water bodies" ;
    pp:candidateCctDependency "eoap.cct.stac" ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "Writes the final rasters to a self-describing output collection; save_result's STAC-catalog output option is the closest openEO equivalent to hand-assembling one." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/stac> ;
    pp:profile "ospd.process-profiles.water-bodies.stac" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:source [ pp:cwl <https://github.com/GeoLabs/ogc-eo-application-package-hands-on/blob/f47258567ddf8efbc7c33fd1ec277e4f1b454883/water-bodies/app-pkg-multiple/stac.cwl> ;
            pp:cwlClass "CommandLineTool" ;
            pp:cwlId "stac" ;
            pp:license "https://spdx.org/licenses/CC-BY-SA-4.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/stac> pp:version "1.4.1" .


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
      "wf4ever": "http://purl.org/wf4ever/wf4ever#",
      "ro": "http://purl.org/wf4ever/ro#",
      "ore": "http://www.openarchives.org/ore/terms/"
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
      "@id": "id:d8353ab3-7279-484e-a461-b04ae4b52890",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0"
        }
      ]
    },
    {
      "@type": "Start",
      "activity": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "starter": "id:1851e03b-b5dd-458e-b892-800c846451b6",
      "time": "2026-09-23T22:09:35.483801"
    },
    {
      "@type": "Start",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "starter": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "time": "2026-09-23T22:09:35.483879"
    },
    {
      "@type": "Start",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "starter": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "time": "2026-09-23T22:09:37.996102"
    },
    {
      "@type": "Start",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "starter": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "time": "2026-09-23T22:14:43.790754"
    },
    {
      "@type": "Start",
      "activity": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "starter": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "time": "2026-09-23T22:17:40.502305"
    },
    {
      "@type": "Activity",
      "@id": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "startTime": "2026-09-23T22:09:35.483832",
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
      "@id": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/water-bodies/node_water_bodies"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "prov:has_provenance": [
        {
          "@value": "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.jsonld",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.nt",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.ttl",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.json",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.provn",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.xml",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/water-bodies/node_water_bodies"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "prov:has_provenance": [
        {
          "@value": "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.nt",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.xml",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.jsonld",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.ttl",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.json",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.provn",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/node_stac"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/water-bodies/node_water_bodies"
    },
    {
      "@type": "Association",
      "activity": "id:006f10ba-bce7-4602-bc25-46f0ca2c5724",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/water-bodies/node_water_bodies"
    },
    {
      "@type": "Association",
      "activity": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "agent": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "plan": "wf:main/node_stac"
    },
    {
      "@type": "Association",
      "activity": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "agent": "id:d8353ab3-7279-484e-a461-b04ae4b52890"
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
          "@value": "wf:main/node_stac",
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
          "@value": "wf:main/node_water_bodies",
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
      "@id": "wf:main/node_stac",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/node_water_bodies",
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
      "@id": "id:b6924a3c-a25c-4107-bdd7-2b5b2bff912e",
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
      "@id": "data:09dd884abf8f162fa6ed55f0e958ce9586b8bffd",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:09dd884abf8f162fa6ed55f0e958ce9586b8bffd",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:511850b1-b1bc-44cd-8316-bdd367fefd98",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:25ff238f-e08b-4dee-a1f9-485e90a02a52",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:8cb131413518c30be6ba485ea61764491444cde5"
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
      "@type": "Entity",
      "@id": "data:8a97a5260b1039d7f867c2f9ab8ee36a5cb5fbd4"
    },
    {
      "@type": "Entity",
      "@id": "data:8a97a5260b1039d7f867c2f9ab8ee36a5cb5fbd4",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e06b906c-ef24-4174-830c-4a184274216f",
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
      "@type": "Entity",
      "@id": "id:3d637621-61a3-4c53-8aaf-70daadac3593",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "type": [
        "ro:Folder",
        "wfprov:Artifact",
        "prov:Collection",
        "prov:Dictionary"
      ],
      "cwlprov:basename": [
        {
          "@value": "docker_tmpwngcerl4"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-afa01c29-85ed-418e-b3a4-99ff6f4b06cf.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:2d2f953e-2ade-4e61-9cd0-64f1866d2c1d",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:23bdb369-3e88-43b2-81e3-b9324f75e079",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:a9451218-986b-4920-9d23-62638b8aea56",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:7d9076f9-073d-4667-84e9-131fd7fda68c",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
      "type": [
        "ro:Folder",
        "wfprov:Artifact",
        "prov:Collection",
        "prov:Dictionary"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2B_10TFK_20210713_0_L2A"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:1aa0c641-ea02-485d-a14b-c5a0aa40154b",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:bbd82449-f35c-4d0e-a771-32af085fe0db",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "otsu.tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:bbd82449-f35c-4d0e-a771-32af085fe0db",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "otsu.tif"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e74c29702b96c01957579e7d11b35d835356376b",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:8a52cbfa-2822-476c-baed-680f3a070398",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2B_10TFK_20210713_0_L2A.json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:1aa0c641-ea02-485d-a14b-c5a0aa40154b",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "S2B_10TFK_20210713_0_L2A.json"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:8a52cbfa-2822-476c-baed-680f3a070398",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:23bdb369-3e88-43b2-81e3-b9324f75e079",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "S2B_10TFK_20210713_0_L2A"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:a234b13e2668a49acb831fdf87f3c1ead120dd41",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "catalog.json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:2d2f953e-2ade-4e61-9cd0-64f1866d2c1d",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "catalog.json"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
      "type": [
        "ro:Folder",
        "wfprov:Artifact",
        "prov:Collection",
        "prov:Dictionary"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_10TFK_20220524_0_L2A"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-df33a1dc-d46c-4154-9213-04cfb8cc55c4.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:0c932b2b-21cb-4d36-8eda-c9d07f86bf53",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:4c5ac9a5-8f70-4cc6-bb2f-89864afd51b9",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:471cf7c7-1a60-4c28-b3d0-904c5aa74707",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "otsu.tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:4c5ac9a5-8f70-4cc6-bb2f-89864afd51b9",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "otsu.tif"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:471cf7c7-1a60-4c28-b3d0-904c5aa74707",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:d6d2a88a822dadbc95c6d3381d6b0386e94a2148",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ac975c99-5d6d-476f-b3ab-750fd0ac460d",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_10TFK_20220524_0_L2A.json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0c932b2b-21cb-4d36-8eda-c9d07f86bf53",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "S2A_10TFK_20220524_0_L2A.json"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:ac975c99-5d6d-476f-b3ab-750fd0ac460d",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:7d9076f9-073d-4667-84e9-131fd7fda68c",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "S2A_10TFK_20220524_0_L2A"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1",
      "type": [
        "ro:Folder",
        "wfprov:Artifact",
        "prov:Collection",
        "prov:Dictionary"
      ],
      "cwlprov:basename": [
        {
          "@value": ".cache"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-a782f6a0-89d7-46ac-9c76-c6569903f8e1.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:3a1a053d-536c-4e6f-a7c6-7a9348502781",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248",
      "type": [
        "ro:Folder",
        "prov:Collection",
        "prov:Dictionary",
        "prov:EmptyDictionary",
        "wfprov:Artifact",
        "prov:EmptyCollection"
      ],
      "cwlprov:basename": [
        {
          "@value": "rosetta"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-76afd8f9-b8f8-4b00-88b9-5bbf50509248.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3a1a053d-536c-4e6f-a7c6-7a9348502781",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "rosetta"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a9451218-986b-4920-9d23-62638b8aea56",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": ".cache"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "entity": "data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad",
      "time": "2026-09-23T22:09:37.991132",
      "role": [
        "wf:main/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "entity": "id:b6924a3c-a25c-4107-bdd7-2b5b2bff912e",
      "time": "2026-09-23T22:09:37.992978",
      "role": [
        "wf:main/bands"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "entity": "data:9d1fba832b03655b5b73ff964bc74d4543bf904a",
      "time": "2026-09-23T22:09:37.993781",
      "role": [
        "wf:main/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "entity": "id:511850b1-b1bc-44cd-8316-bdd367fefd98",
      "time": "2026-09-23T22:09:37.995200",
      "role": [
        "wf:main/stac_items"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "entity": "id:25ff238f-e08b-4dee-a1f9-485e90a02a52",
      "time": "2026-09-23T22:17:40.581639",
      "role": [
        "wf:main/node_stac/item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "entity": "id:3d637621-61a3-4c53-8aaf-70daadac3593",
      "time": "2026-09-23T22:17:40.582084",
      "role": [
        "wf:main/node_stac/rasters"
      ]
    },
    {
      "@type": "Membership",
      "collection": "id:b6924a3c-a25c-4107-bdd7-2b5b2bff912e",
      "entity": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c"
    },
    {
      "@type": "Membership",
      "collection": "id:b6924a3c-a25c-4107-bdd7-2b5b2bff912e",
      "entity": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd"
    },
    {
      "@type": "Membership",
      "collection": "id:511850b1-b1bc-44cd-8316-bdd367fefd98",
      "entity": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2"
    },
    {
      "@type": "Membership",
      "collection": "id:511850b1-b1bc-44cd-8316-bdd367fefd98",
      "entity": "data:09dd884abf8f162fa6ed55f0e958ce9586b8bffd"
    },
    {
      "@type": "Membership",
      "collection": "id:25ff238f-e08b-4dee-a1f9-485e90a02a52",
      "entity": "data:5f0002427ab880579cf6a5a5c704bd399f3310f2"
    },
    {
      "@type": "Membership",
      "collection": "id:25ff238f-e08b-4dee-a1f9-485e90a02a52",
      "entity": "data:09dd884abf8f162fa6ed55f0e958ce9586b8bffd"
    },
    {
      "@type": "Membership",
      "collection": "id:3d637621-61a3-4c53-8aaf-70daadac3593",
      "entity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019"
    },
    {
      "@type": "Membership",
      "collection": "id:3d637621-61a3-4c53-8aaf-70daadac3593",
      "entity": "id:e06b906c-ef24-4174-830c-4a184274216f"
    },
    {
      "@type": "Membership",
      "collection": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
      "entity": "id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5"
    },
    {
      "@type": "Membership",
      "collection": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
      "entity": "id:8a52cbfa-2822-476c-baed-680f3a070398"
    },
    {
      "@type": "Membership",
      "collection": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "entity": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0"
    },
    {
      "@type": "Membership",
      "collection": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "entity": "id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313"
    },
    {
      "@type": "Membership",
      "collection": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
      "entity": "id:471cf7c7-1a60-4c28-b3d0-904c5aa74707"
    },
    {
      "@type": "Membership",
      "collection": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
      "entity": "id:ac975c99-5d6d-476f-b3ab-750fd0ac460d"
    },
    {
      "@type": "Membership",
      "collection": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "entity": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4"
    },
    {
      "@type": "Membership",
      "collection": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1",
      "entity": "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248"
    },
    {
      "@type": "Membership",
      "collection": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "entity": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:5fa19808-d14c-4c01-8bd1-05a7a8845019",
      "generalEntity": "data:8cb131413518c30be6ba485ea61764491444cde5"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:e06b906c-ef24-4174-830c-4a184274216f",
      "generalEntity": "data:8a97a5260b1039d7f867c2f9ab8ee36a5cb5fbd4"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5",
      "generalEntity": "data:8cb131413518c30be6ba485ea61764491444cde5"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:8a52cbfa-2822-476c-baed-680f3a070398",
      "generalEntity": "data:e74c29702b96c01957579e7d11b35d835356376b"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313",
      "generalEntity": "data:a234b13e2668a49acb831fdf87f3c1ead120dd41"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:471cf7c7-1a60-4c28-b3d0-904c5aa74707",
      "generalEntity": "data:8a97a5260b1039d7f867c2f9ab8ee36a5cb5fbd4"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:ac975c99-5d6d-476f-b3ab-750fd0ac460d",
      "generalEntity": "data:d6d2a88a822dadbc95c6d3381d6b0386e94a2148"
    },
    {
      "@type": "Generation",
      "entity": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "activity": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "time": "2026-09-23T22:17:45.432581",
      "role": [
        "wf:main/node_stac/stac_catalog"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "time": "2026-09-23T22:17:45.465410",
      "role": [
        "wf:main/primary/stac"
      ]
    },
    {
      "@type": "End",
      "activity": "id:fbfd9735-117b-4cdd-9707-61f171585925",
      "ender": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "time": "2026-09-23T22:17:45.432570"
    },
    {
      "@type": "End",
      "activity": "id:43f96d95-9aa3-42a3-8046-388cdfaf7a80",
      "ender": "id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c",
      "time": "2026-09-23T22:17:45.465485"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf#ore",
      "generalEntity": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-afa01c29-85ed-418e-b3a4-99ff6f4b06cf.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0#ore",
      "generalEntity": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4#ore",
      "generalEntity": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-df33a1dc-d46c-4154-9213-04cfb8cc55c4.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1#ore",
      "generalEntity": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-a782f6a0-89d7-46ac-9c76-c6569903f8e1.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248#ore",
      "generalEntity": "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-76afd8f9-b8f8-4b00-88b9-5bbf50509248.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-afa01c29-85ed-418e-b3a4-99ff6f4b06cf.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
          "type": [
            "ore:Aggregation",
            "ro:Folder"
          ],
          "ore:aggregates": [
            {
              "@value": "id:2d2f953e-2ade-4e61-9cd0-64f1866d2c1d",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:23bdb369-3e88-43b2-81e3-b9324f75e079",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:a9451218-986b-4920-9d23-62638b8aea56",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:7d9076f9-073d-4667-84e9-131fd7fda68c",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:23bdb369-3e88-43b2-81e3-b9324f75e079",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "S2B_10TFK_20210713_0_L2A"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:2d2f953e-2ade-4e61-9cd0-64f1866d2c1d",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "catalog.json"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:7d9076f9-073d-4667-84e9-131fd7fda68c",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "S2A_10TFK_20220524_0_L2A"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:a9451218-986b-4920-9d23-62638b8aea56",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": ".cache"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1",
              "@type": "xsd:QName"
            }
          ]
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
          "type": [
            "ore:Aggregation",
            "ro:Folder"
          ],
          "ore:aggregates": [
            {
              "@value": "id:1aa0c641-ea02-485d-a14b-c5a0aa40154b",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:bbd82449-f35c-4d0e-a771-32af085fe0db",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:bbd82449-f35c-4d0e-a771-32af085fe0db",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "otsu.tif"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:1aa0c641-ea02-485d-a14b-c5a0aa40154b",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "S2B_10TFK_20210713_0_L2A.json"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:8a52cbfa-2822-476c-baed-680f3a070398",
              "@type": "xsd:QName"
            }
          ]
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-df33a1dc-d46c-4154-9213-04cfb8cc55c4.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
          "type": [
            "ore:Aggregation",
            "ro:Folder"
          ],
          "ore:aggregates": [
            {
              "@value": "id:0c932b2b-21cb-4d36-8eda-c9d07f86bf53",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:4c5ac9a5-8f70-4cc6-bb2f-89864afd51b9",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:4c5ac9a5-8f70-4cc6-bb2f-89864afd51b9",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "otsu.tif"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:471cf7c7-1a60-4c28-b3d0-904c5aa74707",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:0c932b2b-21cb-4d36-8eda-c9d07f86bf53",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "S2A_10TFK_20220524_0_L2A.json"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:ac975c99-5d6d-476f-b3ab-750fd0ac460d",
              "@type": "xsd:QName"
            }
          ]
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-a782f6a0-89d7-46ac-9c76-c6569903f8e1.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1",
          "type": [
            "ore:Aggregation",
            "ro:Folder"
          ],
          "ore:aggregates": [
            {
              "@value": "id:3a1a053d-536c-4e6f-a7c6-7a9348502781",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:3a1a053d-536c-4e6f-a7c6-7a9348502781",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "rosetta"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248",
              "@type": "xsd:QName"
            }
          ]
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-76afd8f9-b8f8-4b00-88b9-5bbf50509248.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "metadata": "arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248",
          "type": [
            "ore:Aggregation",
            "ro:Folder"
          ]
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix cwlprov: <https://w3id.org/cwl/prov#> .
@prefix data: <urn:hash::sha1:> .
@prefix id: <urn:uuid:> .
@prefix metadata: <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/metadata/> .
@prefix ore: <http://www.openarchives.org/ore/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix provext: <https://openprovenance.org/ns/provext#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ro: <http://purl.org/wf4ever/ro#> .
@prefix wf: <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#> .
@prefix wf4ever: <http://purl.org/wf4ever/wf4ever#> .
@prefix wfdesc: <http://purl.org/wf4ever/wfdesc#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

metadata:directory-1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0.ttl a prov:Bundle .

metadata:directory-76afd8f9-b8f8-4b00-88b9-5bbf50509248.ttl a prov:Bundle .

metadata:directory-a782f6a0-89d7-46ac-9c76-c6569903f8e1.ttl a prov:Bundle .

metadata:directory-afa01c29-85ed-418e-b3a4-99ff6f4b06cf.ttl a prov:Bundle .

metadata:directory-df33a1dc-d46c-4154-9213-04cfb8cc55c4.ttl a prov:Bundle .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_water_bodies> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

id:006f10ba-bce7-4602-bc25-46f0ca2c5724 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/water-bodies/node_water_bodies" ;
    prov:has_provenance "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.json"^^xsd:QName,
        "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.jsonld"^^xsd:QName,
        "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.nt"^^xsd:QName,
        "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.provn"^^xsd:QName,
        "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.ttl"^^xsd:QName,
        "provenance:workflow_20node_water_bodies.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.xml"^^xsd:QName,
        "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.json"^^xsd:QName,
        "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.jsonld"^^xsd:QName,
        "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.nt"^^xsd:QName,
        "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.provn"^^xsd:QName,
        "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.ttl"^^xsd:QName,
        "provenance:workflow_20node_water_bodies_2.006f10ba-bce7-4602-bc25-46f0ca2c5724.cwlprov.xml"^^xsd:QName ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/water-bodies/node_water_bodies> ],
        [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/water-bodies/node_water_bodies> ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:14:43.790754"^^xsd:dateTime ;
            prov:hadActivity id:43f96d95-9aa3-42a3-8046-388cdfaf7a80 ],
        [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:37.996102"^^xsd:dateTime ;
            prov:hadActivity id:43f96d95-9aa3-42a3-8046-388cdfaf7a80 ] .

id:0c932b2b-21cb-4d36-8eda-c9d07f86bf53 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:ac975c99-5d6d-476f-b3ab-750fd0ac460d"^^xsd:QName ;
    prov:pairKey "S2A_10TFK_20220524_0_L2A.json" .

id:1aa0c641-ea02-485d-a14b-c5a0aa40154b a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:8a52cbfa-2822-476c-baed-680f3a070398"^^xsd:QName ;
    prov:pairKey "S2B_10TFK_20210713_0_L2A.json" .

<urn:uuid:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0.ttl"^^xsd:QName ;
            provext:generalEntity id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0 ] .

id:23bdb369-3e88-43b2-81e3-b9324f75e079 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0"^^xsd:QName ;
    prov:pairKey "S2B_10TFK_20210713_0_L2A" .

id:2d2f953e-2ade-4e61-9cd0-64f1866d2c1d a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313"^^xsd:QName ;
    prov:pairKey "catalog.json" .

id:3a1a053d-536c-4e6f-a7c6-7a9348502781 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:76afd8f9-b8f8-4b00-88b9-5bbf50509248"^^xsd:QName ;
    prov:pairKey "rosetta" .

id:4c5ac9a5-8f70-4cc6-bb2f-89864afd51b9 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:471cf7c7-1a60-4c28-b3d0-904c5aa74707"^^xsd:QName ;
    prov:pairKey "otsu.tif" .

<urn:uuid:76afd8f9-b8f8-4b00-88b9-5bbf50509248#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-76afd8f9-b8f8-4b00-88b9-5bbf50509248.ttl"^^xsd:QName ;
            provext:generalEntity id:76afd8f9-b8f8-4b00-88b9-5bbf50509248 ] .

id:7d9076f9-073d-4667-84e9-131fd7fda68c a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:df33a1dc-d46c-4154-9213-04cfb8cc55c4"^^xsd:QName ;
    prov:pairKey "S2A_10TFK_20220524_0_L2A" .

<urn:uuid:a782f6a0-89d7-46ac-9c76-c6569903f8e1#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-a782f6a0-89d7-46ac-9c76-c6569903f8e1.ttl"^^xsd:QName ;
            provext:generalEntity id:a782f6a0-89d7-46ac-9c76-c6569903f8e1 ] .

id:a9451218-986b-4920-9d23-62638b8aea56 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:a782f6a0-89d7-46ac-9c76-c6569903f8e1"^^xsd:QName ;
    prov:pairKey ".cache" .

<urn:uuid:afa01c29-85ed-418e-b3a4-99ff6f4b06cf#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-afa01c29-85ed-418e-b3a4-99ff6f4b06cf.ttl"^^xsd:QName ;
            provext:generalEntity id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf ] .

id:bbd82449-f35c-4d0e-a771-32af085fe0db a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5"^^xsd:QName ;
    prov:pairKey "otsu.tif" .

<urn:uuid:df33a1dc-d46c-4154-9213-04cfb8cc55c4#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-df33a1dc-d46c-4154-9213-04cfb8cc55c4.ttl"^^xsd:QName ;
            provext:generalEntity id:df33a1dc-d46c-4154-9213-04cfb8cc55c4 ] .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/node_stac"^^xsd:QName,
        "wf:main/node_water_bodies"^^xsd:QName .

<arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_stac> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

data:9d1fba832b03655b5b73ff964bc74d4543bf904a a wfprov:Artifact,
        prov:Entity ;
    prov:value "EPSG:4326" .

data:a234b13e2668a49acb831fdf87f3c1ead120dd41 a wfprov:Artifact,
        prov:Entity .

data:ba936cb0e062bea4078e8b56371ca8fe054093dd a wfprov:Artifact,
        prov:Entity ;
    prov:value "nir" .

data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c a wfprov:Artifact,
        prov:Entity ;
    prov:value "green" .

data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad a wfprov:Artifact,
        prov:Entity ;
    prov:value "-121.399,39.834,-120.74,40.472" .

data:d6d2a88a822dadbc95c6d3381d6b0386e94a2148 a wfprov:Artifact,
        prov:Entity .

data:e74c29702b96c01957579e7d11b35d835356376b a wfprov:Artifact,
        prov:Entity .

id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8cb131413518c30be6ba485ea61764491444cde5 ] ;
    cwlprov:basename "otsu.tif" .

id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:a234b13e2668a49acb831fdf87f3c1ead120dd41 ] ;
    cwlprov:basename "catalog.json" .

id:1851e03b-b5dd-458e-b892-800c846451b6 a prov:Agent .

id:25ff238f-e08b-4dee-a1f9-485e90a02a52 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:09dd884abf8f162fa6ed55f0e958ce9586b8bffd ],
        [ a provext:Membership ;
            provext:member data:5f0002427ab880579cf6a5a5c704bd399f3310f2 ] .

id:3d637621-61a3-4c53-8aaf-70daadac3593 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:5fa19808-d14c-4c01-8bd1-05a7a8845019 ],
        [ a provext:Membership ;
            provext:member id:e06b906c-ef24-4174-830c-4a184274216f ] .

id:471cf7c7-1a60-4c28-b3d0-904c5aa74707 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8a97a5260b1039d7f867c2f9ab8ee36a5cb5fbd4 ] ;
    cwlprov:basename "otsu.tif" .

id:511850b1-b1bc-44cd-8316-bdd367fefd98 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:09dd884abf8f162fa6ed55f0e958ce9586b8bffd ],
        [ a provext:Membership ;
            provext:member data:5f0002427ab880579cf6a5a5c704bd399f3310f2 ] .

id:5fa19808-d14c-4c01-8bd1-05a7a8845019 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8cb131413518c30be6ba485ea61764491444cde5 ] ;
    cwlprov:basename "otsu.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "otsu" .

id:8a52cbfa-2822-476c-baed-680f3a070398 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e74c29702b96c01957579e7d11b35d835356376b ] ;
    cwlprov:basename "S2B_10TFK_20210713_0_L2A.json" .

id:ac975c99-5d6d-476f-b3ab-750fd0ac460d a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:d6d2a88a822dadbc95c6d3381d6b0386e94a2148 ] ;
    cwlprov:basename "S2A_10TFK_20220524_0_L2A.json" .

id:afa01c29-85ed-418e-b3a4-99ff6f4b06cf a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-afa01c29-85ed-418e-b3a4-99ff6f4b06cf.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:23bdb369-3e88-43b2-81e3-b9324f75e079"^^xsd:QName,
        "id:2d2f953e-2ade-4e61-9cd0-64f1866d2c1d"^^xsd:QName,
        "id:7d9076f9-073d-4667-84e9-131fd7fda68c"^^xsd:QName,
        "id:a9451218-986b-4920-9d23-62638b8aea56"^^xsd:QName ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:fbfd9735-117b-4cdd-9707-61f171585925 ;
            prov:atTime "2026-09-23T22:17:45.432581"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_stac/stac_catalog> ],
        [ a prov:Generation ;
            prov:activity id:43f96d95-9aa3-42a3-8046-388cdfaf7a80 ;
            prov:atTime "2026-09-23T22:17:45.465410"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/primary/stac> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0 ],
        [ a provext:Membership ;
            provext:member id:df33a1dc-d46c-4154-9213-04cfb8cc55c4 ],
        [ a provext:Membership ;
            provext:member id:a782f6a0-89d7-46ac-9c76-c6569903f8e1 ],
        [ a provext:Membership ;
            provext:member id:0d06dfcd-e7b7-4fad-a2a5-66cddd416313 ] ;
    cwlprov:basename "docker_tmpwngcerl4" .

id:b6924a3c-a25c-4107-bdd7-2b5b2bff912e a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:ba936cb0e062bea4078e8b56371ca8fe054093dd ],
        [ a provext:Membership ;
            provext:member data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c ] .

id:d8353ab3-7279-484e-a461-b04ae4b52890 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0" ;
    cwlprov:image "ghcr.io/terradue/ogc-eo-application-package-hands-on/stac:1.5.0" .

id:e06b906c-ef24-4174-830c-4a184274216f a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8a97a5260b1039d7f867c2f9ab8ee36a5cb5fbd4 ] ;
    cwlprov:basename "otsu.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "otsu" .

id:fbfd9735-117b-4cdd-9707-61f171585925 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/node_stac" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_stac> ],
        [ a prov:Association ;
            prov:agent id:d8353ab3-7279-484e-a461-b04ae4b52890 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:17:45.432570"^^xsd:dateTime ;
            prov:hadActivity id:43f96d95-9aa3-42a3-8046-388cdfaf7a80 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:17:40.502305"^^xsd:dateTime ;
            prov:hadActivity id:43f96d95-9aa3-42a3-8046-388cdfaf7a80 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:17:40.581639"^^xsd:dateTime ;
            prov:entity id:25ff238f-e08b-4dee-a1f9-485e90a02a52 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_stac/item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:17:40.582084"^^xsd:dateTime ;
            prov:entity id:3d637621-61a3-4c53-8aaf-70daadac3593 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/node_stac/rasters> ] .

data:09dd884abf8f162fa6ed55f0e958ce9586b8bffd a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_10TFK_20220524_0_L2A" .

data:5f0002427ab880579cf6a5a5c704bd399f3310f2 a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A" .

data:8a97a5260b1039d7f867c2f9ab8ee36a5cb5fbd4 a wfprov:Artifact,
        prov:Entity .

data:8cb131413518c30be6ba485ea61764491444cde5 a wfprov:Artifact,
        prov:Entity .

id:1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0 a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-1d5bc5ed-98ce-4f75-8ca8-c19f497b03c0.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:1aa0c641-ea02-485d-a14b-c5a0aa40154b"^^xsd:QName,
        "id:bbd82449-f35c-4d0e-a771-32af085fe0db"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:8a52cbfa-2822-476c-baed-680f3a070398 ],
        [ a provext:Membership ;
            provext:member id:0825c9ab-8336-4546-bdb6-27a7ec74c6b5 ] ;
    cwlprov:basename "S2B_10TFK_20210713_0_L2A" .

id:76afd8f9-b8f8-4b00-88b9-5bbf50509248 a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:EmptyCollection,
        prov:EmptyDictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-76afd8f9-b8f8-4b00-88b9-5bbf50509248.ttl"^^xsd:QName ;
    cwlprov:basename "rosetta" .

id:a782f6a0-89d7-46ac-9c76-c6569903f8e1 a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-a782f6a0-89d7-46ac-9c76-c6569903f8e1.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:3a1a053d-536c-4e6f-a7c6-7a9348502781"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:76afd8f9-b8f8-4b00-88b9-5bbf50509248 ] ;
    cwlprov:basename ".cache" .

id:df33a1dc-d46c-4154-9213-04cfb8cc55c4 a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-df33a1dc-d46c-4154-9213-04cfb8cc55c4.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:0c932b2b-21cb-4d36-8eda-c9d07f86bf53"^^xsd:QName,
        "id:4c5ac9a5-8f70-4cc6-bb2f-89864afd51b9"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:471cf7c7-1a60-4c28-b3d0-904c5aa74707 ],
        [ a provext:Membership ;
            provext:member id:ac975c99-5d6d-476f-b3ab-750fd0ac460d ] ;
    cwlprov:basename "S2A_10TFK_20220524_0_L2A" .

id:43f96d95-9aa3-42a3-8046-388cdfaf7a80 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T22:17:45.465485"^^xsd:dateTime ;
            prov:hadActivity id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:35.483879"^^xsd:dateTime ;
            prov:hadActivity id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.991132"^^xsd:dateTime ;
            prov:entity data:c968ad55dbad27ec9518fb34f62e7ac54bcbe7ad ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.992978"^^xsd:dateTime ;
            prov:entity id:b6924a3c-a25c-4107-bdd7-2b5b2bff912e ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/bands> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.993781"^^xsd:dateTime ;
            prov:entity data:9d1fba832b03655b5b73ff964bc74d4543bf904a ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T22:09:37.995200"^^xsd:dateTime ;
            prov:entity id:511850b1-b1bc-44cd-8316-bdd367fefd98 ;
            prov:hadRole <arcp://uuid,43f96d95-9aa3-42a3-8046-388cdfaf7a80/workflow/packed.cwl#main/stac_items> ] ;
    prov:startedAtTime "2026-09-23T22:09:35.483832"^^xsd:dateTime .

id:39955f0d-0ccf-44b0-b0a9-70d1dd48559c a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T22:09:35.483801"^^xsd:dateTime ;
            prov:hadActivity id:1851e03b-b5dd-458e-b892-800c846451b6 ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `stac` (CWL
  CommandLineTool). Pins the process id and the input/output names; the input/output
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
      const: stac
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - item
      - rasters
      propertyNames:
        enum:
        - item
        - rasters
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - stac_catalog
      propertyNames:
        enum:
        - stac_catalog
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
        - item
        - rasters
        propertyNames:
          enum:
          - item
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
          - stac_catalog
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
      - stac_catalog
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/water-bodies/stac/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/water-bodies/stac`

