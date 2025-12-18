class NonNegativeDescriptor:
    """
    Section 8: Descriptors - Reusable attribute logic.
    Used internally by @property and static methods.
    """
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} cannot be negative")
        instance.__dict__[self.name] = value

class SingletonMeta(type):
    """
    Section 9: Metaclass - Controlling class creation.
    Ensures only one instance of a class exists.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    port = NonNegativeDescriptor("port") # Using the descriptor

    def __init__(self, port):
        self.port = port

if __name__ == "__main__":
    db1 = DatabaseConnection(5432)
    db2 = DatabaseConnection(8080)
    print(f"Is same instance? {db1 is db2}") # True due to Metaclass