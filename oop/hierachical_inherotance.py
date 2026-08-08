"""Hierarchical inheritance."""


class Employee:
    """Represent an employee."""
    def __init__(self, emp_name: str) -> None:
        self.emp_name = emp_name

    def display_employee_information(self) -> None:
        """Display employee information."""
        print(f"Employee Name: {self.emp_name}")


class Trainer(Employee):
    """Represent a trainer."""
    def __init__(self, emp_name: str, course_name: str) -> None:
        super().__init__(emp_name)
        self.course_name = course_name

    def display_trainer_information(self) -> None:
        """Display the trainer information."""
        self.display_employee_information()
        print(f"Course Name: {self.course_name}")


class Developer(Employee):
    """Represent a developer."""
    def __init__(self, emp_name: str, programming_language: str) -> None:
        super().__init__(emp_name)
        self.programming_language = programming_language

    def display_developer_information(self) -> None:
        """Display developer information."""
        self.display_employee_information()
        print(f"Programming Language: {self.programming_language}")


def main() -> None:
    """Run the main program."""
    trainer_obj = Trainer(emp_name="Pradip", course_name="Python Developer")
    trainer_obj.display_trainer_information()
    developer_obj = Developer(emp_name="Amit", programming_language="Python")
    developer_obj.display_developer_information()


if __name__ == "__main__":
    main()
