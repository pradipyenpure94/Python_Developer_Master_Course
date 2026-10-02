"""Design and develop custom functions."""

from numbers import Real
from .. import constants


def calculate_salary(bonus: Real, basic_salary: float) -> Real:
    """Return and calculate the salary."""

    return constants.BONUS + basic_salary
