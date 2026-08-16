"""
Employee Counter

Create an Employee class that maintains the total number of employees using
a class variable.
"""


class Employee:
    """Represent an employee."""
    total_employees = 0

    def __init__(self):
        Employee.total_employees += 1


def main() -> None:
    """Run the main program."""
    employee1 = Employee()
    employee2 = Employee()

    print(f"Total number of employees: {Employee.total_employees}")


if __name__ == "__main__":
    main()
