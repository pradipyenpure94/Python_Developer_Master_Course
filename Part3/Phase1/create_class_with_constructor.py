"""Create an Employee class with constructor."""


class Employee:
    """Represent an employee."""

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Employee name: {self.name}"


def main() -> None:
    """Run the main program."""
    employee_object = Employee(name="Pradip")
    print(employee_object)


if __name__ == "__main__":
    main()
