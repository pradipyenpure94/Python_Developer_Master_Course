"""Demonstrate hierarchical inheritance."""


class Employee:
    """Represent an employee."""

    def __init__(self, name: str) -> None:
        self.name = name

    def show_name(self) -> None:
        """Display employee name."""
        print(f"Employee Name: {self.name}")


class Developer(Employee):
    """Represent a developer."""

    def __init__(self, name: str, position: str) -> None:
        super().__init__(name)
        self.position = position

    def show_position(self) -> None:
        """Display developer position."""
        print(f"Work Position: {self.position}")


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, name: str, position: str) -> None:
        super().__init__(name)
        self.position = position

    def show_position(self) -> None:
        """Display work position."""
        print(f"Work Position: {self.position}")


def main() -> None:
    """Run the main program."""
    mgr = Manager(name="Pradip", position="Senior Manager")
    mgr.show_name()
    mgr.show_position()

    dev = Developer(name="Ajay", position="QA")
    dev.show_name()
    dev.show_position()


if __name__ == "__main__":
    main()
