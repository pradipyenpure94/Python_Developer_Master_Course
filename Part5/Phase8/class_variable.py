"""Create College class variable shared by all students."""


class College:
    """Represent a college."""
    college_name = "MIT"

    def __init__(self, location: str) -> None:
        self.location = location


# Object1
college_object1 = College(location="Kothrud")
print(college_object1.college_name)
print(college_object1.location)
# Object2
college_object2 = College(location="Loni")
print(college_object2.college_name)
print(college_object2.location)
