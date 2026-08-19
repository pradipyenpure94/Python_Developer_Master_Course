"""
Animal Sound

Create:

    Animal
    ├── Dog
    └── Cat

Parent:

    sound()

Override sound() in both children.
"""


class Animal:
    """Represent an animal."""

    def sound(self) -> None:
        """Make an animal sound."""
        print("Animal sound.")


class Cat(Animal):
    """Represent a cat."""

    def sound(self) -> None:
        """Make a cat sound."""
        print("Cat meows...")


class Dog(Animal):
    """Represent a dog."""

    def sound(self) -> None:
        """Make a dog sound."""
        print("Dog barks...")


def main() -> None:
    """Run the main program."""
    animals = [Animal(), Cat(), Dog()]

    for animal in animals:
        animal.sound()


if __name__ == "__main__":
    main()
