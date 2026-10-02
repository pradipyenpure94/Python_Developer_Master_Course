"""Import and reuse the functions."""

from company.employee import Employee


employee = Employee(name="Pradip", bonus=5600, basic_salary=89000)

print(f"Employee Name   : {employee.name}")
print(f"Employee Salary : {employee.salary:.2f}")
