import time
import subprocess

from utils.logger import logger


def run_benchmark(workload_name, iterations, command):
    logger.info(f"Starting workload: {workload_name}")

    print(f"\nRunning benchmark for {workload_name}")

    start_time = time.time()

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    end_time = time.time()

    execution_time = round(end_time - start_time, 2)

    logger.info(
        f"Completed workload: {workload_name} | Execution Time: {execution_time} sec"
    )

    return {
        "workload": workload_name,
        "iterations": iterations,
        "execution_time_sec": execution_time,
        "command": command,
        "output": result.stdout.strip(),
        "return_code": result.returncode
    }