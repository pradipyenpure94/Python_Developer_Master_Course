"""Sort tuple of strings."""

fruits = ("Banana", "apple", "cherry", "kiwi", "Orange")

# Selection sort algorithm
fruits_list = list(fruits)

for i, _ in enumerate(fruits_list):
    min_index = i

    for j in range(i + 1, len(fruits_list)):
        if fruits_list[j].casefold() < fruits_list[min_index].casefold():
            min_index = j

    if i != min_index:
        fruits_list[i], fruits_list[min_index] = (fruits_list[min_index],
                                                  fruits_list[i])


sorted_tuple = tuple(fruits_list)
print(f"Sorted tuple: {sorted_tuple}")
