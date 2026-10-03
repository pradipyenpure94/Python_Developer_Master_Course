"""Import and reuse function, class, constant, variable."""

from company.employee.employee import Employee


employee = Employee(name="Pradip", basic_salary=86000)

print("Employee Information:")
print(f"Employee Name   : {employee.name}")
print(f"Employee Salary : {employee.salary:.2f}")
print(f"Employee Tax    : {employee.tax:.2f}")
