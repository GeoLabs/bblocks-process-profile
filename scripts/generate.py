#!/usr/bin/env python3
"""Generate the process-profile Building Blocks of bblocks-process-profiles.

Semi-automated pipeline (Step 3):
  1. read each CWL process from a local clone of its pinned source (never downloaded here);
  2. isolate it (packed $graph elements inherit the document-level keys, see docs/DEVIATIONS.md M-03);
  3. apply the eoap.cct.cwl-to-ogcprocess jq transform (unchanged, from a local clone of bblocks-eoap-cct);
  4. apply the documented manual corrections (M-01, M-02, M-04) and keep the raw output next to them;
  5. template the provenance view, process-type entry, openEO links, execution examples and docs
     from scripts/profiles.yaml (the Step 0 table) and from real `cwltool --provenance` run records
     (scripts/sources.yaml `runs:`, local research objects, never downloaded).

Usage:
  python3 scripts/generate.py --sources-root DIR [--w1 DIR] [--w2 DIR]

DIR must contain clones named as in scripts/sources.yaml (`clone:`), or pass --w1/--w2 explicitly.
Generated files under _sources/<workflow>/<process>/ are overwritten.
"""
import argparse
import copy
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
BASE = "https://geolabs.github.io/bblocks-process-profiles/def/"
PTYPE_SCHEME = BASE + "process-type"
PHASE_BASE = BASE + "phase/"
BBLOCK_IRI = "https://www.opengis.net/def/bblocks/"
PREFIX = "ospd.process-profiles."
TODAY = "2026-09-22"
PART1_CORE = "http://www.opengis.net/spec/ogcapi-processes-1/1.0/conf/core"

PHASE_LABELS = {
    "filter-configuration": "Filter configuration",
    "selection-filtering": "Selection / filtering",
    "data-retrieval": "Data retrieval",
    "pre-processing": "Pre-processing",
    "scientific-computation": "Scientific computation",
    "export-aggregation": "Export / aggregation",
}

# CWL `format` IRIs (after namespace expansion) -> media types (M-01)
FORMAT_MEDIA = {
    "http://www.opengis.net/def/media-type/ogc/1.0/geotiff": "image/tiff; application=geotiff",
    "https://www.iana.org/assignments/media-types/image/tiff": "image/tiff",
    "https://www.iana.org/assignments/media-types/image/jp2": "image/jp2",
    "https://www.iana.org/assignments/media-types/image/png": "image/png",
    "https://www.iana.org/assignments/media-types/application/geo+json": "application/geo+json",
}


PROCESS_BASE = BASE + "process/"

# JSON-LD context written next to every profile Building Block (context.jsonld).
#
# Without one, bblocks-postprocess derives a context from the annotated schema alone. The
# OGC API - Processes schemas carry almost no x-jsonld-* annotations, so that derived context
# binds none of the properties the examples actually use, every snippet uplifts to an empty
# RDF graph, and the validator reports each one as an error ("**Empty** output Turtle", which
# is hard-coded as is_error and cannot be switched off).
#
# Terms that match no schema property are still emitted, as x-jsonld-extra-terms, so this one
# context also covers the payloads that only exist under $defs: ogcapppkg, execute, results,
# provenance, process-run and process-type.
#
# @vocab is not optional here: the keys of results.json are the process's own output names and
# cannot be enumerated up front. It is re-scoped under inputs/outputs/usedInput so that an
# arbitrary CWL parameter name -- an input literally called `name`, for instance -- cannot be
# captured by a vocabulary term.
PROFILE_CONTEXT = {
    "@context": {
        "@version": 1.1,
        "@vocab": BASE,
        "pp": BASE,
        "proc": "https://w3id.org/ogc/api/processes/",
        "prov": "http://www.w3.org/ns/prov#",
        "dct": "http://purl.org/dc/terms/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "wfprov": "http://purl.org/wf4ever/wfprov#",
        "oa": "http://www.w3.org/ns/oa#",

        "id": "@id",
        # `type` must be claimed here: the inherited /links/type binding (proc:type) is
        # otherwise hoisted to the root and turns every `type` into a literal. Scoping
        # `links` below (as the upstream provenance contexts do) frees the root term.
        "type": "@type",
        "ProcessRun": "wfprov:ProcessRun",
        "WorkflowRun": "wfprov:WorkflowRun",
        "WorkflowEngine": "wfprov:WorkflowEngine",
        "Artifact": "wfprov:Artifact",
        "ProcessType": "skos:Concept",

        # processDescription (OGC API - Processes Part 1)
        "title": "dct:title",
        "description": "dct:description",
        "keywords": "dct:subject",
        "version": "pp:version",
        "mutable": "proc:mutable",
        "jobControlOptions": "proc:jobControlOptions",
        "outputTransmission": "proc:outputTransmission",
        "metadata": "proc:metadata",
        "role": {"@id": "proc:role", "@type": "@id"},
        "inputs": {"@id": "proc:inputs", "@context": {"@vocab": BASE + "input/"}},
        "outputs": {"@id": "proc:outputs", "@context": {"@vocab": BASE + "output/"}},
        "links": {"@id": "rdfs:seeAlso", "@context": {
            "href": {"@id": "oa:hasTarget", "@type": "@id"},
            "rel": {"@id": "http://www.iana.org/assignments/relation", "@type": "@id",
                    "@context": {"@base": "http://www.iana.org/assignments/relation/"}},
            "type": "dct:type", "title": "rdfs:label"}},
        "response": "proc:response",

        # ogcapppkg (Part 2) / results / execution bundle
        "executionUnit": "proc:executionUnit",
        "processDescription": "pp:processDescription",
        "result": "pp:result",
        "engine": "pp:engine",
        "run": "pp:run",

        # provenance view (W3C PROV) -- same bindings as ogc.bbr.provenance.provenance:
        # activityType / entityType are rdf:types, not pp: properties
        "provType": {"@id": "@type", "@type": "@vocab"},
        "provName": "rdfs:label",
        "activityType": {"@id": "@type", "@type": "@id"},
        "entityType": {"@id": "@type", "@type": "@id"},
        "used": {"@id": "prov:used", "@type": "@id"},
        "wasAssociatedWith": {"@id": "prov:wasAssociatedWith", "@type": "@id"},
        "wasGeneratedBy": {"@id": "prov:wasGeneratedBy", "@type": "@id"},
        "wasDerivedFrom": {"@id": "prov:wasDerivedFrom", "@type": "@id"},
        "wasAttributedTo": {"@id": "prov:wasAttributedTo", "@type": "@id"},
        "qualifiedAssociation": {"@id": "prov:qualifiedAssociation"},
        "agent": {"@id": "prov:agent", "@type": "@id"},
        "hadPlan": {"@id": "prov:hadPlan", "@type": "@id"},
        "startedAtTime": {"@id": "prov:startedAtTime", "@type": "xsd:dateTime"},
        "endedAtTime": {"@id": "prov:endedAtTime", "@type": "xsd:dateTime"},
        "value": "rdf:value",

        # process run / execution bundle -- same bindings as the Wf4Ever bblocks
        # (ogc.bbr.wf4ever.wfprov.ProcessRun / WorkflowRun) and ogc.bbr.provenance.execution
        "describedByProcess": {"@id": "wfprov:describedByProcess", "@type": "@id"},
        "describedByWorkflow": {"@id": "wfprov:describedByWorkflow", "@type": "@id"},
        "usedInput": {"@id": "wfprov:usedInput", "@type": "@id"},
        "wasEnactedBy": {"@id": "prov:wasAssociatedWith", "@type": "@id"},
        "wasPartOfWorkflowRun": {"@id": "wfprov:wasPartOfWorkflowRun", "@type": "@id"},
        "hadSubProcessRun": {"@id": "wfprov:hadSubProcessRun", "@type": "@id"},
        "wasOutputFrom": {"@id": "prov:generated", "@type": "@id"},

        # process-type register entry (mirrors _sources/process-type/context.jsonld)
        "prefLabel": "skos:prefLabel",
        "definition": "skos:definition",
        "inScheme": {"@id": "skos:inScheme", "@type": "@id"},
        "status": "pp:status",
        "phase": {"@id": "skos:broader", "@type": "@id"},
        "profile": "pp:profile",
        "source": "pp:source",
        "cwl": {"@id": "pp:cwl", "@type": "@id"},
        "cwlClass": "pp:cwlClass",
        "cwlId": "pp:cwlId",
        "provenanceClass": {"@id": "pp:provenanceClass", "@type": "@id"},
        "cctDependencies": "pp:cctDependency",
        "candidateCctDependencies": "pp:candidateCctDependency",
        "hasStep": {"@id": "pp:hasStep", "@type": "@id"},
        "exactMatch": {"@id": "skos:exactMatch", "@type": "@id"},
        "closeMatch": {"@id": "skos:closeMatch", "@type": "@id"},
        "relatedMatch": {"@id": "skos:relatedMatch", "@type": "@id"},
        "openeoEquivalence": "pp:openeoEquivalence",
        "level": "pp:equivalenceLevel",
        "rationale": "pp:rationale",
        "decomposition": {"@id": "pp:decomposition", "@container": "@list"},
        "stage": "pp:stage",
        "openeo": "pp:openeo",
        "note": "skos:note",
    }
}


