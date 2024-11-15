import asyncio
import time

async def fetch_data(url):
    print(f"Start fetching {url}")
    await asyncio.sleep(2)
    print (f"finished fetching {url}")
    return f"Data from {url}"

async def main():
    urls= ["http://example.com/page1","http://example.com/page2", "http://example.com/page3"]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print("Results:", results)

asyncio.run(main())