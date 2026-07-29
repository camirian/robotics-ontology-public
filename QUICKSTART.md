# Robotics Ontology: Quickstart Guide

## 1. Prerequisites
- Python 3.10+.
- Protege or similar OWL editor (optional).

## 2. Installation
```bash
git clone gitea@localhost:citadel/robotics-ontology.git
cd robotics-ontology
pip install -r requirements.txt
```

## 3. Querying the Ontology
To run a sample SPARQL query against the robotics model:
```bash
python3 scripts/query_ontology.py --query="Identify all actuator subclasses."
```

## 4. Validating SysML Models
Check for consistency between the OWL ontology and the SysML v2 models:
```bash
python3 scripts/validate_models.py --path sysml_v2_models/
```

## 5. Knowledge Base Integration
Export the ontology for use in the RAG pipeline:
```bash
./scripts/export_for_rag.sh
```
