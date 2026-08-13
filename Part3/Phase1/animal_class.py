"""Animal → Mammal → Dog. Multi-level inheritance."""


class Animal:
    """Represent an animal."""
    def display_animal_data(self) -> None:
        """Display animal information."""
        print("Animal - class1")


class Mammal(Animal):
    """Represent a mammal."""
    def display_mammal_data(self) -> None:
        """Display mammal information."""
        print("Mammal - class2")


class Dog(Mammal):
    """Represent a dog."""
    def display_dog_data(self) -> None:
        """Display dog information."""
        print("Dog - class3")


def main() -> None:
    """Run the main program."""
    dog_object = Dog()
    dog_object.display_animal_data()
    dog_object.display_mammal_data()
    dog_object.display_dog_data()


if __name__ == "__main__":
    main()
