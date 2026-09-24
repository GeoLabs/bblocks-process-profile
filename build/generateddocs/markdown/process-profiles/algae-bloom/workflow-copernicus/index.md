
# Process profile: algae-usecase-workflow-copernicus (Schema)

`ospd.process-profiles.algae-bloom.workflow-copernicus` *v0.1*

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-copernicus` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`algae-usecase-workflow-copernicus`** (Workflow, W1 Algae Bloom).

> Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.

## Source

- CWL: [algae-usecase-workflow-copernicus.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Filter configuration → Selection / filtering → Data retrieval → Pre-processing → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.geojson`, `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.algae-bloom.select-products-sentinel2`, `ospd.process-profiles.algae-bloom.workflow-copernicus-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `date` | string | `chlorophyll_a` | File[] |
| `delta` | int? | `chlorophyll_a_color` | File[] |
| `aoi` | File | `chlorophyll_a_plot` | File[] |
| `collection` | string | `cyanobacteria` | File[] |
| `cloud_cover` | double? | `cyanobacteria_color` | File[] |
| `s3_access_key` | string | `cyanobacteria_plot` | File[] |
| `s3_secret_key` | string | `turbidity` | File[] |
|  |  | `turbidity_color` | File[] |
|  |  | `turbidity_plot` | File[] |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-04 inputs.s3_access_key: declared in cwltool:Secrets -> writeOnly: true
- M-04 inputs.s3_secret_key: declared in cwltool:Secrets -> writeOnly: true

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-copernicus`: Copernicus variant of the pinned W1 package, `cwltool --outdir ./results1 --provenance ./PROV1 algae-usecase-workflow-copernicus.cwl example/algae-usecase-job-copernicus.yml` with Copernicus Data Space S3 credentials, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; one product (S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542). cwltool writes the `cwltool:Secrets` inputs as `(secret-<uuid>)` placeholders in the research object), activity `main` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite; same structure as the Earth-Search variant but over Copernicus Data Space (SAFE products on S3, credentials required). openEO hides credentials in the back-end.


| Stage | openEO | Level | Note |
|---|---|---|---|
| select_products | `ogc.openeo.processes.cubes.load_collection` | closeMatch |  |
| process (scatter over urls) | — | none |  |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL Workflow is referenced, not copied: <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl>.

### processDescription
OGC API - Processes processDescription derived from the CWL (manually corrected, see description).
#### json
```json
{
  "id": "algae-usecase-workflow-copernicus",
  "version": "2.0.0",
  "title": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n",
  "description": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n",
  "mutable": true,
  "keywords": [
    "water-quality",
    "algae-bloom",
    "Copernicus",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n"
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
      "title": "date",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
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
    "aoi": {
      "title": "aoi",
      "description": "",
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
    },
    "s3_access_key": {
      "title": "S3 access key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string",
        "writeOnly": true
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string",
        "writeOnly": true
      },
      "minOccurs": 1,
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "id": "algae-usecase-workflow-copernicus",
  "version": "2.0.0",
  "title": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n",
  "description": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n",
  "mutable": true,
  "keywords": [
    "water-quality",
    "algae-bloom",
    "Copernicus",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n"
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
      "title": "date",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
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
    "aoi": {
      "title": "aoi",
      "description": "",
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
    },
    "s3_access_key": {
      "title": "S3 access key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string",
        "writeOnly": true
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string",
        "writeOnly": true
      },
      "minOccurs": 1,
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
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <http://schema.org/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus> dcterms:description """Finds Sentinel-2 products on Copernicus using filtering parameters
and performs band calculation on retrieved Sentinel-2 products
to evaluate algae bloom for water quality assessment.
""" ;
    dcterms:subject "Copernicus",
        "OSPD",
        "algae-bloom",
        "demo",
        "water-quality" ;
    dcterms:title """Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.
""" ;
    pp:version "2.0.0" ;
    proc:inputs [ ns1:aoi [ dcterms:description "" ;
                    dcterms:title "aoi" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentEncoding "binary" ;
                            ns2:contentMediaType "application/geo+json" ] ] ;
            ns1:cloud_cover [ dcterms:description "" ;
                    dcterms:title "cloud_cover" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns1:collection [ dcterms:description "" ;
                    dcterms:title "collection" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:date [ dcterms:description "" ;
                    dcterms:title "date" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:delta [ dcterms:description "" ;
                    dcterms:title "delta" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "4"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns1:s3_access_key [ dcterms:description """Access key to Copernicus data provider.
See https://documentation.dataspace.copernicus.eu/Registration.html 
and https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.
""" ;
                    dcterms:title "S3 access key required to retrieve products hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns2:writeOnly true ] ] ;
            ns1:s3_secret_key [ dcterms:description """Access key to Copernicus data provider.
See https://documentation.dataspace.copernicus.eu/Registration.html 
and https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.
""" ;
                    dcterms:title "S3 secret key required to retrieve products hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns2:writeOnly true ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "2.0.0" ;
            proc:role schema:softwareVersion ],
        [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ],
        [ rdf:value [ a ns4:Person ;
                    ns4:email "francis.charette-migneault@crim.ca" ;
                    ns4:identifier "http://orcid.org/0000-0003-4862-3349" ;
                    ns4:name "Francis Charette-Migneault" ] ;
            proc:role schema:author ],
        [ rdf:value """Finds Sentinel-2 products on Copernicus using filtering parameters
and performs band calculation on retrieved Sentinel-2 products
to evaluate algae bloom for water quality assessment.
""" ;
            proc:role schema:description ],
        [ rdf:value """Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.
""" ;
            proc:role schema:name ],
        [ rdf:value "https://gitlab.ogc.org/ogc/ogc-ospd" ;
            proc:role schema:codeRepository ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:chlorophyll_a [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:chlorophyll_a_color [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a_color" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:chlorophyll_a_plot [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/png" ] ] ] ;
            ns3:cyanobacteria [ dcterms:description "" ;
                    dcterms:title "cyanobacteria" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:cyanobacteria_color [ dcterms:description "" ;
                    dcterms:title "cyanobacteria_color" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:cyanobacteria_plot [ dcterms:description "" ;
                    dcterms:title "cyanobacteria_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/png" ] ] ] ;
            ns3:turbidity [ dcterms:description "" ;
                    dcterms:title "turbidity" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:turbidity_color [ dcterms:description "" ;
                    dcterms:title "turbidity_color" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns3:turbidity_plot [ dcterms:description "" ;
                    dcterms:title "turbidity_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns2:items [ proc:type "string" ;
                                    ns2:contentEncoding "binary" ;
                                    ns2:contentMediaType "image/png" ] ] ] ] .


```


