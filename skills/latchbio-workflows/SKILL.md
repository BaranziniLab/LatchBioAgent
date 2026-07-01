---
name: latchbio-workflows
description: Use LatchBioAgent when working with LatchBio platform data, API resources, provenance, or reproducibility checks from inside BioRouter.
license: Apache-2.0
user-invocable: false
---

# LatchBioAgent Skill

Use this extension to inspect LatchBio workflows, workspace objects, and execution metadata. Keep workflow launches gated behind explicit user confirmation.

## Operating rules

- Start with `get_latchbioagent_status` to confirm whether credentials and base URLs are configured.
- Use `get_latchbioagent_request_plan` before any endpoint that may create, update, launch, upload, or delete a resource.
- Prefer read-only `GET` requests through `call_latchbioagent_api` while exploring.
- Do not pass `allow_mutation=true` unless the user has explicitly approved the exact operation, target resource, and expected side effect.
- Preserve platform IDs, versions, owners/authors, timestamps, and URLs in any report.
- Never print API tokens, passwords, bearer headers, or session cookies.

## Useful starting endpoints

- `/workflows`
- `/executions`
- `/data`
