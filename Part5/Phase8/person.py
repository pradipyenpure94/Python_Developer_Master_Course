"""Create Person ---> Employee ---> Manager."""


class Person:
    """Represent a person."""

    def work(self) -> None:
        """Display the person working status."""
        print("He is waiting for work.")


class Employee(Person):
    """Represent an employee."""

    def code(self) -> None:
        """Perform coding work."""
        print("He is enjoying coding.")


class Manager(Employee):
    """Represent a manager."""

    def team_manage(self) -> None:
        """Manage the team."""
        print("He manages the team well.")


def main() -> None:
    """Run the main program."""
    mgr = Manager()
    mgr.work()
    mgr.code()
    mgr.team_manage()


if __name__ == "__main__":
    main()
