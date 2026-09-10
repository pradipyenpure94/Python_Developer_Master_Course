"""Demonstrate the hybrid inheritance."""


class Person:
    """Represent a person."""

    def __init__(self, person_name: str) -> None:
        self.person_name = person_name

    def show_person_name(self) -> None:
        """Display person name."""
        print(f"Person Name         : {self.person_name}")


class Employee(Person):
    """Represent an employee."""

    def __init__(self, person_name: str, emp_name: str) -> None:
        super().__init__(person_name)
        self.emp_name = emp_name

    def show_employee_name(self) -> None:
        """Display employee name."""
        print(f"Employee Name       : {self.emp_name}")


class Developer:
    """Represent a developer."""

    def __init__(self, position: str) -> None:
        self.position = position

    def show_designation(self) -> None:
        """Display employee designation."""
        print(f"Employee Designation: {self.position}")


class Manager(Employee, Developer):
    """Represent a manager."""

    def __init__(
        self,
        person_name: str,
        emp_name: str,
        position: str,
        project_name: str
    ) -> None:
        super().__init__(person_name, emp_name)
        Developer.__init__(self, position)
        self.project_name = project_name

    def show_project_name(self) -> None:
        """Display project name."""
        print(f"Project             : {self.project_name}")


def main() -> None:
    """Run the main program."""
    mgr = Manager(
        person_name="Pradip",
        emp_name="P.R.Y",
        position="Sr. Python Developer",
        project_name="Aquent"
    )
    mgr.show_person_name()
    mgr.show_employee_name()
    mgr.show_designation()
    mgr.show_project_name()


if __name__ == "__main__":
    main()
