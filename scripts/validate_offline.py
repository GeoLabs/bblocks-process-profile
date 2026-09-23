#!/usr/bin/env python3
"""Offline JSON Schema pre-check of the register.

This is NOT a substitute for the Docker build (`./build.sh`, bblocks-postprocess), which remains the
authoritative validation. It exists because the build could not be run in the environment where the
register was bootstrapped (no Docker daemon, *.github.io and ghcr.io unreachable).

What it checks:
  - bblocks-config.yaml, every bblock.json and examples.yaml against the bblocks-postprocess
    metadata schemas;
  - every example snippet against its schema (default schema.yaml, or `schema-ref`), resolving
    `bblocks://` identifiers and published register URLs to LOCAL clones (see DEPS below);
  - negative checks: a processDescription must be rejected by the profile of another process.

It does NOT run: JSON-LD uplift, SHACL, transforms, format assertions, docs generation.

Usage: python3 scripts/validate_offline.py --deps-root DIR
DIR contains the clones named in DEPS (symlinks are fine).
"""
import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urldefrag

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parent.parent

# published URL prefix -> local clone path (relative to --deps-root)
URL_MAPS = {
    "https://ogcincubator.github.io/bblock-prov-schema/build/": "bblock-prov-schema/build/",
    "https://opengeospatial.github.io/bblocks/annotated-schemas/": "bblocks/annotated-schemas/",
    "https://geolabs.github.io/bblocks-ogcapi-processes/build/": "bblocks-ogcapi-processes/build/",
    "https://ogcincubator.github.io/bblocks-wf4ever/build/": "bblocks-wf4ever/build/",
    "https://geolabs.github.io/bblocks-eoap-cct/build/": "bblocks-eoap-cct/build/",
    "https://ogcincubator.github.io/bblocks-cwl/build/": "bblocks-cwl/build/",
    "https://geolabs.github.io/bblocks-openeo/build/": "bblocks-openeo/build/",
}
# registers available as built register.json (identifier -> published schema URL)
BUILT_REGISTERS = [
    "bblock-prov-schema/build/register.json",
    "bblocks/register.json",
    "bblocks-ogcapi-processes/build/register.json",
    "bblocks-wf4ever/build/register.json",
    "bblocks-eoap-cct/build/register.json",
    "bblocks-cwl/build/register.json",
    "bblocks-openeo/build/register.json",
]
# registers only available as sources (no published build found): (identifier prefix, _sources dir)
SOURCE_REGISTERS = [
    ("ogc.bbr.provenance.", "bblocks-generic-provenance-profile/_sources"),
    ("ogc.api.processes.", "bblock-ogcapi-processes-part2/_sources"),
]


def load(path: Path):
    text = path.read_text()
    return json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)


