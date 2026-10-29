"""Sort employees by salary using sorted() and a key function."""

employees = [("Pradip", 2500000), ("Amit", 400000), ("Pranjal", 3600000)]

sorted_employees = sorted(employees, key=lambda employee: employee[1])
print(sorted_employees)
