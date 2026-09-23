Process profile of **`crop`** (CommandLineTool, W3 Water Bodies).

> Crop a Sentinel-2 COG band to an area of interest

## Source

- CWL: [app-water-bodies-cloud-native.cwl#crop](https://github.com/gfenoy/mastering-app-package/blob/40ecc096da56c6810758b87b01a87502f7c4507c/cwl-workflow/app-water-bodies-cloud-native.cwl#crop) (pinned commit `40ecc09`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Data retrieval
- EOAP CWL custom types used: none; candidates: `eoap.cct.bbox`, `eoap.cct.stac`, `eoap.cct.string-format`
- Used by: `ospd.process-profiles.water-bodies.detect-water-body`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `item` | string | `cropped` | File |
| `aoi` | string |  |  |
| `epsg` | string |  |  |
| `band` | string |  |  |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/crop:1.5.0`.
Reads one asset of the given STAC item directly over the network (`NetworkAccess`; no `File`
input -- `item` is a plain STAC item URL string), windowed-reads and reprojects the requested
`band` to `epsg` cropped to `aoi`, writes one GeoTIFF (`crop_<band>.tif`).

**CWL specifics.** `item`, `aoi`, `epsg`, `band` are all plain strings: `item` is a STAC Item
URL (candidate `eoap.cct.stac` or `eoap.cct.string-format`), `aoi` a comma-separated bbox
(candidate `eoap.cct.bbox`, but as one string, not the object EOAP's own BBox type expects).
`band` is an unconstrained string (`green`, `nir`, ...), not an enum: any STAC asset key the
item happens to expose is accepted, so an invalid band name fails only at execution.

**Provenance.** No input is a `File`: `aoi`/`epsg`/`item`/`band` are literal-valued entities;
the network fetch itself leaves no provenance trace beyond the output file (GP-3, GP-4).

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (mastering-app-package 40ecc09 `app-water-bodies-cloud-native.cwl#water-bodies`), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out` against a locally patched copy (U-06), 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_crop` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: closeMatch.** load_collection with a spatial_extent (aoi) and a single band selected (filter_bands); the STAC item is given by URL rather than resolved by collection/date/bbox search, and the windowed COG read (no full download) is an implementation detail openEO back-ends make transparently.

- `closeMatch`: `ogc.openeo.processes.cubes.load_collection`, `ogc.openeo.processes.cubes.filter_bands`

## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/crop` (`ospd.process-profiles.process-type`), status `submitted`.
