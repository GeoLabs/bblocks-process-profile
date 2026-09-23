#!/usr/bin/env python3
"""Run the reference workflows with `cwltool --provenance` and (optionally) regenerate the register.

The runs are described in scripts/sources.yaml under `runs:` (the same entries generate.py reads
the research objects from): which CWL of which pinned clone, which job, where the bag goes.
This script is the local counterpart of a CI job: it builds the W1 images when asked, runs the
workflows one after the other, and hands the resulting research objects to generate.py.

  python3 scripts/run_workflows.py --sources-root DIR --runs-root DIR [--only NAME ...]
                                   [--build-images] [--force] [--generate]

Safety rules, both learned the hard way:
  - cwltool deletes an existing `--provenance` directory before it starts. The bag is therefore
    written to a temporary directory and moved into place only when the run succeeded; a failed
    run is kept next to it as `<bag>-failed-<timestamp>` and the previous good bag is untouched.
  - An existing bag is never replaced without --force.

Copernicus credentials come from the environment variables named in the run's `secrets:`; when a
variable is not set and a terminal is attached, the value is asked for interactively (never echoed).
They go into a temporary copy of the job file, never into the clone. cwltool records them in the
research object as `(secret-<uuid>)` placeholders only (docs/DEVIATIONS.md M-04).

The pinned clones (scripts/sources.yaml `repo:` / `commit:` / `clone:`) are fetched under
--sources-root when missing and checked out at the pinned commit when they are clean; a clone with
local modifications is left alone and reported. generate.py itself never downloads anything: it
only reads what this script (or you) put there. --no-fetch skips this step.

Running the W1 package needs the deviations of docs/DEVIATIONS.md U-03..U-05; --build-images
applies U-03 (build `base` first, tag `reproject-image:latest`) and, on arm64 hosts, U-04.
"""
import argparse
import getpass
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "scripts" / "sources.yaml"

W1_IMAGES = ["select-products-sentinel2", "download-band-sentinel2-stac-item",
             "download-band-sentinel2-product-safe", "calculate-band", "reproject-image", "plot-image"]

ARM64_CALC_FIX = """\
# linux/arm64 only (docs/DEVIATIONS.md U-04): conda-forge gdal=3.6.2 aarch64 ships gdal_calc.py with
# a cross-compilation shebang that does not exist at runtime. Same tag, same CWL, one line rewritten.
FROM ogc-ospd/algae-usecase/calculate-band:1.1.0
USER root
RUN sed -i '1s|^#!.*$|#!/opt/conda/envs/algae-usecase/bin/python|' /opt/conda/envs/algae-usecase/bin/gdal_calc.py
USER mambauser
"""


def sh(cmd, cwd=None, log=None, env=None):
    print("  $", " ".join(str(c) for c in cmd), flush=True)
    if log:
        with open(log, "w") as f:
            return subprocess.run(cmd, cwd=cwd, stdout=f, stderr=subprocess.STDOUT, env=env).returncode
    return subprocess.run(cmd, cwd=cwd, env=env).returncode


