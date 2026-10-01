"""Design and develop class."""


class Employee:
    """Represent an employee."""
    company_name = "IBM"

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def display(self) -> None:
        """Display employee information."""
        print(f"Employee Name   : {self.name}")
        print(f"Employee Salary : {self.salary:.2f}")
