"""__ge__() method."""


class Employee:
    """Represent an employee."""
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary >= other.salary


def main() -> None:
    """Run the main program."""
    emp_obj1 = Employee(name="Pradip", salary=125000)
    emp_obj2 = Employee(name="Amit", salary=30000)
    print(emp_obj1 >= emp_obj2)


if __name__ == "__main__":
    main()