# ------------------------------------------------------------------ helpers

def dump_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def dump_yaml(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100))


def cwl_items(section):
    """CWL inputs/outputs as an ordered dict, whatever the source form (map or list)."""
    if isinstance(section, dict):
        return {k: (v if isinstance(v, dict) else {"type": v}) for k, v in section.items()}
    return {i["id"].split("#")[-1].split("/")[-1]: i for i in section or []}


def expand(value, ns):
    if isinstance(value, str) and ":" in value and not value.startswith("http"):
        p, local = value.split(":", 1)
        if p in ns:
            return ns[p] + local
    return value


def is_optional(t):
    return (isinstance(t, str) and t.endswith("?")) or (isinstance(t, list) and "null" in t)


def base_type(t):
    if isinstance(t, str):
        return t.rstrip("?")
    if isinstance(t, list):
        nn = [x for x in t if x != "null"]
        return base_type(nn[0]) if len(nn) == 1 else nn
    if isinstance(t, dict):
        return t.get("type")
    return t


def _qn(v):
    return v.get("$") if isinstance(v, dict) else v


def _lst(v):
    return v if isinstance(v, list) else [v]


MEDIA_BY_EXT = {".tiff": "geotiff", ".tif": "geotiff", ".png": "png", ".jp2": "jp2",
                ".geojson": "geojson", ".json": "application/json", ".csv": "text/csv"}


def load_bag(path: Path):
    """Read a `cwltool --provenance` research object (CWLProv 0.6, BagIt).

    Returns the engine, and every activity of every bundle with its plan (`main/step[_N]`), the
    container image, UTC start/end and typed inputs/outputs: a literal (`value`), a file
    (`file`, `sha1`, `size`), a directory (`dir`, `files` listed recursively with relative
    paths) or a list. Two cwltool behaviours are handled here so that nothing else has to know
    about them: `prov:time` is naive local time, so the offset is taken from the engine log,
    which is UTC; and a run that failed inside a scatter has no primary bundle, so all
    `*.cwlprov.json` bundles are read and each activity remembers the scatter iteration of the
    bundle it came from (bundle name suffix `_2`, `_3`, ...; the first iteration has none)."""
    prov_dir = path / "metadata" / "provenance"
    bundles = {}
    for f in sorted(prov_dir.glob("*.cwlprov.json")):
        stem = f.name.split(".", 1)[0]
        if stem == "primary":
            iteration = None
        else:
            m = re.search(r"_(\d+)$", stem)
            iteration = int(m.group(1)) if m else 1
        bundles[iteration if iteration is not None else "primary"] = (f.name, json.loads(f.read_text()))
    if not bundles:
        sys.exit(f"{path}: no *.cwlprov.json bundle found")

    sizes = {p.name: p.stat().st_size for p in (path / "data").rglob("*") if p.is_file()}

    # UTC offset: engine log line for the workflow start vs the earliest prov:time
    offset = timedelta(0)
    logs = list((path / "metadata" / "logs").glob("engine.*.txt"))
    m = logs and re.search(r"\[(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d),\d+\.\d+Z\] \[workflow \] start",
                           logs[0].read_text())
    starts = [datetime.fromisoformat(_qn(v["prov:time"]))
              for _, b in bundles.values() for vv in b.get("wasStartedBy", {}).values() for v in _lst(vv)
              if v.get("prov:time")]
    if m and starts:
        delta = min(starts) - datetime.fromisoformat(m.group(1))
        offset = timedelta(seconds=round(delta.total_seconds() / 900) * 900)

    def utc(t):
        if not t:
            return None
        return (datetime.fromisoformat(_qn(t)) - offset).strftime("%Y-%m-%dT%H:%M:%SZ")

    engine = None
    activities = []
    for iteration, (bundle_name, d) in bundles.items():
        agents = {k: _lst(v)[0] for k, v in d.get("agent", {}).items()}
        ents = {k: _lst(v)[0] for k, v in d.get("entity", {}).items()}
        general = {}
        for vv in d.get("specializationOf", {}).values():
            for v in _lst(vv):
                general[v.get("prov:specificEntity")] = v.get("prov:generalEntity")
        members = {}  # prov:hadMember is a top-level relation in PROV-JSON, not an entity attribute
        for vv in d.get("hadMember", {}).values():
            for v in _lst(vv):
                members.setdefault(v.get("prov:collection"), []).append(v.get("prov:entity"))
        for ag in agents.values():
            label = ag.get("prov:label", "")
            if label.startswith("cwltool ") and engine is None:
                engine = {"name": "cwltool", "version": label.split()[1]}

        def artefact(eid, prefix=""):
            e = ents.get(eid, {})
            base = e.get("cwlprov:basename")
            if "prov:hadDictionaryMember" in e:
                pairs = [ents.get(_qn(mm), {}) for mm in _lst(e["prov:hadDictionaryMember"])]
                if base is None:  # a CWL record (e.g. the EOAP BBox), not a directory
                    return {"record": {p.get("prov:pairKey"): artefact(_qn(p.get("prov:pairEntity"))) for p in pairs}}
                files = []
                for p in pairs:
                    child = artefact(_qn(p.get("prov:pairEntity")), prefix + p.get("prov:pairKey", "") + "/")
                    if "file" in child:
                        files.append({"path": prefix + p.get("prov:pairKey"), "sha1": child["sha1"], "size": child["size"]})
                    elif "dir" in child:
                        files += child["files"]
                return {"dir": base, "files": sorted(files, key=lambda x: x["path"])}
            if eid in members and base is None:
                return {"list": [artefact(mm) for mm in members[eid]]}
            if "prov:value" in e:
                return {"value": _qn(e["prov:value"])}
            sha = eid[5:] if eid.startswith("data:") else (general.get(eid, "")[5:] if str(general.get(eid, "")).startswith("data:") else None)
            if base or sha:
                return {"file": base, "sha1": sha, "size": sizes.get(sha)}
            return {}

        for aid, a in d.get("activity", {}).items():
            a = _lst(a)[0]
            rec = {"id": aid, "iteration": iteration, "bundle": bundle_name, "plan": None, "image": None,
                   "start": None, "end": None, "inputs": {}, "outputs": {}}
            for vv in d.get("wasStartedBy", {}).values():
                for v in _lst(vv):
                    if v.get("prov:activity") == aid:
                        rec["start"] = utc(v.get("prov:time"))
            for vv in d.get("wasEndedBy", {}).values():
                for v in _lst(vv):
                    if v.get("prov:activity") == aid:
                        rec["end"] = utc(v.get("prov:time"))
            for vv in d.get("wasAssociatedWith", {}).values():
                for v in _lst(vv):
                    if v.get("prov:activity") != aid:
                        continue
                    if v.get("prov:plan"):
                        rec["plan"] = _qn(v["prov:plan"]).split(":", 1)[-1]
                    img = agents.get(v.get("prov:agent"), {}).get("cwlprov:image")
                    if img:
                        rec["image"] = img
            for rel, key in (("used", "inputs"), ("wasGeneratedBy", "outputs")):
                for vv in d.get(rel, {}).values():
                    for v in _lst(vv):
                        if v.get("prov:activity") == aid and v.get("prov:role"):
                            rec[key][_qn(v["prov:role"]).rsplit("/", 1)[-1]] = artefact(v.get("prov:entity"))
            activities.append(rec)
    return {"path": str(path), "engine": engine, "activities": activities}


