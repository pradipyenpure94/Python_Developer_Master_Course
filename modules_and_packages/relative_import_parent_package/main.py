"""Import and reused the functions."""

from company.finance.salary import calculate_salary


print(f"Employee Salary: {calculate_salary(
    bonus=4500,
    basic_salary=89630
):.2f}")
