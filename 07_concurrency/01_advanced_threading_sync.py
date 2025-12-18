import threading
import time
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

class SafeCounter:
    """Section 2: Using a Lock to prevent race conditions."""
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            # Only one thread can enter this block at a time
            current = self.value
            time.sleep(0.01)  # Simulate some work
            self.value = current + 1

def producer_consumer_demo():
    """Section 3: Using a thread-safe Queue for data sharing."""
    pipeline = Queue(maxsize=5)
    
    def producer():
        for i in range(5):
            print(f"Producing {i}")
            pipeline.put(i)
    
    def consumer():
        while not pipeline.empty():
            item = pipeline.get()
            print(f"Consuming {item}")
            pipeline.task_done()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer)
        executor.submit(consumer)

if __name__ == "__main__":
    counter = SafeCounter()
    # Running 10 threads to increment the counter
    threads = [threading.Thread(target=counter.increment) for _ in range(10)]
    for t in threads: t.start()
    for t in threads: t.join()
    
    print(f"Final Counter Value: {counter.value}")
    producer_consumer_demo()