"""Create a Student class with common college name."""


class Student:
    """Represent a student."""
    college_name = "MIT College, Pune"

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return (
            f"College Name: {self.college_name}\n"
            f"Student Name: {self.name}"
        )


def main() -> None:
    """Run the main program."""
    student_object = Student(name="Pradip")
    print(student_object)


if __name__ == "__main__":
    main()
