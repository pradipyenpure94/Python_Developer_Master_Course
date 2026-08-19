"""
super() — Employee → Manager

Use super() to call the parent constructor and
initialize common employee information.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, employee_id: int, name: str) -> None:
        self.employee_id = employee_id
        self.name = name


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, employee_id: int, name: str, department: str) -> None:
        super().__init__(employee_id=employee_id, name=name)
        self.department = department

    def display_manager_info(self) -> None:
        """Display manager information."""
        print("-" * 40)
        print("Manager Information: ")
        print("-" * 40)
        print(f"ID          : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    manager = Manager(employee_id=101, name="Pradip", department="R & D")
    manager.display_manager_info()


if __name__ == "__main__":
    main()
