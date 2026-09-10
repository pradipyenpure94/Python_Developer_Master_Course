"""Create Father + Mother ----> Child."""


class Father:
    """Represent a father."""

    def __init__(self, father_name: str) -> None:
        self.father_name = father_name

    def show_father_name(self) -> None:
        """Display father name."""
        print(f"Father Name   : {self.father_name}")


class Mother:
    """Represent a mother."""

    def __init__(self, mother_name: str) -> None:
        self.mother_name = mother_name

    def show_mother_name(self) -> None:
        """Display mother name."""
        print(f"Mother Name   : {self.mother_name}")


class Child(Father, Mother):
    """Represent a child."""

    def __init__(self, father_name: str, mother_name: str, name: str) -> None:
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name

    def show_child_name(self) -> None:
        """Display the child name."""
        print(f"Child Name    : {self.name}")


def main() -> None:
    """Run the main program."""
    child = Child(father_name="Rajendra", mother_name="Surekha", name="Pradip")
    child.show_child_name()
    child.show_father_name()
    child.show_mother_name()


if __name__ == "__main__":
    main()
