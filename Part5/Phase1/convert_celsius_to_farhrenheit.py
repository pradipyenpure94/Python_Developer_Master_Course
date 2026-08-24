"""Convert Celsius to Fahrenheit."""

try:
    celsius = float(input("Enter the temperature in celsius: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    fahrenheit = celsius * (9 / 5) + 32
    print(f"Convert Celsius to Fahrenheit: {fahrenheit:.2f}")
