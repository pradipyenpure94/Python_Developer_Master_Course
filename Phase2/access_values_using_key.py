"""Access values using key."""

students = {"name": "Pradip",
            "age": 33}

name, age = students.get("name"), students.get("age")
print(f"Name: {name}")
print(f"Age: {age}")
