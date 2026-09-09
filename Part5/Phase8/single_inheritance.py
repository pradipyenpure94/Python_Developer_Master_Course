"""Single Inheritance."""


class Parent:
    """Represent a parent."""

    def show_parent(self) -> None:
        """Display parent information."""
        print("Parent class")


class Child(Parent):
    """Represent a child."""

    def show_child(self) -> None:
        """Display child information."""
        print("Child class.")


def main() -> None:
    """Run the main Program."""
    child = Child()
    child.show_child()
    child.show_parent()


if __name__ == "__main__":
    main()
