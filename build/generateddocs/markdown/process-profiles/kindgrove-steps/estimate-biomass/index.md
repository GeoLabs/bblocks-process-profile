
# Process profile: estimate_biomass (Schema)

`ospd.process-profiles.kindgrove-steps.estimate-biomass` *v0.1*

OGC API - Processes profile of the CWL CommandLineTool `estimate_biomass` (W2 KindGrove), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`estimate_biomass`** (CommandLineTool, W2b KindGrove (step notebooks)).

> Mangrove detection, allometric biomass and IPCC carbon stock

## Source

- CWL: [mangrove-workflow-steps.cwl#estimate_biomass](https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass) (GitHub Release `v0.0.2-rc2`, sha256 `361cb6a75d54`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none; candidates: `eoap.cct.stac`
- Used by: `ospd.process-profiles.kindgrove-steps.mangrove-workflow-steps`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `ndvi_file` | File | `mangrove_mask_file` | File |
| `ndwi_file` | File | `biomass_file` | File |
| `savi_file` | File | `biomass_summary_file` | File |
| `stac_item` | File | `carbon_summary_file` | File |
| `ndvi_min` | float? | `analysis_summary_file` | File |
| `ndvi_max` | float? |  |  |
| `ndwi_min` | float? |  |  |
| `savi_min` | float? |  |  |
| `biomass_slope` | float? |  |  |
| `biomass_intercept` | float? |  |  |
| `carbon_fraction` | float? |  |  |

## Analysis

**Behaviour.** `/app/cwl/bin/steps/05_estimate_biomass`, `ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2`.
Masks pixels within the `ndvi_min`/`ndvi_max`/`ndwi_min`/`savi_min` thresholds as mangrove,
applies `biomass = biomass_slope * ndvi + biomass_intercept` per masked pixel, and
`carbon = biomass * carbon_fraction`; writes the mask, the biomass raster, two CSV summaries
and a JSON analysis summary.

**CWL specifics.** `stac_item` (the scene's own STAC Item) is threaded through purely to
carry scene metadata into the outputs, not read as a raster.

**Provenance.** Three file inputs (ndvi/ndwi/savi) plus the STAC item; five file outputs, a
genuine fan-in/fan-out (GP-10 applies here the same way it does to `kindgrove.mangrove`).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `kindgrove-steps`: the pinned W2b source itself (GeoLabs/KindGrove v0.0.2-rc2 `mangrove-workflow-steps.cwl#mangrove-workflow-steps`), the same execute inputs as `w2-pinned` for comparability, `cwltool --enable-ext --provenance ro --outdir out`, 2026-09-24, cwltool 3.1.20260108082145 on an arm64 macOS host, ~5 min; scene selected by `days_back` on that day, three bands scattered (red, green, nir) through download_band and reproject_band), activity `main/estimate_biomass` (engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** Opaque: a threshold-based mangrove mask (ndvi_min/max, ndwi_min, savi_min) followed by a fixed linear allometric formula (biomass_slope/intercept) and an IPCC carbon_fraction constant. No openEO process expresses a domain-specific regression model, same as `kindgrove.mangrove`.


## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL CommandLineTool is referenced, not copied: <https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass>.

### processDescription
OGC API - Processes processDescription derived from the CWL.
#### json
```json
{
  "id": "estimate_biomass",
  "version": "0.1.0",
  "title": "estimate_biomass",
  "description": "Process converted from CWL",
  "mutable": true,
  "keywords": [
    "ospd",
    "mangrove",
    "biomass",
    "carbon"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "estimate_biomass"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "0.1.0"
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://github.com/starling-foundries/KindGrove"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
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
        "affiliation": "GeoLabs"
      }
    },
    {
      "role": "https://schema.org/description",
      "value": "Mangrove detection, allometric biomass and IPCC carbon stock"
    }
  ],
  "inputs": {
    "ndvi_file": {
      "title": "ndvi_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "ndwi_file": {
      "title": "ndwi_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "savi_file": {
      "title": "savi_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "stac_item": {
      "title": "stac_item",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "ndvi_min": {
      "title": "ndvi_min",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.3
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "ndvi_max": {
      "title": "ndvi_max",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.9
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "ndwi_min": {
      "title": "ndwi_min",
      "description": "",
      "schema": {
        "type": "number",
        "default": -0.3
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "savi_min": {
      "title": "savi_min",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.2
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "biomass_slope": {
      "title": "biomass_slope",
      "description": "",
      "schema": {
        "type": "number",
        "default": 250.5
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "biomass_intercept": {
      "title": "biomass_intercept",
      "description": "",
      "schema": {
        "type": "number",
        "default": -75.2
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "carbon_fraction": {
      "title": "carbon_fraction",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.47
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "mangrove_mask_file": {
      "title": "mangrove_mask_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "biomass_file": {
      "title": "biomass_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "biomass_summary_file": {
      "title": "biomass_summary_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "carbon_summary_file": {
      "title": "carbon_summary_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "analysis_summary_file": {
      "title": "analysis_summary_file",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld",
  "id": "estimate_biomass",
  "version": "0.1.0",
  "title": "estimate_biomass",
  "description": "Process converted from CWL",
  "mutable": true,
  "keywords": [
    "ospd",
    "mangrove",
    "biomass",
    "carbon"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "estimate_biomass"
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "0.1.0"
    },
    {
      "role": "https://schema.org/codeRepository",
      "value": "https://github.com/starling-foundries/KindGrove"
    },
    {
      "role": "https://schema.org/license",
      "value": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
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
        "affiliation": "GeoLabs"
      }
    },
    {
      "role": "https://schema.org/description",
      "value": "Mangrove detection, allometric biomass and IPCC carbon stock"
    }
  ],
  "inputs": {
    "ndvi_file": {
      "title": "ndvi_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "ndwi_file": {
      "title": "ndwi_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "savi_file": {
      "title": "savi_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "stac_item": {
      "title": "stac_item",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "ndvi_min": {
      "title": "ndvi_min",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.3
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "ndvi_max": {
      "title": "ndvi_max",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.9
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "ndwi_min": {
      "title": "ndwi_min",
      "description": "",
      "schema": {
        "type": "number",
        "default": -0.3
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "savi_min": {
      "title": "savi_min",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.2
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "biomass_slope": {
      "title": "biomass_slope",
      "description": "",
      "schema": {
        "type": "number",
        "default": 250.5
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "biomass_intercept": {
      "title": "biomass_intercept",
      "description": "",
      "schema": {
        "type": "number",
        "default": -75.2
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "carbon_fraction": {
      "title": "carbon_fraction",
      "description": "",
      "schema": {
        "type": "number",
        "default": 0.47
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "mangrove_mask_file": {
      "title": "mangrove_mask_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "biomass_file": {
      "title": "biomass_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "biomass_summary_file": {
      "title": "biomass_summary_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "carbon_summary_file": {
      "title": "carbon_summary_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "analysis_summary_file": {
      "title": "analysis_summary_file",
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
@prefix ns3: <http://schema.org/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/estimate_biomass> dcterms:description "Process converted from CWL" ;
    dcterms:subject "biomass",
        "carbon",
        "mangrove",
        "ospd" ;
    dcterms:title "estimate_biomass" ;
    pp:version "0.1.0" ;
    proc:inputs [ ns1:biomass_intercept [ dcterms:description "" ;
                    dcterms:title "biomass_intercept" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "-75.2"^^rdf:JSON ;
                            proc:type "number" ] ] ;
            ns1:biomass_slope [ dcterms:description "" ;
                    dcterms:title "biomass_slope" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "250.5"^^rdf:JSON ;
                            proc:type "number" ] ] ;
            ns1:carbon_fraction [ dcterms:description "" ;
                    dcterms:title "carbon_fraction" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "0.47"^^rdf:JSON ;
                            proc:type "number" ] ] ;
            ns1:ndvi_file [ dcterms:description "" ;
                    dcterms:title "ndvi_file" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:ndvi_max [ dcterms:description "" ;
                    dcterms:title "ndvi_max" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "0.9"^^rdf:JSON ;
                            proc:type "number" ] ] ;
            ns1:ndvi_min [ dcterms:description "" ;
                    dcterms:title "ndvi_min" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "0.3"^^rdf:JSON ;
                            proc:type "number" ] ] ;
            ns1:ndwi_file [ dcterms:description "" ;
                    dcterms:title "ndwi_file" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:ndwi_min [ dcterms:description "" ;
                    dcterms:title "ndwi_min" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "-0.3"^^rdf:JSON ;
                            proc:type "number" ] ] ;
            ns1:savi_file [ dcterms:description "" ;
                    dcterms:title "savi_file" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns1:savi_min [ dcterms:description "" ;
                    dcterms:title "savi_min" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "0.2"^^rdf:JSON ;
                            proc:type "number" ] ] ;
            ns1:stac_item [ dcterms:description "" ;
                    dcterms:title "stac_item" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "Mangrove detection, allometric biomass and IPCC carbon stock" ;
            proc:role schema:description ],
        [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ],
        [ rdf:value "https://github.com/starling-foundries/KindGrove" ;
            proc:role schema:codeRepository ],
        [ rdf:value "0.1.0" ;
            proc:role schema:softwareVersion ],
        [ rdf:value [ a ns3:Person ;
                    ns3:name "Cameron Sajedi" ] ;
            proc:role schema:author ],
        [ rdf:value [ a ns3:Person ;
                    ns3:affiliation "GeoLabs" ;
                    ns3:name "Gérald Fenoy" ] ;
            proc:role schema:contributor ],
        [ rdf:value "estimate_biomass" ;
            proc:role schema:name ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns4:analysis_summary_file [ dcterms:description "" ;
                    dcterms:title "analysis_summary_file" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns4:biomass_file [ dcterms:description "" ;
                    dcterms:title "biomass_file" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns4:biomass_summary_file [ dcterms:description "" ;
                    dcterms:title "biomass_summary_file" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns4:carbon_summary_file [ dcterms:description "" ;
                    dcterms:title "carbon_summary_file" ;
                    proc:schema [ proc:type "string" ;
                            ns2:contentMediaType "application/octet-stream" ] ] ;
            ns4:mangrove_mask_file [ dcterms:description "" ;
                    dcterms:title "mangrove_mask_file" ;
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
      "id": "estimate_biomass",
      "version": "0.1.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld",
  "processDescription": {
    "process": {
      "id": "estimate_biomass",
      "version": "0.1.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/estimate_biomass> pp:version "0.1.0" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/estimate_biomass> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass" ;
            pp:rel "http://www.opengis.net/def/rel/ogc/1.0/executionUnit" ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "ndvi_file": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndvi.tif",
      "type": "image/tiff; application=geotiff"
    },
    "ndwi_file": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndwi.tif",
      "type": "image/tiff; application=geotiff"
    },
    "savi_file": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/savi.tif",
      "type": "image/tiff; application=geotiff"
    },
    "stac_item": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/scene_item.json",
      "type": "application/geo+json"
    }
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld",
  "inputs": {
    "ndvi_file": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndvi.tif",
      "type": "image/tiff; application=geotiff"
    },
    "ndwi_file": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndwi.tif",
      "type": "image/tiff; application=geotiff"
    },
    "savi_file": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/savi.tif",
      "type": "image/tiff; application=geotiff"
    },
    "stac_item": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/scene_item.json",
      "type": "application/geo+json"
    }
  },
  "response": "document"
}
```

#### ttl
```ttl
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

[] proc:inputs [ ns1:ndvi_file [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndvi.tif" ;
                    proc:type "image/tiff; application=geotiff" ] ;
            ns1:ndwi_file [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndwi.tif" ;
                    proc:type "image/tiff; application=geotiff" ] ;
            ns1:savi_file [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/savi.tif" ;
                    proc:type "image/tiff; application=geotiff" ] ;
            ns1:stac_item [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/scene_item.json" ;
                    proc:type "application/geo+json" ] ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "analysis_summary_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/analysis_summary.json",
    "type": "application/json"
  },
  "biomass_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass.tif",
    "type": "image/tiff; application=geotiff"
  },
  "biomass_summary_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass_summary.csv",
    "type": "text/csv"
  },
  "carbon_summary_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/carbon_summary.csv",
    "type": "text/csv"
  },
  "mangrove_mask_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/mangrove_mask.tif",
    "type": "image/tiff; application=geotiff"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld",
  "analysis_summary_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/analysis_summary.json",
    "type": "application/json"
  },
  "biomass_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass.tif",
    "type": "image/tiff; application=geotiff"
  },
  "biomass_summary_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass_summary.csv",
    "type": "text/csv"
  },
  "carbon_summary_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/carbon_summary.csv",
    "type": "text/csv"
  },
  "mangrove_mask_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/mangrove_mask.tif",
    "type": "image/tiff; application=geotiff"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:analysis_summary_file [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/json> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/analysis_summary.json" ] ;
    pp:biomass_file [ pp:href "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass.tif" ] ;
    pp:biomass_summary_file [ a <https://geolabs.github.io/bblocks-process-profiles/def/text/csv> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass_summary.csv" ] ;
    pp:carbon_summary_file [ a <https://geolabs.github.io/bblocks-process-profiles/def/text/csv> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/carbon_summary.csv" ] ;
    pp:mangrove_mask_file [ pp:href "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/mangrove_mask.tif" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:kindgrove-steps:estimate-biomass",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass",
    "startedAtTime": "2026-09-24T10:59:40Z",
    "used": [
      "urn:example:entity:estimate-biomass:in:ndvi_file",
      "urn:example:entity:estimate-biomass:in:ndwi_file",
      "urn:example:entity:estimate-biomass:in:savi_file",
      "urn:example:entity:estimate-biomass:in:stac_item"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145",
      "urn:example:image:ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/estimate_biomass"
      }
    ],
    "endedAtTime": "2026-09-24T10:59:47Z"
  },
  {
    "id": "urn:example:entity:estimate-biomass:in:ndvi_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/ndvi_file",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndvi.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  {
    "id": "urn:example:entity:estimate-biomass:in:ndwi_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/ndwi_file",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndwi.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  {
    "id": "urn:example:entity:estimate-biomass:in:savi_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/savi_file",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/savi.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  {
    "id": "urn:example:entity:estimate-biomass:in:stac_item",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/stac_item",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/scene_item.json",
        "rel": "item",
        "type": "application/geo+json"
      }
    ]
  },
  {
    "id": "urn:example:entity:estimate-biomass:out:analysis_summary_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/analysis_summary_file",
    "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
    "wasDerivedFrom": [
      "urn:example:entity:estimate-biomass:in:ndvi_file",
      "urn:example:entity:estimate-biomass:in:ndwi_file",
      "urn:example:entity:estimate-biomass:in:savi_file",
      "urn:example:entity:estimate-biomass:in:stac_item"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/analysis_summary.json",
        "rel": "item",
        "type": "application/json"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:estimate-biomass:out:biomass_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/biomass_file",
    "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
    "wasDerivedFrom": [
      "urn:example:entity:estimate-biomass:in:ndvi_file",
      "urn:example:entity:estimate-biomass:in:ndwi_file",
      "urn:example:entity:estimate-biomass:in:savi_file",
      "urn:example:entity:estimate-biomass:in:stac_item"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:estimate-biomass:out:biomass_summary_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/biomass_summary_file",
    "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
    "wasDerivedFrom": [
      "urn:example:entity:estimate-biomass:in:ndvi_file",
      "urn:example:entity:estimate-biomass:in:ndwi_file",
      "urn:example:entity:estimate-biomass:in:savi_file",
      "urn:example:entity:estimate-biomass:in:stac_item"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass_summary.csv",
        "rel": "item",
        "type": "text/csv"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:estimate-biomass:out:carbon_summary_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/carbon_summary_file",
    "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
    "wasDerivedFrom": [
      "urn:example:entity:estimate-biomass:in:ndvi_file",
      "urn:example:entity:estimate-biomass:in:ndwi_file",
      "urn:example:entity:estimate-biomass:in:savi_file",
      "urn:example:entity:estimate-biomass:in:stac_item"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/carbon_summary.csv",
        "rel": "item",
        "type": "text/csv"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:estimate-biomass:out:mangrove_mask_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/mangrove_mask_file",
    "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
    "wasDerivedFrom": [
      "urn:example:entity:estimate-biomass:in:ndvi_file",
      "urn:example:entity:estimate-biomass:in:ndwi_file",
      "urn:example:entity:estimate-biomass:in:savi_file",
      "urn:example:entity:estimate-biomass:in:stac_item"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/mangrove_mask.tif",
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
    "id": "urn:example:image:ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2",
    "provType": "prov:SoftwareAgent",
    "name": "container image ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2"
  }
]

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:kindgrove-steps:estimate-biomass",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass",
      "startedAtTime": "2026-09-24T10:59:40Z",
      "used": [
        "urn:example:entity:estimate-biomass:in:ndvi_file",
        "urn:example:entity:estimate-biomass:in:ndwi_file",
        "urn:example:entity:estimate-biomass:in:savi_file",
        "urn:example:entity:estimate-biomass:in:stac_item"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145",
        "urn:example:image:ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/estimate_biomass"
        }
      ],
      "endedAtTime": "2026-09-24T10:59:47Z"
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:ndvi_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/ndvi_file",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndvi.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ]
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:ndwi_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/ndwi_file",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndwi.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ]
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:savi_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/savi_file",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/savi.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ]
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:stac_item",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/stac_item",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/scene_item.json",
          "rel": "item",
          "type": "application/geo+json"
        }
      ]
    },
    {
      "id": "urn:example:entity:estimate-biomass:out:analysis_summary_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/analysis_summary_file",
      "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
      "wasDerivedFrom": [
        "urn:example:entity:estimate-biomass:in:ndvi_file",
        "urn:example:entity:estimate-biomass:in:ndwi_file",
        "urn:example:entity:estimate-biomass:in:savi_file",
        "urn:example:entity:estimate-biomass:in:stac_item"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/analysis_summary.json",
          "rel": "item",
          "type": "application/json"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:estimate-biomass:out:biomass_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/biomass_file",
      "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
      "wasDerivedFrom": [
        "urn:example:entity:estimate-biomass:in:ndvi_file",
        "urn:example:entity:estimate-biomass:in:ndwi_file",
        "urn:example:entity:estimate-biomass:in:savi_file",
        "urn:example:entity:estimate-biomass:in:stac_item"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:estimate-biomass:out:biomass_summary_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/biomass_summary_file",
      "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
      "wasDerivedFrom": [
        "urn:example:entity:estimate-biomass:in:ndvi_file",
        "urn:example:entity:estimate-biomass:in:ndwi_file",
        "urn:example:entity:estimate-biomass:in:savi_file",
        "urn:example:entity:estimate-biomass:in:stac_item"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass_summary.csv",
          "rel": "item",
          "type": "text/csv"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:estimate-biomass:out:carbon_summary_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/carbon_summary_file",
      "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
      "wasDerivedFrom": [
        "urn:example:entity:estimate-biomass:in:ndvi_file",
        "urn:example:entity:estimate-biomass:in:ndwi_file",
        "urn:example:entity:estimate-biomass:in:savi_file",
        "urn:example:entity:estimate-biomass:in:stac_item"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/carbon_summary.csv",
          "rel": "item",
          "type": "text/csv"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:estimate-biomass:out:mangrove_mask_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/mangrove_mask_file",
      "wasGeneratedBy": "urn:example:run:kindgrove-steps:estimate-biomass",
      "wasDerivedFrom": [
        "urn:example:entity:estimate-biomass:in:ndvi_file",
        "urn:example:entity:estimate-biomass:in:ndwi_file",
        "urn:example:entity:estimate-biomass:in:savi_file",
        "urn:example:entity:estimate-biomass:in:stac_item"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/mangrove_mask.tif",
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
      "id": "urn:example:image:ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2",
      "provType": "prov:SoftwareAgent",
      "name": "container image ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2"
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
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:entity:estimate-biomass:out:analysis_summary_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/analysis_summary_file> ;
    rdfs:seeAlso [ dcterms:type "application/json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/analysis_summary.json> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:estimate-biomass:in:ndvi_file>,
        <urn:example:entity:estimate-biomass:in:ndwi_file>,
        <urn:example:entity:estimate-biomass:in:savi_file>,
        <urn:example:entity:estimate-biomass:in:stac_item> ;
    prov:wasGeneratedBy <urn:example:run:kindgrove-steps:estimate-biomass> .

<urn:example:entity:estimate-biomass:out:biomass_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/biomass_file> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:estimate-biomass:in:ndvi_file>,
        <urn:example:entity:estimate-biomass:in:ndwi_file>,
        <urn:example:entity:estimate-biomass:in:savi_file>,
        <urn:example:entity:estimate-biomass:in:stac_item> ;
    prov:wasGeneratedBy <urn:example:run:kindgrove-steps:estimate-biomass> .

<urn:example:entity:estimate-biomass:out:biomass_summary_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/biomass_summary_file> ;
    rdfs:seeAlso [ dcterms:type "text/csv" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/biomass_summary.csv> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:estimate-biomass:in:ndvi_file>,
        <urn:example:entity:estimate-biomass:in:ndwi_file>,
        <urn:example:entity:estimate-biomass:in:savi_file>,
        <urn:example:entity:estimate-biomass:in:stac_item> ;
    prov:wasGeneratedBy <urn:example:run:kindgrove-steps:estimate-biomass> .

<urn:example:entity:estimate-biomass:out:carbon_summary_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/carbon_summary_file> ;
    rdfs:seeAlso [ dcterms:type "text/csv" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/carbon_summary.csv> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:estimate-biomass:in:ndvi_file>,
        <urn:example:entity:estimate-biomass:in:ndwi_file>,
        <urn:example:entity:estimate-biomass:in:savi_file>,
        <urn:example:entity:estimate-biomass:in:stac_item> ;
    prov:wasGeneratedBy <urn:example:run:kindgrove-steps:estimate-biomass> .

<urn:example:entity:estimate-biomass:out:mangrove_mask_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#outputs/mangrove_mask_file> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/kindgrove-steps-estimate-biomass-0001/results/mangrove_mask.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:estimate-biomass:in:ndvi_file>,
        <urn:example:entity:estimate-biomass:in:ndwi_file>,
        <urn:example:entity:estimate-biomass:in:savi_file>,
        <urn:example:entity:estimate-biomass:in:stac_item> ;
    prov:wasGeneratedBy <urn:example:run:kindgrove-steps:estimate-biomass> .

<urn:example:image:ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2> a prov:SoftwareAgent ;
    pp:name "container image ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2" .

<urn:example:run:kindgrove-steps:estimate-biomass> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass> ;
    prov:endedAtTime "2026-09-24T10:59:47+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/estimate_biomass> ] ;
    prov:startedAtTime "2026-09-24T10:59:40+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:estimate-biomass:in:ndvi_file>,
        <urn:example:entity:estimate-biomass:in:ndwi_file>,
        <urn:example:entity:estimate-biomass:in:savi_file>,
        <urn:example:entity:estimate-biomass:in:stac_item> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145>,
        <urn:example:image:ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2> .

<urn:example:entity:estimate-biomass:in:ndvi_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/ndvi_file> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndvi.tif> ] .

<urn:example:entity:estimate-biomass:in:ndwi_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/ndwi_file> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/upstream-step/results/ndwi.tif> ] .

<urn:example:entity:estimate-biomass:in:savi_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/savi_file> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/upstream-step/results/savi.tif> ] .

<urn:example:entity:estimate-biomass:in:stac_item> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/estimate_biomass#inputs/stac_item> ;
    rdfs:seeAlso [ dcterms:type "application/geo+json" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/upstream-step/results/scene_item.json> ] .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Process run (wfprov:ProcessRun, gap GP-1)
#### json
```json
{
  "id": "urn:example:run:kindgrove-steps:estimate-biomass",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/estimate_biomass",
  "usedInput": [
    {
      "id": "urn:example:entity:estimate-biomass:in:ndvi_file"
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:ndwi_file"
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:savi_file"
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:stac_item"
    }
  ],
  "startedAtTime": "2026-09-24T10:59:40Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:kindgrove-steps:mangrove-workflow-steps"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld",
  "id": "urn:example:run:kindgrove-steps:estimate-biomass",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/estimate_biomass",
  "usedInput": [
    {
      "id": "urn:example:entity:estimate-biomass:in:ndvi_file"
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:ndwi_file"
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:savi_file"
    },
    {
      "id": "urn:example:entity:estimate-biomass:in:stac_item"
    }
  ],
  "startedAtTime": "2026-09-24T10:59:40Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:kindgrove-steps:mangrove-workflow-steps"
}
```

#### ttl
```ttl
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:run:kindgrove-steps:estimate-biomass> a wfprov:ProcessRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass> ;
    wfprov:describedByProcess <https://ospd.example.org/ogc-api/processes/estimate_biomass> ;
    wfprov:usedInput <urn:example:entity:estimate-biomass:in:ndvi_file>,
        <urn:example:entity:estimate-biomass:in:ndwi_file>,
        <urn:example:entity:estimate-biomass:in:savi_file>,
        <urn:example:entity:estimate-biomass:in:stac_item> ;
    wfprov:wasPartOfWorkflowRun <urn:example:run:kindgrove-steps:mangrove-workflow-steps> ;
    prov:startedAtTime "2026-09-24T10:59:40+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass",
  "type": "ProcessType",
  "prefLabel": "Mangrove detection, allometric biomass and IPCC carbon stock",
  "definition": "Detects mangrove pixels and estimates above-ground biomass and carbon stock from NDVI, NDWI and SAVI.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.kindgrove-steps.estimate-biomass",
  "processDescription": {
    "id": "estimate_biomass",
    "version": "0.1.0"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass",
    "cwlClass": "CommandLineTool",
    "cwlId": "estimate_biomass",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.stac"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Opaque: a threshold-based mangrove mask (ndvi_min/max, ndwi_min, savi_min) followed by a fixed linear allometric formula (biomass_slope/intercept) and an IPCC carbon_fraction constant. No openEO process expresses a domain-specific regression model, same as `kindgrove.mangrove`."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass",
  "type": "ProcessType",
  "prefLabel": "Mangrove detection, allometric biomass and IPCC carbon stock",
  "definition": "Detects mangrove pixels and estimates above-ground biomass and carbon stock from NDVI, NDWI and SAVI.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation"
  ],
  "profile": "ospd.process-profiles.kindgrove-steps.estimate-biomass",
  "processDescription": {
    "id": "estimate_biomass",
    "version": "0.1.0"
  },
  "source": {
    "cwl": "https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass",
    "cwlClass": "CommandLineTool",
    "cwlId": "estimate_biomass",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [
    "eoap.cct.stac"
  ],
  "openeoEquivalence": {
    "level": "none",
    "rationale": "Opaque: a threshold-based mangrove mask (ndvi_min/max, ndwi_min, savi_min) followed by a fixed linear allometric formula (biomass_slope/intercept) and an IPCC carbon_fraction constant. No openEO process expresses a domain-specific regression model, same as `kindgrove.mangrove`."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/kindgrove-steps/estimate-biomass> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/scientific-computation> ;
    skos:definition "Detects mangrove pixels and estimates above-ground biomass and carbon stock from NDVI, NDWI and SAVI." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Mangrove detection, allometric biomass and IPCC carbon stock" ;
    pp:candidateCctDependency "eoap.cct.stac" ;
    pp:openeoEquivalence [ pp:equivalenceLevel "none" ;
            pp:rationale "Opaque: a threshold-based mangrove mask (ndvi_min/max, ndwi_min, savi_min) followed by a fixed linear allometric formula (biomass_slope/intercept) and an IPCC carbon_fraction constant. No openEO process expresses a domain-specific regression model, same as `kindgrove.mangrove`." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/estimate_biomass> ;
    pp:profile "ospd.process-profiles.kindgrove-steps.estimate-biomass" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:source [ pp:cwl <https://github.com/GeoLabs/KindGrove/releases/download/v0.0.2-rc2/mangrove-workflow-steps.cwl#estimate_biomass> ;
            pp:cwlClass "CommandLineTool" ;
            pp:cwlId "estimate_biomass" ;
            pp:license "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/estimate_biomass> pp:version "0.1.0" .


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
      "researchobject": "arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/",
      "metadata": "arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/metadata/",
      "provenance": "arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/metadata/provenance/",
      "wf": "arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#",
      "input": "arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/primary-job.json#",
      "wf4ever": "http://purl.org/wf4ever/wf4ever#",
      "ro": "http://purl.org/wf4ever/ro#",
      "ore": "http://www.openarchives.org/ore/terms/"
    },
    "https://openprovenance.org/prov-jsonld/context.jsonld"
  ],
  "@graph": [
    {
      "@type": "Agent",
      "@id": "id:82a589e5-da3e-471d-959a-5f0ada295abf"
    },
    {
      "@type": "Agent",
      "@id": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
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
      "@id": "id:f6c152ab-0593-4080-aa4f-1eeb02a954b6",
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
      "@id": "id:4d33da78-bc2b-4f11-927c-55071695661b",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/select-scene:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/select-scene:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:f3cf79d9-5592-4f15-a94b-728004a97650",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:112f1253-d984-432e-8b9c-f6b600dc0867",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:0a68208c-621e-48fe-b955-774694ac318c",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:7dcbf0c1-1cea-4c69-a6a5-252d188398ca",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:7814458d-34a1-43b8-91a4-d47c15a05095",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:936a4bd7-abcd-4bf2-9423-94ae772bd057",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:0628dd54-097a-4857-a725-9ce3cd63fc2c",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/calculate-indices:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/calculate-indices:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:e932c1b9-7fde-4dbd-a1af-1b17de8a38de",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:114fd6b8-e343-4c8d-b816-20e051ac87a0",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ghcr.io/geolabs/kindgrove/export-stac:v0.0.2-rc2"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ghcr.io/geolabs/kindgrove/export-stac:v0.0.2-rc2"
        }
      ]
    },
    {
      "@type": "Start",
      "activity": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "starter": "id:82a589e5-da3e-471d-959a-5f0ada295abf",
      "time": "2026-09-24T12:57:44.628379"
    },
    {
      "@type": "Start",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "starter": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "time": "2026-09-24T12:57:44.628464"
    },
    {
      "@type": "Start",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:57:45.249740"
    },
    {
      "@type": "Start",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:57:48.481355"
    },
    {
      "@type": "Start",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:58:01.354035"
    },
    {
      "@type": "Start",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:58:16.254478"
    },
    {
      "@type": "Start",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:58:36.186017"
    },
    {
      "@type": "Start",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:12.204580"
    },
    {
      "@type": "Start",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:18.360040"
    },
    {
      "@type": "Start",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:25.490304"
    },
    {
      "@type": "Start",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:32.442072"
    },
    {
      "@type": "Start",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:40.439020"
    },
    {
      "@type": "Start",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "starter": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:47.598635"
    },
    {
      "@type": "Activity",
      "@id": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "startTime": "2026-09-24T12:57:44.628413",
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
      "@id": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
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
      "@id": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/select_scene"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_band"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_band_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_band_3"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/reproject_band"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/reproject_band_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:af446720-3625-4794-9126-810a0620808f",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/reproject_band_3"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/calculate_indices"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/estimate_biomass"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/export_stac"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/parse_aoi"
    },
    {
      "@type": "Association",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "agent": "id:f6c152ab-0593-4080-aa4f-1eeb02a954b6"
    },
    {
      "@type": "Association",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/select_scene"
    },
    {
      "@type": "Association",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "agent": "id:4d33da78-bc2b-4f11-927c-55071695661b"
    },
    {
      "@type": "Association",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/download_band"
    },
    {
      "@type": "Association",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "agent": "id:f3cf79d9-5592-4f15-a94b-728004a97650"
    },
    {
      "@type": "Association",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/download_band_2"
    },
    {
      "@type": "Association",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "agent": "id:112f1253-d984-432e-8b9c-f6b600dc0867"
    },
    {
      "@type": "Association",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/download_band_3"
    },
    {
      "@type": "Association",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "agent": "id:0a68208c-621e-48fe-b955-774694ac318c"
    },
    {
      "@type": "Association",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/reproject_band"
    },
    {
      "@type": "Association",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "agent": "id:7dcbf0c1-1cea-4c69-a6a5-252d188398ca"
    },
    {
      "@type": "Association",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/reproject_band_2"
    },
    {
      "@type": "Association",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "agent": "id:7814458d-34a1-43b8-91a4-d47c15a05095"
    },
    {
      "@type": "Association",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/reproject_band_3"
    },
    {
      "@type": "Association",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "agent": "id:936a4bd7-abcd-4bf2-9423-94ae772bd057"
    },
    {
      "@type": "Association",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/calculate_indices"
    },
    {
      "@type": "Association",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "agent": "id:0628dd54-097a-4857-a725-9ce3cd63fc2c"
    },
    {
      "@type": "Association",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/estimate_biomass"
    },
    {
      "@type": "Association",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "agent": "id:e932c1b9-7fde-4dbd-a1af-1b17de8a38de"
    },
    {
      "@type": "Association",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "agent": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "plan": "wf:main/export_stac"
    },
    {
      "@type": "Association",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "agent": "id:114fd6b8-e343-4c8d-b816-20e051ac87a0"
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
          "@value": "wf:main/select_scene",
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
          "@value": "wf:main/download_band",
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
          "@value": "wf:main/estimate_biomass",
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
          "@value": "wf:main/reproject_band",
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
          "@value": "wf:main/export_stac",
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
      "@id": "wf:main",
      "wfdesc:hasSubProcess": [
        {
          "@value": "wf:main/calculate_indices",
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
      "@id": "wf:main/select_scene",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_band",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/estimate_biomass",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/reproject_band",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/export_stac",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/parse_aoi",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/calculate_indices",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:8ea13029-7217-48c6-83b2-5168cf85a135",
      "type": [
        "wfprov:Artifact",
        "prov:Collection",
        "prov:Dictionary"
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:5ac41596-c778-4a85-89d7-230b7e014d7d",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:57d70ea4-3ea9-4fa6-80e3-6504a20bafdc",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0117a745-b852-44ba-a7a0-08e529a7067d",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ab8af93b-6ae4-4bf6-86ac-989a33e53741",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:105cc922-459c-4a99-a431-5d4b3b38aea9",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3a6146e3-99f8-4cdc-aa09-aa71cf40578e",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:57d70ea4-3ea9-4fa6-80e3-6504a20bafdc",
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
          "@value": "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b",
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
      "@id": "id:5ac41596-c778-4a85-89d7-230b7e014d7d",
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
      "@id": "id:3f96db66-4f0b-4af4-9034-8d14f35016b5",
      "value": [
        {
          "@value": "-75.2",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:aabf8f10-1849-4b0c-891f-dd7a04a822a7",
      "value": [
        {
          "@value": "250.5",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:1d5c6165-738d-4f3e-815b-21b08a3876bc",
      "value": [
        {
          "@value": "0.47",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c3c368d8-6ec0-4064-bcfe-a0c6ebea821c",
      "value": [
        {
          "@value": "20",
          "@type": "xsd:int"
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
      "@id": "id:95ff8885-0a15-43aa-82fa-7cd8b1e37f8d",
      "value": [
        {
          "@value": "90",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c8ba466f-bf4e-4bf3-a2cb-e7013b6146cf",
      "value": [
        {
          "@value": "4326",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6dc7f217-6174-4e64-be16-a87833936301",
      "value": [
        {
          "@value": "0.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c66a4eb4-76b6-4a3d-b5ee-aa35009027e1",
      "value": [
        {
          "@value": "0.3",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5fc90b70-355b-4773-ab64-068be1b36cdc",
      "value": [
        {
          "@value": "-0.3",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6f5fd862-1f4d-4a1b-9c03-5f531e769ee6",
      "value": [
        {
          "@value": "0.0001",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:068eb4ce-9e22-4f53-8d00-6a22656436bb",
      "value": [
        {
          "@value": "0.2",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5052a0c49b2beb0515446c40d4eee08c7fcad904",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v1"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:5052a0c49b2beb0515446c40d4eee08c7fcad904",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "https://earth-search.aws.element84.com/v1"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:81daad74-dad7-41e0-bc70-26432d1dfb21",
      "type": [
        "wfprov:Artifact",
        "prov:Collection",
        "prov:Dictionary"
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:d8f4f618-3e0f-4024-a17f-b5c9d24b67b9",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:5356eeb5-2499-42be-bc4e-e8528bde1ff8",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a60dd30c-c4c6-4254-be37-68b96605a358",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:2f66b1e4-39fc-4551-8aa8-49831c3211bb",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c0bace95-d5f7-47c8-85c2-88006db5ab2d",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:dd4db319-ab09-4589-93be-c0ab5a21b781",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:4c4659c5-50da-43e0-8077-7def82bdd204",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d8f4f618-3e0f-4024-a17f-b5c9d24b67b9",
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
          "@value": "id:4c4659c5-50da-43e0-8077-7def82bdd204",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5356eeb5-2499-42be-bc4e-e8528bde1ff8",
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
      "@id": "id:37dc1519-928c-46ff-b08a-8fa656dcede4",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c436c153-ead6-49cd-8341-ee3fc3d94747",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e88dab08-862b-4933-9271-22712490f7bb",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ff077bb5-6a4d-426d-be0c-e1baf185a250",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5d3a2cf8-ee6d-4729-9049-1b13ac82b9c8",
      "value": [
        {
          "@value": "20",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e2d4aa64-8b79-4922-beaa-658f42437197",
      "value": [
        {
          "@value": "90",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:df87d5ba-da6e-432b-b924-80ec05cd6e0b",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e279fef3-8bfb-464b-9df4-3497a11b9735",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d092277a-8801-406a-94ec-078bb314ec37",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d124ea7e-589c-4dd3-9515-031b20191cf3",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b441775de2d148543034d26997c017d3a24544ed",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "scene_item.json"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "scene_item"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:78988010b890ce6f4d2136481f392787ec6d6106",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "red"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d1fc5582-5435-437c-afc6-7bf715e11ac9",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:183be3aa-ca39-47b3-9cb9-9972ab5b4b04",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d81429c0-f7f3-4b1c-b7bb-0dd72a874aff",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:8f1f4d19-7ab7-48f7-a279-0cd0f11d5bb3",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e657235e3d4603e9bbdf1f26c7101ece981f1255",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:7f3077b0-d507-4f90-b1ce-76c822fefb1e",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "red.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "red"
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
      "@id": "id:547c8cdb-eb07-4b2e-bd53-a0e43e839323",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d7eaf21e-997d-440a-9c59-f5def6552d98",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e10c43d5-f616-4774-8ff7-be84cdf977aa",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:50e7a067-7cf5-48cc-a7a9-995f535a42a5",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:73c3313bdf7eed97c6d53d58dd7df2687f3ac1bf",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:cb4e16e3-e34d-4252-820f-27055b12f9f0",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "green.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "green"
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
      "@id": "id:7ad088e7-2b84-406e-a4ef-5e791c3c5457",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3874df5f-5219-46d7-b883-f927b2718f98",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c11e8081-a4e0-43ef-ae32-f37e0aa2b9a7",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e858184a-032a-4649-a114-21e67c56c9b7",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9b8ad0ffede9b72258d46c48d2555b75623aaa2e",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a1526e7f-b483-4350-9c60-e56f786bfff3",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "nir.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "nir"
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
      "@id": "id:e70e9f12-3e5c-4948-9ca6-449d0d53c077",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:aa6dbd65-080e-408b-8c01-0acfe33cc871",
      "value": [
        {
          "@value": "4326",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e8ec687a-b9d1-4afa-83c6-6c3bf9266d3e",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:eff8560e-cd59-4a84-8dac-2f766310d52a",
      "value": [
        {
          "@value": "0.0001",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e56a0493-0204-4306-b246-d6f0a0ed8e0b",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:74367791-176c-4eaf-9ca3-e10883dc4521",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:3f01f1f6a0a77a28c7ffde131fe58339eba52a01",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6ee43ae1-f7f0-44e8-9521-f520ee73f8d5",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "red_4326.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "red_4326"
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
      "@id": "id:faffe676-addb-4b7c-ac15-34a991f69f69",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:87d73316-63b5-4c3d-ba48-d2812d5dd71a",
      "value": [
        {
          "@value": "4326",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c521c30a-5aa8-4fc8-9d25-b8d9de55c870",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6811beb8-4d7f-45b8-9707-e34238fed895",
      "value": [
        {
          "@value": "0.0001",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:61f78ec9-45f1-4537-9ed6-4f4e8616efbf",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6b4a4879-8c4b-4f74-9957-2902ed5cce8e",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:dd6dd1205c33f51e783742f16e856d1752beceda",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:cbcc2c55-1928-47ce-88e9-9cc945faa37e",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "green_4326.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "green_4326"
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
      "@id": "id:e6cc9d7e-080c-437c-a66b-4f386982b118",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ffc8283b-4edf-49e1-bcab-9bd74542ce23",
      "value": [
        {
          "@value": "4326",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:72b6e1b9-31a6-41a5-9509-2fb54eb7a854",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e2de3352-f3cb-41aa-976e-7d0fa8018bcc",
      "value": [
        {
          "@value": "0.0001",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d2cddbd6-1979-4e51-b267-7fec4bab3dc8",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5f1b745b-1648-40c5-8fbe-a8197ea712d1",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9c81f26b42f7f833fea1b35727ffbcc91dab6e3c",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a29b44cd-ed7f-4617-8e76-6b4279377f1d",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "nir_4326.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "nir_4326"
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
      "@id": "id:380f03a1-1d47-401e-b9d6-4e6b30363135",
      "type": [
        "wfprov:Artifact",
        "prov:Collection"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:31cacee3ed40818e05aaa338979596497705bf56",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:da18af81-c62b-42a2-8596-4e773968588d",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "ndvi.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "ndvi"
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
      "@id": "data:938fb14bf0a2470ab2ae9b0420a64e5b81671271",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:4a3cec45-e5c9-449f-b623-e71818c12362",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "ndwi.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "ndwi"
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
      "@id": "data:d1a501118882d0e474e5342dbf965ace5b931cca",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:87573e08-1a69-4a83-a551-f2a1c560cc7c",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "savi.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "savi"
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
      "@id": "id:54cd6275-9321-44c8-856b-5978bcb26eae",
      "value": [
        {
          "@value": "-75.2",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d9c2f532-47b2-45e7-9825-ed5413dea033",
      "value": [
        {
          "@value": "250.5",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:14e98d45-e476-4164-bcdd-e4822839bf51",
      "value": [
        {
          "@value": "0.47",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3ba979c6-c4b1-4d94-bd53-556aca41e518",
      "value": [
        {
          "@value": "0.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:32255a12-525c-491e-bf2f-f579c17fdf39",
      "value": [
        {
          "@value": "0.3",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:10db2d8a-f421-4312-aef9-6c5efbad211d",
      "value": [
        {
          "@value": "-0.3",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:f5beff83-d577-48b1-b086-b1a35ed1b44b",
      "value": [
        {
          "@value": "0.2",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:7f0e99772494c2b7c3755662f3725e91b7991785",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:924dc3e6-e45e-4ae0-940f-d538dce7a6e4",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "analysis_summary.json"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "analysis_summary"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:2b8178722e8bb6fbc41909e7e32e88d4aa439eb8",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:2b8178722e8bb6fbc41909e7e32e88d4aa439eb8",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:bc49aa46-3931-4344-8b1e-7788b5f50e0f",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "biomass.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "biomass"
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
      "@id": "data:4451dd50c71fb43e9f78bbe62b52f4d6349624a8",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:4451dd50c71fb43e9f78bbe62b52f4d6349624a8",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3659eb06-f1ed-4ec3-8ccd-74774fdae9ac",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "biomass_summary.csv"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "biomass_summary"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".csv"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:661fc93f43cc808586d1ba6bf1b9e22a963ce449",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:661fc93f43cc808586d1ba6bf1b9e22a963ce449",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:9c4478e2-935b-41d5-857b-c2641d1c917d",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "carbon_summary.csv"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "carbon_summary"
        }
      ],
      "cwlprov:nameext": [
        {
          "@value": ".csv"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:443e27d9b969edf33b0080e08bc8bffe154f06f9",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:443e27d9b969edf33b0080e08bc8bffe154f06f9",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:d9517d0d-9e97-4d22-afa7-a402d0537cf6",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "mangrove_mask.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "mangrove_mask"
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
      "@id": "id:dc91669b-4a2f-4bd1-92c9-382337d78dba",
      "value": [
        {
          "@value": "95.35",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6818485a-eeb1-4ded-8202-995389ee3c9e",
      "value": [
        {
          "@value": "16.1",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:c5451c9d-b6ce-42de-b9a3-9512e9784e73",
      "value": [
        {
          "@value": "15.9",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:37378d08-0575-4061-9f35-0bd44e06d360",
      "value": [
        {
          "@value": "95.15",
          "@type": "xsd:double"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
      "type": [
        "wfprov:Artifact",
        "prov:Collection",
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
          "@value": "metadata:directory-2363b376-af39-4421-ac82-298f9b5bf5d6.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:dcb23f91-1dbc-4929-9021-d23ee962fc04",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:758a05e3-6c7f-41d7-af5a-b4798d4b882f",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:943b0707a0f1a109dd1de1d61e37a1654a191ae9",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:f70266c8-9af3-4228-89f4-230a39e31c83",
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
      "@id": "id:dcb23f91-1dbc-4929-9021-d23ee962fc04",
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
          "@value": "id:f70266c8-9af3-4228-89f4-230a39e31c83",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "type": [
        "wfprov:Artifact",
        "prov:Collection",
        "prov:Dictionary",
        "ro:Folder"
      ],
      "cwlprov:basename": [
        {
          "@value": "mangrove-analysis-20260924-105955"
        }
      ],
      "ore:isDescribedBy": [
        {
          "@value": "metadata:directory-03305ae1-bded-486a-bfd3-b2f244261014.ttl",
          "@type": "xsd:QName"
        }
      ],
      "prov:hadDictionaryMember": [
        {
          "@value": "id:eeb1bf4b-58a7-41c1-b269-d3320e3156e8",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:416a29f6-ecc2-420e-8f48-4d5bce2c3263",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:827caa38-b109-46f9-be8f-4bc99371b11f",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:4640e02b-c74b-40e1-a818-75d60264864b",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:2adedd6a-e764-47f5-82f0-d38efb1e074a",
          "@type": "xsd:QName"
        },
        {
          "@value": "id:0fea0e08-9d5a-41e3-8889-fcd05025f7f7",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "biomass.tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:eeb1bf4b-58a7-41c1-b269-d3320e3156e8",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "biomass.tif"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:7238dd3cfee022d8d78263cad6a90a7ed0b1c31a",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:2125c168-2391-4a9c-924c-8d5d7330ffd5",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "mangrove-analysis-20260924-105955.json"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0fea0e08-9d5a-41e3-8889-fcd05025f7f7",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "mangrove-analysis-20260924-105955.json"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:2125c168-2391-4a9c-924c-8d5d7330ffd5",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3a808b83-4512-4301-9193-fe5620d0ece5",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "carbon_summary.csv"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:4640e02b-c74b-40e1-a818-75d60264864b",
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
          "@value": "id:3a808b83-4512-4301-9193-fe5620d0ece5",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:8982a81b-193e-4e8f-bacf-43df0bb2e832",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "biomass_summary.csv"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:416a29f6-ecc2-420e-8f48-4d5bce2c3263",
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
          "@value": "id:8982a81b-193e-4e8f-bacf-43df0bb2e832",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "mangrove_mask.tif"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:827caa38-b109-46f9-be8f-4bc99371b11f",
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
          "@value": "id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:0ff4ea33ebd17218fd87cba84943c04e4e56137f",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec",
      "type": [
        "wfprov:Artifact",
        "wf4ever:File"
      ],
      "cwlprov:basename": [
        {
          "@value": "biomass_quicklook.png"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:2adedd6a-e764-47f5-82f0-d38efb1e074a",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "biomass_quicklook.png"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:758a05e3-6c7f-41d7-af5a-b4798d4b882f",
      "type": [
        "prov:KeyEntityPair"
      ],
      "prov:pairKey": [
        {
          "@value": "mangrove-analysis-20260924-105955"
        }
      ],
      "prov:pairEntity": [
        {
          "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Membership",
      "collection": "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b",
      "entity": "id:0117a745-b852-44ba-a7a0-08e529a7067d"
    },
    {
      "@type": "Membership",
      "collection": "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b",
      "entity": "id:ab8af93b-6ae4-4bf6-86ac-989a33e53741"
    },
    {
      "@type": "Membership",
      "collection": "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b",
      "entity": "id:105cc922-459c-4a99-a431-5d4b3b38aea9"
    },
    {
      "@type": "Membership",
      "collection": "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b",
      "entity": "id:3a6146e3-99f8-4cdc-aa09-aa71cf40578e"
    },
    {
      "@type": "Membership",
      "collection": "id:8ea13029-7217-48c6-83b2-5168cf85a135",
      "entity": "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b"
    },
    {
      "@type": "Membership",
      "collection": "id:8ea13029-7217-48c6-83b2-5168cf85a135",
      "entity": "data:09b42388eb37be1a4b972127a78f691ec6eb3795"
    },
    {
      "@type": "Membership",
      "collection": "id:4c4659c5-50da-43e0-8077-7def82bdd204",
      "entity": "id:a60dd30c-c4c6-4254-be37-68b96605a358"
    },
    {
      "@type": "Membership",
      "collection": "id:4c4659c5-50da-43e0-8077-7def82bdd204",
      "entity": "id:2f66b1e4-39fc-4551-8aa8-49831c3211bb"
    },
    {
      "@type": "Membership",
      "collection": "id:4c4659c5-50da-43e0-8077-7def82bdd204",
      "entity": "id:c0bace95-d5f7-47c8-85c2-88006db5ab2d"
    },
    {
      "@type": "Membership",
      "collection": "id:4c4659c5-50da-43e0-8077-7def82bdd204",
      "entity": "id:dd4db319-ab09-4589-93be-c0ab5a21b781"
    },
    {
      "@type": "Membership",
      "collection": "id:81daad74-dad7-41e0-bc70-26432d1dfb21",
      "entity": "id:4c4659c5-50da-43e0-8077-7def82bdd204"
    },
    {
      "@type": "Membership",
      "collection": "id:81daad74-dad7-41e0-bc70-26432d1dfb21",
      "entity": "data:09b42388eb37be1a4b972127a78f691ec6eb3795"
    },
    {
      "@type": "Membership",
      "collection": "id:380f03a1-1d47-401e-b9d6-4e6b30363135",
      "entity": "id:6ee43ae1-f7f0-44e8-9521-f520ee73f8d5"
    },
    {
      "@type": "Membership",
      "collection": "id:380f03a1-1d47-401e-b9d6-4e6b30363135",
      "entity": "id:cbcc2c55-1928-47ce-88e9-9cc945faa37e"
    },
    {
      "@type": "Membership",
      "collection": "id:380f03a1-1d47-401e-b9d6-4e6b30363135",
      "entity": "id:a29b44cd-ed7f-4617-8e76-6b4279377f1d"
    },
    {
      "@type": "Membership",
      "collection": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
      "entity": "id:f70266c8-9af3-4228-89f4-230a39e31c83"
    },
    {
      "@type": "Membership",
      "collection": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "entity": "id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0"
    },
    {
      "@type": "Membership",
      "collection": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "entity": "id:2125c168-2391-4a9c-924c-8d5d7330ffd5"
    },
    {
      "@type": "Membership",
      "collection": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "entity": "id:3a808b83-4512-4301-9193-fe5620d0ece5"
    },
    {
      "@type": "Membership",
      "collection": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "entity": "id:8982a81b-193e-4e8f-bacf-43df0bb2e832"
    },
    {
      "@type": "Membership",
      "collection": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "entity": "id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149"
    },
    {
      "@type": "Membership",
      "collection": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "entity": "id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec"
    },
    {
      "@type": "Membership",
      "collection": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
      "entity": "id:03305ae1-bded-486a-bfd3-b2f244261014"
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:8ea13029-7217-48c6-83b2-5168cf85a135",
      "time": "2026-09-24T12:57:45.244804",
      "role": [
        "wf:main/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:3f96db66-4f0b-4af4-9034-8d14f35016b5",
      "time": "2026-09-24T12:57:45.244872",
      "role": [
        "wf:main/biomass_intercept"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:aabf8f10-1849-4b0c-891f-dd7a04a822a7",
      "time": "2026-09-24T12:57:45.244914",
      "role": [
        "wf:main/biomass_slope"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:1d5c6165-738d-4f3e-815b-21b08a3876bc",
      "time": "2026-09-24T12:57:45.244950",
      "role": [
        "wf:main/carbon_fraction"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:c3c368d8-6ec0-4064-bcfe-a0c6ebea821c",
      "time": "2026-09-24T12:57:45.244986",
      "role": [
        "wf:main/cloud_cover_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "data:4c89b83017b6bf2fdefdc95f52a039255235ba37",
      "time": "2026-09-24T12:57:45.245944",
      "role": [
        "wf:main/collection"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:95ff8885-0a15-43aa-82fa-7cd8b1e37f8d",
      "time": "2026-09-24T12:57:45.246023",
      "role": [
        "wf:main/days_back"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:c8ba466f-bf4e-4bf3-a2cb-e7013b6146cf",
      "time": "2026-09-24T12:57:45.246066",
      "role": [
        "wf:main/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:6dc7f217-6174-4e64-be16-a87833936301",
      "time": "2026-09-24T12:57:45.246104",
      "role": [
        "wf:main/ndvi_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:c66a4eb4-76b6-4a3d-b5ee-aa35009027e1",
      "time": "2026-09-24T12:57:45.246141",
      "role": [
        "wf:main/ndvi_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:5fc90b70-355b-4773-ab64-068be1b36cdc",
      "time": "2026-09-24T12:57:45.246177",
      "role": [
        "wf:main/ndwi_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:6f5fd862-1f4d-4a1b-9c03-5f531e769ee6",
      "time": "2026-09-24T12:57:45.246218",
      "role": [
        "wf:main/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "id:068eb4ce-9e22-4f53-8d00-6a22656436bb",
      "time": "2026-09-24T12:57:45.246255",
      "role": [
        "wf:main/savi_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "entity": "data:5052a0c49b2beb0515446c40d4eee08c7fcad904",
      "time": "2026-09-24T12:57:45.247187",
      "role": [
        "wf:main/stac_api"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "entity": "id:81daad74-dad7-41e0-bc70-26432d1dfb21",
      "time": "2026-09-24T12:57:45.385435",
      "role": [
        "wf:main/parse_aoi/aoi"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "id:5d3a2cf8-ee6d-4729-9049-1b13ac82b9c8",
      "time": "2026-09-24T12:57:48.577808",
      "role": [
        "wf:main/select_scene/cloud_cover_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "data:4c89b83017b6bf2fdefdc95f52a039255235ba37",
      "time": "2026-09-24T12:57:48.578733",
      "role": [
        "wf:main/select_scene/collection"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "id:e2d4aa64-8b79-4922-beaa-658f42437197",
      "time": "2026-09-24T12:57:48.578791",
      "role": [
        "wf:main/select_scene/days_back"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "id:df87d5ba-da6e-432b-b924-80ec05cd6e0b",
      "time": "2026-09-24T12:57:48.578840",
      "role": [
        "wf:main/select_scene/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "id:e279fef3-8bfb-464b-9df4-3497a11b9735",
      "time": "2026-09-24T12:57:48.579301",
      "role": [
        "wf:main/select_scene/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "id:d092277a-8801-406a-94ec-078bb314ec37",
      "time": "2026-09-24T12:57:48.579345",
      "role": [
        "wf:main/select_scene/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "data:5052a0c49b2beb0515446c40d4eee08c7fcad904",
      "time": "2026-09-24T12:57:48.579889",
      "role": [
        "wf:main/select_scene/stac_api"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "entity": "id:d124ea7e-589c-4dd3-9515-031b20191cf3",
      "time": "2026-09-24T12:57:48.579935",
      "role": [
        "wf:main/select_scene/west"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "entity": "data:78988010b890ce6f4d2136481f392787ec6d6106",
      "time": "2026-09-24T12:58:01.588345",
      "role": [
        "wf:main/download_band/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "entity": "id:d1fc5582-5435-437c-afc6-7bf715e11ac9",
      "time": "2026-09-24T12:58:01.588501",
      "role": [
        "wf:main/download_band/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "entity": "id:183be3aa-ca39-47b3-9cb9-9972ab5b4b04",
      "time": "2026-09-24T12:58:01.588559",
      "role": [
        "wf:main/download_band/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "entity": "id:d81429c0-f7f3-4b1c-b7bb-0dd72a874aff",
      "time": "2026-09-24T12:58:01.588601",
      "role": [
        "wf:main/download_band/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "entity": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "time": "2026-09-24T12:58:01.588654",
      "role": [
        "wf:main/download_band/stac_item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "entity": "id:8f1f4d19-7ab7-48f7-a279-0cd0f11d5bb3",
      "time": "2026-09-24T12:58:01.588695",
      "role": [
        "wf:main/download_band/west"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "entity": "data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c",
      "time": "2026-09-24T12:58:16.268376",
      "role": [
        "wf:main/download_band_2/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "entity": "id:547c8cdb-eb07-4b2e-bd53-a0e43e839323",
      "time": "2026-09-24T12:58:16.268610",
      "role": [
        "wf:main/download_band_2/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "entity": "id:d7eaf21e-997d-440a-9c59-f5def6552d98",
      "time": "2026-09-24T12:58:16.268667",
      "role": [
        "wf:main/download_band_2/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "entity": "id:e10c43d5-f616-4774-8ff7-be84cdf977aa",
      "time": "2026-09-24T12:58:16.268706",
      "role": [
        "wf:main/download_band_2/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "entity": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "time": "2026-09-24T12:58:16.268791",
      "role": [
        "wf:main/download_band_2/stac_item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "entity": "id:50e7a067-7cf5-48cc-a7a9-995f535a42a5",
      "time": "2026-09-24T12:58:16.268833",
      "role": [
        "wf:main/download_band_2/west"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "entity": "data:ba936cb0e062bea4078e8b56371ca8fe054093dd",
      "time": "2026-09-24T12:58:36.200068",
      "role": [
        "wf:main/download_band_3/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "entity": "id:7ad088e7-2b84-406e-a4ef-5e791c3c5457",
      "time": "2026-09-24T12:58:36.200263",
      "role": [
        "wf:main/download_band_3/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "entity": "id:3874df5f-5219-46d7-b883-f927b2718f98",
      "time": "2026-09-24T12:58:36.200318",
      "role": [
        "wf:main/download_band_3/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "entity": "id:c11e8081-a4e0-43ef-ae32-f37e0aa2b9a7",
      "time": "2026-09-24T12:58:36.200371",
      "role": [
        "wf:main/download_band_3/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "entity": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "time": "2026-09-24T12:58:36.200427",
      "role": [
        "wf:main/download_band_3/stac_item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "entity": "id:e858184a-032a-4649-a114-21e67c56c9b7",
      "time": "2026-09-24T12:58:36.200466",
      "role": [
        "wf:main/download_band_3/west"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "entity": "id:7f3077b0-d507-4f90-b1ce-76c822fefb1e",
      "time": "2026-09-24T12:59:12.290487",
      "role": [
        "wf:main/reproject_band/band_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "entity": "id:e70e9f12-3e5c-4948-9ca6-449d0d53c077",
      "time": "2026-09-24T12:59:12.290654",
      "role": [
        "wf:main/reproject_band/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "entity": "id:aa6dbd65-080e-408b-8c01-0acfe33cc871",
      "time": "2026-09-24T12:59:12.290700",
      "role": [
        "wf:main/reproject_band/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "entity": "id:e8ec687a-b9d1-4afa-83c6-6c3bf9266d3e",
      "time": "2026-09-24T12:59:12.290735",
      "role": [
        "wf:main/reproject_band/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "entity": "id:eff8560e-cd59-4a84-8dac-2f766310d52a",
      "time": "2026-09-24T12:59:12.290768",
      "role": [
        "wf:main/reproject_band/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "entity": "id:e56a0493-0204-4306-b246-d6f0a0ed8e0b",
      "time": "2026-09-24T12:59:12.290800",
      "role": [
        "wf:main/reproject_band/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "entity": "id:74367791-176c-4eaf-9ca3-e10883dc4521",
      "time": "2026-09-24T12:59:12.290832",
      "role": [
        "wf:main/reproject_band/west"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "entity": "id:cb4e16e3-e34d-4252-820f-27055b12f9f0",
      "time": "2026-09-24T12:59:18.368809",
      "role": [
        "wf:main/reproject_band_2/band_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "entity": "id:faffe676-addb-4b7c-ac15-34a991f69f69",
      "time": "2026-09-24T12:59:18.368961",
      "role": [
        "wf:main/reproject_band_2/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "entity": "id:87d73316-63b5-4c3d-ba48-d2812d5dd71a",
      "time": "2026-09-24T12:59:18.369015",
      "role": [
        "wf:main/reproject_band_2/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "entity": "id:c521c30a-5aa8-4fc8-9d25-b8d9de55c870",
      "time": "2026-09-24T12:59:18.369051",
      "role": [
        "wf:main/reproject_band_2/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "entity": "id:6811beb8-4d7f-45b8-9707-e34238fed895",
      "time": "2026-09-24T12:59:18.369083",
      "role": [
        "wf:main/reproject_band_2/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "entity": "id:61f78ec9-45f1-4537-9ed6-4f4e8616efbf",
      "time": "2026-09-24T12:59:18.369114",
      "role": [
        "wf:main/reproject_band_2/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "entity": "id:6b4a4879-8c4b-4f74-9957-2902ed5cce8e",
      "time": "2026-09-24T12:59:18.369145",
      "role": [
        "wf:main/reproject_band_2/west"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "entity": "id:a1526e7f-b483-4350-9c60-e56f786bfff3",
      "time": "2026-09-24T12:59:25.509369",
      "role": [
        "wf:main/reproject_band_3/band_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "entity": "id:e6cc9d7e-080c-437c-a66b-4f386982b118",
      "time": "2026-09-24T12:59:25.509555",
      "role": [
        "wf:main/reproject_band_3/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "entity": "id:ffc8283b-4edf-49e1-bcab-9bd74542ce23",
      "time": "2026-09-24T12:59:25.509607",
      "role": [
        "wf:main/reproject_band_3/epsg"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "entity": "id:72b6e1b9-31a6-41a5-9509-2fb54eb7a854",
      "time": "2026-09-24T12:59:25.509646",
      "role": [
        "wf:main/reproject_band_3/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "entity": "id:e2de3352-f3cb-41aa-976e-7d0fa8018bcc",
      "time": "2026-09-24T12:59:25.509686",
      "role": [
        "wf:main/reproject_band_3/resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "entity": "id:d2cddbd6-1979-4e51-b267-7fec4bab3dc8",
      "time": "2026-09-24T12:59:25.509728",
      "role": [
        "wf:main/reproject_band_3/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "entity": "id:5f1b745b-1648-40c5-8fbe-a8197ea712d1",
      "time": "2026-09-24T12:59:25.509771",
      "role": [
        "wf:main/reproject_band_3/west"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "entity": "id:380f03a1-1d47-401e-b9d6-4e6b30363135",
      "time": "2026-09-24T12:59:32.637646",
      "role": [
        "wf:main/calculate_indices/band_files"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:54cd6275-9321-44c8-856b-5978bcb26eae",
      "time": "2026-09-24T12:59:40.534079",
      "role": [
        "wf:main/estimate_biomass/biomass_intercept"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:d9c2f532-47b2-45e7-9825-ed5413dea033",
      "time": "2026-09-24T12:59:40.534147",
      "role": [
        "wf:main/estimate_biomass/biomass_slope"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:14e98d45-e476-4164-bcdd-e4822839bf51",
      "time": "2026-09-24T12:59:40.534185",
      "role": [
        "wf:main/estimate_biomass/carbon_fraction"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:da18af81-c62b-42a2-8596-4e773968588d",
      "time": "2026-09-24T12:59:40.534219",
      "role": [
        "wf:main/estimate_biomass/ndvi_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:3ba979c6-c4b1-4d94-bd53-556aca41e518",
      "time": "2026-09-24T12:59:40.534255",
      "role": [
        "wf:main/estimate_biomass/ndvi_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:32255a12-525c-491e-bf2f-f579c17fdf39",
      "time": "2026-09-24T12:59:40.534286",
      "role": [
        "wf:main/estimate_biomass/ndvi_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:4a3cec45-e5c9-449f-b623-e71818c12362",
      "time": "2026-09-24T12:59:40.534311",
      "role": [
        "wf:main/estimate_biomass/ndwi_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:10db2d8a-f421-4312-aef9-6c5efbad211d",
      "time": "2026-09-24T12:59:40.534343",
      "role": [
        "wf:main/estimate_biomass/ndwi_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:87573e08-1a69-4a83-a551-f2a1c560cc7c",
      "time": "2026-09-24T12:59:40.534371",
      "role": [
        "wf:main/estimate_biomass/savi_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:f5beff83-d577-48b1-b086-b1a35ed1b44b",
      "time": "2026-09-24T12:59:40.534404",
      "role": [
        "wf:main/estimate_biomass/savi_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "entity": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "time": "2026-09-24T12:59:40.534428",
      "role": [
        "wf:main/estimate_biomass/stac_item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:924dc3e6-e45e-4ae0-940f-d538dce7a6e4",
      "time": "2026-09-24T12:59:47.691973",
      "role": [
        "wf:main/export_stac/analysis_summary_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:bc49aa46-3931-4344-8b1e-7788b5f50e0f",
      "time": "2026-09-24T12:59:47.692088",
      "role": [
        "wf:main/export_stac/biomass_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:3659eb06-f1ed-4ec3-8ccd-74774fdae9ac",
      "time": "2026-09-24T12:59:47.692122",
      "role": [
        "wf:main/export_stac/biomass_summary_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:9c4478e2-935b-41d5-857b-c2641d1c917d",
      "time": "2026-09-24T12:59:47.692148",
      "role": [
        "wf:main/export_stac/carbon_summary_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:dc91669b-4a2f-4bd1-92c9-382337d78dba",
      "time": "2026-09-24T12:59:47.692292",
      "role": [
        "wf:main/export_stac/east"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:d9517d0d-9e97-4d22-afa7-a402d0537cf6",
      "time": "2026-09-24T12:59:47.692318",
      "role": [
        "wf:main/export_stac/mangrove_mask_file"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:6818485a-eeb1-4ded-8202-995389ee3c9e",
      "time": "2026-09-24T12:59:47.692360",
      "role": [
        "wf:main/export_stac/north"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:c5451c9d-b6ce-42de-b9a3-9512e9784e73",
      "time": "2026-09-24T12:59:47.692412",
      "role": [
        "wf:main/export_stac/south"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "time": "2026-09-24T12:59:47.692457",
      "role": [
        "wf:main/export_stac/stac_item"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "entity": "id:37378d08-0575-4061-9f35-0bd44e06d360",
      "time": "2026-09-24T12:59:47.692513",
      "role": [
        "wf:main/export_stac/west"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:37dc1519-928c-46ff-b08a-8fa656dcede4",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "time": "2026-09-24T12:57:48.476740",
      "role": [
        "wf:main/parse_aoi/east"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:c436c153-ead6-49cd-8341-ee3fc3d94747",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "time": "2026-09-24T12:57:48.476740",
      "role": [
        "wf:main/parse_aoi/north"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:e88dab08-862b-4933-9271-22712490f7bb",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "time": "2026-09-24T12:57:48.476740",
      "role": [
        "wf:main/parse_aoi/south"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:ff077bb5-6a4d-426d-be0c-e1baf185a250",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "time": "2026-09-24T12:57:48.476740",
      "role": [
        "wf:main/parse_aoi/west"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "time": "2026-09-24T12:58:01.337315",
      "role": [
        "wf:main/select_scene/stac_item"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:7f3077b0-d507-4f90-b1ce-76c822fefb1e",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "time": "2026-09-24T12:58:16.231617",
      "role": [
        "wf:main/download_band/band_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:cb4e16e3-e34d-4252-820f-27055b12f9f0",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "time": "2026-09-24T12:58:36.167096",
      "role": [
        "wf:main/download_band_2/band_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a1526e7f-b483-4350-9c60-e56f786bfff3",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "time": "2026-09-24T12:59:12.183023",
      "role": [
        "wf:main/download_band_3/band_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6ee43ae1-f7f0-44e8-9521-f520ee73f8d5",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "time": "2026-09-24T12:59:18.344902",
      "role": [
        "wf:main/reproject_band/reprojected_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:cbcc2c55-1928-47ce-88e9-9cc945faa37e",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "time": "2026-09-24T12:59:25.470134",
      "role": [
        "wf:main/reproject_band_2/reprojected_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a29b44cd-ed7f-4617-8e76-6b4279377f1d",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "time": "2026-09-24T12:59:32.420687",
      "role": [
        "wf:main/reproject_band_3/reprojected_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:da18af81-c62b-42a2-8596-4e773968588d",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "time": "2026-09-24T12:59:40.382890",
      "role": [
        "wf:main/calculate_indices/ndvi_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:4a3cec45-e5c9-449f-b623-e71818c12362",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "time": "2026-09-24T12:59:40.382890",
      "role": [
        "wf:main/calculate_indices/ndwi_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:87573e08-1a69-4a83-a551-f2a1c560cc7c",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "time": "2026-09-24T12:59:40.382890",
      "role": [
        "wf:main/calculate_indices/savi_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:924dc3e6-e45e-4ae0-940f-d538dce7a6e4",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "time": "2026-09-24T12:59:47.581661",
      "role": [
        "wf:main/estimate_biomass/analysis_summary_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:bc49aa46-3931-4344-8b1e-7788b5f50e0f",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "time": "2026-09-24T12:59:47.581661",
      "role": [
        "wf:main/estimate_biomass/biomass_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:3659eb06-f1ed-4ec3-8ccd-74774fdae9ac",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "time": "2026-09-24T12:59:47.581661",
      "role": [
        "wf:main/estimate_biomass/biomass_summary_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:9c4478e2-935b-41d5-857b-c2641d1c917d",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "time": "2026-09-24T12:59:47.581661",
      "role": [
        "wf:main/estimate_biomass/carbon_summary_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d9517d0d-9e97-4d22-afa7-a402d0537cf6",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "time": "2026-09-24T12:59:47.581661",
      "role": [
        "wf:main/estimate_biomass/mangrove_mask_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "time": "2026-09-24T12:59:58.100038",
      "role": [
        "wf:main/export_stac/stac_catalog"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:58.171647",
      "role": [
        "wf:main/primary/stac"
      ]
    },
    {
      "@type": "End",
      "activity": "id:931b869b-928e-447a-bf72-bc6914cb5e33",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:57:48.476728"
    },
    {
      "@type": "End",
      "activity": "id:effb40f4-0a75-4498-80d7-d04365cf463b",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:58:01.337237"
    },
    {
      "@type": "End",
      "activity": "id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:58:16.231585"
    },
    {
      "@type": "End",
      "activity": "id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:58:36.167066"
    },
    {
      "@type": "End",
      "activity": "id:ad22cfb2-89d1-476b-a33a-73bf3be4c782",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:12.183003"
    },
    {
      "@type": "End",
      "activity": "id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:18.344891"
    },
    {
      "@type": "End",
      "activity": "id:f4cf1f0f-6d62-483b-ba92-38d6e1040135",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:25.470107"
    },
    {
      "@type": "End",
      "activity": "id:af446720-3625-4794-9126-810a0620808f",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:32.420671"
    },
    {
      "@type": "End",
      "activity": "id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:40.382878"
    },
    {
      "@type": "End",
      "activity": "id:376997e3-8d83-426b-b84f-e985b2af4046",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:47.581645"
    },
    {
      "@type": "End",
      "activity": "id:c16504e6-ec23-43da-92c9-c00151a037f2",
      "ender": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "time": "2026-09-24T12:59:58.100015"
    },
    {
      "@type": "End",
      "activity": "id:e96466cd-dd6c-469a-af95-6bbc439a3156",
      "ender": "id:1432f81c-9552-435f-a0ab-6b28e12ea1b3",
      "time": "2026-09-24T12:59:58.171742"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:db33c88c-4dd2-4ea1-b06b-577175d50413",
      "generalEntity": "data:b441775de2d148543034d26997c017d3a24544ed"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:7f3077b0-d507-4f90-b1ce-76c822fefb1e",
      "generalEntity": "data:e657235e3d4603e9bbdf1f26c7101ece981f1255"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:cb4e16e3-e34d-4252-820f-27055b12f9f0",
      "generalEntity": "data:73c3313bdf7eed97c6d53d58dd7df2687f3ac1bf"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:a1526e7f-b483-4350-9c60-e56f786bfff3",
      "generalEntity": "data:9b8ad0ffede9b72258d46c48d2555b75623aaa2e"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:6ee43ae1-f7f0-44e8-9521-f520ee73f8d5",
      "generalEntity": "data:3f01f1f6a0a77a28c7ffde131fe58339eba52a01"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:cbcc2c55-1928-47ce-88e9-9cc945faa37e",
      "generalEntity": "data:dd6dd1205c33f51e783742f16e856d1752beceda"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:a29b44cd-ed7f-4617-8e76-6b4279377f1d",
      "generalEntity": "data:9c81f26b42f7f833fea1b35727ffbcc91dab6e3c"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:da18af81-c62b-42a2-8596-4e773968588d",
      "generalEntity": "data:31cacee3ed40818e05aaa338979596497705bf56"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:4a3cec45-e5c9-449f-b623-e71818c12362",
      "generalEntity": "data:938fb14bf0a2470ab2ae9b0420a64e5b81671271"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:87573e08-1a69-4a83-a551-f2a1c560cc7c",
      "generalEntity": "data:d1a501118882d0e474e5342dbf965ace5b931cca"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:924dc3e6-e45e-4ae0-940f-d538dce7a6e4",
      "generalEntity": "data:7f0e99772494c2b7c3755662f3725e91b7991785"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:bc49aa46-3931-4344-8b1e-7788b5f50e0f",
      "generalEntity": "data:2b8178722e8bb6fbc41909e7e32e88d4aa439eb8"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3659eb06-f1ed-4ec3-8ccd-74774fdae9ac",
      "generalEntity": "data:4451dd50c71fb43e9f78bbe62b52f4d6349624a8"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:9c4478e2-935b-41d5-857b-c2641d1c917d",
      "generalEntity": "data:661fc93f43cc808586d1ba6bf1b9e22a963ce449"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:d9517d0d-9e97-4d22-afa7-a402d0537cf6",
      "generalEntity": "data:443e27d9b969edf33b0080e08bc8bffe154f06f9"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:f70266c8-9af3-4228-89f4-230a39e31c83",
      "generalEntity": "data:943b0707a0f1a109dd1de1d61e37a1654a191ae9"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0",
      "generalEntity": "data:2b8178722e8bb6fbc41909e7e32e88d4aa439eb8"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:2125c168-2391-4a9c-924c-8d5d7330ffd5",
      "generalEntity": "data:7238dd3cfee022d8d78263cad6a90a7ed0b1c31a"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3a808b83-4512-4301-9193-fe5620d0ece5",
      "generalEntity": "data:661fc93f43cc808586d1ba6bf1b9e22a963ce449"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:8982a81b-193e-4e8f-bacf-43df0bb2e832",
      "generalEntity": "data:4451dd50c71fb43e9f78bbe62b52f4d6349624a8"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149",
      "generalEntity": "data:443e27d9b969edf33b0080e08bc8bffe154f06f9"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec",
      "generalEntity": "data:0ff4ea33ebd17218fd87cba84943c04e4e56137f"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:2363b376-af39-4421-ac82-298f9b5bf5d6#ore",
      "generalEntity": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-2363b376-af39-4421-ac82-298f9b5bf5d6.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:03305ae1-bded-486a-bfd3-b2f244261014#ore",
      "generalEntity": "id:03305ae1-bded-486a-bfd3-b2f244261014",
      "prov:asInBundle": [
        {
          "@value": "metadata:directory-03305ae1-bded-486a-bfd3-b2f244261014.ttl",
          "@type": "xsd:QName"
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-2363b376-af39-4421-ac82-298f9b5bf5d6.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
          "type": [
            "ro:Folder",
            "ore:Aggregation"
          ],
          "ore:aggregates": [
            {
              "@value": "id:dcb23f91-1dbc-4929-9021-d23ee962fc04",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:758a05e3-6c7f-41d7-af5a-b4798d4b882f",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:dcb23f91-1dbc-4929-9021-d23ee962fc04",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "catalog.json"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:f70266c8-9af3-4228-89f4-230a39e31c83",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:758a05e3-6c7f-41d7-af5a-b4798d4b882f",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "mangrove-analysis-20260924-105955"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:2363b376-af39-4421-ac82-298f9b5bf5d6",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
              "@type": "xsd:QName"
            }
          ]
        }
      ]
    },
    {
      "@type": "Bundle",
      "@id": "metadata:directory-03305ae1-bded-486a-bfd3-b2f244261014.ttl",
      "@context": [
        {
          "ro": "http://purl.org/wf4ever/ro#",
          "ore": "http://www.openarchives.org/ore/terms/",
          "id": "urn:uuid:",
          "metadata": "arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/metadata/"
        }
      ],
      "@graph": [
        {
          "@type": "Entity",
          "@id": "id:03305ae1-bded-486a-bfd3-b2f244261014",
          "type": [
            "ro:Folder",
            "ore:Aggregation"
          ],
          "ore:aggregates": [
            {
              "@value": "id:eeb1bf4b-58a7-41c1-b269-d3320e3156e8",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:416a29f6-ecc2-420e-8f48-4d5bce2c3263",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:827caa38-b109-46f9-be8f-4bc99371b11f",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:4640e02b-c74b-40e1-a818-75d60264864b",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:2adedd6a-e764-47f5-82f0-d38efb1e074a",
              "@type": "xsd:QName"
            },
            {
              "@value": "id:0fea0e08-9d5a-41e3-8889-fcd05025f7f7",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:eeb1bf4b-58a7-41c1-b269-d3320e3156e8",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "biomass.tif"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:0fea0e08-9d5a-41e3-8889-fcd05025f7f7",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "mangrove-analysis-20260924-105955.json"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:2125c168-2391-4a9c-924c-8d5d7330ffd5",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:4640e02b-c74b-40e1-a818-75d60264864b",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "carbon_summary.csv"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:3a808b83-4512-4301-9193-fe5620d0ece5",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:416a29f6-ecc2-420e-8f48-4d5bce2c3263",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "biomass_summary.csv"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:8982a81b-193e-4e8f-bacf-43df0bb2e832",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:827caa38-b109-46f9-be8f-4bc99371b11f",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "mangrove_mask.tif"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149",
              "@type": "xsd:QName"
            }
          ]
        },
        {
          "@type": "Entity",
          "@id": "id:2adedd6a-e764-47f5-82f0-d38efb1e074a",
          "type": [
            "ro:FolderEntry",
            "ore:Proxy"
          ],
          "ro:entryName": [
            {
              "@value": "biomass_quicklook.png"
            }
          ],
          "ore:proxyIn": [
            {
              "@value": "id:03305ae1-bded-486a-bfd3-b2f244261014",
              "@type": "xsd:QName"
            }
          ],
          "ore:proxyFor": [
            {
              "@value": "id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec",
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
@prefix metadata: <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/metadata/> .
@prefix ore: <http://www.openarchives.org/ore/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix provext: <https://openprovenance.org/ns/provext#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ro: <http://purl.org/wf4ever/ro#> .
@prefix wf: <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#> .
@prefix wf4ever: <http://purl.org/wf4ever/wf4ever#> .
@prefix wfdesc: <http://purl.org/wf4ever/wfdesc#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

metadata:directory-03305ae1-bded-486a-bfd3-b2f244261014.ttl a prov:Bundle .

metadata:directory-2363b376-af39-4421-ac82-298f9b5bf5d6.ttl a prov:Bundle .

<urn:uuid:03305ae1-bded-486a-bfd3-b2f244261014#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-03305ae1-bded-486a-bfd3-b2f244261014.ttl"^^xsd:QName ;
            provext:generalEntity id:03305ae1-bded-486a-bfd3-b2f244261014 ] .

id:0fea0e08-9d5a-41e3-8889-fcd05025f7f7 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:2125c168-2391-4a9c-924c-8d5d7330ffd5"^^xsd:QName ;
    prov:pairKey "mangrove-analysis-20260924-105955.json" .

<urn:uuid:2363b376-af39-4421-ac82-298f9b5bf5d6#ore> provext:qualifiedSpecialization [ a provext:Specialization ;
            prov:asInBundle "metadata:directory-2363b376-af39-4421-ac82-298f9b5bf5d6.ttl"^^xsd:QName ;
            provext:generalEntity id:2363b376-af39-4421-ac82-298f9b5bf5d6 ] .

id:2adedd6a-e764-47f5-82f0-d38efb1e074a a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec"^^xsd:QName ;
    prov:pairKey "biomass_quicklook.png" .

id:37dc1519-928c-46ff-b08a-8fa656dcede4 a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:931b869b-928e-447a-bf72-bc6914cb5e33 ;
            prov:atTime "2026-09-24T12:57:48.476740"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/parse_aoi/east> ] ;
    prov:value 9.535e+01 .

id:416a29f6-ecc2-420e-8f48-4d5bce2c3263 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:8982a81b-193e-4e8f-bacf-43df0bb2e832"^^xsd:QName ;
    prov:pairKey "biomass_summary.csv" .

id:4640e02b-c74b-40e1-a818-75d60264864b a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:3a808b83-4512-4301-9193-fe5620d0ece5"^^xsd:QName ;
    prov:pairKey "carbon_summary.csv" .

id:5356eeb5-2499-42be-bc4e-e8528bde1ff8 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "data:09b42388eb37be1a4b972127a78f691ec6eb3795"^^xsd:QName ;
    prov:pairKey "crs" .

id:57d70ea4-3ea9-4fa6-80e3-6504a20bafdc a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b"^^xsd:QName ;
    prov:pairKey "bbox" .

id:5ac41596-c778-4a85-89d7-230b7e014d7d a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "data:09b42388eb37be1a4b972127a78f691ec6eb3795"^^xsd:QName ;
    prov:pairKey "crs" .

id:758a05e3-6c7f-41d7-af5a-b4798d4b882f a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:03305ae1-bded-486a-bfd3-b2f244261014"^^xsd:QName ;
    prov:pairKey "mangrove-analysis-20260924-105955" .

id:827caa38-b109-46f9-be8f-4bc99371b11f a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149"^^xsd:QName ;
    prov:pairKey "mangrove_mask.tif" .

id:c436c153-ead6-49cd-8341-ee3fc3d94747 a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:931b869b-928e-447a-bf72-bc6914cb5e33 ;
            prov:atTime "2026-09-24T12:57:48.476740"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/parse_aoi/north> ] ;
    prov:value 1.61e+01 .

id:d8f4f618-3e0f-4024-a17f-b5c9d24b67b9 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:4c4659c5-50da-43e0-8077-7def82bdd204"^^xsd:QName ;
    prov:pairKey "bbox" .

id:dcb23f91-1dbc-4929-9021-d23ee962fc04 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:f70266c8-9af3-4228-89f4-230a39e31c83"^^xsd:QName ;
    prov:pairKey "catalog.json" .

id:e88dab08-862b-4933-9271-22712490f7bb a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:931b869b-928e-447a-bf72-bc6914cb5e33 ;
            prov:atTime "2026-09-24T12:57:48.476740"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/parse_aoi/south> ] ;
    prov:value 1.59e+01 .

id:eeb1bf4b-58a7-41c1-b269-d3320e3156e8 a prov:Entity,
        prov:KeyEntityPair ;
    prov:pairEntity "id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0"^^xsd:QName ;
    prov:pairKey "biomass.tif" .

id:ff077bb5-6a4d-426d-be0c-e1baf185a250 a prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:931b869b-928e-447a-bf72-bc6914cb5e33 ;
            prov:atTime "2026-09-24T12:57:48.476740"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/parse_aoi/west> ] ;
    prov:value 9.515e+01 .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/calculate_indices"^^xsd:QName,
        "wf:main/download_band"^^xsd:QName,
        "wf:main/estimate_biomass"^^xsd:QName,
        "wf:main/export_stac"^^xsd:QName,
        "wf:main/parse_aoi"^^xsd:QName,
        "wf:main/reproject_band"^^xsd:QName,
        "wf:main/select_scene"^^xsd:QName .

<arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/calculate_indices> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/parse_aoi> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

data:0ff4ea33ebd17218fd87cba84943c04e4e56137f a wfprov:Artifact,
        prov:Entity .

data:31cacee3ed40818e05aaa338979596497705bf56 a wfprov:Artifact,
        prov:Entity .

data:3f01f1f6a0a77a28c7ffde131fe58339eba52a01 a wfprov:Artifact,
        prov:Entity .

data:7238dd3cfee022d8d78263cad6a90a7ed0b1c31a a wfprov:Artifact,
        prov:Entity .

data:73c3313bdf7eed97c6d53d58dd7df2687f3ac1bf a wfprov:Artifact,
        prov:Entity .

data:78988010b890ce6f4d2136481f392787ec6d6106 a wfprov:Artifact,
        prov:Entity ;
    prov:value "red" .

data:7f0e99772494c2b7c3755662f3725e91b7991785 a wfprov:Artifact,
        prov:Entity .

data:938fb14bf0a2470ab2ae9b0420a64e5b81671271 a wfprov:Artifact,
        prov:Entity .

data:943b0707a0f1a109dd1de1d61e37a1654a191ae9 a wfprov:Artifact,
        prov:Entity .

data:9b8ad0ffede9b72258d46c48d2555b75623aaa2e a wfprov:Artifact,
        prov:Entity .

data:9c81f26b42f7f833fea1b35727ffbcc91dab6e3c a wfprov:Artifact,
        prov:Entity .

data:b441775de2d148543034d26997c017d3a24544ed a wfprov:Artifact,
        prov:Entity .

data:ba936cb0e062bea4078e8b56371ca8fe054093dd a wfprov:Artifact,
        prov:Entity ;
    prov:value "nir" .

data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c a wfprov:Artifact,
        prov:Entity ;
    prov:value "green" .

data:d1a501118882d0e474e5342dbf965ace5b931cca a wfprov:Artifact,
        prov:Entity .

data:dd6dd1205c33f51e783742f16e856d1752beceda a wfprov:Artifact,
        prov:Entity .

data:e657235e3d4603e9bbdf1f26c7101ece981f1255 a wfprov:Artifact,
        prov:Entity .

id:0117a745-b852-44ba-a7a0-08e529a7067d a prov:Entity ;
    prov:value 9.515e+01 .

id:0628dd54-097a-4857-a725-9ce3cd63fc2c a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/calculate-indices:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/calculate-indices:v0.0.2-rc2" .

id:068eb4ce-9e22-4f53-8d00-6a22656436bb a prov:Entity ;
    prov:value 2e-01 .

id:0a68208c-621e-48fe-b955-774694ac318c a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2" .

id:105cc922-459c-4a99-a431-5d4b3b38aea9 a prov:Entity ;
    prov:value 9.535e+01 .

id:10db2d8a-f421-4312-aef9-6c5efbad211d a prov:Entity ;
    prov:value -3e-01 .

id:112f1253-d984-432e-8b9c-f6b600dc0867 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2" .

id:114fd6b8-e343-4c8d-b816-20e051ac87a0 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/export-stac:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/export-stac:v0.0.2-rc2" .

id:14e98d45-e476-4164-bcdd-e4822839bf51 a prov:Entity ;
    prov:value 4.7e-01 .

id:183be3aa-ca39-47b3-9cb9-9972ab5b4b04 a prov:Entity ;
    prov:value 1.61e+01 .

id:1d5c6165-738d-4f3e-815b-21b08a3876bc a prov:Entity ;
    prov:value 4.7e-01 .

id:2125c168-2391-4a9c-924c-8d5d7330ffd5 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:7238dd3cfee022d8d78263cad6a90a7ed0b1c31a ] ;
    cwlprov:basename "mangrove-analysis-20260924-105955.json" .

id:2363b376-af39-4421-ac82-298f9b5bf5d6 a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-2363b376-af39-4421-ac82-298f9b5bf5d6.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:758a05e3-6c7f-41d7-af5a-b4798d4b882f"^^xsd:QName,
        "id:dcb23f91-1dbc-4929-9021-d23ee962fc04"^^xsd:QName ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:c16504e6-ec23-43da-92c9-c00151a037f2 ;
            prov:atTime "2026-09-24T12:59:58.100038"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/stac_catalog> ],
        [ a prov:Generation ;
            prov:activity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ;
            prov:atTime "2026-09-24T12:59:58.171647"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/primary/stac> ] ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:f70266c8-9af3-4228-89f4-230a39e31c83 ],
        [ a provext:Membership ;
            provext:member id:03305ae1-bded-486a-bfd3-b2f244261014 ] ;
    cwlprov:basename "outputs" .

id:2f66b1e4-39fc-4551-8aa8-49831c3211bb a prov:Entity ;
    prov:value 1.59e+01 .

id:32255a12-525c-491e-bf2f-f579c17fdf39 a prov:Entity ;
    prov:value 3e-01 .

id:3659eb06-f1ed-4ec3-8ccd-74774fdae9ac a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:376997e3-8d83-426b-b84f-e985b2af4046 ;
            prov:atTime "2026-09-24T12:59:47.581661"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/biomass_summary_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:4451dd50c71fb43e9f78bbe62b52f4d6349624a8 ] ;
    cwlprov:basename "biomass_summary.csv" ;
    cwlprov:nameext ".csv" ;
    cwlprov:nameroot "biomass_summary" .

id:37378d08-0575-4061-9f35-0bd44e06d360 a prov:Entity ;
    prov:value 9.515e+01 .

id:380f03a1-1d47-401e-b9d6-4e6b30363135 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:a29b44cd-ed7f-4617-8e76-6b4279377f1d ],
        [ a provext:Membership ;
            provext:member id:6ee43ae1-f7f0-44e8-9521-f520ee73f8d5 ],
        [ a provext:Membership ;
            provext:member id:cbcc2c55-1928-47ce-88e9-9cc945faa37e ] .

id:3874df5f-5219-46d7-b883-f927b2718f98 a prov:Entity ;
    prov:value 1.61e+01 .

id:3a6146e3-99f8-4cdc-aa09-aa71cf40578e a prov:Entity ;
    prov:value 1.61e+01 .

id:3a808b83-4512-4301-9193-fe5620d0ece5 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:661fc93f43cc808586d1ba6bf1b9e22a963ce449 ] ;
    cwlprov:basename "carbon_summary.csv" .

id:3ba979c6-c4b1-4d94-bd53-556aca41e518 a prov:Entity ;
    prov:value 9e-01 .

id:3f96db66-4f0b-4af4-9034-8d14f35016b5 a prov:Entity ;
    prov:value -7.52e+01 .

id:4a3cec45-e5c9-449f-b623-e71818c12362 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930 ;
            prov:atTime "2026-09-24T12:59:40.382890"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/calculate_indices/ndwi_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:938fb14bf0a2470ab2ae9b0420a64e5b81671271 ] ;
    cwlprov:basename "ndwi.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "ndwi" .

id:4c4659c5-50da-43e0-8077-7def82bdd204 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:dd4db319-ab09-4589-93be-c0ab5a21b781 ],
        [ a provext:Membership ;
            provext:member id:2f66b1e4-39fc-4551-8aa8-49831c3211bb ],
        [ a provext:Membership ;
            provext:member id:c0bace95-d5f7-47c8-85c2-88006db5ab2d ],
        [ a provext:Membership ;
            provext:member id:a60dd30c-c4c6-4254-be37-68b96605a358 ] .

id:4d33da78-bc2b-4f11-927c-55071695661b a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/select-scene:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/select-scene:v0.0.2-rc2" .

id:50e7a067-7cf5-48cc-a7a9-995f535a42a5 a prov:Entity ;
    prov:value 9.515e+01 .

id:547c8cdb-eb07-4b2e-bd53-a0e43e839323 a prov:Entity ;
    prov:value 9.535e+01 .

id:54cd6275-9321-44c8-856b-5978bcb26eae a prov:Entity ;
    prov:value -7.52e+01 .

id:5d3a2cf8-ee6d-4729-9049-1b13ac82b9c8 a prov:Entity ;
    prov:value "20"^^xsd:int .

id:5f1b745b-1648-40c5-8fbe-a8197ea712d1 a prov:Entity ;
    prov:value 9.515e+01 .

id:5fc90b70-355b-4773-ab64-068be1b36cdc a prov:Entity ;
    prov:value -3e-01 .

id:61f78ec9-45f1-4537-9ed6-4f4e8616efbf a prov:Entity ;
    prov:value 1.59e+01 .

id:6811beb8-4d7f-45b8-9707-e34238fed895 a prov:Entity ;
    prov:value 1e-04 .

id:6818485a-eeb1-4ded-8202-995389ee3c9e a prov:Entity ;
    prov:value 1.61e+01 .

id:6b4a4879-8c4b-4f74-9957-2902ed5cce8e a prov:Entity ;
    prov:value 9.515e+01 .

id:6dc7f217-6174-4e64-be16-a87833936301 a prov:Entity ;
    prov:value 9e-01 .

id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_band" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band> ],
        [ a prov:Association ;
            prov:agent id:f3cf79d9-5592-4f15-a94b-728004a97650 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:58:16.231585"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:58:01.354035"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:01.588695"^^xsd:dateTime ;
            prov:entity id:8f1f4d19-7ab7-48f7-a279-0cd0f11d5bb3 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:01.588601"^^xsd:dateTime ;
            prov:entity id:d81429c0-f7f3-4b1c-b7bb-0dd72a874aff ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:01.588654"^^xsd:dateTime ;
            prov:entity id:db33c88c-4dd2-4ea1-b06b-577175d50413 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band/stac_item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:01.588501"^^xsd:dateTime ;
            prov:entity id:d1fc5582-5435-437c-afc6-7bf715e11ac9 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:01.588559"^^xsd:dateTime ;
            prov:entity id:183be3aa-ca39-47b3-9cb9-9972ab5b4b04 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:01.588345"^^xsd:dateTime ;
            prov:entity data:78988010b890ce6f4d2136481f392787ec6d6106 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band/band> ] .

id:6ee43ae1-f7f0-44e8-9521-f520ee73f8d5 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b ;
            prov:atTime "2026-09-24T12:59:18.344902"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/reprojected_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:3f01f1f6a0a77a28c7ffde131fe58339eba52a01 ] ;
    cwlprov:basename "red_4326.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "red_4326" .

id:6f5fd862-1f4d-4a1b-9c03-5f531e769ee6 a prov:Entity ;
    prov:value 1e-04 .

id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:0117a745-b852-44ba-a7a0-08e529a7067d ],
        [ a provext:Membership ;
            provext:member id:ab8af93b-6ae4-4bf6-86ac-989a33e53741 ],
        [ a provext:Membership ;
            provext:member id:3a6146e3-99f8-4cdc-aa09-aa71cf40578e ],
        [ a provext:Membership ;
            provext:member id:105cc922-459c-4a99-a431-5d4b3b38aea9 ] .

id:72b6e1b9-31a6-41a5-9509-2fb54eb7a854 a prov:Entity ;
    prov:value 1.61e+01 .

id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:2b8178722e8bb6fbc41909e7e32e88d4aa439eb8 ] ;
    cwlprov:basename "biomass.tif" .

id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:0ff4ea33ebd17218fd87cba84943c04e4e56137f ] ;
    cwlprov:basename "biomass_quicklook.png" .

id:74367791-176c-4eaf-9ca3-e10883dc4521 a prov:Entity ;
    prov:value 9.515e+01 .

id:7814458d-34a1-43b8-91a4-d47c15a05095 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2" .

id:7ad088e7-2b84-406e-a4ef-5e791c3c5457 a prov:Entity ;
    prov:value 9.535e+01 .

id:7dcbf0c1-1cea-4c69-a6a5-252d188398ca a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2" .

id:7f3077b0-d507-4f90-b1ce-76c822fefb1e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:6ed05a19-69ad-401e-9b2a-5d24ea6d9f57 ;
            prov:atTime "2026-09-24T12:58:16.231617"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band/band_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e657235e3d4603e9bbdf1f26c7101ece981f1255 ] ;
    cwlprov:basename "red.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "red" .

id:81daad74-dad7-41e0-bc70-26432d1dfb21 a wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    prov:hadDictionaryMember "id:5356eeb5-2499-42be-bc4e-e8528bde1ff8"^^xsd:QName,
        "id:d8f4f618-3e0f-4024-a17f-b5c9d24b67b9"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member data:09b42388eb37be1a4b972127a78f691ec6eb3795 ],
        [ a provext:Membership ;
            provext:member id:4c4659c5-50da-43e0-8077-7def82bdd204 ] .

id:82a589e5-da3e-471d-959a-5f0ada295abf a prov:Agent .

id:87573e08-1a69-4a83-a551-f2a1c560cc7c a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930 ;
            prov:atTime "2026-09-24T12:59:40.382890"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/calculate_indices/savi_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:d1a501118882d0e474e5342dbf965ace5b931cca ] ;
    cwlprov:basename "savi.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "savi" .

id:87d73316-63b5-4c3d-ba48-d2812d5dd71a a prov:Entity ;
    prov:value "4326"^^xsd:int .

id:8982a81b-193e-4e8f-bacf-43df0bb2e832 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:4451dd50c71fb43e9f78bbe62b52f4d6349624a8 ] ;
    cwlprov:basename "biomass_summary.csv" .

id:8ea13029-7217-48c6-83b2-5168cf85a135 a wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    prov:hadDictionaryMember "id:57d70ea4-3ea9-4fa6-80e3-6504a20bafdc"^^xsd:QName,
        "id:5ac41596-c778-4a85-89d7-230b7e014d7d"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:728b8a7c-ecb1-4cd6-b49e-3f7537dd514b ],
        [ a provext:Membership ;
            provext:member data:09b42388eb37be1a4b972127a78f691ec6eb3795 ] .

id:8f1f4d19-7ab7-48f7-a279-0cd0f11d5bb3 a prov:Entity ;
    prov:value 9.515e+01 .

id:924dc3e6-e45e-4ae0-940f-d538dce7a6e4 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:376997e3-8d83-426b-b84f-e985b2af4046 ;
            prov:atTime "2026-09-24T12:59:47.581661"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/analysis_summary_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:7f0e99772494c2b7c3755662f3725e91b7991785 ] ;
    cwlprov:basename "analysis_summary.json" ;
    cwlprov:nameext ".json" ;
    cwlprov:nameroot "analysis_summary" .

id:936a4bd7-abcd-4bf2-9423-94ae772bd057 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/reproject-band:v0.0.2-rc2" .

id:95ff8885-0a15-43aa-82fa-7cd8b1e37f8d a prov:Entity ;
    prov:value "90"^^xsd:int .

id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_band_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:112f1253-d984-432e-8b9c-f6b600dc0867 ],
        [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:58:36.167066"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:58:16.254478"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:16.268833"^^xsd:dateTime ;
            prov:entity id:50e7a067-7cf5-48cc-a7a9-995f535a42a5 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:16.268706"^^xsd:dateTime ;
            prov:entity id:e10c43d5-f616-4774-8ff7-be84cdf977aa ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:16.268376"^^xsd:dateTime ;
            prov:entity data:bc74f4f071a5a33f00ab88a6d6385b5e6638b86c ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:16.268791"^^xsd:dateTime ;
            prov:entity id:db33c88c-4dd2-4ea1-b06b-577175d50413 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2/stac_item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:16.268610"^^xsd:dateTime ;
            prov:entity id:547c8cdb-eb07-4b2e-bd53-a0e43e839323 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:16.268667"^^xsd:dateTime ;
            prov:entity id:d7eaf21e-997d-440a-9c59-f5def6552d98 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2/north> ] .

id:9c4478e2-935b-41d5-857b-c2641d1c917d a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:376997e3-8d83-426b-b84f-e985b2af4046 ;
            prov:atTime "2026-09-24T12:59:47.581661"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/carbon_summary_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:661fc93f43cc808586d1ba6bf1b9e22a963ce449 ] ;
    cwlprov:basename "carbon_summary.csv" ;
    cwlprov:nameext ".csv" ;
    cwlprov:nameroot "carbon_summary" .

id:a1526e7f-b483-4350-9c60-e56f786bfff3 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:ad22cfb2-89d1-476b-a33a-73bf3be4c782 ;
            prov:atTime "2026-09-24T12:59:12.183023"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3/band_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:9b8ad0ffede9b72258d46c48d2555b75623aaa2e ] ;
    cwlprov:basename "nir.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "nir" .

id:a29b44cd-ed7f-4617-8e76-6b4279377f1d a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:af446720-3625-4794-9126-810a0620808f ;
            prov:atTime "2026-09-24T12:59:32.420687"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/reprojected_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:9c81f26b42f7f833fea1b35727ffbcc91dab6e3c ] ;
    cwlprov:basename "nir_4326.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "nir_4326" .

id:a60dd30c-c4c6-4254-be37-68b96605a358 a prov:Entity ;
    prov:value 9.515e+01 .

id:aa6dbd65-080e-408b-8c01-0acfe33cc871 a prov:Entity ;
    prov:value "4326"^^xsd:int .

id:aabf8f10-1849-4b0c-891f-dd7a04a822a7 a prov:Entity ;
    prov:value 2.505e+02 .

id:ab8af93b-6ae4-4bf6-86ac-989a33e53741 a prov:Entity ;
    prov:value 1.59e+01 .

id:ad22cfb2-89d1-476b-a33a-73bf3be4c782 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_band_3" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:0a68208c-621e-48fe-b955-774694ac318c ],
        [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:12.183003"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:58:36.186017"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:36.200466"^^xsd:dateTime ;
            prov:entity id:e858184a-032a-4649-a114-21e67c56c9b7 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:36.200068"^^xsd:dateTime ;
            prov:entity data:ba936cb0e062bea4078e8b56371ca8fe054093dd ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:36.200263"^^xsd:dateTime ;
            prov:entity id:7ad088e7-2b84-406e-a4ef-5e791c3c5457 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:36.200371"^^xsd:dateTime ;
            prov:entity id:c11e8081-a4e0-43ef-ae32-f37e0aa2b9a7 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:36.200318"^^xsd:dateTime ;
            prov:entity id:3874df5f-5219-46d7-b883-f927b2718f98 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:58:36.200427"^^xsd:dateTime ;
            prov:entity id:db33c88c-4dd2-4ea1-b06b-577175d50413 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_3/stac_item> ] .

id:af446720-3625-4794-9126-810a0620808f a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/reproject_band_3" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3> ],
        [ a prov:Association ;
            prov:agent id:936a4bd7-abcd-4bf2-9423-94ae772bd057 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:32.420671"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:59:25.490304"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:25.509686"^^xsd:dateTime ;
            prov:entity id:e2de3352-f3cb-41aa-976e-7d0fa8018bcc ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:25.509728"^^xsd:dateTime ;
            prov:entity id:d2cddbd6-1979-4e51-b267-7fec4bab3dc8 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:25.509607"^^xsd:dateTime ;
            prov:entity id:ffc8283b-4edf-49e1-bcab-9bd74542ce23 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:25.509555"^^xsd:dateTime ;
            prov:entity id:e6cc9d7e-080c-437c-a66b-4f386982b118 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:25.509646"^^xsd:dateTime ;
            prov:entity id:72b6e1b9-31a6-41a5-9509-2fb54eb7a854 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:25.509369"^^xsd:dateTime ;
            prov:entity id:a1526e7f-b483-4350-9c60-e56f786bfff3 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/band_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:25.509771"^^xsd:dateTime ;
            prov:entity id:5f1b745b-1648-40c5-8fbe-a8197ea712d1 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_3/west> ] .

id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:443e27d9b969edf33b0080e08bc8bffe154f06f9 ] ;
    cwlprov:basename "mangrove_mask.tif" .

id:bc49aa46-3931-4344-8b1e-7788b5f50e0f a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:376997e3-8d83-426b-b84f-e985b2af4046 ;
            prov:atTime "2026-09-24T12:59:47.581661"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/biomass_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:2b8178722e8bb6fbc41909e7e32e88d4aa439eb8 ] ;
    cwlprov:basename "biomass.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "biomass" .

id:c0bace95-d5f7-47c8-85c2-88006db5ab2d a prov:Entity ;
    prov:value 9.535e+01 .

id:c11e8081-a4e0-43ef-ae32-f37e0aa2b9a7 a prov:Entity ;
    prov:value 1.59e+01 .

id:c16504e6-ec23-43da-92c9-c00151a037f2 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/export_stac" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac> ],
        [ a prov:Association ;
            prov:agent id:114fd6b8-e343-4c8d-b816-20e051ac87a0 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:58.100015"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:59:47.598635"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692318"^^xsd:dateTime ;
            prov:entity id:d9517d0d-9e97-4d22-afa7-a402d0537cf6 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/mangrove_mask_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692088"^^xsd:dateTime ;
            prov:entity id:bc49aa46-3931-4344-8b1e-7788b5f50e0f ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/biomass_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.691973"^^xsd:dateTime ;
            prov:entity id:924dc3e6-e45e-4ae0-940f-d538dce7a6e4 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/analysis_summary_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692292"^^xsd:dateTime ;
            prov:entity id:dc91669b-4a2f-4bd1-92c9-382337d78dba ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692122"^^xsd:dateTime ;
            prov:entity id:3659eb06-f1ed-4ec3-8ccd-74774fdae9ac ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/biomass_summary_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692513"^^xsd:dateTime ;
            prov:entity id:37378d08-0575-4061-9f35-0bd44e06d360 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692457"^^xsd:dateTime ;
            prov:entity id:db33c88c-4dd2-4ea1-b06b-577175d50413 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/stac_item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692360"^^xsd:dateTime ;
            prov:entity id:6818485a-eeb1-4ded-8202-995389ee3c9e ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692412"^^xsd:dateTime ;
            prov:entity id:c5451c9d-b6ce-42de-b9a3-9512e9784e73 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:47.692148"^^xsd:dateTime ;
            prov:entity id:9c4478e2-935b-41d5-857b-c2641d1c917d ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/export_stac/carbon_summary_file> ] .

id:c3c368d8-6ec0-4064-bcfe-a0c6ebea821c a prov:Entity ;
    prov:value "20"^^xsd:int .

id:c521c30a-5aa8-4fc8-9d25-b8d9de55c870 a prov:Entity ;
    prov:value 1.61e+01 .

id:c5451c9d-b6ce-42de-b9a3-9512e9784e73 a prov:Entity ;
    prov:value 1.59e+01 .

id:c66a4eb4-76b6-4a3d-b5ee-aa35009027e1 a prov:Entity ;
    prov:value 3e-01 .

id:c8ba466f-bf4e-4bf3-a2cb-e7013b6146cf a prov:Entity ;
    prov:value "4326"^^xsd:int .

id:cb4e16e3-e34d-4252-820f-27055b12f9f0 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:9c060ac7-786e-4f1d-874a-ac1dc995d3a5 ;
            prov:atTime "2026-09-24T12:58:36.167096"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/download_band_2/band_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:73c3313bdf7eed97c6d53d58dd7df2687f3ac1bf ] ;
    cwlprov:basename "green.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "green" .

id:cbcc2c55-1928-47ce-88e9-9cc945faa37e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f4cf1f0f-6d62-483b-ba92-38d6e1040135 ;
            prov:atTime "2026-09-24T12:59:25.470134"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/reprojected_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:dd6dd1205c33f51e783742f16e856d1752beceda ] ;
    cwlprov:basename "green_4326.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "green_4326" .

id:d092277a-8801-406a-94ec-078bb314ec37 a prov:Entity ;
    prov:value 1.59e+01 .

id:d124ea7e-589c-4dd3-9515-031b20191cf3 a prov:Entity ;
    prov:value 9.515e+01 .

id:d1fc5582-5435-437c-afc6-7bf715e11ac9 a prov:Entity ;
    prov:value 9.535e+01 .

id:d2cddbd6-1979-4e51-b267-7fec4bab3dc8 a prov:Entity ;
    prov:value 1.59e+01 .

id:d7eaf21e-997d-440a-9c59-f5def6552d98 a prov:Entity ;
    prov:value 1.61e+01 .

id:d81429c0-f7f3-4b1c-b7bb-0dd72a874aff a prov:Entity ;
    prov:value 1.59e+01 .

id:d9517d0d-9e97-4d22-afa7-a402d0537cf6 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:376997e3-8d83-426b-b84f-e985b2af4046 ;
            prov:atTime "2026-09-24T12:59:47.581661"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/mangrove_mask_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:443e27d9b969edf33b0080e08bc8bffe154f06f9 ] ;
    cwlprov:basename "mangrove_mask.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "mangrove_mask" .

id:d9c2f532-47b2-45e7-9825-ed5413dea033 a prov:Entity ;
    prov:value 2.505e+02 .

id:da18af81-c62b-42a2-8596-4e773968588d a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930 ;
            prov:atTime "2026-09-24T12:59:40.382890"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/calculate_indices/ndvi_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:31cacee3ed40818e05aaa338979596497705bf56 ] ;
    cwlprov:basename "ndvi.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "ndvi" .

id:dc91669b-4a2f-4bd1-92c9-382337d78dba a prov:Entity ;
    prov:value 9.535e+01 .

id:dd4db319-ab09-4589-93be-c0ab5a21b781 a prov:Entity ;
    prov:value 1.61e+01 .

id:df87d5ba-da6e-432b-b924-80ec05cd6e0b a prov:Entity ;
    prov:value 9.535e+01 .

id:e10c43d5-f616-4774-8ff7-be84cdf977aa a prov:Entity ;
    prov:value 1.59e+01 .

id:e279fef3-8bfb-464b-9df4-3497a11b9735 a prov:Entity ;
    prov:value 1.61e+01 .

id:e2d4aa64-8b79-4922-beaa-658f42437197 a prov:Entity ;
    prov:value "90"^^xsd:int .

id:e2de3352-f3cb-41aa-976e-7d0fa8018bcc a prov:Entity ;
    prov:value 1e-04 .

id:e56a0493-0204-4306-b246-d6f0a0ed8e0b a prov:Entity ;
    prov:value 1.59e+01 .

id:e6cc9d7e-080c-437c-a66b-4f386982b118 a prov:Entity ;
    prov:value 9.535e+01 .

id:e70e9f12-3e5c-4948-9ca6-449d0d53c077 a prov:Entity ;
    prov:value 9.535e+01 .

id:e858184a-032a-4649-a114-21e67c56c9b7 a prov:Entity ;
    prov:value 9.515e+01 .

id:e8ec687a-b9d1-4afa-83c6-6c3bf9266d3e a prov:Entity ;
    prov:value 1.61e+01 .

id:e932c1b9-7fde-4dbd-a1af-1b17de8a38de a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/estimate-biomass:v0.0.2-rc2" .

id:eff8560e-cd59-4a84-8dac-2f766310d52a a prov:Entity ;
    prov:value 1e-04 .

id:effb40f4-0a75-4498-80d7-d04365cf463b a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/select_scene" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:4d33da78-bc2b-4f11-927c-55071695661b ],
        [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:58:01.337237"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:57:48.481355"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.578733"^^xsd:dateTime ;
            prov:entity data:4c89b83017b6bf2fdefdc95f52a039255235ba37 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/collection> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.579935"^^xsd:dateTime ;
            prov:entity id:d124ea7e-589c-4dd3-9515-031b20191cf3 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.577808"^^xsd:dateTime ;
            prov:entity id:5d3a2cf8-ee6d-4729-9049-1b13ac82b9c8 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/cloud_cover_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.578840"^^xsd:dateTime ;
            prov:entity id:df87d5ba-da6e-432b-b924-80ec05cd6e0b ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.579345"^^xsd:dateTime ;
            prov:entity id:d092277a-8801-406a-94ec-078bb314ec37 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.579301"^^xsd:dateTime ;
            prov:entity id:e279fef3-8bfb-464b-9df4-3497a11b9735 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.578791"^^xsd:dateTime ;
            prov:entity id:e2d4aa64-8b79-4922-beaa-658f42437197 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/days_back> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:48.579889"^^xsd:dateTime ;
            prov:entity data:5052a0c49b2beb0515446c40d4eee08c7fcad904 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/stac_api> ] .

id:f3cf79d9-5592-4f15-a94b-728004a97650 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2" ;
    cwlprov:image "ghcr.io/geolabs/kindgrove/download-band:v0.0.2-rc2" .

id:f4cf1f0f-6d62-483b-ba92-38d6e1040135 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/reproject_band_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:7814458d-34a1-43b8-91a4-d47c15a05095 ],
        [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:25.470107"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:59:18.360040"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:18.369114"^^xsd:dateTime ;
            prov:entity id:61f78ec9-45f1-4537-9ed6-4f4e8616efbf ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:18.369015"^^xsd:dateTime ;
            prov:entity id:87d73316-63b5-4c3d-ba48-d2812d5dd71a ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:18.368961"^^xsd:dateTime ;
            prov:entity id:faffe676-addb-4b7c-ac15-34a991f69f69 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/east> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:18.369145"^^xsd:dateTime ;
            prov:entity id:6b4a4879-8c4b-4f74-9957-2902ed5cce8e ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:18.369051"^^xsd:dateTime ;
            prov:entity id:c521c30a-5aa8-4fc8-9d25-b8d9de55c870 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:18.368809"^^xsd:dateTime ;
            prov:entity id:cb4e16e3-e34d-4252-820f-27055b12f9f0 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/band_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:18.369083"^^xsd:dateTime ;
            prov:entity id:6811beb8-4d7f-45b8-9707-e34238fed895 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band_2/resolution> ] .

id:f5beff83-d577-48b1-b086-b1a35ed1b44b a prov:Entity ;
    prov:value 2e-01 .

id:f6c152ab-0593-4080-aa4f-1eeb02a954b6 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image alpine:3.22.2" ;
    cwlprov:image "alpine:3.22.2" .

id:f6decba1-ec9c-4822-a5f2-feb5a1bd925b a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/reproject_band" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band> ],
        [ a prov:Association ;
            prov:agent id:7dcbf0c1-1cea-4c69-a6a5-252d188398ca ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:18.344891"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:59:12.204580"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:12.290768"^^xsd:dateTime ;
            prov:entity id:eff8560e-cd59-4a84-8dac-2f766310d52a ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:12.290735"^^xsd:dateTime ;
            prov:entity id:e8ec687a-b9d1-4afa-83c6-6c3bf9266d3e ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/north> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:12.290487"^^xsd:dateTime ;
            prov:entity id:7f3077b0-d507-4f90-b1ce-76c822fefb1e ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/band_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:12.290700"^^xsd:dateTime ;
            prov:entity id:aa6dbd65-080e-408b-8c01-0acfe33cc871 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:12.290832"^^xsd:dateTime ;
            prov:entity id:74367791-176c-4eaf-9ca3-e10883dc4521 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/west> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:12.290800"^^xsd:dateTime ;
            prov:entity id:e56a0493-0204-4306-b246-d6f0a0ed8e0b ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/south> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:12.290654"^^xsd:dateTime ;
            prov:entity id:e70e9f12-3e5c-4948-9ca6-449d0d53c077 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/reproject_band/east> ] .

id:f70266c8-9af3-4228-89f4-230a39e31c83 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:943b0707a0f1a109dd1de1d61e37a1654a191ae9 ] ;
    cwlprov:basename "catalog.json" .

id:faffe676-addb-4b7c-ac15-34a991f69f69 a prov:Entity ;
    prov:value 9.535e+01 .

id:ffc8283b-4edf-49e1-bcab-9bd74542ce23 a prov:Entity ;
    prov:value "4326"^^xsd:int .

data:09b42388eb37be1a4b972127a78f691ec6eb3795 a wfprov:Artifact,
        prov:Entity ;
    prov:value "CRS84" .

data:2b8178722e8bb6fbc41909e7e32e88d4aa439eb8 a wfprov:Artifact,
        prov:Entity .

data:443e27d9b969edf33b0080e08bc8bffe154f06f9 a wfprov:Artifact,
        prov:Entity .

data:4451dd50c71fb43e9f78bbe62b52f4d6349624a8 a wfprov:Artifact,
        prov:Entity .

data:4c89b83017b6bf2fdefdc95f52a039255235ba37 a wfprov:Artifact,
        prov:Entity ;
    prov:value "sentinel-2-l2a" .

data:5052a0c49b2beb0515446c40d4eee08c7fcad904 a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v1" .

data:661fc93f43cc808586d1ba6bf1b9e22a963ce449 a wfprov:Artifact,
        prov:Entity .

id:03305ae1-bded-486a-bfd3-b2f244261014 a ro:Folder,
        wfprov:Artifact,
        prov:Collection,
        prov:Dictionary,
        prov:Entity ;
    ore:isDescribedBy "metadata:directory-03305ae1-bded-486a-bfd3-b2f244261014.ttl"^^xsd:QName ;
    prov:hadDictionaryMember "id:0fea0e08-9d5a-41e3-8889-fcd05025f7f7"^^xsd:QName,
        "id:2adedd6a-e764-47f5-82f0-d38efb1e074a"^^xsd:QName,
        "id:416a29f6-ecc2-420e-8f48-4d5bce2c3263"^^xsd:QName,
        "id:4640e02b-c74b-40e1-a818-75d60264864b"^^xsd:QName,
        "id:827caa38-b109-46f9-be8f-4bc99371b11f"^^xsd:QName,
        "id:eeb1bf4b-58a7-41c1-b269-d3320e3156e8"^^xsd:QName ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:2125c168-2391-4a9c-924c-8d5d7330ffd5 ],
        [ a provext:Membership ;
            provext:member id:b3b5ccdd-6d2b-4e1c-b9d3-f904fd999149 ],
        [ a provext:Membership ;
            provext:member id:73d52f8a-86fe-46bd-a3e3-ed71eaa8b8d0 ],
        [ a provext:Membership ;
            provext:member id:3a808b83-4512-4301-9193-fe5620d0ece5 ],
        [ a provext:Membership ;
            provext:member id:740ff7b1-6fac-4641-92f3-b9a9b32a0eec ],
        [ a provext:Membership ;
            provext:member id:8982a81b-193e-4e8f-bacf-43df0bb2e832 ] ;
    cwlprov:basename "mangrove-analysis-20260924-105955" .

id:b05b7747-ddf9-4e6a-9b4a-2426b0e4b930 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_indices" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:0628dd54-097a-4857-a725-9ce3cd63fc2c ],
        [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/calculate_indices> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:40.382878"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:59:32.442072"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:32.637646"^^xsd:dateTime ;
            prov:entity id:380f03a1-1d47-401e-b9d6-4e6b30363135 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/calculate_indices/band_files> ] .

id:931b869b-928e-447a-bf72-bc6914cb5e33 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/parse_aoi" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/parse_aoi> ],
        [ a prov:Association ;
            prov:agent id:f6c152ab-0593-4080-aa4f-1eeb02a954b6 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:57:48.476728"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:57:45.249740"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.385435"^^xsd:dateTime ;
            prov:entity id:81daad74-dad7-41e0-bc70-26432d1dfb21 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/parse_aoi/aoi> ] .

id:376997e3-8d83-426b-b84f-e985b2af4046 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/estimate_biomass" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass> ],
        [ a prov:Association ;
            prov:agent id:e932c1b9-7fde-4dbd-a1af-1b17de8a38de ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:47.581645"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:59:40.439020"^^xsd:dateTime ;
            prov:hadActivity id:e96466cd-dd6c-469a-af95-6bbc439a3156 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534185"^^xsd:dateTime ;
            prov:entity id:14e98d45-e476-4164-bcdd-e4822839bf51 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/carbon_fraction> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534428"^^xsd:dateTime ;
            prov:entity id:db33c88c-4dd2-4ea1-b06b-577175d50413 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/stac_item> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534371"^^xsd:dateTime ;
            prov:entity id:87573e08-1a69-4a83-a551-f2a1c560cc7c ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/savi_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534219"^^xsd:dateTime ;
            prov:entity id:da18af81-c62b-42a2-8596-4e773968588d ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/ndvi_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534147"^^xsd:dateTime ;
            prov:entity id:d9c2f532-47b2-45e7-9825-ed5413dea033 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/biomass_slope> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534255"^^xsd:dateTime ;
            prov:entity id:3ba979c6-c4b1-4d94-bd53-556aca41e518 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/ndvi_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534286"^^xsd:dateTime ;
            prov:entity id:32255a12-525c-491e-bf2f-f579c17fdf39 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/ndvi_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534079"^^xsd:dateTime ;
            prov:entity id:54cd6275-9321-44c8-856b-5978bcb26eae ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/biomass_intercept> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534404"^^xsd:dateTime ;
            prov:entity id:f5beff83-d577-48b1-b086-b1a35ed1b44b ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/savi_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534311"^^xsd:dateTime ;
            prov:entity id:4a3cec45-e5c9-449f-b623-e71818c12362 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/ndwi_file> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:59:40.534343"^^xsd:dateTime ;
            prov:entity id:10db2d8a-f421-4312-aef9-6c5efbad211d ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/estimate_biomass/ndwi_min> ] .

id:db33c88c-4dd2-4ea1-b06b-577175d50413 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:effb40f4-0a75-4498-80d7-d04365cf463b ;
            prov:atTime "2026-09-24T12:58:01.337315"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/select_scene/stac_item> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:b441775de2d148543034d26997c017d3a24544ed ] ;
    cwlprov:basename "scene_item.json" ;
    cwlprov:nameext ".json" ;
    cwlprov:nameroot "scene_item" .

id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:57:44.628379"^^xsd:dateTime ;
            prov:hadActivity id:82a589e5-da3e-471d-959a-5f0ada295abf ] .

id:e96466cd-dd6c-469a-af95-6bbc439a3156 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-24T12:59:58.171742"^^xsd:dateTime ;
            prov:hadActivity id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-24T12:57:44.628464"^^xsd:dateTime ;
            prov:hadActivity id:1432f81c-9552-435f-a0ab-6b28e12ea1b3 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.244950"^^xsd:dateTime ;
            prov:entity id:1d5c6165-738d-4f3e-815b-21b08a3876bc ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/carbon_fraction> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.244872"^^xsd:dateTime ;
            prov:entity id:3f96db66-4f0b-4af4-9034-8d14f35016b5 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/biomass_intercept> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.246218"^^xsd:dateTime ;
            prov:entity id:6f5fd862-1f4d-4a1b-9c03-5f531e769ee6 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.245944"^^xsd:dateTime ;
            prov:entity data:4c89b83017b6bf2fdefdc95f52a039255235ba37 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/collection> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.244804"^^xsd:dateTime ;
            prov:entity id:8ea13029-7217-48c6-83b2-5168cf85a135 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/aoi> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.246066"^^xsd:dateTime ;
            prov:entity id:c8ba466f-bf4e-4bf3-a2cb-e7013b6146cf ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/epsg> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.247187"^^xsd:dateTime ;
            prov:entity data:5052a0c49b2beb0515446c40d4eee08c7fcad904 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/stac_api> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.246104"^^xsd:dateTime ;
            prov:entity id:6dc7f217-6174-4e64-be16-a87833936301 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/ndvi_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.244914"^^xsd:dateTime ;
            prov:entity id:aabf8f10-1849-4b0c-891f-dd7a04a822a7 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/biomass_slope> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.246023"^^xsd:dateTime ;
            prov:entity id:95ff8885-0a15-43aa-82fa-7cd8b1e37f8d ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/days_back> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.244986"^^xsd:dateTime ;
            prov:entity id:c3c368d8-6ec0-4064-bcfe-a0c6ebea821c ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/cloud_cover_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.246177"^^xsd:dateTime ;
            prov:entity id:5fc90b70-355b-4773-ab64-068be1b36cdc ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/ndwi_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.246141"^^xsd:dateTime ;
            prov:entity id:c66a4eb4-76b6-4a3d-b5ee-aa35009027e1 ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/ndvi_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-24T12:57:45.246255"^^xsd:dateTime ;
            prov:entity id:068eb4ce-9e22-4f53-8d00-6a22656436bb ;
            prov:hadRole <arcp://uuid,e96466cd-dd6c-469a-af95-6bbc439a3156/workflow/packed.cwl#main/savi_min> ] ;
    prov:startedAtTime "2026-09-24T12:57:44.628413"^^xsd:dateTime .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `estimate_biomass`
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
      const: estimate_biomass
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - ndvi_file
      - ndwi_file
      - savi_file
      - stac_item
      - ndvi_min
      - ndvi_max
      - ndwi_min
      - savi_min
      - biomass_slope
      - biomass_intercept
      - carbon_fraction
      propertyNames:
        enum:
        - ndvi_file
        - ndwi_file
        - savi_file
        - stac_item
        - ndvi_min
        - ndvi_max
        - ndwi_min
        - savi_min
        - biomass_slope
        - biomass_intercept
        - carbon_fraction
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - mangrove_mask_file
      - biomass_file
      - biomass_summary_file
      - carbon_summary_file
      - analysis_summary_file
      propertyNames:
        enum:
        - mangrove_mask_file
        - biomass_file
        - biomass_summary_file
        - carbon_summary_file
        - analysis_summary_file
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
        - ndvi_file
        - ndwi_file
        - savi_file
        - stac_item
        propertyNames:
          enum:
          - ndvi_file
          - ndwi_file
          - savi_file
          - stac_item
          - ndvi_min
          - ndvi_max
          - ndwi_min
          - savi_min
          - biomass_slope
          - biomass_intercept
          - carbon_fraction
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
          - mangrove_mask_file
          - biomass_file
          - biomass_summary_file
          - carbon_summary_file
          - analysis_summary_file
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
      - mangrove_mask_file
      - biomass_file
      - biomass_summary_file
      - carbon_summary_file
      - analysis_summary_file
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/kindgrove-steps/estimate-biomass/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/kindgrove-steps/estimate-biomass`

