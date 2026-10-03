"""Design and develop a class."""

from .. finance import tax
from . import salary


EMPLOYEE_BONUS = 5600


class Employee:
    """Represent an employee."""

    def __init__(self, name: str, basic_salary: float) -> None:
        self.name = name
        self.basic_salary = basic_salary
        self.salary = salary.calculate_salary(
            bonus=EMPLOYEE_BONUS,
            basic_salary=basic_salary
        )
        self.tax = tax.calculate_tax(salary=self.salary)
