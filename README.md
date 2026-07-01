# LatchBioAgent

MCP access to LatchBio workspace, workflow, file, and execution metadata with guarded API request helpers for reproducible computational biology workflows.

This repository follows the BioRouter `.brxt` extension convention used by `SPOKEAgent` and `UCSFOMOPAgent`: a root `manifest.json`, Python package under `src/`, and optional bundled skills under `skills/`.

## Tools

- `get_latchbioagent_status`: report configured environment variables without revealing secrets.
- `get_latchbioagent_request_plan`: explain whether an API request is read-only or requires explicit mutation approval.
- `call_latchbioagent_api`: call a platform API endpoint with write methods blocked unless `allow_mutation=true`.
- `summarize_latchbioagent_resource`: summarize a JSON export or API payload without making a network call.

## Configuration

| Variable | Required | Secret | Purpose |
|---|---:|---:|---|
| `LATCHBIO_API_TOKEN` | true | true | LatchBio API token |
| `LATCHBIO_BASE_URL` | false | false | LatchBio API base URL |
| `LATCHBIO_LOG_LEVEL` | false | false | Logging level |


## Build

```bash
uv sync
scripts/build_brxt.sh
```

The bundle is written to `dist/latchbioagent.brxt`.

## Install in BioRouter

```bash
biorouter extension install dist/latchbioagent.brxt
```

Add the required secrets with `--secret KEY=value` or configure them in the BioRouter UI.

## License

Apache-2.0. See `LICENSE`.
