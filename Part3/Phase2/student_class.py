"""
Student Class

Create a Student class with:
    - name
    - age
    - course

Create 3 student objects and display their details.
"""


class Student:
    """Represent a student."""

    def __init__(self, name: str, age: int, course: str) -> None:
        self.name = name
        self.age = age
        self.course = course

    def __str__(self) -> str:
        """Return the student information."""
        return (
            f"Name    : {self.name}\n"
            f"Age     : {self.age}\n"
            f"Course  : {self.course}\n"
        )


student1 = Student(name="Pradip", age=33, course="Python")
student2 = Student(name="Amit", age=30, course="Tally")
student3 = Student(name="Pranjal", age=23, course="Oracle")

students = [student1, student2, student3]

for student in students:
    print("-" * 40)
    print("Student information:")
    print("-" * 40)
    print(student)
