# Master Plan: Robotics Ontology

## 1. Executive Summary

### Facts

- This repository is a public-facing AI and robotics glossary plus SysML v2 model library. Evidence: `README.md:1`, `README.md:19`.
- It is described as a canonical terminology authority and MBSE model library for related robotics projects. Evidence: `README.md:6`.
- The repo contains `GLOSSARY.md`, `ARCHITECTURE.md`, `docs/OPERATING_STANDARD.md`, and `sysml_v2_models/` with AMR SysML v2 examples. Evidence: `GLOSSARY.md`, `ARCHITECTURE.md`, `docs/OPERATING_STANDARD.md`, `sysml_v2_models/README.md`.
- The README documents a private/public split where the public repo contains curated technical assets and excludes non-public operational context. Evidence: `README.md:35`, `README.md:39`.

### Assumptions

- The public product should be a clean terminology and model reference, not a full ontology runtime.
- Some usage docs describe future or private-only tooling that is not currently present in this public candidate.

### Recommendations

- Position the repo as a curated public glossary and SysML model reference until executable ontology tooling is present.
- Reconcile README/quickstart usage claims with visible files before adding new model content.
- Make the first implementation slice a public-safe source-of-truth and validation-boundary pass.

## 2. Current-State Findings, With File/Path Evidence

### Facts

- `README.md` instructs readers to read `AGENTS.md`, but no repo-local `AGENTS.md` is visible in the current file inventory. Evidence: `README.md:3`.
- `README.md` references `docs/OPERATING_STANDARD.md`, which is present and defines the repo role as glossary and terminology reference. Evidence: `README.md:3`, `docs/OPERATING_STANDARD.md:4`.
- `ARCHITECTURE.md` describes OWL 2, SysML v2, W3C SSN, core classes, and Hermit/Pellet reasoning. Evidence: `ARCHITECTURE.md:7`, `ARCHITECTURE.md:18`.
- `QUICKSTART.md` references `requirements.txt`, `scripts/query_ontology.py`, `scripts/validate_models.py`, and `scripts/export_for_rag.sh`, none of which are visible in the current file inventory. Evidence: `QUICKSTART.md:11`, `QUICKSTART.md:17`, `QUICKSTART.md:23`, `QUICKSTART.md:29`.
- `USAGE.md` references `scripts/validate_models.py` and `scripts/update_rag_index.sh`, not visible in the current file inventory. Evidence: `USAGE.md:11`, `USAGE.md:17`.
- `WALKTHROUGH.md` references `ROADMAP.md`, which is not visible in the current file inventory. Evidence: `WALKTHROUGH.md:16`.
- `sysml_v2_models/README.md` describes AMR decomposition and lists `bdd_amr_architecture.sysml`, `ibd_amr_interconnects.sysml`, `pkg_amr_decomposition.sysml`, and `uaf_reference_outline.md`, all visible in the file inventory. Evidence: `sysml_v2_models/README.md:3`, `sysml_v2_models/README.md:45`.
- Recent git history includes public mirror sync and sanitization commits, including `chore: sanitize robotics ontology public mirror` and `Harden public repository surface`.

### Assumptions

- OWL and reasoner tooling may be planned or private-only, but it is not currently exported.
- SysML models are current public source assets; generated diagrams or rendered model outputs are not present.

### Recommendations

- Downgrade executable ontology and RAG export instructions until the supporting files exist publicly.
- Keep `GLOSSARY.md` and `sysml_v2_models/` as the initial public source of truth.
- Add a validation plan that distinguishes syntax/lint checks available now from semantic reasoning checks planned later.

## 3. Product Requirements

### Facts

- The operating standard says the repo should keep definitions concise and queryable, acronyms and cross-links explicit, glossary consistency across projects, and the terminal baseline simple. Evidence: `docs/OPERATING_STANDARD.md:7`.
- SysML v2 models demonstrate MBSE principles for an AMR system. Evidence: `sysml_v2_models/README.md:3`.

### Assumptions

- Target readers need clear definitions and examples more than a heavy ontology application.

### Recommendations

- Target users:
  - Robotics portfolio reviewer.
  - Engineer looking up terminology used by related public projects.
  - MBSE reviewer inspecting SysML v2 examples.
  - Agent maintaining cross-repo terminology consistency.
- Primary workflows:
  - Look up a term in `GLOSSARY.md`.
  - Inspect AMR SysML v2 model examples.
  - Follow cross-links from related public repos.
  - Run public-safe validation checks before release.
- Non-goals:
  - Production ontology service.
  - Certified model repository.
  - Private RAG index export.
  - Publishing internal taxonomy, private prompts, or private project strategy.
- Required features:
  - Glossary source of truth.
  - SysML v2 model library.
  - Public-safe operating standard.
  - File-reference and claim accuracy checks.
  - Sync provenance from private to public.
