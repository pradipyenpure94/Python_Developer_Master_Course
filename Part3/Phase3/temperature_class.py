"""
Temperature Converter

Create a Temperature class.

Store temperature in Celsius and provide methods to convert it to:

    Fahrenheit
    Kelvin

Also validate that Kelvin cannot be below absolute zero.

Concepts: Class, Object, Constructor, Instance Variables.
"""

ABSOLUTE_ZERO_CELSIUS = -273.15


class Temperature:
    """Represent a temperature."""

    def __init__(self, celsius: float) -> None:
        """Initialize a temperature in Celsius."""
        if not isinstance(celsius, (int, float)):
            raise TypeError("Celsius value must be an int or float.")
        if celsius < ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(
                "Celsius temperature cannot be less than "
                f"{ABSOLUTE_ZERO_CELSIUS}."
            )
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        """Convert Celsius to Fahrenheit."""
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self) -> float:
        """Convert Celsius to Kelvin."""
        return self.celsius - ABSOLUTE_ZERO_CELSIUS


def main() -> None:
    """Run the main program."""
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        temperature = Temperature(celsius=celsius)
        print(f"Celsius      : {temperature.celsius:.2f} C")
        fahrenheit = temperature.to_fahrenheit()
        print(f"Fahrenheit   : {fahrenheit:.2f} F")
        kelvin = temperature.to_kelvin()
        print(f"Kelvin       : {kelvin:.2f} K")

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
