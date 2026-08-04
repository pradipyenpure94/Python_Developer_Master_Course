"""Create student class and object."""

MIN_ROLL_NO = 1
MAX_NAME_LENGTH = 50


def validate_student_roll_no(roll_no: int) -> None:
    """Validate the student roll no."""
    if roll_no < MIN_ROLL_NO:
        raise ValueError(f"Roll number must be at least {MIN_ROLL_NO}.")


def validate_student_name(name: str) -> None:
    """Validate the student's name"""
    if not name:
        raise ValueError("Name cannot be empty.")

    if len(name) > MAX_NAME_LENGTH:
        raise ValueError("Name is too long.")

    if not name.replace(" ", "").isalpha():
        raise ValueError("Name must contain only alphabetic characters.")


class Student:
    """Create student class and object"""
    def __init__(self, roll_no: int, name: str) -> None:
        validate_student_roll_no(roll_no=roll_no)
        validate_student_name(name=name)

        self.roll_no = roll_no
        self.name = name

    def __str__(self) -> str:
        return f"Roll No: {self.roll_no}\nName: {self.name}"


def main() -> None:
    """Run the main Program."""
    try:
        roll_no = int(input("Enter the student roll no.: "))
        name = input("Enter the student name: ").strip()
        student_obj = Student(roll_no=roll_no, name=name)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(student_obj)


if __name__ == "__main__":
    main()
