"""
Employee Company

Create an Employee class where all employees share the same company name.
"""


class Employee:
    """Represent an employee."""
    company_name = "IBM"

    def __init__(self, name: str, designation: str) -> None:
        self.name = name
        self.designation = designation

    def display_employee_info(self) -> None:
        """Display the employee information."""
        print("-" * 40)
        print("Employee Information:")
        print("-" * 40)
        print(f"Company      : {Employee.company_name}")
        print(f"Name         : {self.name}")
        print(f"Designation  : {self.designation}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    employee1 = Employee(name="Pradip", designation="Python Developer")
    employee1.display_employee_info()
    employee2 = Employee(name="Amit", designation="Accountant")
    employee2.display_employee_info()


if __name__ == "__main__":
    main()
