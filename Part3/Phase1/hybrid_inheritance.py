"""Employee hierarchy using multiple inheritance. (Hybrid)."""


class Employee:
    """Represent an employee."""

    def show_employee_info(self) -> None:
        """Show employee information."""
        print("Show employee information.")


class Developer(Employee):
    """Represent a developer."""

    def show_developer_info(self) -> None:
        """Show developer information."""
        print("Show developer information.")


class Manager(Employee):
    """Represent a manager."""

    def show_manager_info(self) -> None:
        """Show manager information."""
        print("Show manager information.")


class TeamLead(Manager, Developer):
    """Represent a team lead."""

    def show_team_lead_info(self) -> None:
        """Show team lead information."""
        print("Show team lead information.")


def main() -> None:
    """Run the main program."""
    team_lead_object = TeamLead()
    team_lead_object.show_employee_info()
    team_lead_object.show_developer_info()
    team_lead_object.show_manager_info()
    team_lead_object.show_team_lead_info()


if __name__ == "__main__":
    main()
