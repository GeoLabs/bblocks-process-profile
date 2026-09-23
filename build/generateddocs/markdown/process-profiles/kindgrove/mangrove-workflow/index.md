
# Process profile: mangrove-workflow (Schema)

`ospd.process-profiles.kindgrove.mangrove-workflow` *v0.1*

OGC API - Processes profile of the CWL Workflow `mangrove-workflow` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`mangrove-workflow`** (Workflow, W2 KindGrove).

> Mangrove Biomass Workflow

## Source

- CWL: [mangrove-workflow.cwl#mangrove-workflow](https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow) (pinned commit `291a741`, license <https://spdx.org/licenses/Apache-2.0>). Referenced, not copied.
- Six-phase position: Filter configuration → Selection / filtering → Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: `eoap.cct.bbox`
- Steps (profiles): `ospd.process-profiles.kindgrove.parse-aoi`, `ospd.process-profiles.kindgrove.mangrove`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `cloud_cover_max` | float | `stac` | Directory |
| `days_back` | int |  |  |
| `aoi` | https://raw.githubusercontent.com/eoap/schemas/main/ogc.yaml#BBox |  |  |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-05 outputs.stac: the Directory output is a STAC Catalog written by the tool itself (run record: `catalog.json` with one Item), not the Collection assumed by the transform

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w2-pinned`: the register's pinned W2 source itself (bblocks-eoap-cct c27c60d `mangrove-workflow.cwl#mangrove-workflow`) run with the profile's execute inputs, `cwltool --no-match-user --provenance ro --outdir out`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, 126 s; scene selected by `days_back` on that day: S2C_46PGC_20260913_0_L2A), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite of a BBox-unpacking helper and one opaque tool; the openEO equivalent is a process graph (see the `mangrove` profile for the stage-by-stage decomposition). `stac.yaml` is imported in `SchemaDefRequirement` but unused.


| Stage | openEO | Level | Note |
|---|---|---|---|
| parse_aoi | — | none | structural; bounding box is a native openEO parameter type |
| step_1 (mangrove_cli) | — | none | see ospd.process-profiles.kindgrove.mangrove |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL Workflow is referenced, not copied: <https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow>.

### processDescription
OGC API - Processes processDescription derived from the CWL (manually corrected, see description).
#### json
```json
{
  "id": "mangrove-workflow",
  "version": "0.0.1",
  "title": "Mangrove Biomass Workflow",
  "description": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n",
  "mutable": true,
  "keywords": [
    "OSPD",
    "mangrove",
    "biomass"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Mangrove Biomass Workflow"
    },
    {
      "role": "https://schema.org/description",
      "value": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "0.0.1"
    },
    {
      "role": "https://schema.org/author",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Cameron Sajedi"
      }
    },
    {
      "role": "https://schema.org/contributor",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Gérald Fenoy",
        "identifier": "https://orcid.org/0000-0002-9617-8641"
      }
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://github.com/starling-foundries/KindGrove"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://github.com/starling-foundries/KindGrove?tab=MIT-1-ov-file#readme"
    }
  ],
  "inputs": {
    "cloud_cover_max": {
      "title": "Maximum Cloud Cover",
      "description": "Maximum acceptable cloud cover percentage (0-100)",
      "schema": {
        "type": "number"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "days_back": {
      "title": "Days Back",
      "description": "Number of days to search backwards from current date",
      "schema": {
        "type": "integer"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "Area of Interest",
      "description": "Area of interest as a bounding box",
      "schema": {
        "type": "object",
        "required": [
          "bbox"
        ],
        "properties": {
          "bbox": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "oneOf": [
              {
                "minItems": 4,
                "maxItems": 4,
                "description": "2D bbox"
              },
              {
                "minItems": 6,
                "maxItems": 6,
                "description": "3D bbox"
              }
            ]
          },
          "crs": {
            "type": "string",
            "enum": [
              "CRS84",
              "CRS84h"
            ],
            "default": "CRS84"
          }
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "stac": {
      "title": "stac",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "id": "mangrove-workflow",
  "version": "0.0.1",
  "title": "Mangrove Biomass Workflow",
  "description": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n",
  "mutable": true,
  "keywords": [
    "OSPD",
    "mangrove",
    "biomass"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Mangrove Biomass Workflow"
    },
    {
      "role": "https://schema.org/description",
      "value": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "0.0.1"
    },
    {
      "role": "https://schema.org/author",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Cameron Sajedi"
      }
    },
    {
      "role": "https://schema.org/contributor",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "G\u00e9rald Fenoy",
        "identifier": "https://orcid.org/0000-0002-9617-8641"
      }
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://github.com/starling-foundries/KindGrove"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://github.com/starling-foundries/KindGrove?tab=MIT-1-ov-file#readme"
    }
  ],
  "inputs": {
    "cloud_cover_max": {
      "title": "Maximum Cloud Cover",
      "description": "Maximum acceptable cloud cover percentage (0-100)",
      "schema": {
        "type": "number"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "days_back": {
      "title": "Days Back",
      "description": "Number of days to search backwards from current date",
      "schema": {
        "type": "integer"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "Area of Interest",
      "description": "Area of interest as a bounding box",
      "schema": {
        "type": "object",
        "required": [
          "bbox"
        ],
        "properties": {
          "bbox": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "oneOf": [
              {
                "minItems": 4,
                "maxItems": 4,
                "description": "2D bbox"
              },
              {
                "minItems": 6,
                "maxItems": 6,
                "description": "3D bbox"
              }
            ]
          },
          "crs": {
            "type": "string",
            "enum": [
              "CRS84",
              "CRS84h"
            ],
            "default": "CRS84"
          }
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "stac": {
      "title": "stac",
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
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <http://schema.org/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove-workflow> dcterms:description """Workflow for Mangrove Biomass Analysis
  
This workflow orchestrates the mangrove biomass estimation process using
Sentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide
a reusable workflow for analyzing different study areas.
""" ;
    dcterms:subject "OSPD",
        "biomass",
        "mangrove" ;
    dcterms:title "Mangrove Biomass Workflow" ;
    pp:version "0.0.1" ;
    proc:inputs [ ns1:aoi [ dcterms:description "Area of interest as a bounding box" ;
                    dcterms:title "Area of Interest" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "object" ;
                            ns2:properties [ ns2:bbox [ proc:type "array" ;
                                            ns2:items [ proc:type "number" ] ;
                                            ns2:oneOf [ dcterms:description "2D bbox" ;
                                                    ns2:maxItems 4 ;
                                                    ns2:minItems 4 ],
                                                [ dcterms:description "3D bbox" ;
                                                    ns2:maxItems 6 ;
                                                    ns2:minItems 6 ] ] ;
                                    ns2:crs [ proc:default "\"CRS84\""^^rdf:JSON ;
                                            proc:enum "CRS84",
                                                "CRS84h" ;
                                            proc:type "string" ] ] ;
                            ns2:required "bbox" ] ] ;
            ns1:cloud_cover_max [ dcterms:description "Maximum acceptable cloud cover percentage (0-100)" ;
                    dcterms:title "Maximum Cloud Cover" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns1:days_back [ dcterms:description "Number of days to search backwards from current date" ;
                    dcterms:title "Days Back" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "integer" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value [ a ns4:Person ;
                    ns4:name "Cameron Sajedi" ] ;
            proc:role schema:author ],
        [ rdf:value "Mangrove Biomass Workflow" ;
            proc:role schema:name ],
        [ rdf:value "https://github.com/starling-foundries/KindGrove?tab=MIT-1-ov-file#readme" ;
            proc:role schema:license ],
        [ rdf:value "https://github.com/starling-foundries/KindGrove" ;
            proc:role schema:codeRepository ],
        [ rdf:value "0.0.1" ;
            proc:role schema:softwareVersion ],
        [ rdf:value """Workflow for Mangrove Biomass Analysis
  
This workflow orchestrates the mangrove biomass estimation process using
Sentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide
a reusable workflow for analyzing different study areas.
""" ;
            proc:role schema:description ],
        [ rdf:value [ a ns4:Person ;
                    ns4:identifier "https://orcid.org/0000-0002-9617-8641" ;
                    ns4:name "Gérald Fenoy" ] ;
            proc:role schema:contributor ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:stac [ dcterms:description "" ;
                    dcterms:title "stac" ;
                    proc:schema [ proc:type "object" ;
                            ns2:format "stac-catalog" ;
                            ns2:properties [ dcterms:description [ proc:type "string" ] ;
                                    dcterms:title [ proc:type "string" ] ;
                                    rdfs:seeAlso [ dcterms:type "array" ] ;
                                    proc:type [ proc:enum "Catalog" ;
                                            proc:type "string" ] ;
                                    ns2:stac_version [ proc:type "string" ] ] ;
                            ns2:required "description",
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
  "id": "mangrove-workflow",
  "version": "0.0.1",
  "title": "Mangrove Biomass Workflow",
  "description": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n",
  "mutable": true,
  "keywords": [
    "OSPD",
    "mangrove",
    "biomass"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Mangrove Biomass Workflow"
    },
    {
      "role": "https://schema.org/description",
      "value": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "0.0.1"
    },
    {
      "role": "https://schema.org/author",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Cameron Sajedi"
      }
    },
    {
      "role": "https://schema.org/contributor",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Gérald Fenoy",
        "identifier": "https://orcid.org/0000-0002-9617-8641"
      }
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://github.com/starling-foundries/KindGrove"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://github.com/starling-foundries/KindGrove?tab=MIT-1-ov-file#readme"
    }
  ],
  "inputs": {
    "cloud_cover_max": {
      "title": "Maximum Cloud Cover",
      "description": "Maximum acceptable cloud cover percentage (0-100)",
      "schema": {
        "type": "number"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "days_back": {
      "title": "Days Back",
      "description": "Number of days to search backwards from current date",
      "schema": {
        "type": "integer"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "Area of Interest",
      "description": "Area of interest as a bounding box",
      "schema": {
        "type": "object",
        "required": [
          "bbox"
        ],
        "properties": {
          "bbox": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "oneOf": [
              {
                "minItems": 4,
                "maxItems": 4,
                "description": "2D bbox"
              },
              {
                "minItems": 6,
                "maxItems": 6,
                "description": "3D bbox"
              }
            ]
          },
          "crs": {
            "type": "string",
            "enum": [
              "CRS84",
              "CRS84h"
            ],
            "default": "CRS84"
          }
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "stac": {
      "title": "stac",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "id": "mangrove-workflow",
  "version": "0.0.1",
  "title": "Mangrove Biomass Workflow",
  "description": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n",
  "mutable": true,
  "keywords": [
    "OSPD",
    "mangrove",
    "biomass"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Mangrove Biomass Workflow"
    },
    {
      "role": "https://schema.org/description",
      "value": "Workflow for Mangrove Biomass Analysis\n  \nThis workflow orchestrates the mangrove biomass estimation process using\nSentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide\na reusable workflow for analyzing different study areas.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "0.0.1"
    },
    {
      "role": "https://schema.org/author",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Cameron Sajedi"
      }
    },
    {
      "role": "https://schema.org/contributor",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "G\u00e9rald Fenoy",
        "identifier": "https://orcid.org/0000-0002-9617-8641"
      }
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://github.com/starling-foundries/KindGrove"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://github.com/starling-foundries/KindGrove?tab=MIT-1-ov-file#readme"
    }
  ],
  "inputs": {
    "cloud_cover_max": {
      "title": "Maximum Cloud Cover",
      "description": "Maximum acceptable cloud cover percentage (0-100)",
      "schema": {
        "type": "number"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "days_back": {
      "title": "Days Back",
      "description": "Number of days to search backwards from current date",
      "schema": {
        "type": "integer"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "Area of Interest",
      "description": "Area of interest as a bounding box",
      "schema": {
        "type": "object",
        "required": [
          "bbox"
        ],
        "properties": {
          "bbox": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "oneOf": [
              {
                "minItems": 4,
                "maxItems": 4,
                "description": "2D bbox"
              },
              {
                "minItems": 6,
                "maxItems": 6,
                "description": "3D bbox"
              }
            ]
          },
          "crs": {
            "type": "string",
            "enum": [
              "CRS84",
              "CRS84h"
            ],
            "default": "CRS84"
          }
        }
      },
      "minOccurs": 1,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "stac": {
      "title": "stac",
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
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <http://schema.org/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove-workflow> dcterms:description """Workflow for Mangrove Biomass Analysis
  
This workflow orchestrates the mangrove biomass estimation process using
Sentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide
a reusable workflow for analyzing different study areas.
""" ;
    dcterms:subject "OSPD",
        "biomass",
        "mangrove" ;
    dcterms:title "Mangrove Biomass Workflow" ;
    pp:version "0.0.1" ;
    proc:inputs [ ns2:aoi [ dcterms:description "Area of interest as a bounding box" ;
                    dcterms:title "Area of Interest" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "object" ;
                            ns1:properties [ ns1:bbox [ proc:type "array" ;
                                            ns1:items [ proc:type "number" ] ;
                                            ns1:oneOf [ dcterms:description "3D bbox" ;
                                                    ns1:maxItems 6 ;
                                                    ns1:minItems 6 ],
                                                [ dcterms:description "2D bbox" ;
                                                    ns1:maxItems 4 ;
                                                    ns1:minItems 4 ] ] ;
                                    ns1:crs [ proc:default "\"CRS84\""^^rdf:JSON ;
                                            proc:enum "CRS84",
                                                "CRS84h" ;
                                            proc:type "string" ] ] ;
                            ns1:required "bbox" ] ] ;
            ns2:cloud_cover_max [ dcterms:description "Maximum acceptable cloud cover percentage (0-100)" ;
                    dcterms:title "Maximum Cloud Cover" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns2:days_back [ dcterms:description "Number of days to search backwards from current date" ;
                    dcterms:title "Days Back" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "integer" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "Mangrove Biomass Workflow" ;
            proc:role schema:name ],
        [ rdf:value """Workflow for Mangrove Biomass Analysis
  
This workflow orchestrates the mangrove biomass estimation process using
Sentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide
a reusable workflow for analyzing different study areas.
""" ;
            proc:role schema:description ],
        [ rdf:value "https://github.com/starling-foundries/KindGrove?tab=MIT-1-ov-file#readme" ;
            proc:role schema:license ],
        [ rdf:value [ a ns4:Person ;
                    ns4:identifier "https://orcid.org/0000-0002-9617-8641" ;
                    ns4:name "Gérald Fenoy" ] ;
            proc:role schema:contributor ],
        [ rdf:value "https://github.com/starling-foundries/KindGrove" ;
            proc:role schema:codeRepository ],
        [ rdf:value [ a ns4:Person ;
                    ns4:name "Cameron Sajedi" ] ;
            proc:role schema:author ],
        [ rdf:value "0.0.1" ;
            proc:role schema:softwareVersion ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:stac [ dcterms:description "" ;
                    dcterms:title "stac" ;
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
      "id": "mangrove-workflow",
      "version": "0.0.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "processDescription": {
    "process": {
      "id": "mangrove-workflow",
      "version": "0.0.1"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove-workflow> pp:version "0.0.1" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove-workflow> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/GeoLabs/bblocks-eoap-cct/raw/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow" ;
            pp:rel "http://www.opengis.net/def/rel/ogc/1.0/executionUnit" ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "aoi": {
      "bbox": [
        95.15,
        15.9,
        95.35,
        16.1
      ],
      "crs": "CRS84"
    },
    "cloud_cover_max": 20,
    "days_back": 90
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "inputs": {
    "aoi": {
      "bbox": [
        95.15,
        15.9,
        95.35,
        16.1
      ],
      "crs": "CRS84"
    },
    "cloud_cover_max": 20,
    "days_back": 90
  },
  "response": "document"
}
```

#### ttl
```ttl
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] proc:inputs [ ns1:aoi [ ns1:bbox 1.59e+01,
                        1.61e+01,
                        9.515e+01,
                        9.535e+01 ;
                    ns1:crs "CRS84" ] ;
            ns1:cloud_cover_max 20 ;
            ns1:days_back 90 ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "stac": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json",
    "type": "application/json"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "stac": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json",
    "type": "application/json"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:stac [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/json> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:kindgrove:mangrove-workflow",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow",
    "startedAtTime": "2026-09-23T08:01:10Z",
    "used": [
      "urn:example:entity:mangrove-workflow:in:aoi",
      "urn:example:entity:mangrove-workflow:in:cloud_cover_max",
      "urn:example:entity:mangrove-workflow:in:days_back"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/mangrove-workflow"
      }
    ],
    "endedAtTime": "2026-09-23T08:03:17Z"
  },
  {
    "id": "urn:example:entity:mangrove-workflow:in:aoi",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/aoi",
    "value": {
      "bbox": [
        95.15,
        15.9,
        95.35,
        16.1
      ],
      "crs": "CRS84"
    }
  },
  {
    "id": "urn:example:entity:mangrove-workflow:in:cloud_cover_max",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/cloud_cover_max",
    "value": 20
  },
  {
    "id": "urn:example:entity:mangrove-workflow:in:days_back",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/days_back",
    "value": 90
  },
  {
    "id": "urn:example:entity:mangrove-workflow:out:stac",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
    "wasGeneratedBy": "urn:example:run:kindgrove:mangrove-workflow",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json",
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
  }
]

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:kindgrove:mangrove-workflow",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow",
      "startedAtTime": "2026-09-23T08:01:10Z",
      "used": [
        "urn:example:entity:mangrove-workflow:in:aoi",
        "urn:example:entity:mangrove-workflow:in:cloud_cover_max",
        "urn:example:entity:mangrove-workflow:in:days_back"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/mangrove-workflow"
        }
      ],
      "endedAtTime": "2026-09-23T08:03:17Z"
    },
    {
      "id": "urn:example:entity:mangrove-workflow:in:aoi",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/aoi",
      "value": {
        "bbox": [
          95.15,
          15.9,
          95.35,
          16.1
        ],
        "crs": "CRS84"
      }
    },
    {
      "id": "urn:example:entity:mangrove-workflow:in:cloud_cover_max",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/cloud_cover_max",
      "value": 20
    },
    {
      "id": "urn:example:entity:mangrove-workflow:in:days_back",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/days_back",
      "value": 90
    },
    {
      "id": "urn:example:entity:mangrove-workflow:out:stac",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasGeneratedBy": "urn:example:run:kindgrove:mangrove-workflow",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json",
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

<urn:example:entity:mangrove-workflow:out:stac> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac> ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:kindgrove:mangrove-workflow> .

<urn:example:entity:mangrove-workflow:in:aoi> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/aoi> ;
    rdf:value [ pp:bbox 1.59e+01,
                1.61e+01,
                9.515e+01,
                9.535e+01 ;
            pp:crs "CRS84" ] .

<urn:example:entity:mangrove-workflow:in:cloud_cover_max> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/cloud_cover_max> ;
    rdf:value 20 .

<urn:example:entity:mangrove-workflow:in:days_back> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/mangrove-workflow#inputs/days_back> ;
    rdf:value 90 .

<urn:example:run:kindgrove:mangrove-workflow> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow> ;
    prov:endedAtTime "2026-09-23T08:03:17+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/mangrove-workflow> ] ;
    prov:startedAtTime "2026-09-23T08:01:10+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:mangrove-workflow:in:aoi>,
        <urn:example:entity:mangrove-workflow:in:cloud_cover_max>,
        <urn:example:entity:mangrove-workflow:in:days_back> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Execution bundle (generic provenance profile)
#### json
```json
{
  "run": {
    "id": "urn:example:run:kindgrove:mangrove-workflow",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/mangrove-workflow",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "kindgrove-mangrove-workflow-0001",
    "startedAtTime": "2026-09-23T08:01:10Z",
    "endedAtTime": "2026-09-23T08:03:17Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:kindgrove:parse-aoi"
      },
      {
        "id": "urn:example:run:kindgrove:mangrove"
      }
    ]
  },
  "engine": {
    "@id": "urn:example:engine:cwltool-3.1.20260108082145",
    "@type": "WorkflowEngine",
    "name": "cwltool",
    "version": "3.1.20260108082145"
  },
  "outputs": [
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json",
      "type": "Artifact",
      "role": "output",
      "mediaType": "application/json",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "8eeff5d9360c12c34666e58c05819462f451c0cb"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/biomass_summary.csv",
      "type": "Artifact",
      "role": "output",
      "mediaType": "text/csv",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "85e5b7702d82de1bc19c00fdebce3e4b00d9ae4c"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/carbon_summary.csv",
      "type": "Artifact",
      "role": "output",
      "mediaType": "text/csv",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "7e692955f3c119da05517da56423ef1afffeb3a1"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove-analysis-20260923-080315.json",
      "type": "Artifact",
      "role": "output",
      "mediaType": "application/json",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "85af35ec75b965fc1c515c5850cb53a81c919b22"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove_mask.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "de0d01dfb965345b5db12bd9c3701bd109aa9362"
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "run": {
    "id": "urn:example:run:kindgrove:mangrove-workflow",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/mangrove-workflow",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "kindgrove-mangrove-workflow-0001",
    "startedAtTime": "2026-09-23T08:01:10Z",
    "endedAtTime": "2026-09-23T08:03:17Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:kindgrove:parse-aoi"
      },
      {
        "id": "urn:example:run:kindgrove:mangrove"
      }
    ]
  },
  "engine": {
    "@id": "urn:example:engine:cwltool-3.1.20260108082145",
    "@type": "WorkflowEngine",
    "name": "cwltool",
    "version": "3.1.20260108082145"
  },
  "outputs": [
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json",
      "type": "Artifact",
      "role": "output",
      "mediaType": "application/json",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "8eeff5d9360c12c34666e58c05819462f451c0cb"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/biomass_summary.csv",
      "type": "Artifact",
      "role": "output",
      "mediaType": "text/csv",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "85e5b7702d82de1bc19c00fdebce3e4b00d9ae4c"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/carbon_summary.csv",
      "type": "Artifact",
      "role": "output",
      "mediaType": "text/csv",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "7e692955f3c119da05517da56423ef1afffeb3a1"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove-analysis-20260923-080315.json",
      "type": "Artifact",
      "role": "output",
      "mediaType": "application/json",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "85af35ec75b965fc1c515c5850cb53a81c919b22"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove_mask.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac",
      "wasOutputFrom": "urn:example:run:kindgrove:mangrove-workflow",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "de0d01dfb965345b5db12bd9c3701bd109aa9362"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json> prov:generated <urn:example:run:kindgrove:mangrove-workflow> ;
    ns1:checksum [ rdf:value "8eeff5d9360c12c34666e58c05819462f451c0cb" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac" ;
    ns1:mediaType "application/json" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/biomass_summary.csv> prov:generated <urn:example:run:kindgrove:mangrove-workflow> ;
    ns1:checksum [ rdf:value "85e5b7702d82de1bc19c00fdebce3e4b00d9ae4c" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac" ;
    ns1:mediaType "text/csv" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/carbon_summary.csv> prov:generated <urn:example:run:kindgrove:mangrove-workflow> ;
    ns1:checksum [ rdf:value "7e692955f3c119da05517da56423ef1afffeb3a1" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac" ;
    ns1:mediaType "text/csv" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove-analysis-20260923-080315.json> prov:generated <urn:example:run:kindgrove:mangrove-workflow> ;
    ns1:checksum [ rdf:value "85af35ec75b965fc1c515c5850cb53a81c919b22" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac" ;
    ns1:mediaType "application/json" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove_mask.tif> prov:generated <urn:example:run:kindgrove:mangrove-workflow> ;
    ns1:checksum [ rdf:value "de0d01dfb965345b5db12bd9c3701bd109aa9362" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/mangrove-workflow#outputs/stac" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<urn:example:engine:cwltool-3.1.20260108082145> a wfprov:WorkflowEngine ;
    pp:name "cwltool" ;
    pp:version "3.1.20260108082145" .

<urn:example:run:kindgrove:mangrove-workflow> a wfprov:WorkflowRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow> ;
    wfprov:describedByWorkflow <https://ospd.example.org/ogc-api/processes/mangrove-workflow> ;
    wfprov:hadSubProcessRun <urn:example:run:kindgrove:mangrove>,
        <urn:example:run:kindgrove:parse-aoi> ;
    prov:endedAtTime "2026-09-23T08:03:17+00:00"^^xsd:dateTime ;
    prov:startedAtTime "2026-09-23T08:01:10+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:jobID "kindgrove-mangrove-workflow-0001" ;
    pp:status "successful" .

[] pp:engine <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:run <urn:example:run:kindgrove:mangrove-workflow> ;
    proc:outputs <https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/catalog.json>,
        <https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/biomass_summary.csv>,
        <https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/carbon_summary.csv>,
        <https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove-analysis-20260923-080315.json>,
        <https://ospd.example.org/ogc-api/jobs/kindgrove-mangrove-workflow-0001/results/mangrove-analysis-20260923-080315/mangrove_mask.tif> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow",
  "type": "ProcessType",
  "prefLabel": "Mangrove Biomass Workflow",
  "definition": "Workflow for Mangrove Biomass Analysis This workflow orchestrates the mangrove biomass estimation process using Sentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide a reusable workflow for analyzing different study areas.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.kindgrove.mangrove-workflow",
  "processDescription": {
    "id": "mangrove-workflow",
    "version": "0.0.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow",
    "cwlClass": "Workflow",
    "cwlId": "mangrove-workflow",
    "license": "https://spdx.org/licenses/Apache-2.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#WorkflowRun",
  "cctDependencies": [
    "eoap.cct.bbox"
  ],
  "candidateCctDependencies": [],
  "hasStep": [
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/parse-aoi",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite of a BBox-unpacking helper and one opaque tool; the openEO equivalent is a process graph (see the `mangrove` profile for the stage-by-stage decomposition). `stac.yaml` is imported in `SchemaDefRequirement` but unused.",
    "decomposition": [
      {
        "stage": "parse_aoi",
        "openeo": [],
        "level": "none",
        "note": "structural; bounding box is a native openEO parameter type"
      },
      {
        "stage": "step_1 (mangrove_cli)",
        "openeo": [],
        "level": "none",
        "note": "see ospd.process-profiles.kindgrove.mangrove"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow",
  "type": "ProcessType",
  "prefLabel": "Mangrove Biomass Workflow",
  "definition": "Workflow for Mangrove Biomass Analysis This workflow orchestrates the mangrove biomass estimation process using Sentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide a reusable workflow for analyzing different study areas.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.kindgrove.mangrove-workflow",
  "processDescription": {
    "id": "mangrove-workflow",
    "version": "0.0.1"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow",
    "cwlClass": "Workflow",
    "cwlId": "mangrove-workflow",
    "license": "https://spdx.org/licenses/Apache-2.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#WorkflowRun",
  "cctDependencies": [
    "eoap.cct.bbox"
  ],
  "candidateCctDependencies": [],
  "hasStep": [
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/parse-aoi",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite of a BBox-unpacking helper and one opaque tool; the openEO equivalent is a process graph (see the `mangrove` profile for the stage-by-stage decomposition). `stac.yaml` is imported in `SchemaDefRequirement` but unused.",
    "decomposition": [
      {
        "stage": "parse_aoi",
        "openeo": [],
        "level": "none",
        "note": "structural; bounding box is a native openEO parameter type"
      },
      {
        "stage": "step_1 (mangrove_cli)",
        "openeo": [],
        "level": "none",
        "note": "see ospd.process-profiles.kindgrove.mangrove"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove-workflow> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> ;
    skos:definition "Workflow for Mangrove Biomass Analysis This workflow orchestrates the mangrove biomass estimation process using Sentinel-2 imagery. It wraps the mangrove_workflow.cwl tool to provide a reusable workflow for analyzing different study areas." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Mangrove Biomass Workflow" ;
    pp:cctDependency "eoap.cct.bbox" ;
    pp:hasStep <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/mangrove>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove/parse-aoi> ;
    pp:openeoEquivalence [ pp:decomposition ( [ skos:note "structural; bounding box is a native openEO parameter type" ;
                        pp:equivalenceLevel "none" ;
                        pp:stage "parse_aoi" ] [ skos:note "see ospd.process-profiles.kindgrove.mangrove" ;
                        pp:equivalenceLevel "none" ;
                        pp:stage "step_1 (mangrove_cli)" ] ) ;
            pp:equivalenceLevel "none" ;
            pp:rationale "Composite of a BBox-unpacking helper and one opaque tool; the openEO equivalent is a process graph (see the `mangrove` profile for the stage-by-stage decomposition). `stac.yaml` is imported in `SchemaDefRequirement` but unused." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove-workflow> ;
    pp:profile "ospd.process-profiles.kindgrove.mangrove-workflow" ;
    pp:provenanceClass wfprov:WorkflowRun ;
    pp:source [ pp:cwl <https://github.com/GeoLabs/bblocks-eoap-cct/blob/291a741c3f2b61da7607f1dbb7a777134374227d/_sources/cwl-to-ogcprocess/examples/mangrove-workflow.cwl#mangrove-workflow> ;
            pp:cwlClass "Workflow" ;
            pp:cwlId "mangrove-workflow" ;
            pp:license "https://spdx.org/licenses/Apache-2.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/mangrove-workflow> pp:version "0.0.1" .


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
      "researchobject": "arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/",
      "metadata": "arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/metadata/",
      "provenance": "arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/metadata/provenance/",
      "wf": "arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#",
      "input": "arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/primary-job.json#",
      "ro": "http://purl.org/wf4ever/ro#",
      "wf4ever": "http://purl.org/wf4ever/wf4ever#",
      "ore": "http://www.openarchives.org/ore/terms/"
    },
    "https://openprovenance.org/prov-jsonld/context.jsonld"
  ],
  "@graph": [
    {
      "@type": "Agent",
      "@id": "id:e6ce2559-8946-4151-834e-df99641e6f0b"
    },
    {
      "@type": "Agent",
      "@id": "id:3ad94428-01ae-451b-a3f4-af56b73e6981",
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
      "@id": "id:aef78493-9502-4ecb-9d44-f04f881f4650",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "alpine:3.22.2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image alpine:3.22.2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:a6977d92-2fbb-47e7-a784-4bfcb0da723b",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/mangrove-cwl:v0.0.1-rc7"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/mangrove-cwl:v0.0.1-rc7"
        }
      ]
    },
    {
      "@type": "Start",
      "activity": "id:3ad94428-01ae-451b-a3f4-af56b73e6981",
      "starter": "id:e6ce2559-8946-4151-834e-df99641e6f0b",
      "time": "2026-09-23T10:01:10.962414"
    },
    {
      "@type": "Start",
      "activity": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "starter": "id:3ad94428-01ae-451b-a3f4-af56b73e6981",
      "time": "2026-09-23T10:01:10.962463"
    },
    {
      "@type": "Start",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "starter": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "time": "2026-09-23T10:01:11.352398"
    },
    {
      "@type": "Start",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "starter": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "time": "2026-09-23T10:01:12.463948"
    },
    {
      "@type": "Activity",
      "@id": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "startTime": "2026-09-23T10:01:10.962438",
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
      "@id": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/parse_aoi"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/step_1"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "agent": "id:3ad94428-01ae-451b-a3f4-af56b73e6981",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "agent": "id:3ad94428-01ae-451b-a3f4-af56b73e6981",
      "plan": "wf:main/parse_aoi"
    },
    {
      "@type": "Association",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "agent": "id:aef78493-9502-4ecb-9d44-f04f881f4650"
    },
    {
      "@type": "Association",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "agent": "id:3ad94428-01ae-451b-a3f4-af56b73e6981",
      "plan": "wf:main/step_1"
    },
    {
      "@type": "Association",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "agent": "id:a6977d92-2fbb-47e7-a784-4bfcb0da723b"
    },
    {
      "@type": "Entity",
      "@id": "wf:main",
      "type": [
        "prov:Plan",
        "wfdesc:Workflow"
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
          "@value": "wf:main/step_1",
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
          "@value": "wf:main/parse_aoi",
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
      "@id": "wf:main/step_1",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/parse_aoi",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:74500aa8-7eb8-4831-a5d7-b57b0d559a7f",
      "type": [
        "prov:Collection",
        "wfprov:Artifact",
        "prov:Dictionary"
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:d4edcbc8-d63f-4e4a-b8fe-e640258e0481",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:93ea57b4-1913-4209-a534-4f43acc9e037",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:05148d8f-b41a-430e-ab3c-e47863420580",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:371c06f9-5e4f-482d-a56d-17457d592305",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3d6a2dea-df15-41de-943f-5c75ffc145fd",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5aa7a676-73f7-4cd5-bcc3-8c24e71dd6e0",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ef051260-da6b-471f-b7ec-77a3f03338f9",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d4edcbc8-d63f-4e4a-b8fe-e640258e0481",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "bbox"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:ef051260-da6b-471f-b7ec-77a3f03338f9",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:09b42388eb37be1a4b972127a78f691ec6eb3795",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "CRS84"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:09b42388eb37be1a4b972127a78f691ec6eb3795",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "CRS84"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:93ea57b4-1913-4209-a534-4f43acc9e037",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "crs"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "data:09b42388eb37be1a4b972127a78f691ec6eb3795",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d41afe53-37b5-4d07-a4d3-8f135d5ee9bd",
      "value": [
        {
          "@value": "20",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ab971800-6389-44da-a7db-d85c11161552",
      "value": [
        {
          "@value": "90",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3d909cf5-e433-4f42-a566-ecc18e8648ac",
      "type": [
        "prov:Collection",
        "wfprov:Artifact",
        "prov:Dictionary"
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:9dc1dc18-e01b-439a-818c-00162dabf4af",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:c78baf60-1897-4153-8e9c-e2eb311497b9",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:84fd2907-ae91-49e6-b896-5337cf88d4e4",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c5bac52b-0236-4d46-9e95-2715e4ebb57f",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:8cae0f0e-8136-47a3-91de-2df4cb915caa",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0b639232-1377-4260-9361-ccfad1f07653",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:9dc1dc18-e01b-439a-818c-00162dabf4af",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "bbox"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c78baf60-1897-4153-8e9c-e2eb311497b9",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "crs"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "data:09b42388eb37be1a4b972127a78f691ec6eb3795",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:100945f6-30da-4f24-8f5f-0cfe008c874a",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:f8e40067-1926-41f5-9278-ae93f18fb929",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e71003c6b7dd4093ce139ac0c51a6ba38d54a439",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "outputs"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e71003c6b7dd4093ce139ac0c51a6ba38d54a439",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "outputs"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5c1c3ee6-0407-4b28-8b0e-1ea049c4f4aa",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:07e4c7e6-d84f-4db0-bbd5-dd80fb19c086",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:980cdadc-8748-4ee0-8e50-02285fada4ac",
      "value": [
        {
          "@value": "20",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:cf0be29b-e4d9-4fd3-bd1b-2ed80a4095a9",
      "value": [
        {
          "@value": "90",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:43bb865a-d8cd-4787-8345-a30f5433a956",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:930cbb58-e736-4bd6-97e8-f8d6fdb3ecca",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a98d2a32-f817-4ba9-9a35-66d4b22bc9de",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d061c0fb-cd9b-4026-acea-7aa18b482246",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
      "type": [
        "prov:Collection",
        "wfprov:Artifact",
        "prov:Dictionary",
        "ro:Folder"
      ],
      "cwlprov:basename": [
        {
          "@value": "outputs"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-570b17a1-1129-4b02-b2bc-a4675847cf5d.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:f6d74394-3b64-40fe-a8c1-7c63d02a3a5e",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:a9056b20-82a6-42a0-a8f8-13f831d67eb4",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3efd1082-30b0-4081-aac3-595258d0235a",
      "type": [
        "prov:Collection",
        "wfprov:Artifact",
        "prov:Dictionary",
        "ro:Folder"
      ],
      "cwlprov:basename": [
        {
          "@value": "mangrove-analysis-20260923-080315"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-3efd1082-30b0-4081-aac3-595258d0235a.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:5cc84ac8-9c80-4fdd-9ec6-34906d34a5b9",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:33112eca-fd4d-4784-b9e2-ee97f20f8aec",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:beef0d3b-cdec-4f99-a497-ed54573e9aa0",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:d2617387-2a90-4dc3-8db3-0d71f8e3d6ef",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:7e692955f3c119da05517da56423ef1afffeb3a1",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:1a78bcc2-8056-4262-8f95-eff699d2deeb",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "carbon_summary.csv"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5cc84ac8-9c80-4fdd-9ec6-34906d34a5b9",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "carbon_summary.csv"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:1a78bcc2-8056-4262-8f95-eff699d2deeb",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:85af35ec75b965fc1c515c5850cb53a81c919b22",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:311c03b4-81b7-421a-8cd4-b744019dc39b",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "mangrove-analysis-20260923-080315.json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d2617387-2a90-4dc3-8db3-0d71f8e3d6ef",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "mangrove-analysis-20260923-080315.json"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:311c03b4-81b7-421a-8cd4-b744019dc39b",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:85e5b7702d82de1bc19c00fdebce3e4b00d9ae4c",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:1ec302cf-1d77-48c8-9550-86945f3a70ef",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "biomass_summary.csv"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:beef0d3b-cdec-4f99-a497-ed54573e9aa0",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "biomass_summary.csv"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:1ec302cf-1d77-48c8-9550-86945f3a70ef",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:de0d01dfb965345b5db12bd9c3701bd109aa9362",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:30f546f9-0831-4994-946d-88f0365ffd8a",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "mangrove_mask.tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:33112eca-fd4d-4784-b9e2-ee97f20f8aec",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "mangrove_mask.tif"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:30f546f9-0831-4994-946d-88f0365ffd8a",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a9056b20-82a6-42a0-a8f8-13f831d67eb4",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "mangrove-analysis-20260923-080315"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:3efd1082-30b0-4081-aac3-595258d0235a",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:8eeff5d9360c12c34666e58c05819462f451c0cb",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:204e8020-f340-4534-bcb6-378a06cfce69",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "catalog.json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:f6d74394-3b64-40fe-a8c1-7c63d02a3a5e",
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
          "@value": "id:204e8020-f340-4534-bcb6-378a06cfce69",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Membership",
      "collection": "id:ef051260-da6b-471f-b7ec-77a3f03338f9",
      "entity": "id:05148d8f-b41a-430e-ab3c-e47863420580"
    },
    {
      "@type": "Membership",
      "collection": "id:ef051260-da6b-471f-b7ec-77a3f03338f9",
      "entity": "id:371c06f9-5e4f-482d-a56d-17457d592305"
    },
    {
      "@type": "Membership",
      "collection": "id:ef051260-da6b-471f-b7ec-77a3f03338f9",
      "entity": "id:3d6a2dea-df15-41de-943f-5c75ffc145fd"
    },
    {
      "@type": "Membership",
      "collection": "id:ef051260-da6b-471f-b7ec-77a3f03338f9",
      "entity": "id:5aa7a676-73f7-4cd5-bcc3-8c24e71dd6e0"
    },
    {
      "@type": "Membership",
      "collection": "id:74500aa8-7eb8-4831-a5d7-b57b0d559a7f",
      "entity": "id:ef051260-da6b-471f-b7ec-77a3f03338f9"
    },
    {
      "@type": "Membership",
      "collection": "id:74500aa8-7eb8-4831-a5d7-b57b0d559a7f",
      "entity": "data:09b42388eb37be1a4b972127a78f691ec6eb3795"
    },
    {
      "@type": "Membership",
      "collection": "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3",
      "entity": "id:84fd2907-ae91-49e6-b896-5337cf88d4e4"
    },
    {
      "@type": "Membership",
      "collection": "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3",
      "entity": "id:c5bac52b-0236-4d46-9e95-2715e4ebb57f"
    },
    {
      "@type": "Membership",
      "collection": "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3",
      "entity": "id:8cae0f0e-8136-47a3-91de-2df4cb915caa"
    },
    {
      "@type": "Membership",
      "collection": "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3",
      "entity": "id:0b639232-1377-4260-9361-ccfad1f07653"
    },
    {
      "@type": "Membership",
      "collection": "id:3d909cf5-e433-4f42-a566-ecc18e8648ac",
      "entity": "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3"
    },
    {
      "@type": "Membership",
      "collection": "id:3d909cf5-e433-4f42-a566-ecc18e8648ac",
      "entity": "data:09b42388eb37be1a4b972127a78f691ec6eb3795"
    },
    {
      "@type": "Membership",
      "collection": "id:3efd1082-30b0-4081-aac3-595258d0235a",
      "entity": "id:1a78bcc2-8056-4262-8f95-eff699d2deeb"
    },
    {
      "@type": "Membership",
      "collection": "id:3efd1082-30b0-4081-aac3-595258d0235a",
      "entity": "id:311c03b4-81b7-421a-8cd4-b744019dc39b"
    },
    {
      "@type": "Membership",
      "collection": "id:3efd1082-30b0-4081-aac3-595258d0235a",
      "entity": "id:1ec302cf-1d77-48c8-9550-86945f3a70ef"
    },
    {
      "@type": "Membership",
      "collection": "id:3efd1082-30b0-4081-aac3-595258d0235a",
      "entity": "id:30f546f9-0831-4994-946d-88f0365ffd8a"
    },
    {
      "@type": "Membership",
      "collection": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
      "entity": "id:3efd1082-30b0-4081-aac3-595258d0235a"
    },
    {
      "@type": "Membership",
      "collection": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
      "entity": "id:204e8020-f340-4534-bcb6-378a06cfce69"
    },
    {
      "@type": "Usage",
      "activity": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "entity": "id:74500aa8-7eb8-4831-a5d7-b57b0d559a7f",
      "time": "2026-09-23T10:01:11.351399",
      "role": [
        "wf:main/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "entity": "id:d41afe53-37b5-4d07-a4d3-8f135d5ee9bd",
      "time": "2026-09-23T10:01:11.351432",
      "role": [
        "wf:main/cloud_cover_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "entity": "id:ab971800-6389-44da-a7db-d85c11161552",
      "time": "2026-09-23T10:01:11.351454",
      "role": [
        "wf:main/days_back"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "entity": "id:3d909cf5-e433-4f42-a566-ecc18e8648ac",
      "time": "2026-09-23T10:01:11.393353",
      "role": [
        "wf:main/parse_aoi/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "entity": "id:980cdadc-8748-4ee0-8e50-02285fada4ac",
      "time": "2026-09-23T10:01:12.503371",
      "role": [
        "wf:main/step_1/cloud_cover_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "entity": "id:cf0be29b-e4d9-4fd3-bd1b-2ed80a4095a9",
      "time": "2026-09-23T10:01:12.503410",
      "role": [
        "wf:main/step_1/days_back"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "entity": "id:43bb865a-d8cd-4787-8345-a30f5433a956",
      "time": "2026-09-23T10:01:12.503436",
      "role": [
        "wf:main/step_1/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "entity": "id:930cbb58-e736-4bd6-97e8-f8d6fdb3ecca",
      "time": "2026-09-23T10:01:12.503452",
      "role": [
        "wf:main/step_1/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "entity": "data:e71003c6b7dd4093ce139ac0c51a6ba38d54a439",
      "time": "2026-09-23T10:01:12.503865",
      "role": [
        "wf:main/step_1/output_dir"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "entity": "id:a98d2a32-f817-4ba9-9a35-66d4b22bc9de",
      "time": "2026-09-23T10:01:12.503886",
      "role": [
        "wf:main/step_1/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "entity": "id:d061c0fb-cd9b-4026-acea-7aa18b482246",
      "time": "2026-09-23T10:01:12.503903",
      "role": [
        "wf:main/step_1/west"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:100945f6-30da-4f24-8f5f-0cfe008c874a",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "time": "2026-09-23T10:01:12.461693",
      "role": [
        "wf:main/parse_aoi/east"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:f8e40067-1926-41f5-9278-ae93f18fb929",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "time": "2026-09-23T10:01:12.461693",
      "role": [
        "wf:main/parse_aoi/north"
      ]
    },
    {
      "@type": "Generation",
      "entity": "data:e71003c6b7dd4093ce139ac0c51a6ba38d54a439",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "time": "2026-09-23T10:01:12.461693",
      "role": [
        "wf:main/parse_aoi/output_dir"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:5c1c3ee6-0407-4b28-8b0e-1ea049c4f4aa",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "time": "2026-09-23T10:01:12.461693",
      "role": [
        "wf:main/parse_aoi/south"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:07e4c7e6-d84f-4db0-bbd5-dd80fb19c086",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "time": "2026-09-23T10:01:12.461693",
      "role": [
        "wf:main/parse_aoi/west"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "time": "2026-09-23T10:03:16.994705",
      "role": [
        "wf:main/step_1/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
      "activity": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "time": "2026-09-23T10:03:17.024364",
      "role": [
        "wf:main/primary/stac"
      ]
    },
    {
      "@type": "End",
      "activity": "id:a475ab91-5a11-4da1-8e90-fc280da2c643",
      "ender": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "time": "2026-09-23T10:01:12.461683"
    },
    {
      "@type": "End",
      "activity": "id:32497dfb-a6ea-4996-a29e-3700668da867",
      "ender": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "time": "2026-09-23T10:03:16.994695"
    },
    {
      "@type": "End",
      "activity": "id:ec5cc9e1-3e83-4551-a759-4745c5b5040b",
      "ender": "id:3ad94428-01ae-451b-a3f4-af56b73e6981",
      "time": "2026-09-23T10:03:17.024390"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1a78bcc2-8056-4262-8f95-eff699d2deeb",
      "generalEntity": "data:7e692955f3c119da05517da56423ef1afffeb3a1"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:311c03b4-81b7-421a-8cd4-b744019dc39b",
      "generalEntity": "data:85af35ec75b965fc1c515c5850cb53a81c919b22"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1ec302cf-1d77-48c8-9550-86945f3a70ef",
      "generalEntity": "data:85e5b7702d82de1bc19c00fdebce3e4b00d9ae4c"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:30f546f9-0831-4994-946d-88f0365ffd8a",
      "generalEntity": "data:de0d01dfb965345b5db12bd9c3701bd109aa9362"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:204e8020-f340-4534-bcb6-378a06cfce69",
      "generalEntity": "data:8eeff5d9360c12c34666e58c05819462f451c0cb"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d#ore",
      "generalEntity": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-570b17a1-1129-4b02-b2bc-a4675847cf5d.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3efd1082-30b0-4081-aac3-595258d0235a#ore",
      "generalEntity": "id:3efd1082-30b0-4081-aac3-595258d0235a",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-3efd1082-30b0-4081-aac3-595258d0235a.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-570b17a1-1129-4b02-b2bc-a4675847cf5d.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
          "type": [
            "ore:Aggregation",
            "ro:Folder"
          ],
          "ore:aggregates": [
            {
              "@value": "id:f6d74394-3b64-40fe-a8c1-7c63d02a3a5e",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:a9056b20-82a6-42a0-a8f8-13f831d67eb4",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:a9056b20-82a6-42a0-a8f8-13f831d67eb4",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "mangrove-analysis-20260923-080315"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:3efd1082-30b0-4081-aac3-595258d0235a",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:f6d74394-3b64-40fe-a8c1-7c63d02a3a5e",
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
              "@value": "id:570b17a1-1129-4b02-b2bc-a4675847cf5d",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:204e8020-f340-4534-bcb6-378a06cfce69",
              "@type": "xsd:QName"
            }
          ]
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-3efd1082-30b0-4081-aac3-595258d0235a.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:3efd1082-30b0-4081-aac3-595258d0235a",
          "type": [
            "ore:Aggregation",
            "ro:Folder"
          ],
          "ore:aggregates": [
            {
              "@value": "id:5cc84ac8-9c80-4fdd-9ec6-34906d34a5b9",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:33112eca-fd4d-4784-b9e2-ee97f20f8aec",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:beef0d3b-cdec-4f99-a497-ed54573e9aa0",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:d2617387-2a90-4dc3-8db3-0d71f8e3d6ef",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:5cc84ac8-9c80-4fdd-9ec6-34906d34a5b9",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "carbon_summary.csv"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:3efd1082-30b0-4081-aac3-595258d0235a",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:1a78bcc2-8056-4262-8f95-eff699d2deeb",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:d2617387-2a90-4dc3-8db3-0d71f8e3d6ef",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "mangrove-analysis-20260923-080315.json"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:3efd1082-30b0-4081-aac3-595258d0235a",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:311c03b4-81b7-421a-8cd4-b744019dc39b",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:beef0d3b-cdec-4f99-a497-ed54573e9aa0",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "biomass_summary.csv"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:3efd1082-30b0-4081-aac3-595258d0235a",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:1ec302cf-1d77-48c8-9550-86945f3a70ef",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:33112eca-fd4d-4784-b9e2-ee97f20f8aec",
          "type": [
            "ore:Proxy",
            "ro:FolderEntry"
          ],
          "ro:entryName": [
            {
              "@value": "mangrove_mask.tif"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:3efd1082-30b0-4081-aac3-595258d0235a",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:30f546f9-0831-4994-946d-88f0365ffd8a",
              "@type": "xsd:QName"
            }
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
@prefix metadata: <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/metadata/> .
@prefix ore: <http://www.openarchives.org/ore/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix provext: <https://openprovenance.org/ns/provext#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ro: <http://purl.org/wf4ever/ro#> .
@prefix wf: <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#> .
@prefix wf4ever: <http://purl.org/wf4ever/wf4ever#> .
@prefix wfdesc: <http://purl.org/wf4ever/wfdesc#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

metadata:directory-3efd1082-30b0-4081-aac3-595258d0235a.ttl a prov:Bundle .

metadata:directory-570b17a1-1129-4b02-b2bc-a4675847cf5d.ttl a prov:Bundle .

id:07e4c7e6-d84f-4db0-bbd5-dd80fb19c086 a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:a475ab91-5a11-4da1-8e90-fc280da2c643 ;
            prov:atTime "2026-09-23T10:01:12.461693"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi/west> ] ;
    prov:value 9.515e+01 .

id:100945f6-30da-4f24-8f5f-0cfe008c874a a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:a475ab91-5a11-4da1-8e90-fc280da2c643 ;
            prov:atTime "2026-09-23T10:01:12.461693"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi/east> ] ;
    prov:value 9.535e+01 .

id:33112eca-fd4d-4784-b9e2-ee97f20f8aec a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:30f546f9-0831-4994-946d-88f0365ffd8a"^^xsd:QName ;
    prov:pairKey "mangrove_mask.tif" .

<urn:uuid:3efd1082-30b0-4081-aac3-595258d0235a#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-3efd1082-30b0-4081-aac3-595258d0235a.ttl"^^xsd:QName ;
            provext:generalEntity id:3efd1082-30b0-4081-aac3-595258d0235a ] .

<urn:uuid:570b17a1-1129-4b02-b2bc-a4675847cf5d#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-570b17a1-1129-4b02-b2bc-a4675847cf5d.ttl"^^xsd:QName ;
            provext:generalEntity id:570b17a1-1129-4b02-b2bc-a4675847cf5d ] .

id:5c1c3ee6-0407-4b28-8b0e-1ea049c4f4aa a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:a475ab91-5a11-4da1-8e90-fc280da2c643 ;
            prov:atTime "2026-09-23T10:01:12.461693"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi/south> ] ;
    prov:value 1.59e+01 .

id:5cc84ac8-9c80-4fdd-9ec6-34906d34a5b9 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:1a78bcc2-8056-4262-8f95-eff699d2deeb"^^xsd:QName ;
    prov:pairKey "carbon_summary.csv" .

id:93ea57b4-1913-4209-a534-4f43acc9e037 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "data:09b42388eb37be1a4b972127a78f691ec6eb3795"^^xsd:QName ;
    prov:pairKey "crs" .

id:9dc1dc18-e01b-439a-818c-00162dabf4af a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3"^^xsd:QName ;
    prov:pairKey "bbox" .

id:a9056b20-82a6-42a0-a8f8-13f831d67eb4 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:3efd1082-30b0-4081-aac3-595258d0235a"^^xsd:QName ;
    prov:pairKey "mangrove-analysis-20260923-080315" .

id:beef0d3b-cdec-4f99-a497-ed54573e9aa0 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:1ec302cf-1d77-48c8-9550-86945f3a70ef"^^xsd:QName ;
    prov:pairKey "biomass_summary.csv" .

id:c78baf60-1897-4153-8e9c-e2eb311497b9 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "data:09b42388eb37be1a4b972127a78f691ec6eb3795"^^xsd:QName ;
    prov:pairKey "crs" .

id:d2617387-2a90-4dc3-8db3-0d71f8e3d6ef a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:311c03b4-81b7-421a-8cd4-b744019dc39b"^^xsd:QName ;
    prov:pairKey "mangrove-analysis-20260923-080315.json" .

id:d4edcbc8-d63f-4e4a-b8fe-e640258e0481 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:ef051260-da6b-471f-b7ec-77a3f03338f9"^^xsd:QName ;
    prov:pairKey "bbox" .

id:f6d74394-3b64-40fe-a8c1-7c63d02a3a5e a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:204e8020-f340-4534-bcb6-378a06cfce69"^^xsd:QName ;
    prov:pairKey "catalog.json" .

id:f8e40067-1926-41f5-9278-ae93f18fb929 a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:a475ab91-5a11-4da1-8e90-fc280da2c643 ;
            prov:atTime "2026-09-23T10:01:12.461693"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi/north> ] ;
    prov:value 1.61e+01 .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/parse_aoi"^^xsd:QName,
        "wf:main/step_1"^^xsd:QName .

<arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

data:7e692955f3c119da05517da56423ef1afffeb3a1 a wfprov:Artifact,
        prov:Entity .

data:85af35ec75b965fc1c515c5850cb53a81c919b22 a wfprov:Artifact,
        prov:Entity .

data:85e5b7702d82de1bc19c00fdebce3e4b00d9ae4c a wfprov:Artifact,
        prov:Entity .

data:8eeff5d9360c12c34666e58c05819462f451c0cb a wfprov:Artifact,
        prov:Entity .

data:de0d01dfb965345b5db12bd9c3701bd109aa9362 a wfprov:Artifact,
        prov:Entity .

data:e71003c6b7dd4093ce139ac0c51a6ba38d54a439 a wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:a475ab91-5a11-4da1-8e90-fc280da2c643 ;
            prov:atTime "2026-09-23T10:01:12.461693"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi/output_dir> ] ;
    prov:value "outputs" .

id:05148d8f-b41a-430e-ab3c-e47863420580 a prov:Entity ;
    prov:value 9.515e+01 .

id:0b639232-1377-4260-9361-ccfad1f07653 a prov:Entity ;
    prov:value 1.61e+01 .

id:1a78bcc2-8056-4262-8f95-eff699d2deeb a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:7e692955f3c119da05517da56423ef1afffeb3a1 ] ;
    cwlprov:basename "carbon_summary.csv" .

id:1ec302cf-1d77-48c8-9550-86945f3a70ef a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:85e5b7702d82de1bc19c00fdebce3e4b00d9ae4c ] ;
    cwlprov:basename "biomass_summary.csv" .

id:204e8020-f340-4534-bcb6-378a06cfce69 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8eeff5d9360c12c34666e58c05819462f451c0cb ] ;
    cwlprov:basename "catalog.json" .

id:30f546f9-0831-4994-946d-88f0365ffd8a a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:de0d01dfb965345b5db12bd9c3701bd109aa9362 ] ;
    cwlprov:basename "mangrove_mask.tif" .

id:311c03b4-81b7-421a-8cd4-b744019dc39b a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:85af35ec75b965fc1c515c5850cb53a81c919b22 ] ;
    cwlprov:basename "mangrove-analysis-20260923-080315.json" .

id:32497dfb-a6ea-4996-a29e-3700668da867 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/step_1" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:3ad94428-01ae-451b-a3f4-af56b73e6981 ;
            prov:hadPlan <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1> ],
        [ a prov:Association ;
            prov:agent id:a6977d92-2fbb-47e7-a784-4bfcb0da723b ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T10:03:16.994695"^^xsd:dateTime ;
            prov:hadActivity id:ec5cc9e1-3e83-4551-a759-4745c5b5040b ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T10:01:12.463948"^^xsd:dateTime ;
            prov:hadActivity id:ec5cc9e1-3e83-4551-a759-4745c5b5040b ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:12.503371"^^xsd:dateTime ;
            prov:entity id:980cdadc-8748-4ee0-8e50-02285fada4ac ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/cloud_cover_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:12.503452"^^xsd:dateTime ;
            prov:entity id:930cbb58-e736-4bd6-97e8-f8d6fdb3ecca ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:12.503436"^^xsd:dateTime ;
            prov:entity id:43bb865a-d8cd-4787-8345-a30f5433a956 ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:12.503410"^^xsd:dateTime ;
            prov:entity id:cf0be29b-e4d9-4fd3-bd1b-2ed80a4095a9 ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/days_back> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:12.503903"^^xsd:dateTime ;
            prov:entity id:d061c0fb-cd9b-4026-acea-7aa18b482246 ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:12.503865"^^xsd:dateTime ;
            prov:entity data:e71003c6b7dd4093ce139ac0c51a6ba38d54a439 ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/output_dir> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:12.503886"^^xsd:dateTime ;
            prov:entity id:a98d2a32-f817-4ba9-9a35-66d4b22bc9de ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/south> ] .

id:371c06f9-5e4f-482d-a56d-17457d592305 a prov:Entity ;
    prov:value 1.59e+01 .

id:3d6a2dea-df15-41de-943f-5c75ffc145fd a prov:Entity ;
    prov:value 9.535e+01 .

id:3d909cf5-e433-4f42-a566-ecc18e8648ac a wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    prov:hadDictionaryMember "id:9dc1dc18-e01b-439a-818c-00162dabf4af"^^xsd:QName,
        "id:c78baf60-1897-4153-8e9c-e2eb311497b9"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3 ],
        [ a provext:Membership ;
            provext:member data:09b42388eb37be1a4b972127a78f691ec6eb3795 ] .

id:43bb865a-d8cd-4787-8345-a30f5433a956 a prov:Entity ;
    prov:value 9.535e+01 .

id:570b17a1-1129-4b02-b2bc-a4675847cf5d a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-570b17a1-1129-4b02-b2bc-a4675847cf5d.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:a9056b20-82a6-42a0-a8f8-13f831d67eb4"^^xsd:QName,
        "id:f6d74394-3b64-40fe-a8c1-7c63d02a3a5e"^^xsd:QName ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:32497dfb-a6ea-4996-a29e-3700668da867 ;
            prov:atTime "2026-09-23T10:03:16.994705"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/step_1/result> ],
        [ a prov:Generation ;
            prov:activity id:ec5cc9e1-3e83-4551-a759-4745c5b5040b ;
            prov:atTime "2026-09-23T10:03:17.024364"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/primary/stac> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:3efd1082-30b0-4081-aac3-595258d0235a ],
        [ a provext:Membership ;
            provext:member id:204e8020-f340-4534-bcb6-378a06cfce69 ] ;
    cwlprov:basename "outputs" .

id:5aa7a676-73f7-4cd5-bcc3-8c24e71dd6e0 a prov:Entity ;
    prov:value 1.61e+01 .

id:639b3f31-e75a-4bcb-891c-0a3a8d2301e3 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:c5bac52b-0236-4d46-9e95-2715e4ebb57f ],
        [ a provext:Membership ;
            provext:member id:0b639232-1377-4260-9361-ccfad1f07653 ],
        [ a provext:Membership ;
            provext:member id:84fd2907-ae91-49e6-b896-5337cf88d4e4 ],
        [ a provext:Membership ;
            provext:member id:8cae0f0e-8136-47a3-91de-2df4cb915caa ] .

id:74500aa8-7eb8-4831-a5d7-b57b0d559a7f a wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    prov:hadDictionaryMember "id:93ea57b4-1913-4209-a534-4f43acc9e037"^^xsd:QName,
        "id:d4edcbc8-d63f-4e4a-b8fe-e640258e0481"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:09b42388eb37be1a4b972127a78f691ec6eb3795 ],
        [ a provext:Membership ;
            provext:member id:ef051260-da6b-471f-b7ec-77a3f03338f9 ] .

id:84fd2907-ae91-49e6-b896-5337cf88d4e4 a prov:Entity ;
    prov:value 9.515e+01 .

id:8cae0f0e-8136-47a3-91de-2df4cb915caa a prov:Entity ;
    prov:value 9.535e+01 .

id:930cbb58-e736-4bd6-97e8-f8d6fdb3ecca a prov:Entity ;
    prov:value 1.61e+01 .

id:980cdadc-8748-4ee0-8e50-02285fada4ac a prov:Entity ;
    prov:value "20"^^xsd:int .

id:a6977d92-2fbb-47e7-a784-4bfcb0da723b a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/mangrove-cwl:v0.0.1-rc7" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/mangrove-cwl:v0.0.1-rc7" .

id:a98d2a32-f817-4ba9-9a35-66d4b22bc9de a prov:Entity ;
    prov:value 1.59e+01 .

id:ab971800-6389-44da-a7db-d85c11161552 a prov:Entity ;
    prov:value "90"^^xsd:int .

id:aef78493-9502-4ecb-9d44-f04f881f4650 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image alpine:3.22.2" ;
    cwlprov:image "alpine:3.22.2" .

id:c5bac52b-0236-4d46-9e95-2715e4ebb57f a prov:Entity ;
    prov:value 1.59e+01 .

id:cf0be29b-e4d9-4fd3-bd1b-2ed80a4095a9 a prov:Entity ;
    prov:value "90"^^xsd:int .

id:d061c0fb-cd9b-4026-acea-7aa18b482246 a prov:Entity ;
    prov:value 9.515e+01 .

id:d41afe53-37b5-4d07-a4d3-8f135d5ee9bd a prov:Entity ;
    prov:value "20"^^xsd:int .

id:e6ce2559-8946-4151-834e-df99641e6f0b a prov:Agent .

id:ef051260-da6b-471f-b7ec-77a3f03338f9 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:371c06f9-5e4f-482d-a56d-17457d592305 ],
        [ a provext:Membership ;
            provext:member id:05148d8f-b41a-430e-ab3c-e47863420580 ],
        [ a provext:Membership ;
            provext:member id:3d6a2dea-df15-41de-943f-5c75ffc145fd ],
        [ a provext:Membership ;
            provext:member id:5aa7a676-73f7-4cd5-bcc3-8c24e71dd6e0 ] .

data:09b42388eb37be1a4b972127a78f691ec6eb3795 a wfprov:Artifact,
        prov:Entity ;
    prov:value "CRS84" .

id:3efd1082-30b0-4081-aac3-595258d0235a a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-3efd1082-30b0-4081-aac3-595258d0235a.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:33112eca-fd4d-4784-b9e2-ee97f20f8aec"^^xsd:QName,
        "id:5cc84ac8-9c80-4fdd-9ec6-34906d34a5b9"^^xsd:QName,
        "id:beef0d3b-cdec-4f99-a497-ed54573e9aa0"^^xsd:QName,
        "id:d2617387-2a90-4dc3-8db3-0d71f8e3d6ef"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:1ec302cf-1d77-48c8-9550-86945f3a70ef ],
        [ a provext:Membership ;
            provext:member id:1a78bcc2-8056-4262-8f95-eff699d2deeb ],
        [ a provext:Membership ;
            provext:member id:311c03b4-81b7-421a-8cd4-b744019dc39b ],
        [ a provext:Membership ;
            provext:member id:30f546f9-0831-4994-946d-88f0365ffd8a ] ;
    cwlprov:basename "mangrove-analysis-20260923-080315" .

id:3ad94428-01ae-451b-a3f4-af56b73e6981 a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T10:01:10.962414"^^xsd:dateTime ;
            prov:hadActivity id:e6ce2559-8946-4151-834e-df99641e6f0b ] .

id:a475ab91-5a11-4da1-8e90-fc280da2c643 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/parse_aoi" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:aef78493-9502-4ecb-9d44-f04f881f4650 ],
        [ a prov:Association ;
            prov:agent id:3ad94428-01ae-451b-a3f4-af56b73e6981 ;
            prov:hadPlan <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T10:01:12.461683"^^xsd:dateTime ;
            prov:hadActivity id:ec5cc9e1-3e83-4551-a759-4745c5b5040b ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T10:01:11.352398"^^xsd:dateTime ;
            prov:hadActivity id:ec5cc9e1-3e83-4551-a759-4745c5b5040b ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:11.393353"^^xsd:dateTime ;
            prov:entity id:3d909cf5-e433-4f42-a566-ecc18e8648ac ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/parse_aoi/aoi> ] .

id:ec5cc9e1-3e83-4551-a759-4745c5b5040b a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:3ad94428-01ae-451b-a3f4-af56b73e6981 ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T10:03:17.024390"^^xsd:dateTime ;
            prov:hadActivity id:3ad94428-01ae-451b-a3f4-af56b73e6981 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T10:01:10.962463"^^xsd:dateTime ;
            prov:hadActivity id:3ad94428-01ae-451b-a3f4-af56b73e6981 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:11.351399"^^xsd:dateTime ;
            prov:entity id:74500aa8-7eb8-4831-a5d7-b57b0d559a7f ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:11.351454"^^xsd:dateTime ;
            prov:entity id:ab971800-6389-44da-a7db-d85c11161552 ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/days_back> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T10:01:11.351432"^^xsd:dateTime ;
            prov:entity id:d41afe53-37b5-4d07-a4d3-8f135d5ee9bd ;
            prov:hadRole <arcp://uuid,ec5cc9e1-3e83-4551-a759-4745c5b5040b/workflow/packed.cwl#main/cloud_cover_max> ] ;
    prov:startedAtTime "2026-09-23T10:01:10.962438"^^xsd:dateTime .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `mangrove-workflow`
  (CWL Workflow). Pins the process id and the input/output names; the input/output
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
      const: mangrove-workflow
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - cloud_cover_max
      - days_back
      - aoi
      propertyNames:
        enum:
        - cloud_cover_max
        - days_back
        - aoi
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - stac
      propertyNames:
        enum:
        - stac
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
        - cloud_cover_max
        - days_back
        - aoi
        propertyNames:
          enum:
          - cloud_cover_max
          - days_back
          - aoi
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
          - stac
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
      - stac
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
  execution:
    $ref: https://geolabs.github.io/bblocks-generic-provenance-profile/build/annotated/bbr/provenance/execution/schema.yaml
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove/mangrove-workflow/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/kindgrove/mangrove-workflow`

