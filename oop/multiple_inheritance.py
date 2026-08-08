"""Multiple inheritance."""


class Employee:
    """Represent an employee class."""
    def __init__(self, emp_name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.emp_name = emp_name

    def display_employee_information(self) -> None:
        """Display employee information."""
        print(f"Employee Name     : {self.emp_name}")


class Trainer:
    """Represent a trainer class."""
    def __init__(self, course_name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.course_name = course_name

    def display_trainer_information(self) -> None:
        """Display trainer information."""
        print(f"Course Name       : {self.course_name}")


class Manager(Employee, Trainer):
    """Represent a manager."""
    def __init__(
        self,
        emp_name: str,
        course_name: str,
        department_name: str
    ) -> None:
        super().__init__(emp_name=emp_name, course_name=course_name)
        self.department_name = department_name

    def display_manager_information(self) -> None:
        """Display manager information."""
        print("-" * 40)
        print("Manager Information:")
        print("-" * 40)
        self.display_employee_information()
        self.display_trainer_information()
        print(f"Department Name   : {self.department_name}")


def main() -> None:
    """Run the main program."""
    manager_obj = Manager(
        emp_name="Pradip Yenpure",
        course_name="Python Developer",
        department_name="R & D"
    )
    manager_obj.display_manager_information()


if __name__ == "__main__":
    main()
