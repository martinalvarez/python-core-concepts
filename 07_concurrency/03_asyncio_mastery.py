import asyncio
import time

async def fetch_api_data(id: int, duration: int):
    """A coroutine representing an I/O bound task."""
    print(f"Task {id}: Starting (will take {duration}s)")
    await asyncio.sleep(duration)
    return f"Data from {id}"

async def main():
    """Section 5: Task management, Timeouts and Gather."""
    
    # 1. Running with Timeout (Section: asyncio.wait_for)
    print("\n--- Timeout Example ---")
    task = asyncio.create_task(fetch_api_data(1, 10))
    try:
        # If it takes more than 2 seconds, cancel it
        result = await asyncio.wait_for(task, timeout=2.0)
    except asyncio.TimeoutError:
        print("Task 1 was too slow and was cancelled automatically!")

    # 2. Running Multiple Tasks Concurrently (Section: gather)
    print("\n--- Gather Example ---")
    start = time.perf_counter()
    results = await asyncio.gather(
        fetch_api_data(2, 1),
        fetch_api_data(3, 1),
        fetch_api_data(4, 1),
        return_exceptions=True # Pro tip: handle errors without crashing gather
    )
    
    end_time = time.perf_counter()
    print(f"Results: {results}")
    print(f"Async execution took: {end_time - start:.4f}s (All ran in parallel!)")

if __name__ == "__main__":
    asyncio.run(main())