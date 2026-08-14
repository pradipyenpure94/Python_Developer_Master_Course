"""Animal.speak() with Dog/Cat. (Method Overriding)."""


class Animal:
    """Represent an animal."""

    def speak(self) -> None:
        """Animal make sound."""
        print("Animal make sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self) -> None:
        """Dog make sound."""
        super().speak()
        print("Dog sound: beo")


class Cat(Animal):
    """Represent a cat."""
    def speak(self) -> None:
        """Cat make sound."""
        super().speak()
        print("Cat sound: meow")


def main() -> None:
    """Run the main program."""
    cat_object = Cat()
    cat_object.speak()

    dog_object = Dog()
    dog_object.speak()


if __name__ == "__main__":
    main()
