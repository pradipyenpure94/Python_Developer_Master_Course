"""Vehicle.start() with Car/Bike. (Method Overriding)."""


class Vehicle:
    """Represent a vehicle."""

    def start(self) -> None:
        """Vehicle start() method."""
        print("Start a vehicle.")


class Car(Vehicle):
    """Represent a car."""

    def start(self) -> None:
        """Car start() method."""
        super().start()
        print("Start a car.")


class Bike(Vehicle):
    """Represent a bike."""

    def start(self) -> None:
        """Bike start() method."""
        super().start()
        print("Start a bike.")


def main() -> None:
    """Run the main program."""
    car_object = Car()
    car_object.start()
    bike_object = Bike()
    bike_object.start()


if __name__ == "__main__":
    main()
