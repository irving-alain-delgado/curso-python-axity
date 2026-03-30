import time
from concurrent.futures import ProcessPoolExecutor


def heavy_computation(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total


def run_cpu_task():
    numbers = [10_000_000] * 4

    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_computation, numbers))

    end = time.perf_counter()

    print(f"CPU parallel time: {end - start:.2f}s")