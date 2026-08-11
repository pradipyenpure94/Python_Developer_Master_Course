"""__getattribute__() method."""


class Student:
    """Represent a Student."""
    def __init__(self, name: str, course: str) -> None:
        self.name = name
        self.course = course

    def __getattribute__(self, attribute_name: str) -> object:
        """Handle the every attribute access."""
        print(f"Accessing attribute: {attribute_name}")
        return object.__getattribute__(self, attribute_name)


def main() -> None:
    """Run the main program."""
    student_obj = Student(name="Pradip", course="Python")
    print(student_obj.name)
    print(student_obj.course)


if __name__ == "__main__":
    main()
