"""Count occurrences of an element."""


numbers = [1, 9, 9, 3]
target = 9
count_occurrences = 0  # How many times element appeared.

for number in numbers:
    if target == number:
        count_occurrences += 1

print(f"Result: {count_occurrences}")
