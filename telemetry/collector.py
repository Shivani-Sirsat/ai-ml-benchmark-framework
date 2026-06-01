import psutil


def collect_system_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "available_memory_gb": round(
            psutil.virtual_memory().available / (1024**3), 2
        ),
    }