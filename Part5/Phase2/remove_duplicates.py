"""Remove duplicates from a list."""

fruits = ["Kiwi", "apple", "cherry", "apple", "Banana", "cherry"]
seen = set()
index = 0

while index < len(fruits):
    if fruits[index] in seen:
        fruits.remove(fruits[index])
    else:
        seen.add(fruits[index])
        index += 1


print(f"Unique fruits list: {fruits}")
