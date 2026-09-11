# Public Reference Plan

## Current role

This repository is a public, docs-only reference for robotics terminology and
illustrative SysML v2 textual models. The source of truth is the glossary, the
model examples, and the operating standard. It is not an executable ontology,
reasoner, RAG system, simulator, or deployment project.

## Public contract

- Publish only public documentation and illustrative model text.
- Keep claims tied to files a visitor can inspect.
- Do not imply safety certification, hardware validation, production readiness,
  formal reasoning, or private-system integration.
- Do not add private operational context, credentials, customer data,
  unpublished research material, machine identifiers, or deployment settings.

## Maintenance priorities

1. Keep the README, quickstart, usage guide, walkthrough, and architecture
   description aligned with the checked-in files.
2. Keep glossary definitions concise, cross-linked, and consistent with related
   public repositories.
3. Keep the SysML examples readable and explicitly illustrative.
4. Run `python3 scripts/check_links.py` after documentation or model-reference
   changes.
5. For public-facing changes, review the exact diff for unsupported claims and
   private context before merging.

## Deliberate non-goals

The repository does not provide a bundled SysML parser, renderer, semantic
validator, ontology reasoner, RAG index, or simulation integration. Any future
tooling must use public inputs, document its scope, and avoid implying that a
successful static check validates a robot or a safety property.
