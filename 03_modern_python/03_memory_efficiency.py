import sys

def showcase_efficiency():
    # 1. List Comprehension (Stores everything in RAM)
    my_list = [x for x in range(10000)]
    
    # 2. Generator Expression (Lazy evaluation, memory efficient)
    my_gen = (x for x in range(10000))

    print(f"List size: {sys.getsizeof(my_list)} bytes")
    print(f"Generator size: {sys.getsizeof(my_gen)} bytes")

def data_streamer():
    """Demonstrates yield for memory-efficient data processing."""
    for i in range(5):
        yield f"Record_{i}"

if __name__ == "__main__":
    showcase_efficiency()
    for record in data_streamer():
        print(record)