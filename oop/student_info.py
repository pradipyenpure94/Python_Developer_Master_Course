"""Student information."""

MAX_NAME_LENGTH = 50
MIN_ROLL_NO = 1


def validate_roll_no(roll_no: int) -> None:
    """Validate the roll number."""
    if roll_no < MIN_ROLL_NO:
        raise ValueError(f"Roll number must be at least {MIN_ROLL_NO}.")


def validate_name(value: str, field_name: str) -> None:
    """Validate the name."""
    if not value:
        raise ValueError(f"{field_name} name cannot be empty.")
    if len(value) > MAX_NAME_LENGTH:
        raise ValueError(
            f"The {field_name.lower()} name can contain "
            f"a maximum of {MAX_NAME_LENGTH} characters."
        )
    if not all(char.isalpha() or char.isspace() for char in value):
        raise ValueError(
            f"{field_name} name must contain only alphabetic characters "
            "and spaces."
        )


class Student:
    """Student information."""
    COLLEGE_NAME = "MIT College"

    def __init__(self, roll_no: int, name: str) -> None:
        self.roll_no = roll_no
        self.name = name

    def __str__(self) -> str:
        """The student information."""
        return (
            f"\n{'-' * 40}\n"
            f"Student Information: \n{'-' * 40}\n"
            f"College Name  : {Student.COLLEGE_NAME}\n"
            f"Roll No.      : {self.roll_no}\n"
            f"Name          : {self.name}\n"
            f"{'-' * 40}"
        )


def main() -> None:
    """Run the Main Program."""
    try:
        roll_no = int(input("Enter the Roll No.: "))
        validate_roll_no(roll_no=roll_no)
        name = input("Enter the name: ").strip()
        validate_name(value=name, field_name="Student")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        student_obj = Student(roll_no=roll_no, name=name)
        print(student_obj)


if __name__ == "__main__":
    main()
