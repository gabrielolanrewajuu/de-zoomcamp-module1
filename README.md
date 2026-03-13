Data Pipeline: From Local Script to Portable Container

This project demonstrates the transition of a Python data pipeline from a local, hardware-dependent environment to a fully containerized Docker solution, ensuring 100% reproducibility across any machine.

(Setting the Scene)
Before diving into infrastructure, we need a baseline. This project uses Python 3.13 and Pandas to process monthly data.

Environment: VS Code on macOS (M4 Apple Silicon).

Language: Python.

The Goal: Build a pipeline that takes a month argument and spits out a processed .parquet file.

The Problem 
Running code locally is "brittle." If I send you my script, it might fail because you have the wrong version of Pandas or a different OS.

In Data Engineering, "it works on my machine" is a failure. Manually installing dependencies (pip install ...) leads to "Version Drift," where the pipeline eventually breaks as libraries update.

Solution: Docker (The Portable Workshop)
Think of Docker not just as a virtual machine, but as a Construction Company for your code.

What: It builds an isolated, "Slim" Linux workshop (a Container) inside your computer.

Why: 
1. Safety: It keeps your main Mac OS clean (no global pip installs).
2. Reproducibility: It freezes the exact versions of the "tools" (Python, Pandas, PyArrow) inside the workshop so the code runs the same in 2026 as it does today.

The "How" (The Technical Roadmap)
To get this running, we follow a three-step workflow:

Step A: The Blueprint (Dockerfile)
We don't just "install" things manually. We write a Dockerfile—a recipe that tells Docker how to build the room.

We use the python:3.13.11-slim image for speed.

We use uv (a high-performance package manager) to lock our dependencies.

Step B: The Build (Baking the Image)
We turn the blueprint into a frozen image.

Bash
docker build -t cosmic-pipeline:v1 .

Step C: The Execution (Running the Container)
We walk into the workshop and run the pipeline for a specific month (e.g., Month 12).

Bash
docker run -it --rm cosmic-pipeline:v1 12


Data Persistence Problem; Using 'Volumes' to establish stateless data