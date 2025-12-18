from functools import wraps
from typing import Callable

def repeat(times: int):
    """
    Advanced: A decorator factory that takes arguments.
    It requires three levels of nested functions.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name: str):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Python Expert")