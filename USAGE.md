# Robotics Ontology: Usage & Modeling Protocols

## 1. Defining a New Robot Type
1. Create a new `.sysml` file in `sysml_v2_models/`.
2. Inherit from the base `RoboticSystem` class.
3. Define the `Actuators` and `Sensors` using the classes defined in `GLOSSARY.md`.

## 2. Validating the Model
Run the consistency check:
```bash
python3 scripts/validate_models.py --path sysml_v2_models/my_new_robot.sysml
```

## 3. Exporting Knowledge
To update the LLM's understanding of the robotic domain:
```bash
./scripts/update_rag_index.sh
```

## 4. Troubleshooting
### Reasoning Timeout
If the reasoner hangs, check for circular dependencies in the class hierarchy. Use the `--depth` flag to limit reasoning complexity.

### SysML Syntax Errors
Verify that you are using the SysML v2 textual notation (KerML).
