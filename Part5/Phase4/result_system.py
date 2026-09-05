"""Create a student result system using functions."""

MIN_MARKS = 0
MAX_MARKS = 100


def student_result(marks: int) -> str:
    """Compute the result of student."""
    if not MIN_MARKS <= marks <= MAX_MARKS:
        raise ValueError(
            f"Student marks must be between {MIN_MARKS} and {MAX_MARKS}."
        )
    if marks >= 35:
        return "Pass"
    return "Fail"


if __name__ == "__main__":
    try:
        marks = int(input("Enter the student marks: "))
        result = student_result(marks=marks)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Student Result: {result}")
