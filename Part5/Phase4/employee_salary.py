"""Create an employee salary calculator using functions."""


def calculate_employee_salary(**salary_components) -> float:
    """Return employee salary."""
    total_salary = sum(salary_components.values())
    return total_salary


if __name__ == "__main__":
    hra = 2500
    ta = 1500
    basic_salary = 16000
    other_allowance = 10000

    result = calculate_employee_salary(
        hra=hra,
        ta=ta,
        basic=basic_salary,
        other=other_allowance
    )
    print(f"Employee Total Salary: {result:.2f}")
