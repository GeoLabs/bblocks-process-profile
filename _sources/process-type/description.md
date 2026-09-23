Schema of a **candidate process-type register entry** (OSPD Activity 4).

A process type classifies the activities recorded in provenance. The link is one-way and uses
plain W3C PROV: a provenance `Activity` (or a `wfprov:ProcessRun` / `wfprov:WorkflowRun`) of this
type carries the entry `id` in `activityType`. The entry itself is a SKOS concept:

- `phase` (→ `skos:broader`) positions the process in the six-phase framework
  (filter configuration → selection/filtering → data retrieval → pre-processing →
  scientific computation → export/aggregation);
- `exactMatch` / `closeMatch` / `relatedMatch` (→ SKOS mapping properties) point to openEO
  Building Blocks (`https://www.opengis.net/def/bblocks/ogc.openeo.*`);
- `openeoEquivalence.level` states the equivalence level explicitly, including `none`, which
  SKOS cannot express, with the rationale and, for composite or opaque processes, a
  stage-by-stage decomposition.

Status values follow ISO 19135. Entries in this register are candidates: at most `submitted`.

The `pp:` vocabulary (`https://geolabs.github.io/bblocks-process-profiles/def/`) and the phase IRIs
are provisional, pending a decision on the process-type register namespace.
