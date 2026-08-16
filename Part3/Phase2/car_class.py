"""
Car Class

Create a Car class with:

    - brand
    - model
    - price
    - speed

    Implement a method to display details.
"""

MIN_CAR_PRICE = 100000


class Car:
    """Represent a car."""

    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        speed: int
    ) -> None:
        if price <= MIN_CAR_PRICE:
            raise ValueError(
                f"Car price must be greater than {MIN_CAR_PRICE}."
            )

        if speed <= 0:
            raise ValueError("Car speed must be greater than zero.")

        self.brand = brand
        self.model = model
        self.price = price
        self.speed = speed

    def display_car_details(self) -> None:
        """Display car information."""
        print("-" * 40)
        print("Car Information:")
        print("-" * 40)
        print(f"\u25A0 Brand  : {self.brand}")
        print(f"\u25A0 Model  : {self.model}")
        print(f"\u25A0 Price  : {self.price:.2f}")
        print(f"\u25A0 Speed  : {self.speed}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    car_object = Car(brand="Honda", model="City", price=250000, speed=180)
    car_object.display_car_details()


if __name__ == "__main__":
    main()
