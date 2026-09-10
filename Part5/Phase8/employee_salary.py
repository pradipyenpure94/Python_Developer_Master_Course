"""Implement polymorphic employee salary calculation."""


class Employee:
    """Represent an employee."""

    def calculate_salary(self) -> float:
        """Return the calculated employee salary."""
        return 0.0


class FullTimeEmployee(Employee):
    """Represent a full-time employee."""

    def __init__(self, monthly_salary: float) -> None:
        super().__init__()
        self.monthly_salary = monthly_salary

    def calculate_salary(self) -> float:
        """Return the full-time employee salary."""
        return self.monthly_salary


class PartTimeEmployee(Employee):
    """Represent a part-time employee."""

    def __init__(self, working_hours: int, hourly_rate: float) -> None:
        super().__init__()
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self) -> float:
        """Return the part-time employee salary."""
        return self.working_hours * self.hourly_rate


def main() -> None:
    """Run the main program."""
    employees = [
        FullTimeEmployee(monthly_salary=150000),
        PartTimeEmployee(working_hours=40, hourly_rate=10000)
    ]

    for employee in employees:
        print(employee.calculate_salary())


if __name__ == "__main__":
    main()
