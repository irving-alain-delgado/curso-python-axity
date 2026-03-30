import asyncio
import httpx
import time


async def fetch_one(client: httpx.AsyncClient, url: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        response = await client.get(url)
        response.raise_for_status()


async def fetch_urls_async(urls: list[str], limit: int = 5):
    start = time.perf_counter()

    semaphore = asyncio.Semaphore(limit)

    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_one(client, url, semaphore)
            for url in urls
        ]
        await asyncio.gather(*tasks)

    end = time.perf_counter()
    print(f"Async time: {end - start:.2f}s")