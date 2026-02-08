# OpenClaw Role Pack Hub

A curated collection of production-ready role packs for OpenClaw workflows.

## Why
Most users need ready-to-use role packs, not raw prompt engineering from scratch.

## What is a role pack
A role pack is a reusable set of role prompts for a domain, e.g.:
- startup
- growth
- security
- support
- research

## Planned MVP
- Standard role-pack format
- Validation script
- Installer helper for local OpenClaw setups
- Community submissions via PR templates

## Goal
Make role-based automation plug-and-play.

## Status
Scaffold released. Seeking contributors.



## Working scaffold validator
```bash
python3 tools/validate_pack.py packs/startup-basic
```


## Validate all packs
```bash
python3 tools/validate_pack.py --all
```

## Role-pack schema
See `schemas/role-pack.schema.json`.


## Install
```bash
pip install -e .
rolepackhub --all
```

## Tests
```bash
python3 -m pytest -q
```


## End-to-end demo
```bash
bash demo/run_demo.sh
```
See generated artifacts in `demo/`.
