import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from benchmarks.runner import run_benchmark


def test_run_benchmark():

    result = run_benchmark(
        "test-workload",
        1,
        "echo Test"
    )

    assert result["return_code"] == 0
    assert result["workload"] == "test-workload"