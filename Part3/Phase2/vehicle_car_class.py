"""
Vehicle → Car → ElectricCar

Create:

    Vehicle
    ↓
    Car
    ↓
    ElectricCar

Add appropriate attributes at every level.
"""


class Vehicle:
    """Represent a vehicle."""

    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type = vehicle_type


class Car(Vehicle):
    """Represent a car."""

    def __init__(self, vehicle_type: str, name: str) -> None:
        super().__init__(vehicle_type=vehicle_type)
        self.name = name


class ElectricCar(Car):
    """Represent an electric car."""

    def __init__(self, vehicle_type: str, name: str, speed: int) -> None:
        super().__init__(vehicle_type=vehicle_type, name=name)
        self.speed = speed

    def display_electric_car_information(self) -> None:
        """Display electric car information."""
        print("-" * 40)
        print("Electric Car Information:")
        print("-" * 40)
        print(f"Vehicle type : {self.vehicle_type}")
        print(f"Name         : {self.name}")
        print(f"Speed        : {self.speed}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    electric_car = ElectricCar(
        vehicle_type="Four Wheeler",
        name="Tata Nexon",
        speed=180
    )

    electric_car.display_electric_car_information()


if __name__ == "__main__":
    main()