def git(args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def ensure_clones(sources, sources_root: Path, repos):
    """The source clones the selected runs need, present under sources_root at their pinned commit."""
    sources_root.mkdir(parents=True, exist_ok=True)
    for key in sorted(repos):
        src = sources[key]
        d = sources_root / src["clone"]
        if not (d / ".git").exists():
            print(f"== cloning {src['repo']} -> {d}")
            if sh(["git", "clone", "--quiet", "--filter=blob:none", src["repo"], str(d)]):
                sys.exit(f"clone of {src['repo']} failed")
        head = git(["rev-parse", "HEAD"], d).stdout.strip()
        dirty = git(["status", "--porcelain"], d).stdout.strip()
        if head == src["commit"]:
            if dirty:  # the run record would not describe the pinned source
                print(f"!! {d} is at the pinned commit but has local modifications:\n   " + dirty.replace("\n", "\n   "))
            continue
        if dirty:
            sys.exit(f"{d} is at {head[:7]}, not the pinned {src['commit'][:7]}, and has local changes: "
                     "commit or stash them, or point --sources-root at a fresh directory")
        print(f"== {d.name}: checking out pinned {src['commit'][:7]} (was {head[:7]})")
        if git(["cat-file", "-e", src["commit"]], d).returncode:
            sh(["git", "fetch", "--quiet", "--all"], cwd=d)
        if sh(["git", "checkout", "--quiet", "--detach", src["commit"]], cwd=d):
            sys.exit(f"checkout of {src['commit']} in {d} failed")


def build_w1_images(w1_root: Path):
    """docs/DEVIATIONS.md U-03 (+ U-04 on arm64). docker compose does not order builds by
    depends_on, so `base` is built alone first."""
    pkg = w1_root / "ogc_app_pkg"
    print("== building W1 images")
    if sh(["docker", "compose", "build", "base"], cwd=pkg):
        sys.exit("base image build failed")
    if sh(["docker", "compose", "build", *W1_IMAGES], cwd=pkg):
        sys.exit("tool image build failed")
    # reproject-image.cwl pulls the image without a tag; compose builds :1.0.0
    sh(["docker", "tag", "ogc-ospd/algae-usecase/reproject-image:1.0.0", "ogc-ospd/algae-usecase/reproject-image:latest"])
    if platform.machine() in ("arm64", "aarch64"):
        print("  arm64 host: rewriting the gdal_calc.py shebang in calculate-band (U-04)")
        r = subprocess.run(["docker", "build", "-q", "-t", "ogc-ospd/algae-usecase/calculate-band:1.1.0", "-"],
                           input=ARM64_CALC_FIX.encode())
        if r.returncode:
            sys.exit("calculate-band arm64 fix failed")


def job_file(run, workdir: Path, tmp: Path) -> Path:
    """The job cwltool gets: the clone's example job, with secrets filled from the environment,
    or the inline `inputs:` of the run. Written under `tmp`, never into the clone."""
    if run.get("inputs"):
        p = tmp / "job.json"
        p.write_text(json.dumps(run["inputs"], indent=2))
        return p
    src = workdir / run["job"]
    if not src.is_file():
        sys.exit(f"{run['_name']}: job file {src} not found (is the clone checked out under --sources-root?)")
    doc = yaml.safe_load(src.read_text())
    for name, var in (run.get("secrets") or {}).items():
        val = os.environ.get(var)
        if not val and sys.stdin.isatty():
            val = getpass.getpass(f"{run['_name']}: value for input `{name}` (or set {var}): ")
        if not val:
            sys.exit(f"{run['_name']}: input `{name}` needs the environment variable {var} (no terminal to ask)")
        doc[name] = val
    # relative paths in the job (the AOI file) are resolved against the job file's directory
    for v in doc.values():
        if isinstance(v, dict) and v.get("class") in ("File", "Directory") and "path" in v and not Path(v["path"]).is_absolute():
            v["path"] = str((src.parent / v["path"]).resolve())
    p = tmp / src.name
    p.write_text(yaml.safe_dump(doc, sort_keys=False))
    return p


def run_one(name, run, sources, sources_root: Path, runs_root: Path, force: bool) -> bool:
    run = dict(run, _name=name)
    bag = Path(run["bag"])
    bag = bag if bag.is_absolute() else runs_root / bag
    if (bag / "metadata" / "provenance").is_dir() and not force:
        print(f"== {name}: bag exists at {bag}, skipped (use --force to rerun)")
        return True
    src = sources[run["workflow"]["repo"]]
    workdir = sources_root / src["clone"] / src["base_path"]
    target = run["workflow"]["file"] + (f"#{run['workflow']['element']}" if run["workflow"].get("element") else "")
    results = Path(run.get("results", str(bag) + "-results"))
    results = results if results.is_absolute() else runs_root / results
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    log = bag.parent / f"{bag.name}.cwltool-{stamp}.log"
    bag.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix=f"{name}-") as tmp:
        tmp = Path(tmp)
        job = job_file(run, workdir, tmp)
        tmp_bag = tmp / "ro"
        tmp_out = tmp / "out"
        print(f"== {name}: cwltool {target} ({workdir})")
        t0 = time.time()
        rc = sh(["cwltool", "--timestamps", *(run.get("cwltool_args") or []),
                 "--provenance", str(tmp_bag), "--outdir", str(tmp_out), target, str(job)],
                cwd=workdir, log=log)
        took = int(time.time() - t0)
        if rc != 0 or not (tmp_bag / "metadata" / "provenance").is_dir():
            failed = bag.parent / f"{bag.name}-failed-{stamp}"
            if tmp_bag.is_dir():
                shutil.move(str(tmp_bag), str(failed))
            print(f"   FAILED after {took}s (exit {rc}); log {log}; partial bag {failed if tmp_bag.is_dir() or failed.is_dir() else 'none'}")
            return False
        if bag.is_dir():
            shutil.rmtree(bag)
        shutil.move(str(tmp_bag), str(bag))
        if results.is_dir():
            shutil.rmtree(results)
        shutil.move(str(tmp_out), str(results))
        print(f"   OK in {took}s: bag {bag}, results {results}, log {log}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources-root", type=Path, required=True,
                    help="directory holding the pinned clones named in scripts/sources.yaml (`clone:`)")
    ap.add_argument("--runs-root", type=Path, help="where the research objects go (`runs:` `bag:` paths); default: --sources-root")
    ap.add_argument("--only", nargs="*", metavar="NAME", help="run names to execute (default: all)")
    ap.add_argument("--no-fetch", action="store_true", help="do not clone/checkout the pinned sources under --sources-root")
    ap.add_argument("--build-images", action="store_true", help="build the W1 images first (docs/DEVIATIONS.md U-03/U-04)")
    ap.add_argument("--force", action="store_true", help="replace an existing bag")
    ap.add_argument("--generate", action="store_true", help="run scripts/generate.py afterwards")
    a = ap.parse_args()
    runs_root = a.runs_root or a.sources_root
    sources = yaml.safe_load(SOURCES.read_text())
    runs = sources.get("runs", {})
    names = a.only or list(runs)
    unknown = [n for n in names if n not in runs]
    if unknown:
        sys.exit(f"unknown run(s) {unknown}; known: {list(runs)}")

    if not a.no_fetch:
        ensure_clones(sources, a.sources_root, {runs[n]["workflow"]["repo"] for n in names})
    if a.build_images:
        build_w1_images(a.sources_root / sources["w1"]["clone"])

    ok = True
    for name in names:  # sequentially: two W1 plots at once exhaust a 16 GB Docker VM (U-05)
        ok = run_one(name, runs[name], sources, a.sources_root, runs_root, a.force) and ok
    if not ok:
        sys.exit("at least one run failed; the register was not regenerated")
    if a.generate:
        print("== regenerating the register")
        rc = sh([sys.executable, str(ROOT / "scripts" / "generate.py"),
                 "--sources-root", str(a.sources_root), "--runs-root", str(runs_root)])
        if rc:
            sys.exit(rc)
        print("Now validate with ./build.sh")


if __name__ == "__main__":
    main()
