import time
import subprocess


def run_benchmark(workload_name, iterations, command):
    print(f"\nRunning benchmark for {workload_name}")

    start_time = time.time()

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    end_time = time.time()

    return {
        "workload": workload_name,
        "iterations": iterations,
        "execution_time_sec": round(end_time - start_time, 2),
        "command": command,
        "output": result.stdout.strip(),
        "return_code": result.returncode
    }