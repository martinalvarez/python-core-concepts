from contextlib import contextmanager

class ResourceManager:
    """Classic Context Manager using class protocol."""
    def __enter__(self):
        print("Connecting to resource...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection safely.")
        if exc_type:
            print(f"Handled error: {exc_val}")
        return True # Suppresses exception for demo purposes

@contextmanager
def simple_resource():
    """Context Manager using a generator (simpler for many cases)."""
    print("Open Resource")
    try:
        yield "DATA_STREAM"
    finally:
        print("Close Resource")

if __name__ == "__main__":
    with ResourceManager() as rm:
        print("Processing...")
    
    with simple_resource() as data:
        print(f"Using: {data}")