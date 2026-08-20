"""
__eq__()

Create an Employee class and compare two employees based on employee ID:

employee1 == employee2
"""


class Employee:
    """Represent an employee."""

    def __init__(self, employee_id: int, name: str) -> None:
        self.employee_id = employee_id
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Employee):
            return NotImplemented
        return self.employee_id == other.employee_id


def main() -> None:
    """Run the main program."""
    employee1 = Employee(employee_id=101, name="Pradip")
    employee2 = Employee(employee_id=102, name="Rahul")
    print(employee1 == employee2)


if __name__ == "__main__":
    main()
