"""Find the square and cube of a number."""

try:
    number = int(input("Enter the number: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    square_number = number ** 2
    print(f"Square Number : {square_number}")
    cube_number = number ** 3
    print(f"Cube Number   : {cube_number}")
