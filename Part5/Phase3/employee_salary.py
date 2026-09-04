"""Create employee salary dictionary and find highest paid employee."""

employee = {"Pradip": 156000, "Amit": 30000, "Swanand": 200000}

result = max(employee, key=employee.get)
print(f"Highest Paid Employee: {result}")
