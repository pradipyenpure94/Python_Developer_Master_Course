"""Father + Mother → Child."""


class Father:
    """Represent a father."""

    def show_father(self) -> None:
        """Father information."""
        print("Show father information.")


class Mother:
    """represent a mother."""

    def show_mother(self) -> None:
        """Mother information."""
        print("Show mother information.")


class Child(Father, Mother):
    """Represent a child."""

    def show_child(self) -> None:
        """Child information."""
        print("Show child information.")


def main() -> None:
    """Run the main program."""
    child_object = Child()
    child_object.show_child()
    child_object.show_father()
    child_object.show_mother()


if __name__ == "__main__":
    main()
