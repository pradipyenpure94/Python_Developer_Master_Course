"""Convert Celsius to Fahrenheit and Fahrenheit to Celsius."""

try:
    # Accept input from user.
    celsius = float(input("Enter the temperature in celsius: "))
    fahrenheit = float(input("Enter the temperature in fahrenheit: "))
except ValueError as error:
    print(f"Error: {error}")
else:
    convert_to_fahrenheit = celsius * (9 / 5) + 32
    convert_to_celsius = (fahrenheit - 32) * (5 / 9)
    print(f"Fahrenheit: {convert_to_fahrenheit:.2f} F")
    print(f"Celsius: {convert_to_celsius:.2f} C")
