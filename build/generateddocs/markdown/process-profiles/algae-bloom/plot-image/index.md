
# Process profile: plot-image (Schema)

`ospd.process-profiles.algae-bloom.plot-image` *v0.1*

OGC API - Processes profile of the CWL CommandLineTool `plot-image` (W1 Algae Bloom), with its provenance view, process-type entry and openEO equivalence.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Process profile of **`plot-image`** (CommandLineTool, W1 Algae Bloom).

> Plots an image with colors.

## Source

- CWL: [plot-image.cwl](https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl) (pinned commit `5edd4ec`, license <https://spdx.org/licenses/CC-BY-NC-SA-4.0>). Referenced, not copied.
- Six-phase position: Export / aggregation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.algae-bloom.workflow-earth-search-process`, `ospd.process-profiles.algae-bloom.workflow-copernicus-process`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `input_image` | File | `output_file` | File |
| `color_scale` | string | `output_plot` | File |
| `output_name` | string? |  |  |
| `plot_name` | string? |  |  |
| `plot_title` | string? |  |  |
| `clip_min` | float? |  |  |
| `clip_max` | float? |  |  |

## Analysis

**Behaviour.** Python/GDAL + matplotlib: applies binned colour scales to a single-band
image, writes a colourised GeoTIFF (`<output_name>.tif`) and a PNG figure (`<plot_name>.png`).

**CWL specifics.** `color_scale` is a JSON array serialised in a `string` (a structured value
hidden in a literal: could be typed as an array of `[number, [r,g,b]]` in the
processDescription, but CWL cannot declare it). Outputs are globbed with
`$(runtime.outdir)/*.tif` / `*.png`, so any extra file would break the step. Output formats
`ogc:geotiff` and `iana:image/png` are dropped by the transform (M-01).

**Provenance.** Two outputs derived from one input; `color_scale` is the parameter that
makes the rendering reproducible.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `c27c60d`, inline variant).

**Manually corrected** (the raw transform output is kept as a separate example):

- M-01/M-02 inputs.input_image: CWL format list ['ogc:geotiff', 'iana:image/tiff', 'iana:image/jp2'] -> oneOf ['image/tiff; application=geotiff', 'image/tiff', 'image/jp2']
- M-01 outputs.output_file: contentMediaType from CWL format `ogc:geotiff` -> `image/tiff; application=geotiff`; contentEncoding binary
- M-01 outputs.output_plot: contentMediaType from CWL format `iana:image/png` -> `image/png`; contentEncoding binary

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `w1-earth-search`: earth-search variant of the pinned W1 package, `cwltool --outdir ./results --provenance ./PROV algae-usecase-workflow-earth-search.cwl example/algae-usecase-job-earth-search.yml`, 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host; two products scattered (S2A_29SPC_20190701_1_L2A then S2A_29SPC_20190701_0_L2A). Three local deviations were needed to run the package at all, none touching the CWL (docs/DEVIATIONS.md U-03, U-04)), activity `main/plot_turbidity_2` (scatter iteration 2, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** Partial: the export part (GeoTIFF + PNG) corresponds to save_result with a GTiff or PNG format; `clip_min`/`clip_max` correspond to math.clip. The colour mapping (`color_scale` bins) and the matplotlib figure (title, colour bar) have no stable openEO process (colour maps are back-end-specific format options).

- `closeMatch`: `ogc.openeo.processes.cubes.save_result`
- `relatedMatch`: `ogc.openeo.processes.math.clip`, `ogc.openeo.processes.math.linear_scale_range`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image` (`ospd.process-profiles.process-type`), status `submitted`.

## Examples

### Source CWL (referenced)
The CWL CommandLineTool is referenced, not copied: <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl>.

### processDescription
OGC API - Processes processDescription derived from the CWL (manually corrected, see description).
#### json
```json
{
  "id": "plot-image",
  "version": "1.0.0",
  "title": "Plots an image with colors.",
  "description": "Applies the specified color mapping with scaled bins to a geospatial image.",
  "mutable": true,
  "keywords": [
    "geospatial",
    "imagery",
    "rendering",
    "visualization",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Plots an image with colors."
    },
    {
      "role": "https://schema.org/description",
      "value": "Applies the specified color mapping with scaled bins to a geospatial image."
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.0.0"
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
    "input_image": {
      "title": "input_image",
      "description": "Image to map with the colors bins.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "binary",
            "contentMediaType": "image/tiff; application=geotiff"
          },
          {
            "type": "string",
            "contentEncoding": "binary",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "binary",
            "contentMediaType": "image/jp2"
          }
        ]
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "color_scale": {
      "title": "Color mappings to bin scales to apply to the image.",
      "description": "JSON-like array with each item being an array of 2 elements, \nthe first for the bin scale value and the second for the RGB color.\nEach RGB value can be either a [0-1] floating point or a [0-255] integer.\n\nExample: '[ [0, [0,0,0]], [20, [0,0,255]], [50, [255,100,0]] ]'\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "output_name": {
      "title": "output_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "output"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_name": {
      "title": "plot_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "plot"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_title": {
      "title": "plot_title",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_min": {
      "title": "clip_min",
      "description": "Clip values below this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_max": {
      "title": "clip_max",
      "description": "Clip values above this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "output_file": {
      "title": "output_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "output_plot": {
      "title": "output_plot",
      "description": "",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "id": "plot-image",
  "version": "1.0.0",
  "title": "Plots an image with colors.",
  "description": "Applies the specified color mapping with scaled bins to a geospatial image.",
  "mutable": true,
  "keywords": [
    "geospatial",
    "imagery",
    "rendering",
    "visualization",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Plots an image with colors."
    },
    {
      "role": "https://schema.org/description",
      "value": "Applies the specified color mapping with scaled bins to a geospatial image."
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.0.0"
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
    "input_image": {
      "title": "input_image",
      "description": "Image to map with the colors bins.",
      "schema": {
        "oneOf": [
          {
            "type": "string",
            "contentEncoding": "binary",
            "contentMediaType": "image/tiff; application=geotiff"
          },
          {
            "type": "string",
            "contentEncoding": "binary",
            "contentMediaType": "image/tiff"
          },
          {
            "type": "string",
            "contentEncoding": "binary",
            "contentMediaType": "image/jp2"
          }
        ]
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "color_scale": {
      "title": "Color mappings to bin scales to apply to the image.",
      "description": "JSON-like array with each item being an array of 2 elements, \nthe first for the bin scale value and the second for the RGB color.\nEach RGB value can be either a [0-1] floating point or a [0-255] integer.\n\nExample: '[ [0, [0,0,0]], [20, [0,0,255]], [50, [255,100,0]] ]'\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "output_name": {
      "title": "output_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "output"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_name": {
      "title": "plot_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "plot"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_title": {
      "title": "plot_title",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_min": {
      "title": "clip_min",
      "description": "Clip values below this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_max": {
      "title": "clip_max",
      "description": "Clip values above this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "output_file": {
      "title": "output_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentEncoding": "binary",
        "contentMediaType": "image/tiff; application=geotiff"
      }
    },
    "output_plot": {
      "title": "output_plot",
      "description": "",
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
@prefix ns1: <http://schema.org/> .
@prefix ns2: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix ns3: <https://w3id.org/ogc/api/schema/> .
@prefix ns4: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/plot-image> dcterms:description "Applies the specified color mapping with scaled bins to a geospatial image." ;
    dcterms:subject "OSPD",
        "demo",
        "geospatial",
        "imagery",
        "rendering",
        "visualization" ;
    dcterms:title "Plots an image with colors." ;
    pp:version "1.0.0" ;
    proc:inputs [ ns2:clip_max [ dcterms:description "Clip values above this threshold for color mapping." ;
                    dcterms:title "clip_max" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns2:clip_min [ dcterms:description "Clip values below this threshold for color mapping." ;
                    dcterms:title "clip_min" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns2:color_scale [ dcterms:description """JSON-like array with each item being an array of 2 elements, 
the first for the bin scale value and the second for the RGB color.
Each RGB value can be either a [0-1] floating point or a [0-255] integer.

Example: '[ [0, [0,0,0]], [20, [0,0,255]], [50, [255,100,0]] ]'
""" ;
                    dcterms:title "Color mappings to bin scales to apply to the image." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns2:input_image [ dcterms:description "Image to map with the colors bins." ;
                    dcterms:title "input_image" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ ns3:oneOf [ proc:type "string" ;
                                    ns3:contentEncoding "binary" ;
                                    ns3:contentMediaType "image/tiff; application=geotiff" ],
                                [ proc:type "string" ;
                                    ns3:contentEncoding "binary" ;
                                    ns3:contentMediaType "image/tiff" ],
                                [ proc:type "string" ;
                                    ns3:contentEncoding "binary" ;
                                    ns3:contentMediaType "image/jp2" ] ] ] ;
            ns2:output_name [ dcterms:description "" ;
                    dcterms:title "output_name" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"output\""^^rdf:JSON ;
                            proc:type "string" ] ] ;
            ns2:plot_name [ dcterms:description "" ;
                    dcterms:title "plot_name" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"plot\""^^rdf:JSON ;
                            proc:type "string" ] ] ;
            ns2:plot_title [ dcterms:description "" ;
                    dcterms:title "plot_title" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ],
        [ rdf:value [ a ns1:Person ;
                    ns1:email "francis.charette-migneault@crim.ca" ;
                    ns1:identifier "http://orcid.org/0000-0003-4862-3349" ;
                    ns1:name "Francis Charette-Migneault" ] ;
            proc:role schema:author ],
        [ rdf:value "Plots an image with colors." ;
            proc:role schema:name ],
        [ rdf:value "https://gitlab.ogc.org/ogc/ogc-ospd" ;
            proc:role schema:codeRepository ],
        [ rdf:value "Applies the specified color mapping with scaled bins to a geospatial image." ;
            proc:role schema:description ],
        [ rdf:value "1.0.0" ;
            proc:role schema:softwareVersion ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns4:output_file [ dcterms:description "" ;
                    dcterms:title "output_file" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/tiff; application=geotiff" ] ] ;
            ns4:output_plot [ dcterms:description "" ;
                    dcterms:title "output_plot" ;
                    proc:schema [ proc:type "string" ;
                            ns3:contentEncoding "binary" ;
                            ns3:contentMediaType "image/png" ] ] ] .


```


### Raw cwl-to-ogcprocess output
Unmodified output of the `eoap.cct.cwl-to-ogcprocess` jq transform.
#### json
```json
{
  "id": "plot-image",
  "version": "1.0.0",
  "title": "Plots an image with colors.",
  "description": "Applies the specified color mapping with scaled bins to a geospatial image.",
  "mutable": true,
  "keywords": [
    "geospatial",
    "imagery",
    "rendering",
    "visualization",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Plots an image with colors."
    },
    {
      "role": "https://schema.org/description",
      "value": "Applies the specified color mapping with scaled bins to a geospatial image."
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.0.0"
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
    "input_image": {
      "title": "input_image",
      "description": "Image to map with the colors bins.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "color_scale": {
      "title": "Color mappings to bin scales to apply to the image.",
      "description": "JSON-like array with each item being an array of 2 elements, \nthe first for the bin scale value and the second for the RGB color.\nEach RGB value can be either a [0-1] floating point or a [0-255] integer.\n\nExample: '[ [0, [0,0,0]], [20, [0,0,255]], [50, [255,100,0]] ]'\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "output_name": {
      "title": "output_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "output"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_name": {
      "title": "plot_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "plot"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_title": {
      "title": "plot_title",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_min": {
      "title": "clip_min",
      "description": "Clip values below this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_max": {
      "title": "clip_max",
      "description": "Clip values above this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "output_file": {
      "title": "output_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "output_plot": {
      "title": "output_plot",
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
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "id": "plot-image",
  "version": "1.0.0",
  "title": "Plots an image with colors.",
  "description": "Applies the specified color mapping with scaled bins to a geospatial image.",
  "mutable": true,
  "keywords": [
    "geospatial",
    "imagery",
    "rendering",
    "visualization",
    "OSPD",
    "demo"
  ],
  "metadata": [
    {
      "role": "https://schema.org/name",
      "value": "Plots an image with colors."
    },
    {
      "role": "https://schema.org/description",
      "value": "Applies the specified color mapping with scaled bins to a geospatial image."
    },
    {
      "role": "https://schema.org/softwareVersion",
      "value": "1.0.0"
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
    "input_image": {
      "title": "input_image",
      "description": "Image to map with the colors bins.",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "color_scale": {
      "title": "Color mappings to bin scales to apply to the image.",
      "description": "JSON-like array with each item being an array of 2 elements, \nthe first for the bin scale value and the second for the RGB color.\nEach RGB value can be either a [0-1] floating point or a [0-255] integer.\n\nExample: '[ [0, [0,0,0]], [20, [0,0,255]], [50, [255,100,0]] ]'\n",
      "schema": {
        "type": "string"
      },
      "minOccurs": 1,
      "maxOccurs": 1
    },
    "output_name": {
      "title": "output_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "output"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_name": {
      "title": "plot_name",
      "description": "",
      "schema": {
        "type": "string",
        "default": "plot"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "plot_title": {
      "title": "plot_title",
      "description": "",
      "schema": {
        "type": "string"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_min": {
      "title": "clip_min",
      "description": "Clip values below this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    },
    "clip_max": {
      "title": "clip_max",
      "description": "Clip values above this threshold for color mapping.",
      "schema": {
        "type": "number"
      },
      "minOccurs": 0,
      "maxOccurs": 1
    }
  },
  "outputs": {
    "output_file": {
      "title": "output_file",
      "description": "",
      "schema": {
        "type": "string",
        "contentMediaType": "application/octet-stream"
      }
    },
    "output_plot": {
      "title": "output_plot",
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
@prefix ns2: <http://schema.org/> .
@prefix ns3: <https://geolabs.github.io/bblocks-process-profiles/def/output/> .
@prefix ns4: <https://w3id.org/ogc/api/schema/> .
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/plot-image> dcterms:description "Applies the specified color mapping with scaled bins to a geospatial image." ;
    dcterms:subject "OSPD",
        "demo",
        "geospatial",
        "imagery",
        "rendering",
        "visualization" ;
    dcterms:title "Plots an image with colors." ;
    pp:version "1.0.0" ;
    proc:inputs [ ns1:clip_max [ dcterms:description "Clip values above this threshold for color mapping." ;
                    dcterms:title "clip_max" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns1:clip_min [ dcterms:description "Clip values below this threshold for color mapping." ;
                    dcterms:title "clip_min" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "number" ] ] ;
            ns1:color_scale [ dcterms:description """JSON-like array with each item being an array of 2 elements, 
the first for the bin scale value and the second for the RGB color.
Each RGB value can be either a [0-1] floating point or a [0-255] integer.

Example: '[ [0, [0,0,0]], [20, [0,0,255]], [50, [255,100,0]] ]'
""" ;
                    dcterms:title "Color mappings to bin scales to apply to the image." ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ] ] ;
            ns1:input_image [ dcterms:description "Image to map with the colors bins." ;
                    dcterms:title "input_image" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 1 ;
                    proc:schema [ proc:type "string" ;
                            ns4:contentMediaType "application/octet-stream" ] ] ;
            ns1:output_name [ dcterms:description "" ;
                    dcterms:title "output_name" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"output\""^^rdf:JSON ;
                            proc:type "string" ] ] ;
            ns1:plot_name [ dcterms:description "" ;
                    dcterms:title "plot_name" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:default "\"plot\""^^rdf:JSON ;
                            proc:type "string" ] ] ;
            ns1:plot_title [ dcterms:description "" ;
                    dcterms:title "plot_title" ;
                    proc:maxOccurs 1 ;
                    proc:minOccurs 0 ;
                    proc:schema [ proc:type "string" ] ] ] ;
    proc:jobControlOptions "async-execute" ;
    proc:metadata [ rdf:value [ a ns2:Person ;
                    ns2:email "francis.charette-migneault@crim.ca" ;
                    ns2:identifier "http://orcid.org/0000-0003-4862-3349" ;
                    ns2:name "Francis Charette-Migneault" ] ;
            proc:role schema:author ],
        [ rdf:value "Plots an image with colors." ;
            proc:role schema:name ],
        [ rdf:value "1.0.0" ;
            proc:role schema:softwareVersion ],
        [ rdf:value "https://gitlab.ogc.org/ogc/ogc-ospd" ;
            proc:role schema:codeRepository ],
        [ rdf:value "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ;
            proc:role schema:license ],
        [ rdf:value "Applies the specified color mapping with scaled bins to a geospatial image." ;
            proc:role schema:description ] ;
    proc:mutable true ;
    proc:outputTransmission "reference",
        "value" ;
    proc:outputs [ ns3:output_file [ dcterms:description "" ;
                    dcterms:title "output_file" ;
                    proc:schema [ proc:type "string" ;
                            ns4:contentMediaType "application/octet-stream" ] ] ;
            ns3:output_plot [ dcterms:description "" ;
                    dcterms:title "output_plot" ;
                    proc:schema [ proc:type "string" ;
                            ns4:contentMediaType "application/octet-stream" ] ] ] .


```


### OGC Application Package (deploy)
Part 2 deploy body: the execution unit is a link to the pinned CWL.
#### json
```json
{
  "processDescription": {
    "process": {
      "id": "plot-image",
      "version": "1.0.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "processDescription": {
    "process": {
      "id": "plot-image",
      "version": "1.0.0"
    }
  },
  "executionUnit": {
    "href": "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl",
    "type": "application/cwl+yaml",
    "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

<https://geolabs.github.io/bblocks-process-profiles/def/process/plot-image> pp:version "1.0.0" .

[] pp:processDescription [ pp:process <https://geolabs.github.io/bblocks-process-profiles/def/process/plot-image> ] ;
    proc:executionUnit [ a <https://geolabs.github.io/bblocks-process-profiles/def/application/cwl+yaml> ;
            pp:href "https://github.com/crim-ca/ogc-ospd-phase1/raw/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl" ;
            pp:rel "http://www.opengis.net/def/rel/ogc/1.0/executionUnit" ] .


```


### Execute request
#### json
```json
{
  "inputs": {
    "input_image": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    },
    "color_scale": "[[0,[73,111,242]],[4,[130,211,95]],[8,[254,253,5]],[12,[253,0,4]],[16,[142,32,38]],[20,[217,124,245]]]",
    "output_name": "S2A_29SPC_20190701_0_L2A_turbidity_color",
    "plot_name": "S2A_29SPC_20190701_0_L2A_turbidity_plot",
    "plot_title": "Turbidity"
  },
  "response": "document"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "inputs": {
    "input_image": {
      "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
      "type": "image/tiff; application=geotiff"
    },
    "color_scale": "[[0,[73,111,242]],[4,[130,211,95]],[8,[254,253,5]],[12,[253,0,4]],[16,[142,32,38]],[20,[217,124,245]]]",
    "output_name": "S2A_29SPC_20190701_0_L2A_turbidity_color",
    "plot_name": "S2A_29SPC_20190701_0_L2A_turbidity_plot",
    "plot_title": "Turbidity"
  },
  "response": "document"
}
```

#### ttl
```ttl
@prefix ns1: <https://geolabs.github.io/bblocks-process-profiles/def/input/> .
@prefix proc: <https://w3id.org/ogc/api/processes/> .

[] proc:inputs [ ns1:color_scale "[[0,[73,111,242]],[4,[130,211,95]],[8,[254,253,5]],[12,[253,0,4]],[16,[142,32,38]],[20,[217,124,245]]]" ;
            ns1:input_image [ ns1:href "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff" ;
                    proc:type "image/tiff; application=geotiff" ] ;
            ns1:output_name "S2A_29SPC_20190701_0_L2A_turbidity_color" ;
            ns1:plot_name "S2A_29SPC_20190701_0_L2A_turbidity_plot" ;
            ns1:plot_title "Turbidity" ] ;
    proc:response "document" .


```


### Results
#### json
```json
{
  "output_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "output_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
    "type": "image/png"
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "output_file": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
    "type": "image/tiff; application=geotiff"
  },
  "output_plot": {
    "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
    "type": "image/png"
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .

[] pp:output_file [ pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif" ] ;
    pp:output_plot [ a <https://geolabs.github.io/bblocks-process-profiles/def/image/png> ;
            pp:href "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png" ] .


```


### Provenance view (generic provenance profile)
W3C PROV chain validated against `ogc.bbr.provenance.provenance`.
#### json
```json
[
  {
    "id": "urn:example:run:algae-bloom:plot-image",
    "provType": "prov:Activity",
    "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image",
    "startedAtTime": "2026-09-23T06:40:29Z",
    "used": [
      "urn:example:entity:plot-image:in:input_image",
      "urn:example:entity:plot-image:in:color_scale",
      "urn:example:entity:plot-image:in:output_name",
      "urn:example:entity:plot-image:in:plot_name",
      "urn:example:entity:plot-image:in:plot_title"
    ],
    "wasAssociatedWith": [
      "urn:example:engine:cwltool-3.1.20260108082145",
      "urn:example:image:ogc-ospd/algae-usecase/plot-image:1.0.0"
    ],
    "qualifiedAssociation": [
      {
        "agent": "urn:example:engine:cwltool-3.1.20260108082145",
        "hadPlan": "https://ospd.example.org/ogc-api/processes/plot-image"
      }
    ],
    "endedAtTime": "2026-09-23T06:40:32Z"
  },
  {
    "id": "urn:example:entity:plot-image:in:input_image",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/input_image",
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ]
  },
  {
    "id": "urn:example:entity:plot-image:in:color_scale",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/color_scale",
    "value": "[[0,[73,111,242]],[4,[130,211,95]],[8,[254,253,5]],[12,[253,0,4]],[16,[142,32,38]],[20,[217,124,245]]]"
  },
  {
    "id": "urn:example:entity:plot-image:in:output_name",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/output_name",
    "value": "S2A_29SPC_20190701_0_L2A_turbidity_color"
  },
  {
    "id": "urn:example:entity:plot-image:in:plot_name",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/plot_name",
    "value": "S2A_29SPC_20190701_0_L2A_turbidity_plot"
  },
  {
    "id": "urn:example:entity:plot-image:in:plot_title",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/plot_title",
    "value": "Turbidity"
  },
  {
    "id": "urn:example:entity:plot-image:out:output_file",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#outputs/output_file",
    "wasGeneratedBy": "urn:example:run:algae-bloom:plot-image",
    "wasDerivedFrom": [
      "urn:example:entity:plot-image:in:input_image"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
        "rel": "item",
        "type": "image/tiff; application=geotiff"
      }
    ],
    "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
  },
  {
    "id": "urn:example:entity:plot-image:out:output_plot",
    "provType": "prov:Entity",
    "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#outputs/output_plot",
    "wasGeneratedBy": "urn:example:run:algae-bloom:plot-image",
    "wasDerivedFrom": [
      "urn:example:entity:plot-image:in:input_image"
    ],
    "links": [
      {
        "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
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
  },
  {
    "id": "urn:example:image:ogc-ospd/algae-usecase/plot-image:1.0.0",
    "provType": "prov:SoftwareAgent",
    "name": "container image ogc-ospd/algae-usecase/plot-image:1.0.0"
  }
]

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "@graph": [
    {
      "id": "urn:example:run:algae-bloom:plot-image",
      "provType": "prov:Activity",
      "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image",
      "startedAtTime": "2026-09-23T06:40:29Z",
      "used": [
        "urn:example:entity:plot-image:in:input_image",
        "urn:example:entity:plot-image:in:color_scale",
        "urn:example:entity:plot-image:in:output_name",
        "urn:example:entity:plot-image:in:plot_name",
        "urn:example:entity:plot-image:in:plot_title"
      ],
      "wasAssociatedWith": [
        "urn:example:engine:cwltool-3.1.20260108082145",
        "urn:example:image:ogc-ospd/algae-usecase/plot-image:1.0.0"
      ],
      "qualifiedAssociation": [
        {
          "agent": "urn:example:engine:cwltool-3.1.20260108082145",
          "hadPlan": "https://ospd.example.org/ogc-api/processes/plot-image"
        }
      ],
      "endedAtTime": "2026-09-23T06:40:32Z"
    },
    {
      "id": "urn:example:entity:plot-image:in:input_image",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/input_image",
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ]
    },
    {
      "id": "urn:example:entity:plot-image:in:color_scale",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/color_scale",
      "value": "[[0,[73,111,242]],[4,[130,211,95]],[8,[254,253,5]],[12,[253,0,4]],[16,[142,32,38]],[20,[217,124,245]]]"
    },
    {
      "id": "urn:example:entity:plot-image:in:output_name",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/output_name",
      "value": "S2A_29SPC_20190701_0_L2A_turbidity_color"
    },
    {
      "id": "urn:example:entity:plot-image:in:plot_name",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/plot_name",
      "value": "S2A_29SPC_20190701_0_L2A_turbidity_plot"
    },
    {
      "id": "urn:example:entity:plot-image:in:plot_title",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#inputs/plot_title",
      "value": "Turbidity"
    },
    {
      "id": "urn:example:entity:plot-image:out:output_file",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#outputs/output_file",
      "wasGeneratedBy": "urn:example:run:algae-bloom:plot-image",
      "wasDerivedFrom": [
        "urn:example:entity:plot-image:in:input_image"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif",
          "rel": "item",
          "type": "image/tiff; application=geotiff"
        }
      ],
      "wasAttributedTo": "urn:example:engine:cwltool-3.1.20260108082145"
    },
    {
      "id": "urn:example:entity:plot-image:out:output_plot",
      "provType": "prov:Entity",
      "entityType": "https://ospd.example.org/ogc-api/processes/plot-image#outputs/output_plot",
      "wasGeneratedBy": "urn:example:run:algae-bloom:plot-image",
      "wasDerivedFrom": [
        "urn:example:entity:plot-image:in:input_image"
      ],
      "links": [
        {
          "href": "https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png",
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
    },
    {
      "id": "urn:example:image:ogc-ospd/algae-usecase/plot-image:1.0.0",
      "provType": "prov:SoftwareAgent",
      "name": "container image ogc-ospd/algae-usecase/plot-image:1.0.0"
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

<urn:example:entity:plot-image:out:output_file> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/plot-image#outputs/output_file> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_color.tif> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:plot-image:in:input_image> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:plot-image> .

<urn:example:entity:plot-image:out:output_plot> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/plot-image#outputs/output_plot> ;
    rdfs:seeAlso [ dcterms:type "image/png" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/algae-bloom-plot-image-0001/results/S2A_29SPC_20190701_0_L2A_turbidity_plot.png> ] ;
    prov:wasAttributedTo <urn:example:engine:cwltool-3.1.20260108082145> ;
    prov:wasDerivedFrom <urn:example:entity:plot-image:in:input_image> ;
    prov:wasGeneratedBy <urn:example:run:algae-bloom:plot-image> .

<urn:example:entity:plot-image:in:color_scale> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/plot-image#inputs/color_scale> ;
    rdf:value "[[0,[73,111,242]],[4,[130,211,95]],[8,[254,253,5]],[12,[253,0,4]],[16,[142,32,38]],[20,[217,124,245]]]" .

<urn:example:entity:plot-image:in:output_name> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/plot-image#inputs/output_name> ;
    rdf:value "S2A_29SPC_20190701_0_L2A_turbidity_color" .

<urn:example:entity:plot-image:in:plot_name> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/plot-image#inputs/plot_name> ;
    rdf:value "S2A_29SPC_20190701_0_L2A_turbidity_plot" .

<urn:example:entity:plot-image:in:plot_title> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/plot-image#inputs/plot_title> ;
    rdf:value "Turbidity" .

<urn:example:image:ogc-ospd/algae-usecase/plot-image:1.0.0> a prov:SoftwareAgent ;
    pp:name "container image ogc-ospd/algae-usecase/plot-image:1.0.0" .

<urn:example:run:algae-bloom:plot-image> a prov:Activity,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image> ;
    prov:endedAtTime "2026-09-23T06:40:32+00:00"^^xsd:dateTime ;
    prov:qualifiedAssociation [ prov:agent <urn:example:engine:cwltool-3.1.20260108082145> ;
            prov:hadPlan <https://ospd.example.org/ogc-api/processes/plot-image> ] ;
    prov:startedAtTime "2026-09-23T06:40:29+00:00"^^xsd:dateTime ;
    prov:used <urn:example:entity:plot-image:in:color_scale>,
        <urn:example:entity:plot-image:in:input_image>,
        <urn:example:entity:plot-image:in:output_name>,
        <urn:example:entity:plot-image:in:plot_name>,
        <urn:example:entity:plot-image:in:plot_title> ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145>,
        <urn:example:image:ogc-ospd/algae-usecase/plot-image:1.0.0> .

<urn:example:entity:plot-image:in:input_image> a prov:Entity,
        <https://ospd.example.org/ogc-api/processes/plot-image#inputs/input_image> ;
    rdfs:seeAlso [ dcterms:type "image/tiff; application=geotiff" ;
            ns1:relation <http://www.iana.org/assignments/relation/item> ;
            oa:hasTarget <https://ospd.example.org/ogc-api/jobs/upstream-step/results/S2A_29SPC_20190701_0_L2A_turbidity.tiff> ] .

<urn:example:engine:cwltool-3.1.20260108082145> a prov:SoftwareAgent ;
    pp:name "cwltool 3.1.20260108082145" .


```


### Process run (wfprov:ProcessRun, gap GP-1)
#### json
```json
{
  "id": "urn:example:run:algae-bloom:plot-image",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/plot-image",
  "usedInput": [
    {
      "id": "urn:example:entity:plot-image:in:input_image"
    },
    {
      "id": "urn:example:entity:plot-image:in:color_scale"
    },
    {
      "id": "urn:example:entity:plot-image:in:output_name"
    },
    {
      "id": "urn:example:entity:plot-image:in:plot_name"
    },
    {
      "id": "urn:example:entity:plot-image:in:plot_title"
    }
  ],
  "startedAtTime": "2026-09-23T06:40:29Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:algae-bloom:workflow-earth-search-process"
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "id": "urn:example:run:algae-bloom:plot-image",
  "type": "ProcessRun",
  "activityType": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image",
  "describedByProcess": "https://ospd.example.org/ogc-api/processes/plot-image",
  "usedInput": [
    {
      "id": "urn:example:entity:plot-image:in:input_image"
    },
    {
      "id": "urn:example:entity:plot-image:in:color_scale"
    },
    {
      "id": "urn:example:entity:plot-image:in:output_name"
    },
    {
      "id": "urn:example:entity:plot-image:in:plot_name"
    },
    {
      "id": "urn:example:entity:plot-image:in:plot_title"
    }
  ],
  "startedAtTime": "2026-09-23T06:40:29Z",
  "wasEnactedBy": "urn:example:engine:cwltool-3.1.20260108082145",
  "wasPartOfWorkflowRun": "urn:example:run:algae-bloom:workflow-earth-search-process"
}
```

#### ttl
```ttl
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:example:run:algae-bloom:plot-image> a wfprov:ProcessRun,
        <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image> ;
    wfprov:describedByProcess <https://ospd.example.org/ogc-api/processes/plot-image> ;
    wfprov:usedInput <urn:example:entity:plot-image:in:color_scale>,
        <urn:example:entity:plot-image:in:input_image>,
        <urn:example:entity:plot-image:in:output_name>,
        <urn:example:entity:plot-image:in:plot_name>,
        <urn:example:entity:plot-image:in:plot_title> ;
    wfprov:wasPartOfWorkflowRun <urn:example:run:algae-bloom:workflow-earth-search-process> ;
    prov:startedAtTime "2026-09-23T06:40:29+00:00"^^xsd:dateTime ;
    prov:wasAssociatedWith <urn:example:engine:cwltool-3.1.20260108082145> .


```


### Process-type register entry (Activity 4)
#### json
```json
{
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image",
  "type": "ProcessType",
  "prefLabel": "Plots an image with colors.",
  "definition": "Applies the specified color mapping with scaled bins to a geospatial image.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.algae-bloom.plot-image",
  "processDescription": {
    "id": "plot-image",
    "version": "1.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "plot-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result"
  ],
  "relatedMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.clip",
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.linear_scale_range"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Partial: the export part (GeoTIFF + PNG) corresponds to save_result with a GTiff or PNG format; `clip_min`/`clip_max` correspond to math.clip. The colour mapping (`color_scale` bins) and the matplotlib figure (title, colour bar) have no stable openEO process (colour maps are back-end-specific format options)."
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld",
  "id": "https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image",
  "type": "ProcessType",
  "prefLabel": "Plots an image with colors.",
  "definition": "Applies the specified color mapping with scaled bins to a geospatial image.",
  "inScheme": "https://geolabs.github.io/bblocks-process-profiles/def/process-type",
  "status": "submitted",
  "phase": [
    "https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation"
  ],
  "profile": "ospd.process-profiles.algae-bloom.plot-image",
  "processDescription": {
    "id": "plot-image",
    "version": "1.0.0"
  },
  "source": {
    "cwl": "https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl",
    "cwlClass": "CommandLineTool",
    "cwlId": "plot-image",
    "license": "https://spdx.org/licenses/CC-BY-NC-SA-4.0"
  },
  "provenanceClass": "http://purl.org/wf4ever/wfprov#ProcessRun",
  "cctDependencies": [],
  "candidateCctDependencies": [],
  "closeMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result"
  ],
  "relatedMatch": [
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.clip",
    "https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.linear_scale_range"
  ],
  "openeoEquivalence": {
    "level": "closeMatch",
    "rationale": "Partial: the export part (GeoTIFF + PNG) corresponds to save_result with a GTiff or PNG format; `clip_min`/`clip_max` correspond to math.clip. The colour mapping (`color_scale` bins) and the matplotlib figure (title, colour bar) have no stable openEO process (colour maps are back-end-specific format options)."
  }
}
```

#### ttl
```ttl
@prefix pp: <https://geolabs.github.io/bblocks-process-profiles/def/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix wfprov: <http://purl.org/wf4ever/wfprov#> .

<https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/plot-image> a skos:Concept ;
    skos:broader <https://geolabs.github.io/bblocks-process-profiles/def/phase/export-aggregation> ;
    skos:closeMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.cubes.save_result> ;
    skos:definition "Applies the specified color mapping with scaled bins to a geospatial image." ;
    skos:inScheme pp:process-type ;
    skos:prefLabel "Plots an image with colors." ;
    skos:relatedMatch <https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.clip>,
        <https://www.opengis.net/def/bblocks/ogc.openeo.processes.math.linear_scale_range> ;
    pp:openeoEquivalence [ pp:equivalenceLevel "closeMatch" ;
            pp:rationale "Partial: the export part (GeoTIFF + PNG) corresponds to save_result with a GTiff or PNG format; `clip_min`/`clip_max` correspond to math.clip. The colour mapping (`color_scale` bins) and the matplotlib figure (title, colour bar) have no stable openEO process (colour maps are back-end-specific format options)." ] ;
    pp:processDescription <https://geolabs.github.io/bblocks-process-profiles/def/process/plot-image> ;
    pp:profile "ospd.process-profiles.algae-bloom.plot-image" ;
    pp:provenanceClass wfprov:ProcessRun ;
    pp:source [ pp:cwl <https://github.com/crim-ca/ogc-ospd-phase1/blob/5edd4ec4cbd21e5fceb7c3f4b6c5d0ce809a57ea/ogc_app_pkg/plot-image.cwl> ;
            pp:cwlClass "CommandLineTool" ;
            pp:cwlId "plot-image" ;
            pp:license "https://spdx.org/licenses/CC-BY-NC-SA-4.0" ] ;
    pp:status "submitted" .

<https://geolabs.github.io/bblocks-process-profiles/def/process/plot-image> pp:version "1.0.0" .


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
      "@id": "id:d9639ebc-984b-431c-a823-05a86eb32fb5",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:ee2b4489-574c-40d5-b36c-b1e9afeb669b",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:0b700855-69e1-4836-9881-4bc2cd023102",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:43debe24-70e3-4566-871e-889b76d6357b",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:9a6bba8a-cc4d-46f8-9374-cf7e4f42608e",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/reproject-image"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/reproject-image"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:f24c1565-ee7f-4d30-9e3e-f439a7d3df25",
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
      "@id": "id:c3a912fe-4417-4bd1-81a8-95e5654f7532",
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
      "@id": "id:10162287-984a-45d3-883f-c473d1b9f4e8",
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
      "@id": "id:a541ab4e-c3d9-4a7f-9b05-fa686586b70f",
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
      "@id": "id:ab87aed1-ceb2-4bf2-9ab2-f5e5de480e7e",
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
      "@id": "id:780ec89d-f9bc-4d68-a37b-36bb3230bca9",
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
      "@id": "id:b1a07bb1-efbb-400e-8886-bb197dbe7345",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:7e607c5d-519f-412b-9070-e1bcbc762376",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:b6170213-9472-4118-a656-1c72592c233b",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:fc7a1f11-3e40-431c-af77-7523c1e37baf",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:fcd270b7-0276-4c6d-b13d-35cb00865823",
      "type": [
        "prov:SoftwareAgent"
      ],
      "cwlprov:image": [
        {
          "@value": "ogc-ospd/algae-usecase/reproject-image"
        }
      ],
      "label": [
        {
          "@value": "Container execution of image ogc-ospd/algae-usecase/reproject-image"
        }
      ]
    },
    {
      "@type": "Agent",
      "@id": "id:0c872b6c-8902-4cfb-a981-8a8d16ca84cc",
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
      "@id": "id:8c44a324-28dd-427d-9f64-6569ea486f8e",
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
      "@id": "id:67aa2703-a2a1-434d-9a49-072e268b1de7",
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
      "@id": "id:88f4398b-bad2-4419-8b31-21a7b0d29e51",
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
      "@id": "id:15e3229d-5bd8-408e-a96a-da5e4356b8d0",
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
      "@id": "id:31508f5e-88d5-4a9b-b917-e0cc6dbe47ec",
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
      "activity": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "starter": "id:9e986cfd-629d-41cf-9c75-eb65ae428d71",
      "time": "2026-09-23T08:26:24.435717"
    },
    {
      "@type": "Start",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "starter": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "time": "2026-09-23T08:26:24.435762"
    },
    {
      "@type": "Start",
      "activity": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:26:25.904018"
    },
    {
      "@type": "Start",
      "activity": "id:94486889-f9f5-43d5-b151-995baade6da8",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:27:22.563012"
    },
    {
      "@type": "Start",
      "activity": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:28:17.508715"
    },
    {
      "@type": "Start",
      "activity": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:29:35.440239"
    },
    {
      "@type": "Start",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:29:43.354293"
    },
    {
      "@type": "Start",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:29:45.564470"
    },
    {
      "@type": "Start",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:30:02.101602"
    },
    {
      "@type": "Start",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:31:51.394989"
    },
    {
      "@type": "Start",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:32.394913"
    },
    {
      "@type": "Start",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:34.726244"
    },
    {
      "@type": "Start",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:37.443398"
    },
    {
      "@type": "Start",
      "activity": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.369662"
    },
    {
      "@type": "Start",
      "activity": "id:cb365be4-5b82-466e-a735-52203624488b",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:36:40.025061"
    },
    {
      "@type": "Start",
      "activity": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:38:35.866253"
    },
    {
      "@type": "Start",
      "activity": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:33.178483"
    },
    {
      "@type": "Start",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:37.327471"
    },
    {
      "@type": "Start",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:38.367140"
    },
    {
      "@type": "Start",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:45.590645"
    },
    {
      "@type": "Start",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:46.623486"
    },
    {
      "@type": "Start",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:28.567857"
    },
    {
      "@type": "Start",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:29.608049"
    },
    {
      "@type": "Start",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "starter": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:32.111555"
    },
    {
      "@type": "Activity",
      "@id": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "startTime": "2026-09-23T08:26:24.435738",
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
      "@id": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
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
      "@id": "id:94486889-f9f5-43d5-b151-995baade6da8",
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
      "@id": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
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
      "@id": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
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
      "@id": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/reproject_b03_60m"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
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
      "@id": "id:af841592-5838-42f8-aa5d-95146384bc26",
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
      "@id": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
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
      "@id": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
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
      "@id": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
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
      "@id": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
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
      "@type": "Activity",
      "@id": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b04_10m_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:cb365be4-5b82-466e-a735-52203624488b",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b03_10m_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b02_10m_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/download_b01_60m_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/reproject_b03_60m_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/calculate_cyanobacteria_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:76594558-3301-40b6-b667-368e942831f2",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/calculate_chlorophyll_a_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/plot_cyanobacteria_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/calculate_turbidity_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/plot_turbidity_2"
        }
      ]
    },
    {
      "@type": "Activity",
      "@id": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "type": [
        "wfprov:ProcessRun"
      ],
      "label": [
        {
          "@value": "Run of workflow/packed.cwl#main/plot_chlorophyll_a_2"
        }
      ]
    },
    {
      "@type": "Association",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main"
    },
    {
      "@type": "Association",
      "activity": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b04_10m"
    },
    {
      "@type": "Association",
      "activity": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
      "agent": "id:d9639ebc-984b-431c-a823-05a86eb32fb5"
    },
    {
      "@type": "Association",
      "activity": "id:94486889-f9f5-43d5-b151-995baade6da8",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b03_10m"
    },
    {
      "@type": "Association",
      "activity": "id:94486889-f9f5-43d5-b151-995baade6da8",
      "agent": "id:ee2b4489-574c-40d5-b36c-b1e9afeb669b"
    },
    {
      "@type": "Association",
      "activity": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b02_10m"
    },
    {
      "@type": "Association",
      "activity": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
      "agent": "id:0b700855-69e1-4836-9881-4bc2cd023102"
    },
    {
      "@type": "Association",
      "activity": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b01_60m"
    },
    {
      "@type": "Association",
      "activity": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
      "agent": "id:43debe24-70e3-4566-871e-889b76d6357b"
    },
    {
      "@type": "Association",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/reproject_b03_60m"
    },
    {
      "@type": "Association",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "agent": "id:9a6bba8a-cc4d-46f8-9374-cf7e4f42608e"
    },
    {
      "@type": "Association",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/calculate_cyanobacteria"
    },
    {
      "@type": "Association",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "agent": "id:f24c1565-ee7f-4d30-9e3e-f439a7d3df25"
    },
    {
      "@type": "Association",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/calculate_chlorophyll_a"
    },
    {
      "@type": "Association",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "agent": "id:c3a912fe-4417-4bd1-81a8-95e5654f7532"
    },
    {
      "@type": "Association",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/plot_cyanobacteria"
    },
    {
      "@type": "Association",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "agent": "id:10162287-984a-45d3-883f-c473d1b9f4e8"
    },
    {
      "@type": "Association",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/calculate_turbidity"
    },
    {
      "@type": "Association",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "agent": "id:a541ab4e-c3d9-4a7f-9b05-fa686586b70f"
    },
    {
      "@type": "Association",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/plot_turbidity"
    },
    {
      "@type": "Association",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "agent": "id:ab87aed1-ceb2-4bf2-9ab2-f5e5de480e7e"
    },
    {
      "@type": "Association",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/plot_chlorophyll_a"
    },
    {
      "@type": "Association",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "agent": "id:780ec89d-f9bc-4d68-a37b-36bb3230bca9"
    },
    {
      "@type": "Association",
      "activity": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b04_10m_2"
    },
    {
      "@type": "Association",
      "activity": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "agent": "id:b1a07bb1-efbb-400e-8886-bb197dbe7345"
    },
    {
      "@type": "Association",
      "activity": "id:cb365be4-5b82-466e-a735-52203624488b",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b03_10m_2"
    },
    {
      "@type": "Association",
      "activity": "id:cb365be4-5b82-466e-a735-52203624488b",
      "agent": "id:7e607c5d-519f-412b-9070-e1bcbc762376"
    },
    {
      "@type": "Association",
      "activity": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b02_10m_2"
    },
    {
      "@type": "Association",
      "activity": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "agent": "id:b6170213-9472-4118-a656-1c72592c233b"
    },
    {
      "@type": "Association",
      "activity": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/download_b01_60m_2"
    },
    {
      "@type": "Association",
      "activity": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "agent": "id:fc7a1f11-3e40-431c-af77-7523c1e37baf"
    },
    {
      "@type": "Association",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/reproject_b03_60m_2"
    },
    {
      "@type": "Association",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "agent": "id:fcd270b7-0276-4c6d-b13d-35cb00865823"
    },
    {
      "@type": "Association",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/calculate_cyanobacteria_2"
    },
    {
      "@type": "Association",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "agent": "id:0c872b6c-8902-4cfb-a981-8a8d16ca84cc"
    },
    {
      "@type": "Association",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/calculate_chlorophyll_a_2"
    },
    {
      "@type": "Association",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "agent": "id:8c44a324-28dd-427d-9f64-6569ea486f8e"
    },
    {
      "@type": "Association",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/plot_cyanobacteria_2"
    },
    {
      "@type": "Association",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "agent": "id:67aa2703-a2a1-434d-9a49-072e268b1de7"
    },
    {
      "@type": "Association",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/calculate_turbidity_2"
    },
    {
      "@type": "Association",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "agent": "id:88f4398b-bad2-4419-8b31-21a7b0d29e51"
    },
    {
      "@type": "Association",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/plot_turbidity_2"
    },
    {
      "@type": "Association",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "agent": "id:15e3229d-5bd8-408e-a96a-da5e4356b8d0"
    },
    {
      "@type": "Association",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "agent": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "plan": "wf:main/plot_chlorophyll_a_2"
    },
    {
      "@type": "Association",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "agent": "id:31508f5e-88d5-4a9b-b917-e0cc6dbe47ec"
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
          "@value": "wf:main/reproject_b03_60m",
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
          "@value": "wf:main/calculate_turbidity_2",
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
          "@value": "wf:main/download_b04_10m_2",
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
          "@value": "wf:main/reproject_b03_60m_2",
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
          "@value": "wf:main/plot_turbidity_2",
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
          "@value": "wf:main/calculate_cyanobacteria_2",
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
          "@value": "wf:main/download_b03_10m_2",
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
          "@value": "wf:main/download_b02_10m_2",
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
          "@value": "wf:main/plot_chlorophyll_a_2",
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
          "@value": "wf:main/calculate_chlorophyll_a_2",
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
          "@value": "wf:main/download_b01_60m_2",
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
          "@value": "wf:main/plot_cyanobacteria_2",
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
      "@id": "wf:main/calculate_turbidity",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b04_10m",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/reproject_b03_60m",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_turbidity",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/calculate_cyanobacteria",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b03_10m",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b02_10m",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_chlorophyll_a",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/calculate_chlorophyll_a",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b01_60m",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_cyanobacteria",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
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
      "@id": "data:e001557ec06062e8b0a518eaf12927e3d1be14ca",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:4e86d762-9ac6-4702-8818-e66cfd5e6425",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B04.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B04"
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
      "@id": "data:50ebd5e63205cb9f8e4322e56677b021e540e57d",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:374994f9-116d-48a7-9749-2f5d0a21702e",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B03.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B03"
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
      "@id": "data:ff826260056bbe39e685113083a05ab78c07c09a",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:6d7d32e8-319d-4d54-9cb2-1094ccae2bda",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B02.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B02"
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
      "@id": "data:4554c3cf3eb5232e005efba0f52710ebf69238d4",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ac7fbdba-ab57-4cab-92ea-86425e0d72da",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B01.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B01"
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
      "@id": "data:3e70bde01ba4a6db2abce9619d91ad7a7e0db919",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "B03_60m"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:3e70bde01ba4a6db2abce9619d91ad7a7e0db919",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "B03_60m"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:451dd3a3-2e5f-4acf-b930-ad5fcd658419",
      "value": [
        {
          "@value": "60",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:bd2db380-4b87-4d7a-a309-23597ccb9c57",
      "value": [
        {
          "@value": "60",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:b9b1351c-627e-45d6-81a3-1283ea584ec8",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
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
      "@id": "data:d54118937320f8cd7cb6a0673991c14035966fe7",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B03_60m.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B03_60m"
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
      "@id": "data:a71d74edcae981a17e7464331cb2525eeabd9092",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "115530*(((B.astype(float)*C.astype(float))/A.astype(float))**2.38)"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:a71d74edcae981a17e7464331cb2525eeabd9092",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "115530*(((B.astype(float)*C.astype(float))/A.astype(float))**2.38)"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:99bf64d1155bc89e1a330d0cf10036305f65955d",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:5764e8024006b4e2959972b2ed8133b75af135e7",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:32ae8712ff4f8b8b6b34af45257c41c16474dc98",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "id:fc882878-31a6-43ba-88a7-5c51bad2cef3",
      "value": [
        {
          "@value": "100000000000000",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:e5d9b324-0df0-444b-b4d9-4e9ccb71c5a7",
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
      "@id": "data:5cd4c929136b7ccfd44b3e4a9e543eaf5497e074",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:dae6881b456c2247c2fe7bf59cb2d891427f2aec",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot"
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
      "@id": "data:88d67511003f18c13b7cdc982f5796ab5ae261fc",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:876c7b4d7381ac5660a4507292c9324eb295a297",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:337c1d5047de712ebdd9cfe4e5bafaad9ed60ca1",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:f4ad1bd9dbf27a2d94b4320d4ffe146bf714a9d0",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:1a0e4fad40b7e324bd7ae77ac30e69a00173cd35",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_turbidity_plot"
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
      "@id": "data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:c991e2bc239887ca885b02cab5fdae42c90a2889",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:74f86325eb5176eac0be70c602f62dd4be091838",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:714bad22665ac25a2625f9795548244c5862c173",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot"
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
      "@id": "data:fb8e7e26b282372c29a35ac739498699e02006a5",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:38185787e3c54223cfadb4c26c22b126ad624d21",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "wf:main/calculate_turbidity_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b04_10m_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/reproject_b03_60m_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_turbidity_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/calculate_cyanobacteria_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b03_10m_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b02_10m_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_chlorophyll_a_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/calculate_chlorophyll_a_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/download_b01_60m_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
      ]
    },
    {
      "@type": "Entity",
      "@id": "wf:main/plot_cyanobacteria_2",
      "type": [
        "prov:Plan",
        "wfdesc:Process"
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
      "@id": "data:06cc034ead339e3cf5f8262cc8a6a0e293c14680",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:51e7c370-3e40-44ef-9dad-344fdf984f23",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B04.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B04"
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
      "@id": "data:9f9130b688abf761a50ad3c0822794bceda8a4cd",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B03.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B03"
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
      "@id": "data:64ae819f0f702c63421c488fa5ccf3a41b388f94",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:f93b46c9-cd7a-4d57-8c11-1356d6797057",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B02.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B02"
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
      "@id": "data:46cf7f768b4167418c8ecec22d3dc976cf2e969e",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:5811cb86-e667-4b42-bd25-995c414a260e",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B01.tif"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B01"
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
      "@id": "id:5c2f550b-8421-44b9-833c-1f6d2b83155f",
      "value": [
        {
          "@value": "60",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:09792302-bb35-4042-a300-a2e7f2acf386",
      "value": [
        {
          "@value": "60",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:a9c6d5fa-9367-4ae4-b720-41f313d07f4c",
      "type": [
        "prov:Collection",
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e33aada2083b35c0160af06da303c293f90b45cb",
      "type": [
        "wfprov:Artifact"
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab",
      "type": [
        "wf4ever:File",
        "wfprov:Artifact"
      ],
      "cwlprov:basename": [
        {
          "@value": "B03_60m.tiff"
        }
      ],
      "cwlprov:nameroot": [
        {
          "@value": "B03_60m"
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
      "@id": "data:3082a66f519914584a632e0abf36aea5b5961253",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:065539f1417b6c8066de9420c143413de2cbcd97",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:6b318d7d0eb73571432d45252f14693013f68feb",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:6947846b1796dd6e940e390f61208a85f45117b0",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "id:a0bf8c1c-f971-418d-9a40-667bb07dd0c4",
      "value": [
        {
          "@value": "100000000000000",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "id:43a057a2-41ef-4082-bdfb-fb1186385f7d",
      "value": [
        {
          "@value": "1000000",
          "@type": "xsd:int"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:b3573acf1e280c5c49f41a5a84acaedc59c5c096",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:4ea652b7d22b69e0d27d1a1ebce1e624f55373fd",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:3822adba1b42a347ef376f9ac0e7259d0ba82b22",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:592104a468524cd5e063a0e9da39927566853012",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:c50376cb72b65a0dad365279023daa2af7208fc9",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:2219e4fef3bb44cade72f7ef4d71d8d686197932",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:9f3f28fc82add0a4e71340746dfbbf9db167a541",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_turbidity_plot"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:a2beee36554454e4c0090480d062bc893f3ae7cc",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:8088de425841559ae78ca6328ecdf8bb0fe578d4",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:c9795ae1700fc9846a06b4c55a43850d79fc8c37",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:3b70ed18810c540d946d852c94d6c9701138000a",
      "type": [
        "wfprov:Artifact"
      ],
      "value": [
        {
          "@value": "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot"
        }
      ]
    },
    {
      "@type": "Entity",
      "@id": "data:e6874b008b758679af8241dfbfb355b204b131b2",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@id": "data:1224781c8a82490664559a3b2e66fa3e14e09956",
      "type": [
        "wfprov:Artifact"
      ]
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
      "@type": "Usage",
      "activity": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
      "entity": "data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0",
      "time": "2026-09-23T08:26:25.961176",
      "role": [
        "wf:main/download_b04_10m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
      "entity": "data:c80240b036ceef4fdcfb684013f5e78f2fd144e7",
      "time": "2026-09-23T08:26:25.961572",
      "role": [
        "wf:main/download_b04_10m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:94486889-f9f5-43d5-b151-995baade6da8",
      "entity": "data:7c5d11a451cde788be37383d50239d7672a8cb1f",
      "time": "2026-09-23T08:27:22.567887",
      "role": [
        "wf:main/download_b03_10m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:94486889-f9f5-43d5-b151-995baade6da8",
      "entity": "data:c80240b036ceef4fdcfb684013f5e78f2fd144e7",
      "time": "2026-09-23T08:27:22.568133",
      "role": [
        "wf:main/download_b03_10m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
      "entity": "data:36dea452bfe795afb42cf14b59c82a3127598281",
      "time": "2026-09-23T08:28:17.514641",
      "role": [
        "wf:main/download_b02_10m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
      "entity": "data:c80240b036ceef4fdcfb684013f5e78f2fd144e7",
      "time": "2026-09-23T08:28:17.515035",
      "role": [
        "wf:main/download_b02_10m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
      "entity": "data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f",
      "time": "2026-09-23T08:29:35.446827",
      "role": [
        "wf:main/download_b01_60m/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
      "entity": "data:c80240b036ceef4fdcfb684013f5e78f2fd144e7",
      "time": "2026-09-23T08:29:35.447263",
      "role": [
        "wf:main/download_b01_60m/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "entity": "id:374994f9-116d-48a7-9749-2f5d0a21702e",
      "time": "2026-09-23T08:29:43.441694",
      "role": [
        "wf:main/reproject_b03_60m/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "entity": "data:3e70bde01ba4a6db2abce9619d91ad7a7e0db919",
      "time": "2026-09-23T08:29:43.442743",
      "role": [
        "wf:main/reproject_b03_60m/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "entity": "id:b9b1351c-627e-45d6-81a3-1283ea584ec8",
      "time": "2026-09-23T08:29:43.442864",
      "role": [
        "wf:main/reproject_b03_60m/output_resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:43.442889",
      "role": [
        "wf:main/reproject_b03_60m/output_dimensions"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "id:6d7d32e8-319d-4d54-9cb2-1094ccae2bda",
      "time": "2026-09-23T08:29:45.690347",
      "role": [
        "wf:main/calculate_cyanobacteria/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "id:374994f9-116d-48a7-9749-2f5d0a21702e",
      "time": "2026-09-23T08:29:45.690422",
      "role": [
        "wf:main/calculate_cyanobacteria/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "id:4e86d762-9ac6-4702-8818-e66cfd5e6425",
      "time": "2026-09-23T08:29:45.690440",
      "role": [
        "wf:main/calculate_cyanobacteria/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "data:a71d74edcae981a17e7464331cb2525eeabd9092",
      "time": "2026-09-23T08:29:45.691185",
      "role": [
        "wf:main/calculate_cyanobacteria/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "data:99bf64d1155bc89e1a330d0cf10036305f65955d",
      "time": "2026-09-23T08:29:45.691467",
      "role": [
        "wf:main/calculate_cyanobacteria/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691484",
      "role": [
        "wf:main/calculate_cyanobacteria/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691495",
      "role": [
        "wf:main/calculate_cyanobacteria/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691504",
      "role": [
        "wf:main/calculate_cyanobacteria/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691514",
      "role": [
        "wf:main/calculate_cyanobacteria/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691523",
      "role": [
        "wf:main/calculate_cyanobacteria/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691538",
      "role": [
        "wf:main/calculate_cyanobacteria/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691549",
      "role": [
        "wf:main/calculate_cyanobacteria/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691563",
      "role": [
        "wf:main/calculate_cyanobacteria/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691574",
      "role": [
        "wf:main/calculate_cyanobacteria/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691583",
      "role": [
        "wf:main/calculate_cyanobacteria/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691593",
      "role": [
        "wf:main/calculate_cyanobacteria/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691602",
      "role": [
        "wf:main/calculate_cyanobacteria/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691612",
      "role": [
        "wf:main/calculate_cyanobacteria/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691621",
      "role": [
        "wf:main/calculate_cyanobacteria/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691630",
      "role": [
        "wf:main/calculate_cyanobacteria/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691642",
      "role": [
        "wf:main/calculate_cyanobacteria/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691652",
      "role": [
        "wf:main/calculate_cyanobacteria/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691661",
      "role": [
        "wf:main/calculate_cyanobacteria/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691669",
      "role": [
        "wf:main/calculate_cyanobacteria/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691680",
      "role": [
        "wf:main/calculate_cyanobacteria/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691689",
      "role": [
        "wf:main/calculate_cyanobacteria/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691699",
      "role": [
        "wf:main/calculate_cyanobacteria/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:29:45.691707",
      "role": [
        "wf:main/calculate_cyanobacteria/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "id:ac7fbdba-ab57-4cab-92ea-86425e0d72da",
      "time": "2026-09-23T08:30:02.118857",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda",
      "time": "2026-09-23T08:30:02.118918",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "data:c6f40f302effca33768fc256bbb5dedaca044174",
      "time": "2026-09-23T08:30:02.122046",
      "role": [
        "wf:main/calculate_chlorophyll_a/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "data:5764e8024006b4e2959972b2ed8133b75af135e7",
      "time": "2026-09-23T08:30:02.123575",
      "role": [
        "wf:main/calculate_chlorophyll_a/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.123630",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.123656",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.125207",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.125259",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.125284",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.125306",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.125327",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128256",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128391",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128428",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128471",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128499",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128521",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128542",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128563",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128612",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128654",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128682",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128704",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128937",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128973",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.128998",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.129020",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:30:02.130693",
      "role": [
        "wf:main/calculate_chlorophyll_a/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "entity": "id:fc882878-31a6-43ba-88a7-5c51bad2cef3",
      "time": "2026-09-23T08:31:51.721547",
      "role": [
        "wf:main/plot_cyanobacteria/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "entity": "id:e5d9b324-0df0-444b-b4d9-4e9ccb71c5a7",
      "time": "2026-09-23T08:31:51.721670",
      "role": [
        "wf:main/plot_cyanobacteria/clip_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "entity": "data:1370052da0755d73768c0c75500107d3759bcc2d",
      "time": "2026-09-23T08:31:51.723232",
      "role": [
        "wf:main/plot_cyanobacteria/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "entity": "id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be",
      "time": "2026-09-23T08:31:51.723272",
      "role": [
        "wf:main/plot_cyanobacteria/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "entity": "data:5cd4c929136b7ccfd44b3e4a9e543eaf5497e074",
      "time": "2026-09-23T08:31:51.723855",
      "role": [
        "wf:main/plot_cyanobacteria/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "entity": "data:dae6881b456c2247c2fe7bf59cb2d891427f2aec",
      "time": "2026-09-23T08:31:51.724390",
      "role": [
        "wf:main/plot_cyanobacteria/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "entity": "data:4ad2eab867b3280cabc93a14c615ab97b6b6575e",
      "time": "2026-09-23T08:31:51.724705",
      "role": [
        "wf:main/plot_cyanobacteria/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "id:ac7fbdba-ab57-4cab-92ea-86425e0d72da",
      "time": "2026-09-23T08:35:32.407492",
      "role": [
        "wf:main/calculate_turbidity/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda",
      "time": "2026-09-23T08:35:32.407551",
      "role": [
        "wf:main/calculate_turbidity/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "data:81e487db73b1725c362decd3aac3a2c13f86d595",
      "time": "2026-09-23T08:35:32.408385",
      "role": [
        "wf:main/calculate_turbidity/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "data:337c1d5047de712ebdd9cfe4e5bafaad9ed60ca1",
      "time": "2026-09-23T08:35:32.408834",
      "role": [
        "wf:main/calculate_turbidity/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408860",
      "role": [
        "wf:main/calculate_turbidity/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408874",
      "role": [
        "wf:main/calculate_turbidity/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408887",
      "role": [
        "wf:main/calculate_turbidity/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408899",
      "role": [
        "wf:main/calculate_turbidity/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408912",
      "role": [
        "wf:main/calculate_turbidity/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408924",
      "role": [
        "wf:main/calculate_turbidity/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408935",
      "role": [
        "wf:main/calculate_turbidity/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408951",
      "role": [
        "wf:main/calculate_turbidity/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408962",
      "role": [
        "wf:main/calculate_turbidity/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408973",
      "role": [
        "wf:main/calculate_turbidity/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408986",
      "role": [
        "wf:main/calculate_turbidity/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.408998",
      "role": [
        "wf:main/calculate_turbidity/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409010",
      "role": [
        "wf:main/calculate_turbidity/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409022",
      "role": [
        "wf:main/calculate_turbidity/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409036",
      "role": [
        "wf:main/calculate_turbidity/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409047",
      "role": [
        "wf:main/calculate_turbidity/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409060",
      "role": [
        "wf:main/calculate_turbidity/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409072",
      "role": [
        "wf:main/calculate_turbidity/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409084",
      "role": [
        "wf:main/calculate_turbidity/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409101",
      "role": [
        "wf:main/calculate_turbidity/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409113",
      "role": [
        "wf:main/calculate_turbidity/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409127",
      "role": [
        "wf:main/calculate_turbidity/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409139",
      "role": [
        "wf:main/calculate_turbidity/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:32.409150",
      "role": [
        "wf:main/calculate_turbidity/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "entity": "data:2b0824b4ba24b098adc7ce01881499891c48d2ea",
      "time": "2026-09-23T08:35:34.733224",
      "role": [
        "wf:main/plot_turbidity/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "entity": "id:4e6424db-66b9-4389-81ca-0a3040fbfd07",
      "time": "2026-09-23T08:35:34.733267",
      "role": [
        "wf:main/plot_turbidity/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "entity": "data:f4ad1bd9dbf27a2d94b4320d4ffe146bf714a9d0",
      "time": "2026-09-23T08:35:34.733619",
      "role": [
        "wf:main/plot_turbidity/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "entity": "data:1a0e4fad40b7e324bd7ae77ac30e69a00173cd35",
      "time": "2026-09-23T08:35:34.733930",
      "role": [
        "wf:main/plot_turbidity/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "entity": "data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c",
      "time": "2026-09-23T08:35:34.735472",
      "role": [
        "wf:main/plot_turbidity/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:34.735498",
      "role": [
        "wf:main/plot_turbidity/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:34.735513",
      "role": [
        "wf:main/plot_turbidity/clip_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "entity": "data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8",
      "time": "2026-09-23T08:35:37.462789",
      "role": [
        "wf:main/plot_chlorophyll_a/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "entity": "id:12b49a35-ae72-4b3d-933e-b2d03c6692b4",
      "time": "2026-09-23T08:35:37.463473",
      "role": [
        "wf:main/plot_chlorophyll_a/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "entity": "data:74f86325eb5176eac0be70c602f62dd4be091838",
      "time": "2026-09-23T08:35:37.464939",
      "role": [
        "wf:main/plot_chlorophyll_a/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "entity": "data:714bad22665ac25a2625f9795548244c5862c173",
      "time": "2026-09-23T08:35:37.467615",
      "role": [
        "wf:main/plot_chlorophyll_a/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "entity": "data:e059662a461e5d1b245f555149febc699f42b537",
      "time": "2026-09-23T08:35:37.469223",
      "role": [
        "wf:main/plot_chlorophyll_a/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:37.469289",
      "role": [
        "wf:main/plot_chlorophyll_a/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:35:37.469315",
      "role": [
        "wf:main/plot_chlorophyll_a/clip_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "entity": "data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0",
      "time": "2026-09-23T08:35:40.379073",
      "role": [
        "wf:main/download_b04_10m_2/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "entity": "data:084a442888f71ba66d9e75fde8221f58dfaa6acf",
      "time": "2026-09-23T08:35:40.379720",
      "role": [
        "wf:main/download_b04_10m_2/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:cb365be4-5b82-466e-a735-52203624488b",
      "entity": "data:7c5d11a451cde788be37383d50239d7672a8cb1f",
      "time": "2026-09-23T08:36:40.030554",
      "role": [
        "wf:main/download_b03_10m_2/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:cb365be4-5b82-466e-a735-52203624488b",
      "entity": "data:084a442888f71ba66d9e75fde8221f58dfaa6acf",
      "time": "2026-09-23T08:36:40.031183",
      "role": [
        "wf:main/download_b03_10m_2/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "entity": "data:36dea452bfe795afb42cf14b59c82a3127598281",
      "time": "2026-09-23T08:38:35.872518",
      "role": [
        "wf:main/download_b02_10m_2/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "entity": "data:084a442888f71ba66d9e75fde8221f58dfaa6acf",
      "time": "2026-09-23T08:38:35.873196",
      "role": [
        "wf:main/download_b02_10m_2/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "entity": "data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f",
      "time": "2026-09-23T08:39:33.186189",
      "role": [
        "wf:main/download_b01_60m_2/band"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "entity": "data:084a442888f71ba66d9e75fde8221f58dfaa6acf",
      "time": "2026-09-23T08:39:33.186583",
      "role": [
        "wf:main/download_b01_60m_2/product_url"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "entity": "id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a",
      "time": "2026-09-23T08:39:37.333038",
      "role": [
        "wf:main/reproject_b03_60m_2/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "entity": "data:3e70bde01ba4a6db2abce9619d91ad7a7e0db919",
      "time": "2026-09-23T08:39:37.333696",
      "role": [
        "wf:main/reproject_b03_60m_2/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "entity": "id:a9c6d5fa-9367-4ae4-b720-41f313d07f4c",
      "time": "2026-09-23T08:39:37.333792",
      "role": [
        "wf:main/reproject_b03_60m_2/output_resolution"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:37.333815",
      "role": [
        "wf:main/reproject_b03_60m_2/output_dimensions"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "id:f93b46c9-cd7a-4d57-8c11-1356d6797057",
      "time": "2026-09-23T08:39:38.373379",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a",
      "time": "2026-09-23T08:39:38.373441",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "id:51e7c370-3e40-44ef-9dad-344fdf984f23",
      "time": "2026-09-23T08:39:38.373467",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "data:a71d74edcae981a17e7464331cb2525eeabd9092",
      "time": "2026-09-23T08:39:38.373980",
      "role": [
        "wf:main/calculate_cyanobacteria_2/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "data:3082a66f519914584a632e0abf36aea5b5961253",
      "time": "2026-09-23T08:39:38.374305",
      "role": [
        "wf:main/calculate_cyanobacteria_2/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374324",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374335",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374346",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374355",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374365",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374374",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374384",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374395",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374405",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374414",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374423",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374432",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374442",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374451",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374460",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374473",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374483",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374492",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374501",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374510",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374520",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374535",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:38.374545",
      "role": [
        "wf:main/calculate_cyanobacteria_2/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "id:5811cb86-e667-4b42-bd25-995c414a260e",
      "time": "2026-09-23T08:39:45.596439",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab",
      "time": "2026-09-23T08:39:45.596481",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "data:c6f40f302effca33768fc256bbb5dedaca044174",
      "time": "2026-09-23T08:39:45.597090",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "data:6b318d7d0eb73571432d45252f14693013f68feb",
      "time": "2026-09-23T08:39:45.597467",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597489",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597503",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597514",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597526",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597537",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597547",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597557",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597569",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597893",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597910",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597920",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597930",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597940",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597950",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597959",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597973",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597983",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.597994",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.598005",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.598025",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.598035",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.598048",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.598058",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:39:45.598067",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "entity": "id:a0bf8c1c-f971-418d-9a40-667bb07dd0c4",
      "time": "2026-09-23T08:39:46.629878",
      "role": [
        "wf:main/plot_cyanobacteria_2/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "entity": "id:43a057a2-41ef-4082-bdfb-fb1186385f7d",
      "time": "2026-09-23T08:39:46.629916",
      "role": [
        "wf:main/plot_cyanobacteria_2/clip_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "entity": "data:1370052da0755d73768c0c75500107d3759bcc2d",
      "time": "2026-09-23T08:39:46.630723",
      "role": [
        "wf:main/plot_cyanobacteria_2/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "entity": "id:f4eb96c4-9178-469a-94da-e74a9ec97592",
      "time": "2026-09-23T08:39:46.630760",
      "role": [
        "wf:main/plot_cyanobacteria_2/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "entity": "data:b3573acf1e280c5c49f41a5a84acaedc59c5c096",
      "time": "2026-09-23T08:39:46.631165",
      "role": [
        "wf:main/plot_cyanobacteria_2/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "entity": "data:4ea652b7d22b69e0d27d1a1ebce1e624f55373fd",
      "time": "2026-09-23T08:39:46.631484",
      "role": [
        "wf:main/plot_cyanobacteria_2/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "entity": "data:4ad2eab867b3280cabc93a14c615ab97b6b6575e",
      "time": "2026-09-23T08:39:46.631794",
      "role": [
        "wf:main/plot_cyanobacteria_2/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "id:5811cb86-e667-4b42-bd25-995c414a260e",
      "time": "2026-09-23T08:40:28.574118",
      "role": [
        "wf:main/calculate_turbidity_2/band_a"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab",
      "time": "2026-09-23T08:40:28.574162",
      "role": [
        "wf:main/calculate_turbidity_2/band_c"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "data:81e487db73b1725c362decd3aac3a2c13f86d595",
      "time": "2026-09-23T08:40:28.574628",
      "role": [
        "wf:main/calculate_turbidity_2/calc"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "data:592104a468524cd5e063a0e9da39927566853012",
      "time": "2026-09-23T08:40:28.575201",
      "role": [
        "wf:main/calculate_turbidity_2/name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575220",
      "role": [
        "wf:main/calculate_turbidity_2/band_b"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575237",
      "role": [
        "wf:main/calculate_turbidity_2/band_d"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575247",
      "role": [
        "wf:main/calculate_turbidity_2/band_e"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575257",
      "role": [
        "wf:main/calculate_turbidity_2/band_f"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575270",
      "role": [
        "wf:main/calculate_turbidity_2/band_g"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575280",
      "role": [
        "wf:main/calculate_turbidity_2/band_h"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575289",
      "role": [
        "wf:main/calculate_turbidity_2/band_i"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575298",
      "role": [
        "wf:main/calculate_turbidity_2/band_j"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575308",
      "role": [
        "wf:main/calculate_turbidity_2/band_k"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575317",
      "role": [
        "wf:main/calculate_turbidity_2/band_l"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575326",
      "role": [
        "wf:main/calculate_turbidity_2/band_m"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575338",
      "role": [
        "wf:main/calculate_turbidity_2/band_n"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575347",
      "role": [
        "wf:main/calculate_turbidity_2/band_o"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575358",
      "role": [
        "wf:main/calculate_turbidity_2/band_p"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575368",
      "role": [
        "wf:main/calculate_turbidity_2/band_q"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575377",
      "role": [
        "wf:main/calculate_turbidity_2/band_r"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575386",
      "role": [
        "wf:main/calculate_turbidity_2/band_s"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575396",
      "role": [
        "wf:main/calculate_turbidity_2/band_t"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575404",
      "role": [
        "wf:main/calculate_turbidity_2/band_u"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575413",
      "role": [
        "wf:main/calculate_turbidity_2/band_v"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575425",
      "role": [
        "wf:main/calculate_turbidity_2/band_w"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575434",
      "role": [
        "wf:main/calculate_turbidity_2/band_x"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575443",
      "role": [
        "wf:main/calculate_turbidity_2/band_y"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:28.575452",
      "role": [
        "wf:main/calculate_turbidity_2/band_z"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "entity": "data:2b0824b4ba24b098adc7ce01881499891c48d2ea",
      "time": "2026-09-23T08:40:29.616392",
      "role": [
        "wf:main/plot_turbidity_2/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "entity": "id:d0b679db-ef77-442f-a4c0-f093f5da8990",
      "time": "2026-09-23T08:40:29.616450",
      "role": [
        "wf:main/plot_turbidity_2/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "entity": "data:2219e4fef3bb44cade72f7ef4d71d8d686197932",
      "time": "2026-09-23T08:40:29.617135",
      "role": [
        "wf:main/plot_turbidity_2/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "entity": "data:9f3f28fc82add0a4e71340746dfbbf9db167a541",
      "time": "2026-09-23T08:40:29.617668",
      "role": [
        "wf:main/plot_turbidity_2/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "entity": "data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c",
      "time": "2026-09-23T08:40:29.618454",
      "role": [
        "wf:main/plot_turbidity_2/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:29.618529",
      "role": [
        "wf:main/plot_turbidity_2/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:29.618548",
      "role": [
        "wf:main/plot_turbidity_2/clip_min"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "entity": "data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8",
      "time": "2026-09-23T08:40:32.119378",
      "role": [
        "wf:main/plot_chlorophyll_a_2/color_scale"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "entity": "id:883ae32e-c86f-491e-bcaf-320d0badfa08",
      "time": "2026-09-23T08:40:32.119425",
      "role": [
        "wf:main/plot_chlorophyll_a_2/input_image"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "entity": "data:c9795ae1700fc9846a06b4c55a43850d79fc8c37",
      "time": "2026-09-23T08:40:32.119821",
      "role": [
        "wf:main/plot_chlorophyll_a_2/output_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "entity": "data:3b70ed18810c540d946d852c94d6c9701138000a",
      "time": "2026-09-23T08:40:32.120366",
      "role": [
        "wf:main/plot_chlorophyll_a_2/plot_name"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "entity": "data:e059662a461e5d1b245f555149febc699f42b537",
      "time": "2026-09-23T08:40:32.120997",
      "role": [
        "wf:main/plot_chlorophyll_a_2/plot_title"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:32.121023",
      "role": [
        "wf:main/plot_chlorophyll_a_2/clip_max"
      ]
    },
    {
      "@type": "Usage",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "entity": "cwlprov:None",
      "time": "2026-09-23T08:40:32.121035",
      "role": [
        "wf:main/plot_chlorophyll_a_2/clip_min"
      ]
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:4e86d762-9ac6-4702-8818-e66cfd5e6425",
      "generalEntity": "data:e001557ec06062e8b0a518eaf12927e3d1be14ca"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:374994f9-116d-48a7-9749-2f5d0a21702e",
      "generalEntity": "data:50ebd5e63205cb9f8e4322e56677b021e540e57d"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:6d7d32e8-319d-4d54-9cb2-1094ccae2bda",
      "generalEntity": "data:ff826260056bbe39e685113083a05ab78c07c09a"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:ac7fbdba-ab57-4cab-92ea-86425e0d72da",
      "generalEntity": "data:4554c3cf3eb5232e005efba0f52710ebf69238d4"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda",
      "generalEntity": "data:d54118937320f8cd7cb6a0673991c14035966fe7"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be",
      "generalEntity": "data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:12b49a35-ae72-4b3d-933e-b2d03c6692b4",
      "generalEntity": "data:32ae8712ff4f8b8b6b34af45257c41c16474dc98"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:f82e4423-a8ac-41d1-9919-25b94a343f05",
      "generalEntity": "data:88d67511003f18c13b7cdc982f5796ab5ae261fc"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:d1872c35-1d75-47b2-8315-90b2bbf42c23",
      "generalEntity": "data:876c7b4d7381ac5660a4507292c9324eb295a297"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:4e6424db-66b9-4389-81ca-0a3040fbfd07",
      "generalEntity": "data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4",
      "generalEntity": "data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:94fcea32-9310-49c6-8684-7517ae960f49",
      "generalEntity": "data:c991e2bc239887ca885b02cab5fdae42c90a2889"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54",
      "generalEntity": "data:fb8e7e26b282372c29a35ac739498699e02006a5"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1",
      "generalEntity": "data:38185787e3c54223cfadb4c26c22b126ad624d21"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:51e7c370-3e40-44ef-9dad-344fdf984f23",
      "generalEntity": "data:06cc034ead339e3cf5f8262cc8a6a0e293c14680"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a",
      "generalEntity": "data:9f9130b688abf761a50ad3c0822794bceda8a4cd"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:f93b46c9-cd7a-4d57-8c11-1356d6797057",
      "generalEntity": "data:64ae819f0f702c63421c488fa5ccf3a41b388f94"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:5811cb86-e667-4b42-bd25-995c414a260e",
      "generalEntity": "data:46cf7f768b4167418c8ecec22d3dc976cf2e969e"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab",
      "generalEntity": "data:e33aada2083b35c0160af06da303c293f90b45cb"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:f4eb96c4-9178-469a-94da-e74a9ec97592",
      "generalEntity": "data:065539f1417b6c8066de9420c143413de2cbcd97"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:883ae32e-c86f-491e-bcaf-320d0badfa08",
      "generalEntity": "data:6947846b1796dd6e940e390f61208a85f45117b0"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1cfc6922-9537-41b3-a579-31eaab50998e",
      "generalEntity": "data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2",
      "generalEntity": "data:3822adba1b42a347ef376f9ac0e7259d0ba82b22"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:d0b679db-ef77-442f-a4c0-f093f5da8990",
      "generalEntity": "data:c50376cb72b65a0dad365279023daa2af7208fc9"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:248923b2-906c-4d76-867f-da6f12462902",
      "generalEntity": "data:a2beee36554454e4c0090480d062bc893f3ae7cc"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2",
      "generalEntity": "data:8088de425841559ae78ca6328ecdf8bb0fe578d4"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:1a896ecf-4e0a-4020-b7e1-107ee08a506c",
      "generalEntity": "data:e6874b008b758679af8241dfbfb355b204b131b2"
    },
    {
      "@type": "Specialization",
      "specificEntity": "id:372c5307-8059-4cb2-afdb-5417b1e9d278",
      "generalEntity": "data:1224781c8a82490664559a3b2e66fa3e14e09956"
    },
    {
      "@type": "Generation",
      "entity": "id:4e86d762-9ac6-4702-8818-e66cfd5e6425",
      "activity": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
      "time": "2026-09-23T08:27:22.493630",
      "role": [
        "wf:main/download_b04_10m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:374994f9-116d-48a7-9749-2f5d0a21702e",
      "activity": "id:94486889-f9f5-43d5-b151-995baade6da8",
      "time": "2026-09-23T08:28:17.439405",
      "role": [
        "wf:main/download_b03_10m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6d7d32e8-319d-4d54-9cb2-1094ccae2bda",
      "activity": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
      "time": "2026-09-23T08:29:35.348861",
      "role": [
        "wf:main/download_b02_10m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:ac7fbdba-ab57-4cab-92ea-86425e0d72da",
      "activity": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
      "time": "2026-09-23T08:29:43.327850",
      "role": [
        "wf:main/download_b01_60m/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "time": "2026-09-23T08:29:45.546400",
      "role": [
        "wf:main/reproject_b03_60m/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "time": "2026-09-23T08:30:01.871709",
      "role": [
        "wf:main/calculate_cyanobacteria/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:12b49a35-ae72-4b3d-933e-b2d03c6692b4",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "time": "2026-09-23T08:31:51.324170",
      "role": [
        "wf:main/calculate_chlorophyll_a/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:f82e4423-a8ac-41d1-9919-25b94a343f05",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "time": "2026-09-23T08:35:32.104232",
      "role": [
        "wf:main/plot_cyanobacteria/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d1872c35-1d75-47b2-8315-90b2bbf42c23",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "time": "2026-09-23T08:35:32.104232",
      "role": [
        "wf:main/plot_cyanobacteria/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:4e6424db-66b9-4389-81ca-0a3040fbfd07",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "time": "2026-09-23T08:35:34.710227",
      "role": [
        "wf:main/calculate_turbidity/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "time": "2026-09-23T08:35:37.417156",
      "role": [
        "wf:main/plot_turbidity/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:94fcea32-9310-49c6-8684-7517ae960f49",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "time": "2026-09-23T08:35:37.417156",
      "role": [
        "wf:main/plot_turbidity/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "time": "2026-09-23T08:35:40.163033",
      "role": [
        "wf:main/plot_chlorophyll_a/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "time": "2026-09-23T08:35:40.163033",
      "role": [
        "wf:main/plot_chlorophyll_a/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:12b49a35-ae72-4b3d-933e-b2d03c6692b4",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%20process/chlorophyll_a"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%2520process/chlorophyll_a_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%252520process/chlorophyll_a_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%25252520process/cyanobacteria"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:f82e4423-a8ac-41d1-9919-25b94a343f05",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%2525252520process/cyanobacteria_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d1872c35-1d75-47b2-8315-90b2bbf42c23",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%252525252520process/cyanobacteria_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:4e6424db-66b9-4389-81ca-0a3040fbfd07",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%25252525252520process/turbidity"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%2525252525252520process/turbidity_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:94fcea32-9310-49c6-8684-7517ae960f49",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.173722",
      "role": [
        "wf:main/workflow%252525252525252520process/turbidity_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:51e7c370-3e40-44ef-9dad-344fdf984f23",
      "activity": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "time": "2026-09-23T08:36:39.949986",
      "role": [
        "wf:main/download_b04_10m_2/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a",
      "activity": "id:cb365be4-5b82-466e-a735-52203624488b",
      "time": "2026-09-23T08:38:35.793003",
      "role": [
        "wf:main/download_b03_10m_2/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:f93b46c9-cd7a-4d57-8c11-1356d6797057",
      "activity": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "time": "2026-09-23T08:39:33.104073",
      "role": [
        "wf:main/download_b02_10m_2/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:5811cb86-e667-4b42-bd25-995c414a260e",
      "activity": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "time": "2026-09-23T08:39:37.315423",
      "role": [
        "wf:main/download_b01_60m_2/product"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "time": "2026-09-23T08:39:38.352561",
      "role": [
        "wf:main/reproject_b03_60m_2/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:f4eb96c4-9178-469a-94da-e74a9ec97592",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "time": "2026-09-23T08:39:45.391793",
      "role": [
        "wf:main/calculate_cyanobacteria_2/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:883ae32e-c86f-491e-bcaf-320d0badfa08",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "time": "2026-09-23T08:39:46.610597",
      "role": [
        "wf:main/calculate_chlorophyll_a_2/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:1cfc6922-9537-41b3-a579-31eaab50998e",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "time": "2026-09-23T08:40:28.335308",
      "role": [
        "wf:main/plot_cyanobacteria_2/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "time": "2026-09-23T08:40:28.335308",
      "role": [
        "wf:main/plot_cyanobacteria_2/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d0b679db-ef77-442f-a4c0-f093f5da8990",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "time": "2026-09-23T08:40:29.594121",
      "role": [
        "wf:main/calculate_turbidity_2/result"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:248923b2-906c-4d76-867f-da6f12462902",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "time": "2026-09-23T08:40:32.099562",
      "role": [
        "wf:main/plot_turbidity_2/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "time": "2026-09-23T08:40:32.099562",
      "role": [
        "wf:main/plot_turbidity_2/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:1a896ecf-4e0a-4020-b7e1-107ee08a506c",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "time": "2026-09-23T08:40:34.302796",
      "role": [
        "wf:main/plot_chlorophyll_a_2/output_file"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:372c5307-8059-4cb2-afdb-5417b1e9d278",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "time": "2026-09-23T08:40:34.302796",
      "role": [
        "wf:main/plot_chlorophyll_a_2/output_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:883ae32e-c86f-491e-bcaf-320d0badfa08",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%20process_2/chlorophyll_a"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:1a896ecf-4e0a-4020-b7e1-107ee08a506c",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%2520process_2/chlorophyll_a_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:372c5307-8059-4cb2-afdb-5417b1e9d278",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%252520process_2/chlorophyll_a_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:f4eb96c4-9178-469a-94da-e74a9ec97592",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%25252520process_2/cyanobacteria"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:1cfc6922-9537-41b3-a579-31eaab50998e",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%2525252520process_2/cyanobacteria_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%252525252520process_2/cyanobacteria_plot"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:d0b679db-ef77-442f-a4c0-f093f5da8990",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%25252525252520process_2/turbidity"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:248923b2-906c-4d76-867f-da6f12462902",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%2525252525252520process_2/turbidity_color"
      ]
    },
    {
      "@type": "Generation",
      "entity": "id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.311312",
      "role": [
        "wf:main/workflow%252525252525252520process_2/turbidity_plot"
      ]
    },
    {
      "@type": "End",
      "activity": "id:29af451f-402f-4925-b588-7d3cdc25c6f9",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:27:22.493610"
    },
    {
      "@type": "End",
      "activity": "id:94486889-f9f5-43d5-b151-995baade6da8",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:28:17.439395"
    },
    {
      "@type": "End",
      "activity": "id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:29:35.348764"
    },
    {
      "@type": "End",
      "activity": "id:f0d8a485-c284-4e61-883c-b97dff3b466f",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:29:43.327839"
    },
    {
      "@type": "End",
      "activity": "id:f6d76af7-483d-4435-9b74-e6f721878714",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:29:45.546381"
    },
    {
      "@type": "End",
      "activity": "id:57b7acfa-2232-4152-9c9c-c828c764753d",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:30:01.871693"
    },
    {
      "@type": "End",
      "activity": "id:af841592-5838-42f8-aa5d-95146384bc26",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:31:51.324117"
    },
    {
      "@type": "End",
      "activity": "id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:32.104196"
    },
    {
      "@type": "End",
      "activity": "id:60b3089e-0d3d-45d0-a4b9-10f73441289d",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:34.710217"
    },
    {
      "@type": "End",
      "activity": "id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:37.417146"
    },
    {
      "@type": "End",
      "activity": "id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:35:40.163022"
    },
    {
      "@type": "End",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "ender": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "time": "2026-09-23T08:35:40.173908"
    },
    {
      "@type": "End",
      "activity": "id:4db7406a-158b-48d8-8594-4e042177c7b6",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:36:39.949967"
    },
    {
      "@type": "End",
      "activity": "id:cb365be4-5b82-466e-a735-52203624488b",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:38:35.792992"
    },
    {
      "@type": "End",
      "activity": "id:e2bfc5c3-1f75-4088-95f8-366b8283237b",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:33.104017"
    },
    {
      "@type": "End",
      "activity": "id:2a9686ec-313f-4d80-93b4-f4867c661dd8",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:37.315412"
    },
    {
      "@type": "End",
      "activity": "id:2140e929-bf51-4666-b8c5-c93b1ba365d6",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:38.352541"
    },
    {
      "@type": "End",
      "activity": "id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:45.391783"
    },
    {
      "@type": "End",
      "activity": "id:76594558-3301-40b6-b667-368e942831f2",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:39:46.610585"
    },
    {
      "@type": "End",
      "activity": "id:eb258705-e788-4815-aaa8-8ce9fe8b95bd",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:28.335295"
    },
    {
      "@type": "End",
      "activity": "id:159f4467-f8cc-430c-9f3c-88fbbac7801c",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:29.594104"
    },
    {
      "@type": "End",
      "activity": "id:667fa027-ed54-41eb-97a1-2dba34cda14d",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:32.099554"
    },
    {
      "@type": "End",
      "activity": "id:404675d7-a7d3-463f-8754-35edf2fc0c25",
      "ender": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "time": "2026-09-23T08:40:34.302789"
    },
    {
      "@type": "End",
      "activity": "id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86",
      "ender": "id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8",
      "time": "2026-09-23T08:40:34.311473"
    },
    {
      "@type": "Membership",
      "collection": "id:b9b1351c-627e-45d6-81a3-1283ea584ec8",
      "entity": "id:451dd3a3-2e5f-4acf-b930-ad5fcd658419"
    },
    {
      "@type": "Membership",
      "collection": "id:b9b1351c-627e-45d6-81a3-1283ea584ec8",
      "entity": "id:bd2db380-4b87-4d7a-a309-23597ccb9c57"
    },
    {
      "@type": "Membership",
      "collection": "id:a9c6d5fa-9367-4ae4-b720-41f313d07f4c",
      "entity": "id:5c2f550b-8421-44b9-833c-1f6d2b83155f"
    },
    {
      "@type": "Membership",
      "collection": "id:a9c6d5fa-9367-4ae4-b720-41f313d07f4c",
      "entity": "id:09792302-bb35-4042-a300-a2e7f2acf386"
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

id:1a896ecf-4e0a-4020-b7e1-107ee08a506c a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%2520process_2/chlorophyll_a_color> ],
        [ a prov:Generation ;
            prov:activity id:404675d7-a7d3-463f-8754-35edf2fc0c25 ;
            prov:atTime "2026-09-23T08:40:34.302796"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/output_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e6874b008b758679af8241dfbfb355b204b131b2 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color" .

id:1cfc6922-9537-41b3-a579-31eaab50998e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%2525252520process_2/cyanobacteria_color> ],
        [ a prov:Generation ;
            prov:activity id:eb258705-e788-4815-aaa8-8ce9fe8b95bd ;
            prov:atTime "2026-09-23T08:40:28.335308"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/output_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_cyanobacteria_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_cyanobacteria_color" .

id:248923b2-906c-4d76-867f-da6f12462902 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:667fa027-ed54-41eb-97a1-2dba34cda14d ;
            prov:atTime "2026-09-23T08:40:32.099562"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/output_file> ],
        [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%2525252525252520process_2/turbidity_color> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:a2beee36554454e4c0090480d062bc893f3ae7cc ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_turbidity_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_turbidity_color" .

id:372c5307-8059-4cb2-afdb-5417b1e9d278 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:404675d7-a7d3-463f-8754-35edf2fc0c25 ;
            prov:atTime "2026-09-23T08:40:34.302796"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/output_plot> ],
        [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%252520process_2/chlorophyll_a_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:1224781c8a82490664559a3b2e66fa3e14e09956 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot" .

id:3a29ce4a-c70b-4cb5-ac90-5cc003d32df1 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e ;
            prov:atTime "2026-09-23T08:35:40.163033"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/output_plot> ],
        [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%252520process/chlorophyll_a_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:38185787e3c54223cfadb4c26c22b126ad624d21 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot" .

id:6d66c47d-61c7-49a1-b045-7a8a19d0ef54 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%2520process/chlorophyll_a_color> ],
        [ a prov:Generation ;
            prov:activity id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e ;
            prov:atTime "2026-09-23T08:35:40.163033"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/output_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:fb8e7e26b282372c29a35ac739498699e02006a5 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color" .

id:6dd26a4a-5269-487b-ad11-0e3cfe83bae2 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%252525252525252520process_2/turbidity_plot> ],
        [ a prov:Generation ;
            prov:activity id:667fa027-ed54-41eb-97a1-2dba34cda14d ;
            prov:atTime "2026-09-23T08:40:32.099562"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/output_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:8088de425841559ae78ca6328ecdf8bb0fe578d4 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_turbidity_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_turbidity_plot" .

id:94fcea32-9310-49c6-8684-7517ae960f49 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1 ;
            prov:atTime "2026-09-23T08:35:37.417156"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/output_plot> ],
        [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%252525252525252520process/turbidity_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:c991e2bc239887ca885b02cab5fdae42c90a2889 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_turbidity_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_turbidity_plot" .

id:a1fdff0a-0d34-46cc-8ad6-0ec1bfee7ad2 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%252525252520process_2/cyanobacteria_plot> ],
        [ a prov:Generation ;
            prov:activity id:eb258705-e788-4815-aaa8-8ce9fe8b95bd ;
            prov:atTime "2026-09-23T08:40:28.335308"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/output_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:3822adba1b42a347ef376f9ac0e7259d0ba82b22 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot" .

id:cc8be8e0-4b98-47f7-8c0c-a757d7a5eff4 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1 ;
            prov:atTime "2026-09-23T08:35:37.417156"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/output_file> ],
        [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%2525252525252520process/turbidity_color> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_turbidity_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_turbidity_color" .

id:d1872c35-1d75-47b2-8315-90b2bbf42c23 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%252525252520process/cyanobacteria_plot> ],
        [ a prov:Generation ;
            prov:activity id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8 ;
            prov:atTime "2026-09-23T08:35:32.104232"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/output_plot> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:876c7b4d7381ac5660a4507292c9324eb295a297 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot.png" ;
    cwlprov:nameext ".png" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot" .

id:f82e4423-a8ac-41d1-9919-25b94a343f05 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%2525252520process/cyanobacteria_color> ],
        [ a prov:Generation ;
            prov:activity id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8 ;
            prov:atTime "2026-09-23T08:35:32.104232"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/output_file> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:88d67511003f18c13b7cdc982f5796ab5ae261fc ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_cyanobacteria_color.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_cyanobacteria_color" .

wf:main a wfdesc:Workflow,
        prov:Entity,
        prov:Plan ;
    rdfs:label "Prospective provenance" ;
    wfdesc:hasSubProcess "wf:main/calculate_chlorophyll_a"^^xsd:QName,
        "wf:main/calculate_chlorophyll_a_2"^^xsd:QName,
        "wf:main/calculate_cyanobacteria"^^xsd:QName,
        "wf:main/calculate_cyanobacteria_2"^^xsd:QName,
        "wf:main/calculate_turbidity"^^xsd:QName,
        "wf:main/calculate_turbidity_2"^^xsd:QName,
        "wf:main/download_b01_60m"^^xsd:QName,
        "wf:main/download_b01_60m_2"^^xsd:QName,
        "wf:main/download_b02_10m"^^xsd:QName,
        "wf:main/download_b02_10m_2"^^xsd:QName,
        "wf:main/download_b03_10m"^^xsd:QName,
        "wf:main/download_b03_10m_2"^^xsd:QName,
        "wf:main/download_b04_10m"^^xsd:QName,
        "wf:main/download_b04_10m_2"^^xsd:QName,
        "wf:main/plot_chlorophyll_a"^^xsd:QName,
        "wf:main/plot_chlorophyll_a_2"^^xsd:QName,
        "wf:main/plot_cyanobacteria"^^xsd:QName,
        "wf:main/plot_cyanobacteria_2"^^xsd:QName,
        "wf:main/plot_turbidity"^^xsd:QName,
        "wf:main/plot_turbidity_2"^^xsd:QName,
        "wf:main/reproject_b03_60m"^^xsd:QName,
        "wf:main/reproject_b03_60m_2"^^xsd:QName .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

<arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m_2> a wfdesc:Process,
        prov:Entity,
        prov:Plan .

data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0 a wfprov:Artifact,
        prov:Entity .

data:065539f1417b6c8066de9420c143413de2cbcd97 a wfprov:Artifact,
        prov:Entity .

data:06cc034ead339e3cf5f8262cc8a6a0e293c14680 a wfprov:Artifact,
        prov:Entity .

data:1224781c8a82490664559a3b2e66fa3e14e09956 a wfprov:Artifact,
        prov:Entity .

data:1a0e4fad40b7e324bd7ae77ac30e69a00173cd35 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_turbidity_plot" .

data:2219e4fef3bb44cade72f7ef4d71d8d686197932 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_turbidity_color" .

data:3082a66f519914584a632e0abf36aea5b5961253 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_cyanobacteria" .

data:32ae8712ff4f8b8b6b34af45257c41c16474dc98 a wfprov:Artifact,
        prov:Entity .

data:337c1d5047de712ebdd9cfe4e5bafaad9ed60ca1 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_turbidity" .

data:38185787e3c54223cfadb4c26c22b126ad624d21 a wfprov:Artifact,
        prov:Entity .

data:3822adba1b42a347ef376f9ac0e7259d0ba82b22 a wfprov:Artifact,
        prov:Entity .

data:3b70ed18810c540d946d852c94d6c9701138000a a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_chlorophyll_a_plot" .

data:4554c3cf3eb5232e005efba0f52710ebf69238d4 a wfprov:Artifact,
        prov:Entity .

data:46cf7f768b4167418c8ecec22d3dc976cf2e969e a wfprov:Artifact,
        prov:Entity .

data:4ea652b7d22b69e0d27d1a1ebce1e624f55373fd a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_cyanobacteria_plot" .

data:50ebd5e63205cb9f8e4322e56677b021e540e57d a wfprov:Artifact,
        prov:Entity .

data:5764e8024006b4e2959972b2ed8133b75af135e7 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_chlorophyll_a" .

data:592104a468524cd5e063a0e9da39927566853012 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_turbidity" .

data:5cd4c929136b7ccfd44b3e4a9e543eaf5497e074 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_cyanobacteria_color" .

data:64ae819f0f702c63421c488fa5ccf3a41b388f94 a wfprov:Artifact,
        prov:Entity .

data:6947846b1796dd6e940e390f61208a85f45117b0 a wfprov:Artifact,
        prov:Entity .

data:6b318d7d0eb73571432d45252f14693013f68feb a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_chlorophyll_a" .

data:714bad22665ac25a2625f9795548244c5862c173 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_chlorophyll_a_plot" .

data:74f86325eb5176eac0be70c602f62dd4be091838 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_chlorophyll_a_color" .

data:7c493f20c0ed3a9a2a729ce9e109ca30f4e9836a a wfprov:Artifact,
        prov:Entity .

data:8088de425841559ae78ca6328ecdf8bb0fe578d4 a wfprov:Artifact,
        prov:Entity .

data:876c7b4d7381ac5660a4507292c9324eb295a297 a wfprov:Artifact,
        prov:Entity .

data:88d67511003f18c13b7cdc982f5796ab5ae261fc a wfprov:Artifact,
        prov:Entity .

data:99bf64d1155bc89e1a330d0cf10036305f65955d a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_cyanobacteria" .

data:9f3f28fc82add0a4e71340746dfbbf9db167a541 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_turbidity_plot" .

data:9f9130b688abf761a50ad3c0822794bceda8a4cd a wfprov:Artifact,
        prov:Entity .

data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8 a wfprov:Artifact,
        prov:Entity .

data:a2beee36554454e4c0090480d062bc893f3ae7cc a wfprov:Artifact,
        prov:Entity .

data:b3573acf1e280c5c49f41a5a84acaedc59c5c096 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_cyanobacteria_color" .

data:c50376cb72b65a0dad365279023daa2af7208fc9 a wfprov:Artifact,
        prov:Entity .

data:c9795ae1700fc9846a06b4c55a43850d79fc8c37 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_0_L2A_chlorophyll_a_color" .

data:c991e2bc239887ca885b02cab5fdae42c90a2889 a wfprov:Artifact,
        prov:Entity .

data:d54118937320f8cd7cb6a0673991c14035966fe7 a wfprov:Artifact,
        prov:Entity .

data:dae6881b456c2247c2fe7bf59cb2d891427f2aec a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_cyanobacteria_plot" .

data:e001557ec06062e8b0a518eaf12927e3d1be14ca a wfprov:Artifact,
        prov:Entity .

data:e33aada2083b35c0160af06da303c293f90b45cb a wfprov:Artifact,
        prov:Entity .

data:e6874b008b758679af8241dfbfb355b204b131b2 a wfprov:Artifact,
        prov:Entity .

data:ee28bfbb1143c5e869cc07962f87b8cfac6106f6 a wfprov:Artifact,
        prov:Entity .

data:f4ad1bd9dbf27a2d94b4320d4ffe146bf714a9d0 a wfprov:Artifact,
        prov:Entity ;
    prov:value "S2A_29SPC_20190701_1_L2A_turbidity_color" .

data:fb8e7e26b282372c29a35ac739498699e02006a5 a wfprov:Artifact,
        prov:Entity .

data:ff826260056bbe39e685113083a05ab78c07c09a a wfprov:Artifact,
        prov:Entity .

id:09792302-bb35-4042-a300-a2e7f2acf386 a prov:Entity ;
    prov:value "60"^^xsd:int .

id:0b700855-69e1-4836-9881-4bc2cd023102 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:0c872b6c-8902-4cfb-a981-8a8d16ca84cc a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:10162287-984a-45d3-883f-c473d1b9f4e8 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:12b49a35-ae72-4b3d-933e-b2d03c6692b4 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%20process/chlorophyll_a> ],
        [ a prov:Generation ;
            prov:activity id:af841592-5838-42f8-aa5d-95146384bc26 ;
            prov:atTime "2026-09-23T08:31:51.324170"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:32ae8712ff4f8b8b6b34af45257c41c16474dc98 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_chlorophyll_a.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_chlorophyll_a" .

id:159f4467-f8cc-430c-9f3c-88fbbac7801c a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_turbidity_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:88f4398b-bad2-4419-8b31-21a7b0d29e51 ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:40:29.594104"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:40:28.567857"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.574628"^^xsd:dateTime ;
            prov:entity data:81e487db73b1725c362decd3aac3a2c13f86d595 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575201"^^xsd:dateTime ;
            prov:entity data:592104a468524cd5e063a0e9da39927566853012 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575404"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575377"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575452"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.574162"^^xsd:dateTime ;
            prov:entity id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575237"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575368"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575413"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575358"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575386"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575220"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575326"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575289"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.574118"^^xsd:dateTime ;
            prov:entity id:5811cb86-e667-4b42-bd25-995c414a260e ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_a> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575338"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575425"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575280"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575257"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575443"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575270"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575247"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575347"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575308"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575434"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575298"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575396"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:28.575317"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/band_l> ] .

id:15e3229d-5bd8-408e-a96a-da5e4356b8d0 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:2140e929-bf51-4666-b8c5-c93b1ba365d6 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/reproject_b03_60m_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m_2> ],
        [ a prov:Association ;
            prov:agent id:fcd270b7-0276-4c6d-b13d-35cb00865823 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:39:38.352541"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:39:37.327471"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:37.333815"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m_2/output_dimensions> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:37.333792"^^xsd:dateTime ;
            prov:entity id:a9c6d5fa-9367-4ae4-b720-41f313d07f4c ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m_2/output_resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:37.333038"^^xsd:dateTime ;
            prov:entity id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m_2/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:37.333696"^^xsd:dateTime ;
            prov:entity data:3e70bde01ba4a6db2abce9619d91ad7a7e0db919 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m_2/output_name> ] .

id:29af451f-402f-4925-b588-7d3cdc25c6f9 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b04_10m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m> ],
        [ a prov:Association ;
            prov:agent id:d9639ebc-984b-431c-a823-05a86eb32fb5 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:27:22.493610"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:26:25.904018"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:25.961176"^^xsd:dateTime ;
            prov:entity data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:26:25.961572"^^xsd:dateTime ;
            prov:entity data:c80240b036ceef4fdcfb684013f5e78f2fd144e7 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m/product_url> ] .

id:2a9686ec-313f-4d80-93b4-f4867c661dd8 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b01_60m_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m_2> ],
        [ a prov:Association ;
            prov:agent id:fc7a1f11-3e40-431c-af77-7523c1e37baf ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:39:37.315412"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:39:33.178483"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:33.186583"^^xsd:dateTime ;
            prov:entity data:084a442888f71ba66d9e75fde8221f58dfaa6acf ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m_2/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:33.186189"^^xsd:dateTime ;
            prov:entity data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m_2/band> ] .

id:31508f5e-88d5-4a9b-b917-e0cc6dbe47ec a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:43a057a2-41ef-4082-bdfb-fb1186385f7d a prov:Entity ;
    prov:value "1000000"^^xsd:int .

id:43debe24-70e3-4566-871e-889b76d6357b a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:451dd3a3-2e5f-4acf-b930-ad5fcd658419 a prov:Entity ;
    prov:value "60"^^xsd:int .

id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%25252520process/cyanobacteria> ],
        [ a prov:Generation ;
            prov:activity id:57b7acfa-2232-4152-9c9c-c828c764753d ;
            prov:atTime "2026-09-23T08:30:01.871709"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:a0b94d0cf953df1bb6e7f4005e31908be982ccf8 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_cyanobacteria.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_cyanobacteria" .

id:4db7406a-158b-48d8-8594-4e042177c7b6 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b04_10m_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:b1a07bb1-efbb-400e-8886-bb197dbe7345 ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:36:39.949967"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:35:40.369662"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:40.379720"^^xsd:dateTime ;
            prov:entity data:084a442888f71ba66d9e75fde8221f58dfaa6acf ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m_2/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:40.379073"^^xsd:dateTime ;
            prov:entity data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m_2/band> ] .

id:4e6424db-66b9-4389-81ca-0a3040fbfd07 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:35:40.173722"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%25252525252520process/turbidity> ],
        [ a prov:Generation ;
            prov:activity id:60b3089e-0d3d-45d0-a4b9-10f73441289d ;
            prov:atTime "2026-09-23T08:35:34.710227"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:01dfc84e7e1d9097b179c43e7647e6e5c1b32bb0 ] ;
    cwlprov:basename "S2A_29SPC_20190701_1_L2A_turbidity.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_1_L2A_turbidity" .

id:4e86d762-9ac6-4702-8818-e66cfd5e6425 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:29af451f-402f-4925-b588-7d3cdc25c6f9 ;
            prov:atTime "2026-09-23T08:27:22.493630"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e001557ec06062e8b0a518eaf12927e3d1be14ca ] ;
    cwlprov:basename "B04.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B04" .

id:51e7c370-3e40-44ef-9dad-344fdf984f23 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:4db7406a-158b-48d8-8594-4e042177c7b6 ;
            prov:atTime "2026-09-23T08:36:39.949986"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b04_10m_2/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:06cc034ead339e3cf5f8262cc8a6a0e293c14680 ] ;
    cwlprov:basename "B04.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B04" .

id:57b7acfa-2232-4152-9c9c-c828c764753d a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_cyanobacteria" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria> ],
        [ a prov:Association ;
            prov:agent id:f24c1565-ee7f-4d30-9e3e-f439a7d3df25 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:30:01.871693"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:29:45.564470"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691593"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691669"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691467"^^xsd:dateTime ;
            prov:entity data:99bf64d1155bc89e1a330d0cf10036305f65955d ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691661"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691689"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691699"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691583"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691504"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691514"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691642"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691652"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691630"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691707"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691563"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.690422"^^xsd:dateTime ;
            prov:entity id:374994f9-116d-48a7-9749-2f5d0a21702e ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691185"^^xsd:dateTime ;
            prov:entity data:a71d74edcae981a17e7464331cb2525eeabd9092 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691549"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691538"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691680"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691574"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691612"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691495"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691523"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.690347"^^xsd:dateTime ;
            prov:entity id:6d7d32e8-319d-4d54-9cb2-1094ccae2bda ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_a> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691484"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691621"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.691602"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:45.690440"^^xsd:dateTime ;
            prov:entity id:4e86d762-9ac6-4702-8818-e66cfd5e6425 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria/band_c> ] .

id:5c2f550b-8421-44b9-833c-1f6d2b83155f a prov:Entity ;
    prov:value "60"^^xsd:int .

id:60b3089e-0d3d-45d0-a4b9-10f73441289d a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_turbidity" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity> ],
        [ a prov:Association ;
            prov:agent id:a541ab4e-c3d9-4a7f-9b05-fa686586b70f ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:35:34.710217"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:35:32.394913"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409047"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409127"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408912"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409036"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.407551"^^xsd:dateTime ;
            prov:entity id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409022"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409060"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409150"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408973"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408860"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408962"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408899"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408951"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409072"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409113"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408874"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408986"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408385"^^xsd:dateTime ;
            prov:entity data:81e487db73b1725c362decd3aac3a2c13f86d595 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409101"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409139"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408935"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408834"^^xsd:dateTime ;
            prov:entity data:337c1d5047de712ebdd9cfe4e5bafaad9ed60ca1 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409084"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408887"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.409010"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.407492"^^xsd:dateTime ;
            prov:entity id:ac7fbdba-ab57-4cab-92ea-86425e0d72da ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_a> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408924"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:32.408998"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity/band_n> ] .

id:67aa2703-a2a1-434d-9a49-072e268b1de7 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:6d7d32e8-319d-4d54-9cb2-1094ccae2bda a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00 ;
            prov:atTime "2026-09-23T08:29:35.348861"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:ff826260056bbe39e685113083a05ab78c07c09a ] ;
    cwlprov:basename "B02.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B02" .

id:76594558-3301-40b6-b667-368e942831f2 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_chlorophyll_a_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:8c44a324-28dd-427d-9f64-6569ea486f8e ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:39:46.610585"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:39:45.590645"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597910"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597983"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597514"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597557"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.598048"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597994"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.598025"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597950"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597467"^^xsd:dateTime ;
            prov:entity data:6b318d7d0eb73571432d45252f14693013f68feb ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.598058"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597526"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.596481"^^xsd:dateTime ;
            prov:entity id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597959"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597569"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597547"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.596439"^^xsd:dateTime ;
            prov:entity id:5811cb86-e667-4b42-bd25-995c414a260e ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_a> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597090"^^xsd:dateTime ;
            prov:entity data:c6f40f302effca33768fc256bbb5dedaca044174 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597940"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597893"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597930"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597920"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.598005"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597973"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597489"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597503"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.598035"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.597537"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:45.598067"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/band_z> ] .

id:780ec89d-f9bc-4d68-a37b-36bb3230bca9 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:7e607c5d-519f-412b-9070-e1bcbc762376 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:883ae32e-c86f-491e-bcaf-320d0badfa08 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%20process_2/chlorophyll_a> ],
        [ a prov:Generation ;
            prov:activity id:76594558-3301-40b6-b667-368e942831f2 ;
            prov:atTime "2026-09-23T08:39:46.610597"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a_2/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:6947846b1796dd6e940e390f61208a85f45117b0 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_chlorophyll_a.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_chlorophyll_a" .

id:88f4398b-bad2-4419-8b31-21a7b0d29e51 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:8c44a324-28dd-427d-9f64-6569ea486f8e a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:94486889-f9f5-43d5-b151-995baade6da8 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b03_10m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m> ],
        [ a prov:Association ;
            prov:agent id:ee2b4489-574c-40d5-b36c-b1e9afeb669b ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:28:17.439395"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:27:22.563012"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:27:22.568133"^^xsd:dateTime ;
            prov:entity data:c80240b036ceef4fdcfb684013f5e78f2fd144e7 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:27:22.567887"^^xsd:dateTime ;
            prov:entity data:7c5d11a451cde788be37383d50239d7672a8cb1f ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m/band> ] .

id:9a6bba8a-cc4d-46f8-9374-cf7e4f42608e a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/reproject-image" ;
    cwlprov:image "ogc-ospd/algae-usecase/reproject-image" .

id:9e986cfd-629d-41cf-9c75-eb65ae428d71 a prov:Agent .

id:a0bf8c1c-f971-418d-9a40-667bb07dd0c4 a prov:Entity ;
    prov:value "100000000000000"^^xsd:int .

id:a541ab4e-c3d9-4a7f-9b05-fa686586b70f a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:a9c6d5fa-9367-4ae4-b720-41f313d07f4c a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:09792302-bb35-4042-a300-a2e7f2acf386 ],
        [ a provext:Membership ;
            provext:member id:5c2f550b-8421-44b9-833c-1f6d2b83155f ] .

id:ab87aed1-ceb2-4bf2-9ab2-f5e5de480e7e a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/plot-image:1.0.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/plot-image:1.0.0" .

id:af841592-5838-42f8-aa5d-95146384bc26 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_chlorophyll_a" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:c3a912fe-4417-4bd1-81a8-95e5654f7532 ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:31:51.324117"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:30:02.101602"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.125284"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128256"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128612"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_r> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.129020"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.123656"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.125306"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.123630"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.125327"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.125259"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128704"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128563"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.122046"^^xsd:dateTime ;
            prov:entity data:c6f40f302effca33768fc256bbb5dedaca044174 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128998"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128973"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.125207"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.130693"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.123575"^^xsd:dateTime ;
            prov:entity data:5764e8024006b4e2959972b2ed8133b75af135e7 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128428"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128542"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128654"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128499"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128937"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128682"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128471"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.118918"^^xsd:dateTime ;
            prov:entity id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.118857"^^xsd:dateTime ;
            prov:entity id:ac7fbdba-ab57-4cab-92ea-86425e0d72da ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_a> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128521"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:30:02.128391"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_chlorophyll_a/band_k> ] .

id:b1a07bb1-efbb-400e-8886-bb197dbe7345 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:b6170213-9472-4118-a656-1c72592c233b a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:b9b1351c-627e-45d6-81a3-1283ea584ec8 a wfprov:Artifact,
        prov:Collection,
        prov:Entity ;
    provext:qualifiedMembership [ a provext:Membership ;
            provext:member id:bd2db380-4b87-4d7a-a309-23597ccb9c57 ],
        [ a provext:Membership ;
            provext:member id:451dd3a3-2e5f-4acf-b930-ad5fcd658419 ] .

id:bd2db380-4b87-4d7a-a309-23597ccb9c57 a prov:Entity ;
    prov:value "60"^^xsd:int .

id:c3a912fe-4417-4bd1-81a8-95e5654f7532 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:cb365be4-5b82-466e-a735-52203624488b a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b03_10m_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:7e607c5d-519f-412b-9070-e1bcbc762376 ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:38:35.792992"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:36:40.025061"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:36:40.031183"^^xsd:dateTime ;
            prov:entity data:084a442888f71ba66d9e75fde8221f58dfaa6acf ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m_2/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:36:40.030554"^^xsd:dateTime ;
            prov:entity data:7c5d11a451cde788be37383d50239d7672a8cb1f ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m_2/band> ] .

id:d0b679db-ef77-442f-a4c0-f093f5da8990 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:159f4467-f8cc-430c-9f3c-88fbbac7801c ;
            prov:atTime "2026-09-23T08:40:29.594121"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_turbidity_2/result> ],
        [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%25252525252520process_2/turbidity> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:c50376cb72b65a0dad365279023daa2af7208fc9 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_turbidity.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_turbidity" .

id:d453fa6b-5d2b-47e8-a494-dbb2aa107a00 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b02_10m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m> ],
        [ a prov:Association ;
            prov:agent id:0b700855-69e1-4836-9881-4bc2cd023102 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:29:35.348764"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:28:17.508715"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:28:17.514641"^^xsd:dateTime ;
            prov:entity data:36dea452bfe795afb42cf14b59c82a3127598281 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:28:17.515035"^^xsd:dateTime ;
            prov:entity data:c80240b036ceef4fdcfb684013f5e78f2fd144e7 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m/product_url> ] .

id:d9639ebc-984b-431c-a823-05a86eb32fb5 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/calculate_cyanobacteria_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2> ],
        [ a prov:Association ;
            prov:agent id:0c872b6c-8902-4cfb-a981-8a8d16ca84cc ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:39:45.391783"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:39:38.367140"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374365"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_h> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374355"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_g> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374501"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_v> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374451"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_q> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374305"^^xsd:dateTime ;
            prov:entity data:3082a66f519914584a632e0abf36aea5b5961253 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374483"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_t> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374335"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_e> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374395"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_k> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374346"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_f> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374405"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_l> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374473"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_s> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374520"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_x> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374492"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_u> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.373441"^^xsd:dateTime ;
            prov:entity id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_b> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374545"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_z> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374423"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_n> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374374"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_i> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374414"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_m> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374432"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_o> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.373379"^^xsd:dateTime ;
            prov:entity id:f93b46c9-cd7a-4d57-8c11-1356d6797057 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_a> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374442"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_p> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.373980"^^xsd:dateTime ;
            prov:entity data:a71d74edcae981a17e7464331cb2525eeabd9092 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/calc> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374324"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_d> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374535"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_y> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374510"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_w> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374384"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_j> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.373467"^^xsd:dateTime ;
            prov:entity id:51e7c370-3e40-44ef-9dad-344fdf984f23 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_c> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:38.374460"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/band_r> ] .

id:e2bfc5c3-1f75-4088-95f8-366b8283237b a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b02_10m_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:b6170213-9472-4118-a656-1c72592c233b ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:39:33.104017"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:38:35.866253"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:38:35.872518"^^xsd:dateTime ;
            prov:entity data:36dea452bfe795afb42cf14b59c82a3127598281 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m_2/band> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:38:35.873196"^^xsd:dateTime ;
            prov:entity data:084a442888f71ba66d9e75fde8221f58dfaa6acf ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m_2/product_url> ] .

id:e5d9b324-0df0-444b-b4d9-4e9ccb71c5a7 a prov:Entity ;
    prov:value "1000000"^^xsd:int .

id:ee2b4489-574c-40d5-b36c-b1e9afeb669b a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:f0d8a485-c284-4e61-883c-b97dff3b466f a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/download_b01_60m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:43debe24-70e3-4566-871e-889b76d6357b ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:29:43.327839"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:29:35.440239"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:35.447263"^^xsd:dateTime ;
            prov:entity data:c80240b036ceef4fdcfb684013f5e78f2fd144e7 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m/product_url> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:35.446827"^^xsd:dateTime ;
            prov:entity data:0e25362cc531cdfa5fe7478737037da2ab1c4b2f ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m/band> ] .

id:f24c1565-ee7f-4d30-9e3e-f439a7d3df25 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/calculate-band:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/calculate-band:1.1.0" .

id:f4eb96c4-9178-469a-94da-e74a9ec97592 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ;
            prov:atTime "2026-09-23T08:40:34.311312"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/workflow%25252520process_2/cyanobacteria> ],
        [ a prov:Generation ;
            prov:activity id:d9e128eb-1ddb-4b2e-b8e5-5c92defdc721 ;
            prov:atTime "2026-09-23T08:39:45.391793"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/calculate_cyanobacteria_2/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:065539f1417b6c8066de9420c143413de2cbcd97 ] ;
    cwlprov:basename "S2A_29SPC_20190701_0_L2A_cyanobacteria.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "S2A_29SPC_20190701_0_L2A_cyanobacteria" .

id:f6d76af7-483d-4435-9b74-e6f721878714 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/reproject_b03_60m" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m> ],
        [ a prov:Association ;
            prov:agent id:9a6bba8a-cc4d-46f8-9374-cf7e4f42608e ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:29:45.546381"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:29:43.354293"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:43.441694"^^xsd:dateTime ;
            prov:entity id:374994f9-116d-48a7-9749-2f5d0a21702e ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:43.442889"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m/output_dimensions> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:43.442864"^^xsd:dateTime ;
            prov:entity id:b9b1351c-627e-45d6-81a3-1283ea584ec8 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m/output_resolution> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:29:43.442743"^^xsd:dateTime ;
            prov:entity data:3e70bde01ba4a6db2abce9619d91ad7a7e0db919 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m/output_name> ] .

id:f93b46c9-cd7a-4d57-8c11-1356d6797057 a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:e2bfc5c3-1f75-4088-95f8-366b8283237b ;
            prov:atTime "2026-09-23T08:39:33.104073"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b02_10m_2/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:64ae819f0f702c63421c488fa5ccf3a41b388f94 ] ;
    cwlprov:basename "B02.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B02" .

id:fc7a1f11-3e40-431c-af77-7523c1e37baf a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" ;
    cwlprov:image "ogc-ospd/algae-usecase/download-band-sentinel2-stac-item:1.1.0" .

id:fc882878-31a6-43ba-88a7-5c51bad2cef3 a prov:Entity ;
    prov:value "100000000000000"^^xsd:int .

id:fcd270b7-0276-4c6d-b13d-35cb00865823 a prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "Container execution of image ogc-ospd/algae-usecase/reproject-image" ;
    cwlprov:image "ogc-ospd/algae-usecase/reproject-image" .

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

data:36dea452bfe795afb42cf14b59c82a3127598281 a wfprov:Artifact,
        prov:Entity ;
    prov:value "B02" .

data:3e70bde01ba4a6db2abce9619d91ad7a7e0db919 a wfprov:Artifact,
        prov:Entity ;
    prov:value "B03_60m" .

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

data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c a wfprov:Artifact,
        prov:Entity ;
    prov:value "Turbidity" .

data:7c5d11a451cde788be37383d50239d7672a8cb1f a wfprov:Artifact,
        prov:Entity ;
    prov:value "B03" .

data:81e487db73b1725c362decd3aac3a2c13f86d595 a wfprov:Artifact,
        prov:Entity ;
    prov:value "(8.93*(C/A))-6.39" .

data:a71d74edcae981a17e7464331cb2525eeabd9092 a wfprov:Artifact,
        prov:Entity ;
    prov:value "115530*(((B.astype(float)*C.astype(float))/A.astype(float))**2.38)" .

data:c6f40f302effca33768fc256bbb5dedaca044174 a wfprov:Artifact,
        prov:Entity ;
    prov:value "4.26*((C/A)**3.94)" .

data:e059662a461e5d1b245f555149febc699f42b537 a wfprov:Artifact,
        prov:Entity ;
    prov:value "Chlorophyll a" .

data:ee59b16f9fd43ef6b27fa343095d5284d49bddd0 a wfprov:Artifact,
        prov:Entity ;
    prov:value "B04" .

id:0f56a8bd-b5e1-4fb4-b83b-1ff1af10828a a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:cb365be4-5b82-466e-a735-52203624488b ;
            prov:atTime "2026-09-23T08:38:35.793003"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m_2/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:9f9130b688abf761a50ad3c0822794bceda8a4cd ] ;
    cwlprov:basename "B03.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B03" .

id:374994f9-116d-48a7-9749-2f5d0a21702e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:94486889-f9f5-43d5-b151-995baade6da8 ;
            prov:atTime "2026-09-23T08:28:17.439405"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b03_10m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:50ebd5e63205cb9f8e4322e56677b021e540e57d ] ;
    cwlprov:basename "B03.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B03" .

id:3dd21e1d-8350-48e9-bfe0-28b4a15b59ab a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:2140e929-bf51-4666-b8c5-c93b1ba365d6 ;
            prov:atTime "2026-09-23T08:39:38.352561"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m_2/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:e33aada2083b35c0160af06da303c293f90b45cb ] ;
    cwlprov:basename "B03_60m.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "B03_60m" .

id:404675d7-a7d3-463f-8754-35edf2fc0c25 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_chlorophyll_a_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2> ],
        [ a prov:Association ;
            prov:agent id:31508f5e-88d5-4a9b-b917-e0cc6dbe47ec ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:40:34.302789"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:40:32.111555"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:32.121023"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:32.119378"^^xsd:dateTime ;
            prov:entity data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:32.119821"^^xsd:dateTime ;
            prov:entity data:c9795ae1700fc9846a06b4c55a43850d79fc8c37 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:32.121035"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:32.120997"^^xsd:dateTime ;
            prov:entity data:e059662a461e5d1b245f555149febc699f42b537 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:32.119425"^^xsd:dateTime ;
            prov:entity id:883ae32e-c86f-491e-bcaf-320d0badfa08 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:32.120366"^^xsd:dateTime ;
            prov:entity data:3b70ed18810c540d946d852c94d6c9701138000a ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a_2/plot_name> ] .

id:448bbe1c-8732-4d0a-a0b2-01dcf453c5f1 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_turbidity" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity> ],
        [ a prov:Association ;
            prov:agent id:ab87aed1-ceb2-4bf2-9ab2-f5e5de480e7e ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:35:37.417146"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:35:34.726244"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:34.735513"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:34.733267"^^xsd:dateTime ;
            prov:entity id:4e6424db-66b9-4389-81ca-0a3040fbfd07 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:34.733619"^^xsd:dateTime ;
            prov:entity data:f4ad1bd9dbf27a2d94b4320d4ffe146bf714a9d0 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:34.733930"^^xsd:dateTime ;
            prov:entity data:1a0e4fad40b7e324bd7ae77ac30e69a00173cd35 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/plot_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:34.733224"^^xsd:dateTime ;
            prov:entity data:2b0824b4ba24b098adc7ce01881499891c48d2ea ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:34.735498"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:34.735472"^^xsd:dateTime ;
            prov:entity data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity/plot_title> ] .

id:5811cb86-e667-4b42-bd25-995c414a260e a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:2a9686ec-313f-4d80-93b4-f4867c661dd8 ;
            prov:atTime "2026-09-23T08:39:37.315423"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m_2/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:46cf7f768b4167418c8ecec22d3dc976cf2e969e ] ;
    cwlprov:basename "B01.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B01" .

id:667fa027-ed54-41eb-97a1-2dba34cda14d a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_turbidity_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:15e3229d-5bd8-408e-a96a-da5e4356b8d0 ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:40:32.099554"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:40:29.608049"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:29.616450"^^xsd:dateTime ;
            prov:entity id:d0b679db-ef77-442f-a4c0-f093f5da8990 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:29.618454"^^xsd:dateTime ;
            prov:entity data:6a9b80ab0cf720811aa23e47d7915bf82f03f56c ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:29.616392"^^xsd:dateTime ;
            prov:entity data:2b0824b4ba24b098adc7ce01881499891c48d2ea ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:29.617668"^^xsd:dateTime ;
            prov:entity data:9f3f28fc82add0a4e71340746dfbbf9db167a541 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/plot_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:29.618529"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:29.617135"^^xsd:dateTime ;
            prov:entity data:2219e4fef3bb44cade72f7ef4d71d8d686197932 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:40:29.618548"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_turbidity_2/clip_min> ] .

id:6f1095f0-e7c1-47e1-96c0-c8fc3262cbd8 a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_cyanobacteria" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:10162287-984a-45d3-883f-c473d1b9f4e8 ],
        [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria> ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:35:32.104196"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:31:51.394989"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:31:51.724705"^^xsd:dateTime ;
            prov:entity data:4ad2eab867b3280cabc93a14c615ab97b6b6575e ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:31:51.721670"^^xsd:dateTime ;
            prov:entity id:e5d9b324-0df0-444b-b4d9-4e9ccb71c5a7 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:31:51.723272"^^xsd:dateTime ;
            prov:entity id:4b2d89fd-9ef0-45c2-a15e-f2e4c32bc7be ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:31:51.723232"^^xsd:dateTime ;
            prov:entity data:1370052da0755d73768c0c75500107d3759bcc2d ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:31:51.723855"^^xsd:dateTime ;
            prov:entity data:5cd4c929136b7ccfd44b3e4a9e543eaf5497e074 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:31:51.721547"^^xsd:dateTime ;
            prov:entity id:fc882878-31a6-43ba-88a7-5c51bad2cef3 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:31:51.724390"^^xsd:dateTime ;
            prov:entity data:dae6881b456c2247c2fe7bf59cb2d891427f2aec ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria/plot_name> ] .

id:9e684a93-4ee7-4ace-b244-0bbaaa4fb10e a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_chlorophyll_a" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a> ],
        [ a prov:Association ;
            prov:agent id:780ec89d-f9bc-4d68-a37b-36bb3230bca9 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:35:40.163022"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:35:37.443398"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:37.464939"^^xsd:dateTime ;
            prov:entity data:74f86325eb5176eac0be70c602f62dd4be091838 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:37.469289"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:37.463473"^^xsd:dateTime ;
            prov:entity id:12b49a35-ae72-4b3d-933e-b2d03c6692b4 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:37.469223"^^xsd:dateTime ;
            prov:entity data:e059662a461e5d1b245f555149febc699f42b537 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:37.469315"^^xsd:dateTime ;
            prov:entity cwlprov:None ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:37.462789"^^xsd:dateTime ;
            prov:entity data:53dc86e3cbc21ff9ef3ae5a5a8cc9f7d1a9942c8 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:35:37.467615"^^xsd:dateTime ;
            prov:entity data:714bad22665ac25a2625f9795548244c5862c173 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_chlorophyll_a/plot_name> ] .

id:ac7fbdba-ab57-4cab-92ea-86425e0d72da a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f0d8a485-c284-4e61-883c-b97dff3b466f ;
            prov:atTime "2026-09-23T08:29:43.327850"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/download_b01_60m/product> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:4554c3cf3eb5232e005efba0f52710ebf69238d4 ] ;
    cwlprov:basename "B01.tif" ;
    cwlprov:nameext ".tif" ;
    cwlprov:nameroot "B01" .

id:ce4d56e2-f5b3-4c5f-bc54-5eead2341bda a wf4ever:File,
        wfprov:Artifact,
        prov:Entity ;
    prov:qualifiedGeneration [ a prov:Generation ;
            prov:activity id:f6d76af7-483d-4435-9b74-e6f721878714 ;
            prov:atTime "2026-09-23T08:29:45.546400"^^xsd:dateTime ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/reproject_b03_60m/result> ] ;
    provext:qualifiedSpecialization [ a provext:Specialization ;
            provext:generalEntity data:d54118937320f8cd7cb6a0673991c14035966fe7 ] ;
    cwlprov:basename "B03_60m.tiff" ;
    cwlprov:nameext ".tiff" ;
    cwlprov:nameroot "B03_60m" .

id:eb258705-e788-4815-aaa8-8ce9fe8b95bd a wfprov:ProcessRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main/plot_cyanobacteria_2" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2> ],
        [ a prov:Association ;
            prov:agent id:67aa2703-a2a1-434d-9a49-072e268b1de7 ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:40:28.335295"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:39:46.623486"^^xsd:dateTime ;
            prov:hadActivity id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 ] ;
    prov:qualifiedUsage [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:46.630760"^^xsd:dateTime ;
            prov:entity id:f4eb96c4-9178-469a-94da-e74a9ec97592 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/input_image> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:46.629916"^^xsd:dateTime ;
            prov:entity id:43a057a2-41ef-4082-bdfb-fb1186385f7d ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/clip_min> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:46.630723"^^xsd:dateTime ;
            prov:entity data:1370052da0755d73768c0c75500107d3759bcc2d ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/color_scale> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:46.631794"^^xsd:dateTime ;
            prov:entity data:4ad2eab867b3280cabc93a14c615ab97b6b6575e ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/plot_title> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:46.631165"^^xsd:dateTime ;
            prov:entity data:b3573acf1e280c5c49f41a5a84acaedc59c5c096 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/output_name> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:46.629878"^^xsd:dateTime ;
            prov:entity id:a0bf8c1c-f971-418d-9a40-667bb07dd0c4 ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/clip_max> ],
        [ a prov:Usage ;
            prov:atTime "2026-09-23T08:39:46.631484"^^xsd:dateTime ;
            prov:entity data:4ea652b7d22b69e0d27d1a1ebce1e624f55373fd ;
            prov:hadRole <arcp://uuid,39aa9d6c-b92f-486d-9c56-5289ebc57918/workflow/packed.cwl#main/plot_cyanobacteria_2/plot_name> ] .

data:084a442888f71ba66d9e75fde8221f58dfaa6acf a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_29SPC_20190701_0_L2A" .

data:c80240b036ceef4fdcfb684013f5e78f2fd144e7 a wfprov:Artifact,
        prov:Entity ;
    prov:value "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_29SPC_20190701_1_L2A" .

id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 a wfprov:WorkflowEngine,
        prov:Agent,
        prov:SoftwareAgent ;
    rdfs:label "cwltool 3.1.20260108082145" ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:26:24.435717"^^xsd:dateTime ;
            prov:hadActivity id:9e986cfd-629d-41cf-9c75-eb65ae428d71 ] .

id:7a4b06ca-ec17-4eac-bbf7-96ba8af7bd86 a wfprov:WorkflowRun,
        prov:Activity ;
    rdfs:label "Run of workflow/packed.cwl#main" ;
    prov:qualifiedAssociation [ a prov:Association ;
            prov:agent id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ;
            prov:hadPlan wf:main ] ;
    prov:qualifiedEnd [ a prov:End ;
            prov:atTime "2026-09-23T08:35:40.173908"^^xsd:dateTime ;
            prov:hadActivity id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ],
        [ a prov:End ;
            prov:atTime "2026-09-23T08:40:34.311473"^^xsd:dateTime ;
            prov:hadActivity id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ] ;
    prov:qualifiedStart [ a prov:Start ;
            prov:atTime "2026-09-23T08:26:24.435762"^^xsd:dateTime ;
            prov:hadActivity id:2eaf041b-2988-4cd3-bd1b-2c3f2028e2c8 ] ;
    prov:startedAtTime "2026-09-23T08:26:24.435738"^^xsd:dateTime .

cwlprov:None a prov:Entity ;
    rdfs:label "None" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Profile of the OGC API - Processes processDescription of `plot-image`
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
      const: plot-image
      x-jsonld-id: '@id'
    inputs:
      type: object
      required:
      - input_image
      - color_scale
      - output_name
      - plot_name
      - plot_title
      - clip_min
      - clip_max
      propertyNames:
        enum:
        - input_image
        - color_scale
        - output_name
        - plot_name
        - plot_title
        - clip_min
        - clip_max
      x-jsonld-id: https://w3id.org/ogc/api/processes/inputs
      x-jsonld-vocab: https://geolabs.github.io/bblocks-process-profiles/def/input/
    outputs:
      type: object
      required:
      - output_file
      - output_plot
      propertyNames:
        enum:
        - output_file
        - output_plot
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
        - input_image
        - color_scale
        propertyNames:
          enum:
          - input_image
          - color_scale
          - output_name
          - plot_name
          - plot_title
          - clip_min
          - clip_max
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
          - output_file
          - output_plot
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
      - output_file
      - output_plot
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

* YAML version: [schema.yaml](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/schema.json)
* JSON version: [schema.json](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/schema.yaml)


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
[context.jsonld](https://geolabs.github.io/bblocks-process-profiles/build/annotated/process-profiles/algae-bloom/plot-image/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/GeoLabs/bblocks-process-profiles](https://github.com/GeoLabs/bblocks-process-profiles)
* Path: `_sources/algae-bloom/plot-image`

