"""__new__() method."""


class Student:
    """Represent a Student."""
    def __new__(cls) -> "Student":
        print("Student __new__() called.")
        return super().__new__(cls)

    def __init__(self):
        """Initialize the object."""
        print("Student __init__() called.")


def main() -> None:
    """Run the main program."""
    student_obj = Student()
    print(student_obj)


if __name__ == "__main__":
    main()