def w3c_prov_example(info, exd: Path):
    """The run record as W3C PROV-JSONLD: the CWLProv bundle that holds this profile's activity,
    re-serialised without loss by the `prov` library (>= 2, the PROV-JSONLD serializer). The
    result validates against ogc.ogc-utils.prov.w3c-prov-jsonld and is read as RDF through its
    own context, which makes it the one example whose PROV-O graph is cwltool's, not this
    register's. PROV-JSONLD cannot carry prov:Mention (dropped from PROV-DM's Recommendation; the
    serializer raises), so the mentions cwltool writes for its nested bundles become
    specializationOf + prov:asInBundle, the workaround documented by that building block."""
    src = Path(info["prov"]["path"]) / "metadata" / "provenance" / info["activity"]["bundle"]
    try:
        from prov.model import ProvDocument, PROV
        from prov.serializers import Registry
        Registry.load_serializers()
        if "jsonld" not in Registry.serializers:
            raise ImportError("no PROV-JSONLD serializer")
    except ImportError as e:
        sys.exit(f"the W3C PROV-JSONLD examples need the `prov` library >= 2 ({e}): pip install 'prov>=2'")
    doc = ProvDocument.deserialize(str(src), format="json")

    def demention(bundle):
        for r in list(bundle.get_records()):
            if r.get_type() == PROV["Mention"]:
                bundle._records.remove(r)
                specific, general, in_bundle = (r.formal_attributes[i][1] for i in range(3))
                bundle.specialization(specific, general).add_attributes({PROV["asInBundle"]: in_bundle})
    demention(doc)
    for b in doc.bundles:
        demention(b)
    doc.serialize(str(exd / "cwlprov.jsonld"), format="jsonld", indent=2)


def bag_activity(bag, step, iteration):
    """The activity a profile's `run: {prov, step, iteration}` designates.

    `step` is the plan leaf (`calculate_turbidity`, `select_products`, or `main` for a
    sub-workflow re-rooted in its own bundle); `iteration` selects the scatter iteration bundle
    (1 = first, unsuffixed; N>1 = bundle and step names carry `_N`); no iteration = primary."""
    want_it = iteration if iteration is not None else "primary"
    leaf = step or "main"
    if isinstance(want_it, int) and want_it > 1 and leaf != "main":
        leaf = f"{leaf}_{want_it}"
    for a in bag["activities"]:
        if a["iteration"] == want_it and a["plan"] and a["plan"].rsplit("/", 1)[-1] == leaf:
            return a
    sys.exit(f"{bag['path']}: no activity for step={step!r} iteration={iteration!r} "
             f"(have {[a['plan'] for a in bag['activities'] if a['iteration'] == want_it]})")


def _ref(art, base, hint, d):
    """One artefact of the run record as an OGC results value."""
    if "file" in art:
        mt = hint.get("type") if isinstance(hint, dict) else None
        return {"href": f"{base}/{art['file']}", "type": media(mt or MEDIA_BY_EXT.get(Path(art["file"]).suffix, "application/octet-stream"), d)}
    if "dir" in art:  # the entry point inside the directory is named by the profile
        return {"href": f"{base}/{hint['href']}", "type": media(hint["type"], d)}
    if "list" in art:
        return [_ref(x, base, hint, d) for x in art["list"]]
    return art.get("value")


def _files_in(art):
    if "file" in art:
        return [{"path": art["file"], "sha1": art["sha1"], "size": art["size"]}]
    if "dir" in art:
        return art["files"]
    if "list" in art:
        return [f for x in art["list"] for f in _files_in(x)]
    return []


# ------------------------------------------------------------------ CWL loading and transform

def load_process(proc, sources, roots):
    src = sources[proc["source"]["repo"]]
    path = roots[proc["source"]["repo"]] / src["base_path"] / proc["source"]["file"]
    doc = yaml.safe_load(path.read_text())
    element = proc["source"].get("element")
    url = f"{src['repo']}/blob/{src['commit']}/{src['base_path']}/{proc['source']['file']}"
    if not element:
        return doc, doc, url
    top = {k: v for k, v in doc.items() if k != "$graph"}
    el = next(e for e in doc["$graph"] if e.get("id") == element)
    if el.get("class") == "Workflow":
        # the transform itself selects the first Workflow of the packed document
        return doc, el, url + "#" + element
    iso = copy.deepcopy(top)  # M-03: tool inherits document-level annotations
    iso.update(copy.deepcopy(el))
    return iso, el, url + "#" + element


