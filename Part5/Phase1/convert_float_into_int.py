"""Convert float into integer."""


try:
    number = float(input("Enter the number: "))
    result = int(number)

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Converted value: {result}")
    print(f"Data type: {type(result).__name__}")
