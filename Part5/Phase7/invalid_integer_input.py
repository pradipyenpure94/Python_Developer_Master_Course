"""Handle invalid integer input."""

try:
    number = int(input("Enter the number: "))
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Input number: {number}")
