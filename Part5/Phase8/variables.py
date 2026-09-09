"""Demonstrate difference between instance and class variables."""

# Instance variable


class Student:
    """Represent a student."""

    def __init__(self, name: str) -> None:
        self.name = name  # Belongs to current object


student_obj = Student(name="Pradip")

# Class Variable


class Circle:
    """Represent a circle."""
    pi = 3.14  # Shared with all objects


circle_obj = Circle()
print(circle_obj.pi)
