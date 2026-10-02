"""Import and reuse the functions."""

from company.employee.employee import Employee
from company.finance.salary import calculate_salary, MIN_BASIC_SALARY

employee = Employee(name="Pradip")
print(f"Employee Name              : {employee.name}")
print(f"Employee Min. Basic Salary : {MIN_BASIC_SALARY:.2f}")
print(f"Employee Salary            : {calculate_salary(
    bonus=8600,
    basic_salary=55000
):.2f}")
