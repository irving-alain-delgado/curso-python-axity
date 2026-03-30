import httpx
import time


def fetch_urls(urls: list[str]) -> None:
    start = time.perf_counter()

    with httpx.Client() as client:
        for url in urls:
            response = client.get(url)
            response.raise_for_status()

    end = time.perf_counter()
    print(f"Sync time: {end - start:.2f}s")