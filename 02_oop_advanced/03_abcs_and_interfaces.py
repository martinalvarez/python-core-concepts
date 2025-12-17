from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Every shape MUST implement this method."""
        pass

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

# This would fail: s = Shape() -> Cannot instantiate abstract class
sq = Square(5)
print(f"Square area: {sq.area()}")