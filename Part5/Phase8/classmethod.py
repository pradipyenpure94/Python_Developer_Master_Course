"""
Implement the super(), classmethod,
and staticmethod in a business-oriented class.
"""


class Employee:
    """Represent an employee."""

    company_name = "IBM"
    total_employee = 0

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        Employee.total_employee += 1

    @classmethod
    def from_string(cls, employee_data: str) -> "Employee":
        """Create an employee from comma-separated string."""
        name, salary = employee_data.split(",")
        return cls(name.strip(), float(salary))

    @classmethod
    def get_total_employee(cls) -> int:
        """Return the total number of employess."""
        return cls.total_employee

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        """Check whether a salary is valid."""
        return salary > 0


class Developer(Employee):
    """Represent a developer."""

    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_details(self) -> None:
        """Display developer details."""
        print(f"Name                 : {self.name}")
        print(f"Salary               : {self.salary}")
        print(f"Programming Language : {self.programming_language}")
        print(f"Company Name         : {self.company_name}")


def main() -> None:
    """Run the main program."""

    # Using Staticmethod
    print(Employee.is_valid_salary(50000))

    # Creating developer object
    developer = Developer(
        name="Pradip",
        salary=50000,
        programming_language="Python"
    )

    developer.display_details()

    # Using classmethod as an alternative constructor
    employee = Employee.from_string("Pradip, 56000")

    print("Employee created from string: ")
    print(f"Name            : {employee.name}")
    print(f"Salary          : {employee.salary:.2f}")

    # Using classmethod
    print(f"Total Employees : {Employee.get_total_employee()}")


if __name__ == "__main__":
    main()
