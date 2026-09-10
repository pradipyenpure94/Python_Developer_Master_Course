"""Demonstrate multiple inheritance."""


class Manager:
    """Represent a manager."""

    def team_manage(self) -> None:
        """Manage the team."""
        print("Team management.")


class Developer:
    """Represent a developer."""

    def write_code(self) -> None:
        """Perform programming work."""
        print("Coding specific programming language.")


class TeamLead:
    """Represent a team lead."""

    def manage_team(self) -> None:
        """Assign work to the team."""
        print("Work distribution.")


class Employee(Manager, Developer, TeamLead):
    """Represent an employee."""

    def __init__(self, name: str) -> None:
        self.name = name

    def show_name(self) -> None:
        """Display the employee name."""
        print(f"Employee Name: {self.name}")


def main() -> None:
    """Run the main program."""
    employee = Employee(name="Pradip")
    employee.show_name()
    employee.team_manage()
    employee.write_code()
    employee.manage_team()


if __name__ == "__main__":
    main()
