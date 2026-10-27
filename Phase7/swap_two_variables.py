"""Swap two variables and explain the assignment behavior."""

first_number = 10
second_number = 20
print("Before Swapping:")
print(f"First Number: {first_number}")
print(f"Second Number: {second_number}")
first_number, second_number = second_number, first_number
print("After Swapping:")
print(f"First Number: {first_number}")
print(f"Second Number: {second_number}")
