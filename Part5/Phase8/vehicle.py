"""Create Vehicle ---> Car."""


class Vehicle:
    """Represent a vehicle."""

    def show_vehicle(self) -> None:
        """Display vehicle behaviour."""
        print("Vehicle is moving.")


class Car(Vehicle):
    """Represent a car."""

    def show_car(self) -> None:
        """Display car-specific behaviour."""
        print("Car is driving.")


def main() -> None:
    """Run the main program."""
    car = Car()
    car.show_car()
    car.show_vehicle()


if __name__ == "__main__":
    main()
