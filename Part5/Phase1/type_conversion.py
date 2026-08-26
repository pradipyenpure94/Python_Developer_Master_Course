"""Demonstrate implicit and explicit type conversion."""


# Implicit conversion
# Example1:
first_number = 10.5
second_number = 10
addition = first_number + second_number
print(f"Addition: {addition}")


# Explicit conversion
# Example1:
first_number = 10.5
result = int(first_number)
print(f"Result: {result}")
print(f"Data type: {type(result).__name__}")

# Example2:
second_number = 123
result = str(second_number)
print(f"Result: {result}")
print(f"Data type: {type(result).__name__}")
