# UAF Reference Outline: Autonomous Mobile Robot (AMR)

This outline maps the AMR system to the Unified Architecture Framework (UAF) to demonstrate advanced MBSE capabilities (Claim `CERT_04`).

## 1. Concept View (CV)
*   **CV-1 (Vision):** The high-level vision for the AMR is to provide autonomous navigation and operation within a structured environment.
*   **CV-2 (Capability Taxonomy):** Identifies the core capabilities: Navigation, Perception, Computation, and Actuation.

## 2. Operational View (OV)
*   **OV-1 (High-Level Operational Concept Graphic):** A high-level illustration of the AMR interacting with its environment (e.g., navigating a warehouse, avoiding obstacles).
*   **OV-2 (Operational Resource Flow Description):** Describes the exchange of information and physical resources between the AMR and external entities (e.g., human operators, charging stations).
*   **OV-5b (Operational Activity Model):** Details the operational activities, such as "Move to Waypoint," "Scan for Obstacles," and "Process Sensor Data."

## 3. Systems View (SV)
*   **SV-1 (Systems Interface Description):** Maps directly to our `ibd_amr_interconnects.sysml`. Defines the system nodes (Compute, Sensor, Motor, Power) and their interfaces.
*   **SV-2 (Systems Resource Flow Description):** Details the data and power flows documented in the IBD.
*   **SV-4 (Systems Functionality Description):** Maps operational activities (from OV-5b) to system functions performed by the AMR components.

## 4. Logical View
*   **Logical Architecture:** Maps directly to `bdd_amr_architecture.sysml` and `pkg_amr_decomposition.sysml`, defining the logical separation of systems (Package -> Block -> Part).
