"""Matrix addition using nested lists."""

x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = []
i = 0

while i < len(x):
    row = []
    j = 0

    while j < len(x[0]):
        row.append(x[i][j] + y[i][j])

        j += 1

    result.append(row)

    i += 1

print(f"Matrix addition: {result}")
