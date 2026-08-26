"""Convert string input into integers."""


try:
    number = input("Enter the number: ")
    result = int(number)
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Converted Value : {result}")
    print(f"Data type       : {type(result).__name__}")
