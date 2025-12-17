"""
Focus: Mutability, Sets for performance, and Comprehensions.
"""

def showcase_structures():
    # 1. List vs Tuple (Mutability)
    # Tuples are faster and memory-efficient (use for fixed data)
    coordinates: tuple[int, int] = (10, 20) 
    
    # 2. List Unpacking (Pro syntax)
    first, *middle, last = [1, 2, 3, 4, 5]
    print(f"First: {first}, Last: {last}, Middle: {middle}")

    # 3. Sets: High-performance uniqueness and logic
    admins = {"Alice", "Bob"}
    users = {"Bob", "Charlie", "David"}
    
    # Set operations (Intersection/Union)
    only_admins = admins & users # Intersection
    print(f"Active admins: {only_admins}")

    # 4. Comprehensions (Dict and List)
    # Cleanest way to transform data
    squares = {x: x**2 for x in range(5) if x % 2 == 0}
    print(f"Even squares dictionary: {squares}")

if __name__ == "__main__":
    showcase_structures()