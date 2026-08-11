"""__setattr__() method."""


class Student:
    """Represent a Student."""
    def __init__(self, name: str, course: str) -> None:
        self.name = name
        self.course = course

    def __setattr__(self, name: str, value: object) -> None:
        """Handle attribute assignment."""
        print(f"Setting {name} = {value}")
        object.__setattr__(self, name, value)


def main() -> None:
    """Run the main program."""
    student_obj = Student(name="Pradip", course="Python")
    student_obj.name = "Amit"
    student_obj.course = "DSA"


if __name__ == "__main__":
    main()
