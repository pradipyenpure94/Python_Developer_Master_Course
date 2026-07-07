"""Calculate celsius to fahrenheit."""

MIN_TEMP_LIMIT = -273.15
# As per the business requirement, defined the max Fahrenheit limit.
MAX_FAHRENHEIT_LIMIT = 1000

try:
    celsius = float(input("Enter the temperature in celsius: "))
    if celsius < MIN_TEMP_LIMIT:
        raise ValueError(
            f"Temperature cannot be below absolute zero ({MIN_TEMP_LIMIT} C).")
    # Convert Celsius to Fahrenheit.
    fahrenheit = (celsius * 9 / 5) + 32
    if fahrenheit > MAX_FAHRENHEIT_LIMIT:
        raise ValueError(f"Temperature cannot exceed {MAX_FAHRENHEIT_LIMIT} F.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    print(f"Celsius to Fahrenheit conversion: {fahrenheit:.2f} F")
finally:
    print("Operation completed.")
