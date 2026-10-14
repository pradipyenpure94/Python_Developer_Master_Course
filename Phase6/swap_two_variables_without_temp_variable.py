"""Swapping two variables without temporary variable."""

first_number = 10
second_number = 20

print("Before swapping:")
print(f"First number  : {first_number}")
print(f"Second number : {second_number}")

# Swapping two variables
first_number, second_number = second_number, first_number

print("After swapping: ")
print(f"First number  : {first_number}")
print(f"Second number : {second_number}")
