from dataclasses import dataclass
from enum import Enum, auto, unique
from sys import getsizeof

@unique
class UserRole(Enum):
    """Section 5: Using Enums for type safety and uniqueness."""
    ADMIN = auto()
    EDITOR = auto()
    GUEST = auto()

@dataclass(frozen=True, slots=True)
class User:
    """
    Section 4 & 9: Modern Object.
    - slots=True: Extreme memory efficiency (no __dict__).
    - frozen=True: Implements __hash__ and __eq__ automatically (Immutable).
    """
    id: int
    username: str
    role: UserRole

def compare_memory():
    class LegacyUser:
        def __init__(self, id, username):
            self.id = id
            self.username = username

    legacy = LegacyUser(1, "old_school")
    modern = User(1, "pythonic", UserRole.ADMIN)
    
    # Legacy uses a __dict__ (heavy), Modern uses __slots__ (light)
    print(f"Legacy Size: {getsizeof(legacy.__dict__)} bytes")
    try:
        print(modern.__dict__)
    except AttributeError:
        print("Modern User has no __dict__, it's memory-optimized via __slots__")

if __name__ == "__main__":
    compare_memory()