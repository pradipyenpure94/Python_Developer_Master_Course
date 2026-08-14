"""Vehicle -> Car -> ElectricCar.  Multilevel."""


class Vehicle:
    """Represent a vehicle."""
    def show_vehicle(self) -> None:
        """Show vehicle information."""
        print("Show vehicle.")


class Car(Vehicle):
    """Represent a car."""
    def show_car(self) -> None:
        """Show car information."""
        print("Show car.")


class ElectricCar(Car):
    """Represent an electric car."""
    def show_electric_car(self) -> None:
        """Show electric car information."""
        print("Show Electric Car.")


def main() -> None:
    """Run the main program."""
    electric_car_object = ElectricCar()
    electric_car_object.show_vehicle()
    electric_car_object.show_car()
    electric_car_object.show_electric_car()


if __name__ == "__main__":
    main()
