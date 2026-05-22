"""Find pairs with given sum."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 1]
target = 3

seen = set()
pairs = set()

for number in numbers:
    diff = target - number
    if diff in seen:
        pair = tuple(sorted((diff, number)))
        pairs.add(pair)
    seen.add(number)

print(f"Sum pairs: {pairs}")
