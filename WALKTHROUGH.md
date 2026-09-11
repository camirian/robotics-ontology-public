# Robotics Reference Walkthrough

## 1. Discover the vocabulary

Browse [GLOSSARY.md](GLOSSARY.md) to find terms for robotic components,
interfaces, simulation, and systems engineering.

## 2. Review the structural examples

Open [sysml_v2_models/README.md](sysml_v2_models/README.md) for the AMR model
overview, then inspect the SysML v2 textual files it links to. The examples
show decomposition and interconnection; they are not a complete robot design.

## 3. Keep claims within the public boundary

This repository does not include an OWL ontology, a reasoner, safety policies,
a RAG index, simulation configuration, or deployment tooling. Do not infer
those capabilities from the historical repository name or the model examples.

## 4. Verify navigability before sharing changes

Run the internal-reference check:

```bash
python3 scripts/check_links.py
```

For a public-facing change, also inspect the changed files for unsupported
claims, private context, and references to tools that are not included here.