def run_transform(cwl_doc, jq_path: Path):
    r = subprocess.run(["jq", "-f", str(jq_path)], input=json.dumps(cwl_doc),
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


STAC_CATALOG_SCHEMA = {
    "type": "object",
    "required": ["type", "stac_version", "id", "description", "links"],
    "properties": {
        "type": {"type": "string", "enum": ["Catalog"]},
        "stac_version": {"type": "string"},
        "id": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "links": {"type": "array"},
    },
    "format": "stac-catalog",
}


def correct(pd, cwl_el, ns, secrets, stac_catalog=()):
    """Apply documented manual corrections. Returns (corrected pd, list of corrections)."""
    pd = copy.deepcopy(pd)
    notes = []
    for name in stac_catalog or ():
        schema = pd.get("outputs", {}).get(name, {}).get("schema", {})
        if schema.get("properties", {}).get("type", {}).get("enum") == ["Collection"]:
            pd["outputs"][name]["schema"] = copy.deepcopy(STAC_CATALOG_SCHEMA)
            notes.append(f"M-05 outputs.{name}: the Directory output is a STAC Catalog written by the tool itself "
                         "(run record: `catalog.json` with one Item), not the Collection assumed by the transform")
    for section, key in (("inputs", "inputs"), ("outputs", "outputs")):
        items = cwl_items(cwl_el.get(key))
        for name, spec in items.items():
            fmt = spec.get("format")
            if not fmt or name not in pd.get(section, {}):
                continue
            fmts = fmt if isinstance(fmt, list) else [fmt]
            media = [FORMAT_MEDIA.get(expand(f, ns)) for f in fmts]
            if None in media:
                notes.append(f"{section}.{name}: unknown CWL format {fmts}, left unchanged")
                continue
            schema = pd[section][name]["schema"]
            target = schema["items"] if schema.get("type") == "array" and "items" in schema else schema
            if target.get("contentMediaType") != "application/octet-stream":
                continue
            new = [{"type": "string", "contentEncoding": "binary", "contentMediaType": m} for m in media]
            target.clear()
            if len(new) == 1:
                target.update(new[0])
                notes.append(f"M-01 {section}.{name}: contentMediaType from CWL format `{fmts[0]}` -> `{media[0]}`; contentEncoding binary")
            else:
                target["oneOf"] = new
                notes.append(f"M-01/M-02 {section}.{name}: CWL format list {fmts} -> oneOf {media}")
    for name in secrets or []:
        if name in pd.get("inputs", {}):
            pd["inputs"][name]["schema"]["writeOnly"] = True
            notes.append(f"M-04 inputs.{name}: declared in cwltool:Secrets -> writeOnly: true")
    return pd, notes


# ------------------------------------------------------------------ builders

def bb_id(proc):
    return f"{PREFIX}{proc['workflow']}.{proc['key']}"


def ptype_iri(proc):
    return f"{PTYPE_SCHEME}/{proc['workflow']}/{proc['key']}"


def pd_url(pd):
    return f"https://ospd.example.org/ogc-api/processes/{pd['id']}"


def media(v, d):
    return d["media"].get(v, v)


def execute_doc(proc, d):
    inputs = {}
    for k, v in proc["execute"]["inputs"].items():
        if isinstance(v, dict) and "href" in v:
            href = v["href"]
            if not re.match(r"^[a-z0-9]+://", href):
                # output of the upstream step (illustrative job URL)
                href = f"{d['job_base']}/upstream-step/results/{href}"
            v = {"href": href, "type": media(v["type"], d)}
        inputs[k] = v
    return {"inputs": inputs, "response": "document"}


def results_doc(proc, d, job_id, info):
    base = f"{d['job_base']}/{job_id}/results"
    hints = proc.get("results", {})
    out = {}
    for name, art in info["activity"]["outputs"].items():
        if not art and name in hints:  # not recoverable from the record: keep the declared value
            out[name] = hints[name]
            continue
        ref = _ref(art, base, hints.get(name, {}), d)
        out[name] = ref[0] if proc.get("results_single") and isinstance(ref, list) else ref
    return out


def run_info(proc, bags):
    """Engine, times, container image and the run-record activity a profile's examples come from.
    Every profile points into a run record; there are no illustrative examples."""
    run = proc.get("run", {})
    if not run.get("prov"):
        sys.exit(f"{proc['key']}: run.prov is required (a run record in scripts/sources.yaml `runs:`)")
    bag = bags[run["prov"]]
    act = bag_activity(bag, run.get("step"), run.get("iteration"))
    eng = {"id": f"urn:example:engine:cwltool-{bag['engine']['version']}",
           "name": bag["engine"]["name"], "version": bag["engine"]["version"]}
    return {"engine": eng, "start": act["start"], "end": act["end"], "image": act["image"],
            "prov": bag, "activity": act}


def docker_image(cwl_el, cwl_doc):
    for sect in ("requirements", "hints"):
        for src in (cwl_el, cwl_doc):
            r = src.get(sect) or {}
            if isinstance(r, list):
                r = {x.get("class"): x for x in r}
            if "DockerRequirement" in r:
                return r["DockerRequirement"].get("dockerPull")
    return None


def provenance_chain(proc, pd, exe, res, info, image, d):
    """Provenance view as an instance of ogc.bbr.provenance.provenance (W3C PROV chain)."""
    key = proc["key"]
    run_id = f"urn:example:run:{proc['workflow']}:{key}"
    eng = info["engine"]
    secrets = set(proc.get("secrets", []))
    ents, used, file_inputs = [], [], []
    for name, v in exe["inputs"].items():
        eid = f"urn:example:entity:{key}:in:{name}"
        e = {"id": eid, "provType": "prov:Entity", "entityType": f"{pd_url(pd)}#inputs/{name}"}
        if isinstance(v, dict) and "href" in v:
            e["links"] = [{"href": v["href"], "rel": "item", "type": v["type"]}]
            file_inputs.append(eid)
        elif name not in secrets:
            e["value"] = v
        ents.append(e)
        used.append(eid)
    for name, v in res.items():
        eid = f"urn:example:entity:{key}:out:{name}"
        e = {"id": eid, "provType": "prov:Entity", "entityType": f"{pd_url(pd)}#outputs/{name}",
             "wasGeneratedBy": run_id}
        if file_inputs:
            e["wasDerivedFrom"] = file_inputs
        vals = v if isinstance(v, list) else [v]
        if all(isinstance(x, dict) and "href" in x for x in vals):
            e["links"] = [{"href": x["href"], "rel": "item", "type": x["type"]} for x in vals]
        else:
            e["value"] = v
        e["wasAttributedTo"] = eng["id"]
        ents.append(e)
    activity = {
        "id": run_id,
        "provType": "prov:Activity",
        "activityType": ptype_iri(proc),
        "startedAtTime": info["start"],
        "used": used,
        "wasAssociatedWith": [eng["id"]] + ([f"urn:example:image:{image}"] if image else []),
        "qualifiedAssociation": [{"agent": eng["id"], "hadPlan": pd_url(pd)}],
    }
    if info["end"]:
        activity["endedAtTime"] = info["end"]
    agents = [{"id": eng["id"], "provType": "prov:SoftwareAgent", "name": f"{eng['name']} {eng['version']}"}]
    if image:
        agents.append({"id": f"urn:example:image:{image}", "provType": "prov:SoftwareAgent",
                       "name": f"container image {image}"})
    return [activity] + ents + agents, run_id


def process_run(proc, pd, run_id, info, parent_run):
    """CommandLineTool run as ogc.bbr.wf4ever.wfprov.ProcessRun (generic profile gap GP-1)."""
    doc = {
        "id": run_id,
        "type": "ProcessRun",
        "activityType": ptype_iri(proc),
        "describedByProcess": pd_url(pd),
        "usedInput": [{"id": f"urn:example:entity:{proc['key']}:in:{n}"} for n in proc["execute"]["inputs"]],
        "startedAtTime": info["start"],
        "wasEnactedBy": info["engine"]["id"],
    }
    if parent_run:
        doc["wasPartOfWorkflowRun"] = parent_run
    return doc


def execution_bundle(proc, pd, run_id, info, job_id, d):
    """Workflow run as ogc.bbr.provenance.execution: every file of the run record, directories
    included (CWLProv content-addresses each file, so a Directory output gets one artifact per
    member with its own checksum, GP-10). None when a file has no checksum."""
    eng = info["engine"]
    base = f"{d['job_base']}/{job_id}/results"
    outputs = []
    for name, art in info["activity"]["outputs"].items():
        for f in _files_in(art):
            if not f["sha1"]:
                return None
            outputs.append({"id": f"{base}/{f['path']}", "type": "Artifact", "role": "output",
                            "mediaType": media(MEDIA_BY_EXT.get(Path(f["path"]).suffix, "application/octet-stream"), d),
                            "describedByParameter": f"{pd_url(pd)}#outputs/{name}",
                            "wasOutputFrom": run_id, "checksum": {"algorithm": "SHA-1", "value": f["sha1"]}})
    if not outputs:
        return None
    run = {"id": run_id, "type": "WorkflowRun", "activityType": ptype_iri(proc),
           "describedByWorkflow": pd_url(pd), "wasEnactedBy": eng["id"], "status": "successful",
           "jobID": job_id, "startedAtTime": info["start"], "endedAtTime": info["end"]}
    if proc.get("steps"):
        run["hadSubProcessRun"] = [{"id": f"urn:example:run:{proc['workflow']}:{s}"} for s in proc["steps"]]
    engine = {"@id": eng["id"], "@type": "WorkflowEngine", "name": eng["name"], "version": eng["version"]}
    return {"run": run, "engine": engine, "outputs": outputs}


def process_type_entry(proc, pd, cwl_el, src, url, by_key):
    oe = proc["openeo"]
    entry = {
        "id": ptype_iri(proc),
        "type": "ProcessType",
        "prefLabel": (proc.get("label") or pd.get("title") or pd["id"]).strip(),
        "definition": " ".join((proc.get("definition") or cwl_el.get("doc") or cwl_el.get("label")
                                or pd.get("description") or "").split()),
        "inScheme": PTYPE_SCHEME,
        "status": "submitted",
        "phase": [PHASE_BASE + p for p in proc["phases"]],
        "profile": bb_id(proc),
        "processDescription": {"id": pd["id"], "version": pd["version"]},
        "source": {"cwl": url, "cwlClass": cwl_el["class"], "cwlId": cwl_el.get("id", pd["id"]),
                   "license": src["license"]},
        "provenanceClass": "http://purl.org/wf4ever/wfprov#" + ("WorkflowRun" if cwl_el["class"] == "Workflow" else "ProcessRun"),
        "cctDependencies": proc.get("cct", []),
        "candidateCctDependencies": proc.get("cct_candidates", []),
    }
    if proc.get("steps"):
        entry["hasStep"] = [ptype_iri(by_key[s]) for s in proc["steps"]]
    for rel in ("exactMatch", "closeMatch", "relatedMatch"):
        if oe.get(rel):
            entry[rel] = [BBLOCK_IRI + t for t in oe[rel]]
    eq = {"level": oe["level"], "rationale": " ".join(oe["rationale"].split())}
    if oe.get("decomposition"):
        eq["decomposition"] = oe["decomposition"]
    entry["openeoEquivalence"] = eq
    return entry


def profile_schema(proc, pd, cwl_el, has_exec):
    req_in = [n for n, v in cwl_items(cwl_el.get("inputs")).items()
              if not is_optional(v.get("type")) and "default" not in v and n in pd["inputs"]]
    workflow = cwl_el["class"] == "Workflow"
    defs = {
        "rawProcessDescription": {"$ref": "bblocks://ogc.api.processes.v1.schemas.process"},
        "applicationPackage": {"$ref": "bblocks://ogc.api.processes.v2.schemas.ogcapppkg"},
        "provenance": {"$ref": "bblocks://ogc.bbr.provenance.provenance"},
        "processTypeEntry": {"$ref": f"bblocks://{PREFIX}process-type"},
        "w3cProvJsonLd": {"$ref": "bblocks://ogc.ogc-utils.prov.w3c-prov-jsonld"},
        "execute": {
            "description": ("Execute request for this process. Built on the processDescription input "
                            "schemas and on ogc.api.processes.v1.schemas.link / qualifiedInputValue, "
                            "because ogc.api.processes.v1.schemas.execute rejects plain strings and "
                            "numbers (upstream issue U-01)."),
            "type": "object",
            "required": ["inputs"],
            "properties": {
                "inputs": {
                    "type": "object",
                    "required": req_in,
                    "propertyNames": {"enum": list(pd["inputs"].keys())},
                    "additionalProperties": {"anyOf": [
                        {"$ref": "bblocks://ogc.api.processes.v1.schemas.link"},
                        {"$ref": "bblocks://ogc.api.processes.v1.schemas.qualifiedInputValue"},
                        {"type": ["string", "number", "integer", "boolean", "array", "object"]},
                    ]},
                },
                "outputs": {"type": "object", "propertyNames": {"enum": list(pd["outputs"].keys())}},
                "response": {"enum": ["raw", "document"]},
            },
        },
        "results": {
            "description": "Results document (response=document) for this process (see U-01).",
            "type": "object",
            "propertyNames": {"enum": list(pd["outputs"].keys())},
            "additionalProperties": {"anyOf": [
                {"$ref": "bblocks://ogc.api.processes.v1.schemas.link"},
                {"type": "array", "items": {"$ref": "bblocks://ogc.api.processes.v1.schemas.link"}},
                {"type": ["string", "number", "integer", "boolean", "array", "object"]},
            ]},
        },
    }
    if workflow and has_exec:
        defs["execution"] = {"$ref": "bblocks://ogc.bbr.provenance.execution"}
    else:
        defs["processRun"] = {"$ref": "bblocks://ogc.bbr.wf4ever.wfprov.ProcessRun"}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "description": (f"Profile of the OGC API - Processes processDescription of `{pd['id']}` "
                        f"(CWL {cwl_el['class']}). Pins the process id and the input/output names; "
                        "the input/output schemas are those derived from the CWL."),
        "allOf": [
            {"$ref": "bblocks://ogc.api.processes.v1.schemas.process"},
            {"$ref": "bblocks://ogc.api.processes.v2.schemas.staticIndicator"},
            {
                "type": "object",
                "required": ["id", "version", "inputs", "outputs"],
                "properties": {
                    "id": {"const": pd["id"]},
                    "inputs": {"type": "object", "required": list(pd["inputs"].keys()),
                               "propertyNames": {"enum": list(pd["inputs"].keys())}},
                    "outputs": {"type": "object", "required": list(pd["outputs"].keys()),
                                "propertyNames": {"enum": list(pd["outputs"].keys())}},
                },
            },
        ],
        "$defs": defs,
    }


