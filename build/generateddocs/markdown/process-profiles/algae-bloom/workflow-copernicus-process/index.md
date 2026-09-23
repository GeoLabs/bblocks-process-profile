
# Process profile: algae-usecase-workflow-copernicus-process (Schema)

`ospd.process-profiles.algae-bloom.workflow-copernicus-process` *v0.1*

OGC API - Processes profile of the CWL Workflow `algae-usecase-workflow-copernicus-process` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`algae-usecase-workflow-copernicus-process`** (Workflow, W1 Algae Bloom).

> Processing on Sentinel-2 bands to evaluate algae bloom.

## Source

- CWL: [algae-usecase-workflow-copernicus-process.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval → Scientific computation → Export / aggregation
- EOAP CWL custom types used: none; candidates: `eoap.cct.string-format`
- Steps (profiles): `ospd.process-profiles.algae-bloom.download-band-sentinel2-product-safe`, `ospd.process-profiles.algae-bloom.calculate-band`, `ospd.process-profiles.algae-bloom.plot-image`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `product_url` | string | `chlorophyll_a` | File |
| `s3_access_key` | string | `chlorophyll_a_color` | File |
| `s3_secret_key` | string | `chlorophyll_a_plot` | File |
|  |  | `cyanobacteria` | File |
|  |  | `cyanobacteria_color` | File |
|  |  | `cyanobacteria_plot` | File |
|  |  | `turbidity` | File |
|  |  | `turbidity_color` | File |
|  |  | `turbidity_plot` | File |

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `c27c60d`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-01 outputs.chlorophyll_a: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.chlorophyll_a_color: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.chlorophyll_a_plot: contentMediaType from CWL format `iana:image/png` -> `image/png`; contentEncoding binary
- M-01 outputs.cyanobacteria: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.cyanobacteria_color: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.cyanobacteria_plot: contentMediaType from CWL format `iana:image/png` -> `image/png`; contentEncoding binary
- M-01 outputs.turbidity: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.turbidity_color: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.turbidity_plot: contentMediaType from CWL format `iana:image/png` -> `image/png`; contentEncoding binary
- M-04 inputs.s3_access_key: declared in cwltool:Secrets -> writeOnly: true
- M-04 inputs.s3_secret_key: declared in cwltool:Secrets -> writeOnly: true

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.

The workflow run is also given as an `ogc.bbr.provenance.execution` bundle.

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-copernicus`: Copernicus variant of the pinned W1 package, `cwltool --outdir ./results1 --provenance ./PROV1 algae-usecase-workflow-copernicus.cwl example/algae-usecase-job-copernicus.yml` with Copernicus Data Space S3 credentials, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; one product (S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542). cwltool writes the `cwltool:Secrets` inputs as `(secret-<uuid>)` placeholders in the research object), activity `main` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Composite (11 steps). No resampling step: the SAFE product already provides 60 m bands, so B03 60 m is downloaded directly instead of being resampled.


| Stage | openEO | Level | Note |
|---|---|---|---|
| download_b0x (x5) | `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands` | closeMatch |  |
| calculate_* (x3) | `ogc.openeo.processes.cubes.reduce_dimension` | closeMatch |  |
| plot_* (x3) | `ogc.openeo.processes.cubes.save_result` | closeMatch | partial |

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL Workflow is referenced, not copied: <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl>.

### processDescription
OGC API - Processes processDescription derived from the CWL (manually corrected, see description).
#### json
```json
{
  "id": "algae-usecase-workflow-copernicus-process",
  "version": "2.1.0",
  "title": "Processing on Sentinel-2 bands to evaluate algae bloom.\n",
  "description": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n",
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
      "value": "Processing on Sentinel-2 bands to evaluate algae bloom.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "2.1.0"
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
    },
    {
      "role": "https://schema.org/isBasedOn",
      "value": "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/se2waq/"
    }
  ],
  "inputs": {
    "product_url": {
      "title": "Sentinel-2 SAFE product S3 reference",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_access_key": {
      "title": "S3 access key required if found products are hosted on a protected S3 location.",
      "description": "",
      "schema": {
        "type": "string",
        "writeOnly": true
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required if found products are hosted on a protected S3 location.",
      "description": "",
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
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "chlorophyll_a_color": {
      "title": "chlorophyll_a_color",
      "description": "Pseudo-color representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "chlorophyll_a_plot": {
      "title": "chlorophyll_a_plot",
      "description": "Plot representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/png"
      }
    },
    "cyanobacteria": {
      "title": "cyanobacteria",
      "description": "",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "cyanobacteria_color": {
      "title": "cyanobacteria_color",
      "description": "Pseudo-color representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "cyanobacteria_plot": {
      "title": "cyanobacteria_plot",
      "description": "Plot representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/png"
      }
    },
    "turbidity": {
      "title": "turbidity",
      "description": "",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "turbidity_color": {
      "title": "turbidity_color",
      "description": "Pseudo-color representation of turbidity.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "turbidity_plot": {
      "title": "turbidity_plot",
      "description": "Plot representation of turbidity.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/png"
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "id": "algae-usecase-workflow-copernicus-process",
  "version": "2.1.0",
  "title": "Processing on Sentinel-2 bands to evaluate algae bloom.\n",
  "description": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n",
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
      "value": "Processing on Sentinel-2 bands to evaluate algae bloom.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "2.1.0"
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
    },
    {
      "role": "https://schema.org/isBasedOn",
      "value": "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/se2waq/"
    }
  ],
  "inputs": {
    "product_url": {
      "title": "Sentinel-2 SAFE product S3 reference",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_access_key": {
      "title": "S3 access key required if found products are hosted on a protected S3 location.",
      "description": "",
      "schema": {
        "type": "string",
        "writeOnly": true
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required if found products are hosted on a protected S3 location.",
      "description": "",
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
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "chlorophyll_a_color": {
      "title": "chlorophyll_a_color",
      "description": "Pseudo-color representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "chlorophyll_a_plot": {
      "title": "chlorophyll_a_plot",
      "description": "Plot representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/png"
      }
    },
    "cyanobacteria": {
      "title": "cyanobacteria",
      "description": "",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "cyanobacteria_color": {
      "title": "cyanobacteria_color",
      "description": "Pseudo-color representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "cyanobacteria_plot": {
      "title": "cyanobacteria_plot",
      "description": "Plot representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/png"
      }
    },
    "turbidity": {
      "title": "turbidity",
      "description": "",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "turbidity_color": {
      "title": "turbidity_color",
      "description": "Pseudo-color representation of turbidity.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "turbidity_plot": {
      "title": "turbidity_plot",
      "description": "Plot representation of turbidity.",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/png"
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
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns3: <https://w3id.org/ogc/api/schema/> .
@prefix ns4: <http://schema.org/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus-process> dcterms:description """Performs band calculation on Sentinel-2 product bands
to evaluate algae bloom for water quality assessment.
""" ;
    dcterms:subject "Copernicus",
        "OSPD",
        "algae-bloom",
        "demo",
        "water-quality" ;
    dcterms:title """Processing on Sentinel-2 bands to evaluate algae bloom.
""" ;
    pp:version "2.1.0" ;
    proc:inputs [ ns1:product_url [ dcterms:description "" ;
                    dcterms:title "Sentinel-2 SAFE product S3 reference" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:s3_access_key [ dcterms:description "" ;
                    dcterms:title "S3 access key required if found products are hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns3:writeOnly true ] ] ;
            ns1:s3_secret_key [ dcterms:description "" ;
                    dcterms:title "S3 secret key required if found products are hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns3:writeOnly true ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ],
        [ rdf:value "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/se2waq/" ;
            proc:role schema:isBasedOn ],
        [ rdf:value "2.1.0" ;
            proc:role schema:softwareVersion ],
        [ rdf:value [ a ns4:Person ;
                    ns4:email "francis.charette-migneault@crim.ca" ;
                    ns4:identifier "http://orcid.org/0000-0003-4862-3349" ;
                    ns4:name "Francis Charette-Migneault" ] ;
            proc:role schema:author ],
        [ rdf:value "https://gitlab.ogc.org/ogc/ogc-ospd" ;
            proc:role schema:codeRepository ],
        [ rdf:value """Processing on Sentinel-2 bands to evaluate algae bloom.
""" ;
            proc:role schema:name ],
        [ rdf:value """Performs band calculation on Sentinel-2 product bands
to evaluate algae bloom for water quality assessment.
""" ;
            proc:role schema:description ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns2:chlorophyll_a [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ;
            ns2:chlorophyll_a_color [ dcterms:description "Pseudo-color representation of chlorophyll-a." ;
                    dcterms:title "chlorophyll_a_color" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ;
            ns2:chlorophyll_a_plot [ dcterms:description "Plot representation of chlorophyll-a." ;
                    dcterms:title "chlorophyll_a_plot" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/png" ] ] ;
            ns2:cyanobacteria [ dcterms:description "" ;
                    dcterms:title "cyanobacteria" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ;
            ns2:cyanobacteria_color [ dcterms:description "Pseudo-color representation of cyanobacteria." ;
                    dcterms:title "cyanobacteria_color" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ;
            ns2:cyanobacteria_plot [ dcterms:description "Plot representation of cyanobacteria." ;
                    dcterms:title "cyanobacteria_plot" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/png" ] ] ;
            ns2:turbidity [ dcterms:description "" ;
                    dcterms:title "turbidity" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ;
            ns2:turbidity_color [ dcterms:description "Pseudo-color representation of turbidity." ;
                    dcterms:title "turbidity_color" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ;
            ns2:turbidity_plot [ dcterms:description "Plot representation of turbidity." ;
                    dcterms:title "turbidity_plot" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/png" ] ] ] .


```


### Raw cwl-to-ogcprocess output
Unmodified output of the `eoap.cct.cwl-to-ogcprocess` jq transform.
#### json
```json
{
  "id": "algae-usecase-workflow-copernicus-process",
  "version": "2.1.0",
  "title": "Processing on Sentinel-2 bands to evaluate algae bloom.\n",
  "description": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n",
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
      "value": "Processing on Sentinel-2 bands to evaluate algae bloom.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "2.1.0"
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
    },
    {
      "role": "https://schema.org/isBasedOn",
      "value": "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/se2waq/"
    }
  ],
  "inputs": {
    "product_url": {
      "title": "Sentinel-2 SAFE product S3 reference",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_access_key": {
      "title": "S3 access key required if found products are hosted on a protected S3 location.",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required if found products are hosted on a protected S3 location.",
      "description": "",
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
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "chlorophyll_a_color": {
      "title": "chlorophyll_a_color",
      "description": "Pseudo-color representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "chlorophyll_a_plot": {
      "title": "chlorophyll_a_plot",
      "description": "Plot representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "cyanobacteria": {
      "title": "cyanobacteria",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "cyanobacteria_color": {
      "title": "cyanobacteria_color",
      "description": "Pseudo-color representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "cyanobacteria_plot": {
      "title": "cyanobacteria_plot",
      "description": "Plot representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "turbidity": {
      "title": "turbidity",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "turbidity_color": {
      "title": "turbidity_color",
      "description": "Pseudo-color representation of turbidity.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "turbidity_plot": {
      "title": "turbidity_plot",
      "description": "Plot representation of turbidity.",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "id": "algae-usecase-workflow-copernicus-process",
  "version": "2.1.0",
  "title": "Processing on Sentinel-2 bands to evaluate algae bloom.\n",
  "description": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n",
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
      "value": "Processing on Sentinel-2 bands to evaluate algae bloom.\n"
    },
    {
      "role": "https://schema.org/description",
      "value": "Performs band calculation on Sentinel-2 product bands\nto evaluate algae bloom for water quality assessment.\n"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "2.1.0"
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
    },
    {
      "role": "https://schema.org/isBasedOn",
      "value": "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/se2waq/"
    }
  ],
  "inputs": {
    "product_url": {
      "title": "Sentinel-2 SAFE product S3 reference",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_access_key": {
      "title": "S3 access key required if found products are hosted on a protected S3 location.",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "s3_secret_key": {
      "title": "S3 secret key required if found products are hosted on a protected S3 location.",
      "description": "",
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
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "chlorophyll_a_color": {
      "title": "chlorophyll_a_color",
      "description": "Pseudo-color representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "chlorophyll_a_plot": {
      "title": "chlorophyll_a_plot",
      "description": "Plot representation of chlorophyll-a.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "cyanobacteria": {
      "title": "cyanobacteria",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "cyanobacteria_color": {
      "title": "cyanobacteria_color",
      "description": "Pseudo-color representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "cyanobacteria_plot": {
      "title": "cyanobacteria_plot",
      "description": "Plot representation of cyanobacteria.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "turbidity": {
      "title": "turbidity",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "turbidity_color": {
      "title": "turbidity_color",
      "description": "Pseudo-color representation of turbidity.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "turbidity_plot": {
      "title": "turbidity_plot",
      "description": "Plot representation of turbidity.",
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
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns2: <https://w3id.org/ogc/api/schema/> .
@prefix ns3: <http://schema.org/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus-process> dcterms:description """Performs band calculation on Sentinel-2 product bands
to evaluate algae bloom for water quality assessment.
""" ;
    dcterms:subject "Copernicus",
        "OSPD",
        "algae-bloom",
        "demo",
        "water-quality" ;
    dcterms:title """Processing on Sentinel-2 bands to evaluate algae bloom.
""" ;
    pp:version "2.1.0" ;
    proc:inputs [ ns4:product_url [ dcterms:description "" ;
                    dcterms:title "Sentinel-2 SAFE product S3 reference" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns4:s3_access_key [ dcterms:description "" ;
                    dcterms:title "S3 access key required if found products are hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns4:s3_secret_key [ dcterms:description "" ;
                    dcterms:title "S3 secret key required if found products are hosted on a protected S3 location." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "https://gitlab.ogc.org/ogc/ogc-ospd" ;
            proc:role schema:codeRepository ],
        [ rdf:value """Performs band calculation on Sentinel-2 product bands
to evaluate algae bloom for water quality assessment.
""" ;
            proc:role schema:description ],
        [ rdf:value """Processing on Sentinel-2 bands to evaluate algae bloom.
""" ;
            proc:role schema:name ],
        [ rdf:value "2.1.0" ;
            proc:role schema:softwareVersion ],
        [ rdf:value [ a ns3:Person ;
                    ns3:email "francis.charette-migneault@crim.ca" ;
                    ns3:identifier "http://orcid.org/0000-0003-4862-3349" ;
                    ns3:name "Francis Charette-Migneault" ] ;
            proc:role schema:author ],
        [ rdf:value "https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/se2waq/" ;
            proc:role schema:isBasedOn ],
        [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns1:chlorophyll_a [ dcterms:description "" ;
                    dcterms:title "chlorophyll_a" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:chlorophyll_a_color [ dcterms:description "Pseudo-color representation of chlorophyll-a." ;
                    dcterms:title "chlorophyll_a_color" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:chlorophyll_a_plot [ dcterms:description "Plot representation of chlorophyll-a." ;
                    dcterms:title "chlorophyll_a_plot" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:cyanobacteria [ dcterms:description "" ;
                    dcterms:title "cyanobacteria" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:cyanobacteria_color [ dcterms:description "Pseudo-color representation of cyanobacteria." ;
                    dcterms:title "cyanobacteria_color" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:cyanobacteria_plot [ dcterms:description "Plot representation of cyanobacteria." ;
                    dcterms:title "cyanobacteria_plot" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:turbidity [ dcterms:description "" ;
                    dcterms:title "turbidity" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:turbidity_color [ dcterms:description "Pseudo-color representation of turbidity." ;
                    dcterms:title "turbidity_color" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:turbidity_plot [ dcterms:description "Plot representation of turbidity." ;
                    dcterms:title "turbidity_plot" ;
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
      "id": "algae-usecase-workflow-copernicus-process",
      "version": "2.1.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "processDescription": {
    "process": {
      "id": "algae-usecase-workflow-copernicus-process",
      "version": "2.1.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus-process> pp:version "2.1.0" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus-process> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl" ;
            pp:rel "http://www.opengis.net/def/rel/ogc/1.0/executionUnit" ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "product_url": "s3:///eodata/Sentinel-2/MSI/L2A/2019/07/01/S2A_MSIL2A_20190701T110621_N0212_R137_T29SPC_20190701T120906.SAFE",
    "s3_access_key": "<redacted>",
    "s3_secret_key": "<redacted>"
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "inputs": {
    "product_url": "s3:///eodata/Sentinel-2/MSI/L2A/2019/07/01/S2A_MSIL2A_20190701T110621_N0212_R137_T29SPC_20190701T120906.SAFE",
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

[] proc:inputs [ ns1:product_url "s3:///eodata/Sentinel-2/MSI/L2A/2019/07/01/S2A_MSIL2A_20190701T110621_N0212_R137_T29SPC_20190701T120906.SAFE" ;
            ns1:s3_access_key "<redacted>" ;
            ns1:s3_secret_key "<redacted>" ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "chlorophyll_a": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
    "type": "image/tiff; application=geotiff"
  },
  "chlorophyll_a_color": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "chlorophyll_a_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
    "type": "image/png"
  },
  "cyanobacteria": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
    "type": "image/tiff; application=geotiff"
  },
  "cyanobacteria_color": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "cyanobacteria_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
    "type": "image/png"
  },
  "turbidity": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
    "type": "image/tiff; application=geotiff"
  },
  "turbidity_color": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "turbidity_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
    "type": "image/png"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "chlorophyll_a": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
    "type": "image/tiff; application=geotiff"
  },
  "chlorophyll_a_color": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "chlorophyll_a_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
    "type": "image/png"
  },
  "cyanobacteria": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
    "type": "image/tiff; application=geotiff"
  },
  "cyanobacteria_color": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "cyanobacteria_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
    "type": "image/png"
  },
  "turbidity": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
    "type": "image/tiff; application=geotiff"
  },
  "turbidity_color": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "turbidity_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
    "type": "image/png"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:chlorophyll_a [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff" ] ;
    pp:chlorophyll_a_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif" ] ;
    pp:chlorophyll_a_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png" ] ;
    pp:cyanobacteria [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff" ] ;
    pp:cyanobacteria_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif" ] ;
    pp:cyanobacteria_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png" ] ;
    pp:turbidity [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff" ] ;
    pp:turbidity_color [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif" ] ;
    pp:turbidity_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process",
    "startedAtTime": "2026-09-23T07:31:01Z",
    "used": [
      "urn:example:entity:workflow-copernicus-process:in:product_url",
      "urn:example:entity:workflow-copernicus-process:in:s3_access_key",
      "urn:example:entity:workflow-copernicus-process:in:s3_secret_key"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process"
      }
    ],
    "endedAtTime": "2026-09-23T07:33:59Z"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:in:product_url",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/product_url",
    "value": "s3:///eodata/Sentinel-2/MSI/L2A/2019/07/01/S2A_MSIL2A_20190701T110621_N0212_R137_T29SPC_20190701T120906.SAFE"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:in:s3_access_key",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/s3_access_key"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:in:s3_secret_key",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/s3_secret_key"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:chlorophyll_a",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:chlorophyll_a_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:chlorophyll_a_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
        "rel": "item",
        "type": "image/png"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:cyanobacteria",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:cyanobacteria_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:cyanobacteria_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
        "rel": "item",
        "type": "image/png"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:turbidity",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:turbidity_color",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_color",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:workflow-copernicus-process:out:turbidity_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process",
      "startedAtTime": "2026-09-23T07:31:01Z",
      "used": [
        "urn:example:entity:workflow-copernicus-process:in:product_url",
        "urn:example:entity:workflow-copernicus-process:in:s3_access_key",
        "urn:example:entity:workflow-copernicus-process:in:s3_secret_key"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process"
        }
      ],
      "endedAtTime": "2026-09-23T07:33:59Z"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:in:product_url",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/product_url",
      "value": "s3:///eodata/Sentinel-2/MSI/L2A/2019/07/01/S2A_MSIL2A_20190701T110621_N0212_R137_T29SPC_20190701T120906.SAFE"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:in:s3_access_key",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/s3_access_key"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:in:s3_secret_key",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/s3_secret_key"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:chlorophyll_a",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:chlorophyll_a_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:chlorophyll_a_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
          "rel": "item",
          "type": "image/png"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:cyanobacteria",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:cyanobacteria_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:cyanobacteria_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
          "rel": "item",
          "type": "image/png"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:turbidity",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:turbidity_color",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_color",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:workflow-copernicus-process:out:turbidity_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
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

<urn:example:entity:workflow-copernicus-process:out:chlorophyll_a> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:chlorophyll_a_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:chlorophyll_a_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:cyanobacteria> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:cyanobacteria_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:cyanobacteria_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:turbidity> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:turbidity_color> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_color> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:out:turbidity_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:workflow-copernicus-process> .

<urn:example:entity:workflow-copernicus-process:in:product_url> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/product_url> ;
    rdf:value "s3:///eodata/Sentinel-2/MSI/L2A/2019/07/01/S2A_MSIL2A_20190701T110621_N0212_R137_T29SPC_20190701T120906.SAFE" .

<urn:example:entity:workflow-copernicus-process:in:s3_access_key> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/s3_access_key> .

<urn:example:entity:workflow-copernicus-process:in:s3_secret_key> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#inputs/s3_secret_key> .

<urn:example:run:algae-bloom:workflow-copernicus-process> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process> ;
    prov:endedAtTime "2026-09-23T07:33:59+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process> ] ;
    prov:startedAtTime "2026-09-23T07:31:01+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:workflow-copernicus-process:in:product_url>,
        <urn:example:entity:workflow-copernicus-process:in:s3_access_key>,
        <urn:example:entity:workflow-copernicus-process:in:s3_secret_key> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Execution bundle (generic provenance profile)
#### json
```json
{
  "run": {
    "id": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "algae-bloom-workflow-copernicus-process-0001",
    "startedAtTime": "2026-09-23T07:31:01Z",
    "endedAtTime": "2026-09-23T07:33:59Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:algae-bloom:download-band-sentinel2-product-safe"
      },
      {
        "id": "urn:example:run:algae-bloom:calculate-band"
      },
      {
        "id": "urn:example:run:algae-bloom:plot-image"
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
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "3b00d9df28c7548e79088d660b1d416953bdb464"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "e6006027bca29c0e9abb13482a5deea81527097b"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "9cf89d0572c2a7632f7e096b040d37f8a99b4307"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b90b2dee65d0b638143e2788b825e245dbe9c4bb"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1b832fde3fc0d94955508d006d745a0a9e9b9596"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1e0302087d93ff81d5ec6b3a7a63ad7d0daec758"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "823dc9c0e24073601b98c7ac80d545355715c6f5"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "run": {
    "id": "urn:example:run:algae-bloom:workflow-copernicus-process",
    "type": "WorkflowRun",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process",
    "describedByWorkflow": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process",
    "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
    "status": "successful",
    "jobID": "algae-bloom-workflow-copernicus-process-0001",
    "startedAtTime": "2026-09-23T07:31:01Z",
    "endedAtTime": "2026-09-23T07:33:59Z",
    "hadSubProcessRun": [
      {
        "id": "urn:example:run:algae-bloom:download-band-sentinel2-product-safe"
      },
      {
        "id": "urn:example:run:algae-bloom:calculate-band"
      },
      {
        "id": "urn:example:run:algae-bloom:plot-image"
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
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "3b00d9df28c7548e79088d660b1d416953bdb464"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "e6006027bca29c0e9abb13482a5deea81527097b"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "9cf89d0572c2a7632f7e096b040d37f8a99b4307"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b90b2dee65d0b638143e2788b825e245dbe9c4bb"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1b832fde3fc0d94955508d006d745a0a9e9b9596"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "1e0302087d93ff81d5ec6b3a7a63ad7d0daec758"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/tiff; application=geotiff",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_color",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
      "checksum": {
        "algorithm": "SHA-1",
        "value": "823dc9c0e24073601b98c7ac80d545355715c6f5"
      }
    },
    {
      "id": "https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png",
      "type": "Artifact",
      "role": "output",
      "mediaType": "image/png",
      "describedByParameter": "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_plot",
      "wasOutputFrom": "urn:example:run:algae-bloom:workflow-copernicus-process",
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

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "3b00d9df28c7548e79088d660b1d416953bdb464" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "e6006027bca29c0e9abb13482a5deea81527097b" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "9cf89d0572c2a7632f7e096b040d37f8a99b4307" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/chlorophyll_a_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "b90b2dee65d0b638143e2788b825e245dbe9c4bb" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "1b832fde3fc0d94955508d006d745a0a9e9b9596" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/cyanobacteria_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "1e0302087d93ff81d5ec6b3a7a63ad7d0daec758" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "823dc9c0e24073601b98c7ac80d545355715c6f5" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_color" ;
    ns1:mediaType "image/tiff; application=geotiff" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png> prov:generated <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    ns1:checksum [ rdf:value "92c53811eb6d7bad871be5ebee515b4f95e0336a" ;
            ns1:algorithm "SHA-1" ] ;
    ns1:describedByParameter "https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process#outputs/turbidity_plot" ;
    ns1:mediaType "image/png" ;
    proc:role <https://geolabs.github.io/bblocks-process-profiles/def/process/output> ;
    proc:type "Artifact" .

<urn:example:engine:cwltool-3.1.20260108082145> a wfprov:WorkflowEngine ;
    pp:name "cwltool" ;
    pp:version "3.1.20260108082145" .

<urn:example:run:algae-bloom:workflow-copernicus-process> a wfprov:WorkflowRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process> ;
    wfprov:describedByWorkflow <https://ospd.example.org/ogc-api/processes/algae-usecase-workflow-copernicus-process> ;
    wfprov:hadSubProcessRun <urn:example:run:algae-bloom:calculate-band>,
        <urn:example:run:algae-bloom:download-band-sentinel2-product-safe>,
        <urn:example:run:algae-bloom:plot-image> ;
    prov:endedAtTime "2026-09-23T07:33:59+00:00"^^xsd:dateTime ;
    prov:startedAtTime "2026-09-23T07:31:01+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:jobID "algae-bloom-workflow-copernicus-process-0001" ;
    pp:status "successful" .

[] pp:engine <urn:example:engine:cwltool-3.1.20260108082145> ;
    pp:run <urn:example:run:algae-bloom:workflow-copernicus-process> ;
    proc:outputs <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif>,
        <https://ospd.example.org/ogc-api/jobs/algae-bloom-workflow-copernicus-process-0001/results/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process",
  "type": "ProcessType",
  "prefLabel": "Processing on Sentinel-2 bands to evaluate algae bloom.",
  "definition": "Performs band calculation on Sentinel-2 product bands to evaluate algae bloom for water quality assessment.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.algae-bloom.workflow-copernicus-process",
  "processDescription": {
    "id": "algae-usecase-workflow-copernicus-process",
    "version": "2.1.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl",
    "cwlClass": "Workflow",
    "cwlId": "algae-usecase-workflow-copernicus-process",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#WorkflowRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.string-format"
  ],
  "hasStep": [
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/download-band-sentinel2-product-safe",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/calculate-band",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite (11 steps). No resampling step: the SAFE product already provides 60 m bands, so B03 60 m is downloaded directly instead of being resampled.",
    "decomposition": [
      {
        "stage": "download_b0x (x5)",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection",
          "ogc.openeo.processes.cubes.filter_bands"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "calculate_* (x3)",
        "openeo": [
          "ogc.openeo.processes.cubes.reduce_dimension"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "plot_* (x3)",
        "openeo": [
          "ogc.openeo.processes.cubes.save_result"
        ],
        "level": "closeMatch",
        "note": "partial"
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process",
  "type": "ProcessType",
  "prefLabel": "Processing on Sentinel-2 bands to evaluate algae bloom.",
  "definition": "Performs band calculation on Sentinel-2 product bands to evaluate algae bloom for water quality assessment.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation",
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.algae-bloom.workflow-copernicus-process",
  "processDescription": {
    "id": "algae-usecase-workflow-copernicus-process",
    "version": "2.1.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl",
    "cwlClass": "Workflow",
    "cwlId": "algae-usecase-workflow-copernicus-process",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#WorkflowRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.string-format"
  ],
  "hasStep": [
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/download-band-sentinel2-product-safe",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/calculate-band",
    "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Composite (11 steps). No resampling step: the SAFE product already provides 60 m bands, so B03 60 m is downloaded directly instead of being resampled.",
    "decomposition": [
      {
        "stage": "download_b0x (x5)",
        "openeo": [
          "ogc.openeo.processes.cubes.load_collection",
          "ogc.openeo.processes.cubes.filter_bands"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "calculate_* (x3)",
        "openeo": [
          "ogc.openeo.processes.cubes.reduce_dimension"
        ],
        "level": "closeMatch"
      },
      {
        "stage": "plot_* (x3)",
        "openeo": [
          "ogc.openeo.processes.cubes.save_result"
        ],
        "level": "closeMatch",
        "note": "partial"
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

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus-process> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/data-retrieval>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation>,
        <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    skos:definition "Performs band calculation on Sentinel-2 product bands to evaluate algae bloom for water quality assessment." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Processing on Sentinel-2 bands to evaluate algae bloom." ;
    pp:candidateCctDependency "eoap.cct.string-format" ;
    pp:hasStep <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/calculate-band>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/download-band-sentinel2-product-safe>,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image> ;
    pp:openeoEquivalence [ pp:decomposition ( [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.filter_bands",
                            "ogc.openeo.processes.cubes.load_collection" ;
                        pp:stage "download_b0x (x5)" ] [ pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.reduce_dimension" ;
                        pp:stage "calculate_* (x3)" ] [ skos:note "partial" ;
                        pp:equivalenceLevel "closeMatch" ;
                        pp:openeo "ogc.openeo.processes.cubes.save_result" ;
                        pp:stage "plot_* (x3)" ] ) ;
            pp:equivalenceLevel "none" ;
            pp:rationale "Composite (11 steps). No resampling step: the SAFE product already provides 60 m bands, so B03 60 m is downloaded directly instead of being resampled." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus-process> ;
    pp:profile "ospd.process-profiles.algae-bloom.workflow-copernicus-process" ;
    pp:provenanceClass wfprov:WorkflowRun ;
    pp:source [ pp:cwl <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/algae-usecase-workflow-copernicus-process.cwl> ;
            pp:cwlClass "Workflow" ;
            pp:cwlId "algae-usecase-workflow-copernicus-process" ;
            pp:license "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/algae-usecase-workflow-copernicus-process> pp:version "2.1.0" .


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
      "@id": "id:136d036c-1194-4d69-b3c7-538ad435fe46",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:271d494f-4cd0-47bc-86d6-bcd7da4a7ff9",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:a8ac9566-6183-46d2-8801-4814c774cbd1",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:1a71a853-4269-4af2-9e7e-0b8b9dd37a24",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:27cdb921-72e1-47e6-96a9-08b6f25e590a",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:e9c353d3-6b40-4b92-becb-8bb1decc76b7",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/calculate-band:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:e268cc0e-1073-422f-af40-acfe6b7db163",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/calculate-band:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:d9e8b09a-c16c-484e-9bc9-27c25011460a",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/calculate-band:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:97e3cfc5-acf5-4568-8df6-99615db81d5f",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/plot-image:1.0.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:6a564363-742d-4015-b71b-70001b3a39ff",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/plot-image:1.0.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:697c2f54-7c7d-4e14-8900-d1e42db3a142",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/plot-image:1.0.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0"
        }
      ]
    },
    {
      "@type": "Start",
      "activity": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "starter": "id:5001cc2f-8b7b-4b93-9043-8ce09886304f",
      "time": "2026-09-23T09:31:01.456509"
    },
    {
      "@type": "Start",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "starter": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "time": "2026-09-23T09:31:01.456549"
    },
    {
      "@type": "Start",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:06.038809"
    },
    {
      "@type": "Start",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:13.105700"
    },
    {
      "@type": "Start",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:20.403484"
    },
    {
      "@type": "Start",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:23.033156"
    },
    {
      "@type": "Start",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:29.717898"
    },
    {
      "@type": "Start",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:32.238304"
    },
    {
      "@type": "Start",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:34.582528"
    },
    {
      "@type": "Start",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:48.321511"
    },
    {
      "@type": "Start",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:50.769647"
    },
    {
      "@type": "Start",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:51.980880"
    },
    {
      "@type": "Start",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "starter": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:56.238639"
    },
    {
      "@type": "Activity",
      "@id": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "startTime": "2026-09-23T09:31:01.456528",
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
      "@id": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b03_10m"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b04_10m"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b01_60m"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b02_10m"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b03_60m"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/calculate_turbidity"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/calculate_cyanobacteria"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/calculate_chlorophyll_a"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/plot_cyanobacteria"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/plot_turbidity"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/plot_chlorophyll_a"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/download_b03_10m"
    },
    {
      "@type": "Association",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "agent": "id:136d036c-1194-4d69-b3c7-538ad435fe46"
    },
    {
      "@type": "Association",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/download_b04_10m"
    },
    {
      "@type": "Association",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "agent": "id:271d494f-4cd0-47bc-86d6-bcd7da4a7ff9"
    },
    {
      "@type": "Association",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/download_b01_60m"
    },
    {
      "@type": "Association",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "agent": "id:a8ac9566-6183-46d2-8801-4814c774cbd1"
    },
    {
      "@type": "Association",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/download_b02_10m"
    },
    {
      "@type": "Association",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "agent": "id:1a71a853-4269-4af2-9e7e-0b8b9dd37a24"
    },
    {
      "@type": "Association",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/download_b03_60m"
    },
    {
      "@type": "Association",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "agent": "id:27cdb921-72e1-47e6-96a9-08b6f25e590a"
    },
    {
      "@type": "Association",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/calculate_turbidity"
    },
    {
      "@type": "Association",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "agent": "id:e9c353d3-6b40-4b92-becb-8bb1decc76b7"
    },
    {
      "@type": "Association",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/calculate_cyanobacteria"
    },
    {
      "@type": "Association",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "agent": "id:e268cc0e-1073-422f-af40-acfe6b7db163"
    },
    {
      "@type": "Association",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/calculate_chlorophyll_a"
    },
    {
      "@type": "Association",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "agent": "id:d9e8b09a-c16c-484e-9bc9-27c25011460a"
    },
    {
      "@type": "Association",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/plot_cyanobacteria"
    },
    {
      "@type": "Association",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "agent": "id:97e3cfc5-acf5-4568-8df6-99615db81d5f"
    },
    {
      "@type": "Association",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/plot_turbidity"
    },
    {
      "@type": "Association",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "agent": "id:6a564363-742d-4015-b71b-70001b3a39ff"
    },
    {
      "@type": "Association",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "agent": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "plan": "wf:main/plot_chlorophyll_a"
    },
    {
      "@type": "Association",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "agent": "id:697c2f54-7c7d-4e14-8900-d1e42db3a142"
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
          "@value": "wf:main/calculate_cyanobacteria",
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
          "@value": "wf:main/calculate_chlorophyll_a",
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
          "@value": "wf:main/download_b03_10m",
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
          "@value": "wf:main/download_b04_10m",
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
          "@value": "wf:main/plot_cyanobacteria",
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
          "@value": "wf:main/download_b01_60m",
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
          "@value": "wf:main/plot_turbidity",
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
          "@value": "wf:main/plot_chlorophyll_a",
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
          "@value": "wf:main/download_b02_10m",
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
          "@value": "wf:main/download_b03_60m",
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
          "@value": "wf:main/calculate_turbidity",
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
      "@id": "wf:main/calculate_cyanobacteria",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/calculate_chlorophyll_a",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b03_10m",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b04_10m",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_cyanobacteria",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b01_60m",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_turbidity",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_chlorophyll_a",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b02_10m",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b03_60m",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/calculate_turbidity",
      "type": [
        "wfdesc:Process",
        "prov:Plan"
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
      "@id": "data:7c5d11a451cde788be37383d50239d7672a8cb1f",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "B03"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:7c5d11a451cde788be37383d50239d7672a8cb1f",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "B03"
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
      "@id": "data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "10m"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "10m"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "10m"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e882c92a-6411-4b82-aae7-70be694c29d7",
      "value": [
        {
          "@value": "false",
          "@type": "xsd:boolean"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:bfcfb6a10e7a05a5a7c2508fd2c2918e7483c6f5",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:b379cd45-e93d-43eb-902f-df573b67ccf0",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "T29SPC_20190701T110621_B03_10m.jp2"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "T29SPC_20190701T110621_B03_10m"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".jp2"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "B04"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a16a5d61-1192-43b9-8be3-6f546af4ccdd",
      "value": [
        {
          "@value": "false",
          "@type": "xsd:boolean"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:f670343b66112543f0c884bdf23886e2d7126070",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:f1093031-b0f1-4f09-bf38-f001b51a13e5",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "T29SPC_20190701T110621_B04_10m.jp2"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "T29SPC_20190701T110621_B04_10m"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".jp2"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "B01"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ccd4d27929279b55bfa676ddddbe7b67aa8d9ce5",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "60m"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ccd4d27929279b55bfa676ddddbe7b67aa8d9ce5",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "60m"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:fbda755c-26d7-4213-8ac3-437112f3f27a",
      "value": [
        {
          "@value": "false",
          "@type": "xsd:boolean"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5d6d0f08e1b29a2d9531b02d6ad6c382ead6b33f",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6e735750-bb9c-4417-b20e-f7ddb07df649",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "T29SPC_20190701T110621_B01_60m.jp2"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "T29SPC_20190701T110621_B01_60m"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".jp2"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:36dea452bfe795afb42cf14b59c82a3127598281",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "B02"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:b509d8cc-cc7b-4fdf-88aa-f13c8d9b47c5",
      "value": [
        {
          "@value": "false",
          "@type": "xsd:boolean"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:86c333c825c3e7e7e612f61b8a330693f3f8bfc2",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:55c5cc1e-5f73-4878-8a63-f5d1ab235cb6",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "T29SPC_20190701T110621_B02_10m.jp2"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "T29SPC_20190701T110621_B02_10m"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".jp2"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ee76b2e7-fa78-416c-982a-0034be8e3618",
      "value": [
        {
          "@value": "false",
          "@type": "xsd:boolean"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:6be82354dccae2e18c5d885d24c5ea13a3420e1b",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:fcc8bc22-4c42-45a2-a828-ef8de070904e",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "T29SPC_20190701T110621_B03_60m.jp2"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "T29SPC_20190701T110621_B03_60m"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".jp2"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:81e487db73b1725c362decd3aac3a2c13f86d595",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "(8.93*(C/A))-6.39"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:cf72a11e7365073ae3c966029d357f3e9b82af8a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "cwlprov:None",
      "label": [
        {
          "@value": "None"
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
      "@id": "data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:a87dac8429196320690ec2c17ae2c00532d9e957",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "115530.31*(((B.astype(float)*C.astype(float))/A.astype(float))**2.38)"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:915294efd60b642abdf0ab2947e15fbb5d702a7e",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b90b2dee65d0b638143e2788b825e245dbe9c4bb",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:c6f40f302effca33768fc256bbb5dedaca044174",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "4.26*((C/A)**3.94)"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:a67be08b0183aa19f78701cd7fb864462a08af4c",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:3b00d9df28c7548e79088d660b1d416953bdb464",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "id:73af567d-64fb-4113-9d5d-24a98b4a23d5",
      "value": [
        {
          "@value": "100000000000000",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:8fc8d4c9-0d3d-43d8-8e04-1fb53d64f191",
      "value": [
        {
          "@value": "1000000",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:1370052da0755d73768c0c75500107d3759bcc2d",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "[\n  [1E6,  [ 18,  28,  60] ],\n  [1E7,  [ 73, 111, 242] ],\n  [1E8,  [130, 211,  95] ],\n  [1E9,  [254, 253,   5] ],\n  [1E10, [253,   0,   4] ],\n  [1E11, [142,  32,  38] ],\n  [1E12, [111, 63,  125] ],\n  [1E13, [ 58,   6,   3] ],\n  [1E14, [ 18,  28,  60] ]\n]\n"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:8655751d19f645dec4f65b6bb306877a7180a3b2",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:a15e03a530b917f396df0bd7bf919d2f342d7ecf",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:4ad2eab867b3280cabc93a14c615ab97b6b6575e",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "Cyanobacteria"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:1b832fde3fc0d94955508d006d745a0a9e9b9596",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:2b0824b4ba24b098adc7ce01881499891c48d2ea",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "[\n  [0,  [ 73, 111, 242] ],\n  [4,  [130, 211,  95] ],\n  [8,  [254, 253,   5] ],\n  [12, [253,   0,   4] ],\n  [16, [142,  32,  38] ],\n  [20, [217, 124, 245] ]\n]\n"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:34bd4f200813f30333e40ecb55d1a316cf2da8af",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:1edf82bd141d9e642e6ec01d71e53d8107df885c",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "Turbidity"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:823dc9c0e24073601b98c7ac80d545355715c6f5",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:92c53811eb6d7bad871be5ebee515b4f95e0336a",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "[\n  [0,  [ 73, 111, 242] ],\n  [6,  [130, 211,  95] ],\n  [12, [254, 253,   5] ],\n  [20, [253,   0,   4] ],\n  [30, [142,  32,  38] ],\n  [50, [217, 124, 245] ]\n]\n"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:6f7a2e56416e7ae7128bf930d39e5c26ca53c5d7",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:f1a11aea9cfbd38e6dbda7e14c05bf9addcd2248",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e059662a461e5d1b245f555149febc699f42b537",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "Chlorophyll a"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e6006027bca29c0e9abb13482a5deea81527097b",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:9cf89d0572c2a7632f7e096b040d37f8a99b4307",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@type": "Usage",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "entity": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "time": "2026-09-23T09:31:06.037596",
      "role": [
        "wf:main/s3_access_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "entity": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "time": "2026-09-23T09:31:06.037821",
      "role": [
        "wf:main/s3_secret_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "entity": "data:7c5d11a451cde788be37383d50239d7672a8cb1f",
      "time": "2026-09-23T09:31:06.087662",
      "role": [
        "wf:main/download_b03_10m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "entity": "data:5e7cb55727e375cb72dac733c05c4c81c30ffaae",
      "time": "2026-09-23T09:31:06.087923",
      "role": [
        "wf:main/download_b03_10m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "entity": "data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b",
      "time": "2026-09-23T09:31:06.088207",
      "role": [
        "wf:main/download_b03_10m/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "entity": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "time": "2026-09-23T09:31:06.088513",
      "role": [
        "wf:main/download_b03_10m/s3_access_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "entity": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "time": "2026-09-23T09:31:06.088743",
      "role": [
        "wf:main/download_b03_10m/s3_secret_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "entity": "id:e882c92a-6411-4b82-aae7-70be694c29d7",
      "time": "2026-09-23T09:31:06.088793",
      "role": [
        "wf:main/download_b03_10m/debug"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "entity": "data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0",
      "time": "2026-09-23T09:31:13.111444",
      "role": [
        "wf:main/download_b04_10m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "entity": "data:5e7cb55727e375cb72dac733c05c4c81c30ffaae",
      "time": "2026-09-23T09:31:13.111723",
      "role": [
        "wf:main/download_b04_10m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "entity": "data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b",
      "time": "2026-09-23T09:31:13.111934",
      "role": [
        "wf:main/download_b04_10m/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "entity": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "time": "2026-09-23T09:31:13.112207",
      "role": [
        "wf:main/download_b04_10m/s3_access_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "entity": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "time": "2026-09-23T09:31:13.112514",
      "role": [
        "wf:main/download_b04_10m/s3_secret_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "entity": "id:a16a5d61-1192-43b9-8be3-6f546af4ccdd",
      "time": "2026-09-23T09:31:13.112573",
      "role": [
        "wf:main/download_b04_10m/debug"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "entity": "data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f",
      "time": "2026-09-23T09:31:20.409442",
      "role": [
        "wf:main/download_b01_60m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "entity": "data:5e7cb55727e375cb72dac733c05c4c81c30ffaae",
      "time": "2026-09-23T09:31:20.409713",
      "role": [
        "wf:main/download_b01_60m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "entity": "data:ccd4d27929279b55bfa676ddddbe7b67aa8d9ce5",
      "time": "2026-09-23T09:31:20.409969",
      "role": [
        "wf:main/download_b01_60m/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "entity": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "time": "2026-09-23T09:31:20.410192",
      "role": [
        "wf:main/download_b01_60m/s3_access_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "entity": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "time": "2026-09-23T09:31:20.410382",
      "role": [
        "wf:main/download_b01_60m/s3_secret_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "entity": "id:fbda755c-26d7-4213-8ac3-437112f3f27a",
      "time": "2026-09-23T09:31:20.410426",
      "role": [
        "wf:main/download_b01_60m/debug"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "entity": "data:36dea452bfe795afb42cf14b59c82a3127598281",
      "time": "2026-09-23T09:31:23.049716",
      "role": [
        "wf:main/download_b02_10m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "entity": "data:5e7cb55727e375cb72dac733c05c4c81c30ffaae",
      "time": "2026-09-23T09:31:23.050787",
      "role": [
        "wf:main/download_b02_10m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "entity": "data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b",
      "time": "2026-09-23T09:31:23.052004",
      "role": [
        "wf:main/download_b02_10m/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "entity": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "time": "2026-09-23T09:31:23.052690",
      "role": [
        "wf:main/download_b02_10m/s3_access_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "entity": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "time": "2026-09-23T09:31:23.053637",
      "role": [
        "wf:main/download_b02_10m/s3_secret_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "entity": "id:b509d8cc-cc7b-4fdf-88aa-f13c8d9b47c5",
      "time": "2026-09-23T09:31:23.053767",
      "role": [
        "wf:main/download_b02_10m/debug"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "entity": "data:7c5d11a451cde788be37383d50239d7672a8cb1f",
      "time": "2026-09-23T09:31:29.723838",
      "role": [
        "wf:main/download_b03_60m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "entity": "data:5e7cb55727e375cb72dac733c05c4c81c30ffaae",
      "time": "2026-09-23T09:31:29.724260",
      "role": [
        "wf:main/download_b03_60m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "entity": "data:ccd4d27929279b55bfa676ddddbe7b67aa8d9ce5",
      "time": "2026-09-23T09:31:29.724514",
      "role": [
        "wf:main/download_b03_60m/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "entity": "data:b75fa50f91a9dd377927a83994bff64245718790",
      "time": "2026-09-23T09:31:29.724732",
      "role": [
        "wf:main/download_b03_60m/s3_access_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "entity": "data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570",
      "time": "2026-09-23T09:31:29.724936",
      "role": [
        "wf:main/download_b03_60m/s3_secret_key"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "entity": "id:ee76b2e7-fa78-416c-982a-0034be8e3618",
      "time": "2026-09-23T09:31:29.724989",
      "role": [
        "wf:main/download_b03_60m/debug"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "id:6e735750-bb9c-4417-b20e-f7ddb07df649",
      "time": "2026-09-23T09:31:32.278687",
      "role": [
        "wf:main/calculate_turbidity/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "id:fcc8bc22-4c42-45a2-a828-ef8de070904e",
      "time": "2026-09-23T09:31:32.278743",
      "role": [
        "wf:main/calculate_turbidity/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "data:81e487db73b1725c362decd3aac3a2c13f86d595",
      "time": "2026-09-23T09:31:32.279388",
      "role": [
        "wf:main/calculate_turbidity/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "data:cf72a11e7365073ae3c966029d357f3e9b82af8a",
      "time": "2026-09-23T09:31:32.279679",
      "role": [
        "wf:main/calculate_turbidity/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279699",
      "role": [
        "wf:main/calculate_turbidity/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279711",
      "role": [
        "wf:main/calculate_turbidity/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279722",
      "role": [
        "wf:main/calculate_turbidity/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279733",
      "role": [
        "wf:main/calculate_turbidity/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279742",
      "role": [
        "wf:main/calculate_turbidity/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279751",
      "role": [
        "wf:main/calculate_turbidity/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279760",
      "role": [
        "wf:main/calculate_turbidity/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279769",
      "role": [
        "wf:main/calculate_turbidity/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279781",
      "role": [
        "wf:main/calculate_turbidity/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279795",
      "role": [
        "wf:main/calculate_turbidity/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279806",
      "role": [
        "wf:main/calculate_turbidity/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279816",
      "role": [
        "wf:main/calculate_turbidity/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279826",
      "role": [
        "wf:main/calculate_turbidity/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279835",
      "role": [
        "wf:main/calculate_turbidity/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279843",
      "role": [
        "wf:main/calculate_turbidity/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279852",
      "role": [
        "wf:main/calculate_turbidity/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279861",
      "role": [
        "wf:main/calculate_turbidity/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279872",
      "role": [
        "wf:main/calculate_turbidity/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279882",
      "role": [
        "wf:main/calculate_turbidity/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279891",
      "role": [
        "wf:main/calculate_turbidity/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279899",
      "role": [
        "wf:main/calculate_turbidity/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279908",
      "role": [
        "wf:main/calculate_turbidity/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279921",
      "role": [
        "wf:main/calculate_turbidity/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:32.279934",
      "role": [
        "wf:main/calculate_turbidity/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "id:55c5cc1e-5f73-4878-8a63-f5d1ab235cb6",
      "time": "2026-09-23T09:31:34.594359",
      "role": [
        "wf:main/calculate_cyanobacteria/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "id:b379cd45-e93d-43eb-902f-df573b67ccf0",
      "time": "2026-09-23T09:31:34.594405",
      "role": [
        "wf:main/calculate_cyanobacteria/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "id:f1093031-b0f1-4f09-bf38-f001b51a13e5",
      "time": "2026-09-23T09:31:34.594422",
      "role": [
        "wf:main/calculate_cyanobacteria/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "data:a87dac8429196320690ec2c17ae2c00532d9e957",
      "time": "2026-09-23T09:31:34.596025",
      "role": [
        "wf:main/calculate_cyanobacteria/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "data:915294efd60b642abdf0ab2947e15fbb5d702a7e",
      "time": "2026-09-23T09:31:34.596397",
      "role": [
        "wf:main/calculate_cyanobacteria/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596418",
      "role": [
        "wf:main/calculate_cyanobacteria/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596433",
      "role": [
        "wf:main/calculate_cyanobacteria/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596452",
      "role": [
        "wf:main/calculate_cyanobacteria/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596463",
      "role": [
        "wf:main/calculate_cyanobacteria/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596473",
      "role": [
        "wf:main/calculate_cyanobacteria/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596483",
      "role": [
        "wf:main/calculate_cyanobacteria/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596492",
      "role": [
        "wf:main/calculate_cyanobacteria/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596518",
      "role": [
        "wf:main/calculate_cyanobacteria/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596530",
      "role": [
        "wf:main/calculate_cyanobacteria/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596540",
      "role": [
        "wf:main/calculate_cyanobacteria/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596549",
      "role": [
        "wf:main/calculate_cyanobacteria/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596558",
      "role": [
        "wf:main/calculate_cyanobacteria/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596567",
      "role": [
        "wf:main/calculate_cyanobacteria/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596576",
      "role": [
        "wf:main/calculate_cyanobacteria/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596585",
      "role": [
        "wf:main/calculate_cyanobacteria/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596594",
      "role": [
        "wf:main/calculate_cyanobacteria/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596606",
      "role": [
        "wf:main/calculate_cyanobacteria/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596617",
      "role": [
        "wf:main/calculate_cyanobacteria/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596626",
      "role": [
        "wf:main/calculate_cyanobacteria/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596635",
      "role": [
        "wf:main/calculate_cyanobacteria/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596648",
      "role": [
        "wf:main/calculate_cyanobacteria/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596658",
      "role": [
        "wf:main/calculate_cyanobacteria/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:34.596667",
      "role": [
        "wf:main/calculate_cyanobacteria/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "id:6e735750-bb9c-4417-b20e-f7ddb07df649",
      "time": "2026-09-23T09:31:48.327798",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "id:fcc8bc22-4c42-45a2-a828-ef8de070904e",
      "time": "2026-09-23T09:31:48.327842",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "data:c6f40f302effca33768fc256bbb5dedaca044174",
      "time": "2026-09-23T09:31:48.328390",
      "role": [
        "wf:main/calculate_chlorophyll_a/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "data:a67be08b0183aa19f78701cd7fb864462a08af4c",
      "time": "2026-09-23T09:31:48.328672",
      "role": [
        "wf:main/calculate_chlorophyll_a/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328691",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328703",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328713",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328723",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328735",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328747",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328761",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328772",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328781",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328790",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328799",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328808",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328819",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328828",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328843",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328852",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328861",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328871",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328880",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328889",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328898",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328907",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328916",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:31:48.328925",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "entity": "id:73af567d-64fb-4113-9d5d-24a98b4a23d5",
      "time": "2026-09-23T09:31:50.803703",
      "role": [
        "wf:main/plot_cyanobacteria/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "entity": "id:8fc8d4c9-0d3d-43d8-8e04-1fb53d64f191",
      "time": "2026-09-23T09:31:50.803738",
      "role": [
        "wf:main/plot_cyanobacteria/clip_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "entity": "data:1370052da0755d73768c0c75500107d3759bcc2d",
      "time": "2026-09-23T09:31:50.804251",
      "role": [
        "wf:main/plot_cyanobacteria/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "entity": "id:1855b873-514a-46e8-85f9-7e6fdd5c1c12",
      "time": "2026-09-23T09:31:50.804275",
      "role": [
        "wf:main/plot_cyanobacteria/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "entity": "data:8655751d19f645dec4f65b6bb306877a7180a3b2",
      "time": "2026-09-23T09:31:50.804535",
      "role": [
        "wf:main/plot_cyanobacteria/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "entity": "data:a15e03a530b917f396df0bd7bf919d2f342d7ecf",
      "time": "2026-09-23T09:31:50.804800",
      "role": [
        "wf:main/plot_cyanobacteria/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "entity": "data:4ad2eab867b3280cabc93a14c615ab97b6b6575e",
      "time": "2026-09-23T09:31:50.805055",
      "role": [
        "wf:main/plot_cyanobacteria/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "entity": "data:2b0824b4ba24b098adc7ce01881499891c48d2ea",
      "time": "2026-09-23T09:33:51.987879",
      "role": [
        "wf:main/plot_turbidity/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "entity": "id:0a64bae7-5f25-441b-b114-51f6437fb00f",
      "time": "2026-09-23T09:33:51.987923",
      "role": [
        "wf:main/plot_turbidity/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "entity": "data:34bd4f200813f30333e40ecb55d1a316cf2da8af",
      "time": "2026-09-23T09:33:51.988466",
      "role": [
        "wf:main/plot_turbidity/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "entity": "data:1edf82bd141d9e642e6ec01d71e53d8107df885c",
      "time": "2026-09-23T09:33:51.988984",
      "role": [
        "wf:main/plot_turbidity/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "entity": "data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c",
      "time": "2026-09-23T09:33:51.989395",
      "role": [
        "wf:main/plot_turbidity/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:33:51.989423",
      "role": [
        "wf:main/plot_turbidity/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:33:51.989440",
      "role": [
        "wf:main/plot_turbidity/clip_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "entity": "data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8",
      "time": "2026-09-23T09:33:56.247945",
      "role": [
        "wf:main/plot_chlorophyll_a/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "entity": "id:7fb56c04-4cb6-45f5-923c-390c6520ae3a",
      "time": "2026-09-23T09:33:56.248008",
      "role": [
        "wf:main/plot_chlorophyll_a/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "entity": "data:6f7a2e56416e7ae7128bf930d39e5c26ca53c5d7",
      "time": "2026-09-23T09:33:56.248701",
      "role": [
        "wf:main/plot_chlorophyll_a/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "entity": "data:f1a11aea9cfbd38e6dbda7e14c05bf9addcd2248",
      "time": "2026-09-23T09:33:56.249375",
      "role": [
        "wf:main/plot_chlorophyll_a/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "entity": "data:e059662a461e5d1b245f555149febc699f42b537",
      "time": "2026-09-23T09:33:56.249844",
      "role": [
        "wf:main/plot_chlorophyll_a/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:33:56.249875",
      "role": [
        "wf:main/plot_chlorophyll_a/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "entity": "cwlprov:None",
      "time": "2026-09-23T09:33:56.249891",
      "role": [
        "wf:main/plot_chlorophyll_a/clip_min"
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:b379cd45-e93d-43eb-902f-df573b67ccf0",
      "generalEntity": "data:bfcfb6a10e7a05a5a7c2508fd2c2918e7483c6f5"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:f1093031-b0f1-4f09-bf38-f001b51a13e5",
      "generalEntity": "data:f670343b66112543f0c884bdf23886e2d7126070"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:6e735750-bb9c-4417-b20e-f7ddb07df649",
      "generalEntity": "data:5d6d0f08e1b29a2d9531b02d6ad6c382ead6b33f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:55c5cc1e-5f73-4878-8a63-f5d1ab235cb6",
      "generalEntity": "data:86c333c825c3e7e7e612f61b8a330693f3f8bfc2"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:fcc8bc22-4c42-45a2-a828-ef8de070904e",
      "generalEntity": "data:6be82354dccae2e18c5d885d24c5ea13a3420e1b"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:0a64bae7-5f25-441b-b114-51f6437fb00f",
      "generalEntity": "data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1855b873-514a-46e8-85f9-7e6fdd5c1c12",
      "generalEntity": "data:b90b2dee65d0b638143e2788b825e245dbe9c4bb"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:7fb56c04-4cb6-45f5-923c-390c6520ae3a",
      "generalEntity": "data:3b00d9df28c7548e79088d660b1d416953bdb464"
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
      "specificEntity": "id:a9c95e1a-ef39-4627-8292-d1020e85dfa1",
      "generalEntity": "data:823dc9c0e24073601b98c7ac80d545355715c6f5"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3b413d9a-adab-454b-8670-0cf37423eec6",
      "generalEntity": "data:92c53811eb6d7bad871be5ebee515b4f95e0336a"
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
      "@type": "Generation",
      "entity": "id:b379cd45-e93d-43eb-902f-df573b67ccf0",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "time": "2026-09-23T09:31:13.060679",
      "role": [
        "wf:main/download_b03_10m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:f1093031-b0f1-4f09-bf38-f001b51a13e5",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "time": "2026-09-23T09:31:20.357696",
      "role": [
        "wf:main/download_b04_10m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6e735750-bb9c-4417-b20e-f7ddb07df649",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "time": "2026-09-23T09:31:23.013686",
      "role": [
        "wf:main/download_b01_60m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:55c5cc1e-5f73-4878-8a63-f5d1ab235cb6",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "time": "2026-09-23T09:31:29.673344",
      "role": [
        "wf:main/download_b02_10m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:fcc8bc22-4c42-45a2-a828-ef8de070904e",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "time": "2026-09-23T09:31:32.223947",
      "role": [
        "wf:main/download_b03_60m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:0a64bae7-5f25-441b-b114-51f6437fb00f",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "time": "2026-09-23T09:31:34.569525",
      "role": [
        "wf:main/calculate_turbidity/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:1855b873-514a-46e8-85f9-7e6fdd5c1c12",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "time": "2026-09-23T09:31:48.067700",
      "role": [
        "wf:main/calculate_cyanobacteria/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:7fb56c04-4cb6-45f5-923c-390c6520ae3a",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "time": "2026-09-23T09:31:50.757395",
      "role": [
        "wf:main/calculate_chlorophyll_a/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:29f23348-9547-4fef-b002-ceefd5b2471b",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "time": "2026-09-23T09:33:51.697961",
      "role": [
        "wf:main/plot_cyanobacteria/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:7e671680-4e90-4584-89b1-36260f670af1",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "time": "2026-09-23T09:33:51.697961",
      "role": [
        "wf:main/plot_cyanobacteria/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a9c95e1a-ef39-4627-8292-d1020e85dfa1",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "time": "2026-09-23T09:33:56.221505",
      "role": [
        "wf:main/plot_turbidity/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:3b413d9a-adab-454b-8670-0cf37423eec6",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "time": "2026-09-23T09:33:56.221505",
      "role": [
        "wf:main/plot_turbidity/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:8fe98067-8e97-40b6-a99a-cf787f26fa36",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "time": "2026-09-23T09:33:59.271268",
      "role": [
        "wf:main/plot_chlorophyll_a/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:ed443e92-82d0-40c9-b63e-724fba739364",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "time": "2026-09-23T09:33:59.271268",
      "role": [
        "wf:main/plot_chlorophyll_a/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:7fb56c04-4cb6-45f5-923c-390c6520ae3a",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%20process/chlorophyll_a"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:8fe98067-8e97-40b6-a99a-cf787f26fa36",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%2520process/chlorophyll_a_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:ed443e92-82d0-40c9-b63e-724fba739364",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%252520process/chlorophyll_a_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:1855b873-514a-46e8-85f9-7e6fdd5c1c12",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%25252520process/cyanobacteria"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:29f23348-9547-4fef-b002-ceefd5b2471b",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%2525252520process/cyanobacteria_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:7e671680-4e90-4584-89b1-36260f670af1",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%252525252520process/cyanobacteria_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:0a64bae7-5f25-441b-b114-51f6437fb00f",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%25252525252520process/turbidity"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a9c95e1a-ef39-4627-8292-d1020e85dfa1",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%2525252525252520process/turbidity_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:3b413d9a-adab-454b-8670-0cf37423eec6",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.283154",
      "role": [
        "wf:main/workflow%252525252525252520process/turbidity_plot"
      ]
    },
    {
      "@type": "End",
      "activity": "id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:13.060666"
    },
    {
      "@type": "End",
      "activity": "id:1f7c9599-10e3-4a9f-a64b-c333d730ff68",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:20.357689"
    },
    {
      "@type": "End",
      "activity": "id:489bffb3-47ea-4505-8a69-fb23eacf14a1",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:23.013674"
    },
    {
      "@type": "End",
      "activity": "id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:29.673327"
    },
    {
      "@type": "End",
      "activity": "id:74e5b6d2-7e78-4e78-9028-bec1988305d6",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:32.223936"
    },
    {
      "@type": "End",
      "activity": "id:63513262-cbe0-42d8-a5b8-843eba63ae68",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:34.569516"
    },
    {
      "@type": "End",
      "activity": "id:f0b22113-c4b4-451a-894f-30fc14eafc60",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:48.067683"
    },
    {
      "@type": "End",
      "activity": "id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:31:50.757388"
    },
    {
      "@type": "End",
      "activity": "id:f5c0b341-97fb-484c-9f8c-0646f0c63e86",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:51.697918"
    },
    {
      "@type": "End",
      "activity": "id:5805a5d2-d626-4eee-a0c2-b4167521a820",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:56.221490"
    },
    {
      "@type": "End",
      "activity": "id:6a328b3b-9e05-4b3b-94c1-551257cc1214",
      "ender": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "time": "2026-09-23T09:33:59.271251"
    },
    {
      "@type": "End",
      "activity": "id:0470b6f9-f5c0-484c-bb2e-534806f95d65",
      "ender": "id:63709288-2770-4d4f-97fa-3e8ff70d0b32",
      "time": "2026-09-23T09:33:59.283374"
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

id:29f23348-9547-4fef-b002-ceefd5b2471b a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%2525252520process/cyanobacteria_color> ],
        [ a prov:Generation ;
            prov:activity id:f5c0b341-97fb-484c-9f8c-0646f0c63e86 ;
            prov:atTime "2026-09-23T09:33:51.697961"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/output_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color" .

id:3b413d9a-adab-454b-8670-0cf37423eec6 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%252525252525252520process/turbidity_plot> ],
        [ a prov:Generation ;
            prov:activity id:5805a5d2-d626-4eee-a0c2-b4167521a820 ;
            prov:atTime "2026-09-23T09:33:56.221505"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/output_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:92c53811eb6d7bad871be5ebee515b4f95e0336a ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot" .

id:7e671680-4e90-4584-89b1-36260f670af1 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%252525252520process/cyanobacteria_plot> ],
        [ a prov:Generation ;
            prov:activity id:f5c0b341-97fb-484c-9f8c-0646f0c63e86 ;
            prov:atTime "2026-09-23T09:33:51.697961"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/output_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:1b832fde3fc0d94955508d006d745a0a9e9b9596 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot" .

id:8fe98067-8e97-40b6-a99a-cf787f26fa36 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:6a328b3b-9e05-4b3b-94c1-551257cc1214 ;
            prov:atTime "2026-09-23T09:33:59.271268"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/output_file> ],
        [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%2520process/chlorophyll_a_color> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e6006027bca29c0e9abb13482a5deea81527097b ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color" .

id:a9c95e1a-ef39-4627-8292-d1020e85dfa1 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:5805a5d2-d626-4eee-a0c2-b4167521a820 ;
            prov:atTime "2026-09-23T09:33:56.221505"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/output_file> ],
        [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%2525252525252520process/turbidity_color> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:823dc9c0e24073601b98c7ac80d545355715c6f5 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color" .

id:ed443e92-82d0-40c9-b63e-724fba739364 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%252520process/chlorophyll_a_plot> ],
        [ a prov:Generation ;
            prov:activity id:6a328b3b-9e05-4b3b-94c1-551257cc1214 ;
            prov:atTime "2026-09-23T09:33:59.271268"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/output_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:9cf89d0572c2a7632f7e096b040d37f8a99b4307 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot" .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/calculate_chlorophyll_a"^^xsd:QName,
        "wf:main/calculate_cyanobacteria"^^xsd:QName,
        "wf:main/calculate_turbidity"^^xsd:QName,
        "wf:main/download_b01_60m"^^xsd:QName,
        "wf:main/download_b02_10m"^^xsd:QName,
        "wf:main/download_b03_10m"^^xsd:QName,
        "wf:main/download_b03_60m"^^xsd:QName,
        "wf:main/download_b04_10m"^^xsd:QName,
        "wf:main/plot_chlorophyll_a"^^xsd:QName,
        "wf:main/plot_cyanobacteria"^^xsd:QName,
        "wf:main/plot_turbidity"^^xsd:QName .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f a wfprov:Artifact,
        prov:Entity ;
    prov:value "B01" .

data:1370052da0755d73768c0c75500107d3759bcc2d a wfprov:Artifact,
        prov:Entity ;
    prov:value """[
  [1E6,  [ 18,  28,  60] ],
  [1E7,  [ 73, 111, 242] ],
  [1E8,  [130, 211,  95] ],
  [1E9,  [254, 253,   5] ],
  [1E10, [253,   0,   4] ],
  [1E11, [142,  32,  38] ],
  [1E12, [111, 63,  125] ],
  [1E13, [ 58,   6,   3] ],
  [1E14, [ 18,  28,  60] ]
]
""" .

data:1b832fde3fc0d94955508d006d745a0a9e9b9596 a wfprov:Artifact,
        prov:Entity .

data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758 a wfprov:Artifact,
        prov:Entity .

data:1edf82bd141d9e642e6ec01d71e53d8107df885c a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_plot" .

data:2b0824b4ba24b098adc7ce01881499891c48d2ea a wfprov:Artifact,
        prov:Entity ;
    prov:value """[
  [0,  [ 73, 111, 242] ],
  [4,  [130, 211,  95] ],
  [8,  [254, 253,   5] ],
  [12, [253,   0,   4] ],
  [16, [142,  32,  38] ],
  [20, [217, 124, 245] ]
]
""" .

data:34bd4f200813f30333e40ecb55d1a316cf2da8af a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity_color" .

data:36dea452bfe795afb42cf14b59c82a3127598281 a wfprov:Artifact,
        prov:Entity ;
    prov:value "B02" .

data:3b00d9df28c7548e79088d660b1d416953bdb464 a wfprov:Artifact,
        prov:Entity .

data:4ad2eab867b3280cabc93a14c615ab97b6b6575e a wfprov:Artifact,
        prov:Entity ;
    prov:value "Cyanobacteria" .

data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8 a wfprov:Artifact,
        prov:Entity ;
    prov:value """[
  [0,  [ 73, 111, 242] ],
  [6,  [130, 211,  95] ],
  [12, [254, 253,   5] ],
  [20, [253,   0,   4] ],
  [30, [142,  32,  38] ],
  [50, [217, 124, 245] ]
]
""" .

data:5d6d0f08e1b29a2d9531b02d6ad6c382ead6b33f a wfprov:Artifact,
        prov:Entity .

data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c a wfprov:Artifact,
        prov:Entity ;
    prov:value "Turbidity" .

data:6be82354dccae2e18c5d885d24c5ea13a3420e1b a wfprov:Artifact,
        prov:Entity .

data:6f7a2e56416e7ae7128bf930d39e5c26ca53c5d7 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_color" .

data:81e487db73b1725c362decd3aac3a2c13f86d595 a wfprov:Artifact,
        prov:Entity ;
    prov:value "(8.93*(C/A))-6.39" .

data:823dc9c0e24073601b98c7ac80d545355715c6f5 a wfprov:Artifact,
        prov:Entity .

data:8655751d19f645dec4f65b6bb306877a7180a3b2 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_color" .

data:86c333c825c3e7e7e612f61b8a330693f3f8bfc2 a wfprov:Artifact,
        prov:Entity .

data:915294efd60b642abdf0ab2947e15fbb5d702a7e a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria" .

data:92c53811eb6d7bad871be5ebee515b4f95e0336a a wfprov:Artifact,
        prov:Entity .

data:9cf89d0572c2a7632f7e096b040d37f8a99b4307 a wfprov:Artifact,
        prov:Entity .

data:a15e03a530b917f396df0bd7bf919d2f342d7ecf a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria_plot" .

data:a67be08b0183aa19f78701cd7fb864462a08af4c a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a" .

data:a87dac8429196320690ec2c17ae2c00532d9e957 a wfprov:Artifact,
        prov:Entity ;
    prov:value "115530.31*(((B.astype(float)*C.astype(float))/A.astype(float))**2.38)" .

data:b42b9a24d33c0b4d0dd3f9942c1c30b83eef37c1 a wfprov:Artifact,
        prov:Entity .

data:b90b2dee65d0b638143e2788b825e245dbe9c4bb a wfprov:Artifact,
        prov:Entity .

data:bfcfb6a10e7a05a5a7c2508fd2c2918e7483c6f5 a wfprov:Artifact,
        prov:Entity .

data:c6f40f302effca33768fc256bbb5dedaca044174 a wfprov:Artifact,
        prov:Entity ;
    prov:value "4.26*((C/A)**3.94)" .

data:cf72a11e7365073ae3c966029d357f3e9b82af8a a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity" .

data:e059662a461e5d1b245f555149febc699f42b537 a wfprov:Artifact,
        prov:Entity ;
    prov:value "Chlorophyll a" .

data:e6006027bca29c0e9abb13482a5deea81527097b a wfprov:Artifact,
        prov:Entity .

data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0 a wfprov:Artifact,
        prov:Entity ;
    prov:value "B04" .

data:f1a11aea9cfbd38e6dbda7e14c05bf9addcd2248 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a_plot" .

data:f670343b66112543f0c884bdf23886e2d7126070 a wfprov:Artifact,
        prov:Entity .

id:0a64bae7-5f25-441b-b114-51f6437fb00f a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%25252525252520process/turbidity> ],
        [ a prov:Generation ;
            prov:activity id:63513262-cbe0-42d8-a5b8-843eba63ae68 ;
            prov:atTime "2026-09-23T09:31:34.569525"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:1e0302087d93ff81d5ec6b3a7a63ad7d0daec758 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_turbidity" .

id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_chlorophyll_a" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a> ],
        [ a prov:Association ;
            prov:agent id:d9e8b09a-c16c-484e-9bc9-27c25011460a ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:50.757388"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:48.321511"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328861"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328703"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328672"^^xsd:dateTime ;
            prov:entity data:a67be08b0183aa19f78701cd7fb864462a08af4c ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328925"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328747"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328691"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.327842"^^xsd:dateTime ;
            prov:entity id:fcc8bc22-4c42-45a2-a828-ef8de070904e ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328819"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328843"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328889"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328898"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328907"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328761"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328781"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328390"^^xsd:dateTime ;
            prov:entity data:c6f40f302effca33768fc256bbb5dedaca044174 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328808"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328799"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328880"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328852"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328871"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328735"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328723"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328790"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328772"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328713"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328916"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.328828"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:48.327798"^^xsd:dateTime ;
            prov:entity id:6e735750-bb9c-4417-b20e-f7ddb07df649 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/band_a> ] .

id:136d036c-1194-4d69-b3c7-538ad435fe46 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" .

id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b03_10m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m> ],
        [ a prov:Association ;
            prov:agent id:136d036c-1194-4d69-b3c7-538ad435fe46 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:13.060666"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:06.038809"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.088513"^^xsd:dateTime ;
            prov:entity data:b75fa50f91a9dd377927a83994bff64245718790 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m/s3_access_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.088207"^^xsd:dateTime ;
            prov:entity data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.087923"^^xsd:dateTime ;
            prov:entity data:5e7cb55727e375cb72dac733c05c4c81c30ffaae ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.088793"^^xsd:dateTime ;
            prov:entity id:e882c92a-6411-4b82-aae7-70be694c29d7 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m/debug> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.087662"^^xsd:dateTime ;
            prov:entity data:7c5d11a451cde788be37383d50239d7672a8cb1f ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.088743"^^xsd:dateTime ;
            prov:entity data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m/s3_secret_key> ] .

id:1855b873-514a-46e8-85f9-7e6fdd5c1c12 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f0b22113-c4b4-451a-894f-30fc14eafc60 ;
            prov:atTime "2026-09-23T09:31:48.067700"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/result> ],
        [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%25252520process/cyanobacteria> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:b90b2dee65d0b638143e2788b825e245dbe9c4bb ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_cyanobacteria" .

id:1a71a853-4269-4af2-9e7e-0b8b9dd37a24 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" .

id:1f7c9599-10e3-4a9f-a64b-c333d730ff68 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b04_10m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:271d494f-4cd0-47bc-86d6-bcd7da4a7ff9 ],
        [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:20.357689"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:13.105700"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:13.111444"^^xsd:dateTime ;
            prov:entity data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:13.112573"^^xsd:dateTime ;
            prov:entity id:a16a5d61-1192-43b9-8be3-6f546af4ccdd ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m/debug> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:13.111934"^^xsd:dateTime ;
            prov:entity data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:13.112207"^^xsd:dateTime ;
            prov:entity data:b75fa50f91a9dd377927a83994bff64245718790 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m/s3_access_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:13.112514"^^xsd:dateTime ;
            prov:entity data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m/s3_secret_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:13.111723"^^xsd:dateTime ;
            prov:entity data:5e7cb55727e375cb72dac733c05c4c81c30ffaae ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m/product_url> ] .

id:271d494f-4cd0-47bc-86d6-bcd7da4a7ff9 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" .

id:27cdb921-72e1-47e6-96a9-08b6f25e590a a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" .

id:489bffb3-47ea-4505-8a69-fb23eacf14a1 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b01_60m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:a8ac9566-6183-46d2-8801-4814c774cbd1 ],
        [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:23.013674"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:20.403484"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:20.410192"^^xsd:dateTime ;
            prov:entity data:b75fa50f91a9dd377927a83994bff64245718790 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m/s3_access_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:20.409969"^^xsd:dateTime ;
            prov:entity data:ccd4d27929279b55bfa676ddddbe7b67aa8d9ce5 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:20.409442"^^xsd:dateTime ;
            prov:entity data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:20.410382"^^xsd:dateTime ;
            prov:entity data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m/s3_secret_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:20.409713"^^xsd:dateTime ;
            prov:entity data:5e7cb55727e375cb72dac733c05c4c81c30ffaae ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:20.410426"^^xsd:dateTime ;
            prov:entity id:fbda755c-26d7-4213-8ac3-437112f3f27a ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m/debug> ] .

id:5001cc2f-8b7b-4b93-9043-8ce09886304f a prov:Agent .

id:55c5cc1e-5f73-4878-8a63-f5d1ab235cb6 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8 ;
            prov:atTime "2026-09-23T09:31:29.673344"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:86c333c825c3e7e7e612f61b8a330693f3f8bfc2 ] ;
    cwlprov:basename "T29SPC_20190701T110621_B02_10m.jp2" ;
    cwlprov:nameext ".jp2" ;
    cwlprov:nameroot "T29SPC_20190701T110621_B02_10m" .

id:63513262-cbe0-42d8-a5b8-843eba63ae68 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_turbidity" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:e9c353d3-6b40-4b92-becb-8bb1decc76b7 ],
        [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:34.569516"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:32.238304"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279781"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279899"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279751"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279891"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279843"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279826"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279679"^^xsd:dateTime ;
            prov:entity data:cf72a11e7365073ae3c966029d357f3e9b82af8a ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279742"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279388"^^xsd:dateTime ;
            prov:entity data:81e487db73b1725c362decd3aac3a2c13f86d595 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279861"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279816"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279760"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279882"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279934"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279711"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279921"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279908"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279733"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.278687"^^xsd:dateTime ;
            prov:entity id:6e735750-bb9c-4417-b20e-f7ddb07df649 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_a> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279722"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279769"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279806"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279852"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279699"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279795"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279872"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.278743"^^xsd:dateTime ;
            prov:entity id:fcc8bc22-4c42-45a2-a828-ef8de070904e ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:32.279835"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_turbidity/band_p> ] .

id:697c2f54-7c7d-4e14-8900-d1e42db3a142 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:6a564363-742d-4015-b71b-70001b3a39ff a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:73af567d-64fb-4113-9d5d-24a98b4a23d5 a prov:Entity ;
    prov:value "100000000000000"^^xsd:int .

id:74e5b6d2-7e78-4e78-9028-bec1988305d6 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b03_60m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:27cdb921-72e1-47e6-96a9-08b6f25e590a ],
        [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:32.223936"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:29.717898"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:29.724514"^^xsd:dateTime ;
            prov:entity data:ccd4d27929279b55bfa676ddddbe7b67aa8d9ce5 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:29.724936"^^xsd:dateTime ;
            prov:entity data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m/s3_secret_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:29.723838"^^xsd:dateTime ;
            prov:entity data:7c5d11a451cde788be37383d50239d7672a8cb1f ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:29.724732"^^xsd:dateTime ;
            prov:entity data:b75fa50f91a9dd377927a83994bff64245718790 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m/s3_access_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:29.724260"^^xsd:dateTime ;
            prov:entity data:5e7cb55727e375cb72dac733c05c4c81c30ffaae ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:29.724989"^^xsd:dateTime ;
            prov:entity id:ee76b2e7-fa78-416c-982a-0034be8e3618 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m/debug> ] .

id:7fb56c04-4cb6-45f5-923c-390c6520ae3a a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ;
            prov:atTime "2026-09-23T09:33:59.283154"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/workflow%20process/chlorophyll_a> ],
        [ a prov:Generation ;
            prov:activity id:0fbabdc1-ddb9-4c88-99d2-7b53d77c7c07 ;
            prov:atTime "2026-09-23T09:31:50.757395"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_chlorophyll_a/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:3b00d9df28c7548e79088d660b1d416953bdb464 ] ;
    cwlprov:basename "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542_chlorophyll_a" .

id:8fc8d4c9-0d3d-43d8-8e04-1fb53d64f191 a prov:Entity ;
    prov:value "1000000"^^xsd:int .

id:97e3cfc5-acf5-4568-8df6-99615db81d5f a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:a16a5d61-1192-43b9-8be3-6f546af4ccdd a prov:Entity ;
    prov:value false .

id:a8ac9566-6183-46d2-8801-4814c774cbd1 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-product-safe:1.1.0" .

id:b379cd45-e93d-43eb-902f-df573b67ccf0 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:15bb5476-8c6a-4c0d-85ac-0ff7f4765451 ;
            prov:atTime "2026-09-23T09:31:13.060679"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_10m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:bfcfb6a10e7a05a5a7c2508fd2c2918e7483c6f5 ] ;
    cwlprov:basename "T29SPC_20190701T110621_B03_10m.jp2" ;
    cwlprov:nameext ".jp2" ;
    cwlprov:nameroot "T29SPC_20190701T110621_B03_10m" .

id:b509d8cc-cc7b-4fdf-88aa-f13c8d9b47c5 a prov:Entity ;
    prov:value false .

id:d9e8b09a-c16c-484e-9bc9-27c25011460a a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:e268cc0e-1073-422f-af40-acfe6b7db163 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:e882c92a-6411-4b82-aae7-70be694c29d7 a prov:Entity ;
    prov:value false .

id:e9c353d3-6b40-4b92-becb-8bb1decc76b7 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:ee76b2e7-fa78-416c-982a-0034be8e3618 a prov:Entity ;
    prov:value false .

id:f0b22113-c4b4-451a-894f-30fc14eafc60 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_cyanobacteria" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:e268cc0e-1073-422f-af40-acfe6b7db163 ],
        [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:48.067683"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:34.582528"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596492"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596617"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596397"^^xsd:dateTime ;
            prov:entity data:915294efd60b642abdf0ab2947e15fbb5d702a7e ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.594422"^^xsd:dateTime ;
            prov:entity id:f1093031-b0f1-4f09-bf38-f001b51a13e5 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596473"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596025"^^xsd:dateTime ;
            prov:entity data:a87dac8429196320690ec2c17ae2c00532d9e957 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596452"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596483"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596558"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596626"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596635"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596576"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596594"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596463"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596658"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596606"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596648"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596585"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596549"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596418"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596530"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596540"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.594405"^^xsd:dateTime ;
            prov:entity id:b379cd45-e93d-43eb-902f-df573b67ccf0 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596433"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596667"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596518"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.596567"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:34.594359"^^xsd:dateTime ;
            prov:entity id:55c5cc1e-5f73-4878-8a63-f5d1ab235cb6 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/calculate_cyanobacteria/band_a> ] .

id:f1093031-b0f1-4f09-bf38-f001b51a13e5 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:1f7c9599-10e3-4a9f-a64b-c333d730ff68 ;
            prov:atTime "2026-09-23T09:31:20.357696"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b04_10m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:f670343b66112543f0c884bdf23886e2d7126070 ] ;
    cwlprov:basename "T29SPC_20190701T110621_B04_10m.jp2" ;
    cwlprov:nameext ".jp2" ;
    cwlprov:nameroot "T29SPC_20190701T110621_B04_10m" .

id:fabfd56f-08a1-4eb4-b698-a069c9e9edb8 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b02_10m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m> ],
        [ a prov:Association ;
            prov:agent id:1a71a853-4269-4af2-9e7e-0b8b9dd37a24 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:31:29.673327"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:23.033156"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:23.053767"^^xsd:dateTime ;
            prov:entity id:b509d8cc-cc7b-4fdf-88aa-f13c8d9b47c5 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m/debug> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:23.049716"^^xsd:dateTime ;
            prov:entity data:36dea452bfe795afb42cf14b59c82a3127598281 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:23.053637"^^xsd:dateTime ;
            prov:entity data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m/s3_secret_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:23.052004"^^xsd:dateTime ;
            prov:entity data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:23.050787"^^xsd:dateTime ;
            prov:entity data:5e7cb55727e375cb72dac733c05c4c81c30ffaae ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:23.052690"^^xsd:dateTime ;
            prov:entity data:b75fa50f91a9dd377927a83994bff64245718790 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b02_10m/s3_access_key> ] .

id:fbda755c-26d7-4213-8ac3-437112f3f27a a prov:Entity ;
    prov:value false .

data:7c5d11a451cde788be37383d50239d7672a8cb1f a wfprov:Artifact,
        prov:Entity ;
    prov:value "B03" .

data:ccd4d27929279b55bfa676ddddbe7b67aa8d9ce5 a wfprov:Artifact,
        prov:Entity ;
    prov:value "60m" .

id:5805a5d2-d626-4eee-a0c2-b4167521a820 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_turbidity" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity> ],
        [ a prov:Association ;
            prov:agent id:6a564363-742d-4015-b71b-70001b3a39ff ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:33:56.221490"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:33:51.980880"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:51.989423"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:51.987879"^^xsd:dateTime ;
            prov:entity data:2b0824b4ba24b098adc7ce01881499891c48d2ea ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:51.989395"^^xsd:dateTime ;
            prov:entity data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:51.989440"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:51.988984"^^xsd:dateTime ;
            prov:entity data:1edf82bd141d9e642e6ec01d71e53d8107df885c ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/plot_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:51.987923"^^xsd:dateTime ;
            prov:entity id:0a64bae7-5f25-441b-b114-51f6437fb00f ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:51.988466"^^xsd:dateTime ;
            prov:entity data:34bd4f200813f30333e40ecb55d1a316cf2da8af ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_turbidity/output_name> ] .

id:6a328b3b-9e05-4b3b-94c1-551257cc1214 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_chlorophyll_a" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a> ],
        [ a prov:Association ;
            prov:agent id:697c2f54-7c7d-4e14-8900-d1e42db3a142 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:33:59.271251"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:33:56.238639"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:56.248701"^^xsd:dateTime ;
            prov:entity data:6f7a2e56416e7ae7128bf930d39e5c26ca53c5d7 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:56.249375"^^xsd:dateTime ;
            prov:entity data:f1a11aea9cfbd38e6dbda7e14c05bf9addcd2248 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/plot_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:56.249875"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:56.247945"^^xsd:dateTime ;
            prov:entity data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:56.249891"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:56.249844"^^xsd:dateTime ;
            prov:entity data:e059662a461e5d1b245f555149febc699f42b537 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:33:56.248008"^^xsd:dateTime ;
            prov:entity id:7fb56c04-4cb6-45f5-923c-390c6520ae3a ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_chlorophyll_a/input_image> ] .

id:6e735750-bb9c-4417-b20e-f7ddb07df649 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:489bffb3-47ea-4505-8a69-fb23eacf14a1 ;
            prov:atTime "2026-09-23T09:31:23.013686"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b01_60m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:5d6d0f08e1b29a2d9531b02d6ad6c382ead6b33f ] ;
    cwlprov:basename "T29SPC_20190701T110621_B01_60m.jp2" ;
    cwlprov:nameext ".jp2" ;
    cwlprov:nameroot "T29SPC_20190701T110621_B01_60m" .

id:f5c0b341-97fb-484c-9f8c-0646f0c63e86 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_cyanobacteria" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria> ],
        [ a prov:Association ;
            prov:agent id:97e3cfc5-acf5-4568-8df6-99615db81d5f ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:33:51.697918"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:50.769647"^^xsd:dateTime ;
            prov:hadActivity id:0470b6f9-f5c0-484c-bb2e-534806f95d65 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:50.804535"^^xsd:dateTime ;
            prov:entity data:8655751d19f645dec4f65b6bb306877a7180a3b2 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:50.804800"^^xsd:dateTime ;
            prov:entity data:a15e03a530b917f396df0bd7bf919d2f342d7ecf ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/plot_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:50.803738"^^xsd:dateTime ;
            prov:entity id:8fc8d4c9-0d3d-43d8-8e04-1fb53d64f191 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:50.803703"^^xsd:dateTime ;
            prov:entity id:73af567d-64fb-4113-9d5d-24a98b4a23d5 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:50.804251"^^xsd:dateTime ;
            prov:entity data:1370052da0755d73768c0c75500107d3759bcc2d ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:50.805055"^^xsd:dateTime ;
            prov:entity data:4ad2eab867b3280cabc93a14c615ab97b6b6575e ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:50.804275"^^xsd:dateTime ;
            prov:entity id:1855b873-514a-46e8-85f9-7e6fdd5c1c12 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/plot_cyanobacteria/input_image> ] .

id:fcc8bc22-4c42-45a2-a828-ef8de070904e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:74e5b6d2-7e78-4e78-9028-bec1988305d6 ;
            prov:atTime "2026-09-23T09:31:32.223947"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/download_b03_60m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:6be82354dccae2e18c5d885d24c5ea13a3420e1b ] ;
    cwlprov:basename "T29SPC_20190701T110621_B03_60m.jp2" ;
    cwlprov:nameext ".jp2" ;
    cwlprov:nameroot "T29SPC_20190701T110621_B03_60m" .

data:6e0ff3f48a8e5ea3d6694c8c7ad596728e98090b a wfprov:Artifact,
        prov:Entity ;
    prov:value "10m" .

data:5e7cb55727e375cb72dac733c05c4c81c30ffaae a wfprov:Artifact,
        prov:Entity ;
    prov:value "s3:///eodata/Sentinel-2/MSI/L2A_N0500/2019/07/01/S2A_MSIL2A_20190701T110621_N0500_R137_T29SPC_20230604T023542.SAFE" .

data:b75fa50f91a9dd377927a83994bff64245718790 a wfprov:Artifact,
        prov:Entity ;
    prov:value "(secret-bf20402e-6bb5-4f48-bf22-6d3ef7bff99c)" .

data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 a wfprov:Artifact,
        prov:Entity ;
    prov:value "(secret-12440283-71a1-46b4-9702-9c8e432a31e6)" .

id:63709288-2770-4d4f-97fa-3e8ff70d0b32 a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:01.456509"^^xsd:dateTime ;
            prov:hadActivity id:5001cc2f-8b7b-4b93-9043-8ce09886304f ] .

id:0470b6f9-f5c0-484c-bb2e-534806f95d65 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T09:33:59.283374"^^xsd:dateTime ;
            prov:hadActivity id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T09:31:01.456549"^^xsd:dateTime ;
            prov:hadActivity id:63709288-2770-4d4f-97fa-3e8ff70d0b32 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.037821"^^xsd:dateTime ;
            prov:entity data:f6cab44ac3c9f733bfece9ad8d3ad1452cbf9570 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/s3_secret_key> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T09:31:06.037596"^^xsd:dateTime ;
            prov:entity data:b75fa50f91a9dd377927a83994bff64245718790 ;
            prov:hadRole <arcp://uuid,44c595c3-0138-459e-bff2-432829fe1bf3/workflow/packed.cwl#main/s3_access_key> ] ;
    prov:startedAtTime "2026-09-23T09:31:01.456528"^^xsd:dateTime .

cwlprov:None a prov:Entity ;
    rdfs:label "None" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `algae-usecase-workflow-copernicus-process`
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
      const: algae-usecase-workflow-copernicus-process
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - product_url
      - s3_access_key
      - s3_secret_key
      propertyNames:
        enum:
        - product_url
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
        - product_url
        - s3_access_key
        - s3_secret_key
        propertyNames:
          enum:
          - product_url
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/workflow-copernicus-process/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/algae-bloom/workflow-copernicus-process`

