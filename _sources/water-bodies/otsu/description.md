Process profile of **`otsu`** (CommandLineTool, W3 Water Bodies).

> Otsu binary threshold

## Source

- CWL: [app-water-bodies-cloud-native.cwl#otsu](https://github.com/gfenoy/mastering-app-package/blob/40ecc096da56c6810758b87b01a87502f7c4507c/cwl-workflow/app-water-bodies-cloud-native.cwl#otsu) (pinned commit `40ecc09`, license <https://spdx.org/licenses/CC-BY-SA-4.0>). Referenced, not copied.
- Six-phase position: Scientific computation
- EOAP CWL custom types used: none
- Used by: `ospd.process-profiles.water-bodies.detect-water-body`

| Input | CWL type | Output | CWL type |
|---|---|---|---|
| `raster` | File | `binary_mask_item` | File |

## Analysis

**Behaviour.** `python -m app`, `ghcr.io/terradue/ogc-eo-application-package-hands-on/otsu:1.5.0`.
Computes an Otsu threshold on the input raster's histogram and writes a binary (water /
not-water) mask GeoTIFF (`otsu.tif`).

**Provenance.** One file input, one file output.

## processDescription derivation

Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct `291a741`, inline variant).

No manual correction: the example is the unmodified transform output.

## Provenance view

Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation.hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal parameters carry `value`, files carry `links`) and the engine / container image as `prov:SoftwareAgent`.
The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the generic profile has no step-level run (GP-1).

Gaps met here are listed in `docs/PROVENANCE-GAPS.md`.

Execution and provenance examples are built from a real `cwltool --provenance` run (CWLProv research object `water-bodies`: the pinned W3 source itself (mastering-app-package 40ecc09 `app-water-bodies-cloud-native.cwl#water-bodies`), inputs from that source's own `water-bodies/params.yml`, run with `cwltool --enable-ext --provenance ro --outdir out` against a locally patched copy (U-06), 2026-09-23, cwltool 3.1.20260108082145 on an arm64 macOS host, ~9 min; two STAC items scattered (S2B_10TFK_20210713_0_L2A then S2A_10TFK_20220524_0_L2A), each over 2 bands (green, nir)), activity `main/node_otsu` (scatter iteration 1, engine cwltool 3.1.20260108082145). Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment.

## openEO equivalence

**Level: none.** openEO has no built-in Otsu (automatic histogram) threshold process; the closest primitive, `ogc.openeo.processes.comparison.gt`, only compares against a caller-supplied constant, not a threshold the process computes itself.


## Process type (Activity 4)

Candidate entry `https://geolabs.github.io/bblocks-process-profiles/def/process-type/water-bodies/otsu` (`ospd.process-profiles.process-type`), status `submitted`.
