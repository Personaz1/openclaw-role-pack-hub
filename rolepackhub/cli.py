import argparse, pathlib, json, sys


def validate(pack_dir):
    d = pathlib.Path(pack_dir)
    pj = d / "pack.json"
    if not pj.exists():
        return False, ["pack.json missing"]
    try:
        data = json.loads(pj.read_text(encoding="utf-8"))
    except Exception as e:
        return False, [f"invalid JSON: {e}"]
    errors = []
    if not data.get("id"): errors.append("id is required")
    if not data.get("version"): errors.append("version is required")
    if not isinstance(data.get("roles"), list) or not data.get("roles"): errors.append("roles[] is required")
    else:
        for r in data["roles"]:
            pf = r.get("prompt_file")
            if not pf or not (d / pf).exists():
                errors.append(f"prompt file not found: {pf}")
    return len(errors) == 0, errors


def validate_all(root="packs"):
    failed = 0
    total = 0
    for d in sorted(pathlib.Path(root).iterdir()):
        if d.is_dir():
            total += 1
            ok, _ = validate(d)
            if not ok: failed += 1
    print(f"checked={total} failed={failed}")
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(prog="rolepackhub")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("path", nargs="?")
    a = ap.parse_args()
    if a.all:
        raise SystemExit(validate_all())
    if not a.path:
        print("Provide pack path or --all")
        raise SystemExit(2)
    ok, errs = validate(a.path)
    if ok:
        print("VALID")
        return
    print("INVALID")
    for e in errs: print("-", e)
    raise SystemExit(1)

if __name__ == "__main__":
    main()
