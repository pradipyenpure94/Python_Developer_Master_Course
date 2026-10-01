"""Import and reuse the class, variable and function."""

from employee import Employee


employee = Employee(name="Pradip", salary=150000.12)

print(f"Employee company name : {Employee.company_name}")
employee.display()
