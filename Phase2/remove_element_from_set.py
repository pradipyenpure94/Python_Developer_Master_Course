"""Remove element from set."""

numbers = {1, 2, 3, 4, 5}

if 5 in numbers:
    numbers.remove(5)
    print(f"After remove: {numbers}")
else:
    print("Element not found.")
