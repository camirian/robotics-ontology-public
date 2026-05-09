# Verification Plan

## Checks

Run the public-export gate before publishing changes:

```bash
python3 repo_preflight.py --repo . --profile public-export --paranoid
```

Manual review:

- Confirm terms and models are generic public examples.
- Confirm no private architecture, private identifiers, or controlled material is included.
- Confirm claims avoid completeness, certification, and production-readiness language.

## Release Decision

Release only when automated checks and manual boundary review pass.

