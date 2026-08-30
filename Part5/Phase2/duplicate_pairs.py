numbers = [9, 7, 6, 4, 8, 3, 7, 9, 3, 9]

duplicate_pairs = []

n = len(numbers)

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            duplicate_pairs.append((numbers[i], numbers[j]))

print(f"Duplicate pairs: {duplicate_pairs}")
