"""Sort tuple of strings."""

fruits = ("Banana", "apple", "cherry", "kiwi", "Orange")

# Insertion sort algorithm
fruits_list = list(fruits)

for i in range(1, len(fruits_list)):
    current = fruits_list[i]
    j = i - 1

    while j >= 0 and fruits_list[j].lower() > current.lower():
        fruits_list[j + 1] = fruits_list[j]
        j -= 1
    fruits_list[j + 1] = current

# Keep back to tuple
sorted_tuple = tuple(fruits_list)
print(f"Sorted tuple: {sorted_tuple}")
