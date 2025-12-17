from typing import Union, Optional, Protocol, List

# Type Alias for readability
Vector = List[float]

# Protocol: Structural subtyping (Modern Python 3.8+)
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str: return "Drawing a circle"

class Square:
    def draw(self) -> str: return "Drawing a square"

def render(shape: Drawable) -> None:
    print(shape.draw())

def process_id(user_id: Union[int, str]) -> str:
    # Union handles multiple possible types
    return f"Processing ID: {user_id}"

def get_config(key: str) -> Optional[str]:
    # Optional[str] is shorthand for Union[str, None]
    return "Value" if key == "valid" else None

if __name__ == "__main__":
    render(Circle())
    print(process_id(101))
    print(get_config("invalid"))