- Supporting capabilities:
  - Glossary term linting for duplicates, acronyms, and broken anchors.
  - SysML syntax check if tooling is available.
  - Generated artifact policy for diagrams and exports.
- Admin/operator workflows:
  - Add terms with evidence and cross-link intent.
  - Validate model files after edits.
  - Audit public boundary before sync/publish.
- Error and recovery states:
  - Missing script in quickstart: block release or correct docs.
  - Definition drift: update source glossary and dependent links together.
  - Generated diagram drift: regenerate from source or mark as stale.
- Data handling:
  - Public docs and model text are source.
  - Generated diagrams, RAG exports, validation logs, and private ontology artifacts are generated or private unless approved.

## 4. DORA AI Capability Alignment

### Facts

- The repo provides shared terminology that other projects link to. Evidence: `README.md:30`.
- The current public export is mostly documentation and SysML model text.

### Assumptions

- AI agents can use this repo as public context for terminology, but should not infer private project strategy.

### Recommendations

- AI stance:
  - Allowed: public glossary lookup, cross-link checks, duplicate term detection, SysML text review, public-safe doc generation.
  - Restricted: ontology reasoning output and RAG exports until tooling and source boundaries are public.
  - Prohibited: private project notes, internal taxonomy not exported, customer data, secrets, private prompts, and unsupported safety/certification claims.
- Data ecosystem:
  - Maintain a source register for glossary entries, SysML files, diagrams, and generated exports.
  - Track owner, freshness, and dependent public repos for each term group.
- AI-accessible internal data:
  - Public glossary and SysML models only.
  - No private RAG indices or private implementation references.
- Version control:
  - Small changes by term group or model file.
  - Review generated-vs-source boundaries.
  - Sync manifest reviewed for private provenance leakage.
- Small batches:
  - First useful slice: reconcile docs with actual public files and add validation boundary.
- User-centricity:
  - Named user: robotics reviewer.
  - Job-to-be-done: understand terms and model examples used across public robotics repos.
  - Success signal: reader can resolve terms and inspect models without broken instructions.
- Internal platform:
  - One-command docs/model validation should eventually run locally without private tools.
- Missing DORA evidence:
  - No visible validation scripts or requirements file despite quickstart references.
  - First action: correct docs or add public-safe validation tooling.

## 5. Architecture Plan

### Facts

- Existing architecture:
  - `GLOSSARY.md`: glossary content.
  - `ARCHITECTURE.md`: ontology architecture narrative.
  - `sysml_v2_models/`: SysML v2 model text and UAF outline.
  - `docs/OPERATING_STANDARD.md`: documentation standard.
  - Root quickstart/usage/walkthrough docs with currently stale executable references.

### Assumptions

- A future ontology toolchain should be optional and public-safe.

### Recommendations

- Proposed architecture:
  - `GLOSSARY.md`: canonical human-readable source.
  - `sysml_v2_models/`: canonical model source.
  - `docs/`: operating standard, contribution/modeling conventions, validation boundaries.
  - `scripts/`: future public-safe validation, link checking, anchor checking, and generated artifact inspection.
  - `generated/`: ignored or explicitly managed output for rendered diagrams and exports.
- Data flow:
  - Glossary/source models -> validation/lint -> optional generated diagrams/exports -> release artifact.
- External integrations:
  - SysML v2 tooling, optional OWL editor/reasoner, markdown link checker.
  - No private RAG or ontology service integration in public release.
- Configuration/secrets:
  - No `.env`, credentials, private RAG endpoints, private repo URLs, or local tool paths.
- ADR needs:
  - ADR: glossary Markdown as source vs OWL as source.
  - ADR: public validation tooling scope.
  - ADR: generated diagram/export retention policy.

## 6. Feature Roadmap

### Recommendations

- Milestone 1: Public doc/reference reconciliation.
  - Acceptance: quickstart, usage, walkthrough, and README reference only present files or mark future/private tools clearly.
- Milestone 2: Glossary quality baseline.
  - Acceptance: duplicate headings, acronyms, anchors, and cross-links are checked.
- Milestone 3: SysML validation baseline.
  - Acceptance: each `.sysml` file has a documented validation path, even if tooling is external.
- Milestone 4: Generated artifact policy.
  - Acceptance: diagrams/exports are labeled source-derived and not confused with source.
- Milestone 5: Optional public ontology tooling.
  - Acceptance: `requirements.txt` and scripts exist, use public fixtures only, and pass static checks.

## 7. Parallelization Plan

### Recommendations

- Workstream A: Documentation reconciliation.
  - Owns: `README.md`, `QUICKSTART.md`, `USAGE.md`, `WALKTHROUGH.md`.
  - Verification: file-reference check.
- Workstream B: Glossary quality.
  - Owns: `GLOSSARY.md`.
  - Verification: heading/anchor duplicate check and cross-link check.
