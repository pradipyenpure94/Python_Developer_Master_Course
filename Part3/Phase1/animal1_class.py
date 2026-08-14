"""Animal → Dog, Cat, Cow. (Hierachical inheritance.)"""


class Animal:
    """Represent an animal."""

    def show_animal_info(self) -> None:
        """Show animal information."""
        print("Show animal information.")


class Dog(Animal):
    """Represent a dog."""

    def show_dog_info(self) -> None:
        """Show dog information."""
        print("Show dog information.")


class Cat(Animal):
    """Represent a cat."""

    def show_cat_info(self) -> None:
        """Show cat information."""
        print("Show cat information.")


class Cow(Animal):
    """Represent a cow."""

    def show_cow_info(self) -> None:
        """Show cow information."""
        print("Show cow information.")


def main() -> None:
    """Run the main program."""
    # Child class 1
    cow_obj = Cow()
    cow_obj.show_cow_info()
    cow_obj.show_animal_info()

    # Child class 2
    cat_obj = Cat()
    cat_obj.show_animal_info()
    cat_obj.show_cat_info()

    # Child class 3
    dog_obj = Dog()
    dog_obj.show_animal_info()
    dog_obj.show_dog_info()


if __name__ == "__main__":
    main()
