"""
Camera + Phone → Smartphone

Create:

    Camera ──┐
            ├── Smartphone
    Phone  ──┘

Implement methods from both parents.
"""


class Camera:
    """Represent a camera."""

    def __init__(self, camera_name: str) -> None:
        self.camera_name = camera_name

    def display_camera_info(self) -> None:
        """Display camera information."""
        print(f"Camera Name     : {self.camera_name}")


class Phone:
    """Represent a phone."""

    def __init__(self, phone_name: str) -> None:
        self.phone_name = phone_name

    def display_phone_info(self) -> None:
        """Display phone information."""
        print(f"Phone Name      : {self.phone_name}")


class Smartphone(Camera, Phone):
    """Represent a smartphone."""

    def __init__(
        self,
        camera_name: str,
        phone_name: str,
        smartphone_name: str
    ) -> None:
        Camera.__init__(self, camera_name=camera_name)
        Phone.__init__(self, phone_name=phone_name)
        self.smartphone_name = smartphone_name

    def display_smartphone_info(self) -> None:
        """Display smartphone information."""
        print(f"Smartphone Name : {self.smartphone_name}")


def main() -> None:
    """Run the main program."""
    smartphone = Smartphone(
        camera_name="Canon",
        phone_name="Mi",
        smartphone_name="Apple"
    )
    print("-" * 40)
    print("Phone Information:")
    print("-" * 40)
    smartphone.display_camera_info()
    smartphone.display_phone_info()
    smartphone.display_smartphone_info()
    print("-" * 40)


if __name__ == "__main__":
    main()
