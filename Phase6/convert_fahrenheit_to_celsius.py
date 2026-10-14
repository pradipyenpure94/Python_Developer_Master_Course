"""Convert Fahrenheit to celsius."""

try:
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))
    celsius = (fahrenheit - 32) * 5 / 9
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print(f"Celsius: {celsius:.2f} C")
