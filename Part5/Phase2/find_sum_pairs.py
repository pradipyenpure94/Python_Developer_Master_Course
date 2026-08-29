"""Find pairs whose sum equals a target."""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

seen = set()
pairs = set()

for number in numbers:
    complement = target - number
    if complement in seen:
        pairs.add((min(number, complement), max(number, complement)))

    seen.add(number)

print(f"Sum pairs: {pairs}")
