"""
Vehicle → Car, Bike, Truck

Create:

    Vehicle
    /     |     \
    Car    Bike   Truck

Implement vehicle-specific methods.
"""


class Vehicle:
    """Represent a vehicle."""

    def __init__(self, name: str) -> None:
        self.name = name


class Car(Vehicle):
    """Represent a car."""

    def display_car_info(self) -> None:
        """Display car information."""
        print(self.name)


class Bike(Vehicle):
    """Represent a bike."""

    def display_bike_info(self) -> None:
        """Display bike information."""
        print(self.name)


class Truck(Vehicle):
    """Represent a truck."""

    def display_truck_info(self) -> None:
        """Display truck information."""
        print(self.name)


def main() -> None:
    """Run the main program."""
    car = Car(name="Car")
    car.display_car_info()

    bike = Bike(name="Bike")
    bike.display_bike_info()

    truck = Truck(name="Truck")
    truck.display_truck_info()


if __name__ == "__main__":
    main()
