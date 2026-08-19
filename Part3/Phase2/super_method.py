"""
super() — Multilevel

Create:

    Person
    ↓
    Employee
    ↓
    Manager

Use super() at each level.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    """Represent an employee."""

    def __init__(self, name: str, employee_id: int) -> None:
        super().__init__(name=name)
        self.employee_id = employee_id


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, name: str, employee_id: int, department: str) -> None:
        super().__init__(name=name, employee_id=employee_id)
        self.department = department

    def display_manager_info(self) -> None:
        """Display manager information."""
        print("-" * 40)
        print("Manager Information: ")
        print("-" * 40)
        print(f"Employee ID  : {self.employee_id}")
        print(f"Name         : {self.name}")
        print(f"Department   : {self.department}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    manager = Manager(name="Pradip", employee_id=101, department="Development")
    manager.display_manager_info()


if __name__ == "__main__":
    main()
