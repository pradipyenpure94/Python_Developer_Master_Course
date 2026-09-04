"""Merge two dictionaries."""

person = {"name": "Pradip", "age": 33}
employee = {"emp_id": 1, "name": "Pradip"}

person.update(employee)
print(person)
