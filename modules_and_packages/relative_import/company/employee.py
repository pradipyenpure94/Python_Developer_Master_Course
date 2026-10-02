"""Design and develop custom class."""

from . salary import calculate_salary


class Employee:
    """Represent an employee."""

    def __init__(
        self,
        name: str,
        bonus: float,
        basic_salary: float,
    ) -> None:
        self.name = name
        self.bonus = bonus
        self.basic_salary = basic_salary
        self.salary = calculate_salary(
            bonus=self.get_bonus(),
            basic_salary=self.get_basic_salary()
        )

    def get_bonus(self) -> float:
        return self.bonus

    def get_basic_salary(self) -> float:
        return self.basic_salary
