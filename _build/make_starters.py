"""Builds LabN/LabN-starter.zip from LabN/exercises/ for every lab.

Run after changing any starter code:   python make_starters.py

Each zip's top-level folder is LabN/, so extracting it into a student's CSSSKL342
folder gives CSSSKL342/LabN/exercises/ex1-.../ (and LabN/examples/) -- the layout each lab page asks for and the
folder students zip and submit. Build leftovers (.o files, compiled programs) are
never included.
"""
import os
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
FIXED_TIME = (2026, 1, 1, 0, 0, 0)        # same bytes on every build


def is_leftover(path):
    if path.endswith((".o", ".exe")):
        return True
    with open(path, "rb") as f:
        return f.read(4) == b"\x7fELF"     # a compiled Linux program


for n in range(1, 6):
    src = os.path.join(ROOT, f"Lab{n}", "exercises")
    if not os.path.isdir(src):
        continue
    # (folder, prefix in the zip): the zip mirrors the lab folder here, so a student
    # gets LabN/exercises/exK-.../ and LabN/examples/..., where the pages' "open in
    # VS Code" links (assets/vscode.js) look for them.
    trees = [(src, "exercises/")]
    ex = os.path.join(ROOT, f"Lab{n}", "examples")
    if os.path.isdir(ex):
        trees.append((ex, "examples/"))
    out = os.path.join(ROOT, f"Lab{n}", f"Lab{n}-starter.zip")
    names = []
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for top, prefix in trees:
            for d, dirs, files in os.walk(top):
                dirs.sort()
                for f in sorted(files):
                    p = os.path.join(d, f)
                    if is_leftover(p):
                        continue
                    arc = f"Lab{n}/" + prefix + os.path.relpath(p, top).replace(os.sep, "/")
                    info = zipfile.ZipInfo(arc, FIXED_TIME)
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o644 << 16          # rw-r--r-- when unzipped on Linux/Mac
                    with open(p, "rb") as fh:
                        z.writestr(info, fh.read())
                    names.append(arc)
    print(f"wrote {os.path.relpath(out, ROOT)}: {len(names)} files")
