import csv
import os


def save_csv_report(results, filename):

    os.makedirs("reports", exist_ok=True)

    with open(filename, "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "workload",
            "execution_time_sec",
            "cpu_percent",
            "memory_percent"
        ])

        for result in results:

            writer.writerow([
                result["benchmark"]["workload"],
                result["benchmark"]["execution_time_sec"],
                result["telemetry"]["cpu_percent"],
                result["telemetry"]["memory_percent"]
            ])

    print(f"CSV report saved: {filename}")