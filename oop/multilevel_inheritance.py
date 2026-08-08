"""Multilevel inheritance."""


class Employee:
    """Represent an employee."""
    def __init__(self, emp_name: str) -> None:
        self.emp_name = emp_name

    def display_employee_information(self) -> None:
        """Display the employee information."""
        print(f"Employee Name         : {self.emp_name}")


class Developer(Employee):
    """Represent a developer."""
    def __init__(self, emp_name: str, designation: str) -> None:
        super().__init__(emp_name)
        self.designation = designation

    def display_developer_information(self) -> None:
        """Display the Developer information."""
        self.display_employee_information()
        print(f"Employee Designation  : {self.designation}")


class Manager(Developer):
    """Represent a manager."""
    def __init__(
        self,
        emp_name: str,
        designation: str,
        department_name: str
    ) -> None:
        super().__init__(emp_name, designation)
        self.department_name = department_name

    def display_manager_information(self) -> None:
        """Display the manager information."""
        print("-" * 40)
        print("Manager Information:")
        print("-" * 40)
        self.display_developer_information()
        print(f"Department Name       : {self.department_name}")


def main() -> None:
    """Run the main program."""
    manager_obj = Manager(
        emp_name="Pradip",
        designation="Python Developer",
        department_name="R & D"
    )
    manager_obj.display_manager_information()


if __name__ == "__main__":
    main()
