"""Create Animal with make_sound() and override it."""


class Animal:
    """Represent an animal."""

    def make_sound(self) -> None:
        print("Make sound.")


class Dog(Animal):
    """Represent a dog."""

    def make_sound(self) -> None:
        print("Dog Barking...")


def main() -> None:
    """Run the main program."""
    dog = Dog()
    dog.make_sound()


if __name__ == "__main__":
    main()
