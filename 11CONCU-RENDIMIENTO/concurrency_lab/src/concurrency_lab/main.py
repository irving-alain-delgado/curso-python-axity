import asyncio
from concurrency_lab.sync_fetcher import fetch_urls
from concurrency_lab.async_fetcher import fetch_urls_async
from concurrency_lab.cpu_task import run_cpu_task


URLS = ["https://httpbin.org/delay/1"] * 10


def main():
    print("Running sync...")
    fetch_urls(URLS)

    print("Running async...")
    asyncio.run(fetch_urls_async(URLS))

    print("Running CPU-bound...")
    run_cpu_task()


if __name__ == "__main__":
    main()