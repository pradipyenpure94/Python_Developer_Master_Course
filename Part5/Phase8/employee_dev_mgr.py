"""Demonstrate multilevel inheritance."""


class Employee:
    """Represent an employee."""

    def work(self) -> str:
        """Perform employee-specific work."""
        return "Working..."


class Developer(Employee):
    """Represent a developer."""

    def code(self) -> str:
        """Perform programming-specific work."""
        return "Coding..."


class Manager(Developer):
    """Represent a manager."""

    def manage_team(self) -> str:
        """Manage team handling specific work."""
        return "Team handling..."


def main() -> None:
    """Run the main program."""
    mgr = Manager()
    print(mgr.work())
    print(mgr.code())
    print(mgr.manage_team())


if __name__ == "__main__":
    main()
