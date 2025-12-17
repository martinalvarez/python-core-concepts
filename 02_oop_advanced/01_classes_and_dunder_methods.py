class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        # Encapsulation: leading underscore indicates 'protected'
        self._price = price 

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __str__(self) -> str:
        return f"Product: {self.name}"

    def __repr__(self) -> str:
        """Official string representation for debugging."""
        return f"Product(name='{self.name}', price={self._price})"

# Demo
p = Product("Laptop", 1200.0)
print(f"User view: {p}")
print(f"Dev view: {repr(p)}")