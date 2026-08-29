"""Remove duplicates from a list."""

fruits = ["Kiwi", "apple", "cherry", "apple", "Banana"]
seen = set()
unique_fruits_list = [
    item for item in fruits if not (item in seen or seen.add(item))
]

print(f"Unique fruits item list: {unique_fruits_list}")
