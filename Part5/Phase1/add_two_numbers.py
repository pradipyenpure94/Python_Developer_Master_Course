"""Add two numbers."""

try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Addition: {first_number + second_number}")
