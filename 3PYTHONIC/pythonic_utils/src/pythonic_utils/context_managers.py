import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Tiempo de ejecución: {end - start:.4f} segundos")