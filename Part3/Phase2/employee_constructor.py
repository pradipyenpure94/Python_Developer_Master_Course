"""
Alternative Constructor

Create an Employee class with:

from_string()

It should create an employee object from:

    101,Pradip,50000
"""


class Employee:
    """Represent an employee."""

    def __init__(self, employee_id: int, name: str, salary: float) -> None:
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, employee_data: str) -> "Employee":
        """Create an employee object from a comma separated string."""
        employee_id, name, salary = employee_data.split(",")
        return cls(
            employee_id=int(employee_id),
            name=name,
            salary=float(salary)
        )

    def display_employee_info(self) -> None:
        """Display Employee Information."""
        print("Employee Information:")
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : {self.salary:.2f}")


def main() -> None:
    """Run the main program."""
    employee_data = "101,Pradip,50000"

    employee = Employee.from_string(employee_data)
    employee.display_employee_info()


if __name__ == "__main__":
    main()
