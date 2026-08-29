"""Count occurrences of an element."""


numbers = [1, 9, 9, 3]
target = 9
count_occurrences = 0  # How many times element appeared.
index = 0

while index < len(numbers):
    count_occurrences += 1 if target == numbers[index] else 0
    index += 1
print(f"Result: {count_occurrences}")