# ------------------------------------------------------------------ documentation

def md_openeo(oe):
    lines = [f"**Level: {oe['level']}.** " + " ".join(oe["rationale"].split()), ""]
    for rel in ("exactMatch", "closeMatch", "relatedMatch"):
        if oe.get(rel):
            lines.append(f"- `{rel}`: " + ", ".join(f"`{t}`" for t in oe[rel]))
    if oe.get("decomposition"):
        lines += ["", "| Stage | openEO | Level | Note |", "|---|---|---|---|"]
        for s in oe["decomposition"]:
            lines.append(f"| {s['stage']} | {', '.join('`'+x+'`' for x in s.get('openeo', [])) or '—'} | "
                         f"{s['level']} | {s.get('note', '')} |")
    return "\n".join(lines)


def description_md(proc, pd, cwl_el, url, src, corrections, has_exec, info, by_key, eoap_commit):
    wf = {"algae-bloom": "W1 Algae Bloom", "kindgrove": "W2 KindGrove"}[proc["workflow"]]
    ins = cwl_items(cwl_el.get("inputs"))
    outs = cwl_items(cwl_el.get("outputs"))
    parts = [
        f"Process profile of **`{pd['id']}`** ({cwl_el['class']}, {wf}).",
        "",
        f"> {(proc.get('label') or cwl_el.get('label') or pd.get('title') or '').strip()}",
        "",
        "## Source",
        "",
        f"- CWL: [{proc['source']['file']}{('#' + proc['source']['element']) if proc['source'].get('element') else ''}]({url}) "
        f"(pinned commit `{src['commit'][:7]}`, license <{src['license']}>). Referenced, not copied.",
        f"- Six-phase position: " + " → ".join(PHASE_LABELS[p] for p in proc["phases"]),
        f"- EOAP CWL custom types used: {', '.join('`'+c+'`' for c in proc.get('cct', [])) or 'none'}"
        + (f"; candidates: {', '.join('`'+c+'`' for c in proc['cct_candidates'])}" if proc.get("cct_candidates") else ""),
    ]
    if proc.get("steps"):
        parts.append("- Steps (profiles): " + ", ".join(f"`{bb_id(by_key[s])}`" for s in proc["steps"]))
    if proc.get("parents"):
        parts.append("- Used by: " + ", ".join(f"`{bb_id(by_key[s])}`" for s in proc["parents"]))
    parts += ["", "| Input | CWL type | Output | CWL type |", "|---|---|---|---|"]
    il, ol = list(ins.items()), list(outs.items())
    for i in range(max(len(il), len(ol))):
        a = il[i] if i < len(il) else ("", {"type": ""})
        b = ol[i] if i < len(ol) else ("", {"type": ""})
        def show(t):
            return t if isinstance(t, str) else json.dumps(t)
        fa = show(a[1].get("type")) if a[0] else ""
        fb = show(b[1].get("type")) if b[0] else ""
        parts.append(f"| {('`'+a[0]+'`') if a[0] else ''} | {fa.replace('|', '/')} | {('`'+b[0]+'`') if b[0] else ''} | {fb.replace('|', '/')} |")
    if proc.get("analysis"):
        parts += ["", "## Analysis", "", proc["analysis"].strip()]
    parts += ["", "## processDescription derivation", "",
              "Derived with the `eoap.cct.cwl-to-ogcprocess` jq transform (bblocks-eoap-cct "
              f"`{eoap_commit[:7]}`, inline variant)."]
    if corrections:
        parts += ["", "**Manually corrected** (the raw transform output is kept as a separate example):", ""]
        parts += [f"- {c}" for c in corrections]
    else:
        parts += ["", "No manual correction: the example is the unmodified transform output."]
    parts += ["", "## Provenance view", "",
              "Expressed against the generic provenance profile (`ogc.bbr.provenance.provenance`, a W3C PROV "
              "chain): one `prov:Activity` whose `activityType` is the process-type IRI, `qualifiedAssociation."
              "hadPlan` pointing to the processDescription, input and output `prov:Entity` objects (literal "
              "parameters carry `value`, files carry `links`) and the engine / container image as "
              "`prov:SoftwareAgent`."]
    if cwl_el["class"] == "Workflow":
        parts.append("" if has_exec else "")
        parts.append("The workflow run is also given as an `ogc.bbr.provenance.execution` bundle."
                     if has_exec else
                     "No `ogc.bbr.provenance.execution` bundle is given: its artifacts require a checksum, which "
                     "a STAC Directory output does not have (GP-10).")
    else:
        parts.append("The run is also given as a `wfprov:ProcessRun` (`ogc.bbr.wf4ever.wfprov.ProcessRun`), because the "
                     "generic profile has no step-level run (GP-1).")
    parts += ["", "Gaps met here are listed in `docs/PROVENANCE-GAPS.md`."]
    if info.get("prov"):
        run = proc["run"]
        where = f"scatter iteration {run['iteration']}, " if run.get("iteration") else ""
        parts += ["", f"Execution and provenance examples are built from a real `cwltool --provenance` run "
                  f"(CWLProv research object `{run['prov']}`: {info['prov']['note']}), activity "
                  f"`{info['activity']['plan']}` ({where}engine {info['engine']['name']} {info['engine']['version']}). "
                  "Timestamps are UTC: cwltool records naive local times, the offset is taken from its engine log. "
                  "Hosts under `ospd.example.org` are illustrative: job and result URLs are not those of a deployment."]
    parts += ["", "## openEO equivalence", "", md_openeo(proc["openeo"]), "",
              "## Process type (Activity 4)", "",
              f"Candidate entry `{ptype_iri(proc)}` (`ospd.process-profiles.process-type`), status `submitted`."]
    return "\n".join(parts) + "\n"


