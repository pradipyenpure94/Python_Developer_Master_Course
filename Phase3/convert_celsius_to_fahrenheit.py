"""Convert celsius to fahrenheit."""


def celsius_to_fahrenheit(celsius: list[int | float]) -> list[float]:
    """Convert a list of Celsius temperature to Fahrenheit.
    Args:
        celsius (list[int | float]): Input celsius in temperature.
    Returns:
        list[float]: Temperature converted from Celsius to Fahrenheit.
    """
    return list(map(lambda c: c * (9/5) + 32, celsius))


if __name__ == "__main__":
    celsius = [1, 2, 3, 4, 5]
    result = celsius_to_fahrenheit(celsius=celsius)
    print(f"Celsius to Fahrenheit conversion:{result}")
