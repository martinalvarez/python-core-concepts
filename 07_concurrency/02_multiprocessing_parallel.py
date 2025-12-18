import multiprocessing
import time
import math

def heavy_computation(n: int) -> int:
    """CPU Bound task: Calculating factorials."""
    return math.factorial(n)

def run_parallel_processing():
    """Section 4: Utilizing all CPU cores with ProcessPoolExecutor."""
    numbers = [50000, 50001, 50002, 50003]
    
    start_time = time.perf_counter()
    
    # Pool will create one process per CPU core by default
    with multiprocessing.Pool() as pool:
        results = pool.map(heavy_computation, numbers)
    
    end_time = time.perf_counter()
    print(f"Multiprocessing results calculated in {end_time - start_time:.4f}s")

if __name__ == "__main__":
    # Multiprocessing in Windows/macOS requires the __main__ guard
    run_parallel_processing()