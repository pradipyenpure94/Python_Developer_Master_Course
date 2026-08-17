"""
Person → Student

Create:

    Person
    ↓
    Student

Person should contain:

    - name
    - age

Student should contain:
    - course
    - marks
"""


class Person:
    """Represent a person."""
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display_person_info(self) -> None:
        """Display person information."""
        print("-" * 40)
        print("Person Information:")
        print("-" * 40)
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print("-" * 40)


class Student(Person):
    """Represent a student."""
    def __init__(self, name: str, age: int, course: str, marks: float) -> None:
        super().__init__(name=name, age=age)
        self.course = course
        self.marks = marks

    def display_student_info(self) -> None:
        """Display student information."""
        print("-" * 40)
        print("Student Information:")
        print("-" * 40)
        print(f"Course : {self.course}")
        print(f"Marks  : {self.marks:.2f}")
        print("-" * 40)


def main() -> None:
    """Run the main program."""
    student = Student(name="Pradip", age=33, course="Python", marks=96)
    student.display_person_info()
    student.display_student_info()


if __name__ == "__main__":
    main()
