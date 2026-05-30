"""Fahrenheit to celsius in temperature conversion."""


def fahrenheit_celsius_conversion(fahrenheit: float) -> float:
    """
    Convert fahrenheit temperature to celsius.

    Args:
        fahrenheit (float): Fahrenheit in temperature.

    Returns:
        float: Converted fahrenheit temperature in celsius.
    """
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


if __name__ == "__main__":
    try:
        fahrenheit_in_temperature = float(
            input("Enter fahrenheit in temperature: "))

        result = fahrenheit_celsius_conversion(
            fahrenheit=fahrenheit_in_temperature)
        print(f"Celsius in temperature: {result:0.2f}")
    except ValueError:
        print("Invalid input! Please enter a number.")
