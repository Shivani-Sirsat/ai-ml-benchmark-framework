# AI/ML Benchmark Framework

A modular benchmarking framework for orchestrating AI/ML workloads, collecting system telemetry, and generating benchmark reports through REST APIs.

## Overview

This project demonstrates the design and implementation of a benchmark orchestration platform that can execute AI/ML workloads, collect resource utilization metrics, and generate execution reports.

The framework is designed to support benchmarking scenarios such as:

* Large Language Models (LLMs)
* Generative AI workloads
* Computer Vision workloads
* OpenVINO-based benchmarks
* Custom benchmarking workflows

---

## Features

* FastAPI-based REST APIs
* YAML-driven workload configuration
* Workload abstraction layer
* Command execution framework
* CPU and memory telemetry collection
* JSON report generation
* CSV report generation
* Logging framework
* Automated testing with Pytest
* Extensible architecture

---

## Supported Workloads

Current implementation includes placeholder workloads for:

* Llama 3.1
* Phi-3 Mini
* Stable Diffusion
* PugetBench
* Procyon

The framework can be extended to run real benchmark workloads by replacing the workload commands in the configuration file. And can be added more workloads.

---

## Architecture

```text
FastAPI API
     |
     v
Benchmark Runner
     |
     v
Workload Modules
     |
     +----> Command Execution
     |
     +----> Telemetry Collection
     |
     v
Report Generation
```

---

## Project Structure

```text
ai-ml-benchmark-framework/
│
├── api/
├── benchmarks/
├── configs/
├── reports/
├── telemetry/
├── tests/
├── utils/
├── workloads/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Returns application health status.

### Workloads

```http
GET /workloads
```

Returns configured workloads.

### Reports

```http
GET /reports
```

Returns generated benchmark reports.

### Run Benchmarks

```http
POST /benchmark/run
```

Executes configured workloads and generates reports.

---

## Example Output

```json
{
  "workload": "phi3-mini",
  "execution_time_sec": 3.12,
  "cpu_percent": 24.5,
  "memory_percent": 82.1
}
```

---

## Testing

Run tests using:

```bash
pytest -v
```

Current test coverage includes:

* Benchmark runner validation
* API health endpoint validation

---

## Technology Stack

* Python
* FastAPI
* Pytest
* YAML
* REST APIs
* JSON & CSV Reporting
* Telemetry Collection


---

## License

MIT License
