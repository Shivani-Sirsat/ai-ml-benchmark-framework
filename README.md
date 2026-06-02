# AI/ML Benchmark Framework

Cloud-native benchmarking framework for orchestrating AI/ML workloads, collecting telemetry, and generating benchmark reports through a modular and extensible architecture.

---

## Overview

The AI/ML Benchmark Framework provides a configurable platform for executing benchmark workloads, collecting system telemetry, and exposing results through REST APIs.

The framework is designed to support AI/ML benchmarking scenarios including:

* Large Language Models (LLMs)
* Generative AI workloads
* Computer Vision workloads
* OpenVINO-based benchmarks
* Industry-standard benchmark suites

The current implementation demonstrates benchmark orchestration using lightweight workload modules while maintaining compatibility with real benchmark execution workflows.

---

## Key Features

* FastAPI-based REST APIs
* YAML-driven workload configuration
* Workload abstraction layer
* Command execution framework
* CPU and memory telemetry collection
* JSON report generation
* Modular architecture
* Docker-ready design
* Kubernetes-ready architecture

---

## Supported Workloads

### Current Repository Implementation

The repository includes lightweight workload modules that simulate benchmark execution and demonstrate the framework architecture.

Implemented workload modules:

* Llama 3.1 Benchmark
* Phi-3 Mini Benchmark
* Stable Diffusion Benchmark
* PugetBench Benchmark
* Procyon Benchmark

### Real Benchmark Integration

The framework architecture is designed to support execution of real AI/ML benchmark workloads.

The design is inspired by real-world benchmarking workflows involving:

* OpenVINO LLM Benchmark Tool
* Llama 3.1 Inference Benchmarking
* Phi-3 Mini Inference Benchmarking
* GPU-based AI/ML Benchmark Execution
* Telemetry Collection and Report Generation

The current repository uses lightweight workload modules to demonstrate benchmark orchestration, workload execution, telemetry collection, and reporting.

Workload modules can be replaced with:

* OpenVINO benchmark commands
* Model inference pipelines
* Docker-based benchmark workloads
* Kubernetes Jobs
* Custom benchmark scripts

without modifying the framework architecture.

---

## Architecture

```text
                    +------------------+
                    |   FastAPI API    |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Benchmark Runner |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    | Workload Modules |
                    +--------+---------+
                             |
           +----------------+----------------+
           |                                 |
           v                                 v
+------------------+             +------------------+
| Telemetry Layer  |             | Command Executor |
+------------------+             +------------------+
           |                                 |
           +----------------+----------------+
                            |
                            v
                  +----------------------+
                  | Report Generation    |
                  +----------------------+
```

---

## Design Philosophy

This project focuses on benchmark orchestration rather than model implementation.

The framework separates:

* API Layer
* Benchmark Execution Layer
* Workload Abstraction Layer
* Telemetry Collection Layer
* Reporting Layer

This enables benchmark workloads to be swapped independently of the framework.

Examples include:

* Placeholder benchmark modules
* OpenVINO benchmark workloads
* LLM inference workloads
* Docker-based benchmark containers
* Kubernetes batch jobs

---

## Project Structure

```text
ai-ml-benchmark-framework/
│
├── api/
├── benchmarks/
├── configs/
├── dashboards/
├── docker/
├── docs/
├── kubernetes/
├── reports/
├── scripts/
├── telemetry/
├── tests/
├── utils/
├── workloads/
│
├── requirements.txt
├── main.py
└── README.md
```

---

## Workload Execution Flow

```text
workloads.yaml
        |
        v
FastAPI Endpoint
        |
        v
Benchmark Runner
        |
        v
Workload Module
        |
        v
Command Execution
        |
        v
Telemetry Collection
        |
        v
Report Generation
```

---

## Available API Endpoints

### Health Check

```http
GET /health
```

Returns application health status.

### Workloads

```http
GET /workloads
```

Returns configured benchmark workloads.

### Reports

```http
GET /reports
```

Returns benchmark execution reports.

### Run Benchmarks

```http
POST /benchmark/run
```

Triggers benchmark execution and report generation.

---

## Example Benchmark Output

```json
{
  "benchmark": {
    "workload": "phi3-mini",
    "execution_time_sec": 3.12,
    "command": "python workloads/phi3_workload.py",
    "output": "Loading model...\nInitializing tokenizer...\nRunning inference...\nAverage latency: 35 ms\nThroughput: 28 tokens/sec",
    "return_code": 0
  }
}
```

---

## Technology Stack

* Python
* FastAPI
* YAML
* REST APIs
* JSON Reporting
* Telemetry Collection
* OpenVINO Integration Ready
* Docker (Planned)
* Kubernetes (Planned)

---

## Current Status

### Completed

* Project Setup
* Benchmark Runner
* Telemetry Collector
* JSON Report Generator
* FastAPI Backend
* YAML Configuration Management
* Command Execution Framework
* Workload Abstraction Layer
* Placeholder Benchmark Workloads

### In Progress

* Logging Framework
* CSV Report Generation

### Planned

* Docker Support
* Kubernetes Deployment
* Automated Testing
* Dashboard Visualization
* Prometheus Metrics
* Grafana Integration

---

## Future Enhancements

* OpenVINO LLM Benchmark Integration
* Llama 3.1 Real Workload Execution
* Phi-3 Mini Real Workload Execution
* GPU/NPU Benchmark Support
* Docker-based Benchmark Execution
* Kubernetes Job Scheduling
* Prometheus Metrics Export
* Grafana Dashboard Integration
* Distributed Benchmark Execution

---

## License

MIT License
