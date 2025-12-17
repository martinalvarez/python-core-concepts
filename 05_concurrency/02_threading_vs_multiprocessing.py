import threading
import multiprocessing
import time

def cpu_intensive_task(n: int):
    """A task that consumes CPU cycles."""
    count = 0
    for i in range(n):
        count += i
    return count

if __name__ == "__main__":
    number = 10_000_000
    
    # 1. Multiprocessing (Better for CPU Bound)
    # Uses different CPU cores, bypassing the GIL
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=cpu_intensive_task, args=(number,))
    p2 = multiprocessing.Process(target=cpu_intensive_task, args=(number,))
    
    p1.start(); p2.start()
    p1.join(); p2.join()
    print(f"Multiprocessing time: {time.perf_counter() - start:.2f}s")

    # 2. Threading (Not efficient for CPU Bound in Python)
    # Still limited by the GIL
    start = time.perf_counter()
    t1 = threading.Thread(target=cpu_intensive_task, args=(number,))
    t2 = threading.Thread(target=cpu_intensive_task, args=(number,))
    
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"Threading time: {time.perf_counter() - start:.2f}s")