class Resolver:
    def __init__(self, deps: Path):
        self.deps = deps
        self.ids = {}       # identifier -> file path
        self.missing = set()
        for reg in BUILT_REGISTERS:
            p = deps / reg
            if not p.exists():
                continue
            for bb in json.loads(p.read_text()).get("bblocks", []):
                url = (bb.get("schema") or {}).get("application/yaml")
                local = self.map_url(url) if url else None
                if local and local.exists():
                    self.ids.setdefault(bb["itemIdentifier"], local)
        for prefix, src in SOURCE_REGISTERS + [("ospd.process-profiles.", None)]:
            base = (ROOT / "_sources") if src is None else deps / src
            for sch in base.rglob("schema.yaml"):
                ident = prefix + ".".join(sch.parent.relative_to(base).parts)
                self.ids[ident] = sch  # sources win over builds (fresher)
        self.cache = {}

    def map_url(self, url):
        for pre, loc in URL_MAPS.items():
            if url.startswith(pre):
                return self.deps / loc / url[len(pre):]
        return None

    def rewrite(self, node):
        if isinstance(node, dict):
            out = {}
            for k, v in node.items():
                if k == "$ref" and isinstance(v, str):
                    out[k] = self.rewrite_ref(v)
                else:
                    out[k] = self.rewrite(v)
            return out
        if isinstance(node, list):
            return [self.rewrite(x) for x in node]
        return node

    def rewrite_ref(self, ref):
        if ref.startswith("bblocks://"):
            ident, frag = urldefrag(ref[len("bblocks://"):])
            path = self.ids.get(ident)
            if not path:
                self.missing.add(ident)
                return ref
            return path.resolve().as_uri() + (f"#{frag}" if frag else "")
        if ref.startswith("http"):
            url, frag = urldefrag(ref)
            local = self.map_url(url)
            if local and local.exists():
                return local.resolve().as_uri() + (f"#{frag}" if frag else "")
            if local is None:
                self.missing.add(url)
        return ref

    def retrieve(self, uri):
        if uri in self.cache:
            return self.cache[uri]
        if not uri.startswith("file://"):
            self.missing.add(uri)
            raise NoSuchResource(ref=uri)
        path = Path(uri[len("file://"):])
        if not path.exists():
            self.missing.add(uri)
            raise NoSuchResource(ref=uri)
        contents = self.rewrite(load(path))
        if isinstance(contents, dict) and "$schema" not in contents:
            contents["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        res = Resource.from_contents(contents, default_specification=DRAFT202012)
        self.cache[uri] = res
        return res

    def validator(self, schema_path: Path, fragment: str | None = None):
        uri = schema_path.resolve().as_uri() + (f"#{fragment}" if fragment else "")
        registry = Registry(retrieve=self.retrieve)
        return Draft202012Validator({"$ref": uri}, registry=registry)


def errors(validator, instance, limit=3):
    out = []
    try:
        for e in validator.iter_errors(instance):
            path = "/".join(str(p) for p in e.absolute_path)
            out.append(f"{path or '<root>'}: {e.message[:300]}")
            if len(out) >= limit:
                break
    except Exception as e:  # unresolvable reference etc.
        out.append(f"{type(e).__name__}: {e}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--deps-root", type=Path, required=True)
    a = ap.parse_args()
    res = Resolver(a.deps_root)
    bbp = a.deps_root / "bblocks-postprocess" / "ogc" / "bblocks" / "schemas"
    results = []

    def check(label, validator, instance):
        errs = errors(validator, instance)
        results.append((label, errs))

    meta = {n: Draft202012Validator(load(bbp / f"{n}.schema.yaml"))
            for n in ("bblock", "examples", "bblocks-config")} if bbp.exists() else {}
    if meta:
        check("bblocks-config.yaml", meta["bblocks-config"], load(ROOT / "bblocks-config.yaml"))

    bb_dirs = sorted(p.parent for p in (ROOT / "_sources").rglob("bblock.json"))
    pds = {}
    for bb in bb_dirs:
        rel = bb.relative_to(ROOT / "_sources")
        if meta:
            check(f"{rel}/bblock.json", meta["bblock"], load(bb / "bblock.json"))
            if (bb / "examples.yaml").exists():
                check(f"{rel}/examples.yaml", meta["examples"], load(bb / "examples.yaml"))
        for ex in load(bb / "examples.yaml") or []:
            for sn in ex.get("snippets", []):
                ref = sn.get("schema-ref")
                frag = ref[1:] if ref and ref.startswith("#") else None
                inst = load(bb / sn["ref"])
                check(f"{rel}/{sn['ref']}" + (f" [{ref}]" if ref else ""), res.validator(bb / "schema.yaml", frag), inst)
                if sn["ref"].endswith("processDescription.json"):
                    pds[bb] = inst

    # negative checks: each profile rejects another process's description
    keys = list(pds)
    for i, bb in enumerate(keys):
        other = keys[(i + 1) % len(keys)]
        errs = errors(res.validator(bb / "schema.yaml"), pds[other], limit=1)
        results.append((f"NEGATIVE {bb.relative_to(ROOT / '_sources')} rejects {other.name}",
                        [] if errs else ["accepted a foreign processDescription"]))

    ok = sum(1 for _, e in results if not e)
    for label, errs in results:
        print(("PASS " if not errs else "FAIL ") + label)
        for e in errs:
            print("     " + e)
    print(f"\n{ok}/{len(results)} checks passed")
    if res.missing:
        print("Unresolved references (not available locally):")
        for m in sorted(res.missing):
            print("  " + m)
    sys.exit(0 if ok == len(results) else 1)


if __name__ == "__main__":
    main()
