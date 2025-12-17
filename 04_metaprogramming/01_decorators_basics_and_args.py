from functools import wraps
import time
from typing import Callable, Any

def execution_timer(func: Callable) -> Callable:
    """Decorator that measures execution time of a function."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__!r} took {end_time - start_time:.4f}s")
        return result
    return wrapper

@execution_timer
def complex_operation(n: int) -> list[int]:
    """Simulates a heavy computation."""
    return [i**2 for i in range(n)]

if __name__ == "__main__":
    complex_operation(1000000)
    print(f"Metadata preserved: {complex_operation.__name__}") # Thanks to @wraps