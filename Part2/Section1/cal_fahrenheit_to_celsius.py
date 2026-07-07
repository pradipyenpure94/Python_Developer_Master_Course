"""Convert Fahrenheit to Celsius."""

# As per the business requirement,
# defined max. Fahrenheit and min. Celsius limit.
MAX_FAHRENHEIT_LIMIT = 1000
MIN_CELSIUS_LIMIT = -273.15

try:
    fahrenheit = float(
        input("Enter the temperature in Fahrenheit: "))

    if fahrenheit > MAX_FAHRENHEIT_LIMIT:
        raise ValueError(
            f"Fahrenheit temperature cannot exceed {MAX_FAHRENHEIT_LIMIT} F.")

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5 / 9

    if celsius < MIN_CELSIUS_LIMIT:
        raise ValueError(
            f"Celsius temperature cannot be below {MIN_CELSIUS_LIMIT} C.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    print(f"Fahrenheit to Celsius: {celsius:.2f} C")
finally:
    print("Operation completed.")
