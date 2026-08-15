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

    def display(self) -> None:
        """Display the student information."""
        print("-" * 40)
        print("Student information:")
        print("-" * 40)
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")
        print("-" * 40)


student1 = Student(name="Pradip", age=33, course="Python")
student2 = Student(name="Amit", age=30, course="Tally")
student3 = Student(name="Pranjal", age=23, course="Oracle")

students = [student1, student2, student3]

for student in students:
    student.display()
