import asyncio
import time

async def fetch_data(id: int, delay: int) -> dict:
    print(f"Task {id}: Fetching data...")
    await asyncio.sleep(delay)  # Simulates I/O (API call)
    return {"id": id, "data": f"Result {id}"}

async def main():
    start_time = time.perf_counter()

    # asyncio.gather runs tasks concurrently
    print("Starting concurrent tasks...")
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 1)
    )

    end_time = time.perf_counter()
    print(f"Results: {results}")
    print(f"Total time: {end_time - start_time:.2f}s (should be ~2s, not 4s)")

if __name__ == "__main__":
    asyncio.run(main())