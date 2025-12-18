from abc import ABC, abstractmethod

class JSONSerializableMixin:
    """Section 7: Mixins - Providing specific functionality to any class."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class BaseService(ABC):
    """Section 4: Abstract Base Class defining a contract."""
    @abstractmethod
    def execute(self):
        pass

class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class AuthService(BaseService, LoggerMixin, JSONSerializableMixin):
    """
    Section 7: Multiple Inheritance.
    Python uses C3 Linearization for MRO.
    """
    def execute(self):
        self.log("Authenticating user...")
        # Business logic here
        return True

if __name__ == "__main__":
    auth = AuthService()
    auth.execute()
    # Check the Method Resolution Order
    print(f"MRO Order: {AuthService.mro()}")