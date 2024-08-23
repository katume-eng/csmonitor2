import time
import httpx
import asyncio
import requests

times_of_requests = [10, 20, 50, 100, 200, 500]
test_site_url = 'http://localhost:8003/test_site/'

async def test_async(request):
    async with httpx.AsyncClient() as client:
        for n in times_of_requests:
            start_time = time.time()
            tasks = [client.get(test_site_url) for _ in range(n)]
            responses = await asyncio.gather(*tasks)
            end_time = time.time()
            print(f"Total time for {n} async requests: {end_time - start_time:.2f} seconds")

def test_sync(request):
    result = []
    for n in times_of_requests:
        responses = []
        start_time = time.time()
        for _ in range(n):
            responses.append(requests.get(test_site_url))
        end_time = time.time()
        result.append(end_time - start_time)
        print("patch end")
        time.sleep(0.5)
    print(result)

def test_site(request):
    return
