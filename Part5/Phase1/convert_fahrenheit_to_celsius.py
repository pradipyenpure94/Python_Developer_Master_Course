"""Convert Fahrenheit to Celsius."""


try:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    celsius_temperature = (fahrenheit - 32) * (5 / 9)
    print(f"Convert Fahrenheit to Celsius: {celsius_temperature:.2f} C")
