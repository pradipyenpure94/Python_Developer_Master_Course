"""Convert integer into string."""


try:
    number = int(input("Enter the number: "))
    result = str(number)
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Converted value: {result}")
    print(f"Data type: {type(result).__name__}")
