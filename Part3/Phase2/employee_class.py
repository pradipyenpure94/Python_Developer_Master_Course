"""
Employee Class

Create an Employee class with:

    employee ID
    name
    salary

    Display employee information.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, employee_id: int, name: str, salary: float) -> None:
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display_employee_info(self) -> None:
        """Display employee information."""
        print("-" * 40)
        print("Employee information: ")
        print("-" * 40)
        print(f"\u25A0 Employee ID      : {self.employee_id}")
        print(f"\u25A0 Employee Name    : {self.name}")
        print(f"\u25A0 Employee Salary  : {self.salary:.2f}")
        print("-" * 40)


employee = Employee(employee_id=101, name="Pradip", salary=20000000)
employee.display_employee_info()
