def make_multiplier(factor: int):
    """
    Section: Closures.
    The inner function 'multi' remembers 'factor' even after 
    'make_multiplier' has finished execution.
    """
    def multi(n: int) -> int:
        return n * factor
    return multi

def counter_closure():
    count = 0
    def increment():
        nonlocal count  # Essential to modify variable in enclosing scope
        count += 1
        return count
    return increment

if __name__ == "__main__":
    times3 = make_multiplier(3)
    print(f"Closure result: {times3(10)}")  # 30
    
    counter = counter_closure()
    print(f"Counter: {counter()}, {counter()}") # 1, 2