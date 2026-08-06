"""Simple and complete polymorphism example."""


class Animal:
    """Represent a generic animal."""

    def sound(self) -> None:
        """Display the default animal sound."""
        print("Animals make different sounds.")


class Dog(Animal):
    """Represent a dog."""

    def sound(self) -> None:
        """Display the dog sound."""
        print("Dog says: Bark! Bark!")


class Cat(Animal):
    """Represent a cat."""

    def sound(self) -> None:
        """Display the cat sound."""
        print("Cat says: Meow! Meow!")


class Cow(Animal):
    """Represent a cow."""

    def sound(self) -> None:
        """Display the cow sound."""
        print("Cow says: Moo! Moo!")


def main() -> None:
    """Run the Main Program."""
    animals = [
        Animal(),
        Dog(),
        Cat(),
        Cow()
    ]

    print("\nAnimal Sounds:")
    print("-" * 30)
    for animal in animals:
        animal.sound()


if __name__ == "__main__":
    main()
