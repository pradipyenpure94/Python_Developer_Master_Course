"""
Count Student Objects

Create a Student class that automatically
counts how many objects have been created.
"""


class Student:
    """Represent a student."""
    object_count = 0

    def __init__(self) -> None:
        Student.object_count += 1


def main() -> None:
    """Run the main program."""
    student1 = Student()
    student2 = Student()
    student3 = Student()

    print(f"Count class objects: {Student.object_count}")


if __name__ == "__main__":
    main()
