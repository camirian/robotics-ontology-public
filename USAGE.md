# Using the Robotics Reference

This repository is a browsable reference, not an executable ontology service.
It includes a Markdown glossary and illustrative SysML v2 textual models.

## Look up a term

Start with [GLOSSARY.md](GLOSSARY.md). Entries define terminology used by the
related public robotics projects and link to relevant concepts where useful.

## Inspect the model examples

Read [sysml_v2_models/README.md](sysml_v2_models/README.md), then open the
three AMR model files in that directory. They are examples for study and
adaptation; this repository does not bundle a SysML parser, renderer, or
semantic validator.

If you need formal parsing or rendering, choose and install an external SysML
v2 toolchain independently. Its output is outside this repository's verified
scope.

## Check repository links

The included standard-library checker verifies internal Markdown links and
SysML file references:

```bash
python3 scripts/check_links.py
```

It checks repository references only. It does not validate SysML syntax,
reason about a model, build a RAG index, or make a safety claim.
