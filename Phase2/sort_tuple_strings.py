"""Sort tuple of strings."""

fruits = ("Banana", "apple", "cherry", "kiwi", "Orange")

# Bubble sort algorithm
fruits_list = list(fruits)

for i in range(len(fruits_list)):
    swapped = False

    for j in range(len(fruits_list) - i - 1):
        if fruits_list[j].casefold() > fruits_list[j + 1].casefold():
            fruits_list[j], fruits_list[j + 1] = (fruits_list[j + 1],
                                                  fruits_list[j])
            swapped = True

    if not swapped:
        break

sorted_tuple = tuple(fruits_list)
print(f"Sorted tuple: {sorted_tuple}")
