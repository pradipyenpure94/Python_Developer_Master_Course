"""Accept employee name, age and salary."""

name = input("Enter the employee name: ")
age = int(input("Enter the employee age: "))
salary = float(input("Enter the employee salary: "))

print("-" * 25)
print("Employee Information: ")
print("-" * 25)
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Salary : {salary}")
