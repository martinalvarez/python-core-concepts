class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_role(self) -> str:
        return "General Employee"

class Developer(Employee):
    def __init__(self, name: str, salary: float, language: str):
        # Call the parent constructor
        super().__init__(name, salary)
        self.language = language

    def get_role(self) -> str:
        # Overriding parent method
        return f"Developer specialized in {self.language}"

# Polymorphism in action
staff = [Employee("Alice", 50000), Developer("Bob", 70000, "Python")]
for person in staff:
    print(f"{person.name}: {person.get_role()}")