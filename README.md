# AI & Robotics Glossary + SysML v2 Model Library

A curated, docs-only reference for cyber-physical robotics work. It contains two things:

1. **[`GLOSSARY.md`](./GLOSSARY.md)** — a living glossary of the terms, acronyms, and concepts used across modern robotics and AI (ROS 2, build tooling, NVIDIA Isaac Sim / Jetson, simulation workflows, and more).
2. **[`sysml_v2_models/`](./sysml_v2_models/)** — a small library of standard-compliant **SysML v2 textual** models for an Autonomous Mobile Robot (AMR), demonstrating Model-Based Systems Engineering (MBSE) decomposition.

There is no build step, no service, and no code to run — everything here is Markdown and SysML v2 text that you read and browse directly on GitHub.

## What this is (and isn't)

- **It is** a personal, curated terminology reference and a worked example of SysML v2 textual modeling that other projects can hyperlink back to.
- **It isn't** an executable OWL ontology, a reasoner, or a RAG pipeline. Despite the historical "ontology" name, no formal OWL/SSN ontology or reasoning engine ships in this repo.

## How to navigate

| If you want to… | Go to |
| --- | --- |
| Look up a term or acronym | [`GLOSSARY.md`](./GLOSSARY.md) |
| See the AMR SysML v2 models and how they fit together | [`sysml_v2_models/README.md`](./sysml_v2_models/README.md) |
| Read a short browse guide | [`QUICKSTART.md`](./QUICKSTART.md) |
| Understand the documentation conventions | [`docs/OPERATING_STANDARD.md`](./docs/OPERATING_STANDARD.md) |

## SysML v2 models

The [`sysml_v2_models/`](./sysml_v2_models/) directory models an AMR across three complementary views, plus a UAF mapping outline:

- **`bdd_amr_architecture.sysml`** — block/part definitions (compute, sensors, motor controller, power) with attributes and ports.
- **`ibd_amr_interconnects.sysml`** — instantiates those parts inside an `AMR_Platform` and wires their ports (data and power flows).
- **`pkg_amr_decomposition.sysml`** — the `Package → Part → Port` hierarchy using redefinitions.
- **`uaf_reference_outline.md`** — a draft outline mapping the AMR to the Unified Architecture Framework.

The files are plain text using SysML v2 textual (KerML) notation. View them in any editor or directly on GitHub; the Mermaid diagram in [`sysml_v2_models/README.md`](./sysml_v2_models/README.md) renders the structural decomposition.

## Optional: check internal links

A small standard-library-only Python script verifies that every internal Markdown link and SysML file reference in this repo resolves:

```bash
python3 scripts/check_links.py
```

It needs only Python 3.8+ (no dependencies) and is the only runnable thing in the repo.

## Integration

Terms defined in [`GLOSSARY.md`](./GLOSSARY.md) are intended to be linked from the `README.md` files of related projects, creating a cohesive cross-project terminology reference.

## License

Licensed under the Apache 2.0 License. See [`LICENSE`](./LICENSE) for details.