### Raw cwl-to-ogcprocess output
Unmodified output of the `eoap.cct.cwl-to-ogcprocess` jq transform.
#### json
```json
{
  "id": "algae-usecase-workflow-copernicus",
  "version": "2.0.0",
  "title": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n",
  "description": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n",
  "mutable": true,
  "keywords": [
    "water-quality",
    "algae-bloom",
    "Copernicus",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n"
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
      "title": "date",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
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
    "aoi": {
      "title": "aoi",
      "description": "",
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
    },
    "s3_access_key": {
      "title": "S3 access key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "id": "algae-usecase-workflow-copernicus",
  "version": "2.0.0",
  "title": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n",
  "description": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n",
  "mutable": true,
  "keywords": [
    "water-quality",
    "algae-bloom",
    "Copernicus",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Finds Sentinel-2 products on Copernicus using filtering parameters\nand performs band calculation on retrieved Sentinel-2 products\nto evaluate algae bloom for water quality assessment.\n"
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
      "title": "date",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
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
    "aoi": {
      "title": "aoi",
      "description": "",
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
    },
    "s3_access_key": {
      "title": "S3 access key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required to retrieve products hosted on a protected S3 location.",
      "description": "Access key to Copernicus data provider.\nSee https://documentation.dataspace.copernicus.eu/Registration.html \nand https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
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
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns3: <http://schema.org/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus> dcterms:description """Finds Sentinel-2 products on Copernicus using filtering parameters
and performs band calculation on retrieved Sentinel-2 products
to evaluate algae bloom for water quality assessment.
""" ;
    dcterms:subject "Copernicus",
        "OSPD",
        "algae-bloom",
        "demo",
        "water-quality" ;
    dcterms:title """Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.
""" ;
    pp:version "2.0.0" ;
    proc:inputs [ ns4:aoi [ dcterms:description "" ;
                    dcterms:title "aoi" ;
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
            ns4:date [ dcterms:description "" ;
                    dcterms:title "date" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns4:delta [ dcterms:description "" ;
                    dcterms:title "delta" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "4"^^rdf:JSON ;
                            proc:type "integer" ] ] ;
            ns4:s3_access_key [ dcterms:description """Access key to Copernicus data provider.
See https://documentation.dataspace.copernicus.eu/Registration.html 
and https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.
""" ;
                    dcterms:title "S3 access key required to retrieve products hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns4:s3_secret_key [ dcterms:description """Access key to Copernicus data provider.
See https://documentation.dataspace.copernicus.eu/Registration.html 
and https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets for details.
""" ;
                    dcterms:title "S3 secret key required to retrieve products hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value """Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.
""" ;
            proc:role schema:name ],
        [ rdf:value "2.0.0" ;
            proc:role schema:softwareVersion ],
        [ rdf:value """Finds Sentinel-2 products on Copernicus using filtering parameters
and performs band calculation on retrieved Sentinel-2 products
to evaluate algae bloom for water quality assessment.
""" ;
            proc:role schema:description ],
        [ rdf:value "https://gitlab.ogc.org/ogc/ogc-ospd" ;
            proc:role schema:codeRepository ],
        [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ],
        [ rdf:value [ a ns3:Person ;
                    ns3:email "francis.charette-migneault@crim.ca" ;
                    ns3:identifier "http://orcid.org/0000-0003-4862-3349" ;
                    ns3:name "Francis Charette-Migneault" ] ;
            proc:role schema:author ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns2:chlorophyll_a [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns2:chlorophyll_a_color [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a_color" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns2:chlorophyll_a_plot [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns2:cyanobacteria [ dcterms:description "" ;
                    dcterms:title "cyanobacteria" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns2:cyanobacteria_color [ dcterms:description "" ;
                    dcterms:title "cyanobacteria_color" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns2:cyanobacteria_plot [ dcterms:description "" ;
                    dcterms:title "cyanobacteria_plot" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/png" ] ] ] ;
            ns2:turbidity [ dcterms:description "" ;
                    dcterms:title "turbidity" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns2:turbidity_color [ dcterms:description "" ;
                    dcterms:title "turbidity_color" ;
                    proc:schema [ proc:type "array" ;
                            ns1:items [ proc:type "string" ;
                                    ns1:contentEncoding "binary" ;
                                    ns1:contentMediaType "image/tiff; application=geotiff" ] ] ] ;
            ns2:turbidity_plot [ dcterms:description "" ;
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
      "id": "algae-usecase-workflow-copernicus",
      "version": "2.0.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "processDescription": {
    "process": {
      "id": "algae-usecase-workflow-copernicus",
      "version": "2.0.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus> pp:version "2.0.0" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl" ;
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
    "collection": "SENTINEL-2",
    "date": "2019-06-29",
    "delta": 4,
    "cloud_cover": 0.1,
    "s3_access_key": "<redacted>",
    "s3_secret_key": "<redacted>"
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "inputs": {
    "aoi": {
      "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson",
      "type": "application/geo+json"
    },
    "collection": "SENTINEL-2",
    "date": "2019-06-29",
    "delta": 4,
    "cloud_cover": 0.1,
    "s3_access_key": "<redacted>",
    "s3_secret_key": "<redacted>"
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
            ns1:collection "SENTINEL-2" ;
            ns1:date "2019-06-29" ;
            ns1:delta 4 ;
            ns1:s3_access_key "<redacted>" ;
            ns1:s3_secret_key "<redacted>" ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "chlorophyll_a": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
      "type": "image/png"
    }
  ],
  "cyanobacteria": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
      "type": "image/png"
    }
  ],
  "turbidity": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
      "type": "image/png"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "chlorophyll_a": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "chlorophyll_a_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
      "type": "image/png"
    }
  ],
  "cyanobacteria": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "cyanobacteria_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
      "type": "image/png"
    }
  ],
  "turbidity": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_color": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
      "type": "image/tiff; application=geotiff"
    }
  ],
  "turbidity_plot": [
    {
      "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
      "type": "image/png"
    }
  ]
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:chlorophyll_a [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff" ] ;
    pp:chlorophyll_a_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif" ] ;
    pp:chlorophyll_a_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png" ] ;
    pp:cyanobacteria [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff" ] ;
    pp:cyanobacteria_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif" ] ;
    pp:cyanobacteria_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png" ] ;
    pp:turbidity [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff" ] ;
    pp:turbidity_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif" ] ;
    pp:turbidity_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:algae-bloom:workflow-copernicus",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus",
    "startedAtTime": "2026-09-23T07:31:01Z",
    "used": [
      "urn:example:entity:workflow-copernicus:in:aoi",
      "urn:example:entity:workflow-copernicus:in:collection",
      "urn:example:entity:workflow-copernicus:in:date",
      "urn:example:entity:workflow-copernicus:in:delta",
      "urn:example:entity:workflow-copernicus:in:cloud_cover",
      "urn:example:entity:workflow-copernicus:in:s3_access_key",
      "urn:example:entity:workflow-copernicus:in:s3_secret_key"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus"
      }
    ],
    "endedAtTime": "2026-09-23T07:33:59Z"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:in:aoi",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/aoi",
    "links": [
      {
        "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson",
        "rel": "item",
        "type": "application/geo+json"
      }
    ]
  },
  {
    "id": "urn:example:entity:workflow-copernicus:in:collection",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/collection",
    "value": "SENTINEL-2"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:in:date",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/date",
    "value": "2019-06-29"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:in:delta",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/delta",
    "value": 4
  },
  {
    "id": "urn:example:entity:workflow-copernicus:in:cloud_cover",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/cloud_cover",
    "value": 0.1
  },
  {
    "id": "urn:example:entity:workflow-copernicus:in:s3_access_key",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/s3_access_key"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:in:s3_secret_key",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/s3_secret_key"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:chlorophyll_a",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:chlorophyll_a_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:chlorophyll_a_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
        "rel": "item",
        "type": "image/png"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:cyanobacteria",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:cyanobacteria_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:cyanobacteria_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
        "rel": "item",
        "type": "image/png"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:turbidity",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:turbidity_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus:out:turbidity_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
    "wasDerivedFrom": [
      "urn:example:entity:workflow-copernicus:in:aoi"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:algae-bloom:workflow-copernicus",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus",
      "startedAtTime": "2026-09-23T07:31:01Z",
      "used": [
        "urn:example:entity:workflow-copernicus:in:aoi",
        "urn:example:entity:workflow-copernicus:in:collection",
        "urn:example:entity:workflow-copernicus:in:date",
        "urn:example:entity:workflow-copernicus:in:delta",
        "urn:example:entity:workflow-copernicus:in:cloud_cover",
        "urn:example:entity:workflow-copernicus:in:s3_access_key",
        "urn:example:entity:workflow-copernicus:in:s3_secret_key"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus"
        }
      ],
      "endedAtTime": "2026-09-23T07:33:59Z"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:in:aoi",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/aoi",
      "links": [
        {
          "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/example/algae-usecase-region.geojson",
          "rel": "item",
          "type": "application/geo+json"
        }
      ]
    },
    {
      "id": "urn:example:entity:workflow-copernicus:in:collection",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/collection",
      "value": "SENTINEL-2"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:in:date",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/date",
      "value": "2019-06-29"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:in:delta",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/delta",
      "value": 4
    },
    {
      "id": "urn:example:entity:workflow-copernicus:in:cloud_cover",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/cloud_cover",
      "value": 0.1
    },
    {
      "id": "urn:example:entity:workflow-copernicus:in:s3_access_key",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/s3_access_key"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:in:s3_secret_key",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/s3_secret_key"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:chlorophyll_a",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:chlorophyll_a_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:chlorophyll_a_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
          "rel": "item",
          "type": "image/png"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:cyanobacteria",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:cyanobacteria_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:cyanobacteria_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
          "rel": "item",
          "type": "image/png"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:turbidity",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:turbidity_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus:out:turbidity_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus",
      "wasDerivedFrom": [
        "urn:example:entity:workflow-copernicus:in:aoi"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
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

<urn:example:entity:workflow-copernicus:out:chlorophyll_a> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:chlorophyll_a_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:chlorophyll_a_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:cyanobacteria> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:cyanobacteria_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:cyanobacteria_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:turbidity> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:turbidity_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:out:turbidity_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:workflow-copernicus:in:aoi> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus> .

<urn:example:entity:workflow-copernicus:in:cloud_cover> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/cloud_cover> ;
    rdf:value 1e-01 .

<urn:example:entity:workflow-copernicus:in:collection> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/collection> ;
    rdf:value "SENTINEL-2" .

<urn:example:entity:workflow-copernicus:in:date> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/date> ;
    rdf:value "2019-06-29" .

<urn:example:entity:workflow-copernicus:in:delta> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/delta> ;
    rdf:value 4 .

<urn:example:entity:workflow-copernicus:in:s3_access_key> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/s3_access_key> .

<urn:example:entity:workflow-copernicus:in:s3_secret_key> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/s3_secret_key> .

<urn:example:run:algae-bloom:workflow-copernicus> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus> ;
    prov:endedAtTime "2026-09-23T07:33:59+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus> ] ;
    prov:startedAtTime "2026-09-23T07:31:01+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:workflow-copernicus:in:aoi>,
        <urn:example:entity:workflow-copernicus:in:cloud_cover>,
        <urn:example:entity:workflow-copernicus:in:collection>,
        <urn:example:entity:workflow-copernicus:in:date>,
        <urn:example:entity:workflow-copernicus:in:delta>,
        <urn:example:entity:workflow-copernicus:in:s3_access_key>,
        <urn:example:entity:workflow-copernicus:in:s3_secret_key> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .

<urn:example:entity:workflow-copernicus:in:aoi> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#inputs/aoi> ;
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
    "id": "urn:example:run:algae-bloom:workflow-copernicus",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "algae-bloom-workflow-copernicus-0001",
    "startedAtTime": "2026-09-23T07:31:01Z",
    "endedAtTime": "2026-09-23T07:33:59Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:algae-bloom:select-products-sentinel2"
      },
      {
        "id": "urn:example:run:algae-bloom:workflow-copernicus-process"
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
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "3b00d9df28c7548e79088d660b1d416953bdb464"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "e6006027bca29c0e9abb13482a5deea81527097b"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "9cf89d0572c2a7632f7e096b040d37f8a99b4307"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b90b2dee65d0b638143e2788b825e245dbe9c4bb"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1b832fde3fc0d94955508d006d745a0a9e9b9596"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1e0302087d93ff81d5ec6b3a7a63ad7d0daec758"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "823dc9c0e24073601b98c7ac80d545355715c6f5"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "92c53811eb6d7bad871be5ebee515b4f95e0336a"
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "run": {
    "id": "urn:example:run:algae-bloom:workflow-copernicus",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "algae-bloom-workflow-copernicus-0001",
    "startedAtTime": "2026-09-23T07:31:01Z",
    "endedAtTime": "2026-09-23T07:33:59Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:algae-bloom:select-products-sentinel2"
      },
      {
        "id": "urn:example:run:algae-bloom:workflow-copernicus-process"
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
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "3b00d9df28c7548e79088d660b1d416953bdb464"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "e6006027bca29c0e9abb13482a5deea81527097b"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "9cf89d0572c2a7632f7e096b040d37f8a99b4307"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b90b2dee65d0b638143e2788b825e245dbe9c4bb"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1b832fde3fc0d94955508d006d745a0a9e9b9596"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1e0302087d93ff81d5ec6b3a7a63ad7d0daec758"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "823dc9c0e24073601b98c7ac80d545355715c6f5"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "92c53811eb6d7bad871be5ebee515b4f95e0336a"
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

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "3b00d9df28c7548e79088d660b1d416953bdb464" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "e6006027bca29c0e9abb13482a5deea81527097b" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "9cf89d0572c2a7632f7e096b040d37f8a99b4307" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/chlorophyll_a_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "b90b2dee65d0b638143e2788b825e245dbe9c4bb" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "1b832fde3fc0d94955508d006d745a0a9e9b9596" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/cyanobacteria_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "1e0302087d93ff81d5ec6b3a7a63ad7d0daec758" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "823dc9c0e24073601b98c7ac80d545355715c6f5" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-copernicus> ;
    ns1:checksum [ rdf:value "92c53811eb6d7bad871be5ebee515b4f95e0336a" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus#outputs/turbidity_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<urn:example:engine:cwltool-3.1.20260108082145> a wfprov:WorkflowEngine ;
    pp:name "cwltool" ;
    pp:version "3.1.20260108082145" .

<urn:example:run:algae-bloom:workflow-copernicus> a wfprov:WorkflowRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus> ;
    wfprov:describedByWorkflow <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus> ;
    wfprov:hadSubProcessRun <urn:example:run:algae-bloom:select-products-sentinel2>,
        <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    prov:endedAtTime "2026-09-23T07:33:59+00:00"^^xsd:dateTime ;
    prov:startedAtTime "2026-09-23T07:31:01+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:jobID "algae-bloom-workflow-copernicus-0001" ;
    pp:status "successful" .

[] pp:engine <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:run <urn:example:run:algae-bloom:workflow-copernicus> ;
    proc:outputs <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus",
  "type": "ProcessType",
  "prefLabel": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.",
  "definition": "Finds Sentinel-2 products on Copernicus using filtering parameters and performs band calculation on retrieved Sentinel-2 products to evaluate algae bloom for water quality assessment.",
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
  "profile": "ospd.process-profiles.algae-bloom.workflow-copernicus",
  "processDescription": {
    "id": "algae-usecase-workflow-copernicus",
    "version": "2.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl",
    "cwlClass": "Workflow",
    "cwlId": "algae-usecase-workflow-copernicus",
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
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite; same structure as the Earth-Search variant but over Copernicus Data Space (SAFE products on S3, credentials required). openEO hides credentials in the back-end.",
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
        "level": "none"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus",
  "type": "ProcessType",
  "prefLabel": "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.",
  "definition": "Finds Sentinel-2 products on Copernicus using filtering parameters and performs band calculation on retrieved Sentinel-2 products to evaluate algae bloom for water quality assessment.",
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
  "profile": "ospd.process-profiles.algae-bloom.workflow-copernicus",
  "processDescription": {
    "id": "algae-usecase-workflow-copernicus",
    "version": "2.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl",
    "cwlClass": "Workflow",
    "cwlId": "algae-usecase-workflow-copernicus",
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
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite; same structure as the Earth-Search variant but over Copernicus Data Space (SAFE products on S3, credentials required). openEO hides credentials in the back-end.",
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
        "level": "none"
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

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/filter-configuration>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/pre-processing>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/selection-filtering> ;
    skos:definition "Finds Sentinel-2 products on Copernicus using filtering parameters and performs band calculation on retrieved Sentinel-2 products to evaluate algae bloom for water quality assessment." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform." ;
    pp:candidateCctDependency "eoap.cct.geojson",
        "eoap.cct.string-format" ;
    pp:hasStep <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/select-products-sentinel2>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process> ;
    pp:openeoEquivalence [ pp:decomposition ( [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.load_collection" ;
                        pp:stage "select_products" ] [ pp:equivalenceLevel "none" ;
                        pp:stage "process (scatter over urls)" ] ) ;
            pp:equivalenceLevel "none" ;
            pp:rationale "Composite; same structure as the Earth-Search variant but over Copernicus Data Space (SAFE products on S3, credentials required). openEO hides credentials in the back-end." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus> ;
    pp:profile "ospd.process-profiles.algae-bloom.workflow-copernicus" ;
    pp:provenanceClass wfprov:WorkflowRun ;
    pp:source [ pp:cwl <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus.cwl> ;
            pp:cwlClass "Workflow" ;
            pp:cwlId "algae-usecase-workflow-copernicus" ;
            pp:license "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus> pp:version "2.0.0" .


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
      "researchobject": "arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/",
      "metadata": "arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/metadata/",
      "provenance": "arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/metadata/provenance/",
      "wf": "arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#",
      "input": "arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/primary-job.json#",
      "wf4ever": "http://purl.org/wf4ever/wf4ever#"
    },
    "https://openprovenance.org/prov-jsonld/context.jsonld"
  ],
  "@graph": [
    {
      "@type": "Agent",
      "@id": "id:5001cc2f-8b7b-4b93-9043-8ce09886304f"
    },
    {
      "@type": "Agent",
      "@id": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
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
      "@id": "id:925ed775-3f3c-444a-b740-a81e965f32e0",
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
      "activity": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "starter": "id:5001cc2f-8b7b-4b93-9043-8ce09886304f",
      "time": "2026-09-23T09:31:01.086649"
    },
    {
      "@type": "Start",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "starter": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "time": "2026-09-23T09:31:01.086687"
    },
    {
      "@type": "Start",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "starter": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:31:02.350383"
    },
    {
      "@type": "Start",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "starter": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:31:06.036894"
    },
    {
      "@type": "Activity",
      "@id": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "startTime": "2026-09-23T09:31:01.086664",
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
      "@id": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
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
      "@id": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/algae-usecase-workflow-copernicus/process"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "prov:has_provenance": [
        {
          "@value": "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.nt",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.jsonld",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.json",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.xml",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.provn",
          "@type": "xsd:QName"
        },
        {
          "@value": "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/select_products"
    },
    {
      "@type": "Association",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "agent": "id:925ed775-3f3c-444a-b740-a81e965f32e0"
    },
    {
      "@type": "Association",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/algae-usecase-workflow-copernicus/process"
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
      "@id": "wf:main/select_products",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/process",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
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
      "@id": "id:cea98bc9-4a78-442d-a99a-eb4850b01d63",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
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
      "@id": "id:c719b109-a5e5-414b-8e1a-2fa5262c9394",
      "value": [
        {
          "@value": "0.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:d184cbedd77b80cede3f63388a471a8634278cf3",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "SENTINEL-2"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:d184cbedd77b80cede3f63388a471a8634278cf3",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "SENTINEL-2"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:aae1ba7d07b94e0929479a0ed4c1ec64718ac191",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "2019-06-29"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:aae1ba7d07b94e0929479a0ed4c1ec64718ac191",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "2019-06-29"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:97f268f3-383e-43a2-ad2b-3212b43b5676",
      "value": [
        {
          "@value": "4",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "(secret-bf20402e-6bb5-4f48-bf22-6d3ef7bff99c)"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "(secret-12440283-71a1-46b4-9702-9c8e432a31e6)"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:653d2ec7-333d-431e-81c5-d30c4c02282a",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
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
      "@id": "data:8bfeb7b030ae1994f504c6c9ec46111b90434378",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "copernicus"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c5d12ec5-693c-4ae4-9157-ffaf8e84a5a2",
      "value": [
        {
          "@value": "0.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:fc839955-c480-42b7-a657-730494fc154e",
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5e7cb55727e375cb72dac733c05c4c81c30ffaae",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "s3:///eodata/Sentinel-2/MSI/L2A_N0500/2019/07/01/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542.SAFE"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:7d2099b8-1e52-4533-8140-dfb685676d26",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:3b00d9df28c7548e79088d660b1d416953bdb464"
    },
    {
      "@type": "Entity",
      "@id": "id:7fb56c04-4cb6-45f5-923c-390c6520ae3a",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a"
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
      "@id": "id:a47fc7dc-2f9a-4925-aacf-c93722a523cd",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e6006027bca29c0e9abb13482a5deea81527097b"
    },
    {
      "@type": "Entity",
      "@id": "id:8fe98067-8e97-40b6-a99a-cf787f26fa36",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color"
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
      "@id": "id:398fcc75-135c-469b-88f3-3e233dd75a21",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9cf89d0572c2a7632f7e096b040d37f8a99b4307"
    },
    {
      "@type": "Entity",
      "@id": "id:ed443e92-82d0-40c9-b63e-724fba739364",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot"
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
      "@id": "id:a5265478-cf9f-4fdd-9446-cb47cfe5629a",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b90b2dee65d0b638143e2788b825e245dbe9c4bb"
    },
    {
      "@type": "Entity",
      "@id": "id:1855b873-514a-46e8-85f9-7e6fdd5c1c12",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria"
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
      "@id": "id:af10a7c3-f90c-434e-820f-0ce388d38dcf",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1"
    },
    {
      "@type": "Entity",
      "@id": "id:29f23348-9547-4fef-b002-ceefd5b2471b",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color"
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
      "@id": "id:6627362d-c06e-46d9-9217-cb29e2dc2c49",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:1b832fde3fc0d94955508d006d745a0a9e9b9596"
    },
    {
      "@type": "Entity",
      "@id": "id:7e671680-4e90-4584-89b1-36260f670af1",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot"
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
      "@id": "id:d7988ddd-8e9e-4bba-aaa5-4cc0ed49fd4e",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758"
    },
    {
      "@type": "Entity",
      "@id": "id:0a64bae7-5f25-441b-b114-51f6437fb00f",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity"
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
      "@id": "id:fcab6658-7e8a-4045-9086-8daf16ffa739",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:823dc9c0e24073601b98c7ac80d545355715c6f5"
    },
    {
      "@type": "Entity",
      "@id": "id:a9c95e1a-ef39-4627-8292-d1020e85dfa1",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color"
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
      "@id": "id:759b68d0-f11e-471f-9055-67965a9955c9",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:92c53811eb6d7bad871be5ebee515b4f95e0336a"
    },
    {
      "@type": "Entity",
      "@id": "id:3b413d9a-adab-454b-8670-0cf37423eec6",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot"
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
      "@id": "id:d6c2d96d-b204-406d-90a1-122d95408dfc",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:cea98bc9-4a78-442d-a99a-eb4850b01d63",
      "generalEntity": "data:09b3c69758a531dc4f198b8a083607dc5a617e4f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:653d2ec7-333d-431e-81c5-d30c4c02282a",
      "generalEntity": "data:09b3c69758a531dc4f198b8a083607dc5a617e4f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:7fb56c04-4cb6-45f5-923c-390c6520ae3a",
      "generalEntity": "data:3b00d9df28c7548e79088d660b1d416953bdb464"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:8fe98067-8e97-40b6-a99a-cf787f26fa36",
      "generalEntity": "data:e6006027bca29c0e9abb13482a5deea81527097b"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:ed443e92-82d0-40c9-b63e-724fba739364",
      "generalEntity": "data:9cf89d0572c2a7632f7e096b040d37f8a99b4307"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1855b873-514a-46e8-85f9-7e6fdd5c1c12",
      "generalEntity": "data:b90b2dee65d0b638143e2788b825e245dbe9c4bb"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:29f23348-9547-4fef-b002-ceefd5b2471b",
      "generalEntity": "data:b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:7e671680-4e90-4584-89b1-36260f670af1",
      "generalEntity": "data:1b832fde3fc0d94955508d006d745a0a9e9b9596"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:0a64bae7-5f25-441b-b114-51f6437fb00f",
      "generalEntity": "data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:a9c95e1a-ef39-4627-8292-d1020e85dfa1",
      "generalEntity": "data:823dc9c0e24073601b98c7ac80d545355715c6f5"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3b413d9a-adab-454b-8670-0cf37423eec6",
      "generalEntity": "data:92c53811eb6d7bad871be5ebee515b4f95e0336a"
    },
    {
      "@type": "Usage",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "entity": "id:cea98bc9-4a78-442d-a99a-eb4850b01d63",
      "time": "2026-09-23T09:31:02.346121",
      "role": [
        "wf:main/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "entity": "id:c719b109-a5e5-414b-8e1a-2fa5262c9394",
      "time": "2026-09-23T09:31:02.346187",
      "role": [
        "wf:main/cloud_cover"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "entity": "data:d184cbedd77b80cede3f63388a471a8634278cf3",
      "time": "2026-09-23T09:31:02.347208",
      "role": [
        "wf:main/collection"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "entity": "data:aae1ba7d07b94e0929479a0ed4c1ec64718ac191",
      "time": "2026-09-23T09:31:02.347708",
      "role": [
        "wf:main/date"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "entity": "id:97f268f3-383e-43a2-ad2b-3212b43b5676",
      "time": "2026-09-23T09:31:02.347746",
      "role": [
        "wf:main/delta"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "entity": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "time": "2026-09-23T09:31:02.348133",
      "role": [
        "wf:main/s3_access_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "entity": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "time": "2026-09-23T09:31:02.348450",
      "role": [
        "wf:main/s3_secret_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "id:653d2ec7-333d-431e-81c5-d30c4c02282a",
      "time": "2026-09-23T09:31:02.391633",
      "role": [
        "wf:main/select_products/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "data:8bfeb7b030ae1994f504c6c9ec46111b90434378",
      "time": "2026-09-23T09:31:02.391980",
      "role": [
        "wf:main/select_products/catalog"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "id:c5d12ec5-693c-4ae4-9157-ffaf8e84a5a2",
      "time": "2026-09-23T09:31:02.392016",
      "role": [
        "wf:main/select_products/cloud_cover"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "data:d184cbedd77b80cede3f63388a471a8634278cf3",
      "time": "2026-09-23T09:31:02.392236",
      "role": [
        "wf:main/select_products/collection"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "data:aae1ba7d07b94e0929479a0ed4c1ec64718ac191",
      "time": "2026-09-23T09:31:02.392439",
      "role": [
        "wf:main/select_products/date"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "id:fc839955-c480-42b7-a657-730494fc154e",
      "time": "2026-09-23T09:31:02.392462",
      "role": [
        "wf:main/select_products/delta"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "data:632ab110c744c188c9ae98cb2c6b74767894037a",
      "time": "2026-09-23T09:31:02.392701",
      "role": [
        "wf:main/select_products/product_level"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:02.392720",
      "role": [
        "wf:main/select_products/toi"
      ]
    },
    {
      "@type": "Membership",
      "collection": "id:7d2099b8-1e52-4533-8140-dfb685676d26",
      "entity": "data:5e7cb55727e375cb72dac733c05c4c81c30ffaae"
    },
    {
      "@type": "Membership",
      "collection": "id:a47fc7dc-2f9a-4925-aacf-c93722a523cd",
      "entity": "id:7fb56c04-4cb6-45f5-923c-390c6520ae3a"
    },
    {
      "@type": "Membership",
      "collection": "id:398fcc75-135c-469b-88f3-3e233dd75a21",
      "entity": "id:8fe98067-8e97-40b6-a99a-cf787f26fa36"
    },
    {
      "@type": "Membership",
      "collection": "id:a5265478-cf9f-4fdd-9446-cb47cfe5629a",
      "entity": "id:ed443e92-82d0-40c9-b63e-724fba739364"
    },
    {
      "@type": "Membership",
      "collection": "id:af10a7c3-f90c-434e-820f-0ce388d38dcf",
      "entity": "id:1855b873-514a-46e8-85f9-7e6fdd5c1c12"
    },
    {
      "@type": "Membership",
      "collection": "id:6627362d-c06e-46d9-9217-cb29e2dc2c49",
      "entity": "id:29f23348-9547-4fef-b002-ceefd5b2471b"
    },
    {
      "@type": "Membership",
      "collection": "id:d7988ddd-8e9e-4bba-aaa5-4cc0ed49fd4e",
      "entity": "id:7e671680-4e90-4584-89b1-36260f670af1"
    },
    {
      "@type": "Membership",
      "collection": "id:fcab6658-7e8a-4045-9086-8daf16ffa739",
      "entity": "id:0a64bae7-5f25-441b-b114-51f6437fb00f"
    },
    {
      "@type": "Membership",
      "collection": "id:759b68d0-f11e-471f-9055-67965a9955c9",
      "entity": "id:a9c95e1a-ef39-4627-8292-d1020e85dfa1"
    },
    {
      "@type": "Membership",
      "collection": "id:d6c2d96d-b204-406d-90a1-122d95408dfc",
      "entity": "id:3b413d9a-adab-454b-8670-0cf37423eec6"
    },
    {
      "@type": "Generation",
      "entity": "id:7d2099b8-1e52-4533-8140-dfb685676d26",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "time": "2026-09-23T09:31:06.035288",
      "role": [
        "wf:main/select_products/urls"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a47fc7dc-2f9a-4925-aacf-c93722a523cd",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/chlorophyll_a"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:398fcc75-135c-469b-88f3-3e233dd75a21",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/chlorophyll_a_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a5265478-cf9f-4fdd-9446-cb47cfe5629a",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/chlorophyll_a_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:af10a7c3-f90c-434e-820f-0ce388d38dcf",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/cyanobacteria"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6627362d-c06e-46d9-9217-cb29e2dc2c49",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/cyanobacteria_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d7988ddd-8e9e-4bba-aaa5-4cc0ed49fd4e",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/cyanobacteria_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:fcab6658-7e8a-4045-9086-8daf16ffa739",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/turbidity"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:759b68d0-f11e-471f-9055-67965a9955c9",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/turbidity_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d6c2d96d-b204-406d-90a1-122d95408dfc",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:33:59.467940",
      "role": [
        "wf:main/primary/turbidity_plot"
      ]
    },
    {
      "@type": "End",
      "activity": "id:3b68ba23-95c2-48fc-92bb-753f98188bf2",
      "ender": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "time": "2026-09-23T09:31:06.035275"
    },
    {
      "@type": "End",
      "activity": "id:44c595c3-0138-459e-bff2-432829fe1bf3",
      "ender": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "time": "2026-09-23T09:33:59.469201"
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
@prefix wf: <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#> .
@prefix wf4ever: <http://purl.org/wf4ever/wf4ever#> .
@prefix wfdesc: <http://purl.org/wf4ever/wfdesc#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/process> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

id:0470b6f9-f5c0-484c-bb2e-534806f95d65 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/algae-usecase-workflow-copernicus/process" ;
    prov:has_provenance "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.json"^^xsd:QName,
        "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.jsonld"^^xsd:QName,
        "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.nt"^^xsd:QName,
        "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.provn"^^xsd:QName,
        "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.ttl"^^xsd:QName,
        "provenance:workflow_20process.0470b6f9-f5c0-484c-bb2e-534806f95d65.cwlprov.xml"^^xsd:QName ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/algae-usecase-workflow-copernicus/process> ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:06.036894"^^xsd:dateTime ;
            prov:hadActivity id:44c595c3-0138-459e-bff2-432829fe1bf3 ] .

id:398fcc75-135c-469b-88f3-3e233dd75a21 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/chlorophyll_a_color> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:8fe98067-8e97-40b6-a99a-cf787f26fa36 ] .

id:6627362d-c06e-46d9-9217-cb29e2dc2c49 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/cyanobacteria_color> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:29f23348-9547-4fef-b002-ceefd5b2471b ] .

id:759b68d0-f11e-471f-9055-67965a9955c9 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/turbidity_color> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:a9c95e1a-ef39-4627-8292-d1020e85dfa1 ] .

id:7d2099b8-1e52-4533-8140-dfb685676d26 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:3b68ba23-95c2-48fc-92bb-753f98188bf2 ;
            prov:atTime "2026-09-23T09:31:06.035288"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/urls> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:5e7cb55727e375cb72dac733c05c4c81c30ffaae ] .

id:a47fc7dc-2f9a-4925-aacf-c93722a523cd a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/chlorophyll_a> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:7fb56c04-4cb6-45f5-923c-390c6520ae3a ] .

id:a5265478-cf9f-4fdd-9446-cb47cfe5629a a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/chlorophyll_a_plot> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:ed443e92-82d0-40c9-b63e-724fba739364 ] .

id:af10a7c3-f90c-434e-820f-0ce388d38dcf a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/cyanobacteria> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:1855b873-514a-46e8-85f9-7e6fdd5c1c12 ] .

id:d6c2d96d-b204-406d-90a1-122d95408dfc a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/turbidity_plot> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:3b413d9a-adab-454b-8670-0cf37423eec6 ] .

id:d7988ddd-8e9e-4bba-aaa5-4cc0ed49fd4e a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/cyanobacteria_plot> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:7e671680-4e90-4584-89b1-36260f670af1 ] .

id:fcab6658-7e8a-4045-9086-8daf16ffa739 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:44c595c3-0138-459e-bff2-432829fe1bf3 ;
            prov:atTime "2026-09-23T09:33:59.467940"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/primary/turbidity> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:0a64bae7-5f25-441b-b114-51f6437fb00f ] .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/process"^^xsd:QName,
        "wf:main/select_products"^^xsd:QName .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

cwlprov:None a prov:Entity ;
    rdfs:label "None" .

data:1b832fde3fc0d94955508d006d745a0a9e9b9596 a prov:Entity .

data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758 a prov:Entity .

data:3b00d9df28c7548e79088d660b1d416953bdb464 a prov:Entity .

data:5e7cb55727e375cb72dac733c05c4c81c30ffaae a wfprov:Artifact,
        prov:Entity ;
    prov:value "s3:///eodata/Sentinel-2/MSI/L2A_N0500/2019/07/01/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542.SAFE" .

data:632ab110c744c188c9ae98cb2c6b74767894037a a wfprov:Artifact,
        prov:Entity ;
    prov:value "L2A" .

data:823dc9c0e24073601b98c7ac80d545355715c6f5 a prov:Entity .

data:8bfeb7b030ae1994f504c6c9ec46111b90434378 a wfprov:Artifact,
        prov:Entity ;
    prov:value "copernicus" .

data:92c53811eb6d7bad871be5ebee515b4f95e0336a a prov:Entity .

data:9cf89d0572c2a7632f7e096b040d37f8a99b4307 a prov:Entity .

data:b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1 a prov:Entity .

data:b75fa50f91a9dd377927a83994bff64245718790 a wfprov:Artifact,
        prov:Entity ;
    prov:value "(secret-bf20402e-6bb5-4f48-bf22-6d3ef7bff99c)" .

data:b90b2dee65d0b638143e2788b825e245dbe9c4bb a prov:Entity .

data:e6006027bca29c0e9abb13482a5deea81527097b a prov:Entity .

data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 a wfprov:Artifact,
        prov:Entity ;
    prov:value "(secret-12440283-71a1-46b4-9702-9c8e432a31e6)" .

id:0a64bae7-5f25-441b-b114-51f6437fb00f a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity" .

id:1855b873-514a-46e8-85f9-7e6fdd5c1c12 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:b90b2dee65d0b638143e2788b825e245dbe9c4bb ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria" .

id:29f23348-9547-4fef-b002-ceefd5b2471b a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color" .

id:3b413d9a-adab-454b-8670-0cf37423eec6 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:92c53811eb6d7bad871be5ebee515b4f95e0336a ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot" .

id:3b68ba23-95c2-48fc-92bb-753f98188bf2 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/select_products" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:925ed775-3f3c-444a-b740-a81e965f32e0 ],
        [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:06.035275"^^xsd:dateTime ;
            prov:hadActivity id:44c595c3-0138-459e-bff2-432829fe1bf3 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:02.350383"^^xsd:dateTime ;
            prov:hadActivity id:44c595c3-0138-459e-bff2-432829fe1bf3 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.392236"^^xsd:dateTime ;
            prov:entity data:d184cbedd77b80cede3f63388a471a8634278cf3 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/collection> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.391980"^^xsd:dateTime ;
            prov:entity data:8bfeb7b030ae1994f504c6c9ec46111b90434378 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/catalog> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.391633"^^xsd:dateTime ;
            prov:entity id:653d2ec7-333d-431e-81c5-d30c4c02282a ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.392016"^^xsd:dateTime ;
            prov:entity id:c5d12ec5-693c-4ae4-9157-ffaf8e84a5a2 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/cloud_cover> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.392439"^^xsd:dateTime ;
            prov:entity data:aae1ba7d07b94e0929479a0ed4c1ec64718ac191 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/date> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.392462"^^xsd:dateTime ;
            prov:entity id:fc839955-c480-42b7-a657-730494fc154e ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/delta> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.392701"^^xsd:dateTime ;
            prov:entity data:632ab110c744c188c9ae98cb2c6b74767894037a ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/product_level> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.392720"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/select_products/toi> ] .

id:5001cc2f-8b7b-4b93-9043-8ce09886304f a prov:Agent .

id:653d2ec7-333d-431e-81c5-d30c4c02282a a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:09b3c69758a531dc4f198b8a083607dc5a617e4f ] ;
    cwlprov:basename "algae-usecase-region.geojson" ;
    cwlprov:nameext ".geojson" ;
    cwlprov:nameroot "algae-usecase-region" .

id:7e671680-4e90-4584-89b1-36260f670af1 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:1b832fde3fc0d94955508d006d745a0a9e9b9596 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot" .

id:7fb56c04-4cb6-45f5-923c-390c6520ae3a a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:3b00d9df28c7548e79088d660b1d416953bdb464 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a" .

id:8fe98067-8e97-40b6-a99a-cf787f26fa36 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e6006027bca29c0e9abb13482a5deea81527097b ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color" .

id:925ed775-3f3c-444a-b740-a81e965f32e0 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/select-products-sentinel2:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/select-products-sentinel2:1.1.0" .

id:97f268f3-383e-43a2-ad2b-3212b43b5676 a prov:Entity ;
    prov:value "4"^^xsd:int .

id:a9c95e1a-ef39-4627-8292-d1020e85dfa1 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:823dc9c0e24073601b98c7ac80d545355715c6f5 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color" .

id:c5d12ec5-693c-4ae4-9157-ffaf8e84a5a2 a prov:Entity ;
    prov:value 1e-01 .

id:c719b109-a5e5-414b-8e1a-2fa5262c9394 a prov:Entity ;
    prov:value 1e-01 .

id:cea98bc9-4a78-442d-a99a-eb4850b01d63 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:09b3c69758a531dc4f198b8a083607dc5a617e4f ] ;
    cwlprov:basename "algae-usecase-region.geojson" ;
    cwlprov:nameext ".geojson" ;
    cwlprov:nameroot "algae-usecase-region" .

id:ed443e92-82d0-40c9-b63e-724fba739364 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:9cf89d0572c2a7632f7e096b040d37f8a99b4307 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot" .

id:fc839955-c480-42b7-a657-730494fc154e a prov:Entity ;
    prov:value "4"^^xsd:int .

data:09b3c69758a531dc4f198b8a083607dc5a617e4f a wfprov:Artifact,
        prov:Entity .

data:aae1ba7d07b94e0929479a0ed4c1ec64718ac191 a wfprov:Artifact,
        prov:Entity ;
    prov:value "2019-06-29" .

data:d184cbedd77b80cede3f63388a471a8634278cf3 a wfprov:Artifact,
        prov:Entity ;
    prov:value "SENTINEL-2" .

id:63709288-2770-4d4f-97fa-3e8ff70d0b32 a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:01.086649"^^xsd:dateTime ;
            prov:hadActivity id:5001cc2f-8b7b-4b93-9043-8ce09886304f ] .

id:44c595c3-0138-459e-bff2-432829fe1bf3 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:33:59.469201"^^xsd:dateTime ;
            prov:hadActivity id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:01.086687"^^xsd:dateTime ;
            prov:hadActivity id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.346121"^^xsd:dateTime ;
            prov:entity id:cea98bc9-4a78-442d-a99a-eb4850b01d63 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.347746"^^xsd:dateTime ;
            prov:entity id:97f268f3-383e-43a2-ad2b-3212b43b5676 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/delta> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.348133"^^xsd:dateTime ;
            prov:entity data:b75fa50f91a9dd377927a83994bff64245718790 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/s3_access_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.347208"^^xsd:dateTime ;
            prov:entity data:d184cbedd77b80cede3f63388a471a8634278cf3 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/collection> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.347708"^^xsd:dateTime ;
            prov:entity data:aae1ba7d07b94e0929479a0ed4c1ec64718ac191 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/date> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.348450"^^xsd:dateTime ;
            prov:entity data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/s3_secret_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:02.346187"^^xsd:dateTime ;
            prov:entity id:c719b109-a5e5-414b-8e1a-2fa5262c9394 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/cloud_cover> ] ;
    prov:startedAtTime "2026-09-23T09:31:01.086664"^^xsd:dateTime .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `algae-usecase-workflow-copernicus`
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
      const: algae-usecase-workflow-copernicus
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - date
      - delta
      - aoi
      - collection
      - cloud_cover
      - s3_access_key
      - s3_secret_key
      propertyNames:
        enum:
        - date
        - delta
        - aoi
        - collection
        - cloud_cover
        - s3_access_key
        - s3_secret_key
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
        - date
        - aoi
        - collection
        - s3_access_key
        - s3_secret_key
        propertyNames:
          enum:
          - date
          - delta
          - aoi
          - collection
          - cloud_cover
          - s3_access_key
          - s3_secret_key
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/algae-bloom/workflow-copernicus`

