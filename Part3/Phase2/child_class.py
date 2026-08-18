"""
Father + Mother → Child

Create:

    Father ──┐
            ├── Child
    Mother ──┘

Demonstrate multiple inheritance.
"""


class Father:
    """Represent a father."""

    def __init__(self, father_name: str) -> None:
        self.father_name = father_name

    def father_info(self) -> None:
        """Display father information."""
        print(f"Father Name: {self.father_name}")


class Mother:
    """Represent a mother."""

    def __init__(self, mother_name: str) -> None:
        self.mother_name = mother_name

    def mother_info(self) -> None:
        """Display mother information."""
        print(f"Mother Name: {self.mother_name}")


class Child(Father, Mother):
    """Represent a child."""

    def __init__(
        self,
        father_name: str,
        mother_name: str,
        child_name: str
    ) -> None:
        Father.__init__(self, father_name=father_name)
        Mother.__init__(self, mother_name=mother_name)
        self.child_name = child_name

    def display_child_information(self) -> None:
        """Display child information."""
        print("-" * 40)
        print("Child information:")
        print("-" * 40)
        print(f"Child Name  : {self.child_name}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    child_object = Child(
        child_name="Pradip",
        father_name="Rajendra",
        mother_name="Surekha"
    )
    child_object.display_child_information()
    child_object.father_info()
    child_object.mother_info()


if __name__ == "__main__":
    main()
