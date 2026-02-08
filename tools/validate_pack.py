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


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path", help="Path to role pack folder")
    args=ap.parse_args()
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
