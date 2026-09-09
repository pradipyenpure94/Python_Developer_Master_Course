"""Create Employee with private salary."""


class Employee:
    """Represent an employee."""

    def __init__(self, salary: float) -> None:
        self.__salary = salary
