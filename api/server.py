from fastapi import FastAPI
import yaml
import json
from pathlib import Path

from benchmarks.runner import run_benchmark
from telemetry.collector import collect_system_metrics
from reports.generate_report import save_report
from reports.generate_csv_report import save_csv_report

app = FastAPI(
    title="AI/ML Benchmark Framework",
    version="0.1"
)


@app.get("/")
def root():
    return {
        "message": "AI/ML Benchmark Framework API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/workloads")
def get_workloads():

    with open("configs/workloads.yaml", "r") as f:
        config = yaml.safe_load(f)

    return config["workloads"]


@app.get("/reports")
def get_reports():

    report_file = Path("reports/benchmark_report.json")

    if not report_file.exists():
        return {
            "message": "No report found"
        }

    with open(report_file, "r") as f:
        data = json.load(f)

    return data


@app.post("/benchmark/run")
def run_benchmarks():

    with open("configs/workloads.yaml", "r") as f:
        config = yaml.safe_load(f)

    all_results = []

    for workload in config["workloads"]:

        benchmark_result = run_benchmark(
            workload["name"],
            workload["iterations"],
            workload["command"]
        )

        telemetry = collect_system_metrics()

        all_results.append({
            "benchmark": benchmark_result,
            "telemetry": telemetry
        })

    save_report(
        all_results,
        "reports/benchmark_report.json"
    )

    save_csv_report(
    all_results,
    "reports/benchmark_report.csv"
    )

    total_execution_time = sum(
        result["benchmark"]["execution_time_sec"]
        for result in all_results
    )

    return {
        "status": "completed",
        "workloads_executed": len(all_results),
        "total_execution_time_sec": round(total_execution_time, 2),
        "report_json": "reports/benchmark_report.json",
        "report_csv": "reports/benchmark_report.csv",
        "log_file": "logs/benchmark.log"
    }