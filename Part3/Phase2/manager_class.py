"""
Employee → Manager

Create:

    Employee
    ↓
    Manager

Manager should inherit employee information and add:
    - department
    - team_size
"""


class Employee:
    """Represent an employee."""
    def __init__(self, name: str) -> None:
        self.name = name


class Manager(Employee):
    """Represent a manager."""
    def __init__(self, name: str, department: str, team_size: int) -> None:
        super().__init__(name=name)
        self.department = department
        self.team_size = team_size

    def display_manager_info(self) -> None:
        """Display manager information."""
        print("-" * 40)
        print("Manager Information:")
        print("-" * 40)
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Team Size   : {self.team_size}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    manager_info = Manager(name="Pradip", department="R & D", team_size=5)
    manager_info.display_manager_info()


if __name__ == "__main__":
    main()
