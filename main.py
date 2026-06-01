print("AI/ML Benchmark Framework Initialized")
import yaml

from benchmarks.runner import run_benchmark
from telemetry.collector import collect_system_metrics
from reports.generate_report import save_report


with open("configs/workloads.yaml", "r") as f:
    config = yaml.safe_load(f)

all_results = []

for workload in config["workloads"]:
    benchmark_result = run_benchmark(
        workload["name"],
        workload["iterations"]
    )

    telemetry = collect_system_metrics()

    all_results.append({
        "benchmark": benchmark_result,
        "telemetry": telemetry
    })

save_report(all_results)