def bblock_json(proc, pd, cwl_el, corrections, has_exec, by_key):
    oe = proc["openeo"]
    targets = oe.get("exactMatch", []) + oe.get("closeMatch", []) + oe.get("relatedMatch", [])
    for s in oe.get("decomposition", []) or []:
        targets += s.get("openeo", [])
    # The workflow/step relation is not a schema dependency (a workflow's processDescription does
    # not embed those of its steps), so it cannot go in dependsOn; seeAlso is what the register
    # and the viewer render as navigable links, in both directions.
    related = [bb_id(by_key[s]) for s in proc.get("steps", [])] + [bb_id(by_key[s]) for s in proc.get("parents", [])]
    see = related + [t for t in dict.fromkeys(targets) if t not in related]
    depends = ["ogc.api.processes.v1.schemas.process", "ogc.api.processes.v2.schemas.staticIndicator",
               "ogc.api.processes.v2.schemas.ogcapppkg", "ogc.bbr.provenance.provenance",
               f"{PREFIX}process-type", "eoap.cct.cwl-to-ogcprocess",
               "ogc.ogc-utils.prov.w3c-prov-jsonld"]
    if cwl_el["class"] == "Workflow":
        depends += ["ogc.bbr.provenance.execution"] if has_exec else []
    else:
        depends += ["ogc.bbr.wf4ever.wfprov.ProcessRun"]
    depends += proc.get("cct", [])
    tags = ["OSPD", "process profile", "CWL", cwl_el["class"], proc["workflow"]]
    if corrections:
        tags.append("manually-corrected")
    return {
        "$schema": "https://raw.githubusercontent.com/opengeospatial/bblocks-postprocess/master/ogc/bblocks/metadata-schema.yaml",
        "name": f"Process profile: {pd['id']}",
        "abstract": (f"OGC API - Processes profile of the CWL {cwl_el['class']} `{pd['id']}` "
                     f"({'W1 Algae Bloom' if proc['workflow'] == 'algae-bloom' else 'W2 KindGrove'}), with its "
                     "provenance view, process-type entry and openEO equivalence."),
        "status": "under-development",
        "dateTimeAddition": f"{TODAY}T00:00:00Z",
        "dateOfLastChange": TODAY,
        "version": "0.1",
        "itemClass": "schema",
        "register": "process-profiles",
        "dependsOn": depends,
        "seeAlso": see + ["ogc.api.processes.part1.requirements.core"],
        "conformanceClasses": [PART1_CORE],
        "scope": "dev",
        "tags": tags,
        "sourceSchema": "schema.yaml",
        "maturity": "development",
        "group": "W1 Algae Bloom" if proc["workflow"] == "algae-bloom" else "W2 KindGrove",
    }


