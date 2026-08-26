"""Convert integer into float."""


try:
    number = int(input("Enter the number: "))
    result = float(number)
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Converted value : {result}")
    print(f"Data type       : {type(result).__name__}")