- Workstream C: SysML model validation.
  - Owns: `sysml_v2_models/*.sysml`, `sysml_v2_models/README.md`.
  - Verification: syntax/model tool or documented manual check.
- Workstream D: Public-release boundary.
  - Owns: docs and future scripts.
  - Verification: public-surface audit and artifact-boundary check.
- Sequential gates:
  - Do not add RAG export or reasoner tooling until source boundaries and fixtures are defined.
- Merge strategy:
  - Keep glossary edits separate from model edits to simplify review.

## 8. Task Backlog

| Priority | Task | Likely files | Tests/docs | Verification | Done condition |
| --- | --- | --- | --- | --- | --- |
| P0 | Reconcile missing `AGENTS.md` reference | `README.md` | Docs | File existence check | No broken instruction reference |
| P0 | Reconcile missing scripts and `requirements.txt` references | `QUICKSTART.md`, `USAGE.md` | Docs | File existence check | Quickstart reflects public files |
| P0 | Reconcile missing `ROADMAP.md` reference | `WALKTHROUGH.md` | Docs | File existence check | No missing roadmap reference |
| P0 | Add glossary validation boundary | docs or future script | Docs | Heading/anchor check | Validation expectations are clear |
| P1 | Add SysML validation instructions | `sysml_v2_models/README.md` | Docs | Tool/manual check | Each model has a validation path |
| P1 | Add generated artifact policy | docs | Policy docs | Artifact manifest review | Diagrams/exports do not blur source role |
| P2 | Add public-safe validation scripts | future `scripts/`, `requirements.txt` | Tests/docs | Run scripts | Tooling matches quickstart |

## 9. Testing And Verification Plan

### Recommendations

- Unit tests:
  - Future glossary parser tests if scripts are added.
- Integration tests:
  - Future SysML/OWL consistency checks only after public tools exist.
- Static checks:
  - `git diff --check`.
  - Markdown link and file-reference checks.
  - Heading duplicate and anchor checks in `GLOSSARY.md`.
  - Scan for unsupported claims about reasoner availability.
- Model checks:
  - Validate `.sysml` syntax with documented tool if available.
  - If unavailable, perform manual review and mark tool gap.
- Security/privacy checks:
  - Scan for private repo references beyond approved private/public split, credentials, private prompts, internal notes, generated RAG exports, customer data, and private strategy.
- Artifact-boundary checks:
  - Inspect generated diagrams/exports and release archive manifests.
- Regression loop:
  - Any term/model change -> static docs check -> model validation -> cross-repo link impact review.

## 10. Release Criteria

### Recommendations

- Definition of done:
  - Public docs and visible files agree.
  - Glossary and model claims are backed by source files.
  - Missing tools are not advertised as runnable.
  - Public/private split is explicit.
- Public readiness:
  - No private operational context, private prompts, internal task lists, customer data, secrets, or private strategy.
  - No claims that the ontology is a certified safety model or production reasoner unless evidence exists.
- Artifact boundary:
  - Source files and generated outputs are separated.
  - Release archive is inspected, extracted, and scanned.
- Operational handoff:
  - A maintainer knows how to add a term, validate a model, and audit public safety.
- Remote preservation:
  - No push or publication without explicit user approval.

## 11. Risks And Open Questions

### Risks

- Broken public instructions reduce credibility.
- Architecture docs may imply OWL/reasoner implementation not present in public files.
- Generated RAG exports could leak private context if added without a boundary.
- Glossary drift could break linked public repos.
- SysML syntax may be unvalidated if tooling is absent.

### Open Questions

- Is Markdown glossary the long-term canonical source, or will OWL become canonical?
- Should public validation scripts be added now, or should docs remain tool-agnostic?
- Which SysML v2 toolchain is the supported validation target?
- Should cross-repo glossary links be tested from this repo or from each dependent repo?

## 12. Recommended First Implementation Slice

### Recommendation

Create a public source-of-truth reconciliation slice.

### Why It Is First

- It fixes the mismatch between docs and visible files.
- It protects the public export boundary before adding ontology tooling.
- It gives future agents a reliable baseline.

### What It Changes

- Update docs to stop referencing absent local files and scripts.
- Add validation-boundary language for glossary and SysML models.
- Add public-surface and artifact-boundary release checks.

### What It Does Not Change

- No private RAG export.
- No private ontology source import.
- No unsupported reasoner claims.
- No public publishing.

### Acceptance Criteria

- All internal file references resolve.
- Glossary and SysML source roles are explicit.
- Generated diagrams/exports have a clear policy.
- Release criteria include public-surface audit, sanitized source boundary, artifact-boundary checks, claim accuracy, generated-vs-source separation, and sync-from-private provenance.

### Verification Path

1. Run file-reference and link checks.
2. Run glossary heading/anchor checks.
3. Validate SysML files with available tooling or record manual review.
4. Run `git diff --check`.
5. Scan release artifact contents before publication.
