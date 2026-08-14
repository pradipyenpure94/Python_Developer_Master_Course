"""Employee salary calculation. Runtime polymorphism."""


class Employee:
    """Represent an employee."""

    def calculate_salary(self) -> float:
        """Calculate the employee salary."""
        return 0.0


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, allowance: float, basic_salary: float) -> None:
        self.allowance = allowance
        self.basic_salary = basic_salary

    def calculate_salary(self) -> float:
        """Calculate the manager salary."""
        return self.basic_salary + self.allowance


class Developer(Employee):
    """Represent a developer."""

    def __init__(self, basic_salary: float, bonus: float) -> None:
        self.bonus = bonus
        self.basic_salary = basic_salary

    def calculate_salary(self) -> float:
        """Calculate the developer salary."""
        return self.basic_salary + self.bonus


def main() -> None:
    """Run the main program."""
    developer_obj = Developer(basic_salary=50000, bonus=25000)
    print(f"Developer salary: {developer_obj.calculate_salary()}")
    manager_obj = Manager(basic_salary=78000, allowance=96000)
    print(f"Manager salary: {manager_obj.calculate_salary()}")


if __name__ == "__main__":
    main()
