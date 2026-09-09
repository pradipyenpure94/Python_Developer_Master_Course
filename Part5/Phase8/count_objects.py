"""Count number of objects created using a class variable."""


class Employee:
    """Represent an employee."""
    count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Employee.count += 1


emp_obj1 = Employee(name="Pradip")
emp_obj2 = Employee(name="Sandeep")
emp_obj3 = Employee(name="Ajay")

print(f"No. of objects: {Employee.count}")
