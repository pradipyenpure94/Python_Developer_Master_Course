"""Check key exists or not"""

students = {"name": "Pradip", "age": 33}

key = "name"

if key in students:
    print(f"{key} key found.")
else:
    print(f"{key} key not found.")
