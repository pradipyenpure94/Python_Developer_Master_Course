"""Celsius to farehenit conversion."""


def celsius_to_fahrenheit_conversion(celsius: float) -> float:
    """
    Convert celsius temperature to fahrenheit.

    Args:
        celsius (float): Temperature in celsius.

    Returns:
        float: Converted to celsius temperature in Fahrenheit
    """
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


if __name__ == "__main__":
    try:
        temperature_in_celsius = float(input("Enter celsius: "))
        result = celsius_to_fahrenheit_conversion(
            celsius=temperature_in_celsius)
        print(f"Fahrenheit: {result:0.2f}")
    except ValueError:
        print("Invalid input! Please enter a number.")
