"""
__init__ dunder / magic method.
Note: Concept unerstand purpose write a program.
"""


class Person:
    """Represent a person."""

    def __init__(self, name: str) -> None:
        self.name = name


class Teacher(Person):
    """Represent a teacher."""
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject

    def display_information(self) -> None:
        """Display information of the teacher."""
        print(f"Person Name     : {self.name}")
        print(f"Teacher subject : {self.subject}")


def main() -> None:
    """Run the main program."""
    teacher_obj = Teacher(name="Pradip", subject="DSA")
    teacher_obj.display_information()


if __name__ == "__main__":
    main()
