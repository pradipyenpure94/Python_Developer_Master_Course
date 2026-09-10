"""Override a parent class method."""


class Parent:
    """Represent a parent."""

    def show(self) -> None:
        print("Parent class.")


class Child(Parent):
    """Represent a child."""

    def show(self) -> None:
        print("Child class.")


def main() -> None:
    """Run the main program."""
    child = Child()
    child.show()


if __name__ == "__main__":
    main()
