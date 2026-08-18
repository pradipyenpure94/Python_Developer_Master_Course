"""
Animal → Dog & Cat

Create:

    Animal
    /      \
    Dog      Cat

Implement different behaviors.
"""


class Animal:
    """Represent an animal."""

    def __init__(self, name: str) -> None:
        self.name = name

    def eating(self) -> None:
        """Eating common behaviour."""
        print(f"{self.name} is eating.")


class Dog(Animal):
    """Represent a dog."""

    def bark(self) -> None:
        """Dog sound."""
        print("Dog barking.")


class Cat(Animal):
    """Represent a cat."""

    def meow(self) -> None:
        """Cat sound."""
        print("Cat meowing.")


def main() -> None:
    """Run the main program."""
    dog_obj = Dog(name="Dog")
    dog_obj.bark()
    dog_obj.eating()

    print()
    cat_obj = Cat(name="Cat")
    cat_obj.eating()
    cat_obj.meow()


if __name__ == "__main__":
    main()
