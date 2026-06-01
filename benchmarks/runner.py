import time


def run_benchmark(workload_name, iterations):
    print(f"Running benchmark for {workload_name}")

    start_time = time.time()

    for i in range(iterations):
        print(f"Iteration {i+1}/{iterations}")
        time.sleep(1)

    end_time = time.time()

    return {
        "workload": workload_name,
        "iterations": iterations,
        "execution_time_sec": round(end_time - start_time, 2),
    }