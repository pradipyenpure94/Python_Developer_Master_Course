"""
Employee → Developer & Tester

Create:

    Employee
    /      \
    Developer   Tester

Each child should have its own method.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, name: str):
        self.name = name


class Developer(Employee):
    """Represent a developer."""

    def display_developer_info(self) -> None:
        """Display developer information."""
        print(f"{self.name} - Python Developer.")


class Tester(Employee):
    """Represent a tester."""

    def display_tester_info(self) -> None:
        """Display tester information."""
        print(f"{self.name} - Quality Assurance Engineer.")


def main() -> None:
    """Run the main program."""
    developer_obj = Developer(name="Pradip")
    developer_obj.display_developer_info()
    print()
    tester_obj = Tester(name="Ajay")
    tester_obj.display_tester_info()


if __name__ == "__main__":
    main()
