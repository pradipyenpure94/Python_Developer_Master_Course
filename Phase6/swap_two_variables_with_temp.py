"""Swap two variables with temporary variable."""

first_number = 10
second_number = 20

print("Before swapping numbers:")
print(f"First number  : {first_number}")
print(f"Second number : {second_number}")

# Swapping variables
temp = first_number
first_number = second_number
second_number = temp

print("After swapping numbers:")
print(f"First number  : {first_number}")
print(f"Second number : {second_number}")
