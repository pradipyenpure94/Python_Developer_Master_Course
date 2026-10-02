"""Design and develop functions."""

from numbers import Real

MIN_BASIC_SALARY = 25000.00


def calculate_salary(bonus: Real, basic_salary: Real) -> Real:
    """Return and calculate the employee salary."""

    return bonus + basic_salary
