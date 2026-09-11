# Architecture: Public Robotics Reference

## Scope

This repository is a static technical reference. Its source of truth is:

- [GLOSSARY.md](GLOSSARY.md) for terminology and concise context;
- [sysml_v2_models/](sysml_v2_models/) for illustrative SysML v2 textual AMR
  models; and
- [docs/OPERATING_STANDARD.md](docs/OPERATING_STANDARD.md) for documentation
  conventions.

There is no running service, ontology database, OWL export, reasoner, RAG
pipeline, simulator integration, or deployment configuration in this public
repository.

## Relationships

The three SysML example files describe complementary views of the same
illustrative Autonomous Mobile Robot:

1. `bdd_amr_architecture.sysml` defines parts and ports.
2. `ibd_amr_interconnects.sysml` instantiates those parts and connects flows.
3. `pkg_amr_decomposition.sysml` records the package-to-part hierarchy.

The glossary explains terms that readers encounter in these examples and in
the related public repositories. It is documentation support, not a formal
machine-reasoned ontology.

## Validation boundary

`python3 scripts/check_links.py` verifies internal Markdown links and SysML
file references. Formal SysML parsing, rendering, and semantic validation
require a separately selected external toolchain and are not verified by this
repository.

## Public boundary

Keep the repository limited to public documentation and illustrative models.
Do not add private operational context, credentials, customer data, unpublished
research material, machine identifiers, deployment configuration, or claims of
safety certification, production readiness, or formal reasoning that the
checked-in files cannot support.
