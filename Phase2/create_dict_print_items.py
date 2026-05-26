"""Create dictionary and print items."""

students = {"name": "Pradip",
            "age": 33}

index = 0
item_list = list(students.items())

while index < len(item_list):
    key, value = item_list[index]

    print(f"{key}: {value}")

    index += 1
