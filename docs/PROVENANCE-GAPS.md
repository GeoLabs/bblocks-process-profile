# Gaps in `bblocks-generic-provenance-profile`

Candidate improvements to GeoLabs/bblocks-generic-provenance-profile (`ogc.bbr.provenance.*`,
commit `7ce65fc`), found while expressing the 13 process profiles as instances of it. They are
**recorded, not worked around locally**: no field was added to the generic profile, and nothing in
this register redefines PROV. Where an incubator Building Block had to be used directly, it is said
so.

How the profiles use the generic profile:

- every profile has a provenance chain validated against `ogc.bbr.provenance.provenance`
  (W3C PROV chain via `ogc.ogc-utils.prov`);
- W1 workflows also have an `ogc.bbr.provenance.execution` bundle (run + engine + output
  artifacts with the real SHA-1 checksums from the CRIM cwltool logs);
- CommandLineTools also have a run record validated against `ogc.bbr.wf4ever.wfprov.ProcessRun`
  (incubator/Wf4Ever, see GP-1).

| ID | Gap | Met in | What was done here | Candidate improvement |
|---|---|---|---|---|
| GP-1 | No step-level run: only `workflow-run` (`wfprov:WorkflowRun`) is profiled | all 8 CommandLineTools | run record validated against `ogc.bbr.wf4ever.wfprov.ProcessRun` directly, with `wasPartOfWorkflowRun` | add `process-run` profiling `wfprov:ProcessRun` (same required links as `workflow-run`: process description, engine, times, status) |
| GP-2 | No link from a run to what was run beyond `describedByWorkflow`: nothing ties an Activity to a process-type register entry (Activity 4) or to the OGC processDescription | all | plain PROV used: `activityType` = process-type IRI; `qualifiedAssociation.hadPlan` = processDescription URL | make `activity` / `workflow-run` require `activityType` pointing to a process-type entry, and document `hadPlan` → processDescription |
| GP-3 | `eoap-artifact` requires `wasOutputFrom` (and `checksum`) even for `role: input`, so workflow inputs that no run produced (the AOI GeoJSON, a remote STAC Item) cannot be recorded; the profile's own example invents an upstream "ingest" run | W1 workflows (`aoi`), download steps | `execution` bundles list outputs only; inputs appear in the provenance chain as plain entities | make `wasOutputFrom` required only for `role: output|intermediate`; allow `wasDerivedFrom` / `hadPrimarySource` for external inputs |
| GP-4 | No parameter (literal value) entity: bbox, dates, cloud cover, band name, `calc` expression, `color_scale`, `string[]` outputs | all 13 | plain `prov:Entity` with `value` (available in `ogc.ogc-utils.prov-entity`) | add a `parameter` profile (Wf4Ever `wfdesc:Parameter` / `roterms:WorkflowValue`) binding a value to the processDescription input/output name |
| GP-5 | No convention for secrets (`cwltool:Secrets`): nothing says a value was withheld | `download-band-sentinel2-product-safe`, Copernicus workflows | entity recorded without `value` | explicit redaction marker (e.g. `redacted: true`) so that absence of value is not ambiguous |
| GP-6 | No software identity for the container: no image reference / digest on an agent | all (W1 images are unregistered local tags, `reproject-image` has no tag at all — which makes the pinned W1 package non-runnable as published, see `DEVIATIONS.md` U-03; W2 uses a tag, not a digest) | image recorded as a `prov:SoftwareAgent` named after the image reference, now taken from the run record (`cwlprov:image`) | agent profile with `image` and `digest` (and engine version), since the digest is what makes a rerun reproducible |
| GP-7 | Placeholder IRIs `https://example.org/bblocks-provenance/def/*` for `role`, `mediaType`, `status`, `jobID` | `execution` bundles | used as is | publish a vocabulary (or reuse `dcat:mediaType`, OGC API job status) |
| GP-8 | **Resolved 2026-09-23, not just documented.** `ogc.bbr.provenance.*` (`GeoLabs/bblocks-generic-provenance-profile`) imported `ogcincubator.github.io/bblocks-eoap-cct` while this register imports `geolabs.github.io/bblocks-eoap-cct` directly — both publish the same 5 `eoap.cct.*` identifiers. `bblocks-postprocess` merges imports with a plain `dict[identifier] = bblock` and no duplicate check (`ImportedBuildingBlocks.load`, confirmed by reading the source); its breadth-first import queue processes this register's own (level-0) imports before generic-provenance-profile's transitive (level-1) ones, so the ogcincubator copy was silently overwriting the GeoLabs one for all 5 identifiers, with no warning anywhere in the build log. Fixed at the source: `bblocks-generic-provenance-profile`'s own `bblocks-config.yaml` now imports `geolabs.github.io/bblocks-eoap-cct` (commit `a03f0e3`) | register config, transitively | fixed in `GeoLabs/bblocks-generic-provenance-profile` | — |
| GP-9 | `checksum` exists only on `eoap-artifact`: the PROV-chain view cannot carry the checksums the engine reports | all file outputs | checksums only in the W1 `execution` bundles | allow `checksum` on the `entity` profile |
| GP-10 | `checksum` is mandatory on `eoap-artifact`, and a `Directory` / STAC stage-out has no single checksum | `kindgrove.mangrove-workflow` | since 2026-09-23 the `execution` bundle lists **one artifact per file of the directory** (`catalog.json`, the Item, `mangrove_mask.tif`, the two CSV), each with the SHA-1 that CWLProv records for it, all `describedByParameter` `#outputs/stac`. The directory itself has no artifact | make `checksum` conditional (files), or accept a manifest checksum for directories; alternatively profile a directory artifact whose members carry the checksums |
| GP-11 | Mixed JSON-LD keys: `execution.engine` (Wf4Ever `WorkflowEngine`) requires `@id`/`@type`, while `run` and artifacts use `id`/`type` | `execution` bundles | followed as required | align on `id`/`type` in the Wf4Ever `WorkflowEngine` schema |
| GP-12 | `ogc.ogc-utils.prov-activity` `Usage` has no `hadRole`, so a used entity cannot be bound to the input name through `qualifiedUsage` (upstream in bblock-prov-schema, inherited by the generic profile) | all | convention: `entityType` = `<processDescription URL>#inputs/<name>` or `#outputs/<name>` | add `hadRole` to `Usage` / `Generation` upstream, then use `qualifiedUsage.hadRole` |
| GP-13 | `workflow-run` requires `endedAtTime`; cwltool logs (without `--timestamps`) give neither end times nor timezone | W1 workflows | `endedAtTime` = start of the last job (lower bound), timestamps from cidfile names written as UTC | keep the requirement, but document which engine source is authoritative (ZOO-Project-DRU job status gives both) |

## Incubator provenance Building Blocks — what was used

| Building Block | Used? | Why |
|---|---|---|
| `ogc.ogc-utils.prov*` (bblock-prov-schema) | yes, through `ogc.bbr.provenance.provenance` | the PROV chain; its July 2026 additions (qualified influences, derivations) are inherited |
| `ogc.bbr.wf4ever.wfprov.ProcessRun` | yes, directly | GP-1 |
| `ogc.profiles.prov.cwl` (prov-cwl) | no | its schema is a bare `$ref` to `ogc.ogc-utils.prov`; its Turtle → PROV-JSON transform is the natural way to turn `cwltool --provenance` output into these examples once real runs exist |
| `ogc.osc.ontology.cwlprov` | no | stub, no content |
| `ogc.osc.api-profiles.processes.*` | no (seeAlso only) | API-level profiles; the profiles here are process-level |
| `KindGroveProvenance.ttl` (geodcat-stac-earthcode experiments example) | no | describes 9 notebook-cell processes; the deployable CWL exposes one (see `kindgrove.mangrove`) |
