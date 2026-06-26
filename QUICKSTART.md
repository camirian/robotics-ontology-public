# Quickstart: Browsing This Repository

This repo is **docs-only** — a glossary plus a SysML v2 model library. There is nothing to install or build. You read it directly.

## 1. Get the files (optional)

You can read everything on GitHub in the browser. To work locally:

```bash
git clone https://github.com/camirian/robotics-ontology-public.git
cd robotics-ontology-public
```

No dependencies, no `requirements.txt`, no virtual environment needed.

## 2. Look up terminology

Open [`GLOSSARY.md`](./GLOSSARY.md). Terms are grouped alphabetically; each entry has a definition and a short note on context/significance.

## 3. Read the SysML v2 models

Open the [`sysml_v2_models/`](./sysml_v2_models/) directory and start with its [`README.md`](./sysml_v2_models/README.md), which explains the three models and renders a Mermaid decomposition diagram. The `.sysml` files are plain SysML v2 textual (KerML) notation — open them in any text editor or on GitHub:

- [`sysml_v2_models/bdd_amr_architecture.sysml`](./sysml_v2_models/bdd_amr_architecture.sysml)
- [`sysml_v2_models/ibd_amr_interconnects.sysml`](./sysml_v2_models/ibd_amr_interconnects.sysml)
- [`sysml_v2_models/pkg_amr_decomposition.sysml`](./sysml_v2_models/pkg_amr_decomposition.sysml)

To parse or render them formally, use an external SysML v2 toolchain (for example the SysIDE editor or the SysML v2 reference implementation / Jupyter kernel). This repo does not bundle one.

## 4. (Optional) Verify internal links

A standard-library-only checker confirms every internal Markdown link and SysML reference resolves:

```bash
python3 scripts/check_links.py
```

Requires only Python 3.8+.
