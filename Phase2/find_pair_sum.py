"""Find pairs with given sum."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 1]
target = 3

seen = set()
pairs = set()
index = 0

while index < len(numbers):

    current_number = numbers[index]
    diff = target - current_number

    if diff in seen:
        pair = tuple(sorted((diff, current_number)))
        pairs.add(pair)

    seen.add(current_number)

    index += 1

print(f"Sum pairs: {pairs}")
