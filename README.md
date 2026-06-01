# AI/ML Benchmark Framework

Cloud-native benchmarking framework for evaluating AI/ML workloads across distributed environments.

## Overview

This project provides a modular and extensible framework for benchmarking AI/ML workloads, collecting system telemetry, and generating structured performance reports.

The framework is designed to support LLM workloads, vision models, benchmarking suites, and distributed execution environments.

## Features

- Configuration-driven workload execution
- Benchmark execution framework
- System telemetry collection
- JSON report generation
- Modular workload architecture
- Docker and Kubernetes ready
- Extensible API-driven design
- Distributed execution support

## Supported Workloads

- Llama 3.1
- Phi-3 Mini
- Stable Diffusion
- Procyon
- PugetBench

## Current Capabilities

### Benchmark Runner

- Executes workloads defined in YAML configuration files
- Tracks execution duration
- Supports configurable iterations

### Telemetry Collection

- CPU utilization monitoring
- Memory utilization monitoring
- Available system memory tracking

### Reporting

- Generates structured JSON benchmark reports
- Stores benchmark and telemetry results

## Project Structure

```text
ai-ml-benchmark-framework/
│
├── benchmarks/
│   └── runner.py
│
├── telemetry/
│   └── collector.py
│
├── reports/
│   └── generate_report.py
│
├── configs/
│   └── workloads.yaml
│
├── api/
├── dashboards/
├── docker/
├── kubernetes/
├── scripts/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

## Tech Stack

- Python
- FastAPI
- Docker
- Kubernetes
- OpenVINO
- Prometheus
- Grafana

## Sample Output

```json
{
  "workload": "llama-3.1-8b",
  "iterations": 5,
  "execution_time_sec": 5.0
}
```

## Roadmap

- FastAPI service layer
- REST API endpoints
- CSV report generation
- Dashboard integration
- Docker deployment
- Kubernetes deployment
- Real workload execution
- Distributed benchmark orchestration

## Status

Current Version: v0.1

Completed:
- Project structure setup
- Benchmark runner implementation
- Telemetry collector implementation
- JSON report generation
- YAML-based workload configuration

In Progress:
- FastAPI backend service
- Benchmark execution APIs
- Report management APIs