def examples_yaml(proc, cwl_el, url, corrected, has_exec):
    ex = [
        {"title": "Source CWL (referenced)",
         "content": f"The CWL {cwl_el['class']} is referenced, not copied: <{url}>."},
        {"title": "processDescription",
         "content": "OGC API - Processes processDescription derived from the CWL"
                    + (" (manually corrected, see description)." if corrected else "."),
         "snippets": [{"language": "json", "ref": "examples/processDescription.json"}]},
    ]
    if corrected:
        ex.append({"title": "Raw cwl-to-ogcprocess output",
                   "content": "Unmodified output of the `eoap.cct.cwl-to-ogcprocess` jq transform.",
                   "snippets": [{"language": "json", "ref": "examples/processDescription.raw.json",
                                 "schema-ref": "#/$defs/rawProcessDescription"}]})
    ex += [
        {"title": "OGC Application Package (deploy)",
         "content": "Part 2 deploy body: the execution unit is a link to the pinned CWL.",
         "snippets": [{"language": "json", "ref": "examples/ogcapppkg.json", "schema-ref": "#/$defs/applicationPackage"}]},
        {"title": "Execute request",
         "snippets": [{"language": "json", "ref": "examples/execute.json", "schema-ref": "#/$defs/execute"}]},
        {"title": "Results",
         "snippets": [{"language": "json", "ref": "examples/results.json", "schema-ref": "#/$defs/results"}]},
        {"title": "Provenance view (generic provenance profile)",
         "content": "W3C PROV chain validated against `ogc.bbr.provenance.provenance`.",
         "snippets": [{"language": "json", "ref": "examples/provenance.json", "schema-ref": "#/$defs/provenance"}]},
    ]
    if cwl_el["class"] == "Workflow":
        if has_exec:
            ex.append({"title": "Execution bundle (generic provenance profile)",
                       "snippets": [{"language": "json", "ref": "examples/execution.json", "schema-ref": "#/$defs/execution"}]})
    else:
        ex.append({"title": "Process run (wfprov:ProcessRun, gap GP-1)",
                   "snippets": [{"language": "json", "ref": "examples/process-run.json", "schema-ref": "#/$defs/processRun"}]})
    ex.append({"title": "Process-type register entry (Activity 4)",
               "snippets": [{"language": "json", "ref": "examples/process-type.json", "schema-ref": "#/$defs/processTypeEntry"}]})
    ex.append({"title": "Run record, W3C PROV-JSONLD (cwltool CWLProv bundle)",
               "content": "The CWLProv bundle of the run record that holds this profile's activity, re-serialised "
                          "as PROV-JSONLD by the `prov` library (mentions of nested bundles rewritten as "
                          "`specializationOf` + `prov:asInBundle`, see that block's notes), validated against "
                          "`ogc.ogc-utils.prov.w3c-prov-jsonld` and read as RDF through its own context: the PROV-O "
                          "graph here is the engine's, not this register's provenance view.",
               "snippets": [{"language": "jsonld", "ref": "examples/cwlprov.jsonld", "schema-ref": "#/$defs/w3cProvJsonLd"}]})
    # Every snippet below is a document about this process, and several carry relative ids
    # (the nested processDescription id of ogcapppkg.json and process-type.json, the id of the
    # processDescription itself). Without a base URI they uplift to file:// IRIs rooted at the
    # uplift working directory; with one they land in the register's process namespace.
    return [e if not e.get("snippets")
            else {"title": e["title"], "base-uri": PROCESS_BASE,
                  **{k: v for k, v in e.items() if k != "title"}}
            for e in ex]


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources-root", type=Path, default=ROOT.parent)
    ap.add_argument("--w1", type=Path)
    ap.add_argument("--w2", type=Path)
    ap.add_argument("--eoap-cct", type=Path)
    ap.add_argument("--runs-root", type=Path,
                    help="directory holding the CWLProv research objects named in scripts/sources.yaml `runs:` "
                         "(default: --sources-root)")
    a = ap.parse_args()

    sources = yaml.safe_load((SCRIPTS / "sources.yaml").read_text())
    cfg = yaml.safe_load((SCRIPTS / "profiles.yaml").read_text())
    d, procs = cfg["defaults"], cfg["processes"]
    by_key = {p["key"]: p for p in procs}
    roots = {"w1": a.w1 or a.sources_root / sources["w1"]["clone"],
             "w2": a.w2 or a.sources_root / sources["w2"]["clone"]}
    eoap = a.eoap_cct or a.sources_root / sources["eoap_cct"]["clone"]
    jq_path = eoap / sources["eoap_cct"]["transform"]
    # real run records: local research objects, never downloaded (like the CWL clones)
    runs_root = a.runs_root or a.sources_root
    bags = {}
    for name, r in sources.get("runs", {}).items():
        p = Path(r["bag"])
        p = p if p.is_absolute() else runs_root / p
        if not (p / "metadata" / "provenance").is_dir():
            sys.exit(f"run {name}: research object not found at {p} (see scripts/sources.yaml `runs:`, --runs-root)")
        bags[name] = load_bag(p)
        bags[name]["note"] = r.get("note", "")

    openeo_reg = a.sources_root / "bblocks-openeo" / "build" / "register.json"
    known = None
    if openeo_reg.exists():
        known = {b["itemIdentifier"] for b in json.loads(openeo_reg.read_text())["bblocks"]}

    summary = []
    for proc in procs:
        src = sources[proc["source"]["repo"]]
        cwl_doc, cwl_el, url = load_process(proc, sources, roots)
        ns = cwl_doc.get("$namespaces", {})
        raw = run_transform(cwl_doc, jq_path)
        pd, corrections = correct(raw, cwl_el, ns, proc.get("secrets"), proc.get("stac_catalog"))
        corrected = bool(corrections)

        if known:
            oe = proc["openeo"]
            ids = oe.get("exactMatch", []) + oe.get("closeMatch", []) + oe.get("relatedMatch", [])
            ids += [x for s in oe.get("decomposition", []) or [] for x in s.get("openeo", [])]
            missing = [i for i in ids if i not in known]
            if missing:
                sys.exit(f"{proc['key']}: unknown openEO identifiers {missing}")

        out = ROOT / "_sources" / proc["workflow"] / proc["key"]
        exd = out / "examples"
        for f in exd.glob("*.json"):
            f.unlink()
        job_id = f"{proc['workflow']}-{proc['key']}-0001"
        info = run_info(proc, bags)
        image = info["image"] or docker_image(cwl_el, cwl_doc)
        exe = execute_doc(proc, d)
        res = results_doc(proc, d, job_id, info)
        chain, run_id = provenance_chain(proc, pd, exe, res, info, image, d)

        dump_json(exd / "processDescription.json", pd)
        if corrected:
            dump_json(exd / "processDescription.raw.json", raw)
        exec_unit_type = "application/cwl+yaml"
        dump_json(exd / "ogcapppkg.json", {
            "processDescription": {"process": {"id": pd["id"], "version": pd["version"]}},
            "executionUnit": {"href": url.replace("/blob/", "/raw/", 1), "type": exec_unit_type, "rel": "http://www.opengis.net/def/rel/ogc/1.0/executionUnit"},
        })
        dump_json(exd / "execute.json", exe)
        dump_json(exd / "results.json", res)
        dump_json(exd / "provenance.json", chain)
        has_exec = False
        if cwl_el["class"] == "Workflow":
            bundle = execution_bundle(proc, pd, run_id, info, job_id, d)
            if bundle:
                dump_json(exd / "execution.json", bundle)
                has_exec = True
        else:
            parents = proc.get("parents") or []
            parent_run = f"urn:example:run:{proc['workflow']}:{parents[0]}" if parents else None
            dump_json(exd / "process-run.json", process_run(proc, pd, run_id, info, parent_run))
        entry = process_type_entry(proc, pd, cwl_el, src, url, by_key)
        dump_json(exd / "process-type.json", entry)
        w3c_prov_example(info, exd)

        dump_json(out / "context.jsonld", PROFILE_CONTEXT)
        dump_yaml(out / "schema.yaml", profile_schema(proc, pd, cwl_el, has_exec))
        dump_yaml(out / "examples.yaml", examples_yaml(proc, cwl_el, url, corrected, has_exec))
        dump_json(out / "bblock.json", bblock_json(proc, pd, cwl_el, corrections, has_exec, by_key))
        (out / "description.md").write_text(description_md(proc, pd, cwl_el, url, src, corrections, has_exec, info, by_key, sources["eoap_cct"]["commit"]))

        summary.append({"id": bb_id(proc), "key": proc["key"], "class": cwl_el["class"], "pd_id": pd["id"],
                        "phases": proc["phases"], "openeo": proc["openeo"], "corrections": corrections,
                        "execution": has_exec, "cct": proc.get("cct", []),
                        "inputs": len(pd["inputs"]), "outputs": len(pd["outputs"])})
        print(f"{bb_id(proc):60s} {cwl_el['class']:16s} corrections={len(corrections)} exec={has_exec}")

    # shared process-type example: reproject-image entry
    pt = ROOT / "_sources" / "process-type"
    dump_json(pt / "examples" / "reproject-image.json",
              json.loads((ROOT / "_sources/algae-bloom/reproject-image/examples/process-type.json").read_text()))
    dump_json(pt / "examples" / "kindgrove-mangrove.json",
              json.loads((ROOT / "_sources/kindgrove/mangrove/examples/process-type.json").read_text()))
    dump_yaml(pt / "examples.yaml", [
        {"title": "reproject-image (closeMatch)", "base-uri": PROCESS_BASE,
         "snippets": [{"language": "json", "ref": "examples/reproject-image.json"}]},
        {"title": "KindGrove mangrove (none, with decomposition)", "base-uri": PROCESS_BASE,
         "snippets": [{"language": "json", "ref": "examples/kindgrove-mangrove.json"}]},
    ])

    # README table
    rows = []
    for s in summary:
        oe = s["openeo"]
        tgt = ", ".join(t.split("ogc.openeo.")[-1] for t in oe.get("exactMatch", []) + oe.get("closeMatch", []))
        rows.append(f"| `{s['id']}` | {s['class']} | {', '.join(PHASE_LABELS[p] for p in s['phases'])} | {oe['level']}{(': ' + tgt) if tgt else ''} |")
    readme = (ROOT / "README.md").read_text()
    readme = re.sub(r"(\|---\|---\|---\|---\|\n)(?:\|.*\|\n)*(?:PROFILE_TABLE\n)?",
                    lambda m: m.group(1) + "\n".join(rows) + "\n", readme, count=1)
    (ROOT / "README.md").write_text(readme)
    dump_json(SCRIPTS / "generated-summary.json", summary)
    write_openeo_doc(summary)


