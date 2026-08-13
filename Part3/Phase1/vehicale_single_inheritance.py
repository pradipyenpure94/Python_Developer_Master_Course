"""Vehicle → Car. Single inheritance."""


class Vehicle:
    """Represent a vehicle."""
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type = vehicle_type

    def __str__(self) -> str:
        return f"Vehicle Type : {self.vehicle_type}"


class Car(Vehicle):
    """Represent a car."""
    def __init__(self, vehicle_type: str, car_name: str) -> None:
        super().__init__(vehicle_type)
        self.car_name = car_name

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"Car Name     : {self.car_name}"
        )


def main() -> None:
    """Run the main program."""
    print("-" * 40)
    print("Vehicle information:")
    print("-" * 40)
    car_obj = Car(vehicle_type="Four wheeler", car_name="Mercedes")
    print(car_obj)
    print("-" * 40)


if __name__ == "__main__":
    main()
