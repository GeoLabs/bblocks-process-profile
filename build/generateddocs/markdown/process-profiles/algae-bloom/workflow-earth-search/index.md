
# Process profile: algae-usecase-workflow-earth-search (Schema)

`ospd.process-profiles.algae-bloom.workflow-earth-search` *v0.1*

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-earth-search` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`algae-usecase-workflow-earth-search`** (Workflow, W1 Algae Bloom).

> Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.

## Source

- CWL: [algae-usecase-workflow-earth-search.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Filter configuration → Selection / filtering → Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.geojson`, `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.algae-bloom.select-products-sentinel2`, `ospd.process-profiles.algae-bloom.workflow-earth-search-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `date` | string? | `chlorophyll_a` | File[] |
| `delta` | int? | `chlorophyll_a_color` | File[] |
| `toi` | string[]? | `chlorophyll_a_plot` | File[] |
| `aoi` | File | `cyanobacteria` | File[] |
| `collection` | string | `cyanobacteria_color` | File[] |
| `cloud_cover` | double? | `cyanobacteria_plot` | File[] |
|  |  | `turbidity` | File[] |
|  |  | `turbidity_color` | File[] |
|  |  | `turbidity_plot` | File[] |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite: a CWL Workflow scattering a per-product subworkflow over the product list. The openEO equivalent would be a user-defined process graph, which has no Building Block of its own; the correspondence is carried by the steps.


| Stage | openEO | Level | Note |
|---|---|---|---|
| select_products | `ogc.openeo.processes.cubes.load_collection` | closeMatch |  |
| process (scatter over urls) | — | none | openEO has no scatter over products; a collection is loaded as one data cube. |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL Workflow is referenced, not copied: <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl>.

### processDescription
OGC API - Processes processDescription derived from the CWL.
#### json
```json
{
  "id": "algae-usecase-workflow-earth-search",
  "version": "2.0.0",
  "title": "Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.\n",
  "description": "Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters\nand performs band calculation on matched Sentinel-2 products to evaluate algae bloom\nfor water quality assessment. For each match, reference bands are downloaded, processed,\nand returned as output with raw data, color map and plot visualization. Each output file\nwill be named with the ID of the original product to distinguish them in case of multiple matches.\n",
  "mutable": true,
  "keywords": [
    "water-quality",
    "algae-bloom",
    "earth-search",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters\nand performs band calculation on matched Sentinel-2 products to evaluate algae bloom\nfor water quality assessment. For each match, reference bands are downloaded, processed,\nand returned as output with raw data, color map and plot visualization. Each output file\nwill be named with the ID of the original product to distinguish them in case of multiple matches.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "2.0.0"
    },
    {
      "role": "https://schema.org/author",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "identifier": "http://orcid.org/0000-0003-4862-3349",
        "email": "francis.charette-migneault@crim.ca",
        "name": "Francis Charette-Migneault"
      }
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://gitlab.ogc.org/ogc/ogc-ospd"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
    }
  ],
  "inputs": {
    "date": {
      "title": "Central date",
      "description": "Date around which ±delta-days will be applied for search. If omitted, 'toi' input must be provided instead.",
      "schema": {
        "type": "string"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "delta": {
      "title": "delta",
      "description": "",
      "schema": {
        "type": "integer",
        "default": 4
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "toi": {
      "title": "Time of interest",
      "description": "Start and end date-time strings. Must be provided if 'date' input is omitted.",
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "Area of interest",
      "description": "Polygon defining the area of interest.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/geo+json",
        "contentEncoding": "binary"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "collection": {
      "title": "collection",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "cloud_cover": {
      "title": "cloud_cover",
      "description": "",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "chlorophyll_a": {
      "title": "chlorophyll_a",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "chlorophyll_a_color": {
      "title": "chlorophyll_a_color",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "chlorophyll_a_plot": {
      "title": "chlorophyll_a_plot",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/png",
          "contentEncoding": "binary"
        }
      }
    },
    "cyanobacteria": {
      "title": "cyanobacteria",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "cyanobacteria_color": {
      "title": "cyanobacteria_color",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "cyanobacteria_plot": {
      "title": "cyanobacteria_plot",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/png",
          "contentEncoding": "binary"
        }
      }
    },
    "turbidity": {
      "title": "turbidity",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "turbidity_color": {
      "title": "turbidity_color",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "turbidity_plot": {
      "title": "turbidity_plot",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/png",
          "contentEncoding": "binary"
        }
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld",
  "id": "algae-usecase-workflow-earth-search",
  "version": "2.0.0",
  "title": "Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.\n",
  "description": "Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters\nand performs band calculation on matched Sentinel-2 products to evaluate algae bloom\nfor water quality assessment. For each match, reference bands are downloaded, processed,\nand returned as output with raw data, color map and plot visualization. Each output file\nwill be named with the ID of the original product to distinguish them in case of multiple matches.\n",
  "mutable": true,
  "keywords": [
    "water-quality",
    "algae-bloom",
    "earth-search",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters\nand performs band calculation on matched Sentinel-2 products to evaluate algae bloom\nfor water quality assessment. For each match, reference bands are downloaded, processed,\nand returned as output with raw data, color map and plot visualization. Each output file\nwill be named with the ID of the original product to distinguish them in case of multiple matches.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "2.0.0"
    },
    {
      "role": "https://schema.org/author",
      "value": {
        "@context": "https://schema.org",
        "@type": "Person",
        "identifier": "http://orcid.org/0000-0003-4862-3349",
        "email": "francis.charette-migneault@crim.ca",
        "name": "Francis Charette-Migneault"
      }
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://gitlab.ogc.org/ogc/ogc-ospd"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
    }
  ],
  "inputs": {
    "date": {
      "title": "Central date",
      "description": "Date around which \u00b1delta-days will be applied for search. If omitted, 'toi' input must be provided instead.",
      "schema": {
        "type": "string"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "delta": {
      "title": "delta",
      "description": "",
      "schema": {
        "type": "integer",
        "default": 4
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "toi": {
      "title": "Time of interest",
      "description": "Start and end date-time strings. Must be provided if 'date' input is omitted.",
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "aoi": {
      "title": "Area of interest",
      "description": "Polygon defining the area of interest.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/geo+json",
        "contentEncoding": "binary"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "collection": {
      "title": "collection",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "cloud_cover": {
      "title": "cloud_cover",
      "description": "",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "chlorophyll_a": {
      "title": "chlorophyll_a",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "chlorophyll_a_color": {
      "title": "chlorophyll_a_color",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "chlorophyll_a_plot": {
      "title": "chlorophyll_a_plot",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/png",
          "contentEncoding": "binary"
        }
      }
    },
    "cyanobacteria": {
      "title": "cyanobacteria",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "cyanobacteria_color": {
      "title": "cyanobacteria_color",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "cyanobacteria_plot": {
      "title": "cyanobacteria_plot",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/png",
          "contentEncoding": "binary"
        }
      }
    },
    "turbidity": {
      "title": "turbidity",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "turbidity_color": {
      "title": "turbidity_color",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/tiff; application=geotiff",
          "contentEncoding": "binary"
        }
      }
    },
    "turbidity_plot": {
      "title": "turbidity_plot",
      "description": "",
      "schema": {
        "type": "array",
        "items": {
          "type": "string",
          "contentMediaType": "image/png",
          "contentEncoding": "binary"
        }
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
@prefix ns2: <http://schema.org/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-earth-search> dcterms:description """Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters
and performs band calculation on matched Sentinel-2 products to evaluate algae bloom
for water quality assessment. For each match, reference bands are downloaded, processed,
and returned as output with raw data, color map and plot visualization. Each output file
will be named with the ID of the original product to distinguish them in case of multiple matches.
""" ;
    dcterms:subject "OSPD",
        "algae-bloom",
        "demo",
        "earth-search",
        "water-quality" ;
    dcterms:title """Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.
""" ;
    pp:version "2.0.0" ;
    proc:inputs [ ns4:aoi [ dcterms:description "Polygon defining the area of interest." ;
                    dcterms:title "Area of interest" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns1:contentEncoding "binary" ;
                            ns1:contentMediaType "application/geo+json" ] ] ;
            ns4:cloud_cover [ dcterms:description "" ;
                    dcterms:title "cloud_cover" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns4:collection [ dcterms:description "" ;
                    dcterms:title "collection" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns4:date [ dcterms:description "Date around which ±delta-days will be applied for search. If omitted, 'toi' input must be provided instead." ;
                    dcterms:title "Central date" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns4:delta [ dcterms:description "" ;
                    dcterms:title "delta" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "4"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns4:toi [ dcterms:description "Start and end date-time strings. Must be provided if 'date' input is omitted." ;
                    dcterms:title "Time of interest" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ] ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value """Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.
""" ;
            proc:role schema:name ],
        [ rdf:value "2.0.0" ;
            proc:role schema:softwareVersion ],
        [ rdf:value [ a ns2:Person ;
                    ns2:email "francis.charette-migneault@crim.ca" ;
                    ns2:identifier "http://orcid.org/0000-0003-4862-3349" ;
                    ns2:name "Francis Charette-Migneault" ] ;
            proc:role schema:author ],
        [ rdf:value "https://gitlab.ogc.org/ogc/ogc-ospd" ;
            proc:role schema:codeRepository ],
        [ rdf:value """Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters
and performs band calculation on matched Sentinel-2 products to evaluate algae bloom
for water quality assessment. For each match, reference bands are downloaded, processed,
and returned as output with raw data, color map and plot visualization. Each output file
will be named with the ID of the original product to distinguish them in case of multiple matches.
""" ;
            proc:role schema:description ],
        [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:chlorophyll_a [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:chlorophyll_a_color [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a_color" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:chlorophyll_a_plot [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:cyanobacteria [ dcterms:description "" ;
                    dcterms:title "cyanobacteria" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:cyanobacteria_color [ dcterms:description "" ;
                    dcterms:title "cyanobacteria_color" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:cyanobacteria_plot [ dcterms:description "" ;
                    dcterms:title "cyanobacteria_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns3:turbidity [ dcterms:description "" ;
                    dcterms:title "turbidity" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:turbidity_color [ dcterms:description "" ;
                    dcterms:title "turbidity_color" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:turbidity_plot [ dcterms:description "" ;
                    dcterms:title "turbidity_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/png" ] ] ] ] .


```


### OGC Application Package (deploy)
Part 2 deploy body: the execution unit is a link to the pinned CWL.
#### json
```json
{
  "processDescription": {
    "process": {
      "id": "algae-usecase-workflow-earth-search",
      "version": "2.0.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld",
  "processDescription": {
    "process": {
      "id": "algae-usecase-workflow-earth-search",
      "version": "2.0.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-earth-search> pp:version "2.0.0" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-earth-search> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl" ;
            pp:rel "http://www.opengis.net/def/rel/ogc/1.0/executionUnit" ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "aoi": {
      "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson",
      "type": "application/geo+json"
    },
    "collection": "sentinel-2-l2a",
    "toi": [
      "2019-06-25",
      "2019-07-03"
    ],
    "delta": 4,
    "cloud_cover": 0.1
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld",
  "inputs": {
    "aoi": {
      "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson",
      "type": "application/geo+json"
    },
    "collection": "sentinel-2-l2a",
    "toi": [
      "2019-06-25",
      "2019-07-03"
    ],
    "delta": 4,
    "cloud_cover": 0.1
  },
  "response": "document"
}
```

#### ttl
```ttl
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] proc:inputs [ ns1:aoi [ ns1:href "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson" ;
                    proc:type "application/geo+json" ] ;
            ns1:cloud_cover 1e-01 ;
            ns1:collection "sentinel-2-l2a" ;
            ns1:delta 4 ;
            ns1:toi "2019-06-25",
                "2019-07-03" ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "chlorophyll_a": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png",
      "type": "image/png"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png",
      "type": "image/png"
    }
  ],
  "cyanobacteria": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png",
      "type": "image/png"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png",
      "type": "image/png"
    }
  ],
  "turbidity": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png",
      "type": "image/png"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
      "type": "image/png"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld",
  "chlorophyll_a": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png",
      "type": "image/png"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png",
      "type": "image/png"
    }
  ],
  "cyanobacteria": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png",
      "type": "image/png"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png",
      "type": "image/png"
    }
  ],
  "turbidity": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif",
      "type": "image/tiff; application=geotiff"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png",
      "type": "image/png"
    },
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
      "type": "image/png"
    }
  ]
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:chlorophyll_a [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff" ] ;
    pp:chlorophyll_a_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif" ] ;
    pp:chlorophyll_a_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png" ],
        [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png" ] ;
    pp:cyanobacteria [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff" ] ;
    pp:cyanobacteria_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif" ] ;
    pp:cyanobacteria_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png" ],
        [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png" ] ;
    pp:turbidity [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff" ] ;
    pp:turbidity_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif" ],
        [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif" ] ;
    pp:turbidity_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png" ],
        [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:algae-bloom:workflow-earth-search",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search",
    "startedAtTime": "2026-09-23T06:26:24Z",
    "used": [
      "urn:example:entity:workflow-earth-search:in:aoi",
      "urn:example:entity:workflow-earth-search:in:collection",
      "urn:example:entity:workflow-earth-search:in:toi",
      "urn:example:entity:workflow-earth-search:in:delta",
      "urn:example:entity:workflow-earth-search:in:cloud_cover"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search"
      }
    ],
    "endedAtTime": "2026-09-23T06:40:34Z"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:in:aoi",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/aoi",
    "links": [
      {
        "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson",
        "rel": "item",
        "type": "application/geo+json"
      }
    ]
  },
  {
    "id": "urn:example:entity:workflow-earth-search:in:collection",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/collection",
    "value": "sentinel-2-l2a"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:in:toi",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/toi",
    "value": [
      "2019-06-25",
      "2019-07-03"
    ]
  },
  {
    "id": "urn:example:entity:workflow-earth-search:in:delta",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/delta",
    "value": 4
  },
  {
    "id": "urn:example:entity:workflow-earth-search:in:cloud_cover",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/cloud_cover",
    "value": 0.1
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:chlorophyll_a",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:chlorophyll_a_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:chlorophyll_a_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png",
        "rel": "item",
        "type": "image/png"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png",
        "rel": "item",
        "type": "image/png"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:cyanobacteria",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:cyanobacteria_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:cyanobacteria_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png",
        "rel": "item",
        "type": "image/png"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png",
        "rel": "item",
        "type": "image/png"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:turbidity",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:turbidity_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-earth-search:out:turbidity_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-earth-search:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png",
        "rel": "item",
        "type": "image/png"
      },
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
        "rel": "item",
        "type": "image/png"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:algae-bloom:workflow-earth-search",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search",
      "startedAtTime": "2026-09-23T06:26:24Z",
      "used": [
        "urn:example:entity:workflow-earth-search:in:aoi",
        "urn:example:entity:workflow-earth-search:in:collection",
        "urn:example:entity:workflow-earth-search:in:toi",
        "urn:example:entity:workflow-earth-search:in:delta",
        "urn:example:entity:workflow-earth-search:in:cloud_cover"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search"
        }
      ],
      "endedAtTime": "2026-09-23T06:40:34Z"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:in:aoi",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/aoi",
      "links": [
        {
          "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson",
          "rel": "item",
          "type": "application/geo+json"
        }
      ]
    },
    {
      "id": "urn:example:entity:workflow-earth-search:in:collection",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/collection",
      "value": "sentinel-2-l2a"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:in:toi",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/toi",
      "value": [
        "2019-06-25",
        "2019-07-03"
      ]
    },
    {
      "id": "urn:example:entity:workflow-earth-search:in:delta",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/delta",
      "value": 4
    },
    {
      "id": "urn:example:entity:workflow-earth-search:in:cloud_cover",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/cloud_cover",
      "value": 0.1
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:chlorophyll_a",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:chlorophyll_a_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:chlorophyll_a_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png",
          "rel": "item",
          "type": "image/png"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png",
          "rel": "item",
          "type": "image/png"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:cyanobacteria",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:cyanobacteria_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:cyanobacteria_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png",
          "rel": "item",
          "type": "image/png"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png",
          "rel": "item",
          "type": "image/png"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:turbidity",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:turbidity_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-earth-search:out:turbidity_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-earth-search",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-earth-search:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png",
          "rel": "item",
          "type": "image/png"
        },
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
          "rel": "item",
          "type": "image/png"
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

<urn:example:entity:workflow-earth-search:out:chlorophyll_a> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff> ],
        [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:chlorophyll_a_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif> ],
        [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:chlorophyll_a_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png> ],
        [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:cyanobacteria> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff> ],
        [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:cyanobacteria_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif> ],
        [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:cyanobacteria_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png> ],
        [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:turbidity> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff> ],
        [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:turbidity_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif> ],
        [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:out:turbidity_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png> ],
        [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-earth-search:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-earth-search> .

<urn:example:entity:workflow-earth-search:in:cloud_cover> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/cloud_cover> ;
    rdf:value 1e-01 .

<urn:example:entity:workflow-earth-search:in:collection> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/collection> ;
    rdf:value "sentinel-2-l2a" .

<urn:example:entity:workflow-earth-search:in:delta> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/delta> ;
    rdf:value 4 .

<urn:example:entity:workflow-earth-search:in:toi> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/toi> ;
    rdf:value "2019-06-25",
        "2019-07-03" .

<urn:example:run:algae-bloom:workflow-earth-search> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search> ;
    prov:endedAtTime "2026-09-23T06:40:34+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search> ] ;
    prov:startedAtTime "2026-09-23T06:26:24+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:workflow-earth-search:in:aoi>,
        <urn:example:entity:workflow-earth-search:in:cloud_cover>,
        <urn:example:entity:workflow-earth-search:in:collection>,
        <urn:example:entity:workflow-earth-search:in:delta>,
        <urn:example:entity:workflow-earth-search:in:toi> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .

<urn:example:entity:workflow-earth-search:in:aoi> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#inputs/aoi> ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson> ] .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Execution bundle (generic provenance profile)
#### json
```json
{
  "run": {
    "id": "urn:example:run:algae-bloom:workflow-earth-search",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "algae-bloom-workflow-earth-search-0001",
    "startedAtTime": "2026-09-23T06:26:24Z",
    "endedAtTime": "2026-09-23T06:40:34Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:algae-bloom:select-products-sentinel2"
      },
      {
        "id": "urn:example:run:algae-bloom:workflow-earth-search-process"
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
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "32ae8712ff4f8b8b6b34af45257c41c16474dc98"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "6947846b1796dd6e940e390f61208a85f45117b0"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "fb8e7e26b282372c29a35ac739498699e02006a5"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "e6874b008b758679af8241dfbfb355b204b131b2"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "38185787e3c54223cfadb4c26c22b126ad624d21"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1224781c8a82490664559a3b2e66fa3e14e09956"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "a0b94d0cf953df1bb6e7f4005e31908be982ccf8"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "065539f1417b6c8066de9420c143413de2cbcd97"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "88d67511003f18c13b7cdc982f5796ab5ae261fc"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "ee28bfbb1143c5e869cc07962f87b8cfac6106f6"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "876c7b4d7381ac5660a4507292c9324eb295a297"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "3822adba1b42a347ef376f9ac0e7259d0ba82b22"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "c50376cb72b65a0dad365279023daa2af7208fc9"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "a2beee36554454e4c0090480d062bc893f3ae7cc"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "c991e2bc239887ca885b02cab5fdae42c90a2889"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "8088de425841559ae78ca6328ecdf8bb0fe578d4"
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld",
  "run": {
    "id": "urn:example:run:algae-bloom:workflow-earth-search",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "algae-bloom-workflow-earth-search-0001",
    "startedAtTime": "2026-09-23T06:26:24Z",
    "endedAtTime": "2026-09-23T06:40:34Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:algae-bloom:select-products-sentinel2"
      },
      {
        "id": "urn:example:run:algae-bloom:workflow-earth-search-process"
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
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "32ae8712ff4f8b8b6b34af45257c41c16474dc98"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "6947846b1796dd6e940e390f61208a85f45117b0"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "fb8e7e26b282372c29a35ac739498699e02006a5"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "e6874b008b758679af8241dfbfb355b204b131b2"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "38185787e3c54223cfadb4c26c22b126ad624d21"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1224781c8a82490664559a3b2e66fa3e14e09956"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "a0b94d0cf953df1bb6e7f4005e31908be982ccf8"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "065539f1417b6c8066de9420c143413de2cbcd97"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "88d67511003f18c13b7cdc982f5796ab5ae261fc"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "ee28bfbb1143c5e869cc07962f87b8cfac6106f6"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "876c7b4d7381ac5660a4507292c9324eb295a297"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "3822adba1b42a347ef376f9ac0e7259d0ba82b22"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "c50376cb72b65a0dad365279023daa2af7208fc9"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "a2beee36554454e4c0090480d062bc893f3ae7cc"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "c991e2bc239887ca885b02cab5fdae42c90a2889"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-earth-search",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "8088de425841559ae78ca6328ecdf8bb0fe578d4"
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

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "6947846b1796dd6e940e390f61208a85f45117b0" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "e6874b008b758679af8241dfbfb355b204b131b2" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "1224781c8a82490664559a3b2e66fa3e14e09956" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "065539f1417b6c8066de9420c143413de2cbcd97" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "ee28bfbb1143c5e869cc07962f87b8cfac6106f6" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "3822adba1b42a347ef376f9ac0e7259d0ba82b22" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "c50376cb72b65a0dad365279023daa2af7208fc9" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "a2beee36554454e4c0090480d062bc893f3ae7cc" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "8088de425841559ae78ca6328ecdf8bb0fe578d4" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "32ae8712ff4f8b8b6b34af45257c41c16474dc98" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "fb8e7e26b282372c29a35ac739498699e02006a5" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "38185787e3c54223cfadb4c26c22b126ad624d21" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/chlorophyll_a_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "a0b94d0cf953df1bb6e7f4005e31908be982ccf8" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "88d67511003f18c13b7cdc982f5796ab5ae261fc" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "876c7b4d7381ac5660a4507292c9324eb295a297" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/cyanobacteria_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-earth-search> ;
    ns1:checksum [ rdf:value "c991e2bc239887ca885b02cab5fdae42c90a2889" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search#outputs/turbidity_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<urn:example:engine:cwltool-3.1.20260108082145> a wfprov:WorkflowEngine ;
    pp:name "cwltool" ;
    pp:version "3.1.20260108082145" .

<urn:example:run:algae-bloom:workflow-earth-search> a wfprov:WorkflowRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search> ;
    wfprov:describedByWorkflow <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-earth-search> ;
    wfprov:hadSubProcessRun <urn:example:run:algae-bloom:select-products-sentinel2>,
        <urn:example:run:algae-bloom:workflow-earth-search-process> ;
    prov:endedAtTime "2026-09-23T06:40:34+00:00"^^xsd:dateTime ;
    prov:startedAtTime "2026-09-23T06:26:24+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:jobID "algae-bloom-workflow-earth-search-0001" ;
    pp:status "successful" .

[] pp:engine <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:run <urn:example:run:algae-bloom:workflow-earth-search> ;
    proc:outputs <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-earth-search-0001/results/S2A_29SPC_20190701_1_L2A_turbidity_plot.png> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search",
  "type": "ProcessType",
  "prefLabel": "Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.",
  "definition": "Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters and performs band calculation on matched Sentinel-2 products to evaluate algae bloom for water quality assessment. For each match, reference bands are downloaded, processed, and returned as output with raw data, color map and plot visualization. Each output file will be named with the ID of the original product to distinguish them in case of multiple matches.",
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
  "profile": "ospd.process-profiles.algae-bloom.workflow-earth-search",
  "processDescription": {
    "id": "algae-usecase-workflow-earth-search",
    "version": "2.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl",
    "cwlClass": "Workflow",
    "cwlId": "algae-usecase-workflow-earth-search",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#WorkflowRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.geojson",
    "eoap.cct.string-format"
  ],
  "hasStep": [
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/select-products-sentinel2",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search-process"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite: a CWL Workflow scattering a per-product subworkflow over the product list. The openEO equivalent would be a user-defined process graph, which has no Building Block of its own; the correspondence is carried by the steps.",
    "decomposition": [
      {
        "stage": "select_products",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "process (scatter over urls)",
        "openeo": [],
        "level": "none",
        "note": "openEO has no scatter over products; a collection is loaded as one data cube."
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search",
  "type": "ProcessType",
  "prefLabel": "Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.",
  "definition": "Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters and performs band calculation on matched Sentinel-2 products to evaluate algae bloom for water quality assessment. For each match, reference bands are downloaded, processed, and returned as output with raw data, color map and plot visualization. Each output file will be named with the ID of the original product to distinguish them in case of multiple matches.",
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
  "profile": "ospd.process-profiles.algae-bloom.workflow-earth-search",
  "processDescription": {
    "id": "algae-usecase-workflow-earth-search",
    "version": "2.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl",
    "cwlClass": "Workflow",
    "cwlId": "algae-usecase-workflow-earth-search",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#WorkflowRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.geojson",
    "eoap.cct.string-format"
  ],
  "hasStep": [
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/select-products-sentinel2",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search-process"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite: a CWL Workflow scattering a per-product subworkflow over the product list. The openEO equivalent would be a user-defined process graph, which has no Building Block of its own; the correspondence is carried by the steps.",
    "decomposition": [
      {
        "stage": "select_products",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "process (scatter over urls)",
        "openeo": [],
        "level": "none",
        "note": "openEO has no scatter over products; a collection is loaded as one data cube."
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

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> ;
    skos:definition "Searches for Sentinel-2 L2A products on Earth-Search using filtering parameters and performs band calculation on matched Sentinel-2 products to evaluate algae bloom for water quality assessment. For each match, reference bands are downloaded, processed, and returned as output with raw data, color map and plot visualization. Each output file will be named with the ID of the original product to distinguish them in case of multiple matches." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform." ;
    pp:candidateCctDependency "eoap.cct.geojson",
        "eoap.cct.string-format" ;
    pp:hasStep <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/select-products-sentinel2>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-earth-search-process> ;
    pp:openeoEquivalence [ pp:decomposition ( [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.load_collection" ;
                        pp:stage "select_products" ] [ skos:note "openEO has no scatter over products; a collection is loaded as one data cube." ;
                        pp:equivalenceLevel "none" ;
                        pp:stage "process (scatter over urls)" ] ) ;
            pp:equivalenceLevel "none" ;
            pp:rationale "Composite: a CWL Workflow scattering a per-product subworkflow over the product list. The openEO equivalent would be a user-defined process graph, which has no Building Block of its own; the correspondence is carried by the steps." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-earth-search> ;
    pp:profile "ospd.process-profiles.algae-bloom.workflow-earth-search" ;
    pp:provenanceClass wfprov:WorkflowRun ;
    pp:source [ pp:cwl <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-earth-search.cwl> ;
            pp:cwlClass "Workflow" ;
            pp:cwlId "algae-usecase-workflow-earth-search" ;
            pp:license "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-earth-search> pp:version "2.0.0" .


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
      "researchobject": "arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/",
      "metadata": "arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/metadata/",
      "provenance": "arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/metadata/provenance/",
      "wf": "arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#",
      "input": "arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/primary-job.json#",
      "wf4ever": "http://purl.org/wf4ever/wf4ever#"
    },
    "https://openprovenance.org/prov-jsonld/context.jsonld"
  ],
  "@graph": [
    {
      "@type": "Agent",
      "@id": "id:9e986cfd-629d-41cf-9c75-eb65ae428d71"
    },
    {
      "@type": "Agent",
      "@id": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "type": [
        "wfprov:WorkflowEngine",
        "prov:SoftwareAgent"
      ],
      "label": [
        {
          "@value": "cwltool 3.1.20260108082145"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:74ee65c3-45e0-49ab-9086-fd0704308112",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/select-products-sentinel2:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/select-products-sentinel2:1.1.0"
        }
      ]
    },
    {
      "@type": "Start",
      "activity": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "starter": "id:9e986cfd-629d-41cf-9c75-eb65ae428d71",
      "time": "2026-09-23T08:26:24.309067"
    },
    {
      "@type": "Start",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "starter": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "time": "2026-09-23T08:26:24.309107"
    },
    {
      "@type": "Start",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "starter": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:26:24.581116"
    },
    {
      "@type": "Start",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "starter": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:26:25.902635"
    },
    {
      "@type": "Start",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "starter": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:35:40.367661"
    },
    {
      "@type": "Activity",
      "@id": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "startTime": "2026-09-23T08:26:24.309085",
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
      "@id": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/select_products"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/algae-usecase-workflow-earth-search/process"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "prov:has_provenance": [
        {
          "@value": "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.json",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.nt",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.ttl",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.xml",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.provn",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.jsonld",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/algae-usecase-workflow-earth-search/process"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "prov:has_provenance": [
        {
          "@value": "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.xml",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.json",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.nt",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.jsonld",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.provn",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/select_products"
    },
    {
      "@type": "Association",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "agent": "id:74ee65c3-45e0-49ab-9086-fd0704308112"
    },
    {
      "@type": "Association",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/algae-usecase-workflow-earth-search/process"
    },
    {
      "@type": "Association",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/algae-usecase-workflow-earth-search/process"
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
          "@value": "wf:main/process",
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
          "@value": "wf:main/select_products",
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
      "@id": "wf:main/process",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/select_products",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:09b3c69758a531dc4f198b8a083607dc5a617e4f",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:09b3c69758a531dc4f198b8a083607dc5a617e4f",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5226a207-b9d6-4693-b683-260e1f1d77cf",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "algae-usecase-region.geojson"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "algae-usecase-region"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".geojson"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:9841304d-a79d-49fb-ba33-d05f45ce0443",
      "value": [
        {
          "@value": "0.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:4c89b83017b6bf2fdefdc95f52a039255235ba37",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "sentinel-2-l2a"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:4c89b83017b6bf2fdefdc95f52a039255235ba37",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "sentinel-2-l2a"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c03c3a8f-fd1a-4796-9014-0da5e9f7866d",
      "value": [
        {
          "@value": "4",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:2a63ee24a0e8e4b59a1f6e59f003d4201c3ecba3",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "2019-06-25"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:2a63ee24a0e8e4b59a1f6e59f003d4201c3ecba3",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "2019-06-25"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e6b6a83d9218e6cb73c53b7fb501615a47a84aaa",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "2019-07-03"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e6b6a83d9218e6cb73c53b7fb501615a47a84aaa",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "2019-07-03"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:50b5b789-1882-4c70-9c6a-59f121c84204",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:bb36ba47-4fd9-4c7e-b7f8-fd944a8f3539",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "algae-usecase-region.geojson"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "algae-usecase-region"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".geojson"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b361b353c05b9c7e9b56b5de806f65ce2c8da7b5",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "earth-search"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:cf1cca44-d0e6-48b5-ba47-0e7ab8eb2752",
      "value": [
        {
          "@value": "0.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:4be4827d-8cb6-4720-99c0-164401d97f27",
      "value": [
        {
          "@value": "4",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:632ab110c744c188c9ae98cb2c6b74767894037a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:71200b7e-dd7c-4784-a342-7f5a60ceba87",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c80240b036ceef4fdcfb684013f5e78f2fd144e7",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_29SPC_20190701_1_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:084a442888f71ba66d9e75fde8221f58dfaa6acf",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_29SPC_20190701_0_L2A"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:43171557-8d98-4580-a7eb-6347713b13d8",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:32ae8712ff4f8b8b6b34af45257c41c16474dc98"
    },
    {
      "@type": "Entity",
      "@id": "id:12b49a35-ae72-4b3d-933e-b2d03c6692b4",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tiff"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:6947846b1796dd6e940e390f61208a85f45117b0"
    },
    {
      "@type": "Entity",
      "@id": "id:883ae32e-c86f-491e-bcaf-320d0badfa08",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tiff"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:042f18c9-28ad-4704-b250-c8dfe82253ab",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:fb8e7e26b282372c29a35ac739498699e02006a5"
    },
    {
      "@type": "Entity",
      "@id": "id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color"
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
      "@id": "data:e6874b008b758679af8241dfbfb355b204b131b2"
    },
    {
      "@type": "Entity",
      "@id": "id:1a896ecf-4e0a-4020-b7e1-107ee08a506c",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color"
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
      "@id": "id:0dd086eb-264f-42f5-bf6e-0e2b215edafc",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:38185787e3c54223cfadb4c26c22b126ad624d21"
    },
    {
      "@type": "Entity",
      "@id": "id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".png"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:1224781c8a82490664559a3b2e66fa3e14e09956"
    },
    {
      "@type": "Entity",
      "@id": "id:372c5307-8059-4cb2-afdb-5417b1e9d278",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".png"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ed4239e2-9d57-4b3c-9644-295b0a843de3",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8"
    },
    {
      "@type": "Entity",
      "@id": "id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tiff"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:065539f1417b6c8066de9420c143413de2cbcd97"
    },
    {
      "@type": "Entity",
      "@id": "id:f4eb96c4-9178-469a-94da-e74a9ec97592",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tiff"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0f27aaca-13e9-4be4-b2d9-ea39fef6101f",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:88d67511003f18c13b7cdc982f5796ab5ae261fc"
    },
    {
      "@type": "Entity",
      "@id": "id:f82e4423-a8ac-41d1-9919-25b94a343f05",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria_color"
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
      "@id": "data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6"
    },
    {
      "@type": "Entity",
      "@id": "id:1cfc6922-9537-41b3-a579-31eaab50998e",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria_color"
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
      "@id": "id:5855d17a-509f-4d45-91ef-c239bcb938de",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:876c7b4d7381ac5660a4507292c9324eb295a297"
    },
    {
      "@type": "Entity",
      "@id": "id:d1872c35-1d75-47b2-8315-90b2bbf42c23",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".png"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:3822adba1b42a347ef376f9ac0e7259d0ba82b22"
    },
    {
      "@type": "Entity",
      "@id": "id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".png"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:8fb08dce-0549-434c-b6bc-251e3b2227d2",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0"
    },
    {
      "@type": "Entity",
      "@id": "id:4e6424db-66b9-4389-81ca-0a3040fbfd07",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tiff"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c50376cb72b65a0dad365279023daa2af7208fc9"
    },
    {
      "@type": "Entity",
      "@id": "id:d0b679db-ef77-442f-a4c0-f093f5da8990",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".tiff"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d5e1a699-e4ec-4961-9136-0c23387faf90",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a"
    },
    {
      "@type": "Entity",
      "@id": "id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity_color"
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
      "@id": "data:a2beee36554454e4c0090480d062bc893f3ae7cc"
    },
    {
      "@type": "Entity",
      "@id": "id:248923b2-906c-4d76-867f-da6f12462902",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity_color"
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
      "@id": "id:0ee12773-4ecf-4b82-9e77-dacfea757a43",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c991e2bc239887ca885b02cab5fdae42c90a2889"
    },
    {
      "@type": "Entity",
      "@id": "id:94fcea32-9310-49c6-8684-7517ae960f49",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity_plot"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".png"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:8088de425841559ae78ca6328ecdf8bb0fe578d4"
    },
    {
      "@type": "Entity",
      "@id": "id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity_plot"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".png"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:78c77861-3ab8-4a56-a0cc-62899eb92912",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:5226a207-b9d6-4693-b683-260e1f1d77cf",
      "generalEntity": "data:09b3c69758a531dc4f198b8a083607dc5a617e4f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:bb36ba47-4fd9-4c7e-b7f8-fd944a8f3539",
      "generalEntity": "data:09b3c69758a531dc4f198b8a083607dc5a617e4f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:12b49a35-ae72-4b3d-933e-b2d03c6692b4",
      "generalEntity": "data:32ae8712ff4f8b8b6b34af45257c41c16474dc98"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:883ae32e-c86f-491e-bcaf-320d0badfa08",
      "generalEntity": "data:6947846b1796dd6e940e390f61208a85f45117b0"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54",
      "generalEntity": "data:fb8e7e26b282372c29a35ac739498699e02006a5"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1a896ecf-4e0a-4020-b7e1-107ee08a506c",
      "generalEntity": "data:e6874b008b758679af8241dfbfb355b204b131b2"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1",
      "generalEntity": "data:38185787e3c54223cfadb4c26c22b126ad624d21"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:372c5307-8059-4cb2-afdb-5417b1e9d278",
      "generalEntity": "data:1224781c8a82490664559a3b2e66fa3e14e09956"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be",
      "generalEntity": "data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:f4eb96c4-9178-469a-94da-e74a9ec97592",
      "generalEntity": "data:065539f1417b6c8066de9420c143413de2cbcd97"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:f82e4423-a8ac-41d1-9919-25b94a343f05",
      "generalEntity": "data:88d67511003f18c13b7cdc982f5796ab5ae261fc"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1cfc6922-9537-41b3-a579-31eaab50998e",
      "generalEntity": "data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:d1872c35-1d75-47b2-8315-90b2bbf42c23",
      "generalEntity": "data:876c7b4d7381ac5660a4507292c9324eb295a297"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2",
      "generalEntity": "data:3822adba1b42a347ef376f9ac0e7259d0ba82b22"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:4e6424db-66b9-4389-81ca-0a3040fbfd07",
      "generalEntity": "data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:d0b679db-ef77-442f-a4c0-f093f5da8990",
      "generalEntity": "data:c50376cb72b65a0dad365279023daa2af7208fc9"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4",
      "generalEntity": "data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:248923b2-906c-4d76-867f-da6f12462902",
      "generalEntity": "data:a2beee36554454e4c0090480d062bc893f3ae7cc"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:94fcea32-9310-49c6-8684-7517ae960f49",
      "generalEntity": "data:c991e2bc239887ca885b02cab5fdae42c90a2889"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2",
      "generalEntity": "data:8088de425841559ae78ca6328ecdf8bb0fe578d4"
    },
    {
      "@type": "Usage",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "entity": "id:5226a207-b9d6-4693-b683-260e1f1d77cf",
      "time": "2026-09-23T08:26:24.577508",
      "role": [
        "wf:main/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "entity": "id:9841304d-a79d-49fb-ba33-d05f45ce0443",
      "time": "2026-09-23T08:26:24.577548",
      "role": [
        "wf:main/cloud_cover"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "entity": "data:4c89b83017b6bf2fdefdc95f52a039255235ba37",
      "time": "2026-09-23T08:26:24.577940",
      "role": [
        "wf:main/collection"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "entity": "id:c03c3a8f-fd1a-4796-9014-0da5e9f7866d",
      "time": "2026-09-23T08:26:24.577974",
      "role": [
        "wf:main/delta"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "entity": "id:50b5b789-1882-4c70-9c6a-59f121c84204",
      "time": "2026-09-23T08:26:24.578511",
      "role": [
        "wf:main/toi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "id:bb36ba47-4fd9-4c7e-b7f8-fd944a8f3539",
      "time": "2026-09-23T08:26:24.618823",
      "role": [
        "wf:main/select_products/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "data:b361b353c05b9c7e9b56b5de806f65ce2c8da7b5",
      "time": "2026-09-23T08:26:24.619154",
      "role": [
        "wf:main/select_products/catalog"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "id:cf1cca44-d0e6-48b5-ba47-0e7ab8eb2752",
      "time": "2026-09-23T08:26:24.619184",
      "role": [
        "wf:main/select_products/cloud_cover"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "data:4c89b83017b6bf2fdefdc95f52a039255235ba37",
      "time": "2026-09-23T08:26:24.619408",
      "role": [
        "wf:main/select_products/collection"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:26:24.619429",
      "role": [
        "wf:main/select_products/date"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "id:4be4827d-8cb6-4720-99c0-164401d97f27",
      "time": "2026-09-23T08:26:24.619451",
      "role": [
        "wf:main/select_products/delta"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "data:632ab110c744c188c9ae98cb2c6b74767894037a",
      "time": "2026-09-23T08:26:24.619722",
      "role": [
        "wf:main/select_products/product_level"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "entity": "id:71200b7e-dd7c-4784-a342-7f5a60ceba87",
      "time": "2026-09-23T08:26:24.620133",
      "role": [
        "wf:main/select_products/toi"
      ]
    },
    {
      "@type": "Membership",
      "collection": "id:50b5b789-1882-4c70-9c6a-59f121c84204",
      "entity": "data:2a63ee24a0e8e4b59a1f6e59f003d4201c3ecba3"
    },
    {
      "@type": "Membership",
      "collection": "id:50b5b789-1882-4c70-9c6a-59f121c84204",
      "entity": "data:e6b6a83d9218e6cb73c53b7fb501615a47a84aaa"
    },
    {
      "@type": "Membership",
      "collection": "id:71200b7e-dd7c-4784-a342-7f5a60ceba87",
      "entity": "data:2a63ee24a0e8e4b59a1f6e59f003d4201c3ecba3"
    },
    {
      "@type": "Membership",
      "collection": "id:71200b7e-dd7c-4784-a342-7f5a60ceba87",
      "entity": "data:e6b6a83d9218e6cb73c53b7fb501615a47a84aaa"
    },
    {
      "@type": "Membership",
      "collection": "id:43171557-8d98-4580-a7eb-6347713b13d8",
      "entity": "data:c80240b036ceef4fdcfb684013f5e78f2fd144e7"
    },
    {
      "@type": "Membership",
      "collection": "id:43171557-8d98-4580-a7eb-6347713b13d8",
      "entity": "data:084a442888f71ba66d9e75fde8221f58dfaa6acf"
    },
    {
      "@type": "Membership",
      "collection": "id:042f18c9-28ad-4704-b250-c8dfe82253ab",
      "entity": "id:12b49a35-ae72-4b3d-933e-b2d03c6692b4"
    },
    {
      "@type": "Membership",
      "collection": "id:042f18c9-28ad-4704-b250-c8dfe82253ab",
      "entity": "id:883ae32e-c86f-491e-bcaf-320d0badfa08"
    },
    {
      "@type": "Membership",
      "collection": "id:0dd086eb-264f-42f5-bf6e-0e2b215edafc",
      "entity": "id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54"
    },
    {
      "@type": "Membership",
      "collection": "id:0dd086eb-264f-42f5-bf6e-0e2b215edafc",
      "entity": "id:1a896ecf-4e0a-4020-b7e1-107ee08a506c"
    },
    {
      "@type": "Membership",
      "collection": "id:ed4239e2-9d57-4b3c-9644-295b0a843de3",
      "entity": "id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1"
    },
    {
      "@type": "Membership",
      "collection": "id:ed4239e2-9d57-4b3c-9644-295b0a843de3",
      "entity": "id:372c5307-8059-4cb2-afdb-5417b1e9d278"
    },
    {
      "@type": "Membership",
      "collection": "id:0f27aaca-13e9-4be4-b2d9-ea39fef6101f",
      "entity": "id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be"
    },
    {
      "@type": "Membership",
      "collection": "id:0f27aaca-13e9-4be4-b2d9-ea39fef6101f",
      "entity": "id:f4eb96c4-9178-469a-94da-e74a9ec97592"
    },
    {
      "@type": "Membership",
      "collection": "id:5855d17a-509f-4d45-91ef-c239bcb938de",
      "entity": "id:f82e4423-a8ac-41d1-9919-25b94a343f05"
    },
    {
      "@type": "Membership",
      "collection": "id:5855d17a-509f-4d45-91ef-c239bcb938de",
      "entity": "id:1cfc6922-9537-41b3-a579-31eaab50998e"
    },
    {
      "@type": "Membership",
      "collection": "id:8fb08dce-0549-434c-b6bc-251e3b2227d2",
      "entity": "id:d1872c35-1d75-47b2-8315-90b2bbf42c23"
    },
    {
      "@type": "Membership",
      "collection": "id:8fb08dce-0549-434c-b6bc-251e3b2227d2",
      "entity": "id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2"
    },
    {
      "@type": "Membership",
      "collection": "id:d5e1a699-e4ec-4961-9136-0c23387faf90",
      "entity": "id:4e6424db-66b9-4389-81ca-0a3040fbfd07"
    },
    {
      "@type": "Membership",
      "collection": "id:d5e1a699-e4ec-4961-9136-0c23387faf90",
      "entity": "id:d0b679db-ef77-442f-a4c0-f093f5da8990"
    },
    {
      "@type": "Membership",
      "collection": "id:0ee12773-4ecf-4b82-9e77-dacfea757a43",
      "entity": "id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4"
    },
    {
      "@type": "Membership",
      "collection": "id:0ee12773-4ecf-4b82-9e77-dacfea757a43",
      "entity": "id:248923b2-906c-4d76-867f-da6f12462902"
    },
    {
      "@type": "Membership",
      "collection": "id:78c77861-3ab8-4a56-a0cc-62899eb92912",
      "entity": "id:94fcea32-9310-49c6-8684-7517ae960f49"
    },
    {
      "@type": "Membership",
      "collection": "id:78c77861-3ab8-4a56-a0cc-62899eb92912",
      "entity": "id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2"
    },
    {
      "@type": "Generation",
      "entity": "id:43171557-8d98-4580-a7eb-6347713b13d8",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "time": "2026-09-23T08:26:25.900602",
      "role": [
        "wf:main/select_products/urls"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:042f18c9-28ad-4704-b250-c8dfe82253ab",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/chlorophyll_a"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:0dd086eb-264f-42f5-bf6e-0e2b215edafc",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/chlorophyll_a_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:ed4239e2-9d57-4b3c-9644-295b0a843de3",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/chlorophyll_a_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:0f27aaca-13e9-4be4-b2d9-ea39fef6101f",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/cyanobacteria"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:5855d17a-509f-4d45-91ef-c239bcb938de",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/cyanobacteria_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:8fb08dce-0549-434c-b6bc-251e3b2227d2",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/cyanobacteria_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d5e1a699-e4ec-4961-9136-0c23387faf90",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/turbidity"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:0ee12773-4ecf-4b82-9e77-dacfea757a43",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/turbidity_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:78c77861-3ab8-4a56-a0cc-62899eb92912",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:40:34.610317",
      "role": [
        "wf:main/primary/turbidity_plot"
      ]
    },
    {
      "@type": "End",
      "activity": "id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27",
      "ender": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "time": "2026-09-23T08:26:25.900591"
    },
    {
      "@type": "End",
      "activity": "id:39aa9d6c-b92f-486d-9c56-5289ebc57918",
      "ender": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "time": "2026-09-23T08:40:34.611137"
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
@prefix wf: <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#> .
@prefix wf4ever: <http://purl.org/wf4ever/wf4ever#> .
@prefix wfdesc: <http://purl.org/wf4ever/wfdesc#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/process> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

id:042f18c9-28ad-4704-b250-c8dfe82253ab a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/chlorophyll_a> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:12b49a35-ae72-4b3d-933e-b2d03c6692b4 ],
        [ a provext:Membership ;
            provext:member id:883ae32e-c86f-491e-bcaf-320d0badfa08 ] .

id:0dd086eb-264f-42f5-bf6e-0e2b215edafc a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/chlorophyll_a_color> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:1a896ecf-4e0a-4020-b7e1-107ee08a506c ],
        [ a provext:Membership ;
            provext:member id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54 ] .

id:0ee12773-4ecf-4b82-9e77-dacfea757a43 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/turbidity_color> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:248923b2-906c-4d76-867f-da6f12462902 ],
        [ a provext:Membership ;
            provext:member id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4 ] .

id:0f27aaca-13e9-4be4-b2d9-ea39fef6101f a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/cyanobacteria> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be ],
        [ a provext:Membership ;
            provext:member id:f4eb96c4-9178-469a-94da-e74a9ec97592 ] .

id:43171557-8d98-4580-a7eb-6347713b13d8 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27 ;
            prov:atTime "2026-09-23T08:26:25.900602"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/urls> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:c80240b036ceef4fdcfb684013f5e78f2fd144e7 ],
        [ a provext:Membership ;
            provext:member data:084a442888f71ba66d9e75fde8221f58dfaa6acf ] .

id:5855d17a-509f-4d45-91ef-c239bcb938de a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/cyanobacteria_color> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:1cfc6922-9537-41b3-a579-31eaab50998e ],
        [ a provext:Membership ;
            provext:member id:f82e4423-a8ac-41d1-9919-25b94a343f05 ] .

id:78c77861-3ab8-4a56-a0cc-62899eb92912 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/turbidity_plot> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2 ],
        [ a provext:Membership ;
            provext:member id:94fcea32-9310-49c6-8684-7517ae960f49 ] .

id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/algae-usecase-workflow-earth-search/process" ;
    prov:has_provenance "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.json"^^xsd:QName,
        "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.jsonld"^^xsd:QName,
        "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.nt"^^xsd:QName,
        "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.provn"^^xsd:QName,
        "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.ttl"^^xsd:QName,
        "provenance:workflow_20process.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.xml"^^xsd:QName,
        "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.json"^^xsd:QName,
        "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.jsonld"^^xsd:QName,
        "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.nt"^^xsd:QName,
        "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.provn"^^xsd:QName,
        "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.ttl"^^xsd:QName,
        "provenance:workflow_20process_2.7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86.cwlprov.xml"^^xsd:QName ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/algae-usecase-workflow-earth-search/process> ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/algae-usecase-workflow-earth-search/process> ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:26:25.902635"^^xsd:dateTime ;
            prov:hadActivity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ],
        [ a prov:Start ;
            prov:atTime "2026-09-23T08:35:40.367661"^^xsd:dateTime ;
            prov:hadActivity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ] .

id:8fb08dce-0549-434c-b6bc-251e3b2227d2 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/cyanobacteria_plot> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:d1872c35-1d75-47b2-8315-90b2bbf42c23 ],
        [ a provext:Membership ;
            provext:member id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2 ] .

id:d5e1a699-e4ec-4961-9136-0c23387faf90 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/turbidity> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:d0b679db-ef77-442f-a4c0-f093f5da8990 ],
        [ a provext:Membership ;
            provext:member id:4e6424db-66b9-4389-81ca-0a3040fbfd07 ] .

id:ed4239e2-9d57-4b3c-9644-295b0a843de3 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ;
            prov:atTime "2026-09-23T08:40:34.610317"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/primary/chlorophyll_a_plot> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:372c5307-8059-4cb2-afdb-5417b1e9d278 ],
        [ a provext:Membership ;
            provext:member id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1 ] .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/process"^^xsd:QName,
        "wf:main/select_products"^^xsd:QName .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

cwlprov:None a prov:Entity ;
    rdfs:label "None" .

data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0 a prov:Entity .

data:065539f1417b6c8066de9420c143413de2cbcd97 a prov:Entity .

data:084a442888f71ba66d9e75fde8221f58dfaa6acf a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_29SPC_20190701_0_L2A" .

data:1224781c8a82490664559a3b2e66fa3e14e09956 a prov:Entity .

data:32ae8712ff4f8b8b6b34af45257c41c16474dc98 a prov:Entity .

data:38185787e3c54223cfadb4c26c22b126ad624d21 a prov:Entity .

data:3822adba1b42a347ef376f9ac0e7259d0ba82b22 a prov:Entity .

data:632ab110c744c188c9ae98cb2c6b74767894037a a wfprov:Artifact,
        prov:Entity ;
    prov:value "L2A" .

data:6947846b1796dd6e940e390f61208a85f45117b0 a prov:Entity .

data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a a prov:Entity .

data:8088de425841559ae78ca6328ecdf8bb0fe578d4 a prov:Entity .

data:876c7b4d7381ac5660a4507292c9324eb295a297 a prov:Entity .

data:88d67511003f18c13b7cdc982f5796ab5ae261fc a prov:Entity .

data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8 a prov:Entity .

data:a2beee36554454e4c0090480d062bc893f3ae7cc a prov:Entity .

data:b361b353c05b9c7e9b56b5de806f65ce2c8da7b5 a wfprov:Artifact,
        prov:Entity ;
    prov:value "earth-search" .

data:c50376cb72b65a0dad365279023daa2af7208fc9 a prov:Entity .

data:c80240b036ceef4fdcfb684013f5e78f2fd144e7 a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_29SPC_20190701_1_L2A" .

data:c991e2bc239887ca885b02cab5fdae42c90a2889 a prov:Entity .

data:e6874b008b758679af8241dfbfb355b204b131b2 a prov:Entity .

data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6 a prov:Entity .

data:fb8e7e26b282372c29a35ac739498699e02006a5 a prov:Entity .

id:12b49a35-ae72-4b3d-933e-b2d03c6692b4 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:32ae8712ff4f8b8b6b34af45257c41c16474dc98 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_chlorophyll_a" .

id:1a896ecf-4e0a-4020-b7e1-107ee08a506c a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e6874b008b758679af8241dfbfb355b204b131b2 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color" .

id:1cfc6922-9537-41b3-a579-31eaab50998e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_cyanobacteria_color" .

id:248923b2-906c-4d76-867f-da6f12462902 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:a2beee36554454e4c0090480d062bc893f3ae7cc ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_turbidity_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_turbidity_color" .

id:372c5307-8059-4cb2-afdb-5417b1e9d278 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:1224781c8a82490664559a3b2e66fa3e14e09956 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot" .

id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:38185787e3c54223cfadb4c26c22b126ad624d21 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot" .

id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_cyanobacteria" .

id:4be4827d-8cb6-4720-99c0-164401d97f27 a prov:Entity ;
    prov:value "4"^^xsd:int .

id:4e6424db-66b9-4389-81ca-0a3040fbfd07 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_turbidity.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_turbidity" .

id:50b5b789-1882-4c70-9c6a-59f121c84204 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:e6b6a83d9218e6cb73c53b7fb501615a47a84aaa ],
        [ a provext:Membership ;
            provext:member data:2a63ee24a0e8e4b59a1f6e59f003d4201c3ecba3 ] .

id:5226a207-b9d6-4693-b683-260e1f1d77cf a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:09b3c69758a531dc4f198b8a083607dc5a617e4f ] ;
    cwlprov:basename "algae-usecase-region.geojson" ;
    cwlprov:nameext ".geojson" ;
    cwlprov:nameroot "algae-usecase-region" .

id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:fb8e7e26b282372c29a35ac739498699e02006a5 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color" .

id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8088de425841559ae78ca6328ecdf8bb0fe578d4 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_turbidity_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_turbidity_plot" .

id:6eeb1082-3e85-4b8c-87e4-db08b8a54f27 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/select_products" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:74ee65c3-45e0-49ab-9086-fd0704308112 ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:26:25.900591"^^xsd:dateTime ;
            prov:hadActivity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:26:24.581116"^^xsd:dateTime ;
            prov:hadActivity id:39aa9d6c-b92f-486d-9c56-5289ebc57918 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.618823"^^xsd:dateTime ;
            prov:entity id:bb36ba47-4fd9-4c7e-b7f8-fd944a8f3539 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.619451"^^xsd:dateTime ;
            prov:entity id:4be4827d-8cb6-4720-99c0-164401d97f27 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/delta> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.619429"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/date> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.619408"^^xsd:dateTime ;
            prov:entity data:4c89b83017b6bf2fdefdc95f52a039255235ba37 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/collection> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.620133"^^xsd:dateTime ;
            prov:entity id:71200b7e-dd7c-4784-a342-7f5a60ceba87 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/toi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.619184"^^xsd:dateTime ;
            prov:entity id:cf1cca44-d0e6-48b5-ba47-0e7ab8eb2752 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/cloud_cover> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.619154"^^xsd:dateTime ;
            prov:entity data:b361b353c05b9c7e9b56b5de806f65ce2c8da7b5 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/catalog> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.619722"^^xsd:dateTime ;
            prov:entity data:632ab110c744c188c9ae98cb2c6b74767894037a ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/select_products/product_level> ] .

id:71200b7e-dd7c-4784-a342-7f5a60ceba87 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:e6b6a83d9218e6cb73c53b7fb501615a47a84aaa ],
        [ a provext:Membership ;
            provext:member data:2a63ee24a0e8e4b59a1f6e59f003d4201c3ecba3 ] .

id:74ee65c3-45e0-49ab-9086-fd0704308112 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/select-products-sentinel2:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/select-products-sentinel2:1.1.0" .

id:883ae32e-c86f-491e-bcaf-320d0badfa08 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:6947846b1796dd6e940e390f61208a85f45117b0 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_chlorophyll_a" .

id:94fcea32-9310-49c6-8684-7517ae960f49 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:c991e2bc239887ca885b02cab5fdae42c90a2889 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_turbidity_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_turbidity_plot" .

id:9841304d-a79d-49fb-ba33-d05f45ce0443 a prov:Entity ;
    prov:value 1e-01 .

id:9e986cfd-629d-41cf-9c75-eb65ae428d71 a prov:Agent .

id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:3822adba1b42a347ef376f9ac0e7259d0ba82b22 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot" .

id:bb36ba47-4fd9-4c7e-b7f8-fd944a8f3539 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:09b3c69758a531dc4f198b8a083607dc5a617e4f ] ;
    cwlprov:basename "algae-usecase-region.geojson" ;
    cwlprov:nameext ".geojson" ;
    cwlprov:nameroot "algae-usecase-region" .

id:c03c3a8f-fd1a-4796-9014-0da5e9f7866d a prov:Entity ;
    prov:value "4"^^xsd:int .

id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_turbidity_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_turbidity_color" .

id:cf1cca44-d0e6-48b5-ba47-0e7ab8eb2752 a prov:Entity ;
    prov:value 1e-01 .

id:d0b679db-ef77-442f-a4c0-f093f5da8990 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:c50376cb72b65a0dad365279023daa2af7208fc9 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_turbidity.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_turbidity" .

id:d1872c35-1d75-47b2-8315-90b2bbf42c23 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:876c7b4d7381ac5660a4507292c9324eb295a297 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot" .

id:f4eb96c4-9178-469a-94da-e74a9ec97592 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:065539f1417b6c8066de9420c143413de2cbcd97 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_cyanobacteria" .

id:f82e4423-a8ac-41d1-9919-25b94a343f05 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:88d67511003f18c13b7cdc982f5796ab5ae261fc ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_cyanobacteria_color" .

data:09b3c69758a531dc4f198b8a083607dc5a617e4f a wfprov:Artifact,
        prov:Entity .

data:2a63ee24a0e8e4b59a1f6e59f003d4201c3ecba3 a wfprov:Artifact,
        prov:Entity ;
    prov:value "2019-06-25" .

data:4c89b83017b6bf2fdefdc95f52a039255235ba37 a wfprov:Artifact,
        prov:Entity ;
    prov:value "sentinel-2-l2a" .

data:e6b6a83d9218e6cb73c53b7fb501615a47a84aaa a wfprov:Artifact,
        prov:Entity ;
    prov:value "2019-07-03" .

id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:26:24.309067"^^xsd:dateTime ;
            prov:hadActivity id:9e986cfd-629d-41cf-9c75-eb65ae428d71 ] .

id:39aa9d6c-b92f-486d-9c56-5289ebc57918 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:40:34.611137"^^xsd:dateTime ;
            prov:hadActivity id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:26:24.309107"^^xsd:dateTime ;
            prov:hadActivity id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.578511"^^xsd:dateTime ;
            prov:entity id:50b5b789-1882-4c70-9c6a-59f121c84204 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/toi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.577508"^^xsd:dateTime ;
            prov:entity id:5226a207-b9d6-4693-b683-260e1f1d77cf ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.577974"^^xsd:dateTime ;
            prov:entity id:c03c3a8f-fd1a-4796-9014-0da5e9f7866d ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/delta> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.577940"^^xsd:dateTime ;
            prov:entity data:4c89b83017b6bf2fdefdc95f52a039255235ba37 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/collection> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:24.577548"^^xsd:dateTime ;
            prov:entity id:9841304d-a79d-49fb-ba33-d05f45ce0443 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/cloud_cover> ] ;
    prov:startedAtTime "2026-09-23T08:26:24.309085"^^xsd:dateTime .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `algae-usecase-workflow-earth-search`
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
      const: algae-usecase-workflow-earth-search
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - date
      - delta
      - toi
      - aoi
      - collection
      - cloud_cover
      propertyNames:
        enum:
        - date
        - delta
        - toi
        - aoi
        - collection
        - cloud_cover
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - chlorophyll_a
      - chlorophyll_a_color
      - chlorophyll_a_plot
      - cyanobacteria
      - cyanobacteria_color
      - cyanobacteria_plot
      - turbidity
      - turbidity_color
      - turbidity_plot
      propertyNames:
        enum:
        - chlorophyll_a
        - chlorophyll_a_color
        - chlorophyll_a_plot
        - cyanobacteria
        - cyanobacteria_color
        - cyanobacteria_plot
        - turbidity
        - turbidity_color
        - turbidity_plot
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
        - aoi
        - collection
        propertyNames:
          enum:
          - date
          - delta
          - toi
          - aoi
          - collection
          - cloud_cover
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
          - chlorophyll_a
          - chlorophyll_a_color
          - chlorophyll_a_plot
          - cyanobacteria
          - cyanobacteria_color
          - cyanobacteria_plot
          - turbidity
          - turbidity_color
          - turbidity_plot
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
      - chlorophyll_a
      - chlorophyll_a_color
      - chlorophyll_a_plot
      - cyanobacteria
      - cyanobacteria_color
      - cyanobacteria_plot
      - turbidity
      - turbidity_color
      - turbidity_plot
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-earth-search/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/algae-bloom/workflow-earth-search`

