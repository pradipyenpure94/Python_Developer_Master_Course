"""Find triplets whose sum equals a target."""

numbers = [9, 7, 6, 4, 8, 3, 7, 9, 3, 9]
target = 18

triplets = set()
n = len(numbers)

for i in range(n - 2):

    seen = set()

    for j in range(i + 1, n):

        complement = target - numbers[i] - numbers[j]

        if complement in seen:

            triplet = tuple(sorted((numbers[i], numbers[j], complement)))

            triplets.add(triplet)

        seen.add(numbers[j])

print(f"Triplets with sum: {triplets}")
