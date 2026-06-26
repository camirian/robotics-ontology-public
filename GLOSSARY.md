# AI & Robotics Glossary

An active glossary of terms, concepts, and acronyms used throughout my AI and robotics projects.

---

## A

### ament_cmake
-   **Definition**: The build type for C++-based ROS 2 packages. It is an extension of CMake that adds ROS 2-specific functionality.
-   **Context/Significance**: We used this as the build type for our `cpp_pubsub` package. The `CMakeLists.txt` file is the entry point for this build system.

---

## C

### CMake
-   **Definition**: An open-source, cross-platform family of tools designed to build, test, and package software. It is the standard build system for C++ projects.
-   **Context/Significance**: In Phase 2, we edited the `CMakeLists.txt` file to tell `colcon` how to compile our C++ code into executable nodes and link them against the necessary ROS 2 libraries.

### Colcon
-   **Stands For**: **Co**llective **Con**struction
-   **Definition**: The standard build tool for ROS 2. It is used to compile and build workspaces containing one or more ROS 2 packages.
-   **Context/Significance**: We use `colcon build` to turn our source code into executable nodes that ROS 2 can run.

---

## D

### DDS
-   **Stands For**: Data Distribution Service
-   **Definition**: An industry-standard, peer-to-peer communication protocol for real-time systems.
-   **Context/Significance**: DDS is the underlying middleware that makes ROS 2's communication system work, enabling the robust, distributed environment we set up in Phase 1.

---

## G

### Git
-   **Definition**: A distributed version control system for tracking changes in source code.
-   **Context/Significance**: Git is the fundamental tool we use to save our work and manage the history of each project in this portfolio.

### GitHub
-   **Definition**: A web-based platform for hosting and collaborating on Git repositories.
-   **Context/Significance**: GitHub is the public "showroom" for this portfolio.

---

## I

### Isaac Sim
-   **Definition**: A photorealistic, physics-accurate robotics simulation platform developed by NVIDIA.
-   **Context/Significance**: Isaac Sim is our "digital twin" environment, allowing us to safely develop and test robotics algorithms before deploying them to physical hardware.

---

## J

### Jetson (Orin Nano)
-   **Definition**: A series of embedded computing boards from NVIDIA designed for edge AI applications.
-   **Context/Significance**: The Jetson is our "physical target" for "sim-to-real" projects, proving that our algorithms can run on a real, resource-constrained robotic brain.

### JetPack SDK
-   **Definition**: The software development kit for NVIDIA Jetson modules, bundling the Linux OS, drivers, and CUDA-X accelerated libraries.
-   **Context/Significance**: We used the JetPack SDK to flash the operating system and all necessary drivers onto our Jetson Orin Nano.

---

## O

### OmniGraph
-   **Definition**: The visual scripting framework within NVIDIA Omniverse and Isaac Sim. It allows for the creation of complex logic and data pipelines by connecting nodes in a graph.
-   **Context/Significance**: In Project 2.3, we used an OmniGraph to create a real-time pipeline that reads robot joint states and publishes them to a ROS 2 topic.

---

## R

### rclcpp
-   **Definition**: The standard C++ client library for ROS 2.
-   **Context/Significance**: We used `rclcpp` to write the high-performance publisher and subscriber nodes in the `cpp_pubsub` package.

### rclpy
-   **Definition**: The standard Python client library for ROS 2.
-   **Context/Significance**: We used `rclpy` to write the publisher and subscriber nodes in the `py_pubsub` package, ideal for rapid prototyping and high-level logic.

### ROS (ROS 2)
-   **Stands For**: Robot Operating System
-   **Definition**: A flexible framework for writing robot software.
-   **Context/Significance**: ROS is the central nervous system for all the projects in this portfolio.

---

## S

### Sim-to-Real
-   **Definition**: A robotics workflow where an algorithm is first trained and tested in simulation and then transferred to a physical robot.
-   **Context/Significance**: The success of this portfolio hinges on demonstrating a successful sim-to-real pipeline.

### SME
-   **Stands For**: Subject Matter Expert
-   **Definition**: An individual who exhibits the highest level of expertise in a specialized domain.
-   **Context/Significance**: The overarching goal of this entire portfolio is to build and demonstrate the skills of an SME in AI and Robotics.

---

## V

### VRAM
-   **Stands For**: Video Random Access Memory
-   **Definition**: The dedicated memory on a GPU used to store graphics and simulation data.
-   **Context/Significance**: VRAM is a critical resource for running Isaac Sim and training large AI models.