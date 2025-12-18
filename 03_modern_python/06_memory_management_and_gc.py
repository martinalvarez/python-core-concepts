import sys
import gc
import weakref

class LargeObject:
    def __del__(self):
        print("Object being destroyed from memory")

def memory_demo():
    obj = LargeObject()
    # 1. Reference Counting
    print(f"Reference count: {sys.getrefcount(obj)}") # obj + sys.getrefcount

    # 2. Weak References
    # Doesn't increase ref count, allows GC to collect the object
    proxy = weakref.ref(obj)
    print(f"Proxy refers to: {proxy()}")

    # 3. Manual GC (rarely needed, but good to know)
    del obj
    gc.collect() 
    print(f"Proxy after deletion: {proxy()}")

if __name__ == "__main__":
    memory_demo()