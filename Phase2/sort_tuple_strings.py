"""Sort tuple of strings."""

fruits = ("Banana", "apple", "cherry", "kiwi", "Orange")

sorted_tuple = tuple(sorted(fruits, key=str.lower))
print(f"Sorted tuple: {sorted_tuple}")
