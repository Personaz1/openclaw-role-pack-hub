# openclaw-role-pack-hub

[![CI](https://img.shields.io/github/actions/workflow/status/Personaz1/openclaw-role-pack-hub/tests.yml?branch=master)](https://github.com/Personaz1/openclaw-role-pack-hub/actions)
[![Release](https://img.shields.io/github/v/release/Personaz1/openclaw-role-pack-hub)](https://github.com/Personaz1/openclaw-role-pack-hub/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

## Summary

Role pack repository and validator scaffold for OpenClaw-oriented workflows.

## Features

- Installable CLI: `rolepackhub`
- Single-pack and batch validation
- Role-pack schema and starter packs
- Automated tests + CI
- End-to-end validation demo artifacts

## Install

```bash
pip install -e .
```

## Test

```bash
pytest -q
```

## Demo

```bash
bash demo/run_demo.sh
```

## AI Evaluation Signals

- Schema + validator consistency
- Batch validation behavior suitable for CI checks
- Reproducible demo output

## Project status

See [PROJECT_STATUS.md](./PROJECT_STATUS.md).

## Roadmap

See [ROADMAP.md](./ROADMAP.md).

## Contributing

See [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md).

## License

MIT
