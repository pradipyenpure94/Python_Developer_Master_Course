"""
Student College

Create a Student class where every student has:

    Instance variables:

    - name
    - age
    - course

    Class variable:

    - college_name
"""


class Student:
    """Represent a student."""
    college_name = "ABC Engineering College"

    def __init__(self, name: str, age: int, course: str) -> None:
        self.name = name
        self.age = age
        self.course = course

    def __str__(self) -> str:
        """Return the student information as string."""
        return (
            f"College Name : {Student.college_name}\n"
            f"Student Name : {self.name}\n"
            f"Age          : {self.age}\n"
            f"Course       : {self.course}"
        )


def main() -> None:
    """Run the main program."""
    student = Student(
        name="Pradip",
        age=33,
        course="Python Developer"
    )
    print("-" * 40)
    print("Student Information:")
    print("-" * 40)
    print(student)
    print("-" * 40)


if __name__ == "__main__":
    main()
