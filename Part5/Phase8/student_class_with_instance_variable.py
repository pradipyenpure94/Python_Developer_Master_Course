"""Create a Student class with instance variables."""


class Student:
    """Represent a student."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


student_obj = Student(name="Pradip", age=33)