OPENEO_HEADER = """# openEO equivalence decisions

Proposed correspondences between the process profiles and the openEO Building Blocks of
[GeoLabs/bblocks-openeo](https://github.com/GeoLabs/bblocks-openeo) (`ogc.openeo.*`, stable
processes of openeo-processes 2.0.0-rc.2). Offered for review, not settled equivalences.
Generated from `scripts/profiles.yaml` by `scripts/generate.py`.

## Criteria

| Level | Used when |
|---|---|
| **exactMatch** | same operation, same parameter semantics, same output type. None found. |
| **closeMatch** | same operation, but a different I/O model (files or URLs vs openEO data cubes), or a parameter subset/superset. |
| **none** | no single openEO process: the step is a composition (process graph), an opaque tool, or a structural helper. |

`relatedMatch` (SKOS) is used for type-level links (e.g. a bounding-box input vs
`ogc.openeo.types.bounding-box`) and for math processes used inside a callback; it never expresses
process equivalence. Composite and opaque processes carry a stage-by-stage `decomposition` in their
process-type entry. openEO `proposals/` (e.g. `load_stac`) are out of scope because
bblocks-openeo only models stable processes.

## Decisions (to be confirmed by Gérald before commit)

| # | Profile | Level | exactMatch / closeMatch | relatedMatch | Rationale (short) |
|---|---|---|---|---|---|
"""


def write_openeo_doc(summary):
    rows = []
    for i, s in enumerate(summary, 1):
        oe = s["openeo"]
        main = ", ".join("`" + t.replace("ogc.openeo.", "") + "`" for t in oe.get("exactMatch", []) + oe.get("closeMatch", [])) or "—"
        rel = ", ".join("`" + t.replace("ogc.openeo.", "") + "`" for t in oe.get("relatedMatch", [])) or "—"
        short = " ".join(oe["rationale"].split())
        short = short.split(". ")[0] + "."
        rows.append(f"| E{i:02d} | `{s['id'].replace('ospd.process-profiles.', '')}` | {oe['level']} | {main} | {rel} | {short} |")
    (ROOT / "docs" / "OPENEO-EQUIVALENCES.md").write_text(
        OPENEO_HEADER + "\n".join(rows) + "\n\nFull rationale and decompositions: each profile's `description.md` and "
        "`examples/process-type.json`.\n")


if __name__ == "__main__":
    main()
