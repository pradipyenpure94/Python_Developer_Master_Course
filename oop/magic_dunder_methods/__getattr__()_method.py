"""__getattr__() method."""


class Student:
    """Represent a Student."""
    def __init__(self, name: str, course: str) -> None:
        self.name = name
        self.course = course

    def __getattr__(self, attribute_name: str) -> str:
        """Handle the attribute that does not exist."""
        return f"{attribute_name} is not available."


def main() -> None:
    """Run the main program."""
    student_obj = Student(name="Pradip", course="Python")
    print(student_obj.name)
    print(student_obj.course)
    print(student_obj.email)


if __name__ == "__main__":
    main()
