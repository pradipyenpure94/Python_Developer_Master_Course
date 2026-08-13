"""Single inheritance."""


class Animal:
    """Represent an animal."""

    def display_animal(self) -> None:
        print("Parent class - Animal.")


class Dog(Animal):
    """Represent a dog."""

    def display(self) -> None:
        print("Child class - Dog.")


def main() -> None:
    """Run the main program."""
    dog_obj = Dog()
    dog_obj.display()
    dog_obj.display_animal()


if __name__ == "__main__":
    main()
