"""
Employee Salary

Create:

    Employee
    ↓
    Manager

Override salary calculation in Manager.
"""


class Employee:
    """Represent an employee."""

    def __init__(self, salary: float) -> None:
        self.salary = salary

    def calculate_salary(self) -> float:
        """Return the employee salary."""
        return self.salary


class Manager(Employee):
    """Represent a manager."""

    def __init__(self, salary: float, bonus: float) -> None:
        super().__init__(salary=salary)
        self.bonus = bonus

    def calculate_bonus(self) -> float:
        """Return the manager bonus."""
        return self.salary * self.bonus / 100

    def calculate_salary(self) -> float:
        """Return the salary of manager with bonus."""
        return self.salary + self.calculate_bonus()


def main() -> None:
    """Run the main program."""
    employees = [Employee(salary=150000), Manager(salary=150000, bonus=10)]

    for employee in employees:
        salary = employee.calculate_salary()
        print(f"Salary: {salary:.2f}")


if __name__ == "__main__":
    main()
