"""Sort a list without sort()."""

alphabets = ["A", "a", "b", "c", "E", "B", "F", "D", "d"]

n = len(alphabets)

for i in range(n):
    for j in range(n - 1 - i):
        if alphabets[j] > alphabets[j + 1]:
            alphabets[j], alphabets[j + 1] = alphabets[j + 1], alphabets[j]

print(f"Alphabets: {alphabets}")
