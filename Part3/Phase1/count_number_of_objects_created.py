"""Count number of objects created."""


class Student:
    """Represent a student."""
    student_count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Student.student_count += 1


def main() -> None:
    """Run the main program."""
    student_object_one = Student(name="Pradip")
    student_object_two = Student(name="Amit")

    print(f"No. of objects created: {Student.student_count}")


if __name__ == "__main__":
    main()
