"""Find union of two sets."""

even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}

# union of two sets
numbers = odd_numbers.copy()

for number in even_numbers:
    numbers.add(number)

print(f"Union of two sets: {numbers}")
