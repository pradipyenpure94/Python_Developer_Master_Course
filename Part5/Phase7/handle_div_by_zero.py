"""Handle division by zero."""

first_number = 10
second_number = 2

try:
    result = first_number / second_number
except ZeroDivisionError as error:
    print(f"Error: {error}")
else:
    print(f"Result: {result}")
