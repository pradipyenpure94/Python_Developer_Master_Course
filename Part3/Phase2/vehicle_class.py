"""
Vehicle → Car

Create:

    Vehicle
    ↓
    Car

Vehicle:
    - brand
    - speed

Car:
    - number_of_doors
"""
MIN_SPEED = 1
MAX_SPEED = 500

MIN_DOORS = 2
MAX_DOORS = 6


def validate_numeric_range(
    value: int,
    minimum: int,
    maximum: int,
    field_name: str
) -> None:
    """
    Validate that a numeric value range
    between minimum and maximum value.
    """
    if not minimum <= value <= maximum:
        raise ValueError(
            f"{field_name} must be between {minimum} and {maximum}."
        )


class Vehicle:
    """Represent a vehicle."""

    def __init__(self, brand: str, speed: int) -> None:
        validate_numeric_range(
            value=speed,
            minimum=MIN_SPEED,
            maximum=MAX_SPEED,
            field_name="Speed"
        )
        self.brand = brand
        self.speed = speed


class Car(Vehicle):
    """Represent a car."""

    def __init__(self, brand: str, speed: int, number_of_doors: int) -> None:
        super().__init__(brand=brand, speed=speed)
        validate_numeric_range(
            value=number_of_doors,
            minimum=MIN_DOORS,
            maximum=MAX_DOORS,
            field_name="Number of doors"
        )
        self.number_of_doors = number_of_doors

    def __str__(self) -> str:
        """Return the formatted car information."""
        return (
            f"Brand         : {self.brand}\n"
            f"Speed         : {self.speed}\n"
            f"No. of doors  : {self.number_of_doors}"
        )


def main() -> None:
    """Run the main program."""
    try:
        car_object = Car(brand="Tata", speed=1, number_of_doors=2)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print("-" * 40)
        print("Car Information:")
        print("-" * 40)
        print(car_object)
        print("-" * 40)


if __name__ == "__main__":
    main()
