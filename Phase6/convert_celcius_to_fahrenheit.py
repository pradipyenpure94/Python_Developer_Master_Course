"""Convert celsius to Fahrenheit."""

try:
    temperature = float(input("Enter the temperature in celsius: "))
    fahrenheit = temperature * 9/5 + 32
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Fahrenheit: {fahrenheit:.2f} F")
