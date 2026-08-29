"""Remove duplicates from a list."""

fruits = ["Kiwi", "apple", "cherry", "apple", "Banana"]
seen = set()
unique_fruits_list = []

for item in fruits:
    if item not in seen:
        seen.add(item)
        unique_fruits_list.append(item)

print(f"Unique fruits item list: {unique_fruits_list}")
