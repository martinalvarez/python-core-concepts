from typing import Callable

"""
Focus: Dynamic arguments (*args/**kwargs) and Functional patterns.
"""

def complex_logger(message: str, *args, **kwargs) -> None:
    """
    Standard Docstring: Demonstrates flexible argument handling.
    """
    print(f"LOG: {message}")
    if args: print(f"Extra info: {args}")
    if kwargs: print(f"Metadata: {kwargs}")

def functional_demo():
    numbers = [1, 2, 3, 4, 5]
    
    # Lambda + Filter/Map (Standard functional Python)
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    doubled = list(map(lambda x: x * 2, evens))
    
    print(f"Original: {numbers} -> Filtered Evens: {evens} -> Doubled: {doubled}")

if __name__ == "__main__":
    complex_logger("System Start", "v1.0", user="Admin", debug=True)
    functional_demo()