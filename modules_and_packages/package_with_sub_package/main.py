"""Import and reuse functions."""

from company.employee.employee import Employee
from company.finance.salary import calculate_salary


employee = Employee(name="Pradip")
print(f"Employee Name   : {employee.name}")
salary = calculate_salary(basic_salary=50000, bonus=7500)
print(f"Employee Salary : {salary:.2f}")
