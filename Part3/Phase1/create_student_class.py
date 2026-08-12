"""Create a Student class and object."""

#  Define the constants as per the business requirement.

MIN_STUDENT_ID = 1
MIN_NAME_LENGTH = 3
MAX_NAME_LENGTH = 50

MIN_STUDENT_AGE = 3
MAX_STUDENT_AGE = 60

MIN_COURSE_NAME_LENGTH = 2
MAX_COURSE_NAME_LENGTH = 30

ALLOWED_SPECIAL_CHARACTERS = "+#.&-/"

MIN_COLLEGE_NAME_LENGTH = 5
MAX_COLLEGE_NAME_LENGTH = 50


def validate_student_id(student_id: int) -> None:
    """
    Validate the student ID.

    Args:
        student_id (int): Accept student ID input from the user.

    Raises:
        ValueError: If the student ID is less than the minimum allowed value.
    """
    if student_id < MIN_STUDENT_ID:
        raise ValueError(
            f"Student ID must be greater than or equal to {MIN_STUDENT_ID}."
        )


def validate_student_name(name: str) -> None:
    """
    Validate the student name.

    Args:
        name (str): Accept the student name from the user.

    Raises:
        ValueError: The student name is empty, has an invalid length,
        or has invalid characters.
    """
    if not name:
        raise ValueError("Student name is required.")

    if not MIN_NAME_LENGTH <= len(name) <= MAX_NAME_LENGTH:
        raise ValueError(
            "Student name length must be between "
            f"{MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters."
        )

    if not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError(
            "The student name must contain only alphabetic characters and"
            " spaces."
        )


def validate_student_age(age: int) -> None:
    """
    Validate the student age.

    Args:
        age (int): Accept the student age from the user.

    Raises:
        ValueError: If the student age is not between 3 and 60.
    """
    if not MIN_STUDENT_AGE <= age <= MAX_STUDENT_AGE:
        raise ValueError(
            "The student age should be between "
            f"{MIN_STUDENT_AGE} and {MAX_STUDENT_AGE}."
        )


def validate_course_name(course_name: str) -> None:
    """
    Validate the student course name.

    Args:
        course_name (str): Accept the student course name from the user.

    Raises:
        ValueError: The course name is empty, has an invalid length,
        or has invalid characters.
    """
    if not course_name:
        raise ValueError("Course name is required.")

    if not (MIN_COURSE_NAME_LENGTH <= len(course_name)
            <= MAX_COURSE_NAME_LENGTH):
        raise ValueError(
            "The student course name length should be between "
            f"{MIN_COURSE_NAME_LENGTH} and {MAX_COURSE_NAME_LENGTH}."
        )

    if not all(
        char.isalnum()
        or char.isspace()
        or char in ALLOWED_SPECIAL_CHARACTERS
        for char in course_name
    ):
        raise ValueError(
            "Only these special characters are allowed: "
            f"{ALLOWED_SPECIAL_CHARACTERS} in the course name."
        )


def validate_college_name(college_name: str) -> None:
    """
    Validate the college name.

    Args:
        college_name (str): Accept the college name from the user.

    Raises:
        ValueError: The college name is empty or has an invalid length.
    """
    if not college_name:
        raise ValueError("College name is required.")

    if not (MIN_COLLEGE_NAME_LENGTH <= len(college_name)
            <= MAX_COLLEGE_NAME_LENGTH):
        raise ValueError(
            "The college name length should be between "
            f"{MIN_COLLEGE_NAME_LENGTH} and {MAX_COLLEGE_NAME_LENGTH}."
        )


class Student:
    """Represent a student."""
    def __init__(
        self,
        student_id: int,
        name: str,
        age: int,
        course: str,
        college_name: str
    ) -> None:
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.college_name = college_name

    def __str__(self) -> str:
        return (
            f"Student_id       : {self.student_id}\n"
            f"Name             : {self.name}\n"
            f"Age              : {self.age}\n"
            f"Course           : {self.course}\n"
            f"College Name     : {self.college_name}"
        )


def main() -> None:
    """Run the main program."""
    try:
        student_id = int(input("Enter the student ID: "))
        validate_student_id(student_id=student_id)

        name = input("Enter the student name: ").strip()
        validate_student_name(name=name)

        age = int(input("Enter the student age: "))
        validate_student_age(age=age)

        course_name = input("Enter the student course name: ").strip()
        validate_course_name(course_name=course_name)

        college_name = input("Enter the student college name: ").strip()
        validate_college_name(college_name=college_name)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        student_object = Student(
            student_id=student_id,
            name=name,
            age=age,
            course=course_name,
            college_name=college_name
        )

        print("-" * 50)
        print("Student Information:")
        print("-" * 50)
        print(student_object)
        print("-" * 50)


if __name__ == "__main__":
    main()
