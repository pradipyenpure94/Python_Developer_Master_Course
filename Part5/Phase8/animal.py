"""Create Animal --> Dog"""


class Animal:
    """Represent an animal."""

    def sound(self) -> None:
        """Animal sound."""
        print("Animal sound")


class Dog(Animal):
    """Represent a dog."""

    def sound(self) -> None:
        """Dog sound."""
        super().sound()
        print("Dog barking.")


def main() -> None:
    """Run the main program."""
    dog = Dog()
    dog.sound()


if __name__ == "__main__":
    main()
