"""Merge two dictionaries."""

students1 = {"name": "Pradip", "age": 32}
students2 = {"age": 33, "gender": "Male"}

students = {**students1, **students2}
print(f"Merged dictionary: {students}")
