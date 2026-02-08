#!/usr/bin/env python3
import argparse, json, pathlib, sys


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
    if not data.get("id"):
        errors.append("id is required")
    if not data.get("version"):
        errors.append("version is required")
    if not isinstance(data.get("roles"), list) or not data.get("roles"):
        errors.append("roles[] is required")
    else:
        for r in data["roles"]:
            pf = r.get("prompt_file")
            if not pf:
                errors.append(f"role {r.get('name')} missing prompt_file")
                continue
            if not (d / pf).exists():
                errors.append(f"prompt file not found: {pf}")

    return len(errors) == 0, errors


def validate_all(root="packs"):
    rootp = pathlib.Path(root)
    if not rootp.exists():
        print("packs directory missing")
        return 1
    failed = 0
    total = 0
    for d in sorted(rootp.iterdir()):
        if not d.is_dir():
            continue
        total += 1
        ok, errors = validate(d)
        if ok:
            print(f"VALID {d}")
        else:
            failed += 1
            print(f"INVALID {d}")
            for e in errors:
                print("-", e)
    print(f"Checked packs: {total}, failed: {failed}")
    return 1 if failed else 0


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", help="Path to role pack folder")
    ap.add_argument("--all", action="store_true", help="Validate all packs/*")
    args=ap.parse_args()
    if args.all:
        sys.exit(validate_all())
    if not args.path:
        print("Provide a pack path or use --all")
        sys.exit(2)
    ok, errors = validate(args.path)
    if ok:
        print("VALID")
        sys.exit(0)
    print("INVALID")
    for e in errors:
        print("-", e)
    sys.exit(1)

if __name__ == "__main__":
    main()
