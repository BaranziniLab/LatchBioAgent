# LatchBioAgent

Retired. This extension no longer calls Latch and only reports that it is retired. Remove it.

Current version: **0.2.0**

> **Retired.** LatchBioAgent was retired on 2026-11-22 and no longer calls any service. Why: It was a generic API wrapper that was never checked against a real Latch workspace, and no maintained replacement exists today. Use instead: Nothing in BAAM replaces it today. Ask for a rebuild on Latch's own Python SDK if you need it.

This is the final release of a retired Biorouter extension. It replaces every
earlier tool with one, `latchbio_status`, which shows the notice above. It holds no
credentials, reads no setting and calls no service. Remove the extension in
Biorouter once you no longer need the notice.

## Tools

- `latchbio_status`: shows why LatchBioAgent was retired and what to use instead. It calls no service.

## Bundled skills

Every skill an earlier release bundled is kept, and each now says where its content
moved. An update never deletes a file an earlier version installed, so keeping the
paths is what replaces the old instructions.

## Develop and release

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python scripts/build_brxt.py
```

Do not edit `src/latchbioagent/_kit/` or `tests/kit_testing/`: they are vendored from the BRXT
adapter kit in the Biorouter repository (`scripts/brxt-adapter-kit/`).

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
