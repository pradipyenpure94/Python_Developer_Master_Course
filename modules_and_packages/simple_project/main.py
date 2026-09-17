"""Arithmetic operations."""

from modules_and_packages.simple_project.calculator import add, sub


result = add(first_number=10, second_number=20)
print(f"Addition    : {result:.2f}")

result = sub(first_number=20, second_number=2)
print(f"Subtraction : {result:.2f}")
