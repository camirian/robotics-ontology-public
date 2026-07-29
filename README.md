# The AI & Robotics SME Glossary

For repo-specific working rules, read [AGENTS.md](AGENTS.md) and [docs/OPERATING_STANDARD.md](docs/OPERATING_STANDARD.md).


> **Part of the Onyx Citadel Cyber-Physical AI Ecosystem**
> *This repository is the canonical terminology authority and MBSE model library for every cyber-physical project in the Citadel. All other repositories hyperlink back to the GLOSSARY.md defined here.*
Welcome to my personal AI & Robotics Glossary. This glossary is a curated, living document of the key terms, concepts, and acronyms that form the language of modern robotics and artificial intelligence.

## 🚀 Purpose

The goal of this glossary is to serve two primary purposes:

1.  **A Knowledge Base:** To solidify my own understanding of core concepts by articulating them in a clear and concise manner.
2.  **A Professional Resource:** To provide context for the technologies and methodologies used in my other portfolio projects, demonstrating a deep and thorough understanding of the field.

This document is a foundational component of my journey to becoming a Subject Matter Expert (SME) in AI and Robotics.

## 🏛️ Systems Engineering (SysML v2 Models)

In addition to the glossary, this workspace hosts foundational Model-Based Systems Engineering (MBSE) artifacts for complex robotic systems. See the [`sysml_v2_models/`](./sysml_v2_models/) directory for standard-compliant SysML v2 block definition, internal block, and system decomposition models.


> [!WARNING]
> DO NOT edit models or documentation natively. Launch via **"Dev Containers: Reopen in Container"** to enforce standardized formatting and text engineering integrity.

## 🔗 Integration

Terms defined in this glossary are linked from the `README.md` files of my other projects. This creates a cohesive and interconnected professional portfolio.

## 📜 License

This project is licensed under the Apache 2.0 License. See the [`LICENSE`](./LICENSE) file for details.

## Private vs public variant strategy

This repo has two coordinated copies:

- `robotics-ontology` (private): working repo with internal notes and implementation references.
- `robotics-ontology-public` (public): sanitized, portfolio-safe publication surface.

The split exists to keep non-public operational context separate while ensuring the public
repo contains only curated technical assets.

### How to keep them aligned

From the private repo root:

1. `./scripts/sync-public.sh`
2. Review the printed status diff.
3. `./scripts/sync-public.sh --push`

Preferred shorthand:

1. `make sync-check`
2. `make sync-preflight` (runs strict check + strict dry-run)
3. `make sync-push`

`--dry-run` is supported for preview-only operation.

Each successful non-dry-run sync writes an auditable `public-sync-manifest.json` into
the public repo summarizing:

- source private commit and branch
- public remote/branch
- sync mode flags
- changed paths in that sync

For deterministic full-prune exports, use:

1. `./scripts/sync-public.sh --strict --dry-run` (or `make sync-dry-run`)
2. `./scripts/sync-public.sh --strict --push` (or `make sync-push`)
